# PEDAGOGY — AI's Four Chips. (claude-hai · teaching explainer, ~3min)

**The ONE insight:** AI is mostly **massive parallel matrix math**, so chips trade
**generality for AI-specific speed** along a spectrum (CPU → GPU → TPU → NPU). It's
a **division of labor, not a ranking** — match the chip to the job.

**Audience (HAI):** learners hearing CPU/GPU/TPU/NPU as jargon who want one lens
that makes all four make sense.

## Act structure (framework-first — built to pass PROOF)
- B00 hook (composer) — the alphabet soup; promise a lens ✓
- **B01 FRAMEWORK before any chip** — the workload: general = steps in order (CPU);
  AI = the same math, in parallel. Why special chips exist ✓
- **B02 the four chips** — CPU / GPU / TPU / NPU, one line each ✓
- **B03 the spectrum (the rubric)** — general ↔ specialized, four placed; specialize →
  more speed, less flexibility ✓
- **B04 worked example** — face-unlock → the NPU (small, on-device, low-power, offline):
  the lens picking a chip ✓
- **B05 falsifiability / edge** — NOT a ranking: a TPU can't run your OS, an NPU won't
  train a model, the CPU still runs the show ✓
- B06 verdict (one-pager) · B07 handoff (check your own hardware) · B08 outro ✓
- Body B01–B05 = 4K PIL cards; Claude UI only at B00/B06/B07/B08 (ILLUSTRATE LAW).

## PROOF rubric self-check (the six)
- Explicit framework before examples — B01 (workload) + B03 (spectrum) ✓
- Reusable rubric — B03 spectrum + the 3 questions (parallel? general/fixed? where?) ✓
- Worked example — B04 (face-unlock → NPU; the reasoning, not just the label) ✓
- Falsifiability / edge — B05 (division of labor, not a leaderboard) ✓
- Active task — B07 (find your device's NPU; on-device vs cloud, and why) ✓
- Friction — B05 forces resisting "newer/more-specialized = better" ✓
- Production gate: definitional claims, no benchmarks/model names/versions; evidence
  on the cards, legible.

## Correctness (DOUBLE-CHECK LAW — accurate, non-dating)
- CPU: few general-purpose cores, sequential-leaning; runs the system.
- GPU: many parallel cores; the general AI workhorse (train + inference).
- TPU: custom silicon (ASIC) built for tensor/matrix ops (datacenter-class).
- NPU: low-power accelerator for on-device AI inference (phones/laptops).
- Core AI op = matrix multiply (multiply-accumulate). No FLOPS/benchmarks, no
  product model numbers, no vendor claims. Spectrum is about generality, and B05
  explicitly says it is NOT a capability ranking.

## Narration review (GATE P)
Listen for: does B01 land "AI = parallel matrix math" BEFORE the chips? Does B03
make the general↔specialized trade the reusable rule? Does B05 kill the "ranking"
misconception?

VERDICT: PASS 
narration self-reviewed against the rubric above before audio generation.
