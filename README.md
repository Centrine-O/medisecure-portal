# MediSecure Portal

A **HIPAA-compliant healthcare patient portal** built with FastAPI (Python), PostgreSQL, Redis, and a to-be-built frontend. Patients can manage appointments and submit medical forms securely; staff/admins can view, review, and manage patient records.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI (Python) |
| Database | PostgreSQL 15 |
| Cache / Queue Broker | Redis 7 |
| Background Jobs | Celery (wired, not yet implemented) |
| Auth | JWT (python-jose) + bcrypt |
| Encryption | Fernet (cryptography lib) |
| Frontend | *(not started)* |
| Containerization | Docker + Docker Compose |
| Orchestration | Kubernetes *(not started)* |

---

## What's Done ✅

### Backend
- [x] FastAPI app setup with CORS, logging, health check (`/health`)
- [x] PostgreSQL database connection (SQLAlchemy)
- [x] Database models: `Patient`, `User`, `Appointment`, `MedicalForm`
- [x] Role-based user model: Admin, Doctor, Nurse, Receptionist, Viewer
- [x] Auth service: bcrypt password hashing, JWT token creation & verification
- [x] Encryption service: Fernet tokenization for SSN, insurance number, credit card; display masking
- [x] Auth API endpoints:
  - `POST /api/v1/auth/patient/register`
  - `POST /api/v1/auth/patient/login`
  - `POST /api/v1/auth/user/register`
  - `POST /api/v1/auth/user/login`
- [x] Docker Compose setup (PostgreSQL + Redis + Backend)

---

## What's Left To Build 🚧

### 1. Backend — Protected Routes & Current User
- [ ] `GET /api/v1/auth/me` — return logged-in patient or staff info from JWT
- [ ] JWT dependency/guard middleware (reusable `get_current_patient`, `get_current_user`)
- [ ] Role-based access guards (e.g., only `admin` can register new staff)
- [ ] Lock down `POST /api/v1/auth/user/register` behind admin auth

### 2. Backend — Patient API
- [ ] `GET /api/v1/patients/me` — get own profile
- [ ] `PUT /api/v1/patients/me` — update own profile
- [ ] `PUT /api/v1/patients/me/sensitive` — update SSN / insurance / payment (encrypts on save)

### 3. Backend — Appointments API
- [ ] `POST /api/v1/appointments` — patient books an appointment
- [ ] `GET /api/v1/appointments/me` — patient views their appointments
- [ ] `PUT /api/v1/appointments/{id}/cancel` — patient cancels appointment
- [ ] `GET /api/v1/appointments` — staff views all appointments (with filters)
- [ ] `PUT /api/v1/appointments/{id}/status` — staff updates appointment status (confirm, complete, no-show)

### 4. Backend — Medical Forms API
- [ ] `POST /api/v1/forms` — patient submits a form (intake, consent, HIPAA, etc.)
- [ ] `GET /api/v1/forms/me` — patient views their submitted forms
- [ ] `GET /api/v1/forms/{id}` — get a specific form
- [ ] `GET /api/v1/forms` — staff views all forms (with filters)
- [ ] `PUT /api/v1/forms/{id}/review` — staff reviews/approves/rejects a form

### 5. Backend — Email Verification Flow
- [ ] Generate and store email verification token on patient registration
- [ ] `GET /api/v1/auth/verify-email?token=...` — verify patient email, set `is_verified=True`
- [ ] Trigger verification email via Celery worker (see below)

### 6. Celery Worker
- [ ] Set up Celery app (`worker/` directory)
- [ ] Task: send registration/email verification email
- [ ] Task: send appointment confirmation email
- [ ] Task: send appointment reminder email (scheduled)

### 7. Frontend
- [ ] Choose framework (React / Next.js recommended)
- [ ] Patient portal:
  - [ ] Registration & Login page
  - [ ] Dashboard (upcoming appointments, pending forms)
  - [ ] Book appointment page
  - [ ] Medical forms page (fill & submit forms)
  - [ ] Profile page
- [ ] Staff portal:
  - [ ] Login page
  - [ ] Patient search & list
  - [ ] Appointment management board
  - [ ] Form review queue
  - [ ] Admin: user management

### 8. Tests
- [ ] Unit tests: auth service, encryption service
- [ ] Integration tests: auth endpoints (register, login)
- [ ] Integration tests: appointment endpoints
- [ ] Integration tests: form endpoints
- [ ] Test fixtures and database setup

### 9. Kubernetes (Production Deployment)
- [ ] Deployment manifests for backend
- [ ] Deployment manifests for worker
- [ ] Service & Ingress config
- [ ] ConfigMap and Secrets
- [ ] Persistent volume for PostgreSQL
- [ ] Horizontal pod autoscaling

---

## Running Locally

```bash
# Start all services (PostgreSQL, Redis, Backend)
docker-compose up --build

# API is available at:
# http://localhost:8000
# Swagger docs: http://localhost:8000/docs
```

---

## Environment Variables

Copy `.env.example` to `.env` in the `backend/` directory and fill in the values before running.

---

## Project Structure

```
medisecure-portal/
├── backend/
│   ├── app/
│   │   ├── api/          # Route handlers
│   │   ├── core/         # Config, DB connection
│   │   ├── models/       # SQLAlchemy models
│   │   └── services/     # Auth, Encryption logic
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/             # (not started)
├── worker/               # Celery worker (not started)
├── tests/                # (not started)
├── k8s/                  # Kubernetes manifests (not started)
└── docker-compose.yml
```
