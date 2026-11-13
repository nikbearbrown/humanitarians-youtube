# Mycroft Project — Phase 6 · Explainable Autonomous Monitoring Copilot (9:16)

Production package for the vertical film.

**Runtime 3:51 (231.33 s) · 2160 × 3840 · 30 fps · native 9:16 · H.264 / AAC 48 kHz.**

> "Hi, I am Dhrumil Shah, and this video is about Mycroft Phase 6, where I built an explainable
> autonomous monitoring copilot that runs five research agents over the market every day, scores
> what deserves a human look, and writes down exactly why."

## What Phase 6 is

The integration phase. Earlier phases each built one kind of signal; Phase 6 runs five together
and makes the combination auditable.

| Agent | What it does | Fires when |
|---|---|---|
| **A** robust anomaly | rolling modified z-score (median + MAD, window 60) on return, volume and intraday range | `max\|z\| ≥ 4.0` |
| **B** peer weakness | ranked inside its own **Industry** — 50% weak 20-day return, 25% high volatility, 25% deep drawdown | `≥ .80` |
| **C** risk score | ranked across the market — 40% volatility, 35% drawdown, 25% intraday range | `≥ .80` |
| **D** thesis deterioration | 0–100 health from 5 ranked components (25/20/20/20/15 %) | `change over 20d ≤ −20` |
| **E** multivariate anomaly | `IsolationForest` (250 trees, contamination .03) over 8 features, **fit on training dates only** | `predict == -1` |

**Review priority** = A×2 + B×1 + C×2 + D×2 + E×2, maximum **9** — plain integer weights, no
learned model. Every flag writes its own reason with the triggering value, e.g.
`robust_anomaly(z=7.5) · risk_score=0.92 · thesis_change20d=-74.0 · isolation_score=0.025`.

## What it produced on 2026-02-11

| | |
|---|---|
| Tickers monitored | 120 |
| Flagged for review | 43 |
| Priority 5 or above | 3 |
| Agents firing | 29 thesis deteriorations · 15 high risk · 11 anomalies · 4 multivariate · 3 peer outliers |
| Top of queue | SPGI 8 · SCHW 6 · UNH 5 · EMR 4 · GD 4 |

Outputs: `latest_human_review_queue.csv`, `latest_event_log.json`,
`review_priority_historical_diagnostic.csv`, `monitoring_summary.json` — with
`human_decision` and `human_rationale` left `null` by design.

## The honest scene

Scene 13 asks whether the priority score means anything. Over six years the large-move rate rises
from **17.8%** at priority 0 to **34.4%** at 4, **39.4%** at 6 and **40.6%** at 8 — but it **dips
at 3, 5 and 7**, and the high scores are rare (n = 64 at priority 9). The film says so on screen
and ends the scene on *"A historical diagnostic, not a forecast."* That scene is not optional.

## Accuracy

Every figure on screen is quoted from the executed notebook. **The notebook was not re-run and the
dataset is not in this package, so nothing was recomputed.** `docs/FACTCHECK.md` gives the source
of each number (F1–F41) and the open items (W1–W5).

## Layout

```
README.md · BUILD-LOG.md · beat_sheet.json
docs/   PRODUCTION-PLAN.md (table, script, storyboard, music, captions, export checklist)
        FACTCHECK.md · NOTEBOOK-OUTPUT.txt
source/ the Phase 6 notebook
audio/  per-beat Kokoro narration · timings.json · final_mix.wav
captions/ cues.json · captions.json · VALIDATION.md
assets/ figures · music · sfx
scenes/remotion/  MycroftPhase6_9x16.tsx · MycroftPhase6Cover9x16.tsx
scripts/  make_beat_sheet → narration → captions → music → mix → sync → render
output/ the four masters   ·   storyboard/ _qc/ thumbnails/
```

## Advisory

> Research decision-support only. Agents prioritize evidence and anomalies; the human reviewer
> makes the final decision.

**Not published.** A rendered master is not permission to upload.
