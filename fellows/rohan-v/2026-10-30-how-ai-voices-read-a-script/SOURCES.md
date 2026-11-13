# SOURCES — How AI Voices Read a Script

Full notes, URLs, confidence levels and the "do not say" list: `week-10/_research/facts-tts.md`. Checked 2026-11-01.

## Our narrator

- Kokoro-82M model card, VOICES.md and config.json (hexgrad, Apache 2.0). The model reads phonemes, not text. B01.
- kokoro-onnx 0.6.1, `tokenizer.py`: phonemizes with espeak-ng through `phonemizer` 3.4.0, and does no text
  normalisation of its own. B01, B02.
- espeak-ng 1.52.0, `docs/dictionary.md` and `dictsource/en_list`: a lookup dictionary plus letter-to-sound rules;
  heteronyms picked by flags from the word before. B02, B03.
- misaki 0.9.4, Kokoro's official G2P (not ours; it tags parts of speech with spaCy). Background.

## Method

- *Text-to-Speech Synthesis*, Cambridge University Press, 2009. The stages of a TTS system. Background.
- "RNN Approaches to Text Normalization: A Challenge," arXiv:1611.00068, 2016. Background.
- g2pE README (numbers, part of speech, dictionary, a model for unknown words). Background.
- "FastSpeech 2," arXiv:2006.04558, 2020. Phoneme input to avoid mispronunciation. Background.

## Phonemes

- *Dictionary of the British English Spelling System*, Open Book Publishers, 2015, ch. 2: about 44
  phonemes in RP, varying by accent. B01.

## Disclosure

- YouTube Help, "Disclosing use of altered or synthetic content". It does not address a stock synthetic narrator,
  so the on-screen disclosure is our choice, not a stated requirement. Background.

## Evidence

- `voice.py`, `export_voice_data.py`, `mix_listen.py` and `evidence/` in this folder. The audio check uses
  faster-whisper base, the model our `align.py` uses.
