# FRICTIONAL — Stem Separation: Estimation, Not Extraction

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-08-28 — Stem separation (week 2, STEM)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's `BUILD-LOG.md`, the commit history and my dated session record with
> Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** How models pull vocals out of a mix, for a smart non-technical
viewer: a mix is several sounds stacked into one file; "stems" are the model's
estimate of those parts, not a recovered original; bleed is normal; and when a
separated vocal is good enough to use versus when it is lying to you. Target
2:30–3:00.

**Tried, and expected.**
- v1 built entirely from existing library cards — Claude windows and verdict
  cards, no waveforms. Delivered at 2:21.
- Expected it to match the first video's look and to explain the idea visually.

**Where it resisted, and what I did next.**
- The docs were missing from the first pass; asked for them.
- Rejected v1: too bare, the end screen did not match the first video, and
  Humanitarians AI was not named at either end. Asked for waveform motion graphics
  at the same length, with the script reworked to fit.
- v2 added three purpose-built scenes — four tracks collapsing into one mix, the
  mix splitting into estimated stems with "probability" borders, and a vocal stem
  with drum bleed ghosted in (`BUILD-LOG.md`, v2).

**What Claude contributed — accepted, changed, rejected.**
- Claude wrote both scripts, built the three waveform components and re-voiced the reel.
- Rejected: v1 as delivered.
- Changed: intro and outro wording and the end card, to match the agent-first
  reel. I asked for every video after this one to keep the same look — and they have.

**Understand now / still don't.**
- Now: a separated stem is a probability estimate, and bleed is a property of the
  method, not a fault in one file.
- Still open: the 9:16 cut is a letterbox of the 16:9 master (`BUILD-LOG.md`,
  Phase 4), never re-rendered natively; and the beat sheet still names
  `ClaudeTitleOutro`, since locked to another channel, so a rebuild would change
  its end card (`../2026-09-11-use-the-tool-first/BUILD-LOG.md` §5).

**Evidence:** [`0942975`](https://github.com/nikbearbrown/humanitarians-youtube/commit/0942975) · [`beat_sheet.json`](./beat_sheet.json) · [`BUILD-LOG.md`](./BUILD-LOG.md) ·
[`PEDAGOGY.md`](./PEDAGOGY.md)

## 2026-09-24 — Repository compliance pass

**Working on.** Checking this folder against the fellows page and the repository's
`fellows/README.md` before my renewal review.

**Tried, and expected.** Expected the folder to pass as committed. It didn't.

**Where it resisted, and what I did next.**
- My surname appeared in `BUILD-LOG.md`, `PEDAGOGY.md`, `PROMPTS.md`, `README.md`,
  `SHOTLIST.md`, `beat_sheet.json`, `description.txt`. The repository allows a first
  name, a last initial and a GitHub id only, and names beat sheets explicitly, so it
  is now "Rohan V." throughout —
  [`c77c339`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c77c339).
- In the beat sheet that meant the presenter field, the end-card subline and the
  spoken sign-off, so a rebuild would no longer match the Drive masters exactly —
  those still carry my full name as they were rendered.
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
