# How AI Music Generators Turn Text Into Audio — Rohan V.

STEM explainer, week of 2026-10-09 · Humanitarians AI · Lyrical Literacy · GitHub `rohanvijaykumar`

## This week's contribution

**Question.** What happens between typing a prompt into a music generator and hearing a song?

**Prediction.** That a small codec could squeeze music into a few hundred tokens a second and still
sound recognisable, and that even a tiny model would guess the next token far better than chance.

**What I built/tried.** `codec.py`: residual vector quantization on MDCT frames (12 k-means codebooks
of 1,024), a trigram next-token model, and a coarse-then-fine generator whose "prompt" picks the
training music; all on synthetic music (`synth.py`), measured on pieces it never heard.

**Observed result.** One codebook loses 16.7 dB of treble; twelve, 5.6 dB. Four codebooks = 375
tokens a second, 376 times less data than a CD. The model guesses the next token right 16.5% of the
time (blind guess 0.1%). Generated music copies at most 0.26 s from its training music.

**Next experiment.** Prompt Suno with and without named instruments and tempo, and compare how much
each version follows the words.

## Human and AI work

**My decisions, implementation and verification:** chose the topic, gave this week's hours and asked for no late label; review of the preview pending at the time of writing.

**AI tools/voices used and what they generated:** Claude (Claude Code) wrote the codec, the model and generator, the six scenes and the narration, fact-checked the published systems (SoundStream, EnCodec, MusicGen, MusicLM), rendered both cuts and drafted these docs. Narration: Kokoro `af_bella`, my one voice for
the series (AI voice, disclosed on screen).

**What I rejected or corrected:** describing Suno's internals (unpublished); a codec trained on too little music; a spectral weighting that tested worse; a quality metric that measured silence; a generator that replayed its training music.

**What remains unverified or failed:** Suno's own method; how much large models copy from their training music; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `79eff6b`, checked 2026-10-10: origin/main `b21f625`
merged locally that day, plus local commits adding this week's scenes and fixes (not pushed
upstream; the scene files are copied into [`scenes/`](./scenes/) here).

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json), [`cues.json`](./cues.json),
[`vertical/beat_sheet.json`](./vertical/beat_sheet.json); scenes `TokSampleCount`, `TokCodebook`, `TokResidual`, `TokCodecQuality`, `TokNextGuess`, `TokTextSteer` (+ `916` siblings, each with its own phone layout) and `scenes/tokens/` (kit + generated data) in the Brutalist toolkit.

**Inputs:** [`codec.py`](./codec.py) and [`synth.py`](./synth.py) → [`evidence/`](./evidence/) (run.log, codec.json, the WAVs the listening clips use); [`export_tok_data.py`](./export_tok_data.py); [`mix_listen.py`](./mix_listen.py); [`MEASUREMENTS.txt`](./MEASUREMENTS.txt).

**Commands:**

```bash
python codec.py && python export_tok_data.py
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

Landscape — [`landscape/AIMusicTokens_RohanV.mp4`](https://drive.google.com/drive/folders/1ULEWIaIqfd9emKcYgctQ_hrt0zAVh44L) — 3840×2160 — 3:29 (209.29 s) — SHA-256 `54ea386750c33e296393c2e29a19bc342217a5bedb1435f601e0952a3e06414d`

Vertical — [`vertical/AIMusicTokens_RohanV.mp4`](https://drive.google.com/drive/folders/1xUcoXftnjYhqYjwUtuMK2eiTsrQI62q0) — 2160×3840 — 3:29 (209.29 s) — SHA-256 `79a982f61e5d300feb42e8a5223cb879e6776233f27bf78023d4c15bbff35a67`

Week folder on Drive: [`2026-10-09/`](https://drive.google.com/drive/folders/1JXFqKVB5WenIxrkxeeEGG_0JOfO8Z0_b)

PM review status: pending · YouTube 4K processing check: pending upload · Publication decision: pending

Docs: [FACTCHECK](./FACTCHECK.md) · [SHOTLIST](./SHOTLIST.md) · [PROMPTS](./PROMPTS.md) · [BUILD-LOG](./BUILD-LOG.md) ·
[FRICTIONAL](./FRICTIONAL.md) · [SOURCES](./SOURCES.md) · [PEDAGOGY](./PEDAGOGY.md) · [FEEDBACK](./FEEDBACK.md) ·
[description](./description.txt)
