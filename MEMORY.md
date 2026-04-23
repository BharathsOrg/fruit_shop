# Project Memory: Fruit Shop API

## 🧠 Context & Knowledge
- **Project Name:** Fruit Shop API
- **Core Objective:** A modular FastAPI service for fruit inventory management.
- **Architecture:** Modular OOP-compliant structure (Models, Schemas, CRUD, API).
- **Key Dependencies:** FastAPI, SQLAlchemy, Alembic, Pydantic-settings, Psycopg2.
- **Database:** Remote PostgreSQL (currently configured for `pg.krishb.in`).

## 🛠️ Technical Details
- **Database URL Construction:** Dynamic, using `POSTGRES_PASSWORD` from environment variables.
- **Migrations:** Managed via Alembic, utilizing `alembic/env.py` to import application metadata for autogenerate capabilities.
- **Environment Management:** Optimized for `uv` and `pip`.

## 🚧 Current State & Known Issues
- **Blocker:** Authentication failure in migrations due to `POSTGRES_PASSWORD` mismatch/missing.
- **Current Phase:** Phase 3 (Database Migrations).
- **Last Successful Action:** Configured `alembic/env.py` and installed `psycopg2-binary`.

## 📂 Folder Map
- `src/core/`: DB connection and configuration logic.
- `src/models/`: SQLAlchemy ORM classes.
- `src/schemas/`: Pydantic validation models.
- `src/api/`: FastAPI route handlers.
- `src/crud/`: Business logic for DB operations.
- `alembic/`: Migration scripts and environment config.
