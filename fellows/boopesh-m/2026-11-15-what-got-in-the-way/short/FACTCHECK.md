# FACTCHECK — What Got in the Way (Short)

Same facts as the 16:9 film; full evidence in [`../FACTCHECK.md`](../FACTCHECK.md), numbers from
`../code/results.json` (`python3 ../code/week_stats.py`, `origin/main` = `dc2963ec`, Nov 8–14 America/New_York).

| Beat | Claim | Evidence | Status |
|---|---|---|---|
| B00/B10 | 31 frictional logs describe obstacles (of 32 added) | `friction.logs_describing_obstacles` | ✅ |
| B10 | Top themes (rough keyword sort, out of 31): layout & picture checks 19, facts & data 11, length & time 10, tools & setup 10 | `friction.theme_logs`; heuristic, said as "my rough sort" | ✅ (approximate by design) |
| B20 | 17 of 31 logs: a problem found by watching the cut, viewing frames or re-reading the words | `friction.found_by_looking_logs` (keyword rule `LOOKED`) | ✅ (approximate by design) |
| B30 | What the Fellows Taught 2:15 + Short 0:50; The Backtest Mirage 2:24 + Short 0:45; 4K; delivered for review | ffprobe of the files in `weekly-submission/` (`boopesh.last_week_deliveries`); no Drive claim | ✅ |
| B30 | His obstacle is access; pull request pending | `fellows/boopesh-m` not on `dc2963ec`; failed fork is Boopesh's own report | ✅ / ⚠️ fork from Boopesh |
