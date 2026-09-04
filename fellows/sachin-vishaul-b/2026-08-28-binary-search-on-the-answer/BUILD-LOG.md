# BUILD-LOG — "Claude, Halved."

Session date: 2026-08-31 · Toolkit: `brutalist.art` (ai-explainer skill,
concept-explainer mode) · Cost: $0.00 · Register: Teardown, claude-liam
channel. Last of the 4 concept reels built this session.

## What was built

9-beat `ai-explainer` reel; B01-B05 are hand-written Manim scenes
(`scenes.py`), including a number-line halving animation and a side-by-side
monotonic/non-monotonic comparison for the falsifiability beat.

## Real bugs found and fixed, in the order hit

1. **GATE A ("shapes never change")**: `B03_Worked` originally used only
   `FadeIn`/one `Write` call — not enough to register as a real animation
   by the toolkit's own check. First attempt added a `Transform` between
   two Text objects (old guess → next guess); this did **not** fix GATE A
   (the checker apparently doesn't credit `Transform` between
   differently-worded Text mobjects the same way it credits a drawn
   shape). Real fix: added a `Create()`-drawn bracket line under the
   worked example's boxes — a genuine geometry-drawing animation.
2. **GATE W (static pre-flight, no render)**: that same `Transform`
   addition then tripped a *different* gate — `guess`/`next_guess`
   flagged as 100% text-on-text overlap, because GATE W's static analysis
   sees both Text objects referenced in the `Transform()` call and doesn't
   model that only one of them ends up rendered. Resolved by removing the
   `Transform` entirely once the `Create()` bracket had already fixed
   GATE A on its own.
3. **GATE W, separately**: `B05_Monotonic`'s two-line caption was flagged
   `OFF-FRAME` — bbox wider than the canvas. Tried
   `.scale_to_fit_width()` first; **this did not fix it**, because GATE W
   reads the literal `font_size` argument in the source text and never
   sees a runtime scale call applied after construction (it's a
   static/heuristic check, not a real render). Real fix: lowered the
   literal `font_size` in the `Text(...)` call itself, from 24 to 18.

## Known gaps in this submission

- **9:16 cut not built.**
- **PROOF-REVIEW: pending.**
