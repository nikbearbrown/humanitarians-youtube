# Frictional log — recipe promotion to RUNNABLE-SAMPLE, and the gate fixes

**Date:** 2026-09-25 · **Commits:** `d6f5b90` (promotion) · `55546b5` (gates 4 and 5)
**Recipe:** `recipes/market-sentiment-analysis-part-1.md`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Claim the promotion the evidence already supported: close the recipe's 13 DEV markers, add
lifecycle frontmatter, record gate decisions, fix three known contract defects, and write the
RUN_LOG entry that the reports had been citing without one existing.

## Where the work resisted

- **The recipe had no open TODO markers to count.** `todos_open: 2` was written before
  checking. The two genuinely open items lived only in step 6's runtime output; the only
  literal markers in the file were inside gate *test commands*. The number was unverifiable
  by the obvious method — grep — and would have read as wrong to anyone who tried.

- **Half the DEV markers could not be closed honestly.** Six were the canonical steps, all
  built. The other six were legacy n8n node mappings, and two of those — *Parse Question &
  Extract Tickers* and *Webhook Response* — have no implementation at all. Closing all
  thirteen the same way would have asserted six more scripts exist.

- **Step 6 was not on the branch I was working on.** The recipe edits were being made on
  `main`, and the pipeline run failed with *No such file or directory* because step 6 lives
  only on its own branch. The promotion depends on all six steps existing.

- **The step-6 branch still carried the sync merge that had just been removed from `main`.**
  Merging it would have silently reintroduced eight upstream commits the user had
  deliberately force-pushed away an hour earlier.

- **Rebasing made that worse before it made it better.** A plain `git rebase main` linearised
  the merge and replayed seven of another contributor's commits onto the branch as new SHAs.
  The branch went from carrying the merge to carrying its contents.

- **The rebase then left a detached HEAD.** `--onto` succeeded but the branch ref stayed
  where it was, so the work was reachable only by SHA.

- **Adding `type_errors` to step 3 risked breaking the thing that proves the pipeline works.**
  The fixture manifest maps D02/D11/D17 to step 4 `flags`. Moving detection to step 3 would
  have invalidated the frozen corpus's expectations and the 18/18 result.

- **A patch aborted mid-edit on a non-unique anchor.** `Human capacity: [EI].` appears twice —
  once in the phase gates, once in the legacy notes.

## What was done about it

- Placed the two real markers where they belong — the DEFINE on step 5's unattributed scoring
  constants, the APPROVE on gate 5 — so `todos_open: 2` is greppable, and documented that the
  same strings also appear inside gate tests where they are the test, not open work.

- Closed the six canonical markers with evidence, and relabelled the legacy section
  **historical, not a work plan**. Each node records where it went: absorbed by a canonical
  step, or never built and saying so.

- Moved the work to the step-6 branch, then used `git rebase --onto main <last-upstream>` to
  drop the replayed commits, leaving exactly two commits, both authored by the user.

- Pointed the branch ref at the rebased HEAD before continuing.

- Added `type_errors` to step 3 as a **report**, not a gate: rows are still promoted, because
  a wrong value is not a wrong shape, and step 4 still flags them — the same carry-forward
  pattern it already uses for step 3's rejects. Re-ran the full corpus and confirmed 18/18
  and every declared total unchanged before committing.

- Re-anchored the failed patch on a unique line.

## What was learned

**Creating the right artifact made an existing defect worse.** Gate 5's test passed if an
approval record existed *or* if an APPROVE marker was present — and the marker is always
present. Before `logs/gate-decisions/` existed, that was merely wrong. Once the folder
existed, it read as a considered clearance: the directory is there, the other gates are
recorded, and gate 5 says pass. Adding evidence to a system can make its lies more credible.
It was fixed the same day, with all three cases break-tested rather than just the passing one.

**A number written before it was checked is the same class of error as a claim written before
it was tested** — the `raw_layer_access` and byte-identical-reruns claims from earlier weeks.
Three instances now, same root: asserting a property because it ought to be true.

**Branch history carries decisions that a diff does not show.** The step-6 branch looked fine
by content and would have quietly undone an explicit instruction. `git merge-base
--is-ancestor` answered in one line what no file comparison would have surfaced.

**Partial honesty beat uniform closure.** Saying *two of these were never built* is a worse-
looking recipe and a truer one, and it cost nothing but a paragraph.
