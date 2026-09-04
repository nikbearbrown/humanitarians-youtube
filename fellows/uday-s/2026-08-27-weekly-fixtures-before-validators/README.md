# Build the Defects First

**Fellow:** Uday Sonawane
**Date:** 2026-08-27
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:02 (182.23s measured) · 13 beats
**Master:** 1080p compiled for QC speed; underlying assets are 4K (Manim 2160p24, Remotion `--scale=2`)
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `9ef4e7f`

## What this video is about

The `market-sentiment` recipe had **six declared steps marked `[TODO: DEV]`**
and no test data. The week did not start with the validators — it started with
the corpus they would be graded against: **3 clean fixtures plus 18 catalogued
defects across 7 classes**, each with an exact locator and a named catcher.
Then step 1, `verify-provenance`, was revised so its digest excludes timestamps
and two runs stay comparable.

The reusable framework (B02, on screen at **19.05s**, ahead of the first
example at 31.20s):

```text
1  ENUMERATE          what kinds of wrong can this data be?
2  PLANT              one instance of each, with an exact locator
3  NAME THE CATCHER   which check must surface it
4  FREEZE             pin timestamps, so two runs stay comparable
```

The falsifiability beat (B09) is the case that **breaks step 1**: wrong-entity
signals are not covered by the corpus, and the manifest says so.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth); carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `SOURCES.md` | Every on-screen figure, how it was re-derived, plus deliberate omissions |
| `FACTCHECK.md` | Claim-level verdicts |
| `CHECKS-REPORT.md` | PROOF gate: 13 SHOW / 0 HOLD / 0 PUNT, with the teaching arc |
| `BUILD-LOG.md` | Decisions, gate history (A / B / V), and REVISION 2 |
| `PROOF-REVIEW.md` | Scored against the PROOF rubric |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts used to build the reel |
| `scenes.py` | Authored Manim scenes for the six data-animation beats |
| `layout_audit.md` / `.json` | Frame-level layout audit |
| `mp3/timings.json` | Measured per-beat narration durations (the clock) |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/*.mp3`, and the masters
(`Mycroft_UdaySonawane_08_28_2026.mp4`,
`weekly-fixtures-before-validators{,-slate}.mp4`).

## 9:16 Short — `short/`

A derivative vertical cut for YouTube Shorts, built with `./art shorts`.

**`weekly-fixtures-before-validators-short.mp4`** · 1080×1920 · ~1:27 (87.33s) ·
6 beats + silent endcard · GATE V **BLOCKER 0**

Seven beats were dropped to get under the 3:00 Shorts cap and to leave one
insight standing — **the four-step method and the case that breaks it**. Kept:
B00 INTRO, B01 PROBLEM, B02 FRAMEWORK, B05 OUTPUT, B09 FALSIFIABILITY, plus a
rewritten funnel outro. Full cut list and reasoning in
[`short/SHOTLIST.md`](./short/SHOTLIST.md).

The audio is the parent's, byte for byte; only the outro was regenerated, per
the Shorts Law. Manim run-times are copied verbatim — geometry changed, timing
did not. Both bookends render from `ClaudeComposerAsk916` /
`ClaudeTitleOutro916`; the four body beats are re-laid-out in
[`short/scenes.py`](./short/scenes.py) for the 4.5 × 8 portrait frame.

## Rendered video

The rendered cuts are not in this repo. Review copies of both of this fellow's
2026-08-27 reels — landscape and Short — are in Google Drive:

<https://drive.google.com/drive/folders/1T7zrj41hh10qB0qOU1LD3qJF6VL0qV0K>

This folder is for review only and is not a publication channel — see
**Publishing** below. The `.mp4` in the repo working tree stays gitignored; the
beat sheet, `scenes.py`, and `mp3/timings.json` here are what actually rebuild it.

## Provenance warning

This reel deliberately lives **outside** the repo it documents, breaking the
toolkit's "videos travel with their book" rule at the author's request. The
subject commit is therefore no longer implied by folder location —
`beat_sheet.json` (`source_repo`, `source_commit`) and `SOURCES.md` are the only
link between this reel and what it describes. Keep them accurate or the
provenance chain is broken.

## Known accepted deviations

- **38 frames (~10%) under the 55% canvas-fill floor**, all build-in ramps in
  B01/B04/B07/B08/B09 plus the deliberately sparse `ClaudeTitleOutro`. Recorded
  rather than silenced with `ART_STRICT=0`. GATE V: **BLOCKER 0** on the clean
  cut (the "24 BLOCKER" headline measures the review cut's timecode burn-in).
- **OUTRO-LOCK overridden** — `@HumanitariansAI`, not the claude-liam
  `@NikBearBrown` default. Logged in `BUILD-LOG.md`, not passed silently.
- `BUILD-LOG.md` §"Decisions that deviate" was written during the `af_bella`
  pass and still reasons from that voice; the shipped voice is `am_onyx` per
  REVISION 2 §3 and `beat_sheet.json`.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Repo: https://github.com/nikbearbrown/brutalist.art

Audio-first, Kokoro-only, no API keys. Regenerate narration first, then let the
measured durations drive the scenes — timing is never fixed by hand.

## Publishing

Not authorized by this package. The master stays local until a human decides to
share or upload.
