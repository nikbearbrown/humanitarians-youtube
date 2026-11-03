# Frictional log — Step 1: Verify provenance

**Date:** 2026-08-27 · **Script:** `scripts/tools/market-sentiment-analysis-part-1-verify-provenance.py` · **Recipe:** `recipes/market-sentiment-analysis-part-1.md`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

A provenance checker that confirms every source the recipe declares exists, parses, and hashes, before any other step is allowed to run.

## Where the work resisted

- The tool layer is forbidden from reading `data/raw/`, but this step has to confirm that raw paths parse. The rule and the job contradicted each other.
- One fixture is *supposed* to be unparseable. A straightforward checker halts on it, which would have made the frozen corpus unusable as an input to its own pipeline.
- `conformance.mjs` reported the finished script as FAILED even though it compiled cleanly.

## What was done about it

- Took the raw-layer read as a documented exception rather than a silent one: bytes are read to hash them and `json.loads` is called only to learn whether parsing raises. The parsed object is discarded and never inspected. The emitted output says so in its own field.
- Added `expected_parse_failure`, which inverts the test for that one file: if it ever *does* parse, the frozen defect catalogue no longer describes what is on disk, and the run stops.
- Traced the conformance failure to `python3` resolving to the Microsoft Store alias stub, which prints an install message and exits 0. Fixed by putting a real `python3` ahead of it on PATH.

## What was learned

A checker with no way to say *this one is supposed to be broken* will either halt on the fixture or quietly stop testing it. Both are worse than the extra field.

And a green check from a tool that is not actually running is worse than a red one, because it buys confidence instead of attention. Every `.py` and `.yaml` conformance check had been silently skipped for the whole first stretch of this work.
