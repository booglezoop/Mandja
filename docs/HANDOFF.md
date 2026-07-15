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
