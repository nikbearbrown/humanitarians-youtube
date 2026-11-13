# Frictional log — Prompt Injection: The Vulnerability Hiding in Plain Text

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

This general-AI-topic explainer (same framework-first genre as the sibling "Why AI-Generated Code" video) teaches a reusable 3-question rubric — Source / Instruction-or-Data / Consequence — for deciding whether text an AI agent reads from the outside world should be allowed to change what it does. The plan was a 9-beat, ~2.5-minute `ai-explainer`: framework shown before any example, a worked example (a hidden-instruction attack on a summarizer agent), a falsifiability case (a recipe blog's imperative sentences that look similar but aren't an attack), and a concrete audit task. Both worked examples were planned as generic/hypothetical from the start — not attributed to a real product or disclosed incident — and the plan deliberately avoided any split-screen/divider beats, sidestepping a divider-crosses-glyph bug class a prior sibling video had hit.

## Where it resisted

- The fact-check process flagged that the central claim — prompt injection as a real, recognized vulnerability class — needed an actual citation rather than being asserted; resolved by adding an on-screen OWASP Top 10 for LLM Applications (LLM01) citation to the rubric beat.
- GATE A caught genuine "shapes never change" errors on three beats (only one non-text shape across the whole hold, or a text-only scene with no shape at all) — fixed by adding real second shapes.
- Three rounds of GATE B failures on the first render pass: a reveal panel pushed off-frame because `set_x()` was setting a block's center rather than accounting for its internal left alignment, and several headers/citation lines landing past the safe-area ceiling or floor because buffs tuned for one beat didn't carry over to others with the same pattern.
- The first full render came back with 13 MAJOR underfill defects — fixed in two rounds: first by replacing a "shrink-only if too tall" scale guard that never grew content to fill available space with an unconditional grow-or-shrink formula, then by widening specific accent lines and panels for the last couple of percentage points.
- The 9:16 Short redesign hit the same portrait Manim CLI bug already documented in a sibling reel (frame_width staying at the 16:9 default despite a portrait `-r` flag) — but this time it wasn't caught immediately: a first diagnosis assumed a simpler "uniform-scale" limitation and a round of fixes for that produced literally no change in the measured 6-8% canvas-fill numbers, which forced tracing the real root cause with a standalone debug scene printing the actual active frame dimensions before the real fix (patching `config.frame_width` at import time) was applied.
- A wrong-handle bug was found by inspection: the Shorts auto-endcard generator defaulted to `@nikbearbrown` instead of this channel's `@HumanitariansAI`, fixed by re-running the tool with the explicit handle.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) drafted the beat sheet and narration, authored all 9 Manim scenes plus the 9 portrait relayouts for the Short, generated Kokoro audio, ran every GATE A/B/V pass, and diagnosed the real defects versus the documented false-positive watermark pattern. The misdiagnosis-then-correct-diagnosis of the portrait frame-width bug is a real example of iterative debugging: an initial fix attempt (rewriting several scenes to solve for buff instead of scale) produced zero improvement, which is what forced the deeper trace that found the actual cause. The fellow reviewed and approved the beat sheet (Gate P) before any audio generation, and the fact-check table shows her resolving two concrete open items: confirming the OWASP citation was needed and confirming both worked examples should stay fully hypothetical with no real company, product, or CVE named.

## Still open / understood now

- One MAJOR underfill finding remains on the long-form cut, understood as a sampling artifact of a skeleton-first reveal (an early frame sample catches the beat before all three rubric rows and the verdict are on screen; the full layout clears the floor once resolved) rather than a real defect.
- Two MAJOR underfill findings remain on the Short's auto-generated endcard, understood as an inherent characteristic of a sparse handle-only card when no beats are cut and there's nothing to tease — not editable without touching the shared toolkit.
- Publishing was not authorized for either the long-form or Shorts cut as of the last BUILD-LOG entry; masters stay in this folder only.
