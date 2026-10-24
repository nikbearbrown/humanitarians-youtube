# FACTCHECK — research-assistant-part-6-short

Status: checked 2026-10-23 by Claude; every claim is a subset of the parent reel's FACTCHECK.md. Awaiting Rishabh's sign-off.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | S01 | Daily 06:00 UTC: fetch, parse, prune, report | PASS | parent FACTCHECK #1 | — |
| 2 | S02 | Friday-afternoon paper announced Monday evening; 'yesterday' misses it | PASS | parent #3 | — |
| 3 | S03 | Last 5 days every run; overlap free (idempotent) | PASS | parent #4 | — |
| 4 | S04 | 1 active run, 2 retries 30 min apart, timeouts 4 h/6 h, batch of 25 | PASS | parent #5, #1 | — |
| 5 | S05 | A run is green if its last tasks succeed; an always-succeeding report hides failures | PASS | parent #8 | — |
| 6 | S06 | Report checks results, logs, raises; run stays red | PASS | parent #8–9 | — |
| 7 | S07 | API dropped sections via response_model; caught by a live request | PASS | parent #13 | — |
