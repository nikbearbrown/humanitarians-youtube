# SOURCES — How Auto-Tune Works

Full notes, confidence levels and the "don't say" items: `week-13/_research/facts-autotune.md`. Checked
2026-11-19. Several of these pages, the patent included, print the inventor's name; it is not repeated here, in the
narration or on screen (fellows-repo rule), and one source whose web address contains it is listed without its URL.

## Release and patent

- Antares Audio Technologies, "About": Auto-Tune "was first released in 1997".
  <https://www.antarestech.com/about>. B06.
- Recording Academy, 2023 special merit award article ("in the spring of 1997"): the year agrees; the month is
  disputed between sources, so the film says only "in 1997". URL in the fact sheet (§1); left out here because it
  contains the inventor's name. B06.
- Sound On Sound, review of Antares Auto-Tune: first shipped as a Pro Tools (TDM) plug-in.
  <https://www.soundonsound.com/reviews/antares-auto-tune>. Background; not stated.
- US patent 5,973,252, "Pitch detection and intonation correction apparatus and method" (filed 15 Oct 1998, granted
  26 Oct 1999): pitch detection "derived from the auto-correlation function of the data"; pitch shifted by
  resampling, with whole cycle periods added or dropped to keep the length.
  <https://patents.google.com/patent/US5973252>. B01, B04.

## Where the maths came from

- Priceonomics, "The inventor of Auto-Tune" (2016): seismic data for oil exploration, read with autocorrelation.
  <https://priceonomics.com/the-inventor-of-auto-tune/>. B06.
- AAPG Explorer, "From rocks to rock: his ideas sound good" (2012).
  <https://www.aapg.org/news-and-media/details/explorer/articleid/2104/from-rocks-to-rock-his-ideas-sound-good>. B06.
- Autocorrelation pitch detection was already standard before Auto-Tune (IEEE Transactions on Acoustics, Speech and
  Signal Processing 25(1), 1977), which is why the film says "similar maths", not that it was invented for Auto-Tune.
  Background; not stated.

## "Believe" and retune speed

- NPR, "20 years of Cher's 'Believe' and its Auto-Tune legacy" (2018): the first famous use of Auto-Tune as an
  audible effect. <https://www.ctpublic.org/2018-10-22/20-years-of-chers-believe-and-its-auto-tune-legacy>. B03.
- Antares blog, "Cher's 'Believe' turns 20": the setting is Retune Speed; at zero it snaps the pitch to the nearest
  note instantly.
  <https://www.antarestech.com/blog/chers-believe-turns-20-song-helped-bring-auto-tune-mainstream>. B03, B07.
- TIME, 2009: the same description of zero retune speed.
  <https://content.time.com/time/subscriber/article/0,33009,1877372,00.html>. B03.
- Sound On Sound, "Recording Cher's 'Believe'" (Feb 1999), and MusicRadar, "25 years of Cher's 'Believe'" (2023):
  the vocoder cover story. <https://www.soundonsound.com/techniques/recording-cher-believe>,
  <https://www.musicradar.com/news/25-years-of-chers-believe-auto-tune>. Background; not stated (whether the
  sound was an accident is disputed, so the film doesn't say).

## How it works

- The patent (above): detection from autocorrelation; resampling plus whole cycles. B01, B04.
- The target is the nearest note of the chosen scale (chromatic by default; you pick the key to limit the
  targets); at normal speeds it glides and vibrato survives (fact sheet §4). B03, B07.
- Formant correction reached Auto-Tune's main mode later, with Auto-Tune Evo (2008; MusicRadar, 20 Aug 2008; Sound
  On Sound, Mar 2009; no URLs in the fact sheet). Why B04 speaks of the patent, not of today's product. Background;
  not stated.

## How common it is

- TIME, 2009, page 2 ("Some Auto-Tuning is almost unavoidable").
  <https://content.time.com/time/subscriber/article/0,33009,1877372-2,00.html>; NPR, 2018 (above). No reliable
  percentage of songs exists, so the film uses the fact sheet's safe wording. B06.

## Tuning

- ISO 16:1975: the A above middle C is 440 Hz. <https://www.iso.org/standard/3601.html>. B01.
- HyperPhysics, "Cents": 12 equal semitones per octave, 100 cents per semitone; the just-noticeable difference is
  about five cents; musicians do better (Hearing Research 219, 2006).
  <https://hyperphysics.gsu.edu/hbase/Music/cents.html>. B01, B02.

## Evidence and tools

- `autotune.py`, `mix_listen.py`, `build_hf.py`, `hyperframes/scenes/` and `evidence/` in this folder; the shared
  week kit in `week-13/_kit/` (`hfkit.py`, `kit3.js`, `add_qc.py`, `vertical_strings.py`); `week-13/run_audio.sh`.
- three.js 0.187.0 (MIT licence), shipped in `hyperframes/assets/` (`three.module.min.js`, `three.core.min.js`,
  `three-LICENSE.txt`); vendored for the week in `week-13/_vendor`.
- HyperFrames (HTML rendered to video, GSAP timeline); Kokoro `af_bella` for the narration; Source Serif 4 and
  Inter for type.
