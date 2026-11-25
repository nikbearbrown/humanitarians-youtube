# Frictional log — Static Into Pictures

## 2026-10-12 — 4:16, 23 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `build_beat_sheet.py`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** A kid-friendly explainer of a from-scratch diffusion
notebook. The first of these notebooks with no defect to report.

**What I tried, and what I expected.** After three teardowns I went in looking for the
flaw.

**Where it resisted, and what I did next.**
* There isn't one. It ships a numerical gradient check, puts real baselines beside its
  results, and says plainly that the loss "does not go to zero, and it never will — that
  is not a bug." Hunting for a fault would have been dishonest, so the reel teaches.
* Rather than illustrate diffusion, the sprinkle scenes **run** it: every dot is placed
  by the notebook's own `x_t = √ᾱ·x₀ + √(1-ᾱ)·noise`, so the on-screen "% left" counter
  and the picture cannot disagree.
* The footprint scene for DDIM came out backwards — 200 steps drew 7 dots and 5 steps
  drew 26, because I mapped count inversely to step size. Also `Number("200 steps")` is
  `NaN`, so the track was empty on the first render.

**What Claude contributed, and what I did with it.** Mine: the call to teach rather than
tear down. Claude's: 7 scenes, the equation-driven animation, the fixes.

**What I understand now, and what I still do not.**
* Understood: when the animation computes the real thing, a whole class of "the picture
  implies something the data doesn't" errors becomes impossible.
* Not resolved: the spiral is drawn parametrically, so the *process* is exact but the
  point cloud is not a replay of the notebook's arrays.
