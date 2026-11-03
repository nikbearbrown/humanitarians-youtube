# Frictional log — Step 4: Transform and quality check

**Date:** 2026-09-10 · **Script:** `scripts/gigo/market-sentiment-analysis-part-1-transform-quality-check.py` · **Recipe:** `recipes/market-sentiment-analysis-part-1.md`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Deduplicate the shape-clean rows, then flag stale timestamps and wrong-typed values without dropping or correcting either.

## Where the work resisted

- The deduplication short-circuited. After a row matched on identity key, it stopped — so a byte-identical repeat never reached the headline pass, which reported 1 duplicate where the corpus expected 2.
- One bad value got counted twice. The string *yesterday* in a timestamp field raised both a type violation and an unreadable-timestamp flag, inflating the totals past what the corpus declared.

## What was done about it

- Split dedup into independent passes so a row can be a duplicate on more than one basis, and removal is the union of them.
- Suppressed the freshness flag when the same field already carried a type violation.

## What was learned

The headline pass is the one that catches a syndicated copy — the same story from a second outlet, with a different id and url, which an id-only dedupe counts as independent and double-weights. Short-circuiting silently disabled exactly the check that justified having two passes.

Nothing failed. The numbers simply came out one lower than the corpus said they should. Without a declared expected total, that would have shipped.
