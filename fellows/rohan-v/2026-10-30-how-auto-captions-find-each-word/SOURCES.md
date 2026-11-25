# SOURCES — How Auto-Captions Find Each Word

Full notes, URLs, confidence levels and the "do not say" list: `week-10/_research/facts-asr.md`. Checked 2026-11-01.

## The model

- "Robust Speech Recognition via Large-Scale Weak Supervision," arXiv:2212.04356, 2022. 680,000
  hours, the 80-band log-Mel input, 30-second chunks, the decoder predicting tokens; repeat loops and
  hallucination among its limitations. B01, B05.
- openai/whisper repository: `audio.py`, `timing.py` (cross-attention + dynamic time warping), model card. B01,
  B02, B05.
- faster-whisper (SYSTRAN) and CTranslate2's `align`: the same timing method in the rebuild our pipeline runs. B02.

## Measuring

- NIST TREC-9 SDR, word error rate = (substitutions + deletions + insertions) / reference words. B04.

## Practice

- YouTube Help, "Use automatic captioning": captions may misrepresent speech; creators should review them. B06.
- W3C WAI, "Captions/Subtitles", and Understanding WCAG 2.2 SC 1.2.2. Background.
- WhisperX (INTERSPEECH 2023) and the Montreal Forced Aligner: forced alignment. Background.
- "Careless Whisper," ACM FAccT 2024: hallucination in 2023 API tests. Background; not stated.

## Evidence

- `captions.py`, `export_cap_data.py`, `mix_listen.py` and `evidence/` in this folder; B05's clean examples from
  `../2026-10-30-how-ai-voices-read-a-script/evidence/run.log`.
