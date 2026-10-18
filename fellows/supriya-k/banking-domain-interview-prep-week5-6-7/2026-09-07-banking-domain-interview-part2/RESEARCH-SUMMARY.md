# RESEARCH-SUMMARY — banking-sql-running-total-bug

## Source

- `books/banking-data-analyst-interview-prep/chapters/08-sql-i-balances-cohorts-window-functions.md`, lines 141–197 (the worked example, current/shipped state).
- `books/banking-data-analyst-interview-prep/factchecks/MASTER_REPORT.md`, Critical Finding #3.

## The book's own mechanism explanation (quoted, this is the general rule the video teaches)

> "One rule explains a whole class of 'why won't my query run' bugs: window functions are
> evaluated *after* `WHERE`, `GROUP BY`, and `HAVING`, and *before* `ORDER BY`/`LIMIT`/`DISTINCT`.
> A window-computed column doesn't exist yet at the point `WHERE` is evaluated, so you cannot
> filter on it directly in the same query — it has to be computed in a subquery or CTE and
> filtered in an outer `WHERE`, exactly like the `rn = 1` pattern above." (chapter line 116)

## The exact bug and fix (quoted verbatim from the chapter)

> "Notice *where* the date filter lives: it's on `last_posting_per_month`, not on `running`. That
> ordering is not cosmetic. If the `WHERE posted_at >= '2026-01-01'` bound were applied inside the
> `running` CTE instead — filtering the ledger down to 2026 H1 *before* the cumulative
> `SUM() OVER` runs — every account's running total would start from zero on January 1 instead of
> carrying forward whatever it actually held at the end of 2025. That produces a number that looks
> like a balance but is really 'net change since January,' which is silently wrong for any account
> with pre-2026 history. The fix is to let `SUM() OVER` see the *entire* ledger (no `WHERE` in
> `running`) so the running total is always the true cumulative balance, and only narrow down to
> 'which months am I reporting' one CTE later, after the balance is already correct." (chapter
> lines 197)

## The fact-check phase's own record of this bug (quoted verbatim)

> "[CORRECTED — real SQL bug] Ch. 8 — worked example running-balance CTE. The `running` CTE
> filtered transactions to the Jan–Jun 2026 reporting window *before* computing the cumulative
> `SUM() OVER`, which would silently truncate balance history for any account with pre-2026
> activity — the 'end-of-month balance' would be wrong. Fixed by moving the date filter downstream
> of the running-total computation, with added prose explaining why the ordering matters."
> (`MASTER_REPORT.md`, Critical Finding #3)

## The full query, both states (from the chapter, lines 144–192)

The book shows only the **fixed** query in the current manuscript (the buggy state was already
corrected by the time of publication). This video reconstructs the buggy state by moving the exact
same `WHERE posted_at >= '2026-01-01' AND posted_at < '2026-07-01'` clause from
`last_posting_per_month` (where it lives in the shipped book) into `running` (where the fact-check
report says it used to live) — a faithful, documented reconstruction, not an invented defect. Full
SQL for both states is reproduced in `beat_sheet.json` beats B04 (buggy) and B07 (fixed), trimmed
per the ACTUAL-CODE LAW.

## What this video adds that is NOT a new invented fact

- **Sample ledger data** for account `ACCT-50231` (one 2025 deposit, three 2026 postings) — needed
  to show a concrete wrong-vs-right result on screen, since the book's own worked example doesn't
  include sample rows. Fully invented, clearly fictional account ID, hand-traced arithmetic shown
  in `VISUAL-PLAN.md`. This is the same license the book itself uses for its own practice
  scenarios (original companies, portfolios, and datasets, per the book's own non-goals: "not a
  question dump — all practice scenarios are original").
- **The general framing** "a WHERE in an earlier CTE still runs before a SUM() OVER two CTEs
  downstream" (B02, B09) — this is a direct, correct corollary of the book's own cited evaluation-
  order rule (chapter line 116), not a new claim requiring independent verification.

Nothing else in the narration, on-screen code, or visual beats introduces a fact not already
present in the two source documents above.
