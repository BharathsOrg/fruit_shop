# Project Memory: Fruit Shop API

## 🧠 Context & Knowledge
- **Project Name:** Fruit Shop API
- **Core Objective:** A modular FastAPI service for managing fruit inventory.
- **Architecture:** Modular OOP-compliant structure (Models, Schemas, CRUD, API).
- **Key Dependencies:** FastAPI, SQLAlchemy, Alemb, Pydantic-settings, Psycopg2.
- **Database:** Remote PostgreSQL (currently configured for `pg.krishb.in`).

## 🛠️ Technical Details
- **Database URL Construction:** Dynamic, using `POSTGRES_PASSWORD` from environment variables.
- **Migrations:** Managed via Alembic, utilizing `alembic/env.py` to import application metadata for autogenerate capabilities.
- **Environment Management:** Optimized for `uv` and `pip`.
- **K8s Deployment Pattern:** Uses Kustomize with a `base` directory and `local` overlay to ensure development environments are isolated and correctly prefixed.

## 🚨 Critical Verification Rule
- **POST-DEPLOYMENT VERIFICATION:** After any deployment to Kubernetes, a verification step **must** be executed to confirm the deployment is successful. 
- **Verification Steps:**
    1. Check pod status: `kubectl get pods -l app=fruit-shop`
    2. Verify service availability: `kubectl get service <local-service-name>`
    3. Perform a liveness check: `curl <service-url>/health`
- **Goal:** Ensure that the "dev version" of the code is actually running and reachable via its intended URL.

## 🚧 Current State & Known Issues
- **Status:** The application is functional; CRUD endpoints are implemented.
- **Deployment Status:** GitOps workflow is active. Pushing to `master` triggers a build, push to Artifact Registry, and a `kubectl apply` using the `local` Kustomize overlay.
- **Current Phase:** Phase 6 (Deployment & Verification).

## 📂 Folder Map
- `src/`: Application source code.
- `tests/`: Pytest suite (Unit & Integration).
- `k8s/kustomize/`: Kustomize manifests (Base & Overlays).
- `skills/`: Custom SDLC automation scripts.
- `Dockerfile`: Container configuration.
- `pyproject.toml`: Modern dependency management (`uv`).
