# SOURCES — How Apps Find a Song's Tempo

Full notes, confidence levels and the "do not say" list: `week-08/_research/facts.md`. Checked
2026-10-17.

## Method

- D. P. W. Ellis, "Beat Tracking by Dynamic Programming," *Journal of New Music Research* 36(1):51–60,
  2007. DOI 10.1080/09298210701653344. Onset envelope from 40 Mel bands; autocorrelation weighted
  toward 120 BPM; dynamic-programming beat placement. B02–B04, B06.
- E. D. Scheirer, "Tempo and beat analysis of acoustic musical signals," *J. Acoust. Soc. Am.*
  103(1):588–601, 1998. Comb-filter resonators; notes their kinship with autocorrelation. Background.
- S. Dixon, "Automatic Extraction of Tempo and Beat from Expressive Performances," *JNMR* 30(1):39–58,
  2001. Halving or doubling as the most common error. B05 background.
- librosa 0.11.0 documentation and source: `beat.beat_track` (cites Ellis 2007; `start_bpm=120`,
  `tightness=100`), `onset.onset_strength` ("spectral flux onset strength envelope"),
  `feature.tempo` (prior on log2 BPM centred at 120, `std_bpm=1.0`, `ac_size=8`).
  https://librosa.org/doc/0.11.0/ · https://github.com/librosa/librosa. B02–B06, and the cross-check.

## Evaluation

- F. Gouyon et al., "An experimental comparison of audio tempo induction algorithms," *IEEE TASLP*
  14(5):1832–1844, 2006. The ISMIR 2004 contest.
- ISMIR 2004 tempo contest, Accuracy 1 / Accuracy 2 definitions (±4%; Accuracy 2 also counts ×2, ×½,
  ×3, ×⅓): https://mtg.upf.edu/ismir2004/contest/tempoContest/node7.html. B04–B05 scoring.
- MIREX Audio Tempo Estimation (two candidates, ±8%): https://music-ir.org/mirex/wiki/2014:Audio_Tempo_Estimation

## People and tempo

- D. Moelants, "Preferred tempo reconsidered," ICMPC 2002 (about 120–130 BPM, via secondary sources;
  hence "roughly" in B04).

## Practice

- Native Instruments Traktor support: half/double BPM detection and how to correct it.
- Serato DJ: beatgrids and the analysis "BPM Range" setting.
- rekordbox 7 manual: "Dynamic" beat-grid analysis for tracks with tempo changes. B06–B07.

## Logo

- librosa's own mark, `docs/img/librosa_logo_text.svg` from github.com/librosa/librosa (ISC licence),
  downloaded 2026-10-17 with Rohan V.'s approval into the toolkit's `icons/logos/librosa/` (LOGO LAW).

## Evidence

- `grooves.py`, `tempo.py`, `export_tempo_data.py` and `evidence/` in this folder. librosa 0.11.0 is an
  optional cross-check installed outside the repository (`PYTHONPATH`); `tempo.py` runs without it.
