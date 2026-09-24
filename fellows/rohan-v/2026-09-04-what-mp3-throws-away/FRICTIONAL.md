# FRICTIONAL — What MP3 Throws Away

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-04 — What MP3 throws away (week 3, STEM)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's `BUILD-LOG.md`, the commit history and my dated session record with
> Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** The STEM half of the week: what lossy compression removes and
what it costs. I asked for audio-topic suggestions and picked lossy compression
from three.

**Tried, and expected.**
- Measure first, script second: white noise encoded at 128 and 320 kbps, decoded,
  then band-measured with ffmpeg.
- Expected 320 kbps to be effectively transparent.

**Where it resisted, and what I did next.**
- A drafted line said 320 kbps "keeps everything". The measurement showed 20 kHz
  3.5 dB down, so it became "survives intact all the way to nineteen" — what was
  actually observed (`BUILD-LOG.md` §2).
- Three frames had dead space under undersized plots. All three were found by
  looking at frames, none by probing; the plots were resized (§6).
- The vertical rewired to native portrait components on the first run — the first
  reel on which the week's portrait fix held.

**What Claude contributed — accepted, changed, rejected.**
- Claude proposed three topics and recommended lossy compression because it was
  the only one that could be measured locally in minutes. I accepted. Claude ran
  the experiment and built four components plus portrait siblings.
- Accepted: measuring before scripting. Every STEM reel since has been built that way.

**Understand now / still don't.**
- Now: 128 kbps has a hard cliff at 16 kHz, 320 kbps matches the source through
  19 kHz, and a file keeps losing ground each time it is re-encoded (measured at 1, 4,
  6 and 11 generations) — all measured here, in `MEASUREMENTS.txt`.
- Still open: the test signal is white noise, so these figures describe the
  encoder on a flat spectrum, not on real music.

**Evidence:** [`5d39e96`](https://github.com/nikbearbrown/humanitarians-youtube/commit/5d39e96) · [`MEASUREMENTS.txt`](./MEASUREMENTS.txt) · [`BUILD-LOG.md`](./BUILD-LOG.md) ·
[`FACTCHECK.md`](./FACTCHECK.md)

## 2026-09-24 — Repository compliance pass

**Working on.** Checking this folder against the fellows page and the repository's
`fellows/README.md` before my renewal review.

**Tried, and expected.** Expected the folder to pass as committed. It didn't.

**Where it resisted, and what I did next.**
- My surname appeared in `BUILD-LOG.md`, `PEDAGOGY.md`, `PROMPT.md`, `PROMPTS.md`,
  `README.md`, `SHOTLIST.md`, `beat_sheet.json`, `description.txt`. The repository
  allows a first name, a last initial and a GitHub id only, and names beat sheets
  explicitly, so it is now "Rohan V." throughout —
  [`c77c339`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c77c339).
- In the beat sheet that meant the presenter field, the end-card subline, the spoken
  sign-off and the build note, so a rebuild would no longer match the Drive masters
  exactly — those still carry my full name as they were rendered.
- The README did not link this reel's renders on Drive; it does now —
  [`e8703b6`](https://github.com/nikbearbrown/humanitarians-youtube/commit/e8703b6).
- `.gitignore` excluded every MP4 by type and blocked `pantry/`. Since 2026-09-18
  build inputs belong in the tree, so renders are now excluded by location only —
  [`c155f99`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c155f99).
- Added this log.

**What Claude contributed — accepted, changed, rejected.** Claude read both rule
sources, scanned every file in my folder and proposed each change as its own
commit, for me to review in a pull request before merge.

**Understand now / still don't.**
- Now: the no-surname rule and the frictional-log rule both arrived on
  2026-09-22, after this folder was committed, and the media rule changed on
  2026-09-18. None of this was against the rules when it went in — but a folder
  has to be checked against the live rules, not the ones it was built under.
- Still open: whether my surname should also come out of the rendered videos in
  Drive, which are outside this repository.

**Evidence:** [`c77c339`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c77c339) · [`e8703b6`](https://github.com/nikbearbrown/humanitarians-youtube/commit/e8703b6) · [`c155f99`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c155f99)
