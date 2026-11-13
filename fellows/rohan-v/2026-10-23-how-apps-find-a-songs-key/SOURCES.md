# SOURCES — How Apps Find a Song's Key

Full notes, confidence levels and the "do not say" list: `week-09/_research/facts-key.md`. Checked 2026-10-23.

## Method

- T. Fujishima, "Realtime chord recognition of musical sound: a system using Common Lisp Music," ICMC 1999.
  The pitch-class profile (chroma). B02.
- C. L. Krumhansl & E. J. Kessler, "Tracing the dynamic changes in perceived tonal organization in a spatial
  representation of musical keys," *Psychological Review* 89(4):334–368, 1982. The probe-tone key profiles. B03.
- C. L. Krumhansl, *Cognitive Foundations of Musical Pitch*, 1990. The Krumhansl–Schmuckler key-finding
  algorithm. B03.
- D. Temperley, "What's key for key? The Krumhansl–Schmuckler key-finding algorithm reconsidered," *Music
  Perception* 17(1):65–100, 1999. Background.
- E. Gómez, *Tonal description of music audio signals*, PhD thesis, Universitat Pompeu Fabra, 2006. Background.
- librosa 0.11.0 (`chroma_stft`, `chroma_cqt`; no key function); Essentia `KeyExtractor` (profile options,
  default "bgate"). Background.

## Evaluation

- MIREX Audio Key Detection: weighted score (right 1.0, fifth 0.5, relative 0.3, parallel 0.2). B05.
- mir_eval `key.weighted_score` (same weights). Background.

## Practice

- Mixed In Key, Camelot wheel documentation (A = minor, B = major; relative keys share a number). B07.
- Serato DJ and rekordbox key display (official pages). B00.

## Evidence

- `songs.py`, `key.py`, `export_key_data.py` and `evidence/` in this folder.
