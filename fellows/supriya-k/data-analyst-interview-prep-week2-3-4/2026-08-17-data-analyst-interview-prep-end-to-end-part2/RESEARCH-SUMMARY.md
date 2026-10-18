# Research Summary — "The SQL Interview Bug Even a Correct-Looking Query Can Hide"

**Source:** `books/data-analyst-interview-prep/chapters/04-sql-ii.md` (primary),
with a one-beat tie-in to `chapters/07-python-pandas-ai-tools.md`.
Both chapters are part of the signed, fact-checked manuscript
(GATE 4 passed 2026-07-15; `factchecks/MASTER_REPORT.md` — zero errors found).

## Chapter 4 — SQL II: Aggregation, Window Functions, and Problem Patterns

**What's tested here (book's own framing):** "Can you reach past `GROUP BY`
when the question needs per-row context — and can you *name the pattern*
fast, then write it correctly and efficiently."

**CTEs.** A `WITH` clause names an intermediate result so a multi-step query
reads top-to-bottom instead of nesting inside-out. The book recommends CTEs
for anything with two or more logical steps.

**Window functions vs. GROUP BY (the core mechanism).** Quoted directly:
"A window function computes a value for each row using a set of rows,
without collapsing them — unlike aggregation with `GROUP BY`, which
collapses each group to one row." They use an `OVER` clause with optional
`PARTITION BY` (defines the groups) and `ORDER BY` (order within each
group). Functions the book names: `ROW_NUMBER()` (sequential, per
partition), `RANK()` (position **with gaps** for ties), `DENSE_RANK()`
(position, **no gaps** for ties), `LAG()`/`LEAD()`, `SUM() OVER (...)`.

**The recurring patterns (book's table).** Top-N per group →
`ROW_NUMBER()` partitioned by the group, filtered to `rn <= N`. Running
total → `SUM() OVER (ORDER BY ...)`. Month-over-month → `LAG()`. Gaps &
islands → row-number differencing. Deduplication → `ROW_NUMBER()` keep
`= 1`.

**The book's own worked example (Loopr, for context — not what this video
builds).** Schema: invented streaming service Loopr, table
`plays(user_id, track_id, played_at)`. The book's worked question is "find
each user's **2nd**-most-played track," solved correctly with
`ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY plays DESC) AS rn ...
WHERE rn = 2`. The book notes: "why a naive `GROUP BY` fails: grouping
collapses each user to one row, so there's no way to point at 'the 2nd' —
you need per-row ranking *within* the user."

**Exercise 3 (Chapter 4) — the scenario this video dramatizes, verbatim:**
"A candidate's 'top track per user' query uses `RANK()` and returns two
rows for users with a tie. Find the bug and fix it so exactly one row
returns per user."

This is a real, book-specified bug-and-fix problem, distinct from (but
built on) the book's own worked "2nd-most-played" example: same schema,
same partition-by-user idea, but "top track" (rn/rnk = 1) instead of "2nd
track" (rn = 2), and it's explicitly about what happens when `RANK()` hits
a tie — which the worked example's data apparently never does, so the bug
never surfaces there. `RANK()` gives every tied row the **same** rank
(with a gap afterward, per the book's own function table), so if two
tracks tie for a user's most-played, both get rank 1 and both survive a
`WHERE rnk = 1` filter — the query "runs" but returns the wrong number of
rows for that user.

**MySQL version note (book, footnoted/confirmed):** MySQL 8.0+ is assumed
throughout — CTEs arrived in 8.0.1, window functions in 8.0.2 (verified
CONFIRMED against dev.mysql.com in the book's fact-check).

## Chapter 7 tie-in (one SUMMARY beat only, not a second topic)

Chapter 7 ("Python & pandas for Analysts (+ AI Tools)") states the book's
2026 AI-tool-judgment position, quoted: "Lean on it for boilerplate, syntax
recall, and first drafts. Read it line by line when correctness matters —
AI output can pass a surface smell test and still be subtly wrong (a filter
applied after an aggregation, a silent type coercion)." This video's whole
demonstration — a query that runs cleanly and still returns the wrong
number of rows on a tie — is the SQL-flavored version of exactly that
warning, so the SUMMARY beat draws the line explicitly and briefly. This is
not a new topic; it is one sentence connecting back to material already in
the book.

## What this video adds that is NOT a new invented fact

The book's Exercise 3 states the bug scenario in the abstract ("a
candidate's query… returns two rows for users with a tie"). To make the
"moving output" concretely demonstrable and *verifiable*, this video
supplies:
1. The full buggy SQL and full fixed SQL (straightforward, standard MySQL
   window-function syntax — not a book fact, but not a claim either; it's
   the code the exercise describes).
2. A small set of illustrative sample rows for Loopr's *already-invented*
   `plays` table (three users, one with a genuine tie) so the "2 rows for
   a tied user" and "1 row after the fix" outcomes are concrete numbers a
   viewer can check by hand. Loopr and its schema are the book's own
   invented company — sample data consistent with an invented company is
   not a new real-world fact. See `SOURCES-FACTCHECK.md` for the full
   worked derivation of both query results.
