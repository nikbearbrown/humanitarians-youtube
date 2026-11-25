# SOURCES — How Spatial Audio Works

Full notes, URLs, confidence levels, dates and the "do not say" list: `week-12/_research/facts-spatial.md`.
Checked 2026-11-10. Apple Support pages change often; the model lists on them were read on 2026-11-09 and are not
used in the narration.

## How we locate sound

- "On our perception of sound direction," *Philosophical Magazine*, 1907 (Lord Rayleigh): timing for low sounds,
  loudness for high ones; front and back confused when the head is still. B02.
- "Sound localization," *Handbook of Clinical Neurology* vol. 129, 2015 (open copy on eScholarship): timing and
  level cues, the spherical-head formula and its 8.75 cm radius, head shadow, the cone of confusion, outer-ear
  cues. B01, B02, B03.
- "Anatomical limits on interaural time differences: an ecological perspective," *Frontiers in Neuroscience*,
  2014: the range of the largest timing gap for real heads. Background for B01; not stated.

## The filters

- MIT Media Lab, KEMAR HRTF measurements (May 1994) and "HRTF measurements of a KEMAR," *JASA*, 1995: 710
  directions on a dummy head. B04.
- "The CIPIC HRTF Database," IEEE WASPAA, 2001: what an HRTF is, rendering by convolution, how much heads and ears
  differ. B04, B06.
- Dolby Professional, "Dolby Atmos for Mobile Devices": Dolby applies HRTFs to turn an Atmos mix into two-channel
  headphone audio. Background for B07; not stated.

## Head tracking

- Apple Newsroom, "Apple reimagines the iPhone experience with iOS 14" (22 Jun 2020) and "iOS 14 is available
  today" (16 Sep 2020): spatial audio with dynamic head tracking for AirPods Pro. B05.
- Apple Newsroom, "Apple introduces AirPods Max" (8 Dec 2020): gyroscope and accelerometer in the headphones and
  the iPhone or iPad; the sound kept anchored to the device. B05.
- Apple Support, "Control Spatial Audio and head tracking on AirPods" (read 2026-11-09): Off, Fixed and Head
  Tracked. B05, B07.
- "The contribution of head movement to the externalization and internalization of sounds," *PLoS ONE*, 2013:
  sounds that stay put are heard outside the head more often. Background for B05; not stated.

## Your ears

- "Localization using nonindividualized head-related transfer functions," *JASA*, 1993: someone else's filters
  bring front-back confusions. B06.
- Apple Newsroom, "Apple unveils new ways to share and communicate in iOS 16" (6 Jun 2022), "Apple announces the
  next generation of AirPods Pro" (7 Sep 2022) and "iOS 16 is available today" (12 Sep 2022): Personalized Spatial
  Audio from the TrueDepth camera. B06.
- Apple Support, "Listen with Personalized Spatial Audio for AirPods and Beats" (dated 23 Sep 2026): the front view
  and both ears; processed on the device. B06, B07.

## Dolby Atmos

- Apple Newsroom, "Apple Music announces Spatial Audio and Lossless Audio" (17 May 2021), and its 8 Jun 2021 update:
  Dolby Atmos in Apple Music from June 2021. B07.
- Apple Support, "About Spatial Audio with Dolby Atmos in Apple Music" (4 Apr 2025): only select songs. B07.

## Evidence and tools

- `spatial.py`, `mix_listen.py`, `build_hf.py`, `hyperframes/scenes/` and `evidence/` in this folder; the shared
  week kit in `_kit/` (`hfkit.py`, `kit3.js`, `add_qc.py`, `vertical_strings.py`); `run_audio.sh`.
- three.js 0.187.0 (MIT licence), shipped in `hyperframes/assets/` (`three.module.min.js`, `three.core.min.js`,
  `three-LICENSE.txt`); vendored for the week in `week-12/_vendor`.
- HyperFrames (HTML rendered to video, GSAP timeline); Kokoro `af_bella` for the narration; Source Serif 4 and
  Inter for type.
