# SOURCES — How Pitch Correction Works

## Executable evidence (this folder)

| Source | Used for |
|---|---|
| `pitch_demo.py` → `evidence/run.log`, `evidence/pitch_demo.json`, `evidence/*.wav` | every curve, number and listening clip in B02–B06 |
| `export_pitch_data.py` → `scenes/pitch/pitchData.ts` (toolkit) | the scenes' data and the typeset equations |
| `mix_listen.py` | B04 and B05 audio: narration + the run's WAVs, level-matched |

## Methods

| Source | Used for |
|---|---|
| A. de Cheveigné and H. Kawahara, "YIN, a fundamental frequency estimator for speech and music", *J. Acoust. Soc. Am.* 111(4), 2002 | the detector in `pitch_demo.py` (difference function, cumulative-mean normalisation, absolute threshold, parabolic interpolation) |
| E. Moulines and F. Charpentier, "Pitch-synchronous waveform processing techniques for text-to-speech synthesis using diphones", *Speech Communication* 9, 1990 | TD-PSOLA, the pitch shifter |
| ISO 16, standard tuning frequency (A4 = 440 Hz) | B01 |
| A. J. Ellis, cents (1885), equal temperament | B01, B03 (100 cents per semitone, 1200 per octave) |

## History

| Source | Used for |
|---|---|
| Wikipedia, "AutoTune" (read 2026-10-05) | released by Antares in September 1997; Hildebrand's pitch detection "involved autocorrelation"; "Cher's 1998 song 'Believe' popularized the use of AutoTune to deliberately distort vocals … the 'Cher effect'"; key assignment (Thom Yorke quote) |

Not used: Antares' product pages did not show a "Retune Speed" range when checked, so the
video says "speed" and quotes no product numbers.
