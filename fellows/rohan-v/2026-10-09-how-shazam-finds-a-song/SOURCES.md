# SOURCES — How Shazam Finds a Song

All outside facts were verified on 2026-10-10; quotes and the exact claims checked are in
`week-07/_research/facts.md`.

## Executable evidence (this folder)

| Source | Used for |
|---|---|
| `synth.py` | the six synthetic songs, the re-performances (new key, faster, hummed); no copyrighted audio |
| `fingerprint.py` → `evidence/run.log`, `evidence/fingerprint.json`, `evidence/*.wav` | every peak, hash, vote, count and listening clip in B01–B06 |
| `export_shazam_data.py` → `scenes/shazam/shazamData.ts`, `public/shazam/spec-*.png` (toolkit) | the scenes' data, the spectrogram images and the typeset equations |
| `mix_listen.py` | B04 audio: narration + the run's two WAVs, level-matched |

## Method

| Source | Used for |
|---|---|
| A. Wang, "An Industrial-Strength Audio Search Algorithm", *Proc. ISMIR 2003* (Baltimore). https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf | the method `fingerprint.py` follows: spectrogram peaks ("constellation map"), anchor + target-zone hashes, offset histogram; robustness to noise; "very sensitive to which particular version", "not expected to generalize to live recordings" |

## Products and history

| Source | Used for |
|---|---|
| YouTube Help, "How Content ID works", https://support.google.com/youtube/answer/2797370 | B07: uploads are checked against "a database of audio and visual files submitted by copyright owners" |
| Google, "The Machine Learning Behind Hum to Search" (2020), https://research.google/blog/the-machine-learning-behind-hum-to-search/ | B06: humming is recognised by a different, melody-based method |
| Wikipedia, "Shazam (music app)"; Apple Newsroom (24 Sep 2018) | background only. Not used in the video: the founding year differs between sources (1999 / 2000) |

Not claimed: that Shazam itself cannot recognise humming (no official statement was found), or
any parameter of Shazam's production system.
