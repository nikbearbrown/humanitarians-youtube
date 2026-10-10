# FACTCHECK — research-assistant-part-4

Status: checked 2026-10-09 by Claude against the Stage 2 doc and the code at commit 22f9c6b; awaiting Rishabh's sign-off.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B13 | Stage 1 ended with one sample paper in the database | PASS | seed script; Stage 2 doc Step 4 Verify: 'Total: 527 papers — Seed paper + two real days' | — |
| 2 | B02 | Stage 2: arXiv → metadata → PDFs → parse → Postgres; 2A is metadata only | PASS | Stage 2 doc goal line; Sections table | — |
| 3 | B03 | `.gitignore` had `test_*.py`; tests and the DAG were never committed | PASS | Step 0 'Bug found: tests and the DAG…'; commit 3039e2d diff (excerpt verbatim) | — |
| 4 | B03 | `Paper` redeclared created_at/updated_at, overriding the mixin, so no defaults | PASS | Step 0 'Bug found: the timestamps had no defaults'; commit 511c15d | — |
| 5 | B04 | Four rules; arXiv allows one request every 3 s | PASS | Guiding Principles 1–4 | — |
| 6 | B05 | rate_limit_delay has ge=3.0; a value of 1 fails validation | PASS | src/config.py; tests/test_config.py::test_rate_limit_below_arxiv_minimum_is_rejected | Excerpt drops description= args; labelled on screen |
| 7 | B06 | Three live requests: normal, bad query, old-style ID | PASS | Step 2a 'Real data drove the design' | — |
| 8 | B06 | Versioned IDs would make a revision a second row; stored without version | PASS | Step 2a table row 1; parser._strip_version | — |
| 9 | B06 | Old-style IDs contain a slash; keep everything after /abs/ | PASS | Step 2a table row 2; parser.py partition('/abs/') | — |
| 10 | B06 | Bad query returns HTTP 400 with the reason in an Atom error entry; parser raises with it | PASS | Step 2a table row 4; parser.py | — |
| 11 | B07 | Malformed entry logged and skipped; broken feed raises; tests use a saved real response, no network | PASS | Step 2a 'Error isolation'; tests/fixtures/arxiv_feed.xml | raise message trimmed to '…'; labelled on screen |
| 12 | B08 | One limiter for searches, retries and later PDF downloads; monotonic clock; injected clock/sleep | PASS | Step 2b Decision 2; rate_limiter.py verbatim | — |
| 13 | B09 | Retry timeouts/429/5xx with doubling backoff + jitter; fail fast on 4xx with arXiv's message | PASS | Step 2b Decision 3; client.py _get, _backoff | — |
| 14 | B09 | Backoff 3, 6, 12 s plus up to 1 s jitter, capped at 60 s | PASS | Decision 3; MAX_BACKOFF_SECONDS = 60.0; random.uniform(0, 1) | — |
| 15 | B10 | Sep 1: 243 papers, unique IDs, 3 requests (start=0/100/200), 6.5 s | PASS | Step 2b 'Verify (live)' — recorded result, labelled as recorded | — |
| 16 | B10 | 2.79 s logged gap: log marks response arrival, limiter spaces sends | PASS | Step 2b 'Verify (live)' bullet 2 | — |
| 17 | B11 | create_all never alters existing tables; parsing takes minutes per paper, so a wipe costs hours | PASS | Step 3 'Why are we?' (Docling 2–3 min each) | — |
| 18 | B11 | One-off migrate service; API and Airflow start only after it succeeds | PASS | Step 3 'Who runs migrations?'; compose.yaml service_completed_successfully | — |
| 19 | B12 | One INSERT … ON CONFLICT DO UPDATE per day; atomic; ran twice → 243 rows, all refreshed | PASS | Step 4 Decision + Verify; repositories/paper.py | One line wrapped; labelled on screen |
| 20 | B13 | Manual DAG for any date; ~9 s; 283 papers for Oct 8; 527 total | PASS | Step 4 Verify table; arxiv_ingestion.py target_date param | — |
| 21 | B14 | A loop and a sleep is fine for a one-off demo | EXEMPT | Editorial judgment that bounds the reel's own advice | — |
| 22 | B15 | Verdict lines restate B05–B12 | PASS | as rows above | — |

Omitted by design: reference-code comparisons ('Things Not to Copy') — build framing only; pre-commit/`make lint` mismatch and sync-vs-async, for length.
