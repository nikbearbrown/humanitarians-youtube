# BUILD-LOG — "Claude, Nearest."

Session date: 2026-08-31 · Toolkit: `brutalist.art` (ai-explainer skill,
concept-explainer mode) · Cost: $0.00 · Register: Teardown, claude-liam
channel.

## What was built

9-beat `ai-explainer` reel; B01-B05 are hand-written Manim scenes
(`scenes.py`); UI only at the bookends per ILLUSTRATE LAW.

## Real bugs found and fixed while building this specific reel

1. **GATE A ("shapes never change")**: `B02_Framework` originally used two
   decorative dashed circles as its only geometry-changing animation.
   Removing them (to fix a GATE B collision, below) briefly left the scene
   with only opacity fades, which correctly failed the toolkit's own
   "not a static slide" check. Fixed by adding two real `Create()`-drawn
   similarity lines in their place.
2. **GATE B (layout audit)**: the dashed cluster circles in `B02_Framework`
   crossed directly through the "truck" label ("label on a curve").
   Dropped the circles entirely — the clustering is legible from dot
   placement alone.
3. **GATE B**: `B03_Query`'s query label, placed directly below the query
   dot, sat on top of a line drawn from that same dot. Moved the label to
   the side (`RIGHT`, not `DOWN`) since both connecting lines are steep.

Shared toolkit fixes (manim PATH shim, QC burn-in mask, audio-encoding bug)
covered once in the `kv-cache` folder's BUILD-LOG.md, apply here too.

## Known gaps in this submission

- **9:16 cut not built.**
- **PROOF-REVIEW: pending.**
