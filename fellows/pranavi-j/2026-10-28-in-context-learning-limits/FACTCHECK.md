# FACTCHECK — In-Context Learning: What the Prompt Can (and Can't) Teach

Status: **RESOLVED — fellow reviewed 2026-10-28. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | In-context learning (ICL) is a model conditioning on examples/instructions given in its prompt at inference time, producing task-appropriate output on new cases, without any weight updates | PASS — this is the standard, generic, widely-used definition of in-context learning in the broader ML/NLP literature; not specific to any one vendor or model | — | — |
| 2 | B03/B04 | What looks like "learning" from a few in-context examples is better described as the model locating/completing a pattern already reachable from its pretraining, using only what's in the current context window — not acquiring a new capability it lacked | PASS — this is a well-documented, broadly-discussed qualitative framing in the ICL research literature (ICL as pattern-completion / task-location rather than parameter learning); stated here generically, with no claim about any one system's internal mechanism as fact rather than a proposed account | Narration kept to "located a pattern... already built to complete" (qualified, mechanism-level framing), not an absolute certainty claim | Keep hedged language ("can," "often," "a proposed account") rather than asserting the mechanism as settled fact for all models |
| 3 | B04 | A toy, invented input→output rule can be demonstrated purely via example pairs in a prompt, and a model can often apply it correctly to a new, unseen input | PASS — matches the standard few-shot ICL setup used throughout the literature; the specific rule and example pairs shown are fully invented for teaching clarity, not a disclosed measurement of a specific named system | Narration must not claim this particular example was tested on any real system — it's an illustration of the general, well-documented mechanism | Keep phrasing generic ("a model," "can often") |
| 4 | B05 | In-context learning can be sensitive to the order in which examples are presented, and to whether the demonstrated mapping agrees or conflicts with what the model's pretraining would otherwise favor — reordering examples or giving a demonstration that contradicts the model's prior can produce a less reliable or inconsistent result compared to a "natural," prior-consistent ordering/mapping | PASS — order-sensitivity of few-shot prompting, and the finding that models do not always fully override a pretrained prior with a demonstrated mapping that conflicts with it, are both well-documented, broadly-discussed findings in the in-context-learning research literature. Stated qualitatively and generically ("can be sensitive," "can produce a less reliable result"), with no specific accuracy numbers, benchmark, or named system attached | Avoid any invented specific percentage or named benchmark for this effect | Keep purely qualitative: "more/less reliable," "inconsistent," never a fabricated number |
| 5 | B03/B06 | In-context learning is bounded by the model's context window — information or examples that don't fit inside the window cannot be used by the model, no matter how many additional examples are added | PASS — definitional/structural claim: a model can only condition on what is actually inside its context at inference time; this is uncontroversial and not benchmark-dependent | — | — |
| 6 | B06, B07 | The 3-test checklist, the scaffolded audit task, and the takeaway | PASS — editorial framework/takeaway and a generic, runnable procedure, not a factual claim requiring external citation | — | — |

## Dramatization check

No beat names or benchmarks a specific real model, claims a specific product's current few-shot
behavior, or presents either illustrative case (B04's toy substitution rule, B05's reordered /
flipped-mapping stress test) as a disclosed test of a named system. Both are framed as generic
illustrations of how in-context learning behaves, consistent with this fellow's established house
style for STEM topic explainers (hallucination, tokenization, lost-in-the-middle, chain-of-thought
faithfulness, calibration).

## Distinct from this fellow's prior videos

This video is explicitly not a re-run of five adjacent, already-covered topics in this series:

- **Not hallucination** (`2026-09-22-hallucination-why-sounding-sure-isnt-being-right`): that video
  is about whether a stated claim is fabricated at all. This video assumes the model is trying to
  follow a demonstrated pattern and asks a different question: what can prompt-only conditioning
  actually teach it to do?
- **Not tokenization**: that topic is about how text is chunked into tokens before any reasoning
  happens. This video operates one level up — what the model does with examples once they're in
  its context, not how those examples are segmented.
- **Not lost-in-the-middle** (`2026-10-06-lost-in-the-middle-why-more-context-isnt-better`): that
  video is about where in a long context a fact sits and whether position affects retrieval. This
  video is about whether examples (anywhere in context) can teach a pattern at all, and how
  robustly.
- **Not chain-of-thought faithfulness** (`2026-10-15-chain-of-thought-why-the-reasoning-isnt-
  always-the-reason`): that video is about whether a stated reasoning trace actually produced the
  answer. This video doesn't examine reasoning traces — only what prompt-given examples can and
  can't teach, with no weight updates involved.
- **Not calibration** (`2026-10-21-calibration-why-confidence-isnt-accuracy`): that video is about
  whether a stated confidence number tracks real accuracy. This video doesn't involve confidence
  scores at all — it's about the mechanism and limits of learning-from-the-prompt itself.

## Resolved 2026-10-28

1. Confirmed the B04 worked example (a toy, invented substitution rule taught via example pairs,
   applied correctly to a new input) and the B05 falsifiability case (the same task reordered,
   with one mapping flipped against the model's likely prior, producing an inconsistent result)
   are fine as described: fully generic, illustrative, no real model/vendor named or benchmarked,
   and the qualitative claims about order-sensitivity and prior-conflicting demonstrations are
   conservative, hedged, and consistent with well-documented findings in the general ICL research
   literature. No specific numeric result, paper, author, or vendor is cited or implied anywhere
   in the beat sheet, narration, or on-screen text.

Gate P (narration review) can proceed.
