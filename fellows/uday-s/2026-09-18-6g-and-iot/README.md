# The Constraint Isn't Speed

**Fellow:** Uday Sonawane
**Date:** 2026-09-18
**Format:** `ai-explainer` chassis on the `claude-hai` channel key (Brutalist)
**Runtime:** ~3:51 (231.45s measured) · 11 beats
**Master:** **3840×2160 @ 24fps, true 4K** (~15 MB), verified by `ffprobe`
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Audience:** students — smart people getting started
**Deliverable (local):** `6G_UdaySonawane_09_18_2026.mp4`

First reel in this folder shipped as a **native 4K master**. `./art final`
recompiled at 2160 from the existing slots with **no beat re-rendered** — every
source asset was already 4K (Manim at 2160p24, Remotion at `--scale=2`). The
`-slate.mp4` review cut stays 1080p; it is a working artifact with timecode
burn-in and 4K would buy nothing there.

## What this video is about

"Pros and cons of 6G for IoT" invites two bullet lists, which is the weakest
possible shape — nothing stops it becoming a feature inventory. The ask that
fixed it was *what actually decides whether an IoT deployment happens? Rank the
real constraints — then check whether the new generation's headline numbers are
on that list at all.*

**They are not. The framework (B02, on screen at 26.90s):**

- **POWER** — what the node's energy budget allows
- **COVERAGE** — whether the network reaches where the node is
- **COST PER NODE** — what each additional device costs to deploy

Both the upside (B04, B05) and the downside (B06) are scored on those same three
axes, so the verdict in B08 is a **comparison rather than a tally**.

Speed is not on the list. That is the title.

## The falsifiability beat

B07 uses a named forecast from a vendor with every incentive to say otherwise —
*find the forecast that would embarrass this technology's marketing, from a
named source, about the year it launches.*

**Ericsson's own IoT forecast: in 2030 — 6G's launch year — 40% of cellular IoT
connections are still projected to be NB-IoT and LTE-M**, technologies
introduced 2015–2017. Four in ten connections not using the generation the
forecaster sells.

The framework predicts exactly that: a new generation will not displace what
already satisfies power, coverage and cost.

## Discipline for a forward-looking topic

6G coverage is overwhelmingly projection, so three rules were applied:

1. **Only named standards bodies or named forecasts** — ITU-R, 3GPP, Ericsson.
   No trade-press figures.
2. **Forecasts are spoken as forecasts** — "projects", never "will be". Three
   rows in `FACTCHECK.md` are marked `PASS-AS-FORECAST` for exactly this.
3. **The most quotable number was cut.** IMT-2030's peak-rate and latency
   targets were available and are absent — they would undercut the thesis and
   date the reel the moment the targets are revised.

One claim was deliberately weakened: an early draft said 5G's massive-IoT
promise "never materialised" — commentary, not measurement, and a verdict on a
previous generation. The beat now makes only the narrower claim the forecast
supports.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Every on-screen figure against ITU-R / 3GPP / Ericsson |
| `FACTCHECK.md` | Claim-level verdicts, incl. the `PASS-AS-FORECAST` rows and the cut figures |
| `CHECKS-REPORT.md` | PROOF gate: 11 SHOW / 0 HOLD / 0 PUNT, with the teaching arc |
| `BUILD-LOG.md` | How the brief was reframed, forward-looking discipline, gate record |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts, incl. the two asks that shaped the reel |
| `scenes.py` | Authored Manim scenes for the eight data beats |
| `layout_audit.md` / `.json` | Frame-level layout audit |
| `mp3/timings.json` | Measured per-beat narration durations (the clock) |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/*.mp3`, `qc-sheet.png`, and the masters.

## Gate record

```
GATE L   searched before authoring; no reusable hit; 8 beats authored as Manim
GATE F   full paperwork set written up front
GATE A   clean on all eight, FIRST PASS
GATE W   clean on all eight, FIRST PASS
GATE B   pixel-true — 0 errors, 0 warnings, FIRST PASS, no re-renders
```

**Seven reels in, the layout helpers have needed no changes for three
consecutive builds** — kicker at `buff=0.72`, content-adaptive box widths,
`fit_src()` reserving the citation strip, every label composed into the fitted
group, `_fit()` scaling up as well as down, never a line through text.

## Known accepted deviations

- **Framework lands at 26.90s**, past PROOF's "~20s" guidance. Measured and
  recorded rather than rounded down; still far ahead of the first 6G capability
  claim at 79.08s.
- The `22 BLOCKER` headline from `./art run` is GATE V reading `*-slate.mp4`,
  the review cut, whose timecode burn-in sits outside title-safe by
  construction.
- **`BUILD-LOG.md`'s gate record does not list a GATE V result for the clean
  cut** — unlike the earlier reels, which all recorded frame/BLOCKER/MAJOR
  counts. Only the slate-pass headline is noted.
- **No `PROOF-REVIEW.md`.** The PROOF self-assessment lives as a table inside
  `BUILD-LOG.md`, as with the other 2026-09 packages.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Repo: https://github.com/nikbearbrown/brutalist.art

Audio-first, Kokoro-only, no API keys. Full prompt path is in `PROMPTS.md`.

## Publishing

Not authorized by this package. The master stays local until a human decides to
share or upload.
