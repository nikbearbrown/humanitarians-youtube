# FACTCHECK — research-assistant-part-6

Status: checked 2026-10-23 by Claude against the Stage 2 doc (Part 2C) and the code at commit 1e40dfb; awaiting Rishabh's sign-off.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | Daily 06:00 UTC: fetch last 5 days → parse batch of 25 → prune >14 days → report | PASS | 2C Result line; Steps 8–11 (lookback_days 5, batch_size 25, cache_retention_days 14) | — |
| 2 | B03 | Airflow 3.3.2: a scheduled run's data interval is zero length | PASS | Step 8 'Checked first' table (checked with next_dagrun_info) | — |
| 3 | B03 | Papers appear only once announced; Friday after 14:00 ET → announced Monday 20:00 ET; a 'yesterday' run misses them | PASS | Step 8 'The real cause of gaps' | — |
| 4 | B04 | Lookback of 5 days; Tuesday run reaches Friday; extra day for holidays; ~45 s of fetching; overlap free (idempotent upsert) | PASS | Step 8 Decision; ingestion.resolve_window lines 31–35 verbatim | — |
| 5 | B05 | Daily incl. weekends at 06:00 UTC after announcements; max_active_runs=1; 2 retries 30 min apart; timeouts 4 h / 6 h | PASS | Step 9 table; arxiv_ingestion.py @dag | Comments trimmed, … = lines omitted; labelled |
| 6 | B06 | Hidden bug: batch_size setting missing; with pdf_limit empty every scheduled run would crash; mypy only checked src/; now checks airflow/dags/; proven with a typo | PASS | Step 9 'The hidden bug caught here'; Step 12 | — |
| 7 | B07 | Cache files older than 14 days deleted; trigger_rule all_done so cleanup runs after failures | PASS | Step 10 Decision + code | — |
| 8 | B08 | Airflow marks a run successful if its leaf tasks succeeded; report reads XComs; missing value = failed; logs then raises | PASS | Step 11 Decisions 2–3 | — |
| 9 | B09 | Report excerpt; retries=0 on the report | PASS | arxiv_ingestion.py lines 101–102, 124–126 | One line wrapped; labelled |
| 10 | B10 | Recorded report (logical date Oct 22, pdf_limit 1): 1190 papers Oct 17–22; parsed 1; files_deleted 1; queue parsed 31 / pending 2924 / skipped 4; retries exhausted 0 | PASS | Step 11 Verify — recorded log, labelled as recorded | — |
| 11 | B11 | Failure run: broken URL on a paper outside the window; parse failed; prune ran; report logged FAILED and raised; run failed | PASS | Step 11 Verify failure-run table | — |
| 12 | B12 | List stays a list with pdf_status; sections only on detail via undefer; stats reuse report queries; /stats before /{arxiv_id}; route-order test fails with 422 when moved | PASS | Step 13 Decisions 1–3; Step 14 test notes; papers.py routes | Comment trimmed, … = lines omitted; labelled |
| 13 | B13 | Detail route kept response_model=PaperResponse; FastAPI filtered sections out silently; only a live check caught it | PASS | Step 13 'Gotcha: response_model silently filters' | — |
| 14 | B14 | Skip schedule/window/report for a script run by hand | EXEMPT | Editorial judgment bounding the reel's own advice | — |
| 15 | B15 | Verdict lines restate B03–B13 | PASS | as rows above | — |

Omitted by design: reference-code comparisons ('Things Not to Copy') — build framing only; the end-of-Stage-2 totals and later-dated runs in the doc.
