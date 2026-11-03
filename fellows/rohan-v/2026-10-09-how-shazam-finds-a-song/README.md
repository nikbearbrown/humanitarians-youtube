# How Shazam Finds a Song — Rohan V.

STEM explainer, week of 2026-10-09 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

## This week's contribution

**Question.** How does an app name a song from five seconds of noisy audio, and what can't it hear?

**Prediction.** That a fingerprint built from a song's loudest points would survive cafe noise as loud
as the music, but fail as soon as the same song was played in another key or at another speed.

**What I built/tried.** `fingerprint.py`: the method of the 2003 Shazam paper (spectrogram peaks,
anchor/target-zone hashes, offset voting) on six synthetic songs (`synth.py`; no copyrighted audio),
tested with noisy, phone-band clips, a 180-clip noise sweep, and re-performances of the same song.

**Observed result.** 5 s of Song C in 0 dB cafe noise: 33 votes at exactly 12.00 s, 2 for the next
best. Sweep: 30/30 found at +10 dB, 29/30 at 0 dB, 22/30 with the noise 5 dB louder, 0/30 at 15 dB
louder, and never a wrong song. A semitone higher, 6% faster or hummed: 1, 4 and 1 votes, no match.

**Next experiment.** Try it on a recording of a real room (my phone, our own music), and test where
a tempo change stops matching.

## Human and AI work

**My decisions, implementation and verification:** chose the topic, gave this week's hours and asked for no late label; review of the preview pending at the time of writing.

**AI tools/voices used and what they generated:** Claude (Claude Code) wrote the fingerprinter, the synthetic songs, the six scenes and the narration, checked the facts against the 2003 paper and YouTube's help pages, rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** a first noise test that scored the start time on looping songs (songs rebuilt, scoring changed); a 'hum' that was a perfect copy of the lead (rebuilt to wander like a person); the claim that Shazam can't hear humming (unverified, so not made).

**What remains unverified or failed:** not run on a real recording or a real room; Shazam's production thresholds are not published; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `79eff6b`, checked 2026-10-10: origin/main `b21f625`
merged locally that day, plus local commits adding this week's scenes and fixes (not pushed
upstream; the scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `ShazamPeaks`, `ShazamHashPairs`, `ShazamOffsetVote`, `ShazamMatch`, `ShazamNoiseSweep`, `ShazamVersions` (+ `916` siblings, each with its own phone layout) and `scenes/shazam/` (kit + generated data) in the Brutalist toolkit.

**Inputs:** [`fingerprint.py`](./fingerprint.py) and [`synth.py`](./synth.py) → [`evidence/`](./evidence/) (run.log, fingerprint.json, the two WAVs the listening clip uses); [`export_shazam_data.py`](./export_shazam_data.py); [`mix_listen.py`](./mix_listen.py); [`MEASUREMENTS.txt`](./MEASUREMENTS.txt).

**Commands:**

```bash
python fingerprint.py && python export_shazam_data.py
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

Landscape — [`landscape/SongFingerprinting_RohanV.mp4`](https://drive.google.com/drive/folders/1ULEWIaIqfd9emKcYgctQ_hrt0zAVh44L) — 3840×2160 — 3:23 (202.58 s) — SHA-256 `5b24240fbbae7f1be861c22bf052bc20ca44fb4029e21af6bc411277f5c1c4ee`

Vertical — [`vertical/SongFingerprinting_RohanV.mp4`](https://drive.google.com/drive/folders/1xUcoXftnjYhqYjwUtuMK2eiTsrQI62q0) — 2160×3840 — 3:23 (202.58 s) — SHA-256 `c21324ac1adb5afb6c0d0048cdd62c39bc5f313bbb810bd063b4cc54cb85cb06`

Week folder on Drive: [`2026-10-09/`](https://drive.google.com/drive/folders/1JXFqKVB5WenIxrkxeeEGG_0JOfO8Z0_b)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
