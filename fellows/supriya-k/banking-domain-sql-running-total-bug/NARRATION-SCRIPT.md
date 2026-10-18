# NARRATION-SCRIPT — banking-sql-running-total-bug

**Format:** CLI-explainer, 12-beat required spine · **Skin:** `claude` (cream/ink/terracotta) ·
**Persona:** none (compliance override — "in for Supriya," no default name, no channel) ·
**Register:** Teardown · **Voice:** Kokoro `af_heart` · **Estimated runtime:** ~190s (~3:10) ·
**Source:** `books/banking-data-analyst-interview-prep/chapters/08-sql-i-balances-cohorts-window-functions.md`
(lines 141–197), `factchecks/MASTER_REPORT.md` (Critical Finding #3).

---

**B00 — INTRO (cold open)**
> In for Supriya. This query runs clean — and it's wrong for any account with a past.

**B01 — PROBLEM (why care)**
> In a bank's data warehouse, "what's this account's balance today" really means "sum every
> posting up to today." Get that running total right, and the report is trustworthy. Get one
> clause out of order, and the query still runs, still returns numbers — and every one of them is
> wrong for any account with history before the reporting window. No error thrown. No warning
> logged. Just a wrong balance that looks completely correct.

**B02 — MECHANISM (the ordering rule)**
> Here's the rule that explains it. A window function runs after WHERE, GROUP BY, and HAVING — but
> only inside its own query. Put that WHERE in an earlier CTE instead, and it still runs first,
> before a SUM() OVER two CTEs downstream ever sees the data. Filter early, and the running total
> built on top never sees what got filtered out.

**B03 — CLI (cycle 1, the ask)**
> Ask Claude to review the chapter's own running-balance query before it ships — six months of
> end-of-month balances, built one CTE at a time.

**B04 — CODE (cycle 1, the buggy query)**
> Here's the CTE that computes the running balance. Read the WHERE clause — it's sitting right
> inside running, filtering the ledger down to twenty-twenty-six before the SUM() OVER ever runs.

**B05 — OUTPUT (cycle 1, the wrong result)**
> Run it against an account that's been open since twenty-twenty-five. The true balance carried
> twelve thousand four hundred dollars into January. This query says January's balance is negative
> three hundred. It didn't error. It just forgot the account had a past.

**B06 — CLI (cycle 2, the required revision)**
> That's a bug, not a feature. The fix is one clause, moved one CTE downstream: pull the date
> filter out of running, and put it on last underscore posting underscore per underscore month
> instead.

**B07 — CODE (cycle 2, the fixed query)**
> Same query, one clause relocated. Running now sees the whole ledger, no WHERE at all. The date
> filter shows up one CTE later — after the sum is already correct, only narrowing which months
> get reported.

**B08 — OUTPUT (cycle 2, the corrected result)**
> Re-run it. January's balance comes back as twelve thousand one hundred dollars — the real prior
> balance, minus the one withdrawal that actually happened in January. Nothing invented. Nothing
> lost.

**B09 — SUMMARY (the lesson)**
> So the bug was never the window function. It was a WHERE clause living one CTE too early.
> Compute the running total over the whole ledger first. Narrow down to your reporting window only
> after the balance is already right.

**B10 — NEXT STEPS (handoff, "Your turn.")**
> Your move: take this prompt, and run it against your own running-balance query. If the date
> filter sits inside the CTE that computes the sum, that's your bug — move it downstream, and
> check it against an account with history older than your reporting window.

**B11 — OUTRO**
> The running-balance bug hiding in a correct-looking SQL query. In for Supriya — building it with
> Claude, then taking it apart.

---

**Word count:** ~470 words across 12 beats. **Pace:** ~2.4–2.5 words/sec at Kokoro's typical rate
(matching the `af_heart` pace observed in the whole-book-trailer project) → **estimated duration
~190s (~3:10)**. Actual per-beat durations lock once `generate_audio_kokoro.py` runs (Gate: "hear
it / lock the clock" — never ship on the word-count estimate).
