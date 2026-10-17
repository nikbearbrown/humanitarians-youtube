# Nothing Errored

**Volunteer:** Kehinde Obidele

A STEM explainer built on my own repo, [loom](https://github.com/Kenny0bi/loom):
an MLOps platform with experiment tracking, a model registry, drift monitoring and
canary rollouts, proven on a simulated year of production life.

## Video Files

On the shared Google Drive under `Medhavy_Kehinde/STEM Topic/nothing-errored/`:

**[Google Drive folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp)**

| File | Aspect | Spec |
|---|---|---|
| `nothing-errored.mp4` | 16:9 | 3840x2160, 30fps, 2m 39s |
| `nothing-errored-short.mp4` | 9:16 | 2160x3840, 30fps, native render |

## The one idea

A broken model does not look broken. It keeps answering every request, on time,
and the answers are worse. The output side gives you no signal at all, so the
signal has to come from the input side.

## What the year looked like

| | |
|---|---|
| Weeks 4 to 6, quiet | PSI 0.021 to 0.030, accuracy steady around 0.64 |
| Week 7, the routine shifts | PSI **1.72**, roughly **70x** higher; accuracy falls to **0.56** |
| Week 8, candidate earns the swap | canary **z = 5.4**, 0.69 against 0.53 |
| Week 11, a poisoned model | canary **z = −12.2**, 0.26 against 0.74, rolled back automatically |

Not one request errored during any of it.

## The gate

A retrained candidate does not simply replace production. It takes a slice of real
traffic and has to earn the swap: promote above z of +2, roll back below −2, and a
tie keeps the incumbent, because the model already carrying the load wins a draw.

In week 11 I deliberately promoted a model trained on poisoned labels, skipping the
evidence. The platform caught it, reverted production and wrote the reason onto
both records without a human in the loop.

## A bug the demo caught in its own platform

The first weekly window had only **112 samples**, and the drift test fired a false
RETRAIN on data that had not changed at all, purely from binning noise. A monitor
that cries wolf gets switched off, which is worse than not having one.

## A note on the figures

Every number above was recomputed from `assets/lifecycle.json`, the committed
record of the run, rather than from the repo README. Where the two disagreed the
run data was used: the README narrates the week 7 drop as "0.70 to 0.56" where the
data records 0.638 to 0.555. That discrepancy should be fixed in the source repo.

The animation is my own Manim scene, re-rendered at 3840x2160 rather than upscaled.

## Files in this repo

- `beat_sheet.json` — the script
- `PEDAGOGY.md` — narration gate, VERDICT: PASS
- `FACTCHECK.md` — every on-screen claim, its source, and the algebra check
- `SHOTLIST.md` — typed work order
- `PROMPTS.md` — the on-screen prompts, plus the Manim build note
- `FRICTIONAL.md` — dated record of the work

Media files are not committed.
