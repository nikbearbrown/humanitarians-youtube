# BUILD-LOG — "Claude, Ringed."

Session date: 2026-08-31 · Toolkit: `brutalist.art` (ai-explainer skill,
concept-explainer mode) · Cost: $0.00 · Register: Teardown, claude-liam
channel.

## What was built

9-beat `ai-explainer` reel; B01-B05 are hand-written Manim ring diagrams
(`scenes.py`). This was the **first** Manim reel built this session — most
of the bugs found here were fixed once and then didn't recur in the other
three concept reels.

## Toolkit fix that made this reel possible

`manim` was not resolvable on PATH at all (`which manim` → not found; only
`python3` had a working shim). Added a matching shim
(`/c/Users/sachi/bin/manim` → the toolkit's venv `manim.exe`) and verified
it with a throwaway smoke-test render (circle + text, 1080p) before
authoring any real content.

## Real layout bugs found and fixed, in the order hit

1. Titles at `to_edge(UP, buff=0.5)` sat ~0.1 units outside the audited
   safe area. Fixed: `buff=0.75` on every title, all 4 concept reels.
2. Server labels placed via `.next_to(dot, p / norm(p) * 0.5)` used a
   non-unit direction vector that drifted toward the title band — a 25-93%
   text-on-text overlap with the title/other labels. First fix
   (`.move_to(p * 1.22)`) didn't move the label far enough and actually
   made the overlap *worse* once combined with a smaller ring radius.
   Real fix: shrink the ring radius from 2.6 → 1.9 for real headroom, keep
   the radial-push label placement.
3. A caption positioned via `.next_to(remap_arc, UP, ...)` landed on top of
   the "S5" label; moving it to a fixed screen position then landed on top
   of the ring's own circle stroke instead ("label on a curve" — the
   circle's stroke passed directly through the caption's bounding box).
   Fixed by moving both bottom captions to fixed coordinates below the
   ring entirely, clear of every drawn shape.
4. B01's BLUF text lines were wide enough to bleed past the frame's
   left/right edges in the final composited output (a Remotion-side GATE V
   BLOCKER — the final compile step conforms every beat to 4K, which can
   crop content that was already near the source frame's edge). Capped
   every BLUF line's width (`scale_to_fit_width(12.0)`) in all 4 concept
   reels as a guarantee independent of exact character count.
5. A stale cached `manim/B01.mp4` was reused after the source fix above —
   the pipeline only re-renders a Manim beat if its output file is
   missing. Had to delete the stale file to force a real re-render before
   the fix actually showed up in the compiled video.

## Known gaps in this submission

- **9:16 cut not built.**
- **PROOF-REVIEW: pending.**
