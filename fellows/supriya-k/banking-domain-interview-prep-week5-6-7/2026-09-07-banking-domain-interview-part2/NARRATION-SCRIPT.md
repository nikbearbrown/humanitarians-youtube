# Narration Script — "The Running-Balance Bug Hiding in a Correct-Looking SQL Query"

cli-explainer · v3 (2026-10-16, branch banking-reels-v3) · 12 beats · 424 words · ~156s estimated at v1's per-beat pace · Voice: Kokoro `af_bella` ("Bella") · Narrator identity: **Supriya**

v1 (453 words, 167.7s) is the baseline commit 516aeb8. Same 12 beat ids and cli-explainer spine. Every number on screen now comes from a real run of `sql/` (see `FACTCHECK.md`, "v3 corrections").

---

**B00** (INTRO). Hi, I am Supriya and this video is about the running-balance bug hiding in a correct-looking SQL query. It runs clean, and it's wrong for any account with a past.

**B01** (PROBLEM). In a bank's data warehouse, "what's this account's balance today" really means "sum every posting up to today." Get that running total right, and the report is trustworthy. Get one clause out of order, and the query still runs and still returns numbers, but they're wrong for any account with history before the reporting window. No error. No warning.

**B02** (PROBLEM (the rule)). Here's the rule behind it. A window function runs after WHERE in the same query. So when the date filter sits in the same CTE as SUM() OVER, the sum only sees the rows that survived the filter. Everything posted before the window is gone before the total starts counting.

**B03** (CLI — cycle 1). So ask Claude to review a running-balance query before it ships: end-of-month balances for the first half of twenty twenty-six, built one CTE at a time.

**B04** (CODE). Here's the draft. Read the WHERE clause. It sits inside running, the same CTE as SUM() OVER, so the ledger is cut down to twenty twenty-six before the sum runs.

**B05** (OUTPUT). Run it on a Cascade Savings account that carried twelve thousand four hundred dollars into January. The query says January ended at minus three hundred. That's not a balance. It's the net change since January, and nothing warned you.

**B06** (CLI — cycle 2 (revision)). That's the bug. The fix moves one clause: take the date filter out of running, and put it on the next CTE, last posting per month.

**B07** (CODE (fixed)). Running now has no WHERE at all, so the sum sees the whole ledger. The same date filter sits one CTE later, after the balance is already right, and only narrows which months get reported. Nothing else changes.

**B08** (OUTPUT (fixed)). Run it again. January ends at twelve thousand one hundred dollars: the real prior balance, minus the one January withdrawal. Nothing invented, nothing lost.

**B09** (SUMMARY). So the bug was never the window function. It was a filter applied before the sum. Compute the running total over the whole ledger first, and narrow to your reporting window only after the balance is right.

**B10** (NEXT STEPS / HANDOFF). Your turn. Try this: Check my running-balance query: is the date filter in the same CTE as SUM() OVER? If so, move it downstream and test it on an account with history before the window. If the answer is yes, that's your bug, and an account with older history is the test that proves the fix.

**B11** (OUTRO). The Running-Balance Bug Hiding in a Correct-Looking SQL Query.

---

On-screen YOUR TURN prompt (identical to the spoken text in B10): Check my running-balance query: is the date filter in the same CTE as SUM() OVER? If so, move it downstream and test it on an account with history before the window.

Word count 424. Source: Ch.8 (`08-sql-i-balances-cohorts-window-functions.md`, worked example + "Notice where the date filter lives").
