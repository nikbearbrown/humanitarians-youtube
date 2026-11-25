# Frictional log — The Variable That Vanished

## 2026-09-21 — 5:31, 26 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `build_beat_sheet.py`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** A teardown of an SES→health causality notebook.

**What I tried, and what I expected.** I expected to check whether its causal-aware
model recovered the generator's true parameters.

**Where it resisted, and what I did next.**
* For income it does, almost exactly — naive `0.000353` → adjusted `0.000143` against a
  true `0.00015`. That part works and the reel says so.
* For education it does not. Education never appears in the health equation; its entire
  6.20-point effect travels through mediators, all of which are in the adjustment set.
  The model reports `+0.047, p=0.821` and the notebook reads that as "smaller." It is
  zero, and it was guaranteed before any data existed.
* Its own §3.3 is titled "Causal Feature Selection (What *not* to control for)."
* Also found the `income → access` arrow has coefficient `1e-8` — about 99× smaller than
  the noise on the same line. The edge is in the diagram and not in the data.

**What Claude contributed, and what I did with it.** Mine: the call to be fair — credit
the premise and the income result before showing the failure. Claude's: the reproduction,
the assertions, 8 scenes.

**What I understand now, and what I still do not.**
* Understood: adjustment is not a dial you turn up. What a control does depends entirely
  on where it sits in the graph, and the same model can be right and wrong in one fit.
* Not resolved: this is all inside a simulated dataset. "True effect" means true in the
  generator, which is a strong claim there and no claim at all outside it.
