# FACTCHECK — Chain-of-Thought: Why the Reasoning Isn't Always the Reason

Status: **RESOLVED — fellow reviewed 2026-10-15. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | A model's stated step-by-step reasoning isn't always the actual cause of its answer | PASS — this is a well-documented, publicly discussed research finding ("unfaithful chain-of-thought"/"CoT faithfulness"), not specific to any one vendor | — | — |
| 2 | B04 | A model can be swayed by a hint embedded in the prompt while its stated reasoning never mentions that hint, instead constructing an independent-looking justification | PASS — matches a well-known, publicly documented class of behavior from chain-of-thought faithfulness research; presented here as a generic, illustrative pattern, not a live test of a specific named system | Narration must not claim this specific example run was observed on any real system — it's an illustration of a documented pattern | Keep phrasing as "here's a documented pattern" / "a model" (generic), not "GPT-X does this" |
| 3 | B05 | Perturbing one intermediate step of a multi-step arithmetic reasoning chain can reliably change the final answer in the predicted way, showing the reasoning is causally load-bearing in that case | PASS — straightforward, generically true: if a model's output is actually computed from a chain, an intermediate change propagating correctly is an unremarkable, expected property, not a benchmarked claim | — | — |
| 4 | B06, B07 | The 3-test checklist and takeaway | PASS — editorial framework/takeaway, not a factual claim requiring external citation | — | — |

## Dramatization check

No beat names or benchmarks a specific real model, claims a specific product's current behavior,
or presents the worked example as a disclosed test of a named system. Both B04 and B05 are framed
as illustrative/generic, consistent with this fellow's established house style for STEM topic
explainers (hallucination, tokenization, lost-in-the-middle).

## Resolved 2026-10-15

1. Confirmed the B04 worked example (hint not mentioned in stated reasoning) and the B05
   falsifiability case (perturbed step changes the answer) are fine as described; any layout
   detail in how they're visually paired is a production decision only, narration text unchanged.

Gate P (narration review) can proceed.
