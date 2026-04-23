# SDLC Skills: fruit_shop_sdlc_cycle

## 🚀 Skill Name: `fruit_shop_sdlc_cycle`
**Description:** A full-lifecycle automation routine that follows the standard SDLC pattern: **Plan $\rightarrow$ Develop $\rightarrow$ Test $\rightarrow$ Deploy**.

---

## 🛠️ The Execution Protocol

This skill is designed to be triggered for every new feature or bug fix to ensure a predictable and high-quality release.

### 📋 Step 1: PLAN (Strategic Architecting)
**Actor:** `planner_agent`  
**Input:** High-level requirement or Issue Description.  
**Action:** 
- Analyze the requirement.
- Break down tasks into a technical roadmap.
- Update `PROGRESS.md` to reflect current progress.
- **Output:** A sequenced list of actionable tasks in `PROGRESS.md`.

### 💻 Step 2: DEVELOP (Implementation)
**Actor:** `developer_agent`  
**Input:** Plan from Phase 1.  
**Action:**
- Implement core logic (Models, Schemas, CRUD, API).
- Maintain `pyproject.toml` and `Dockerfile` integrity.
- Ensure code follows the modular OOP pattern.
- **Output:** Functional, modular code in the `src/` directory.

### 🧪 Step 3: TEST (Verification)
**Actor:** `tester_agent` (or `developer_agent` performing verification)  
**Input:** Implemented code and `tests/` directory.  
**Action:**
- Execute `pytest` suites.
- Validate API endpoints via `TestClient`.
- Verify dependency resolution via `uv sync`.
- **Output:** A `PASSED` or `FAILED` status report.

### 🚢 Step 4: DEPLOY (GitOps & CI/CD)
**Actor:** `cicd_agent`  
**Input:** Verified code and `k8s/` manifests.  
**Action:**
- `git add`, `commit`, and `push` to the `master` branch.
- Trigger GitHub Actions (Build Docker Image $\rightarrow$ Push to GCP Artifact Registry).
- (Optional) Apply Kustomize overlays to the local/production K8s cluster.
- **Output:** Successful deployment to the target environment.

---

## 🚦 Failure Handling
If any phase fails, the skill execution **MUST STOP** immediately and report the specific phase and error to the User.

- **Phase 1/2 Failure:** A documentation or code error (e.g., `ModuleNotFoundError`).
- **Phase 3 Failure:** A logic error (e.g., `AssertionError` in `pytest`).
- **Phase 4 Failure:** A deployment error (e.g., `GCP_SA_KEY` authentication issue).

## 📝 Usage Examples
- *Trigger:* `"Run fruit_shop_sdlc_cycle for [Feature Name]"`
- *Status Check:* `"Check progress of the current cycle."`
