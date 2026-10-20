# Sources & Fact-Check — banking-sql-running-total-bug

**Source chapter:** `books/banking-data-analyst-interview-prep/chapters/08-sql-i-balances-cohorts-window-functions.md`, lines 141–197.
**Source fact-check entry:** `books/banking-data-analyst-interview-prep/factchecks/MASTER_REPORT.md`, Critical Finding #3 ("[CORRECTED — real SQL bug] Ch. 8 — worked example running-balance CTE").

---

## Claim-by-claim trace

| # | Claim (as narrated / shown on screen) | Source | Verdict |
|---|---|---|---|
| 1 | "What's this account's balance today" really means "sum every posting up to today" (B01) | Chapter line 38: *"The recurring prompt is some version of 'what was this account's balance as of date X?' — which is really 'sum every posting up to and including X.'"* | CONFIRMED — direct paraphrase |
| 2 | The book's real query is a 3-CTE (plus a 4th for dormancy) structure: `running` → `last_posting_per_month` → `monthly_balances` → `dormant_flag` (B04, B07 code beats) | Chapter lines 144–184, verbatim SQL | CONFIRMED — quoted/trimmed directly from the manuscript |
| 3 | The buggy version filters `WHERE posted_at >= '2026-01-01' AND < '2026-07-01'` **inside** the `running` CTE, before `SUM() OVER` runs (B04) | `MASTER_REPORT.md` Critical Finding #3: *"The `running` CTE filtered transactions to the Jan–Jun 2026 reporting window before computing the cumulative `SUM() OVER`"* | CONFIRMED — this is the exact bug the fact-check phase found and the book fixed; the buggy version shown on screen is a reconstruction of the pre-fix state, not invented |
| 4 | The bug silently truncates balance history for any account with pre-2026 activity — no error, no warning (B01, B05) | `MASTER_REPORT.md`: *"which would silently truncate balance history for any account with pre-2026 activity — the 'end-of-month balance' would be wrong"*; chapter line 197: *"That produces a number that looks like a balance but is really 'net change since January,' which is silently wrong for any account with pre-2026 history."* | CONFIRMED |
| 5 | The fix: move the date filter out of `running`, into `last_posting_per_month`, so `SUM() OVER` sees the entire ledger first (B06, B07, B09) | `MASTER_REPORT.md`: *"Fixed by moving the date filter downstream of the running-total computation"*; chapter line 197: *"The fix is to let `SUM() OVER` see the entire ledger... and only narrow down to 'which months am I reporting' one CTE later, after the balance is already correct."* | CONFIRMED — this is the book's actual shipped fix, quoted directly |
| 6 | The fixed query shown in B07 is the book's real, current, shipped query | Chapter lines 144–172 (current manuscript state) | CONFIRMED — this is not a "corrected-for-video" rewrite, it's the query as it exists in the book today |
| 7 | General rule: a window function's evaluation happens after `WHERE`/`GROUP BY`/`HAVING` *within its own query* (B02, B09) | Chapter line 116: *"window functions are evaluated after WHERE, GROUP BY, and HAVING, and before ORDER BY/LIMIT/DISTINCT... A window-computed column doesn't exist yet at the point WHERE is evaluated"* | CONFIRMED — the video's extension of this rule to "a WHERE in an earlier CTE still runs first" is a direct, correct corollary of the cited rule, not a new claim |

---

## What is new here (not in the book, and why it's not a fabricated fact)

The book's own worked example doesn't include specific sample account/transaction rows or dollar
figures — it's schema + query + prose. For B05 and B08 (the OUTPUT beats), this video needed
concrete numbers to show a wrong result versus a corrected one. Per `VISUAL-PLAN.md`, the sample
data is:

- One fictional account, `ACCT-50231`, with a $12,400.00 deposit on 2025-11-03 (before the
  reporting window) and three small 2026 postings.
- All dollar amounts, dates, and the account ID are **invented for illustration**, hand-computed
  under both the buggy and fixed query logic (arithmetic shown in `VISUAL-PLAN.md`), and clearly
  labeled as a sample in the video's own visual (a fictional account ID, never presented as a real
  bank record). This mirrors the book's own convention of inventing companies/portfolios for
  practice material — no real institution, account, or customer is referenced.

No other narrated or on-screen claim in this video is new relative to the two source documents
above.

## Original-questions rule

This video does not introduce a new interview question or exercise — it walks through a real bug
found during this book's own fact-check phase, using the book's real (fixed) query as the "after."
The "before" (buggy) query is a faithful reconstruction of the pre-fix state as documented in
`MASTER_REPORT.md`, not an invented defect.

## No paid services

Kokoro (local, free) for narration; Manim (local, free) for the 5 animated data/mechanism beats;
Remotion (local, free, already-installed `node_modules`) for the 7 composer/code/outro beats. No
ElevenLabs, no Higgsfield, no paid API calls anywhere in this build.
