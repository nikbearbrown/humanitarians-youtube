# Stage 2B — PDF processing: download, parse with Docling, save

**Week:** 12–16 Oct 2026 · logged 2026-10-16
**Project:** AI Research Assistant — production RAG over arXiv papers
**Repository:** https://github.com/RishabhHM/AI-Research-Assistant
**Evidence of commit:** [`10d074b`](https://github.com/RishabhHM/AI-Research-Assistant/commit/10d074b4324e2b00eb8546eefcb25f3d12509873)

- **Drive:** https://drive.google.com/drive/folders/1rca04Q1xJCdidYSC3QelYdoodXrX9G1H
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `research-assistant-part-5.mp4` (16:9, 4:51) · `short/research-assistant-part-5-short.mp4` (9:16, 1:20)
- **Previous stage:** [Stage 2A](../2026-10-09-research-assistant-part-4/)

## What this stage was for

2A filled `papers` with real arXiv metadata. 2B turns each paper's PDF into text:
`pending` papers get their PDF downloaded (rate-limited, cached on disk), parsed by Docling
inside Airflow, and saved as sections. Every failure is recorded on its own paper.
**Flow:** `ingest_metadata` → `process_pdfs`.

## What was built

| File | What it does |
|---|---|
| `src/services/arxiv/client.py` | `download_pdf`: through the shared rate limiter and retries; size cap; bytes must start with `%PDF-` (arXiv can send HTML with 200). |
| `src/services/pdf_cache.py` | One file per paper *version*; temp file in the same folder, then `os.replace`; mode set to 0644. |
| `airflow/`, `compose.yaml` | Docling 2.144.0 only in the Airflow image (uv `pipeline` group), models baked in at build time, `HF_HUB_OFFLINE=1`, a `pdf_cache` named volume. |
| `src/services/pdf_parser.py` | `DoclingParser`: one converter per run, `page_range` truncation, reading order with tables as Markdown, one `PdfParseError`. |
| `src/models/paper.py`, `migrations/…/657e3da8defb` | `pdf_status` (pending / parsed / failed / skipped, `VARCHAR` + `CHECK`), `pdf_attempts`, `pdf_error`, `pdf_processed_at`, `parser_version`, `sections` (JSONB, deferred). |
| `src/repositories/paper.py` | `get_pending_pdfs`, `mark_pdf_parsed/failed`; `upsert_many` resets status when the PDF version changes. |
| `src/services/processing.py` | Queue → download/parse → per-paper result in its own short transaction; all-failed raises. |
| `airflow/dags/arxiv_ingestion.py` | New `process_pdfs` task and a `pdf_limit` param. |
| `personal/eval/compare_parsers.py` | pypdf vs Docling comparison — ready, not run. |

## Results

| Measure | Value |
|---|---|
| Papers queued by the migration | 527 (`server_default 'pending'`) |
| BERT parse inside Airflow | 16 pages, 31 sections, 6 with tables, ~28 s |
| Images | API 421 MB (no Docling) · Airflow 7.54 GB (was 3.22 GB) |
| Happy path (`pdf_limit = 3`) | run succeeded in ~1.5 min; 3 newest papers parsed (24, 38, 44 sections) |
| Failure test (`2609.99999v1`) | run failed as designed; row `failed`, 1 attempt, HTTP 404 |
| Version reset | same URL keeps status; new version → `pending`, attempts 0 |
| Capacity | ~30–45 s per paper → ~2–3 h of CPU for a day of cs.AI |

## Problems found by running it

1. **`Permission denied` on the new volume** — the mount point didn't exist in the image, so Docker created it as root.
2. **"Writable" didn't prove a volume** — the mount line was missing; `mount | grep` is the real check (`9e1ba6d`).
3. **`LocalEntryNotFoundError` with `HF_HUB_OFFLINE=1`** — Docling's models live in its own folder; pass `artifacts_path` (`e3b7bcc`).
4. **`Can't locate revision '657e3da8defb'`** — the `migrate` image copies migrations at build time; `make build` first.
5. **Autogenerate missed the CHECK constraint** — added by hand (`aaf7f21`).
6. **527 still `pending`** — the only run was the old DAG version; triggering the new one fixed it.

## Evidence

- Commits `f24bfa8` … `10d074b` (Oct 12–15) — [`f24bfa8…10d074b`](https://github.com/RishabhHM/AI-Research-Assistant/compare/f24bfa86f43ea8084a88e17e337bd1454b238cb6~1...10d074b4324e2b00eb8546eefcb25f3d12509873)
- `personal/Documentation/Stage 2 - Data Pipeline.md`, Part 2B (Verify sections hold the results above)

## Next: 2C (19–23 Oct)

The daily schedule (logical date, data intervals, no weekend gap, a fallback for manual runs), retries and
`max_active_runs`, a run report, the API (`PaperSummary`, status filter, detail endpoint, `/papers/stats`), and tests.
