# Frictional log — Step 3: Validate data shape

**Date:** 2026-09-03 · **Script:** `scripts/gigo/market-sentiment-analysis-part-1-validate-data-shape.py` · **Recipe:** `recipes/market-sentiment-analysis-part-1.md`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Enforce a required-field contract and promote only shape-clean rows into the verified layer.

## Where the work resisted

- There was no schema to validate against. `DATA_CONTRACT.md` carries no entry for this recipe.
- The recipe gave this step five output fields, and a wrong-typed value is none of them. There was nowhere to report that a field held the string *N/A* where a number belonged.

## What was done about it

- Read the required fields, identity keys and freshness windows from the fixture manifest — the only declared schema that exists — rather than restating them, so the validator and the corpus cannot drift apart.
- Left type checking alone and recorded the contract gap as a defect, instead of smuggling type errors into the missing-fields list where they would have looked like something they are not.

## What was learned

When a contract has no home for a finding, inventing one hides the gap instead of closing it. Logging it plainly is what got it fixed: `type_errors` was added to the recipe on 2026-09-25, three weeks later, and this step now reports them properly.

The workaround was honest about being a workaround, which is why it did not become permanent.
