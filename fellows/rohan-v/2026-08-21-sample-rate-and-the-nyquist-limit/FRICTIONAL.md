# FRICTIONAL — Sample Rate and the Nyquist Limit

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-08-21 — Sample Rate and the Nyquist Limit (week 1, STEM)

> **Written 2026-09-24, five weeks after the week it describes.** No working
> notes from this week survive — my session record with Claude begins on
> 2026-08-28 — so this entry rests only on the files in this folder and the
> commit history. It is thin because the record is thin; nothing below is filled
> in from memory. Drafted with Claude from those files.

**Working on.** The second of my two week-1 explainers: sampling as snapshots,
Nyquist as half the sample rate, and aliasing — a high pitch stored as a false low
one. Upsampling does not restore cycles that were never captured.

**Tried, and expected.**
- Manim teaching scenes (`scenes.py`) with Remotion bookends; Kokoro `af_bella` at 0.95.
- What I expected going in was not written down.

**Where it resisted, and what I did next.**
- `BUILD-LOG.md` has a single entry: a named intro, with "AI" respelled *ay-eye*
  so the voice says the letters. No other difficulty is recorded — which does not
  mean there was none.
- As with its sibling, my PR [#32](https://github.com/nikbearbrown/humanitarians-youtube/pull/32) was closed unmerged and this
  folder reached `main` in the program's snapshot [`e6e678c`](https://github.com/nikbearbrown/humanitarians-youtube/commit/e6e678c).
- No QC contact sheet: `compile.py --review` could not complete on Windows at the
  time (found in week 3, `../2026-09-04-unblocking-the-team/BUILD-LOG.md` §7).

**What Claude contributed — accepted, changed, rejected.**
- Claude authored the beat sheet, the Manim scenes and the docs, and ran the renders.
- What I accepted, changed or rejected this week is not recorded.

**Understand now / still don't.**
- Now: why this reel has no contact sheet (found in week 3).
- Still open: the frames were never checked against a contact sheet.

**Evidence:** [`beat_sheet.json`](./beat_sheet.json) · [`scenes.py`](./scenes.py) ·
[`BUILD-LOG.md`](./BUILD-LOG.md) · [`FACTCHECK.md`](./FACTCHECK.md) · [`e6e678c`](https://github.com/nikbearbrown/humanitarians-youtube/commit/e6e678c) · PR [#32](https://github.com/nikbearbrown/humanitarians-youtube/pull/32)

## 2026-09-24 — Repository compliance pass

**Working on.** Checking this folder against the fellows page and the repository's
`fellows/README.md` before my renewal review.

**Tried, and expected.** Expected the folder to pass as committed. It didn't.

**Where it resisted, and what I did next.**
- My surname appeared in `BUILD-LOG.md`, `README.md`, `beat_sheet.json`,
  `short/beat_sheet.json`. The repository allows a first name, a last initial and a
  GitHub id only, and names beat sheets explicitly, so it is now "Rohan V."
  throughout —
  [`c77c339`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c77c339).
- In both beat sheets (landscape and `short/`) that meant the spoken intro and
  sign-off and the build note, so a rebuild would no longer match the Drive masters
  exactly — those still carry my full name as they were rendered.
- The README did not link this reel's renders on Drive; it does now —
  [`e8703b6`](https://github.com/nikbearbrown/humanitarians-youtube/commit/e8703b6).
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

**Evidence:** [`c77c339`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c77c339) · [`e8703b6`](https://github.com/nikbearbrown/humanitarians-youtube/commit/e8703b6)
