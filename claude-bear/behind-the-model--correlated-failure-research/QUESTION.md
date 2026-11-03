# QUESTION.md

**Question:** Correlated Failure in AI Auditing — Consensus Is Not Verification.

**Asked by:** framed from the source reel `anthropics/youtube/behind-the-model/correlated-failure-research`
(redo, per SUBJECT.json). Name not applicable — no individual asker attached to the source.

**Where:** internal — this is a `hai-simple` redo of an existing `behind-the-model` CLI-explainer
reel into the Plain-register Humanitarians AI cut.

**Name usable:** N/A.

## The argument, kept from the source

The source reel (Teardown register, CLI 10-beat spine, `am_onyx`/Liam narration already)
makes these load-bearing claims, carried into this redo unchanged:

1. **Ensemble theory result:** cross-checking reduces error only when the checkers fail
   *independently*. If two checkers share a failure mode, their agreement is not evidence
   of correctness.
2. **LLMs auditing LLMs are correlated, not independent** — they share training data, RLHF
   tuning, and distributional biases. Agreement between them is evidence of shared priors,
   not evidence of correctness.
3. **Three documented, structural LLM-as-judge failures:** positional bias (favors the
   first answer shown), verbosity bias (favors the longer answer), self-enhancement bias
   (favors output matching the judge's own style). Not bugs — structural.
4. **The concrete falsifying case (source B05/B06):** send the same two answers to an LLM
   judge twice, in each order. The verdict flips with the order, not the content. That is
   positional bias made visible and reproducible.
5. **The fix is pairing, not zero-AI:** each claim type gets a check with a *structurally
   different* failure mode from an LLM — a factual claim against retrieval, a math result
   against actual code execution, a schema/format claim against a validator.
6. **The summary (source B07/B08):** more AI does not mean better verification, it means
   more consensus from systems that share failure modes; the actionable next step is to
   find every LLM-checks-LLM seam in a pipeline and replace the highest-stakes one with a
   structurally independent check.

## What this redo does NOT change

The facts above are unchanged. What changes is register (Teardown → Plain, judgment
removed), structure (CLI 10-beat "ask/terminal/output" spine → hai-simple's
writer-open + body + carry-out + your-turn + outro spine), the cold open
(`NikBearBrownOpen` → `BrutalistHesitantWriter`), voice (unchanged — Liam, already
`am_onyx` in the source), and the close (Humanitarians AI skin, `@HumanitariansAI`).

## Deliberately not claimed

- **Not "AI-on-AI checking is always worthless."** The reel states both directions: a
  structurally independent check (code execution, retrieval) agreeing with an AI's claim
  *is* real evidence; three LLM judges agreeing with each other is not, by itself.
- **Not "disagreement between AI judges proves one is wrong."** Disagreement can just
  mean the same shared bias landed differently on a given run — the reel states this as
  the negative-result direction.
- **No accusation of any specific product or vendor.** The bias findings (positional,
  verbosity, self-enhancement) are described as documented and structural, not as a flaw
  unique to any one system.
