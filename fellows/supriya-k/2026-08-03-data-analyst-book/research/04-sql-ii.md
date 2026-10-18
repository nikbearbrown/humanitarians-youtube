# Research — Ch. 4: SQL II (Aggregation, Window Functions, Patterns)

*Phase 1 notes and sources. No chapter prose. MySQL target dialect (window functions require MySQL 8.0+).*

## Key claims & sources

- **A window function computes a value for each row using values from one or multiple rows, without collapsing rows** (unlike aggregate functions with GROUP BY, which collapse groups into one row).
  Source: Wikipedia, "Window function (SQL)," https://en.wikipedia.org/wiki/Window_function_(SQL) (accessed 2026-07-15). *Tertiary/secondary reference.*
- **Window functions are evaluated after GROUP BY aggregation**, and use an `OVER` clause with optional `PARTITION BY` and `ORDER BY`. If `PARTITION BY` is omitted, the whole result set is one partition.
  Source: Wikipedia, "Window function (SQL)" (as above).
- **Common window functions:** `ROW_NUMBER` (sequential numbering), `RANK` (positions with gaps for ties), `DENSE_RANK` (no gaps), `LAG`/`LEAD` (previous/next row values), and running aggregates (`SUM`/`AVG`/`COUNT` over an ordered frame).
  Source: Wikipedia, "Window function (SQL)" (as above).
- **Window functions entered the SQL standard in SQL:2003**; support rolled out across major databases over time.
  Source: Wikipedia, "Window function (SQL)" (as above).

## Interview-craft (editorial)
- Recurring SQL problem patterns to teach: top-N-per-group, running totals, month-over-month, gaps/islands, deduplication. *(Editorial framing — patterns are widely taught; specific phrasing is original.)*
- Common wrong answer: filtering on an aggregate in `WHERE` instead of `HAVING`; using `GROUP BY` where a window function is needed (loses row detail).

## MySQL specifics to confirm during drafting
- **[UNVERIFIED]** MySQL 8.0 CTE syntax (`WITH`) and exact window-function support/edge cases — confirm against MySQL 8.0 reference manual at draft time.

## Original worked-example dataset
- "Loopr" streaming service (`plays`: user_id, track_id, played_at) — fully invented.

## [UNVERIFIED] list
- MySQL 8.0 CTE/window syntax specifics (confirm against official docs when writing examples).
