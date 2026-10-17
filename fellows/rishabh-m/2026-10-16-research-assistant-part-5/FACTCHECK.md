# FACTCHECK — research-assistant-part-5

Status: checked 2026-10-16 by Claude against the Stage 2 doc (Part 2B) and the code at commit 10d074b; awaiting Rishabh's sign-off.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B07 | 527 papers had metadata and were queued for PDF processing | PASS | 2B Step 7a Decision 5 ('all 527 papers were queued automatically'); Verify 'pending 527' | — |
| 2 | B02 | Flow: pending → download → Docling → sections in Postgres; failures recorded per paper | PASS | Part 2B Result line | — |
| 3 | B03 | Downloads use the shared rate limiter (_get); size cap; bytes must start with %PDF-; arXiv can send HTML with 200 | PASS | Step 5 Decisions 1–2; client.py download_pdf | Docstring dropped, messages trimmed with …; labelled |
| 4 | B04 | Cache one file per paper version; temp file in same folder then os.replace; mkstemp 0600 found from real output | PASS | Step 5 Decisions 3–4; pdf_cache.py; '0600 … found from real output' | Comments trimmed; labelled |
| 5 | B05 | API image 421 MB without Docling; Airflow 7.54 GB with models baked in; HF_HUB_OFFLINE=1; Docling looked in the wrong folder | PASS | Step 6 Verify (421 MB / 7.54 GB); Step 6b 'Checked in the real Airflow container' | — |
| 6 | B05 | Without the flag the first run would download 1.4 GB | PASS | Step 6b: 'would have quietly downloaded 1.4 GB' | — |
| 7 | B06 | Reading order via iterate_items; tables as Markdown | PASS | Step 6b; pdf_parser._sections verbatim (lines 66–77) | — |
| 8 | B06 | BERT: 16 pages, 31 sections, 6 with tables, ~28 s | PASS | Step 6b Verify (inside Airflow) | — |
| 9 | B06 | Docling chosen for structured documents; no local benchmark run; comparison script ready | PASS | Step 6a ('No local benchmark was run'; compare_parsers.py ready) | — |
| 10 | B07 | Statuses pending/parsed/failed/skipped; failed retried up to 3 attempts; too large skipped | PASS | Step 7a table; Step 7 Decision 2; max_attempts default 3 | — |
| 11 | B08 | Autogenerate doesn't detect CHECK constraints; added by hand | PASS | Step 7a 'The migration'; 657e3da8defb line 32 | — |
| 12 | B08 | migrate image had copied old migrations; 'Can't locate revision'; nothing started; rule: rebuild | PASS | Step 7a 'Gotcha: the database was newer than the migrate image' | — |
| 13 | B09 | Per-paper try; no session open during parse; skipped vs failed; broad except only at the item boundary; all-failed raises | PASS | Step 7 Decisions 1–2 + notes; processing.py lines 33–53 | Lines omitted/trimmed with …; labelled |
| 14 | B10 | New pdf_url resets status to pending and attempts to 0 | PASS | Step 7 Decision 3; paper.py lines 58–69 verbatim | — |
| 15 | B11 | pdf_limit 3: three newest parsed in ~1.5 min, 24/38/44 sections; fake 2609.99999v1 → run failed, failed, 1 attempt, HTTP 404 | PASS | Step 7 Verify table | — |
| 16 | B12 | ~30–45 s per paper; ~250 papers a day; ~2–3 h of CPU; pdf_limit parameter | PASS | Step 7 Decision 4 | — |
| 17 | B13 | Abstracts come with the metadata | PASS | 2A: abstract column stored at ingestion | — |
| 18 | B13 | Skip PDFs when only abstracts are needed | EXEMPT | Editorial judgment bounding the reel's own advice | — |
| 19 | B14 | Verdict lines restate B03–B11 | PASS | as rows above | — |

Omitted by design: reference-code comparisons ('Things Not to Copy') — build framing only; the YAML volume typo and `docker compose cp` permissions, for length.
