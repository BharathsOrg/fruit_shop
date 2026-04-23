# Agents

This document tracks the roles and responsibilities of the agents involved in the Fruit Shop API development.

## 🤖 Agent Roles

### 1. User (Project Lead)
- **Role:** Provides high-level requirements, technical constraints, and approvals.
- **Responsibilities:**
    - Define the scope of the project.
    - Provide environment credentials (e.g., `POSTGRES_PASSWORD`).
    - Review and approve progress (e.g., "LGTM").
    - Direct the direction of development phases.

### 2. Planner Agent
- **Role:** Strategic architect and task orchestrator.
- **Responsibilities:**
    - Break down high-level requirements into actionable phases.
    - Create the development roadmap and `PROGRESS.md`.
    - Sequence tasks (Models -> Migrations -> CRUD -> API -> Testing).

### 3. Developer Agent
- **Role:** Implementation engineer (Full-Stack/Backend).
- **Responsibilities:**
    - Scaffold the project directory structure.
    - Write modular, OOP-compliant code (Models, Schemas, CRUD, API).
    - Configure database connections and Alembic migrations.
    - Manage dependencies using `uv`.
    - Troubleshoot environment and connection errors.
    - Maintain project documentation (`README.md`, `MEMORY.md`, `PROGRESS.md`).

### 4. Tester Agent
- **Role:** Quality Assurance and Verification.
- **Responsibilities:**
    - Write and execute Pytest suites.
    - Verify API functionality (Endpoints, Status Codes, JSON payloads).
    - Ensure the `src` package is correctly structured for imports.

### 5. CI/CD Agent
- **Role:** Deployment and Automation.
- **Responsibilities:**
    - Manage Dockerfile and Containerization.
    - Handle Kubernetes manifests and Kustomize overlays.
    - Execute GitOps workflows (Push to trigger build/deploy).
