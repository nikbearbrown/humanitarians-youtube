# The Brand That Didn't Exist

**Fellow:** Uday Sonawane
**Date:** 2026-09-03
**Format:** `ai-explainer` chassis on the `claude-hai` channel key (Brutalist)
**Runtime:** ~3:04 (184.45s measured) · 11 beats
**Master:** 1920×1080; assets are 4K (Manim 2160p24, Remotion `--scale=2`), so `./art final` yields a true 4K master with no re-render
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Audience:** students — smart people getting started with AI
**Subject:** `D:/Projects/geo-main.zip` — a GEO research platform (code + results + paper)
**Deliverable (local):** `GenerativeEngineOptimization_2026-09-03.mp4`

## What this video is about

When you ask an AI which product to buy, some brands show up and some never do.
Generative Engine Optimization is the question of what decides that.

**The framework (B02, on screen at 21.06s — ahead of the first result at 39.47s):**

- **PARAMETRIC** — what the model already knows from training
- **PRESENCE** — whether your content is retrieved into the context
- **QUALITY** — whether that content is written to be quoted

Each lever is then measured in turn across the same nine brands (B03 → B04 →
B05), so the viewer watches one variable move at a time:

| Lever moved | Mean mention rate |
|---|---|
| Baseline, no retrieval | **50.3%** |
| + neutral retrieval | **86.7%** (+36.4) |
| + GEO-optimized content | **91.1%** (+4.4 over neutral) |

The bottom tier gains **+69.4** and the top tier **+11.7** — retrieval matters
far more if you start invisible.

Then B06 reframes all of it: **invent a brand that does not exist.** Cold, it is
mentioned 8.6% of the time (3 of 35). Give it retrieved content and it reaches
**90% and 95%** — and it is ranked **#1 in every case where it is mentioned.**
B07 is the falsifiability beat the framework predicts: if presence dominates,
fiction wins, so mention rate does not measure whether a product is good.

## Attribution — no author names

Per the author's instruction this is a **topic explainer, not a work report**.
No personal names appear anywhere, and the intro speaks none. On-screen credit
goes to `results/` filenames and one external citation (KDD 2024,
[arXiv:2311.09735](https://arxiv.org/abs/2311.09735)).

This is the one reel in this folder whose intro does not speak the fellow's
name — deliberate, not an omission.

## The verification, which is the real story

The archive ships **both the claims and the data behind them**, so the first
pass was verification rather than summary. Recomputing every headline figure in
the paper's abstract from `results/` found **seven that the shipped data does
not support** — including the model name and the direction of the "context
dilution effect".

Every finding's *direction* survives; the magnitudes and setup counts do not.

| Abstract says | Archive shows |
|---|---|
| HubSpot 87.1%, Copper 0% | 95.0% and 15.0% |
| Copper 0% → 100% under optimized RAG | 15.0% → 92.5% |
| Pseudo-brand 50% mention rate | 8.6% cold; 90% / 95% with RAG |
| 140 queries | 80 baseline records (20 prompts × 4 models) |

**The abstract's figures appear nowhere in the reel.** Every on-screen number is
recomputed from the shipped data and cited to the file it came from, at the
moment of the claim. No dilution claim is made at all. Full table, including the
three further failures, is in [`FACTCHECK.md`](./FACTCHECK.md).

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `FACTCHECK.md` | GATE F signed; every figure recomputed, plus the seven abstract claims that failed |
| `CHECKS-REPORT.md` | PROOF gate: 11 SHOW / 0 HOLD / 0 PUNT, with the teaching arc |
| `BUILD-LOG.md` | The verification decision, attribution, gate record |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts used to build the reel |
| `scenes.py` | Authored Manim scenes for the eight data beats |
| `layout_audit.md` / `.json` | Frame-level layout audit |
| `layout_audit_frames/*.png` | Sampled audit still |
| `mp3/timings.json` | Measured per-beat narration durations (the clock) |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/*.mp3`, `qc-sheet.png`, and the masters.

**No `SOURCES.md` in this package.** Unlike the Mycroft reels, the sourcing
ledger lives entirely in `FACTCHECK.md` — that file carries both the derivation
of every used figure and the list of rejected ones.

## Gate record

```
GATE L   searched before authoring; no reusable hit; 8 beats authored as Manim
GATE F   failed once — SHOTLIST.md and PROMPTS.md missing. Written, passed
GATE A   clean on all eight after one fix (stale duplicate assignment in bar_row)
GATE W   clean on all eight, first pass
GATE B   pixel-true — 0 errors, 0 warnings
GATE V   clean cut: 369 frames, BLOCKER 0, MAJOR 82 (78 underfill · 4 low-contrast)
```

One GATE B fix worth recording: B03's mean label was positioned relative to the
group *after* `fit()`, so when the group grew it landed on the citation. Fixed by
composing it into the fitted group — the same defect class the earlier reels hit.

## Known accepted deviations

- **82 MAJOR** on the clean cut (78 underfill · 4 low-contrast) — build-in ramps
  plus the sparse outro card; the low-contrast flags co-occur with near-blank
  beat openings. Accepted and documented, not silenced with `ART_STRICT=0`.
- The `BLOCKER` headline from `./art run` measures the `*-slate.mp4` review cut,
  whose timecode burn-in sits outside title-safe by construction.
- **No `PROOF-REVIEW.md`.** The PROOF self-assessment for this cut lives as a
  table inside `BUILD-LOG.md` rather than its own file, unlike the 2026-08-27
  packages.

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
