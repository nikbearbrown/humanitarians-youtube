# Weekly Hours: Week 9 — Docker Layers, Caching & Scanning Learning

**Project:** MEDAS Aggregation Frontend — CI/CD & Rollback Pipeline
**Friction Log:** [FICTIONAL.md](FICTIONAL.md)
**Report Week:** Nov 5, 2026
**Total Hours:** 23.0 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Hours |
|---|---|---:|
| **Meetings** | Weekly supervisor check-in | 2.0 |
| **Research: Docker Layer Caching & Multi-Stage Builds** | Studying per-instruction layer caching, why instruction order matters, and why multi-stage builds discard the heavy toolchain so only the final output ships | 8.0 |
| **Research: CI Caching & Vulnerability Scanning** | Studying how CI-level dependency caching differs from and complements Docker's own layer cache, and how container vulnerability scanning checks image layers against CVE databases | 10.5 |
| **Brutalist Video Reel Production** | Scripting and rendering the `docker-layers-caching-scanning-learning` 4K reel | 1.5 |
| **Documentation** | Authoring `README.md` and `FICTIONAL.md` for this folder | 1.0 |
| **Total** | | **23.0** |

*Learning-only week — concepts studied here inform the existing multi-stage Dockerfile and CI pipeline rather than introducing new pipeline changes this week (see `FICTIONAL.md`).*

---
