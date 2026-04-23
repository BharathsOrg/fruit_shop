# Fruit Shop API

A production-ready, modular FastAPI service for managing a fruit inventory, featuring PostgreSQL integration, SQLAlchemy ORM, and Alembic migrations.

## 🚀 Features

- **Framework:** FastAPI for high-performance API development.
- **Database:** PostgreSQL with SQLAlchemy ORM.
- **Migrations:** Alembice for scalable schema management.
- **Configuration:** `pydantic-settings` for robust environment variable management.
- **Architecture:** Modular OOP-compliant structure separating concerns (Models, Schemas, CRUD, API).
- **Health Check:** Built-in `/health` endpoint for monitoring.
- **Containerization:** Fully Dockerized with optimized `uv` dependency management.
- **Orchestration:** Kustomize-ready Kubernetes manifests (Base & Overlays).

## 🛠️ Tech Stack

- **Language:** Python 3.14
- **API Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Migration Tool:** Alembic
- **Dependency Management:** `uv` (Standardized via `dependency-groups`)
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Kustomize)

## 📂 Project Structure

```text
fruit_shop/
├── .github/            # GitHub Actions Workflows
├── alembic/            # Database migration environment
├── k8s/                # Kubernetes Manifests
│   └── kustomize/      # Kustomize configuration (Base & Over-lays)
├── src/                # Application source code
│   ├── api/            # API routes and endpoints
│   ├── core/           # Database connection and configuration
│   ├── crud/           # Business logic (CRUD operations)
│   ├── main.py         # Application entry point
│   ├── models/         # SQLAlchemy ORM models
│   └── schemas/        # Pydantic validation schemas
├── tests/              # Pytest suite (Unit & Integration)
├── pyproject.toml      # Modern dependency management (uv)
├── Dockerfile          # Container configuration
├── alembic.ini         # Alembic configuration
└── README.md           # Project documentation
```

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd fruit_shop
```

### 2. Environment Variables
The project requires a `POSTGRES_PASSWORD` environment variable to connect to the remote database.
```bash
export POSTG_PASSWORD='your_password_here'
```

### 3. Install Dependencies
Using `uv` (Recommended):
```bash
uv sync
```

### 4. Database Migrations
To initialize the database schema:
```bash
alembic upgrade head
```

## 🚀 Running the Application

To start the development server:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive documentation can be found at `/docs`.
- **Health Check:** `http://localhost:8000/health`
