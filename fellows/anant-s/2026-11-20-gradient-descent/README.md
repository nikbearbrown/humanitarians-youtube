# Gradient Descent, One Step at a Time

- **Status:** final — delivered (4K master, gates passed)
- **Series:** STEM AI explainer series · Film 1 (the first film of the series)
- **Channel:** @NikBearBrown (claude-liam brand) · **Voice:** Kokoro `am_onyx` (Liam, in for Bear) · **Greeting:** "Ciao, Liam"
- **Long:** 3840×2160 · 3:12 · 11 beats — `claude-liam-gradient-descent.mp4`
- **Last updated:** 2026-11-22

## Subject

How a neural network learns: one rule, θₜ₊₁ = θₜ − η∇L(θₜ), a step against the slope. It is worked on L = θ² from θ = 3 with executed numbers (3 → 2.4 → 1.92, ×0.8 per step), then broken two ways: a step size of 1.1 that runs away to θ₁₀ = 18.5752, and a two-valley loss where the start decides the valley. It closes on how the rule scales: backpropagation and small batches.

## Notes

- ai-explainer format: cold open in the Claude composer → hesitant-writer summary → six Manim scenes → Verdict recap → Your Turn → title outro.
- The fact check corrected two draft claims: "millions of times" → "step after step" (B01), and "this same rule" → "a version of this same rule" (B07).
- BVDT gained a sixth line after GATE P ("Where you start decides which valley you end in.") for canvas fill. It restates B06; only BVDT audio was regenerated, and it was flagged for review.
- Known cosmetic issue, not fixed: the locked `ClaudeTitleOutro` wraps the title as "…One Step at a / Time.". Remotion stays at 4.0.535 (4.0.545 available, upgrade not run).
