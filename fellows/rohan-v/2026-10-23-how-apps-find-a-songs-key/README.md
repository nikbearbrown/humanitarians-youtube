# How Apps Find a Song's Key — Rohan V.

STEM explainer, week of 2026-10-23 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

## This week's contribution

**Question.** How does an app work out a song's key from the sound alone, and where does it go wrong?

**Prediction.** Going in, the working assumption was that the classic method (chroma, then the
Krumhansl–Kessler key profiles) would get clean synthetic songs right, and that its mistakes would land on
closely related keys.

**What I built/tried.** `key.py`: STFT chroma, a whole-song note profile, and correlation with the 24 rotated
Krumhansl–Kessler profiles, tested on 60 synthetic Western songs (`songs.py`: pop, rock with a flat 7th,
12-bar blues, minor with a raised 7th, natural-minor ballads; each in 12 keys), scored with the MIREX weights;
plus a pop song that moves up a semitone halfway.

**Observed result.** 50 of 60 right (mean MIREX score 0.883). Pop, rock, blues and raised-7th minor: 12 of 12
each. Natural-minor ballads: 10 of 12 named the relative major (A minor 0.886 vs C major 0.891). The key-change
song: the whole-song answer was C minor (wrong for both halves); 8-second windows heard C major, then C sharp major.

**Next experiment.** Run it on our own Suno songs, whose style prompts name a key, and see whether the
generated key matches.

## Human and AI work

**My decisions, implementation and verification:** chose both topics from four suggestions and gave this week's hours; review of the preview pending at the time of writing.

**AI tools/voices used and what they generated:** Claude (Claude Code) researched the method and scoring, wrote the detector, the synthetic songs, the six scenes and the narration, rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** log-compressed chroma that flattened every profile (energy per pitch class used instead); 4-second windows that heard chords, not keys (8 s used); a first script that called A minor the runner-up (it is G major); claiming which errors are most common in general (unverified).

**What remains unverified or failed:** not run on real recordings; how commercial apps detect keys is not documented; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `95d5ff6`, checked 2026-10-23: origin/main `a187fab`
merged locally that day (Remotion 4.0.535), plus local commits adding this week's scenes and fixes
(not pushed upstream; the scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `KeyNotes`, `KeyChroma`, `KeyProfiles`, `KeyGrid`, `KeyRelative`, `KeyChange` (+ `916` siblings, each with its own phone layout) and `scenes/keys/` (kit + generated data) in the Brutalist toolkit.

**Inputs:** [`key.py`](./key.py) and [`songs.py`](./songs.py) → [`evidence/`](./evidence/) (run.log, results.json, scene.json, the song WAVs); [`export_key_data.py`](./export_key_data.py); [`mix_listen.py`](./mix_listen.py); [`MEASUREMENTS.txt`](./MEASUREMENTS.txt).

**Commands:**

```bash
python key.py && python export_key_data.py
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

Landscape — [`landscape/KeyDetection_RohanV.mp4`](https://drive.google.com/drive/folders/14Yhgb5Zwmr4JZk2mat7gXJTKMNDCOIYT) — 3840×2160 — 2:40 (160.46 s) — SHA-256 `8aaaba05dc26112ebe94a8d262eb68b3fcb209e3202559094a4a41f4291532c8`

Vertical — [`vertical/KeyDetection_RohanV.mp4`](https://drive.google.com/drive/folders/10e-2Fu4oCVwEOEgSsGb2QdDca-boVuec) — 2160×3840 — 2:40 (160.46 s) — SHA-256 `3cb6c7ae32aa75f8b887bb9c2828868c078eedfaa1d3b46ae83cc023577fa7ae`

Week folder on Drive: [`2026-10-23/`](https://drive.google.com/drive/folders/1AY5DOJuUvMLFiJPpuiCOuQAmDVdbEfGO)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
