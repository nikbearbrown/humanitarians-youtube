# RESEARCH-SUMMARY — banking-domain-interview-end-to-end-v2

## Source

- `books/banking-data-analyst-interview-prep/book.md` — the six-part outline (Landscape,
  Regulation/Risk/Governance, Modern Data Stack, Technical Prep, Behavioral/Case/Systems, Day-Of).
- `books/banking-data-analyst-interview-prep/chapters/08-sql-i-balances-cohorts-window-functions.md`,
  lines 100–197 (the running-balance worked example — same source `banking-domain-sql-running-total-bug`
  used, shown here in its correct, shipped form — no bug reconstruction in this reel).
- `books/banking-data-analyst-interview-prep/chapters/09-sql-ii-charge-off-waterfalls-vintage-curves.md`,
  lines 155–206 (the Harborline Card Co. vintage-curve worked example).

## The book's own pitch (quoted, this is what B00/B01 compress)

> "A detailed, interview-ready guide for Data Analyst candidates targeting US banks, fintechs, and
> financial services firms — covering the regulatory landscape, core banking products and metrics,
> the modern banking data stack, SQL and Python patterns on financial data, and the behavioral and
> case interview scenarios asked in 2026." (`book.md`, One-Sentence Pitch)
> "A data analyst with 2–6 years of experience preparing for US banking / financial services
> interviews." (`book.md`, The Reader)

## The six-part map (quoted, this is what B02/B09 draw)

> "Part I — US Banking Landscape... Part II — Regulation, Risk, Governance... Part III — Modern
> Banking Data Stack... Part IV — Technical Prep: 40+ SQL problems... Python for banking... Part V
> — Behavioral, Case, Systems... Part VI — Day-Of: glossary, acronyms, ratio cheat sheets, one-page
> reg reference." (`book.md`, High-Level Outline)

## Worked example 1 — Ch. 8 running balance (quoted, the CORRECT/shipped query — B03–B05)

> "Notice *where* the date filter lives: it's on `last_posting_per_month`, not on `running`...
> The fix is to let `SUM() OVER` see the *entire* ledger (no `WHERE` in `running`) so the running
> total is always the true cumulative balance, and only narrow down to 'which months am I
> reporting' one CTE later, after the balance is already correct." (chapter, line 197)

This reel shows the query in its already-correct, shipped state — unlike
`banking-domain-sql-running-total-bug`, which reconstructs the pre-fix buggy state as its subject.
No bug is reconstructed here.

## Worked example 2 — Ch. 9 vintage curve (quoted — B06–B08)

> "Build a charge-off waterfall showing, for the January 2025 cohort, what % of accounts are in
> each DPD bucket at 3, 6, and 9 months on book." (chapter, "Worked example — Harborline Card Co.")
> "A plain `GROUP BY snapshot_month, dpd_bucket` alone would answer a different, calendar-month
> question — it can't tell you what happened to *this* cohort specifically, because the
> origination-month filter and the `months_on_book` computation are what anchor every row back to
> January 2025." (chapter, same section)

## What this video adds that is NOT a new invented fact

- **Sample ledger data for `ACCT-50231`** (B05's output numbers) — reused verbatim from
  `banking-domain-sql-running-total-bug/VISUAL-PLAN.md`, not re-invented. Same fictional account,
  same four transactions, same hand-traced arithmetic.
- **Sample cohort percentages for Harborline Card Co.'s January 2025 cohort** (B08's output
  numbers) — invented for illustration since the chapter's own worked example doesn't include
  sample bucket counts. Fully fictional counts, hand-computed to sum to 100% per months-on-book
  column, disclosed in `VISUAL-PLAN.md`. Same license the book itself uses for its own practice
  scenarios (original companies, portfolios, datasets).
- **The framing "two moves, same discipline"** (B09) linking Ch. 8's evaluation-order rule to
  Ch. 9's cohort-preservation rule — a direct comparison of two rules the book states
  independently, not a new claim about either.

Nothing else in the narration, on-screen code, or visual beats introduces a fact not already
present in `book.md` or the two chapters cited above.
