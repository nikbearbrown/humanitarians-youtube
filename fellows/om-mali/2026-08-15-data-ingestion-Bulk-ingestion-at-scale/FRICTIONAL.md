# Frictional log — 2026-08-15

**Week 2 · data ingestion · 80 million filed rows down to a 5,806-row universe**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `docs/worklog.md`,
`DATABASE_SETUP.md` or `logs/RUN_LOG.md` in the project repo.

---

## What I was working on

Turning one hand-verified quarter into a panel. Fourteen quarters of SEC bulk data, filtered
down to the universe companies, reconciled so that every filed row is accounted for and
loaded into Postgres.

The deliverable is boring on purpose: **80,571,213 source rows → 22,041,937 private →
5,806 universe**, with a per-quarter table showing where every row went.

## What I tried, and what I expected

I expected this to be the week where nothing interesting happens — download, filter, load,
count. The plan asked for 27 quarters; I downloaded 14 (2023Q1–2026Q2, 5.9 GB) because the
feasibility work in week 1 concluded the AI cohort barely existed in fund portfolios before
about 2023.

I also expected to confirm the $589.0095 Anthropic repricing I had hand-verified the week
before. It was the single most striking number in the project.

## Where it resisted, and what I did next

**The repricing is not in the bulk data, and it never will be on this route.** No Anthropic row
anywhere in 2026Q2 exceeds **$318.57**. I assumed a bug in my filter and spent real time
looking for one.

There is no bug. **The bulk sets are indexed by filing quarter, not by period.** Filings lag
their period end by roughly 56 days, so the newest as-of date in the 2026Q2 set is
**2026-04-30**, not 2026-06-30. The 5/29 and 5/31 marks were filed in late July and land in
2026Q3, which the SEC has not published — `2026q3_nport.zip` returns 404.

That is a structural property of the path, not a defect, so I pinned it with a test named
`test_bulk_cannot_reach_the_589_repricing`. A test that asserts a limitation is the only way
to stop a future me quietly "fixing" it. It also promoted the plan's live-EDGAR path from a
nice-to-have to the only route to the current period.

**Dates sorted alphabetically, and it would have inverted the project's headline.** DERA writes
dates as `DD-MON-YYYY` **text**. Left unparsed, `30-APR` sorts before `31-MAR`. The project's
main output is propagation lag measured in days between period ends — so this one unparsed
column would have silently reversed the result. Now parsed to a real `DATE` at ingest.

**And the obvious date column was the wrong one.** `REPORT_ENDING_PERIOD` is the fund's fiscal
*year* end, not the quarter end. The correct field is `REPORT_DATE`, the as-of date of the
holdings. I verified it on a case that makes the difference visible: **BlackRock files with a
fiscal year end of 31-MAY-2026 carrying holdings as of 27-FEB-2026.** Three months apart. Using
the wrong column would have scrambled every mark date in the panel.

**Fidelity was counted as four managers.** `Variable Insurance Products Fund I–IV` are
Fidelity — CIKs 356494 / 831016 / 927384 / 720318, which are in the plan's own holder table.
Unmapped, they appeared as four independent families, inflating precisely the count that
cross-manager dispersion depends on. After the fix Fidelity consolidates from 2,514 rows / 15
CIKs to **3,004 / 19**. Lincoln Financial has a similarly-named trust and is kept distinct by
needle ordering, pinned by its own test so a future edit cannot merge them.

**Three more filter corrections, each from reading data rather than reasoning about it:**

- **`ASSET_CAT` is an allow-list, not a deny-list.** My first instinct was to exclude `OTHER`
  as junk. But `OTHER` holds the mark the whole project turns on — `ANTHROPIC` 964,742 shares
  / $249,999,768.80 = **$259.1364**, the price six managers agree on. An EC/EP-only rule would
  have thrown away the best data in the set. 329 rows are excluded across 14 quarters and
  counted in the reconciliation rather than dropped silently.
- **OpenAI needs `%OPEN AI%` as well as `%OPENAI%`.** BlackRock writes `Open AI Group PBC` with
  a space. One missing pattern lost a whole manager's position.
- **SpaceX needs `%SPACEX%` as well as `%SPACE EXPLORATION%`** — `SPACEX-CL A PP` carries no
  spelled-out name.

**I corrected my own week-1 write-up.** `docs/feasibility.md` §8 recorded Cohere as having
"zero at Level 3". Measured on the same quarter there are **two** — both
`COHERE TECHNOLOGIES, INC.`, a wireless company. The exclusion was right; the stated count was
not. Cohere stays in as a deliberate false-positive canary, with a test asserting it can never
be promoted to a full member.

**And I answered four complexes the plan left unverified.** Neuberger Berman (133 rows) and
Morgan Stanley (103) are real holders; Baillie Gifford and Invesco have no presence at all.
More usefully, **31 complexes hold the universe that week 1's EDGAR search missed** — Baron
Capital at 324 rows, Lincoln Financial 149, SunAmerica 110, Coatue 36. Week 1's holder list
came from full-text search on one company. The real holder base is much wider.

## What Claude contributed, and what I did with it

Claude wrote nearly all the code this week — `universe.py`, `build_parquet.py`, the schema,
the loader, the reconciliation script, 20 tests. For a job this mechanical that is the correct
use, and the downloader from week 1 needed no changes at all across 13 new fetches.

**What I did not delegate was the scope decision.** Claude would have followed the plan's 27
quarters. I cut it to 14 on measured evidence — 2023Q1 returns 187 universe rows against 948
in 2026Q2 — and wrote down that 2019Q4–2022Q4 are a known, deliberate gap rather than an
oversight. Phase 1 asks for eight quarters; shipping 14 with a stated boundary is a different
claim from shipping 27 badly.

I also overruled the storage design. The obvious implementation puts the whole private layer
in Postgres; at ~694k rows a quarter that is 22 million rows and past the free tier. The wide
layer stays in Parquet, queryable with DuckDB and re-runnable, and Postgres carries only the
universe-matched subset.

**The date-column bug is the one I want on the record.** The code was correct. It read a column
named `REPORT_ENDING_PERIOD`, which sounds exactly like what you want. Finding it meant pulling
one BlackRock filing and noticing a three-month gap between two dates that should have matched.
That is a reading problem, not a coding problem.

## What I understand now, and what I still do not

**Understood.** The bulk path can never reach the current quarter — roughly two months of lag,
measured across all 14 quarters, not assumed. The stagger that propagation analysis depends on
is real: **12 of 12 calendar months carry universe period ends.** The Anthropic series runs 33
period ends, 2023-04-28 to 2026-04-30, $11.79 → $388.19, and **43 distinct CIKs** reproduce the
$259.14 mark where week 1 hand-verified six.

**Not understood.** The private-row count oscillates by quarter — 2.32M in 2023Q1 against 694k
in 2026Q2, with q1/q3 consistently higher than q2/q4 — and I have not investigated why. It does
not affect the universe layer, which grows smoothly, but it is unexplained and I have left it
written down rather than rationalised. Two Anthropic period ends show implausible spreads (161%
and 80%); OpenAI's range starts at $1.00 and SpaceX spans $70–$5,265.90. Those are unit
artifacts I can see but have not yet separated from real moves.

**Postgres had never actually been connected when I wrote this up.** `DATABASE_URL` in `.env`
was the Supabase *project* URL, not a Postgres URI, so `psycopg2` could not use it — which
means the loader and the schema were written but unexecuted. I said so plainly rather than
implying the pipeline had run end to end.

**The gate was not cleared this week.** The reconciliation table is evidence, not a verdict.
Whether 14 quarters and this holder coverage are *adequate* is a judgment, and I had not made
it yet.
