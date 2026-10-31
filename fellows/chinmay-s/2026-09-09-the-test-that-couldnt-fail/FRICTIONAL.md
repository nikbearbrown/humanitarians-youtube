# Frictional log — The Test That Couldn't Fail

## 2026-09-09 — 5:48, 26 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `build_beat_sheet.py`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** A teardown of a synthetic-data notebook whose evaluation
passes everything.

**What I tried, and what I expected.** I expected to reproduce its summary numbers and
walk through them.

**Where it resisted, and what I did next.**
* Reproducing the dataset at seed 42 showed the criterion in the summary is not the
  criterion the numbers were judged against. Same seven values, different line.
* The control run is degenerate: training on real data scores identically to the base
  rate, and F1 is exactly zero — it never once predicts the positive class.
* Correlations with the target are all under 0.014, so there was never a pattern to
  learn. Had to magnify the bars ~5,000× to be visible at all, and say so aloud in the
  reel rather than let the picture imply a signal.

**What Claude contributed, and what I did with it.** Mine: the decision to be explicit
about the magnification. Claude's: the reproduction, the assertions, 10 scenes.

**What I understand now, and what I still do not.**
* Understood: a scoreboard without a baseline beside it can certify anything.
* Not resolved: I never retrained the generator. The findings concern the dataset and
  the evaluation, both reproducible without a GPU, but the KS values would shift
  slightly on a retrain.
