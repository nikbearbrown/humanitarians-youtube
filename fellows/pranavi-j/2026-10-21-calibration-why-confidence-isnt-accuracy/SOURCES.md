# Sources — Calibration: Why Confidence Isn't Accuracy

General AI/STEM topic explainer. Model calibration — whether a model's stated or implied
confidence in an answer tracks the real frequency with which that answer is correct — is a
well-known, widely-discussed, generically-named property studied across predictive machine
learning broadly (not unique to language models), often measured by grouping predictions into
confidence buckets and comparing each bucket's average stated confidence against its observed
accuracy (the general shape behind terms like "expected calibration error"). This video describes
the general, settled shape of the idea qualitatively — what it means to check calibration, and why
"sounds confident" and "is accurate" are different claims — and does not cite a specific paper's
numeric result or claim any specific real model's current calibration behavior (calibration varies
by model, task, and how confidence is elicited, and is an active area of ongoing work).

No specific real model or vendor is named or benchmarked. The worked example (a "90% confident"
answer bucket that turns out to be right only 60% of the time) and its falsifiability case (a
different "90% confident" bucket that is right about 90% of the time) are both fully generic and
illustrative, with round numbers chosen for teaching clarity, matching the pattern used in this
fellow's prior STEM videos (e.g. the "strawberry" tokenization example, the fabricated-citation
hallucination example, the agronomy-hint chain-of-thought example).

## Distinct from adjacent, already-covered topics in this series

- `2026-09-22-hallucination-why-sounding-sure-isnt-being-right` covers whether a claim is
  fabricated at all. This video assumes a claim already exists and asks whether its attached
  confidence number tracks real accuracy — a different, narrower question.
- `2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason` covers whether a stated
  reasoning trace actually caused the answer. This video does not examine reasoning traces at all.
