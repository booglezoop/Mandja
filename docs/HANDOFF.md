# Project Handoff Document

**Project:** Food Tracker MVP
**Repository:** food-tracker
**Status:** Development Environment Setup Phase
**Last Updated:** 2026-07-14

---

# 1. Project Overview

## Purpose

Food Tracker is a personal macronutrient tracking application focused on reducing friction in food logging.

The core concept is a **user-built food library**:

- Users create and maintain their own database of foods.
- Frequently used foods become reusable entries.
- New foods can be added through multiple ingestion methods:
  - Manual entry
  - Barcode scanning
  - Nutrition label scanning (OCR)

The MVP is intended as:

1. A personally useful nutrition tracking tool.
2. A portfolio-quality software engineering project demonstrating:
   - Full-stack development
   - Mobile development
   - API design
   - Database architecture
   - AI/OCR integration
   - Production development practices

---

# 2. Product Scope

## MVP Features

The initial MVP will include:

### Authentication

- User registration
- Login
- Persistent sessions

---

### Personal Food Library

Users can:

- Create foods manually
- Edit foods
- Delete foods
- Search foods
- Reuse existing foods

Food attributes:

- Name
- Brand
- Serving size
- Calories
- Protein
- Carbohydrates
- Fat

---

### Food Logging

Users can:

- Log foods to meals
- Adjust serving sizes
- View daily macro totals

Meal categories:

- Breakfast
- Lunch
- Dinner
- Snack

---

### Food Ingestion

Future MVP features:

## Barcode scanning

Flow:
Barcode scan
|
v
Local database lookup
|
v
External API lookup if unavailable
|
v
Save normalized food

Planned external source:

- OpenFoodFacts API

---

## Nutrition Label OCR

Flow:
Camera image
|
v
OCR extraction
|
v
Nutrition data parsing
|
v
User confirmation
|
v
Food library

Extracted data:

- Product name
- Brand
- Serving size
- Calories
- Protein
- Carbohydrates
- Fat

---

# 3. Technical Architecture

## Planned Stack

## Mobile Application

Technology:

- React Native
- Expo
- TypeScript

Responsibilities:

- User interface
- Camera access
- Barcode scanning
- Diary interface
- API communication

---

## Backend API

Technology:

- FastAPI
- Python

Responsibilities:

- Business logic
- Authentication handling
- Food management
- Diary management
- OCR processing
- Barcode integration

---

## Database

Technology:

- PostgreSQL
- Supabase

Responsibilities:

- User data
- Food library
- Diary entries
- OCR history
- Barcode cache

---

## Storage

Technology:

- Supabase Storage

Used for:

- Nutrition label images
- Optional food images

---

# 4. Repository Structure

Current intended structure:
food-tracker/

├── .github/
│
├── .vscode/
│
├── backend/
│
├── mobile/
│
├── docs/
│ ├── EPRD.md
│ ├── ARCHITECTURE.md
│ ├── DATABASE.md
│ ├── API.md
│ ├── DECISIONS.md
│ └── HANDOFF.md
│
├── scripts/
│
├── README.md
├── LICENSE
└── .gitignore

---

# 5. Current Development Status

## Completed

### GitHub Repository

Completed:

- Repository created
- Git initialized
- GitHub connection verified

---

### Documentation Foundation

Created:

- EPRD.md
- ARCHITECTURE.md placeholder
- DATABASE.md placeholder
- API.md placeholder
- DECISIONS.md placeholder

---

### VS Code Setup

Completed:

- Repository opened in VS Code
- Workspace configured
- `.vscode/settings.json` added

Current settings:

- Format on save enabled
- Trailing whitespace removal
- Final newline enforcement

---

### Development Environment

Completed:

- Distrobox installed and verified
- Development container created:
  dev

Container:
Ubuntu 24.04 LTS

Current environment:
SteamOS Host
|
|
Distrobox
|
Ubuntu 24.04 Container

---

# 6. Current Environment State

## Host Machine

Operating System:
SteamOS 3.8.14
Architecture:
Linux

---

## Development Container

Container:
dev

OS:
Ubuntu 24.04.4 LTS

Verified:
Python 3.12.3
Node.js 18.19.1
npm 9.2.0
Git installed

---

# 7. Current Location Issue

Repository currently exists at:

/home/deck/Desktop/Mandja/Mandja

Recommended future location:

/home/deck/Development/food-tracker

Reason:

- Cleaner development organization
- Easier backup
- Better for managing multiple projects
- Avoid Desktop clutter

The repository should be moved before initializing backend/mobile projects.

---

# 8. Next Steps

## Step 1 — Move Repository

Move:

Desktop/Mandja/Mandja

to:

~/Development/food-tracker

Verify Git still works:

git status

---

## Step 2 — Install Development Tooling

Inside Distrobox:

Install:

- uv
- pnpm

Potential future:

- Node.js upgrade to Node 22 LTS

---

## Step 3 — Initialize Backend

Create FastAPI application:

Expected result:
backend/

├── app/
├── tests/
├── pyproject.toml
└── uv.lock

---

## Step 4 — Initialize Mobile App

Create Expo application:

Expected result:
mobile/

├── app/
├── package.json
├── tsconfig.json
└── app.json

---

## Step 5 — Configure Local Development

Goal:

Run:

Backend:

localhost:8000

Mobile:

Expo development server

Test using:

Expo Go on iPhone

---

# 9. Development Principles

The project should follow:

## Feature-first organization

Avoid:

controllers/
services/
models/

Prefer:

food/
diary/
auth/
ocr/
barcode/

Each feature owns its:

- routes
- services
- models
- tests

---

## API-first development

Mobile application communicates only through backend APIs.

No direct database access.

---

## Version Control

Use conventional commits:

Examples:

feat: add food creation endpoint

fix: correct macro calculation

docs: update architecture notes

chore: update dependencies

---

## Branch Strategy

Main branch:

main

Feature branches:

feature/auth
feature/backend-api
feature/barcode
feature/ocr

---

# 10. Important Decisions

## Decision: Distrobox over modifying SteamOS

Reason:

- Keeps SteamOS stable
- Reproducible environment
- Easier dependency management

---

## Decision: FastAPI backend instead of direct Supabase usage

Reason:

The goal is to demonstrate backend engineering:

- API design
- Business logic
- Data validation
- Service architecture

Supabase remains infrastructure, not the application backend.

---

## Decision: Expo for mobile development

Reason:

The developer machine runs Linux and the target device is iPhone.

Expo allows:

- iOS testing without macOS
- Fast iteration
- Native device testing

---

## Decision: Add barcode_scan_log table (not in EPRD.md)

Reason:
Barcode_cache is global/shared, so it carries no per-user trace of who scanned what. Added a lightweight per-user audit table to preserve that visibility. This is an engineering addition beyond EPRD.md's stated FRs — not scope creep in the feature sense (no new user-facing capability), but flagged here for traceability.

---

# Current Priority

The immediate next task is:

**Move repository → finalize development tooling → scaffold FastAPI backend.**

No application features should be implemented until the development environment is stable.

---

# 11. Lessons Learned — Dev Environment Setup (2026-07-15)

Captured while scaffolding the FastAPI backend, since most friction was environment/tooling, not application code.

## Shell profile matters more than expected

- VS Code's integrated terminal defaulted to `sh` (dash), not `bash`.
- `sh` only reads `~/.profile`, and only as a **login shell** — it does NOT read `~/.bashrc`.
- `bash` reads `~/.bashrc` on every interactive start, login or not — more forgiving.
- Fix: set `"terminal.integrated.defaultProfile.linux": "bash"` in VS Code user settings, and make sure `~/.bashrc` actually exists (Distrobox containers don't always ship one by default).
- Symptom if this is misconfigured: PATH exports "don't stick" between terminal sessions, `uv`/other tools intermittently "disappear."

## Don't manually `source .venv/bin/activate` when using `uv`

- `uv run <command>` already resolves and uses the project's `.venv` automatically based on the nearest `pyproject.toml`.
- Manually activating a venv AND using `uv run` at the same time can cause confusion about which environment is actually active.
- The `(venvname)` prefix VS Code/bash shows in the prompt is just a **label** from activation — it does NOT reflect your current working directory. Don't trust it as a location indicator; use `pwd` to actually confirm where you are.
- Going forward: just `cd` into the project folder and use `uv run ...` — no `source`/`activate`/`deactivate` needed, ever.

## Watch for duplicate/stray venvs

- A second, empty `.venv` appeared at the **repo root** (`food-tracker/.venv`) alongside the real one at `backend/.venv`.
- Likely cause: VS Code's "Create Virtual Environment..." option in the interpreter picker, triggered accidentally while trying to select an interpreter.
- Symptom: activating the wrong one silently gives you a venv with none of your actual dependencies installed.
- Fix going forward: only ever let `uv init`/`uv add` create venvs; avoid VS Code's own "Create Virtual Environment" flow for this project.

## VS Code Pylance doesn't auto-discover nested venvs

- Workspace root is `food-tracker/`, but the venv lives one level down at `backend/.venv`.
- Pylance's interpreter auto-discovery didn't find it; had to manually enter the interpreter path.
- Fix applied: `backend/.vscode/settings.json` now pins `python.defaultInterpreterPath` explicitly so this doesn't need to be re-done if the venv is ever recreated.

## File creation via VS Code "New File" can land in the wrong folder

- `app/main.py`'s real content briefly ended up at `app/core/main.py` instead — one folder too deep.
- `uv init`'s auto-generated placeholder `main.py` (the "Hello from backend!" stub) was left in place at `app/main.py` and had to be explicitly deleted/overwritten.
- Takeaway: after creating files via right-click → New File, double check the file landed in the intended folder (visible in the editor tab breadcrumb) before pasting content — especially when creating several similarly-named files (multiple `routes.py`, multiple `main.py`-shaped content) in a row.

## Terminal "new tab" may restore old scrollback, not a truly blank session

- Opening a new terminal tab in VS Code can show previous commands/output still on screen.
- This looks like a command "already ran" when it didn't — always check for an actual blank prompt with cursor before assuming something executed.

## Missing CLI tools in this container

- `lsof` and `fuser` are not installed by default — use `ss -tlnp` as a fallback, or just pick a different port (e.g. 8001) instead of hunting down and killing a stale process, when unblocking quickly matters more than root-causing immediately.
