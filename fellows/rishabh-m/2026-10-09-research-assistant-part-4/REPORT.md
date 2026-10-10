# Stage 2A — Metadata ingestion: real arXiv papers into Postgres

**Week:** 5–9 Oct 2026 · logged 2026-10-09
**Project:** AI Research Assistant — production RAG over arXiv papers
**Repository:** https://github.com/RishabhHM/AI-Research-Assistant
**Evidence of commit:** [`22f9c6b`](https://github.com/RishabhHM/AI-Research-Assistant/commit/22f9c6b39ff163efd52be7e7d4a6892f5bb2aefc)

- **Drive:** https://drive.google.com/drive/folders/1TcLfQncfg-LSAnTao7RW7xvedUpr2oOB
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `research-assistant-part-4.mp4` (16:9, 5:37) · `short/research-assistant-part-4-short.mp4` (9:16, 1:23)

## What this stage was for

Stage 1 ended with every service running and a database holding one sample paper.
Stage 2's goal is to fill it automatically: arXiv API → metadata → PDF → parse → Postgres.
2A is the first third: real cs.AI metadata in the `papers` table, through a script and a
manually triggered Airflow DAG, with Alembic managing the schema.

Four rules were set before any code: **respect the service** (one arXiv request every 3 s),
**design from real data**, **isolate failures at the right level**, and **make every run safe
to repeat**.

## What was built

| File | What it does |
|---|---|
| `src/config.py` | Nested `ArxivSettings` (`ARXIV__*` env vars). `rate_limit_delay` has a floor, `ge=3.0`: a faster value fails validation. |
| `src/schemas/arxiv.py` | `ArxivPaper` — arXiv's shape, mapped to `PaperCreate` in one place. |
| `src/services/arxiv/parser.py` | Pure XML → `ArxivPaper`. IDs stored without version; old-style IDs (`cs/0112017`) kept whole; malformed entries skipped, broken feeds raise. |
| `src/services/arxiv/rate_limiter.py` | One limiter every request goes through. Monotonic clock, injected clock/sleep for tests. |
| `src/services/arxiv/client.py` | Sync httpx client: paging, retries on timeouts/429/5xx with backoff + jitter (capped at 60 s), fail fast on 4xx with arXiv's own message. |
| `src/repositories/paper.py` | `upsert_many`: one `INSERT … ON CONFLICT DO UPDATE` per batch — atomic and idempotent. |
| `src/services/ingestion.py`, `scripts/ingest_papers.py` | Fetch → upsert, for a date range; local runs and backfills. |
| `airflow/dags/arxiv_ingestion.py` | Manual DAG with a `target_date` param. |
| `alembic.ini`, `migrations/` | Alembic; first revision `252395d5cf36` creates `papers`. Runs in a one-off `migrate` compose service that API and Airflow wait on. |
| `.pre-commit-config.yaml` | Local `uv run` hooks, so pre-commit matches `make lint`. |
| Tests | `tests/test_config.py`, `tests/test_arxiv_parser.py` + a real-data fixture; the Stage 1 tests that `.gitignore` had hidden. |

## Results

| Measure | Value |
|---|---|
| Sep 1 cs.AI fetch | 243 papers, all IDs unique |
| Requests / time | 3 (start = 0 / 100 / 200), 6.5 s |
| Same day ingested twice | still 243 rows, all refreshed — idempotent |
| DAG run (Oct 8) | success in ~9 s, 283 papers |
| Papers in the database | 527 (sample + Sep 1 + Oct 8) |

## Problems found by running it

1. **Docker had no volumes at all** after a month away; the planned volume reset failed with `no such volume`. Used `make reset`.
2. **Timestamps had no defaults.** `Paper` redeclared `created_at`/`updated_at`, replacing the mixin's columns. Caught with `\d papers` (`511c15d`).
3. **Tests were never committed.** `.gitignore` held `test_*.py` (`3039e2d`).
4. **Pre-commit passed a mypy error `make lint` caught** — its isolated mypy couldn't see pydantic (`ec3c8d9`).
5. **A 2.79 s logged gap** looked like a rate-limit violation; httpx logs response arrival, the limiter spaces sends.

## Evidence

- Commits `511c15d` … `22f9c6b` (Oct 5–8) — [`511c15d…22f9c6b`](https://github.com/RishabhHM/AI-Research-Assistant/compare/511c15d2e116a8a6c2bc2c8c4442a68059850ad1~1...22f9c6b39ff163efd52be7e7d4a6892f5bb2aefc)
- `personal/Documentation/Stage 2 - Data Pipeline.md`, Part 2A (Verify sections hold the recorded results above)

## Next: 2B (12–16 Oct)

PDF download and cache through the shared rate limiter; pypdf vs Docling on real papers;
the first real migration (`pdf_status`, parsed content, errors, attempts); per-paper failure isolation.
