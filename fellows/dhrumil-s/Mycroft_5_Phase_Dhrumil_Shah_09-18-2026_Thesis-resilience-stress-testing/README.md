# Mycroft Phase 5 — Quantitative Thesis Resilience, Contradiction Detection & Stress Testing (9:16)

Production package for the vertical film.

**Runtime 3:49 (228.86 s) · 2160 × 3840 · 30 fps · native 9:16 · H.264 / AAC 48 kHz.**

> "Hi, I am Dhrumil Shah, and this video is about Mycroft Phase 5, where I built a quantitative
> thesis-resilience, contradiction-detection, and stress-testing framework to evaluate the health
> and risk of investment theses using market data."

## What the film explains

Earlier phases asked *will this stock go up or down?* Phase 5 asks whether the **quantitative
thesis** is still healthy, what evidence contradicts it, how it survives stress, and what an
analyst should look at first.

| Component | What the notebook does |
|---|---|
| Thesis health | 7 factors ranked cross-sectionally each date → a 0–100 score (weights 20/18/16/15/13/10/8 %) |
| Thesis state | broken < 35 · weakening 35–50 · stable 50–65 · strong > 65 |
| Deterioration | 5-day and 20-day health change, plus a drop to a worse state than 20 days ago |
| Contradiction | health falls 20 pts in 20 days, **or** weakens while trailing its sector, **or** > 8% below SMA-50 with a > 15% drawdown |
| Stress test | beta to the equal-weighted dataset market, idiosyncratic split, 3,000 bootstrapped 20-day paths, ×1.8 volatility, −8% day-1 shock |
| Tail risk | VaR 95% (the threshold) and CVaR 95% (the average beyond it) |
| Resilience | health ×.55 + (1−prob_loss) ×.20 + (1−prob_severe) ×.15 + volatility rank ×.10 → fragile / watch / resilient / high_resilience |
| Review priority | contradiction ×3 + weak band ×2 + sharp health drop ×2 + high severe-loss chance ×2 (max 9) |

**On 2026-02-11, 17 names reached priority 9** — ORCL, UNH and SPGI at the top, all in the
`fragile` band.

## The honest scene

Scene 13 measures what the contradiction flag is actually worth. Across all history, flagged rows
saw a large 5-day move **21.9%** of the time (n = 62,831) against **19.1%** for unflagged rows
(n = 120,707) — a real difference, but small, and the flag fires on about a third of all rows.
The notebook itself prints "Historical diagnostic (not a forecast)", and the film says the same.
That scene is not optional.

## Accuracy

Every figure on screen is quoted from the author's executed notebook run. **The notebook was not
re-run and `Stock_Prices_Dataset.csv` is not in this package, so nothing was recomputed.**
`docs/FACTCHECK.md` gives the source of each number (F1–F35) and the open items (W1–W5).

Both charts are the notebook's own matplotlib output, extracted from the `.ipynb` display data.
The one drawn-not-measured visual is the loss-distribution *shape* in S10 — labelled schematic on
screen; only the two marked ORCL values are real.

## Layout

```
PRODUCTION docs   README.md · BUILD-LOG.md · docs/STORYBOARD.md · docs/FACTCHECK.md
                  docs/NOTEBOOK-OUTPUT.txt (executed stdout, verbatim)
beat_sheet.json   14 scenes with measured start/duration and narration
source/           the Phase 5 notebook, kept with the package
audio/            per-beat Kokoro narration, timings.json, final_mix.wav
captions/         cues.json · captions.json · VALIDATION.md
assets/figures/   the notebook's two figures  ·  assets/music, assets/sfx
scenes/remotion/  MycroftPhase5_9x16.tsx · MycroftPhase5Cover9x16.tsx
scripts/          make_beat_sheet → narration → captions → music → mix → sync → render
output/           the four masters   ·   storyboard/ _qc/ thumbnails/
```

## Reproduce

```bash
python scripts/make_beat_sheet.py
python scripts/generate_narration.py
python scripts/build_captions.py
python scripts/generate_music_sfx.py
python scripts/mix_audio.py
python scripts/sync_to_remotion.py
python scripts/render_masters.py storyboard | review | late | master | cover | qc
```

Rendering needs the `brutalist.art-main` workspace — Remotion renders from its composition registry.

## Advisory

> AI-assisted quantitative research and decision support.
> Not financial advice, and not an autonomous trading system.

Shown in the S01 source line, on the S12 strip and on the end card.

**Not published.** A rendered master is not permission to upload.
