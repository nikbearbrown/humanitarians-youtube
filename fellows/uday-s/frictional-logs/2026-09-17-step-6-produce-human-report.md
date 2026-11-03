# Frictional log — Step 6: Produce human report

**Date:** 2026-09-17 · **Script:** `scripts/tools/market-sentiment-analysis-part-1-produce-human-report.py` · **Recipe:** `recipes/market-sentiment-analysis-part-1.md`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Turn the prior steps' machine output into a report a human can decide on, plus the agent log and an audit beside the data.

## Where the work resisted

- The step claimed its reruns were byte-identical. They were not — the agent log carries a `generated_at` field the recipe's contract requires, so it changes every run.
- After an unrelated rebase, the report started citing a hash for its own script that no longer matched the file. The scripts had been re-checked-out with different line endings, so every script hash in the report was reproducible only on this machine.

## What was done about it

- Corrected the idempotence claim rather than the behaviour, and stated exactly which single field differs and why.
- Extended the line-ending rules to cover the step scripts, normalised them, and regenerated the reports so every cited hash re-verifies against its committed blob.

## What was learned

The report hashes its own inputs, which is how it caught a defect in itself. A self-verifying artifact pays for the extra machinery the first time something drifts underneath it.

Writing a property into a docstring before testing it is how two false claims got into this work. Both were caught on review, not by a test.
