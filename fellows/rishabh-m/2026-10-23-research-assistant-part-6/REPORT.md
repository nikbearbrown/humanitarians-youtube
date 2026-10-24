# Stage 2C — Orchestration and operations: a daily pipeline that stays honest

**Week:** 19–23 Oct 2026 · logged 2026-10-23
**Project:** AI Research Assistant — production RAG over arXiv papers
**Repository:** https://github.com/RishabhHM/AI-Research-Assistant
**Evidence of commit:** [`cc5cdd3`](https://github.com/RishabhHM/AI-Research-Assistant/commit/cc5cdd3ac3470e7f8467be413099bec5e627f340)

- **Drive:** https://drive.google.com/drive/folders/1L6V_ArnaUhA5H21NCZkvHcUROG6IgxBY
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `research-assistant-part-6.mp4` (16:9, 4:51) · `short/research-assistant-part-6-short.mp4` (9:16, 1:10)
- **Previous stage:** [Stage 2B](../2026-10-16-research-assistant-part-5/)

## What this stage was for

2B could parse PDFs when triggered by hand. 2C makes the pipeline run itself: `arxiv_ingestion`
runs every day at 06:00 UTC — `ingest_metadata` → `process_pdfs` → `prune_pdf_cache` → `report` —
re-fetching an overlapping window so no paper is missed, retrying itself, capping its own run time,
cleaning the cache, and reporting, **staying red when something failed**. The API shows each paper's
pipeline status, its parsed sections and overall stats.

## What was built

| File | What it does |
|---|---|
| `src/services/ingestion.py` | `resolve_window`: the last 5 days up to the run's logical date (or now for manual runs); `target_date` backfills one day. |
| `airflow/dags/arxiv_ingestion.py` | Daily 06:00 UTC, weekends included; `catchup=False`; `max_active_runs=1`; 2 retries 30 min apart; 4 h / 6 h timeouts; `pdf_limit` falls back to `PDF__BATCH_SIZE` (25). |
| `src/services/pdf_cache.py` | `prune`: deletes cached `.pdf`/`.part` files older than 14 days; the task runs with `trigger_rule="all_done"`. |
| `report` task | Reads every upstream XCom; a missing one means a failed task; logs window, results, cache and queue, then raises so the run stays red (`retries=0`). |
| `src/repositories/paper.py` | `pdf_status_counts`, `count_retries_exhausted`, `stats`, `get_by_arxiv_id(with_sections)`, status filter on `get_all`. |
| `src/routers/papers.py`, `src/schemas/paper.py` | `GET /papers?status=…` (still a list, now with `pdf_status`), `GET /papers/stats` (declared before the ID route), `GET /papers/{arxiv_id}[vN]` with sections. |
| `pyproject.toml`, `Makefile` | mypy on `src/` **and** `airflow/dags/`; `make check-dags`. |
| Tests | `test_ingestion_window.py`, `test_pdf_cache.py`, `test_papers_api.py` — 22 tests in total. |

## Results

| Measure | Value |
|---|---|
| Normal run (logical date Oct 22, `pdf_limit` 1) | 1,190 papers, Oct 17–22; parsed 1; cache 1 file deleted; queue parsed 31 · pending 2,924 · skipped 4; retries exhausted 0 |
| Manual run (logical date Oct 20) | window Oct 15–20, 1,238 papers |
| Failure run (logical date Oct 24) | fetch ✓ · parse ✗ (404) · prune ✓ (all_done) · report ✗ (raised) · **run red** |
| API | `/papers/stats` matches the report; `?status=parsed` returns no sections; `/papers/{id}v1` found with 24 sections; bad status / bad ID → 422, unknown ID → 404 |
| Tests | 22 pass; the route-order test fails (`assert 422 == 200`) when `/stats` is moved below the ID route |

## Problems found by running it

1. **Airflow 3's data interval is zero-length**, and CLI runs get `logical_date = None` — fixed with `resolve_window` (`b885747`).
2. **arXiv's announcement delay** — "yesterday" misses late-announced papers forever; an overlapping 5-day window, daily (`e1ebbb5`).
3. **A hidden `batch_size` bug** no check could see — mypy now covers `airflow/dags/`, plus `make check-dags` (`cf79650`).
4. **An always-run report could turn failed runs green** — it now raises on a missing XCom (`830b725`).
5. **A failure test that would pass for the wrong reason** — re-run on a paper outside the window.
6. **`response_model` silently dropped sections** — only a live `curl` showed it (`8cf4a2c`).

## Evidence

- Commits [`b885747…cc5cdd3`](https://github.com/RishabhHM/AI-Research-Assistant/compare/b885747947f7f20a525de1ff1477879c225f43de~1...cc5cdd3ac3470e7f8467be413099bec5e627f340) (Oct 19–23)
- `personal/Documentation/Stage 2 - Data Pipeline.md`, Part 2C and the Stage 2 Wrap-Up

## Next: Stage 3

Search over the ingested papers: OpenSearch BM25 plus vectors.
