# How Auto-Captions Find Each Word — Rohan V.

STEM explainer, week of 2026-10-26 to 2026-10-30 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

## This week's contribution

**Question.** How does speech recognition write captions and time each word, and how far can it be trusted?

**Prediction.** Going in, the working assumption was that Whisper would be nearly perfect on clean narration,
that its word times would be close, and that noise would make it fail gradually.

**What I built/tried.** `captions.py`: 24 Western sentences (238 words) built word by word from the narrator's
voice, so every true word start is known; faster-whisper base (the model our align.py uses) with word
timestamps, clean and with pink noise at +20, +10, +5, 0 and −5 dB SNR; WER by Levenshtein alignment.

**Observed result.** Clean: 234 of 238 words right (WER 1.7%); word starts a median 0.24 s early, 9 in 10 within
0.3 s. +10 dB 2.9%, +5 dB 10.9%, then a cliff: 0 dB over 70% (73.1% in the final run); at −5 dB it wrote over
300 words for 238, in repeat loops. On clean speech it writes what it expects ("Row-Haan" → Rohan).

**Next experiment.** Repeat the noise test with the small and medium Whisper models and with real room
recordings instead of pink noise.

## Human and AI work

**My decisions, implementation and verification:** chose both topics from four suggestions and gave this week's hours; review of the preview pending at the time of writing.

**AI tools/voices used and what they generated:** Claude (Claude Code) researched speech recognition and caption guidance, wrote the test program, the five scenes and the narration, rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** a first run whose word starts were 0.85 s off because 24 kHz audio was read as 16 kHz (resampled); scoring "9" against "nine" as an error (numbers spelled out first); exact noisy-run figures in the narration (they vary between runs; "over seventy percent" and "over three hundred" hold for both); claims that YouTube uses Whisper or any accuracy figure for YouTube (unverified).

**What remains unverified or failed:** one model size, synthetic noise, one voice; what YouTube's own recogniser does; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `3103d150`, checked 2026-11-01: origin/main `a99b532`
merged locally that day (Remotion 4.0.535), plus local commits adding this week's scenes and fixes
(not pushed upstream; the scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `CapSpectro`, `CapTiming`, `CapAccuracy`, `CapNoise`, `CapCatch` (+ `916` siblings, each with its own phone layout) and `scenes/captions/` (kit + generated data) in the Brutalist toolkit.

**Inputs:** [`captions.py`](./captions.py) → [`evidence/`](./evidence/) (run.log, results.json, scene.json, the WAVs); [`export_cap_data.py`](./export_cap_data.py); [`mix_listen.py`](./mix_listen.py); [`MEASUREMENTS.txt`](./MEASUREMENTS.txt).

**Commands:**

```bash
python captions.py && python export_cap_data.py
python runtime/scripts/generate_audio_kokoro.py <reel> && python runtime/scripts/align.py <reel>
python mix_listen.py && python runtime/scripts/sync_cues.py <reel>
./art vertical <reel> && python vertical_strings.py
./art final <reel> --height 2160 --out <reel>
./art final <reel>/vertical --height 3840 --out <reel>/vertical
```

**Approvals and checks:** GATE F (FACTCHECK, SHOTLIST, PROMPTS), GATE T and Gate V on both cuts;
results in [`BUILD-LOG.md`](./BUILD-LOG.md) and [`TYPECHECK.md`](./TYPECHECK.md). No human approval
record is required for this reel type; none is claimed.

## Watch and review

Landscape — [`landscape/AutoCaptions_RohanV.mp4`](https://drive.google.com/drive/folders/1QbmXf3x_F2FGazzyBhfRNHv2q7fDmmCT) — 3840×2160 — 2:17 (136.92 s) — SHA-256 `df9167c57e64e050403d5f48784cc086b5364f355d9e728adce9eed2d2845df6`

Vertical — [`vertical/AutoCaptions_RohanV.mp4`](https://drive.google.com/drive/folders/13-P9eWyxNqWy4OsLsnJBow9lZiVM2WDs) — 2160×3840 — 2:17 (136.92 s) — SHA-256 `72089a97d106156c1e37c4cdb47a3b10295d382ba95fe9ce0c2259b63f3c5754`

Week folder on Drive: [`2026-10-30/`](https://drive.google.com/drive/folders/1_qj0XWilWw5mLy8kPWws-jyWFEGN7BOv)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
