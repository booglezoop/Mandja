# Engineering Product Requirements Document (EPRD)

**Project:** Food Tracker MVP  
**Version:** 1.0  
**Status:** Draft  
**Author:** Iliyan Donev  
**Last Updated:** YYYY-MM-DD

---

# 1. Overview

## Purpose

Build a cross-platform mobile application that enables users to quickly track macronutrients by maintaining a personal food library.

The application prioritizes rapid food logging through reusable foods, barcode scanning, and nutrition label OCR.

This project is intended as both a personal productivity tool and a software engineering portfolio project.

---

# 2. Goals

## Primary Goals

- Build a production-quality mobile application.
- Maintain a personal food database.
- Reduce repetitive food entry.
- Track daily calories and macronutrients.
- Support barcode and nutrition label ingestion.

## Success Criteria

- Food can be logged in under 15 seconds.
- OCR successfully extracts nutrition labels requiring minimal correction.
- Barcode scanning retrieves food information when available.
- Daily macro calculations are accurate.

---

# 3. Non-Goals

The following features are explicitly out of scope for the MVP:

- Social features
- Friends
- Public food database
- Community food sharing
- Weight tracking
- AI nutrition coaching
- Meal planning
- Grocery lists
- Micronutrient tracking
- Apple Health integration
- Google Fit integration
- Wearable support
- Recipe parsing
- Food image calorie estimation
- Subscription/payment functionality

---

# 4. User Roles

## User

A single authenticated user capable of:

- Managing foods
- Logging meals
- Viewing daily macro totals
- Scanning nutrition labels
- Scanning barcodes

No additional roles exist.

---

# 5. Functional Requirements

## Authentication

### FR-001

Users shall be able to register using email and password.

### FR-002

Users shall be able to log in.

### FR-003

Users shall remain authenticated across sessions.

---

## Food Library

### FR-100

Users shall be able to manually create foods.

### FR-101

Users shall edit foods.

### FR-102

Users shall delete foods.

### FR-103

Users shall search foods.

### FR-104

Users shall mark foods as favorites.

---

## Barcode

### FR-200

Users shall scan product barcodes.

### FR-201

The backend shall search the local database first.

### FR-202

If unavailable locally, the backend shall query an external food database.

### FR-203

Successfully retrieved foods shall be cached locally.

---

## OCR

### FR-300

Users shall capture a nutrition label using the camera.

### FR-301

The system shall extract:

- Product name
- Brand
- Serving size
- Calories
- Protein
- Carbohydrates
- Fat

### FR-302

OCR output shall require user confirmation before persistence.

### FR-303

OCR confidence scores shall be stored.

---

## Diary

### FR-400

Users shall create diary entries.

### FR-401

Diary entries shall belong to one meal:

- Breakfast
- Lunch
- Dinner
- Snack

### FR-402

Users shall modify serving quantities.

### FR-403

Users shall delete diary entries.

### FR-404

Macro totals shall update automatically.

---

## Dashboard

### FR-500

Display:

- Calories consumed
- Protein consumed
- Carbohydrates consumed
- Fat consumed

### FR-501

Display remaining calories/macros based on configured goals.

---

# 6. Non-Functional Requirements

## Performance

- App launch < 2 seconds
- Barcode lookup < 1 second (cached)
- OCR processing < 5 seconds
- Food search < 150 ms

---

## Reliability

- Offline support for previously cached foods
- Automatic retry of failed API requests
- Graceful degradation if OCR fails

---

## Security

- HTTPS only
- JWT authentication
- Password hashing
- Row-Level Security (RLS)
- Input validation on all endpoints

---

## Maintainability

- Layered architecture
- Feature-based modules
- Strong typing
- Automated linting
- Automated formatting

---

# 7. Technical Stack

## Mobile

- React Native
- Expo
- TypeScript
- TanStack Query
- Zustand

## Backend

- FastAPI
- Python
- SQLModel
- Alembic

## Database

- PostgreSQL
- Supabase

## Storage

- Supabase Storage

## OCR

- Vision-capable LLM (initial implementation)

## Barcode

- OpenFoodFacts API

---

# 8. API Requirements

The backend shall expose REST endpoints.

Minimum endpoints:

POST   /auth/register

POST   /auth/login

GET    /foods

POST   /foods

PATCH  /foods/{id}

DELETE /foods/{id}

POST   /barcode

POST   /ocr

GET    /diary/{date}

POST   /diary

PATCH  /diary/{id}

DELETE /diary/{id}

---

# 9. Data Requirements

The system shall persist:

- Users
- Foods
- Diary Entries
- OCR Scans
- Barcode Cache

Food records shall contain:

- Name
- Brand
- Barcode (optional)
- Serving size
- Calories
- Protein
- Carbohydrates
- Fat

---

# 10. Acceptance Criteria

The MVP is considered complete when:

- Users can authenticate.
- Users can manually create foods.
- Users can search foods.
- Users can scan nutrition labels.
- Users can scan barcodes.
- Users can log meals.
- Daily macro totals calculate correctly.
- The application is deployable.
- The application is usable on Android and iOS.

---

# 11. Future Enhancements

The following features are intentionally deferred:

- AI meal recommendations
- Recipe parsing
- Receipt scanning
- Voice food logging
- Food photo recognition
- Nutrition analytics
- Goal adaptation
- Meal templates
- Shared food libraries
- Web client
