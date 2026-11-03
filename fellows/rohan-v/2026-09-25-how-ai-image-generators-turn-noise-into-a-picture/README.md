# How AI Image Generators Turn Noise Into a Picture — Rohan V.

STEM video, week of 2026-09-25 · Humanitarians AI · Lyrical Literacy ·
GitHub `rohanvijaykumar`

## This week's contribution

**Question.** What actually happens between typing a Midjourney prompt and
getting four pictures back, explained for someone with no AI background?

**Prediction.** That it could be shown honestly on a model small enough to train
on a laptop, without claiming anything about Midjourney's unpublished internals.

**What I built/tried.** A toy diffusion model trained from scratch in numpy
(12,000 16×16 pictures of hearts and music notes, 1.6M parameters, 31 minutes on
CPU, no GPU, no downloads), a logged seed scan, and an exporter that feeds every
picture and number into five new Remotion scenes. The one equation is typeset
with the house renderer; Midjourney's own Seeds page is the only source for
Midjourney claims.

**Observed result.** From pure static the model produces clear hearts and music
notes in 1,000 steps. The same static under two prompts gives two different
pictures; one prompt under four seeds gives four different hearts (mean pixel
difference 52.2/255). All 40 scanned seeds produced both prompts recognisably.

**Next experiment.** _Proposed, not yet decided:_ show the same idea on a
text-conditioned model (one that reads a real prompt), if one can run locally and free.

## Human and AI work

**My decisions, implementation and verification:** chose the topic from fifteen
options after rejecting one that overlapped earlier videos; set the brief and the
"follow the framework to the T" rule; reviewed the plan.

**AI tools/voices used and what they generated:** Claude (Claude Code) merged the
Brutalist update, wrote and ran the model, seed scan and exporter, built the
scenes, rendered, and drafted these docs. Narration: Kokoro `af_bella`, my
persistent voice for the series (AI voice, disclosed on screen).

**What I rejected or corrected:** the first topic (sound → tokens: repeated the
MP3 and Nyquist videos); the first list of three topics. Before render: a caption
claiming Midjourney shows a "grid of four" (my own captures show one row of
four), and percentage "shares" that summed past 100%.

**What remains unverified or failed:** how Midjourney's own model differs from
the toy — not published. YouTube 4K playback is not yet checked (see below).

## Reproduce

**Brutalist version/commit and date checked:** `26894b5` (main, merged
with origin/main `6a8380a` on 2026-09-25) plus this week's scenes — checked
2026-09-25.

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json),
[`cues.json`](./cues.json), [`vertical/beat_sheet.json`](./vertical/beat_sheet.json);
scenes `DiffuseSeedStatic`, `DiffuseRainForward`, `DiffuseMixEquation`,
`DiffuseReverseRun`, `DiffuseSeedPrompt` (+ `916` siblings) and
`scenes/diffusion/` in the Brutalist toolkit.

**Commands, dependencies, inputs:**

```bash
python train_toy_diffusion.py      # ~31 min on CPU; numpy + Pillow only
python scan_seeds.py               # seed rule for B05
python export_toy_data.py          # writes scenes/diffusion/toyData.ts (needs matplotlib)
./art final path/to/2026-09-25-how-ai-image-generators-turn-noise-into-a-picture
./art vertical path/to/2026-09-25-how-ai-image-generators-turn-noise-into-a-picture
```

Evidence: [`MEASUREMENTS.txt`](./MEASUREMENTS.txt), [`evidence/`](./evidence/).

**Approvals and checks:** GATE F (FACTCHECK, SHOTLIST, PROMPTS present), GATE T
(type check) and Gate V (frame QC) on both cuts — results in
[`BUILD-LOG.md`](./BUILD-LOG.md). No human approval record is required for this
reel type; none is claimed.

## Watch and review

Landscape — [`landscape/ImageDiffusion_RohanV.mp4`](https://drive.google.com/drive/folders/1TYRVlCh91t0EzFt3ZYOAGAzgzXeNDHah) — 3840×2160 — 2:27 (147.92 s) — SHA-256 `a88affa64998ab5c5c0f3db2b661af2cd9603803e6e363c2ca24306a2a1b2e6c`

Vertical — [`vertical/ImageDiffusion_RohanV.mp4`](https://drive.google.com/drive/folders/1cNSkXK6U4DmUPhBRF8HIortJicGE8kCk) — 2160×3840 — 2:27 (147.92 s) — SHA-256 `fa8f813e023a5c0ec1ecb1a17c23f9c4e0467b13937b5e51e24883dac6df26c3`

Sources/large assets: none beyond this folder.

PM review status: pending
YouTube 4K processing check: pending upload
Professors' publication decision: pending

## Files

| | |
|---|---|
| [`beat_sheet.json`](./beat_sheet.json) · [`cues.json`](./cues.json) | the build contract and the word-clock anchors |
| [`train_toy_diffusion.py`](./train_toy_diffusion.py) · [`scan_seeds.py`](./scan_seeds.py) · [`export_toy_data.py`](./export_toy_data.py) | the executable evidence |
| [`evidence/`](./evidence/) · [`MEASUREMENTS.txt`](./MEASUREMENTS.txt) | every run's log, the record, the weights |
| [`FACTCHECK.md`](./FACTCHECK.md) · [`SOURCES.md`](./SOURCES.md) | every claim and its source; the algebra check |
| [`SOURCE-brief.md`](./SOURCE-brief.md) · [`PROMPT.md`](./PROMPT.md) · [`PEDAGOGY.md`](./PEDAGOGY.md) · [`PROMPTS.md`](./PROMPTS.md) · [`SHOTLIST.md`](./SHOTLIST.md) | the brief, design and per-beat plan |
| [`BUILD-LOG.md`](./BUILD-LOG.md) · [`FEEDBACK.md`](./FEEDBACK.md) · [`FRICTIONAL.md`](./FRICTIONAL.md) | what broke, reviewer notes, the frictional log |
| [`description.txt`](./description.txt) | the YouTube description |
| `qc-sheet-16x9.png` · `qc-sheet-9x16.png` | contact sheets of both masters |
