# FACTCHECK — research-assistant-part-4-short

Status: checked 2026-10-09 by Claude; every claim is a subset of the parent reel's FACTCHECK.md. Awaiting Rishabh's sign-off.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | S00, S07 | The database held one sample paper before Stage 2A | PASS | parent FACTCHECK #1 | — |
| 2 | S01 | Four rules | PASS | parent FACTCHECK #5 (Guiding Principles 1–4) | — |
| 3 | S02 | Delay has a 3.0 s floor; 1.0 s fails validation | PASS | parent FACTCHECK #6; src/config.py ge=3.0 | — |
| 4 | S03 | IDs carry a version (stripped, else duplicate rows); old IDs have a slash (keep after /abs/) | PASS | parent FACTCHECK #8–9 | — |
| 5 | S04 | One limiter for searches, retries and later PDFs | PASS | parent FACTCHECK #12 | — |
| 6 | S05 | One upsert per day; ran Sep 1 twice, still 243 rows | PASS | parent FACTCHECK #18 | — |
| 7 | S06 | Migrations run once in their own container; nothing starts until it succeeds | PASS | parent FACTCHECK #17 | — |
| 8 | S07 | Manual DAG ran the same code; 527 papers | PASS | parent FACTCHECK #19 | — |
