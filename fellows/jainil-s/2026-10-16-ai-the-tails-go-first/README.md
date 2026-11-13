# The Tails Go First

**Track:** educational (STEM / AI) · **Week ending:** 2026-10-16

> Train a model on its own output, over and over, and the average stays fine.
> What disappears is the rare stuff — quietly, and permanently.

Two cuts delivered separately: a 16:9 master at 3840×2160 and a 9:16 Short at
2160×3840, both 2:22. **No video files are in this repo** — this is the record
of how they were built and why each claim holds.

## The argument

Recursive generative training: each generation is a model fitted to the
previous generation's output, never to real data again. Start with a world that
has a rare subpopulation in it — 5% of the data, far from the bulk — and watch
what the loop does to it.

1. **The rare part thins out.** 4.5% at generation 0, 3.25% by generation 10,
   1.5% by generation 20, zero by generation 30.
2. **And then it is gone for good.** Extinct in **49 of 60 runs**, and in **0
   of those 49** did it ever come back. Nothing in the loop can reinvent a
   region once no sample occupies it.
3. **The model still looks healthy.** Mean moves +0.28 → +0.36. Standard
   deviation 1.60 → 1.67. Neither number says 5% of the world is missing.

Point 3 is the one worth carrying away: the diagnostics most people check are
exactly the diagnostics this failure does not move.

## Reproduce it

```bash
python collapse_evidence.py
```

Pure numpy, no download, seconds to run. 60 seeds, n = 200 per generation, 120
generations, medians over seeds. The script prints every figure in the video,
including the two density curves drawn on screen and the per-generation series
plotted on B04.

Each point carries a lineage label saying whether it descends from the rare
subpopulation. The model never sees the label; it exists so the script can say
exactly when the subpopulation is gone rather than inferring it from a
threshold that bulk outliers can drift across. The script prints the lineage
share beside the observable "fraction beyond x = 4" so you can confirm they
track.

## Beats

| # | Act | Scene | What it does |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | The question, answered in two lines |
| B01 | BLUF | `BrutalistHesitantWriter` | "and nothing is lost" → **the rare things are** |
| B02 | SETUP | `DistributionShape` | The world: a bulk, plus a rare 5% far out |
| B03 | TURN | `StageRail` | Real data → Gen 1 → Gen 2 → Gen n; real data seen once |
| B04 | EVIDENCE | `PositionCurve` | The share falling to zero and staying there |
| B05 | LAND | `DistributionShape` | Generation 40 with generation 0 ghosted behind, plus the healthy-looking stats |
| B06 | SOURCE | `FormACard` | Shumailov et al., Nature 2024, verbatim |
| B07 | HANDOFF | `ClaudeComposerAsk` | A prompt for a training set you own |
| B08 | OUTRO | `HaiTitleOutro` | Title restate · @HumanitariansAI |

## Built for this reel

`DistributionShape` + `DistributionShape916`. GATE L found nothing that could
draw a **ghost** of a previous shape behind the current one, which is what makes
B05 work — absence shown rather than asserted.

Two components were **reused unmodified**: `StageRail` (built for the
2026-10-09 weekly report) and `PositionCurve` (built for *Lost in the Middle*,
2026-10-02). `PositionCurve` gained an opt-in `plotScale` prop, defaulting to 1
so no existing reel changed.

## Honesty notes

- **No numeric claim about LLMs.** "Generation 20" and "49 of 60" are
  properties of this experiment at this sample size. Generation counts do not
  transfer to a language model and the reel does not imply they do.
- **This isolates one of the paper's three mechanisms** — statistical error
  from finite sampling. Expressivity and approximation error are real and are
  not shown here.
- **No claim that synthetic data is bad.** The finding is about *indiscriminate
  recursive* training with no real data re-entering the loop.
- **The experiment was wrong twice before it was right**, and both corrections
  are recorded in `FACTCHECK.md` — once because the model inflated variance
  instead of collapsing it, once because the metric let bulk outliers
  masquerade as the rare subpopulation.

Full ledger in `FACTCHECK.md`, sources in `SOURCES.md`, build record in
`FRICTIONAL.md`.
