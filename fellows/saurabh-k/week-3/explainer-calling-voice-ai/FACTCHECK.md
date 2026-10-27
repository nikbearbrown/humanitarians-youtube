# FACTCHECK — hai-calling-voice-ai

Status: **GATE F — drafted 2026-10-26. 7 rows VERIFIED-LOCAL, 2 rows SPEC-ASSERTED, 1 row ARGUMENT.**

Verdict vocabulary: **VERIFIED-LOCAL** = checked against first-party evidence produced on this
machine during the build, reproducible by re-running the named command. **SPEC-ASSERTED** = a
statement about how the engine is documented to work, consistent with observed behaviour but not
independently re-derived. **ARGUMENT** = reasoning or advice, not a measurement.

**This reel is self-referential by design.** Its subject is the voice engine that narrates it, so
every claim is checkable against the audio the viewer is listening to.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B00 | The narrating voice is a model running locally, not the fellow's own | **VERIFIED-LOCAL** | Kokoro `am_onyx` via `generate_audio_kokoro.py`, 10 beats generated 2026-10-26, reported `cost $0.00`. Disclosure is spoken in B00 and recorded in the beat sheet metadata | Keep the disclosure spoken, not only written |
| 2 | B01/B02 | The model never receives your text; the text is converted to phonemes first | **VERIFIED-LOCAL** | `kokoro_onnx.Kokoro.create` source: `phonemes = text if is_phonemes else self.tokenizer.phonemize(text, lang)` followed by `tokens = self.tokenizer.tokenize(phonemes)`. The network is fed tokens derived from phonemes, never the characters | The public function still *accepts* text — the conversion happens inside. Keep the claim scoped to what the model receives |
| 3 | B04 | `"Calling voice AI."` becomes `kˈɔːlɪŋ vˈɔɪs ˌeɪˈaɪ.` | **VERIFIED-LOCAL** | `generate_audio_kokoro.py --phonemize "Calling voice AI."` run on 2026-10-26; output quoted exactly, stress marks included | Re-run if the phonemizer or its language default changes |
| 4 | B05 | One call returns an array of samples plus a sample rate: 24000 Hz, float32 | **VERIFIED-LOCAL** | `k.create('test', voice='am_onyx', speed=1.0, lang='en-us')` returned `sample_rate = 24000`, `dtype = float32`, 13904 samples for the word "test" | — |
| 5 | B06 | The model file is 310 MB and the voice file is 26 MB | **VERIFIED-LOCAL** | `ls` on `runtime/models/kokoro/`: `kokoro-v1.0.onnx` 310MB, `voices-v1.0.bin` 26MB, downloaded 2026-10-26 from the kokoro-onnx `model-files-v1.0` release | — |
| 6 | B06 | 54 voices across nine languages | **VERIFIED-LOCAL** | `--list-voices` returns 54 entries. Prefix counts: af 11, am 9, bf 4, bm 4, zf 4, zm 4, jf 4, pm 2, hm 2, hf 2, em 2, pf 1, jm 1, im 1, if 1, ff 1, ef 1. The leading letter encodes language: a and b are American and British English, e Spanish, f French, h Hindi, i Italian, j Japanese, p Portuguese, z Chinese — nine distinct languages | Recount if the voice pack is updated |
| 7 | B06 | It ran locally with no account and no key, at zero cost | **VERIFIED-LOCAL** | The generator printed `cost $0.00` for all 10 beats. The toolkit's own HOW-TO states "Zero API keys". No network call is made at synthesis time once the model files are present | The one-time model download does require network |
| 8 | B03 | Working definitions of phoneme, voice, sample rate, inference | SPEC-ASSERTED | Ordinary definitions, consistent with the observed behaviour in rows 2-5. Not quoted from a standard | Keep as working definitions |
| 9 | B07 | The model cannot clone a real person; every voice is a preset | SPEC-ASSERTED | `generate_audio_kokoro.py` header: *"The catch: no cloning — none of these voices is yours."* Consistent with the fixed 54-entry voice file in row 6, which contains no enrolment path | Confirm against the Kokoro model card before publishing |
| 10 | B07 | If you publish with a generated voice, say so out loud | **ARGUMENT** | Advice, not a finding. It is also this series' own practice — every reel discloses in B00 | Keep attributed as the series' practice |

## Honesty notes

- **Narration is AI-generated** (Kokoro `am_onyx`) and that is the subject, not an aside.
- **Rows 2 through 7 are first-party** — every number was produced by running the engine on this
  machine during this build, not read off a datasheet.
- **Row 2 is the one to watch.** "You don't send text" is true of what the neural network receives
  and false of the function signature, which takes a string. The narration is written to say the
  text is converted first, which is the accurate version.
- **Row 9 is the weakest.** It rests on the toolkit's own documentation rather than the upstream
  model card. That check is the fellow's before publishing.
