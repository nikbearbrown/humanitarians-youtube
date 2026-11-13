# PEDAGOGY — System One. (claude-hai · teaching explainer, ~3min)

**The ONE insight:** a **System One model** reads a *state* and returns a
**typed, calibrated decision your code can act on** — not generated text. It's
for fast, structured judgment; an LLM is for writing/reasoning.

**Audience (HAI):** learners/builders who know chatbots and want to understand a
different class of model they can wire into software.

**Source (DOUBLE-CHECK LAW):** TypeSafe "System One" documentation pasted by the
creator. Use ONLY what the docs state — no invented benchmarks, pricing, or
adoption claims. Primitive example values (choice "billing", score 1.4, noul
0.95) are illustrative per the docs. Flagship model: **Jev** ("jev-latest").

## Act structure (framework-first — built to pass PROOF)
- B00 hook (composer) — a different kind of model: returns a decision, not text ✓
- **B01 FRAMEWORK before any example** — the definition: state in → typed answer +
  probability out (Jev) ✓
- **B02 the distinction** — LLM (generates text you parse) vs System One (returns a
  typed decision) — the reusable mental model ✓
- **B03 the primitives** — Choice / Score / Noul (how you define the answer space) ✓
- **B04 calibration (the honest caveat / friction)** — calibrated across GROUPS,
  not a guarantee for one answer; use confidence to set act-vs-escalate thresholds ✓
- **B05 worked example** — the refund workflow: state → 3 independent questions →
  code combines → act or escalate ✓
- **B06 when-to-use / what it's NOT (falsifiability)** — decide → System One; write
  or reason → LLM; it does not produce replies, code, or explanations ✓
- B07 verdict (one-pager) · B08 handoff (scaffolded task) · B09 outro ✓
- Body B01–B06 = 4K PIL cards; Claude UI only at B00/B07/B08/B09 (ILLUSTRATE LAW).

## PROOF rubric self-check (the six)
- Explicit framework before examples — B01/B02 ✓
- Reusable rubric — B02 (LLM vs System One) + B06 (which tool when) ✓
- Worked example — B05 refund workflow (the reasoning, not just the conclusion) ✓
- Falsifiability / edge case — B06 (what it's NOT: can't write/code/explain) ✓
- Active task — B08 scaffold (typed question + escalate threshold) ✓
- Friction — B04 (confident ≠ correct; calibration across groups) ✓
- Production gate: claims are definitional and sourced to the docs; example values
  labelled illustrative; evidence on the cards, legible.

## Correctness notes
- "Noul" is the docs' name for the true/false primitive — kept verbatim.
- Text-only input today (no image/audio/video) — not overstated; not featured as a
  limitation beat to avoid dating, but narration never implies other modalities.
- No claim about accuracy/benchmarks/market — none are in the source.

## Narration review (GATE P)
Listen for: does B01 land "typed decision, not text" BEFORE examples? Does B04
make "calibrated across groups, not one answer" clear? Is B06 explicit that it
can't write/reason (use an LLM)?

VERDICT: PASS ;
narration self-reviewed against the source docs before audio generation.
