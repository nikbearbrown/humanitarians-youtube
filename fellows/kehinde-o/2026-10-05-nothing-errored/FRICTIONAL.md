# Frictional log — Explainer: Nothing Errored

## 2026-10-05 — a model that kept answering and was quietly wrong

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/STEM Topic/nothing-errored/`)
- **Report:** [REPORT.md](REPORT.md)
- **Source project:** https://github.com/Kenny0bi/loom
- **Paired report:** [Fact-Checking Chapter 6](../2026-10-05-chapter-6-review/)

**What I was working on.** A STEM explainer on my own MLOps platform, paired with
the Chapter 6 report because both are about the same failure: something that still
responds correctly on the surface while being wrong underneath.

**What I tried, and what I expected.**
- I expected a failing model to look like a failure. It does not. It answers every
  request, on time, and the answers get worse.
- I expected the README's figures to be usable as written.

**Where it resisted, and what I did next.**
- **The README disagrees with the run data.** It narrates week 7 as accuracy
  falling "0.70 to 0.56". The committed `lifecycle.json` records 0.638 to 0.555.
  I used the run data and treated the README as stale. That is my own repository,
  so the discrepancy is mine to fix there.
- **My two visuals would have used different symbols for the same quantity.** The
  Manim scene renders PSI with live and reference terms. The equation beat I wrote
  used actual and expected. Two notations for one formula, forty seconds apart, in
  a video whose whole job is to make that formula legible. Changed the equation
  beat to match the animation.
- **The animation is much shorter than its narration.** Ten point seven seconds
  against nineteen. The pipeline retimes rather than truncates, so it plays at
  about 0.56 speed. For a chart animation with a caption that reads "the routine
  shifts, slowly", that is acceptable, but I checked frames rather than assuming.
- **The portrait version needed measuring, not eyeballing.** I cropped to the
  content bounds read off a frame and verified the result sits inside title-safe
  on all four edges before compiling, because guessing that crop cost a blocked
  master on an earlier video.

**What Claude contributed, and what I did with it.**
- Mine: the platform, the simulated year, the Manim scene, and the decision to
  pair this with Chapter 6.
- Claude's: the beat sheet, the figure verification against `lifecycle.json`, and
  catching the notation clash between the equation beat and my own animation.
- Accepted: leading on the week 11 saboteur, where I deliberately promoted a
  poisoned model and the platform reverted it without me. Admitting the planted
  mistake is more convincing than only showing the successes.
- Rejected/changed: an early narration described the demo as a care system. It is
  a simulation on synthetic logs, and saying otherwise would overstate it.
- Evidence: `assets/lifecycle.json` in the source repo; every figure in
  FACTCHECK.md traces to a field in it.

**What I understand now, and what I still do not.**
- Understood: uptime is not correctness. The output side of a drifting model gives
  no signal, so the signal has to come from watching the inputs.
- Understood: a monitor that cries wolf gets switched off. Mine fired a false
  retrain on 112 samples from binning noise alone, which is worse than no monitor.
- Not resolved: the whole year is simulated. Whether these thresholds hold on real
  traffic is not something this project shows.
