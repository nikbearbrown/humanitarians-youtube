# Frictional Log — 2026-11-05

**Learnings:** Docker's per-instruction layer caching and why instruction order matters; why multi-stage builds discard the heavy toolchain so only the final output ships; how CI-level dependency caching (keyed off a lockfile hash) differs from and complements Docker's own layer cache; how container vulnerability scanning checks image layers against CVE databases.

**Implemented work:** Learning-only week — no separate implementation video. Concepts studied here inform the existing multi-stage Dockerfile and CI pipeline rather than introducing new pipeline changes this week.
