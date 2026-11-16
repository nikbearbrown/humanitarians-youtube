# Frictional Log — 2026-08-25

**Learnings:** Google Cloud Workload Identity Federation — how an existing WIF provider's trust condition can be widened to accept a new GitHub repo instead of standing up a new identity pool; how IAM impersonation on a shared service account separates two repos cryptographically; Cloud Run as a deploy target behind a tag-triggered pipeline.

**Implemented work:** Full GCP setup for the frontend — a dedicated Artifact Registry repo, widened the backend's existing WIF provider to also trust this repo, granted the frontend repo impersonation rights on the shared service account, and wired the GitHub Environment secrets/variables that tie it together. Built the tag-based CI/CD pipeline itself: a two-stage Docker build, a GitHub Actions workflow, and deploy to Cloud Run.
