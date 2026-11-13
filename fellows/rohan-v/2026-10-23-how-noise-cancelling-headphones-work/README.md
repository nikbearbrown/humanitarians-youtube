# How Noise-Cancelling Headphones Work — Rohan V.

STEM explainer, week of 2026-10-23 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

## This week's contribution

**Question.** How do noise-cancelling headphones make noise disappear, and why do some sounds get through?

**Prediction.** Going in, the working assumption was that a simulated feedforward headphone would cancel
steady low noise well and fail on high or sudden sounds, because of its timing.

**What I built/tried.** `anc.py`: a feedforward headphone at 48 kHz (outside mic, an 83 µs acoustic lead, 125 µs
of electronic latency, a 128-tap filtered-x LMS filter, an in-ear error mic) on synthetic engine hum, rumble,
voice babble, clatter and pink noise; and the phase rule 2·sin(φ/2), checked against a simulated late copy.

**Observed result.** Engine hum −25.5 dB, low rumble −31.4, voices −11.2, clatter +0.9 (slightly louder). Pink
noise: at least 10 dB quieter up to 315 Hz, some reduction up to 3,150 Hz, +0.5 to +2.3 dB from 4 to 8 kHz. A
0.1 ms timing error costs 3.6° at 100 Hz (−24 dB) but 72° at 2 kHz (+1.4 dB).

**Next experiment.** Add a passive ear-cup model and a feedback mic, and compare feedforward, feedback and
hybrid on the same noises.

## Human and AI work

**My decisions, implementation and verification:** chose both topics from four suggestions and gave this week's hours; review of the preview pending at the time of writing.

**AI tools/voices used and what they generated:** Claude (Claude Code) researched the physics and the products' documentation, wrote the simulation, the five scenes and the narration, rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** saying all headphones adapt in real time (many use fixed filters; the narration says mine does); unsourced attenuation figures; claims about who invented ANC; levelling the off/on clips separately (one clip, one gain, so the difference stays).

**What remains unverified or failed:** a simulation, not a real headphone; no passive-isolation model; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `95d5ff6`, checked 2026-10-23: origin/main `a187fab`
merged locally that day (Remotion 4.0.535), plus local commits adding this week's scenes and fixes
(not pushed upstream; the scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `AncWaves`, `AncSystem`, `AncPhase`, `AncTypes`, `AncCurve` (+ `916` siblings, each with its own phone layout) and `scenes/anc/` (kit + generated data) in the Brutalist toolkit.

**Inputs:** [`anc.py`](./anc.py) → [`evidence/`](./evidence/) (run.log, results.json, scene.json, the WAVs); [`export_anc_data.py`](./export_anc_data.py); [`mix_listen.py`](./mix_listen.py); [`MEASUREMENTS.txt`](./MEASUREMENTS.txt).

**Commands:**

```bash
python anc.py && python export_anc_data.py
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

Landscape — [`landscape/NoiseCancelling_RohanV.mp4`](https://drive.google.com/drive/folders/14Yhgb5Zwmr4JZk2mat7gXJTKMNDCOIYT) — 3840×2160 — 2:22 (142.50 s) — SHA-256 `354c809f00b37c6867bcf9eaae191a8472b44044783c8f6cc24f7450d6b36353`

Vertical — [`vertical/NoiseCancelling_RohanV.mp4`](https://drive.google.com/drive/folders/10e-2Fu4oCVwEOEgSsGb2QdDca-boVuec) — 2160×3840 — 2:22 (142.50 s) — SHA-256 `df0b440f0e51acf2a5f29c647ba812ae43f58bdf8bf9960e3d7dac9028a87851`

Week folder on Drive: [`2026-10-23/`](https://drive.google.com/drive/folders/1AY5DOJuUvMLFiJPpuiCOuQAmDVdbEfGO)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
