# Fruit Shop API

A production-ready, modular FastAPI service for managing a fruit inventory, featuring PostgreSQL integration, SQLAlchemy ORM, and Alembic migrations.

## 🚀 Features

- **Framework:** FastAPI for high-performance API development.
- **Database:** PostgreSQL with SQLAlchemy ORM.
- **Migrations:** Alembic for scalable schema management.
- **Configuration:** `pydantic-settings` for robust environment variable management.
- **Architecture:** Modular OOP-compliant structure separating concerns (Models, Schemas, CRUD, API).

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **API Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Migration Tool:** Alembic
- **Dependency Management:** `uv` / `pip`

## 📂 Project Structure

```text
fruit_shop/
├── alembic/            # Database migration environment
├── src/
│   ├── api/            # API routes and endpoints
│   ├── core/           # Database connection and configuration
│   ├── crud/           # Business logic (CRUD operations)
│   ├── models/         # SQLAlchemy ORM models
│   └── schemas/        # Pydantic validation schemas
├── tests/              # Pytest suite
├── alembic.ini         # Alembic configuration
├── PROGRESS.md         # Project status and roadmap
├── requirements.txt    # Project dependencies
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
export POSTGRES_PASSWORD='your_password_here'
```

### 3. Install Dependencies
Using `uv` (recommended):
```bash
uv pip install -r requirements.txt
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
