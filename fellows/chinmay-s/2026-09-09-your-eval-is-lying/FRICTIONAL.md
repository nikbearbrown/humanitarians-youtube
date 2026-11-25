# Frictional log — Your Eval Is Lying to You

## 2026-09-09 — 5:57, 26 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `build_beat_sheet.py`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** A teardown of a prompt-engineering notebook whose metrics
all came back zero.

**What I tried, and what I expected.** I expected to explain prompt engineering and
report which prompt won.

**Where it resisted, and what I did next.**
* There was nothing to report. `OPENAI_AVAILABLE` was False, every prediction was the
  literal string `MOCK_OUTPUT`, and `plt.show()` happily drew four zero-height bars.
  The notebook cannot distinguish "the model failed" from "the harness failed."
* Running its own scoring functions surfaced three real bugs: `normalize_text` keeps
  periods, so a correct `"...is Paris."` scores **0.00** on both metrics; it strips
  non-ASCII, so `normalize("Brasília")` is `'bras lia'` and the answer key itself breaks.
* I had to decide whether to publish a critique of a notebook. Chose to, with the whole
  reel built from values recomputed by the notebook's own functions at build time.

**What Claude contributed, and what I did with it.** Mine: the decision to run the bug
angle rather than a straight walkthrough, and to stay on free local computation.
Claude's: finding the bugs, the scenes, the build-time recomputation.

**What I understand now, and what I still do not.**
* Understood: an all-zeros result is a symptom, not a measurement. The cheapest possible
  guard is handing your scorer an answer you already know is right.
* Not resolved: the reel makes no claim about whether chain-of-thought beat the baseline,
  because the notebook never called a model. That question is still unanswered.
