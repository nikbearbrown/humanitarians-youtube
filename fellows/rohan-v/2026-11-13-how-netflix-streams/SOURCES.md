# SOURCES — How Netflix Streams

Full notes, URLs, confidence levels and the "do not say" list: `week-12/_research/facts-netflix.md`. Checked
2026-11-10. Netflix restates its numbers often, so each one below carries its source's date.

## The ladder and the player

- Netflix TechBlog, "Per-Title Encode Optimization" (14 Dec 2015): "bitrate ladder", pre-encoding each title at
  several bitrates, the player choosing between them. B01, B03.
- "A Buffer-Based Approach to Rate Adaptation: Evidence from a Large Video Streaming Service", ACM SIGCOMM, 2014
  (a study run with Netflix): chunks of 4 s in the 2013 test setup, a 235 kb/s to 5 Mb/s ladder, choosing the rate
  from the buffer. B01, B04, and the idea behind `stream.py`'s buffer-based player.
- Netflix TechBlog, "HTML5 Video at Netflix" (15 Apr 2013). Background; not stated.
- Netflix TechBlog, "Bringing AV1 Streaming to Netflix Members' TVs" (9 Nov 2021): players switch to a lower
  bitrate when the connection can't keep up. B00.

## The score

- Netflix TechBlog, "Toward A Practical Perceptual Video Quality Metric" (6 Jun 2016): VMAF, built with a
  university group at USC, trained on viewers' ratings, open-sourced that month. B02.
- VMAF on GitHub (Netflix/vmaf): the open-source code and the libvmaf library the run uses. B02, `stream.py`.
- Netflix TechBlog, "Toward a Better Quality Metric for the Video Community" (7 Dec 2020). Background; not stated.

## Per title, and newer codecs

- Netflix TechBlog, "Per-Title Encode Optimization" (14 Dec 2015): one ladder doesn't fit every title; a ladder for
  each title. B03.
- Netflix TechBlog, "Dynamic optimizer — a perceptual video encoding optimization framework" (5 Mar 2018) and
  "Optimized shot-based encodes: Now Streaming!" (9 Mar 2018). Background (shot-by-shot encoding); not stated.
- Netflix TechBlog, "AV1 — Now Powering 30% of Netflix Streaming" (1 Dec 2025; data of 13 Nov 2025): about 30% of
  viewing, about a third less bandwidth. B06.

## Open Connect

- Netflix, "Open Connect Overview" (PDF): Netflix's own delivery network, servers inside internet providers and at
  internet exchanges, filled off-peak. B05.
- Netflix TechBlog, "Netflix and Fill" (11 Aug 2016): the overnight fill. B05.
- About Netflix, "Open Connect: Celebrating a Decade of Smooth and Efficient Streaming" (14 Dec 2022): 18,000
  servers in 6,000 locations across 175 countries. B06.

## Scale and speeds

- Netflix Q4 2025 shareholder letter (20 Jan 2026, SEC EDGAR): over 325 million paid memberships. B06.
- Netflix Help Center, "Internet connection speed recommendations" (undated page, read 2026-11-09): 5 Mbps for
  Full HD, 15 for 4K, and a stable connection. B07.

## Software and assets

- ffmpeg with libx264 and libvmaf: the test clips (`testsrc2`, `mandelbrot`, `noise` filters), the encodes and the
  scores. `stream.py`.
- three.js 0.187.0 (MIT licence), shipped in `hyperframes/assets/` with `three-LICENSE.txt`. The 3D stages in B01–B06.
- HyperFrames and GSAP: the compositions and their timelines. Source Serif 4 (SIL Open Font License,
  `hyperframes/assets/fonts/OFL.txt`) and Inter for the type.
- Netflix's "N" mark, from Wikimedia Commons `Netflix_2016_N_logo.svg`, shown only beside Netflix's name (LOGO LAW).
- Kokoro `af_bella`: the narration (AI voice).

## Evidence

- `stream.py`, `build_hf.py`, `hyperframes/scenes/` and `evidence/` in this folder; the shared kit in `_kit/`
  (`kit3.js`, `hfkit.py`).
