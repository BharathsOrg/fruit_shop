# Project Memory: Fruit Shop API

## 🧠 Context & Knowledge
- **Project Name:** Fruit Shop API
- **Core Objective:** A modular FastAPI service for managing fruit inventory.
- **Architecture:** Modular OOP-compliant structure (Models, Schemas, CRUD, API).
- **Key Dependencies:** FastAPI, SQLAlchemy, Alembic, Pydantic-settings, Psycopg2.
- **Database:** Remote PostgreSQL (currently configured for `pg.krishb.in`).

## 🛠️ Technical Details
- **Database URL Construction:** Dynamic, using `POSTGRES_PASSWORD` from environment variables.
- **Migrations:** Managed via Alembic, utilizing `alembic/env.py` to import application metadata for autogenerate capabilities.
- **Environment Management:** Optimized for `uv` and `pip`.

## 🚧 Current State & Known Issues
- **Status:** The application is functional; CRUD endpoints are implemented and the `/health` endpoint is live.
- **Dependency Management:** Switched from `requirements.txt` to `pyproject.toml` using `uv` for robust version control.
- **Blocker Resolved:** Successfully implemented `src/main.py` and a `/health` endpoint to verify service availability.
- **Current Phase:** Phase 5 (Testing) - Moving toward expanded Pytest suites.

## 📂 Folder Map
- `src/core/`: DB connection and configuration logic.
- `src/models/`: SQLAlchemy ORM classes.
- `src/schemas/`: Pydantic validation models.
- `src/api/`: FastAPI route handlers (includes `v1/endpoints/health.py` and `v1/endpoints/fruit.py`).
- `src/crud/`: Business logic for DB operations (includes `crud_fruit.py`).
- `src/main.py`: Application entry point.
- `alembic/`: Migration scripts and environment config.
