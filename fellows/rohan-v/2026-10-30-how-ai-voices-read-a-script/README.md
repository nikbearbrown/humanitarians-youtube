# How AI Voices Read a Script — Rohan V.

STEM explainer, week of 2026-10-26 to 2026-10-30 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

## This week's contribution

**Question.** How does a text-to-speech voice turn a script into sound, and where does it go wrong?

**Prediction.** Going in, the working assumption was that our narrator (Kokoro-82M) would mostly get the
voice right and that its mistakes would come from the words-to-sounds step, not the voice itself.

**What I built/tried.** `voice.py`: the narrator's own letters-to-sounds step (espeak-ng through phonemizer, as
kokoro-onnx 0.6.1 uses it) on 8 heteronyms in 16 sentences, 7 clean-up cases (titles, abbreviations, numbers,
a date, a time, a price), and the 4 respellings our scripts already use; Kokoro clips of the price and the
presenter's name before and after respelling, checked with faster-whisper base.

**Observed result.** Heteronyms: 10 of 16 sentences read right; only 2 of 8 words (live, tears) right both
ways. Clean-up: 6 of 7 as a person would say them; "$3.50" came out "dollar three. fifty". Respelling fixed all
four words (Rohan, dhol, sitar, tabla) at the phoneme level.

**Next experiment.** Run the same checks with a second G2P (misaki, which Kokoro's own pipeline uses) and
compare the heteronym score.

## Human and AI work

**My decisions, implementation and verification:** chose both topics from four suggestions and gave this week's hours; review of the preview pending at the time of writing.

**AI tools/voices used and what they generated:** Claude (Claude Code) researched the TTS pipeline, wrote the test program, the five scenes and the narration, rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** assuming the narrator uses misaki (it uses espeak-ng through phonemizer; checked in the installed package); a B03 line that said "read and read" so both readings sounded the same (reworded); narration that would itself mispronounce dhol and sitar (the respellings are used); a B04 line that said "one thousand and twenty-four", which the run never read (re-voiced).

**What remains unverified or failed:** one TTS system only; whether other voices make the same mistakes; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `3103d150`, checked 2026-11-01: origin/main `a99b532`
merged locally that day (Remotion 4.0.535), plus local commits adding this week's scenes and fixes
(not pushed upstream; the scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `VoicePipeline`, `VoiceG2P`, `VoiceHeteronyms`, `VoiceNumbers`, `VoiceRespell` (+ `916` siblings, each with its own phone layout) and `scenes/voice/` (kit + generated data) in the Brutalist toolkit.

**Inputs:** [`voice.py`](./voice.py) → [`evidence/`](./evidence/) (run.log, results.json, the clips); [`export_voice_data.py`](./export_voice_data.py); [`mix_listen.py`](./mix_listen.py); [`MEASUREMENTS.txt`](./MEASUREMENTS.txt).

**Commands:**

```bash
python voice.py && python export_voice_data.py
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

Landscape — [`landscape/AIVoices_RohanV.mp4`](https://drive.google.com/drive/folders/1QbmXf3x_F2FGazzyBhfRNHv2q7fDmmCT) — 3840×2160 — 2:16 (135.83 s) — SHA-256 `be35130f6924306d3d58ca5df7cdc415eb07fdcc28af1eaac803c31b1224de02`

Vertical — [`vertical/AIVoices_RohanV.mp4`](https://drive.google.com/drive/folders/13-P9eWyxNqWy4OsLsnJBow9lZiVM2WDs) — 2160×3840 — 2:16 (135.83 s) — SHA-256 `938ae583f5349b4d6ac064f67562f8b44b1417e17a74737d0a4f26ece254dcca`

Week folder on Drive: [`2026-10-30/`](https://drive.google.com/drive/folders/1_qj0XWilWw5mLy8kPWws-jyWFEGN7BOv)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
