# PEDAGOGY — Small Language Models. (claude-hai · teaching explainer, ~2.5min)

**The ONE insight:** **size is a trade, not a score.** For a narrow, repeated task a
small specialized model can match a big general one while being faster, cheaper, and
private — but the big model still wins for open-ended, broad, or novel work.

**Audience (HAI):** learners/builders who default to the biggest model and should
learn to right-size it.

## Act structure (framework-first — built to pass PROOF)
- B00 hook (composer) — everyone reaches for the biggest; when is smaller smarter? ✓
- **B01 WHAT (definition)** — SLM = small LM: fast, cheap, private, fine-tunable ✓
- **B02 THE REFRAME (framework/rubric)** — size is a trade: big = knowledge/reasoning;
  small = speed/cost/privacy/fine-tune ✓
- **B03 worked example** — routing support tickets: a fine-tuned SLM matches a frontier
  model, cheaper/faster/private ✓
- **B04 which-when (falsifiability + rubric)** — smaller isn't always better; LLM wins
  for open-ended/broad/novel ✓
- B05 verdict · B06 handoff (right-size one repeated task) · B07 outro ✓
- Body B01–B04 = 4K PIL cards; Claude UI only at B00/B05/B06/B07 (ILLUSTRATE LAW).

## PROOF rubric self-check
- Explicit framework before examples — B01 + B02 ✓
- Reusable rubric — B02 (the trade) + B04 (which-when) ✓
- Worked example — B03 (ticket routing, the reasoning for the choice) ✓
- Falsifiability / edge — B04 (names when the SLM is the wrong call) ✓
- Active task — B06 (right-size a real repeated task; estimate the saving) ✓
- Friction — B02/B04 force resisting "biggest is best" ✓
- Production gate: qualitative claims only (no param counts, benchmarks, or model
  names), evidence on the cards, legible.

## Correctness (DOUBLE-CHECK LAW — accurate, non-dating)
- No specific parameter counts (SLM sizes drift) — "orders of magnitude fewer params".
- No benchmark numbers or named models; "matches a frontier model on a narrow task"
  stated qualitatively, which is the defensible, non-dating claim.
- The trade is framed as task-fit, not a capability ranking; B04 explicitly names the
  cases where the large model is the right choice.

## Narration review (GATE P)
Listen for: does B02 land "size is a trade, not a score" BEFORE the example? Does B04
make clear smaller isn't always better? Is B06 a task the viewer can actually run?

VERDICT: PASS 