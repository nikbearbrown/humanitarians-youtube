# Frictional Log: step-two-was-the-last-one-i-built (Week 32 work video, long and Short)

**Record provenance:** drafted 2026-11-23 with Claude from this folder's own records (`ANGLE.md`, `FACTCHECK.md`, `PEDAGOGY.md`, `PROOF-REVIEW.md`) and the session's measurements, after the work was done rather than while it happened. **Reviewed by Tanmay.** Every entry points at the record it comes from.

## 2026-11-23: a recipe step that two earlier steps were standing in for
- **Work and expectation:** add step 2 (ingest declared inputs) to the Portfolio Price Fetcher recipe and open the pull request ([nikbearbrown/mycroft#94](https://github.com/nikbearbrown/mycroft/pull/94), merged as `fef5caa`).
- **Where it resisted:** the first draft of the script did not implement `--sample`, which the recipe's step-command table advertises; the repository's own check caught it.
- **What was done:** the flag was added before the commit; the pull request adds 19 files and edits none, so the recipe's own text still says step 2 is open and the film says so (`FACTCHECK.md`).

## 2026-11-23: the angle was already half-used
- **Where it resisted:** several candidate angles failed the five-axis check (claim, teachable move, shape, hook, vocabulary) against the earlier work videos, one on a claim already made in Week 29 ("run again with the clock pinned").
- **What was done:** the stand-in angle passed on all five axes; a hash-versus-correctness angle was kept only as a beat inside it (`ANGLE.md`).

## 2026-11-23: two sentences in the script claimed more than the code
- **Where it resisted:** the script said a wrong price "never reaches step three" (step 3 still reads the sample folder directly), and later that step 3 asked only whether a file parsed and had a price (it also checks the ticker).
- **What was done:** both rewritten to what the scripts do, the second as a logged Gate P amendment (`PEDAGOGY.md`, `PROOF-REVIEW.md`).

## 2026-11-23: the framework arrived after the example
- **Where it resisted:** the first scoring gave the long film 11/12: the three-question check appeared at B08 and B10, after the worked example.
- **What was done:** B01 now says it aloud and shows it, with a three-chip bar through B02 to B10 (a second logged amendment).

## 2026-11-23: measuring changed the pictures and the Short
- B06 named "that file" before introducing it; B04 and B05 opened empty for about 2 s; B03 sat 8 s on a table that only re-outlined; after audio the Short's loop was not closed (first frame already held a caption). Each was caught on the rendered video and fixed (`PROOF-REVIEW.md`).
- The masters were compiled with an explicit BT.709 matrix and tags; solid fills decode within 1 level.
