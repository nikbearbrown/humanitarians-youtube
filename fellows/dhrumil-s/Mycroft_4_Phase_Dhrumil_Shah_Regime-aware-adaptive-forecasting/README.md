# Mycroft Phase 4 — Regime-Aware Adaptive Forecasting (9:16)

Production package for the vertical film **"Mycroft Phase 4 — Teaching a Forecasting Model Where
It Is Wrong."**

**Runtime 3:05 (184.91 s) · 2160 × 3840 · 30 fps · native 9:16.**

> "Hi, I am Dhrumil Shah, and this video is about Mycroft Phase 4, where I added market-regime
> discovery and regime-aware thresholds so the system reports **where** its forecasts hold up,
> instead of one score for every market."

## What the film says

Phase 3 ended with one honest number: five-day price direction was close to a coin flip. Phase 4
asks whether that weakness is uniform — and finds it is not.

| | |
|---|---|
| Overall test ROC-AUC | **0.5178** (n = 26,760), Brier 0.2501 — still weak, and the film says so twice |
| `high_volatility` | 0.5359 (n = 1,080) |
| `sideways_mixed` | 0.5239 (n = 9,600) |
| `calm_bull` | **0.4909** (n = 16,080) — below chance, in the largest and calmest regime |
| Most useful feature | **`regime_id`**, ahead of the next feature by roughly 11× |

The deliverable is not a better score. It is a system that localises its own weakness and reports
it — and a research queue that only surfaces names clearing their regime's threshold by 0.08.

## What is in this folder

```
PRODUCTION-PLAN.md   the full plan — title, opening line, 14 scenes, narration,
                     visuals, code segments, diagrams, editing, layout, export specs
BUILD-LOG.md         how it was built, what was fixed, claim discipline
docs/FACTCHECK.md    every number with its provenance (F1-F37) and the open items (W1-W5)
docs/NOTEBOOK-OUTPUT.txt   the notebook's executed stdout, saved verbatim
beat_sheet.json      machine-readable scenes with measured start/duration
audio/               Kokoro narration per beat, timings.json, final_mix.wav
captions/            cues.json, captions.json, VALIDATION.md
assets/figures/      the notebook's own two figures, extracted unchanged
assets/music/, sfx/  code-synthesised bed and cues
scenes/remotion/     MycroftPhase4_9x16.tsx, MycroftPhase4Cover9x16.tsx
scripts/             narration -> captions -> music -> mix -> sync -> render
output/              the four delivered masters
storyboard/, _qc/, thumbnails/
```

## Accuracy

Every figure on screen is quoted from the author's executed notebook run. **The notebook was not
re-run and `Stock_Prices_Dataset.csv` is not in this package, so nothing was recomputed.**
`docs/FACTCHECK.md` records the source of each number and lists what is still work in progress:
per-regime calibration, the regime-label naming step, the untestable `stressed_bear` sample, and
the single-window threshold tuning.

The two charts are the notebook's own matplotlib output, carried over unchanged — including the
negative bars in the importance chart. The only drawn-not-measured visual is the pair of
sparklines in S03, labelled on screen as illustrative.

## Advisory

> Research queue for human review. Educational research output — not financial advice.

Shown in S13 and again on the end card, as in the source notebook's framing.

**Not published.** A rendered master is not permission to upload.
