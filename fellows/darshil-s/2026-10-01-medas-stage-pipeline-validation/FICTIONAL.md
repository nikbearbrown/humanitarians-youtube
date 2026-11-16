# Frictional Log — 2026-10-01

**Learnings:** Treating a deployment as a sequence of independently verifiable checkpoints (auth → build → push → deploy) rather than one black-box pass/fail; reading GitHub Actions' own logs and step-summaries as the observability layer that makes that kind of structured triage possible.

**Implemented work:** Triggered the first real `stage-v1.0.0` deployment and validated it checkpoint by checkpoint — authentication, build, push, and deploy — then confirmed the rollback workflow against that same deployed image, closing the loop on both the forward and recovery paths before calling the staging pipeline verified end-to-end.
