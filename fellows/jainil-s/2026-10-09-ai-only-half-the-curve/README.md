# You're Only Seeing Half the Curve

**Track:** educational (STEM / AI) · **Week ending:** 2026-10-09

> More parameters means more overfitting — until it doesn't. Past the point
> where a model has exactly as many parameters as training examples, test error
> spikes, and then falls again, below the best the textbook rule can reach.

Two cuts are delivered separately: a 16:9 master at 3840×2160 and a 9:16 Short
at 2160×3840. **No video files are in this repo** — everything here is the
record of how they were built and why each claim holds.

## The argument

The bias-variance curve every course draws is real and it is incomplete. It
describes what happens while a model has *fewer* parameters than it has training
examples. Cross that line and three things happen that the textbook picture has
no room for:

1. **The error spikes.** Not climbs — spikes. At exactly `parameters = training
   examples` there is only one parameter setting that fits the data, and you get
   it whether it is sensible or not. In our experiment it is **159× worse** than
   the best classical model.
2. **It comes back down, and keeps going.** Past the threshold, many settings
   fit the data exactly, so the fitting procedure can *choose* — and minimum-norm
   least squares picks the smallest, smoothest one. Error falls **below** the
   classical optimum: 0.29 against 0.70.
3. **Training loss goes blind.** It reaches zero at the threshold and stays
   there. Every model to the right is perfect on the training set while the test
   error swings through a factor of nearly 400.

The practical consequence, which is the reason the video exists: **stopping the
moment validation error turns upward can mean stopping at the worst point on the
curve.** Whether that applies to you depends on where you stopped, which almost
nobody checks.

## Reproduce it

```bash
python double_descent_evidence.py
```

Pure numpy. No scikit-learn, no dataset download, no GPU, a few seconds to run.
Every figure spoken or shown in the video is printed by this file: 12 seeds,
median over seeds, `n = 100` training examples fixed while `p` sweeps 2 → 4000.

The model is ridgeless (minimum-norm) least squares on `p` random Fourier
features. The feature directions are drawn **once** and reused as `p` grows, so
the 200-feature model literally contains the 100-feature model's features — only
capacity moves along the x axis.

| | |
|---|---|
| Best below the threshold (`p = 60`) | 0.700 |
| At the threshold (`p = n = 100`) | 111.263 — 159× worse |
| Far past it (`p = 4000`) | 0.293 — below the classical best |
| Training error at `p ≥ 100` | ~1e-27 |
| Seeds where the modern regime wins | **12 / 12** (worst seed 18% better) |

## Beats

| # | Act | Scene | What it does |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | The practitioner's question, answered in two lines |
| B01 | BLUF | `BrutalistHesitantWriter` | "The error curve dips once." → **twice** |
| B02 | EVIDENCE | `DoubleDescentCurve` | The textbook U, on a linear axis, stated fairly |
| B03 | EVIDENCE | `DoubleDescentCurve` | Axis redrawn — the spike and the second descent |
| B04 | MECHANISM | `InterpolatorChoice` | One forced fit vs many, and why smoothness wins |
| B05 | EVIDENCE | `DoubleDescentCurve` | Training loss flat on zero while test error swings |
| B06 | SOURCE | `FormACard` | Belkin et al., PNAS 2019, verbatim |
| B07 | HANDOFF | `ClaudeComposerAsk` | A prompt for a model you actually abandoned |
| B08 | OUTRO | `HaiTitleOutro` | Title restate · @HumanitariansAI |

## Built for this reel

`DoubleDescentCurve` and `InterpolatorChoice`, each with a 9:16 variant — four
new scenes, all indexed and reusable. GATE L found no existing scene that plots
a curve with a called-out *peak*, a threshold marker and a staged reveal, and
nothing at all that draws "many curves through the same points, one chosen".

## Honesty notes

- **No numeric claim is made about deep networks.** These figures describe a
  linear model with random features. In a deep network the peak tracks effective
  model complexity, not a parameter count you can read off an architecture.
  Transferring our numbers would be the exact error the video is about.
- **The experiment was rebuilt three times** before the narration was written,
  because the first two configurations did not actually produce a second descent
  below the classical best. See `FACTCHECK.md` → "Changed during the build".
- **The axis changes between B02 and B03**, deliberately and out loud — the
  narration says the axis has to be redrawn, because the textbook plot genuinely
  cannot contain the number.
- **One mechanism claim is flagged as interpretation**, not theorem: minimum-norm
  is a theorem, "therefore smoothest" is its honest reading for this feature
  family. `FACTCHECK.md` row 10.

Full claim-by-claim ledger in `FACTCHECK.md`; every source in `SOURCES.md`;
the build's own record in `FRICTIONAL.md`.
