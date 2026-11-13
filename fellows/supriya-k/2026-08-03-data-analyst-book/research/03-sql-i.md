# Research — Ch. 3: SQL I (Querying, Filtering, Joins)

*Phase 1 notes and sources. No chapter prose. MySQL is the target dialect.*

## Key claims & sources

- **SQL is a domain-specific language for managing data in a relational database (RDBMS).**
  Source: Wikipedia, "SQL," https://en.wikipedia.org/wiki/SQL (accessed 2026-07-15). *Tertiary/secondary reference.*
- **SQL statements group into sublanguages: DQL (query, e.g. SELECT), DDL, DML, DCL.** Common keywords: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, WHERE.
  Source: Wikipedia, "SQL" (as above).
- **SQL dialects differ across vendors** — date/time syntax, string concatenation, NULL handling, identifier case sensitivity — so code rarely ports unchanged between engines. *(Justifies standardizing the book on MySQL.)*
  Source: Wikipedia, "SQL" (as above).
- **INNER JOIN** returns only rows with matching values in both tables; unmatched rows are excluded.
  Source: Wikipedia, "Join (SQL)," https://en.wikipedia.org/wiki/Join_(SQL) (accessed 2026-07-15). *Tertiary/secondary reference.*
- **LEFT (OUTER) JOIN** returns all rows from the left table plus matching right-table rows; unmatched right columns are NULL.
  Source: Wikipedia, "Join (SQL)" (as above).
- **RIGHT (OUTER) JOIN** is the inverse: all rows from the right table plus matching left rows; unmatched left columns are NULL.
  Source: Wikipedia, "Join (SQL)" (as above).
- **Self-join** = joining a table to itself, using aliases to distinguish the two references.
  Source: Wikipedia, "Join (SQL)" (as above).

## Interview-craft (editorial, not sourced fact)
- The screen grades *logic and communication*, not just whether the query runs (see `../blueprint-trends-notes.md`, sourced).
- Recurring skill: translating a plain-English ask into SQL and narrating join choice aloud.

## MySQL specifics to confirm during drafting
- **[UNVERIFIED]** Exact MySQL syntax details (backtick identifiers, `LIMIT n`, `WHERE` vs `HAVING` order) — confirm against MySQL 8.0 reference manual (dev.mysql.com) when drafting examples.

## Original worked-example dataset
- "FreshCrate" meal-kit schema (`customers`, `orders`, `order_items`) — fully invented; no external source needed.

## [UNVERIFIED] list
- MySQL 8.0 exact function/syntax details (to confirm against official MySQL docs at draft time).
