# FACTCHECK — Calibration: Why Confidence Isn't Accuracy

Status: **RESOLVED — fellow reviewed 2026-10-21. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | A model's stated or implied confidence in an answer does not always track how often that answer is actually correct | PASS — this is a well-documented, publicly discussed, generically-named property of predictive models ("calibration" / "expected calibration error" — grouping predictions by stated confidence and comparing against observed accuracy per group), not specific to any one vendor | — | — |
| 2 | B04 | A model's answers bucketed at roughly the same stated confidence (e.g. "90% sure") can show a real accuracy well below that number across many questions (e.g. 60%), indicating overconfidence | PASS — matches the standard, generic definition of a calibration gap / positive expected-calibration-error; presented here as a generic, illustrative pattern with made-up round numbers for teaching clarity, not a disclosed measurement of a specific named system | Narration must not claim this specific 90%/60% pairing was observed on any real system — it's an illustration of how the measurement works | Keep phrasing as "here's a documented pattern" / "a model" (generic), not "GPT-X does this" or "measured at X%" |
| 3 | B05 | A different, well-calibrated model/bucket can show stated confidence and actual accuracy nearly matching (e.g. both near 90%) | PASS — straightforward, generically true: a model whose confidence tracks its accuracy is the definition of well-calibrated; not a benchmarked claim, just the other side of the same generic measurement shown in B04 | — | — |
| 4 | B06, B07 | The 3-test checklist and takeaway | PASS — editorial framework/takeaway, not a factual claim requiring external citation | — | — |

## Dramatization check

No beat names or benchmarks a specific real model, claims a specific product's current confidence
behavior, or presents either illustrative bucket (B04's overconfident 90%/60% example, B05's
well-calibrated 90%/90% example) as a disclosed test of a named system. Both are framed as generic
illustrations of how a calibration check works, consistent with this fellow's established house
style for STEM topic explainers (hallucination, tokenization, lost-in-the-middle,
chain-of-thought faithfulness).

## Distinct from this fellow's prior videos

This video is explicitly not a re-run of two adjacent, already-covered topics in this series:

- **Not hallucination** (`2026-09-22-hallucination-why-sounding-sure-isnt-being-right`): that video
  is about whether a stated claim is fabricated at all (invented citations, facts). This video
  assumes the claim-generation question is separate and asks a different question: when a model
  says how sure it is, does that number track how often it's actually right?
- **Not chain-of-thought faithfulness** (`2026-10-15-chain-of-thought-why-the-reasoning-isnt-
  always-the-reason`): that video is about whether a stated reasoning trace actually produced the
  answer. This video doesn't look at reasoning traces at all — only at the stated/implied
  confidence number or phrase and the real accuracy rate it should predict.

## Resolved 2026-10-21

1. Confirmed the B04 worked example (a 90%-confident bucket actually right 60% of the time) and
   the B05 falsifiability case (a 90%-confident bucket actually right ~90% of the time) are fine as
   described, fully generic illustrative round numbers chosen for teaching clarity, not claimed as
   measured results from any real system. Any layout detail in how the bars/bucket are drawn is a
   production decision only, narration text unchanged.

Gate P (narration review) can proceed.
