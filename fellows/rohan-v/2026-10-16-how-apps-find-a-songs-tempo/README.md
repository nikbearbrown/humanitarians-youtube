# How Apps Find a Song's Tempo — Rohan V.

STEM explainer, week of 2026-10-16 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

## This week's contribution

**Question.** How does an app work out a song's BPM from the sound alone, and where does it go wrong?

**Prediction.** Going in, the working assumption was that a classic detector (onset curve,
autocorrelation, a preference near 120 BPM) would get most clean drum-machine grooves right, and that
any misses would be exactly double or half.

**What I built/tried.** `tempo.py`: mel-band spectral flux, 8-second windowed autocorrelation,
librosa's default log-normal preference centred at 120 BPM, and an Ellis 2007 dynamic-programming beat
tracker, tested on 40 synthetic Western grooves (`grooves.py`: rock, funk, house, hip hop, slow ballad,
drum and bass, waltz, jazz swing; five tempos each), cross-checked against librosa 0.11.0, plus a
"live drummer" groove that speeds up from 120 to 123.4 BPM.

**Observed result.** Strongest repeat: 13/40 right, 20 misses exactly half. With the preference:
17/40 exactly right, 33/40 right or exactly double or half; every ballad doubled, every drum and bass
groove halved, funk thrown to a 4/3 repeat. librosa gave the same verdict on 34/40. On the drifting
groove, a fixed grid was up to 140 ms off; the beat tracker's median error was 6 ms.

**Next experiment.** Run it on our own Suno songs at the BPM their style prompts ask for, and see
whether the generated tempo matches the prompt.

## Human and AI work

**My decisions, implementation and verification:** chose the topic from four suggestions, limited the test set to Western grooves, approved downloading librosa's logo for the LOGO LAW, and gave this week's hours; review of the preview pending at the time of writing.

**AI tools/voices used and what they generated:** Claude (Claude Code) researched the method and scoring, wrote the detector, the synthetic grooves, the six scenes and the narration, rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** log-spaced bands that let the bass dominate; uncentred frames and an uncorrected 25 ms onset latency; whole-clip autocorrelation (librosa's 8-s windows used instead); naming any app's internal algorithm or genre tempo ranges (unverified).

**What remains unverified or failed:** not run on real recordings; how commercial apps choose a tempo is not documented; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `e758e22`, checked 2026-10-17: origin/main `4115560`
merged locally that day (Remotion 4.0.535), plus local commits adding this week's scenes and fixes
(not pushed upstream; the scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `TempoBeats`, `TempoOnsets`, `TempoAutocorr`, `TempoPrior`, `TempoGrid`, `TempoDrift` (+ `916` siblings, each with its own phone layout) and `scenes/tempo/` (kit + generated data) in the Brutalist toolkit.

**Inputs:** [`tempo.py`](./tempo.py) and [`grooves.py`](./grooves.py) → [`evidence/`](./evidence/) (run.log, results.json, scene.json, the groove WAVs); [`export_tempo_data.py`](./export_tempo_data.py); [`mix_listen.py`](./mix_listen.py); [`MEASUREMENTS.txt`](./MEASUREMENTS.txt).

**Commands:**

```bash
python tempo.py && python export_tempo_data.py   # librosa on PYTHONPATH adds the cross-check
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

Landscape — [`landscape/TempoDetection_RohanV.mp4`](https://drive.google.com/drive/folders/1vQFZdDag6dH7hFnyrmtsHsdTYe8Q6Rhi) — 3840×2160 — 3:22 (202.08 s) — SHA-256 `7ad56fbd866c2bef380e00b83fcfe1311f69a445f86ff793d8671155a32975af`

Vertical — [`vertical/TempoDetection_RohanV.mp4`](https://drive.google.com/drive/folders/12Sjys-7FJ2klZNPhihIldT9TLa3Mc_W5) — 2160×3840 — 3:22 (202.08 s) — SHA-256 `01d23230be380a8a3757502e8f5eda6d47aa028002b71c68db9bc754fc58bace`

Week folder on Drive: [`2026-10-16/`](https://drive.google.com/drive/folders/17pJ6dCN9-GP_vnSmeY3U5a4KKg59V85g)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
