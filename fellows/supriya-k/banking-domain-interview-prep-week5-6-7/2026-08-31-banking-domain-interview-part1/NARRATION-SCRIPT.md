# Narration Script — "Banking Domain Data Analyst Interview Prep — the SQL Banks Actually Ask"

cli-explainer · v3 (2026-10-16, branch banking-reels-v3) · 12 beats · 405 words · ~158s estimated at v1's per-beat pace · Voice: Kokoro `af_bella` ("Bella") · Narrator identity: **Supriya**

v2 (491 words, 191.8s; shortened 9:16 at 153.7s) is the baseline commit 516aeb8. Same 12 beat ids. Every number on screen now comes from a real run of `sql/` (see `FACTCHECK.md`, "v3 corrections").

---

**B00** (INTRO). Hi, I am Supriya and this video is about the SQL that banking interviews actually ask. You already know SQL. That's not what trips people up.

**B01** (PROBLEM). A general analytics interview tests joins, cohorts, and dashboards: skills you already have. A banking one adds a second language on top: regulators like the OCC and the CFPB, ratios like CET1 and LCR, and the habit of asking whether a number is regulatory-reportable, or could be fraud.

**B02** (PROBLEM (the book's map)). This book maps that layer in six parts: the banking landscape, regulation and risk, the modern data stack, technical prep with forty-plus SQL problems and Python for banking, the behavioral and case rounds, and a day-of cheat sheet.

**B03** (CLI — cycle 1). Take one worked problem from chapter eight: end-of-month balances for the first half of twenty twenty-six, built one CTE at a time.

**B04** (CODE). Here's the shape. Running computes the cumulative balance over the whole ledger, with no WHERE clause at all. One CTE later, the date filter narrows to the reporting window and keeps each month's last posting. Sum first. Filter after.

**B05** (OUTPUT). Run it on a Cascade Savings account that carried twelve thousand four hundred dollars into January. The month-end balances on screen are the true ones, because the sum saw the whole ledger first.

**B06** (CLI — cycle 2). That's one shape. Chapter nine adds a harder one, on a different dataset: a card issuer's monthly snapshots, where the job is to keep one cohort intact.

**B07** (CODE). Isolate the January twenty twenty-five cohort first. Compute months on book by diffing each snapshot against the origination month. Then group by months on book and bucket. A calendar-month group-by would lose the cohort.

**B08** (OUTPUT). Run it on a Harborline sample cohort. At month three, ninety-two percent are current. By month nine, four percent are ninety-plus days past due and three percent charged off. Each column adds back to five hundred, because this sample has one snapshot per account per month.

**B09** (SUMMARY). Two moves: get the SQL evaluation order right, and never lose the cohort. That's chapters eight and nine. The rest of the book covers regulatory metrics, the data stack, and the behavioral and case rounds.

**B10** (NEXT STEPS / HANDOFF). Your turn. Try this: Check my banking SQL for two bugs: is any date filter applied before a running SUM() OVER, and does every row stay tied to its cohort? Both bugs run without an error, so the only way to find them is to ask.

**B11** (OUTRO). Banking Domain Data Analyst Interview Prep: the SQL banks actually ask.

---

On-screen YOUR TURN prompt (identical to the spoken text in B10): Check my banking SQL for two bugs: is any date filter applied before a running SUM() OVER, and does every row stay tied to its cohort?

Word count 405. Sources: `book.md`; Ch.8 worked example; Ch.9 worked example (Harborline).
