# Frictional Log — 2026-10-08

**Learnings:** Cloud Run's immutable-revision model — every deploy creates a new revision, traffic is pointed at it, and old revisions stay available for rollback or traffic shifting; the "golden signals" framing for service health (latency, traffic, errors) as the basis for what to monitor.

**Implemented work:** Added an automated smoke test that runs immediately after every staging deploy, gating success on a correct live response. Built awareness of Cloud Run's traffic splitting/pinning across revisions into the staging process. Wired all staging application/request logs into Cloud Logging for a centralized, searchable view, and set up basic monitoring tracking request latency, error rate, and traffic volume.
