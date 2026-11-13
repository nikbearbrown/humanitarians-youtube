# Frictional log — Indexed or Invisible

## 2026-08-11 — 10:52, 42 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** A 42-beat deep-explainer tracing five layers: database,
exposure, discovery, programmatic SEO, validation. First reel with purpose-built scenes.

**What I tried, and what I expected.** I expected rendering 42 beats at
`--concurrency=4` to be simply faster than the toolkit's hardcoded `1`.

**Where it resisted, and what I did next.**
* It leaked Chrome processes until memory ran out. Beats then failed **silently**: the
  conform step still wrote an *audio-only* mp4, and `slate_resolves()` counts any
  existing `media/<bid>.mp4` as a successful fill. 17 of 42 beats shipped broken and it
  only surfaced when `compile.py` choked on a stream with no video.
* Worse, re-running skipped those beats, because the broken files existed. Had to delete
  them explicitly before re-rendering.
* Added a stream audit (`ffprobe` for a video stream on every beat) as a standing step
  before every compile. It has run on every reel since.

**What Claude contributed, and what I did with it.** Mine: the topic, the five-layer
structure, the call to drop to `--scale=1` for previz. Claude's: 12 scene components,
the diagnosis, the audit script.

**What I understand now, and what I still do not.**
* Understood: "the file exists" is not "the render succeeded." Any pipeline that treats
  presence as success will eventually lie to you.
* Not resolved: two figures on screen are mine, not measured — the sitemap tree's
  sub-counts and the FAQ card's open-role numbers. Flagged in `PEDAGOGY.md` §3.
