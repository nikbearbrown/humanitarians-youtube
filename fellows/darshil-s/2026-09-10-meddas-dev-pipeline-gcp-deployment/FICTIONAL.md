# Frictional Log — 2026-10-09

**Learnings:** Revisited the full dev pipeline as one connected system rather than separate pieces — multi-stage Docker build, Cloud Run + Artifact Registry infrastructure, WIF auth, PR gates, tag-triggered deploys, and rollback all reinforcing each other, and why an environment-agnostic pipeline design is what lets the same workflow carry forward into staging and production.

**Implemented work:** Consolidated documentation of the complete CI/CD pipeline end to end, confirming each piece (build, auth, deploy gates, rollback) is correctly wired together and ready to serve as the template for staging and production.
