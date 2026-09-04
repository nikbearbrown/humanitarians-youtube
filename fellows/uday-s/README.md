# Uday Sonawane — Humanitarians AI fellow

Weekly work reports and AI explainers for the `@HumanitariansAI` channel, built
on the Brutalist audio-first chassis.

## Voice choice

**Voice:** Onyx (`am_onyx`)
**Register:** Pragmatist — method first, then when it applies and when it does not.
**Channel chip / handle on cut:** `@HumanitariansAI`

`am_onyx` was selected by the fellow and is recorded in every episode
`beat_sheet.json`. It is kept across this series; a change would be an explicit,
documented re-voice decision, not a per-episode default.

Note for the weekly-fixtures cut: `am_onyx` replaced an earlier `af_bella` pass
at the fellow's request. Because the toolkit is audio-first, that re-voice
re-timed the whole reel and every Manim scene was re-authored to the new
measured clock — see that episode's `BUILD-LOG.md`, "REVISION 2".

## Reports in this folder

- [2026-08-27 — Build the Defects First](./2026-08-27-weekly-fixtures-before-validators/) —
  weekly work report on `mycroft` @ `9ef4e7f`: building a defect corpus (3 clean
  fixtures, 18 catalogued defects) before writing any validator, then revising
  step 1 to verify provenance. 13 beats · ~3:02 · plus a 9:16 Short (~1:27).
- [2026-08-27 — State Space Models and Mamba](./2026-08-27-state-space-models-and-mamba/) —
  AI explainer on the `claude-hai` channel key: a STATE / UPDATE / COST rubric,
  applied to RNNs and Transformers, then SSM → S4 → Mamba, then the copying
  ceiling the rubric predicts. 12 beats · ~3:35 · plus a 9:16 Short (~1:48).
- [2026-09-03 — Transport, Do Not Repair](./2026-09-03-mycroft-weekly-transport-do-not-repair/) —
  weekly work report on `mycroft` @ `bdc1bc1`, **episode 2**: three questions for
  any pipeline stage (DECIDES / REFUSES / EVIDENCE), both steps scored on them,
  and the CRLF bug that breaks axis 3. 13 beats · ~3:22.
- [2026-09-03 — The Brand That Didn't Exist](./2026-09-03-generative-engine-optimization/) —
  topic explainer on Generative Engine Optimization: three levers (PARAMETRIC /
  PRESENCE / QUALITY), each measured, then a brand that does not exist reaching
  90% mention rate. 11 beats · ~3:04.

The two 2026-08-27 folders carry a `short/` subfolder: a derivative 1080×1920 cut
for YouTube Shorts, reusing the parent's audio with only the funnel outro
regenerated. Both Shorts pass GATE V with **BLOCKER 0**. The 2026-09-03 reels are
landscape only so far.

**Series continuity:** the Mycroft weekly is a running series — episode 1's
ledger closes on "gate 2 cannot clear", and episode 2 opens on that same list
and resolves two rows of it. Watch them in order.

**One exception to the voice/name convention:** *The Brand That Didn't Exist* is
a topic explainer, not a work report, and per the author's instruction it carries
**no personal names anywhere** — its intro speaks none. Every other reel here
opens with "I'm Uday Sonawane".

## Rendered videos

The rendered cuts are in Google Drive, not in this repo:

<https://drive.google.com/drive/folders/1T7zrj41hh10qB0qOU1LD3qJF6VL0qV0K>

Review copies only. That folder held the two 2026-08-27 reels and their Shorts
when it was linked; the 2026-09-03 masters may still need uploading.

## Publishing

No package here is authorized for publication. Masters and all audio/video
assets stay out of git; only the beat sheets, scene source, and review paperwork
are tracked here. The Drive folder above is a review location, not a release.

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Uday Sonawane

This folder organizes video projects built around beat sheets. Each project
README explains the subject and documents the free local rebuild workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

<!-- END BRUTALIST REBUILD GUIDE -->
