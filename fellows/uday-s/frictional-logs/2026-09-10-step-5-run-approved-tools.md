# Frictional log — Step 5: Run approved tools

**Date:** 2026-09-10 · **Script:** `scripts/tools/market-sentiment-analysis-part-1-run-approved-tools.py` · **Recipe:** `recipes/market-sentiment-analysis-part-1.md`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Port the source workflow's sentiment arithmetic faithfully, so a historical score can be reconstructed, and prepare the model and notification calls without performing them.

## Where the work resisted

- The original is not defensive. A missing or non-numeric price silently becomes 0, and a source with no rows scores 50 — which reads as *neutral* but is a default. Fixing it would change what the number means; leaving it would launder a defect into a score.
- The flags for those coercions could not be reached through the fixtures at all. The original reads only the first price quote, and that one is clean.
- The finished step emitted a field claiming it never touched the raw layer, while reading the run envelope out of it.

## What was done about it

- Ported the arithmetic unchanged and emitted a named flag for every substitution it makes, so a score cannot be quoted without its caveats travelling alongside it.
- Built inputs by hand in a temp directory to force each unreachable path — missing price, non-numeric price, empty streams, an over-length news set — and confirmed each flag fires.
- Replaced the false claim with a precise one naming exactly what is read: two scalars from a control file, no records.

## What was learned

A false claim about provenance is worse than the access it conceals, because it spends the credibility that the rest of the trail depends on.

And an error path the test corpus cannot reach is a claim, not a feature. If the fixtures cannot exercise it, it has to be exercised some other way or not asserted at all.
