# Database Schema

**Project:** Food Tracker MVP
**Status:** Draft — pre-implementation
**Last Updated:** 2026-07-15

---

# 1. Overview

This document defines the initial relational schema for the Food Tracker MVP, derived from EPRD.md's functional requirements. It is intentionally scoped to MVP needs only — see EPRD.md Section 3 (Non-Goals) for explicitly deferred features (social, weight tracking, meal planning, etc.), which this schema does not accommodate.

Database: PostgreSQL via Supabase.
Access pattern: backend-only (FastAPI). Mobile client never queries the database directly (see HANDOFF.md, API-first development principle).

---

# 2. Row-Level Security (RLS) Policy

RLS is applied **per-table**, not uniformly, based on whether the table contains user-specific data or shared reference data:

| Table | RLS Scope | Reason |
|---|---|---|
| users | Row = self only | User can only read/edit own account |
| foods | user_id-scoped | Personal food library, private per EPRD Security NFR |
| diary_entries | user_id-scoped | Personal logs |
| ocr_scans | user_id-scoped | Personal scan history, may contain personal photos |
| barcode_cache | **No RLS — global, read-only for all authenticated users** | Reference data (OpenFoodFacts product info), not user-specific. No confidentiality boundary exists. |
| barcode_scan_log | user_id-scoped | Audit trail is per-user by definition |

**Write access to `barcode_cache` is backend-only.** No client (mobile or otherwise) writes to this table directly; only the `/barcode` endpoint's server-side logic writes after validating the external API response. This prevents cache poisoning by a malicious or malfunctioning client.

---

# 3. Tables

## 3.1 `users`

| Column | Type | Notes |
|---|---|---|
| id | uuid, pk | |
| email | text, unique | |
| password_hash | text | |
| created_at | timestamptz | default now() |

---

## 3.2 `foods`

Personal food library entry. Source of truth for FR-100–FR-104.

| Column | Type | Notes |
|---|---|---|
| id | uuid, pk | |
| user_id | uuid, fk → users.id | RLS boundary |
| name | text | |
| brand | text, nullable | |
| barcode | text, nullable, indexed | Links back to barcode_cache.barcode, not enforced fk (external data may not exist yet) |
| serving_size | text | e.g. "100g", "1 cup" |
| calories | numeric | |
| protein | numeric | grams |
| carbs | numeric | grams |
| fat | numeric | grams |
| is_favorite | boolean | default false — FR-104 |
| source | enum(manual, barcode, ocr) | Provenance of the entry |
| created_at | timestamptz | |
| updated_at | timestamptz | |

---

## 3.3 `diary_entries`

Meal log entries. FR-400–FR-404.

| Column | Type | Notes |
|---|---|---|
| id | uuid, pk | |
| user_id | uuid, fk → users.id | RLS boundary |
| food_id | uuid, fk → foods.id | |
| meal | enum(breakfast, lunch, dinner, snack) | FR-401 |
| date | date | |
| quantity | numeric | Multiplier applied to food's serving_size — FR-402 |
| created_at | timestamptz | |

Daily macro totals (FR-404, FR-500) are computed, not stored — sum `foods.calories * diary_entries.quantity` (and same for protein/carbs/fat) grouped by user_id + date.

---

## 3.4 `ocr_scans`

Nutrition label scan history. FR-300–FR-303.

| Column | Type | Notes |
|---|---|---|
| id | uuid, pk | |
| user_id | uuid, fk → users.id | RLS boundary |
| image_url | text | Supabase Storage reference |
| raw_extracted_json | jsonb | Full OCR output before user correction |
| confidence_score | numeric | FR-303 |
| confirmed | boolean | default false — FR-302, whether user accepted the OCR result into their food library |
| resulting_food_id | uuid, fk → foods.id, nullable | Set once confirmed |
| created_at | timestamptz | |

---

## 3.5 `barcode_cache`

**Global, shared across all users.** Not scoped to any single user — represents cached OpenFoodFacts lookups. FR-200–FR-203.

| Column | Type | Notes |
|---|---|---|
| barcode | text, pk | |
| food_data_json | jsonb | Normalized OpenFoodFacts response |
| last_fetched_at | timestamptz | Used for future staleness/re-fetch policy (not implemented in MVP — see Section 5) |

---

## 3.6 `barcode_scan_log`

**Per-user audit trail**, separate from the cache itself. Not required by any EPRD FR directly, but added to preserve visibility into who scanned what, since the cache itself has no per-user trace. (this table is an engineering addition beyond spec)

| Column | Type | Notes |
|---|---|---|
| id | uuid, pk | |
| user_id | uuid, fk → users.id | RLS boundary |
| barcode | text, fk → barcode_cache.barcode | Not enforced if barcode wasn't found (log the attempt anyway) |
| found_in_cache | boolean | Whether this hit the local cache (FR-201) or required an external lookup (FR-202) |
| scanned_at | timestamptz | |

---

# 4. Entity Relationships

```
users
  └─< foods
  └─< diary_entries >─ foods
  └─< ocr_scans >─ foods (resulting_food_id, nullable)
  └─< barcode_scan_log >─ barcode_cache (barcode, loosely linked)

barcode_cache (global, no user_id)
```

---

# 5. Deferred Decisions

Flagged here so they aren't lost, per project convention of not silently dropping open questions:

- **Cache staleness policy for `barcode_cache`:** no re-fetch/expiry logic in MVP. `last_fetched_at` is stored so a policy (e.g., re-fetch if > 90 days old) can be added later without a schema change.
- **`barcode_scan_log` retention:** no pruning strategy defined yet. Fine for MVP volume; revisit if this table grows unbounded.
- **Enums as Postgres types vs. string constraints:** implementation detail left to Alembic migration authoring in Step 3 — not a schema-shape decision, just an enforcement mechanism choice.
