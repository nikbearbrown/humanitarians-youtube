# PROMPTS — state-space-models-and-mamba

## Open slots: none

All twelve beats render from this folder — nine Manim scenes in `scenes.py`,
three registered Claude components. No pantry asset is required.

## The asks that built this reel (reusable for the weekly STEM format)

**1 — find the idea, not the summary**

```
claude "read the Mamba paper abstract and the S4 abstract. What is the ONE
architectural decision that separates them, and what does that decision cost?"
```

**2 — the framework (this is the beat that makes it teach)**

```
claude "give me three axes I can score ANY sequence architecture on — axes that
would predict a failure mode, not just describe features. Then score RNN,
Transformer and Mamba on them."
```

**3 — the falsifiability beat (do not skip this one)**

```
claude "what is the proven limitation of state space models? Find the paper,
quote the actual theoretical result, and tell me which of my three axes
predicts it."
```

That ask is what surfaced Jelassi et al. 2024 and turned the framework from a
description into something that forecasts. A framework that cannot predict a
failure is decoration.

**4 — the source check, run before narration was written**

```
claude "for each claim in this beat sheet, quote the sentence in the source
that supports it. Flag anything I am stating more strongly than the source does."
```

This produced the two PASS-WITH-WORDING rows in FACTCHECK.md: "non-trivial
result on Path-X" (not "solved"), and "streaming" being my inference rather
than a paper claim.

## Next week

Swap the topic and the sources; keep the spine — BLUF, framework, worked
scoring, mechanism, evidence with citations on screen, a falsifiability beat
the framework predicts, verdict with when-NOT-to, scaffolded task.
