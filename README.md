# aks-apps

A SaaS-style application and its Kubernetes delivery: a **FastAPI** REST API and a **Celery** background worker, backed by **PostgreSQL** and **Redis**, deployed to **AKS** via **Kustomize** overlays and **Argo CD** (GitOps).

## Architecture

- **API** — FastAPI service exposing item CRUD plus Kubernetes liveness/readiness probes.
- **Worker** — Celery worker for asynchronous jobs (Redis broker, PostgreSQL backing store).
- **Manifests** — Kustomize base + per-environment overlays (dev / staging / prod).
- **GitOps** — Argo CD Application definitions; dev/staging auto-sync, prod manual sync.

## Status

| Area | State |
|---|---|
| API — item CRUD + health endpoints | In progress |
| Celery worker | Planned |
| Containerization (multi-stage images) | Planned |
| Kustomize manifests | Planned |
| Argo CD GitOps | Planned |

## Local development

```bash
cd src
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
# interactive API docs at http://localhost:8000/docs
```

## Tests

```bash
pip install -r requirements-dev.txt
pytest
```

> The suite emits a Starlette warning suggesting `httpx2`. That's a typosquat impersonating `httpx`.
