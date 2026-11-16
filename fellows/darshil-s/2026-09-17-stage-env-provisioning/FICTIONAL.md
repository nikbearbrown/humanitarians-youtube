# Frictional Log — 2026-09-17

**Learnings:** How one Workload Identity Federation pool can safely serve multiple trust boundaries — dev and stage — through attribute-conditions and separately scoped principal sets, rather than needing a new identity provider per environment; GitHub Environments as a way to give each deployment target its own secrets and variables within a single repo.

**Implemented work:** Provisioned a dedicated `medas-frontend-stage` Artifact Registry repo, widened the existing WIF provider's trust condition to also accept stage-environment runs, added an IAM binding scoped specifically to the stage GitHub Environment's principal set, and created the `stage` GitHub Environment with its own secrets and variables. Validated with a real `stage-v0.1.0` tag deploy, then a rollback run against that same tag.
