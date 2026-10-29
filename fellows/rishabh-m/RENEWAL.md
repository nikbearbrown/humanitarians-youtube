# Renewal Request — Rishabh M.

- **Role:** Technical Lead
- **Supervisor:** Nik Bear Brown
- **Current agreement:** 1 Aug — 31 Oct
- **Requested period:** 1 Nov — 31 Jan


## What the current period produced

**AI Research Assistant, Stages 1 and 2 — complete.** All evidence is in the repository above;
every figure below comes from a logged run, not an estimate.

- **Infrastructure first:** FastAPI, PostgreSQL, Ollama, OpenSearch and Airflow 3 wired
  together and health-checked before any AI logic, with an `/ask` contract, contract tests and a
  one-command `make reset`.
- **Metadata Ingestion:** a rate-limited arXiv client (one shared limiter, retries with
  backoff, fail fast on bad requests), a parser designed from real API responses, one idempotent
  `INSERT … ON CONFLICT` per batch, and Alembic migrations run by a one-off container.
- **PDF Processing:** PDFs downloaded through the same limiter, byte-checked and cached
  atomically by version; parsed by Docling inside Airflow only, with models baked into the image;
  per-paper status in the database, so one bad PDF fails alone and the work queue is a query.
- **Orchestration:** a daily DAG that re-fetches an overlapping five-day window (arXiv
  announces late, especially over weekends), one run at a time with retries and timeouts, cache
  retention that runs even after failures, a run report that keeps failed runs red, and an API that
  shows each paper's status, its parsed sections and pipeline stats.
- **At the end of Stage 2:** 2,959 papers in Postgres; 22 tests, plus mypy on `src/` and the DAG code.

**Humanitarians AI site and portal:** the Fellows Portal moved from one shared admin password to
three roles (fellow, admin, super-admin), and the site's dead links, duplicated tool files and an
unreachable route were fixed.

**Explainers:** a three-part *Agentic Design Patterns* series, and a six-part *Building a Research
Assistant* series documenting Stages 1 and 2, each with a 9:16 Short.

**As Technical Lead:** weekly scheduled office hours (3 h), email and Discord, guiding volunteers,
and the end-of-period renewal requests.

### Evidence

| Week | Work | Drive | Commit | Log |
|---|---|---|---|---|
| [3–7 Aug](./2026-07-29-fellows-portal-refactor/) | Fellows Portal refactor | [folder](https://drive.google.com/drive/folders/1nCRcJBro2DOLOOiIDad9eehPNXtCSQsp) | - | - |
| [10–14 Aug](./2026-08-14-dead-links-live-redirects/) | Site link and route cleanup | [folder](https://drive.google.com/drive/folders/1ZpGBUbUjC_IPkM-zQ-sbvsQYPRLAgZKO) | - | - |
| [24–28 Aug](./2026-08-28-agentic-design-patterns-part-1/) | Agentic Design Patterns · Part 1 | [folder](https://drive.google.com/drive/folders/13w6xlluEtCFhMQGBpVoiqvvPo4Qyo1gM) | - | - |
| [31 Aug – 4 Sep](./2026-09-04-agentic-design-patterns-part-2/) | Agentic Design Patterns · Part 2 | [folder](https://drive.google.com/drive/folders/1Qn7Qh_WEXj12mIUq6F8RUpesRn-fAZAu) | - | - |
| [7–11 Sep](./2026-09-11-agentic-design-patterns-part-3/) | Agentic Design Patterns · Part 3 | [folder](https://drive.google.com/drive/folders/1-T8VfuV9PZTEEDlliOZzI6VuOj_VoZHO) | - | - |
| [14–18 Sep](./2026-09-18-research-assistant-part-1/) | Infrastructure Setup | [folder](https://drive.google.com/drive/folders/1j0UDC0IdGHN4p1YBhjwIisUKjXqrA3-K) | [repo](https://github.com/RishabhHM/AI-Research-Assistant) | - |
| [21–25 Sep](./2026-09-25-research-assistant-part-2/) | Building on Designing Principles | [folder](https://drive.google.com/drive/folders/16plFmboLsS9cXeln9Xs9OEbUUr9O7hN1) | [repo](https://github.com/RishabhHM/AI-Research-Assistant) | - |
| [28 Sep – 2 Oct](./2026-10-02-research-assistant-part-3/) | Working on Bugs and rules | [folder](https://drive.google.com/drive/folders/1QOtmHi60Fr26abq6rK3c_mb0sWLQoWW7) | [`9849fdf`](https://github.com/RishabhHM/AI-Research-Assistant/commit/9849fdfc17981b74dbb8042edbbe6413bd191b33) | - |
| [5–9 Oct](./2026-10-09-research-assistant-part-4/) | Metadata Ingestion | [folder](https://drive.google.com/drive/folders/1TcLfQncfg-LSAnTao7RW7xvedUpr2oOB) | [`22f9c6b`](https://github.com/RishabhHM/AI-Research-Assistant/commit/22f9c6b39ff163efd52be7e7d4a6892f5bb2aefc) | [log](./2026-10-09-research-assistant-part-4/FRICTIONAL.md) |
| [12–16 Oct](./2026-10-16-research-assistant-part-5/) | PDF Processing | [folder](https://drive.google.com/drive/folders/1rca04Q1xJCdidYSC3QelYdoodXrX9G1H) | [`10d074b`](https://github.com/RishabhHM/AI-Research-Assistant/commit/10d074b4324e2b00eb8546eefcb25f3d12509873) | [log](./2026-10-16-research-assistant-part-5/FRICTIONAL.md) |
| [19–23 Oct](./2026-10-23-research-assistant-part-6/) | Orchestration and the Papers API | [folder](https://drive.google.com/drive/folders/1L6V_ArnaUhA5H21NCZkvHcUROG6IgxBY) | [`cc5cdd3`](https://github.com/RishabhHM/AI-Research-Assistant/commit/cc5cdd3ac3470e7f8467be413099bec5e627f340) | [log](./2026-10-23-research-assistant-part-6/FRICTIONAL.md) |

Weekly hours: [HOURS.md](HOURS.md). Weekly Frictional logs: one per work folder from Stage 2A,
listed in [README.md](README.md).

## Plan for the requested period

1. **Stage 3: search**, with OpenSearch BM25 plus vectors.
2. **Stage 4: question answering** with the local LLM and cited sources, replacing the mock `/ask`.
3. **Stage 5: observability and a simple UI.**

Each stage is estimated to take around a week.

Reporting continues as it has: a dated Frictional log per work folder, weekly hours, and an
explainer with a Short for each stage.

## Open items I am carrying

- The first scheduled run's batch-size check (parsed + failed + skipped = 25)
- SQL tests against real Postgres, and the arXiv client tests deferred from 2A
