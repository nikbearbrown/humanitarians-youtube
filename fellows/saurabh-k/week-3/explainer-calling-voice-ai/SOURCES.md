# SOURCES — hai-calling-voice-ai

The subject is the voice engine that narrates the film, so every source can be re-run and
heard. Claim-level verdicts are in [FACTCHECK.md](FACTCHECK.md).

## Where phonemization happens

`kokoro_onnx.Kokoro.create`, read on 2026-10-26:

```python
phonemes = text if is_phonemes else self.tokenizer.phonemize(text, lang)
...
tokens = self.tokenizer.tokenize(phonemes)
```

The network receives tokens derived from phonemes, never the characters. The public
function still *accepts* a string — the conversion happens inside. The narration is worded
to say the text is converted first, which is the accurate version of the claim.

## The phoneme shown in B04

```
$ generate_audio_kokoro.py --phonemize "Calling voice AI."
kˈɔːlɪŋ vˈɔɪs ˌeɪˈaɪ.
```

Quoted exactly, stress marks included. The portrait cut shows the shorter
`"voice"` → `vˈɔɪs`, verified by the same command, because the 16:9 string does not fit a
portrait code card.

## The call shown in B05

```python
k.create('test', voice='am_onyx', speed=1.0, lang='en-us')
# -> sample_rate = 24000, dtype = float32, 13904 samples
```

Run on this machine during the build.

## What it weighs (B06)

`ls runtime/models/kokoro/` after the one-time download from the kokoro-onnx
`model-files-v1.0` release:

- `kokoro-v1.0.onnx` — 310 MB
- `voices-v1.0.bin` — 26 MB

`--list-voices` returns **54** entries. Prefix counts: af 11, am 9, bf 4, bm 4, zf 4, zm 4,
jf 4, pm 2, hm 2, hf 2, em 2, pf 1, jm 1, im 1, if 1, ff 1, ef 1. The leading letter is the
language — a and b are American and British English, e Spanish, f French, h Hindi, i
Italian, j Japanese, p Portuguese, z Chinese. **Nine languages.**

The generator printed `cost $0.00` for all ten beats. The toolkit's HOW-TO states "Zero API
keys". No network call is made at synthesis time once the model files are present; the
one-time download does require network.

## No cloning

`generate_audio_kokoro.py` header: *"The catch: no cloning — none of these voices is
yours."* Consistent with the fixed 54-entry voice file, which contains no enrolment path.
This is the one claim taken from the toolkit's documentation rather than re-derived, and
confirming it against the upstream model card is still open.

## Narration

Kokoro `am_onyx` — the subject of the film, disclosed in B00.
