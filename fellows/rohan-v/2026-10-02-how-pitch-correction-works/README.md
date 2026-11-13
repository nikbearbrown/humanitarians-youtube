# How Pitch Correction Works — Rohan V.

STEM explainer, week of 2026-10-02 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

> **Submitted late:** built and submitted on Monday 2026-10-05; I forgot to submit on Friday 2 Oct.

## This week's contribution

**Question.** How does a pitch corrector like Auto-Tune decide a sung note is off, and what do
its two big settings (the key and the speed) actually change?

**Prediction.** That a small detector-and-corrector could get a drifting melody to within a few
cents, and that leaving the key unset would send a badly flat note to the wrong neighbour.

**What I built/tried.** `pitch_demo.py`: synthesises a seven-note test melody (drift, scoops,
vibrato), detects pitch with YIN, snaps to the nearest note (chromatic or C major), glides there
with a retune time constant, shifts the audio with TD-PSOLA, and measures the result again.
The video plays the before and after.

**Observed result.** 39.9 cents off on average before; 2.8 cents after instant correction, 19.2
after slow (250 ms), re-measured. With every note allowed, the last note (75 cents flat of G)
lands on F♯4; with the key set to C major, on G4.

**Next experiment.** Try the same detector on a real recorded vocal (my own, with consent) and
compare with a commercial tool's result.

## Human and AI work

**My decisions, implementation and verification:** chose the topic (over the recommended text-to-speech), gave this week's hours, and directed the build; reviewed both cuts on 2026-10-06, no changes requested.

**AI tools/voices used and what they generated:** Claude (Claude Code) wrote the evidence script, the six new scenes and the narration, verified the history against Wikipedia, rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** the recommended topic; a 62-cent wrong-note example whose vibrato flickered between notes (moved to 75 cents and re-voiced).

**What remains unverified or failed:** the detector has not been run on a real voice; commercial tools' internals are not published; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `098fbc8`, checked 2026-10-05: origin/main `22264a3`
merged locally that day, plus two local commits adding this week's scenes (not pushed upstream; the
scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `PitchCycles`, `PitchFindPeriod`, `PitchSnapCents`, `PitchMelodyFix`, `PitchRetuneSpeed`, `PitchWrongNote` (+ `916` siblings, each with its own phone layout) and `scenes/pitch/` (kit + generated data) in the Brutalist toolkit.

**Inputs:** [`pitch_demo.py`](./pitch_demo.py) → [`evidence/`](./evidence/) (run.log, pitch_demo.json, the WAVs the listening clips use); [`export_pitch_data.py`](./export_pitch_data.py); [`mix_listen.py`](./mix_listen.py); [`MEASUREMENTS.txt`](./MEASUREMENTS.txt).

**Commands:**

```bash
python pitch_demo.py && python export_pitch_data.py
python runtime/scripts/generate_audio_kokoro.py <reel> && python runtime/scripts/align.py <reel>
python mix_listen.py && python runtime/scripts/sync_cues.py <reel>
./art final <reel> --height 2160 --out <reel>
./art final <reel>/vertical --height 3840 --out <reel>/vertical
```

**Approvals and checks:** GATE F (FACTCHECK, SHOTLIST, PROMPTS), GATE T and Gate V on both cuts;
results in [`BUILD-LOG.md`](./BUILD-LOG.md) and [`TYPECHECK.md`](./TYPECHECK.md). No human approval
record is required for this reel type; none is claimed.

## Watch and review

Landscape — [`landscape/PitchCorrection_RohanV.mp4`](https://drive.google.com/drive/folders/1UwqjjrSjNVImmV4h0O-BlK2zqaZT8W_6) — 3840×2160 — 3:17 (197.38 s) — SHA-256 `4f5e7b5c45f5005e2947494ccd344aad1545d702d902024af634de2a219d2001`

Vertical — [`vertical/PitchCorrection_RohanV.mp4`](https://drive.google.com/drive/folders/1zTLwRuGQklj3NC5lyshPXgLxEBfGV06_) — 2160×3840 — 3:17 (197.38 s) — SHA-256 `492264e767ec41c49f272d709350086af37cc981269a197ee5357d03812c6042`

Week folder on Drive: [`2026-10-02/`](https://drive.google.com/drive/folders/1P5rUqd8BM9Y9-MWwsTVTNtMLx_0FmiEe)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
