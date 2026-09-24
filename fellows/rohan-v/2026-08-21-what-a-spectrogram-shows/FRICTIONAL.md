# FRICTIONAL — What a Spectrogram Shows

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-08-21 — What a Spectrogram Shows (week 1, STEM)

> **Written 2026-09-24, five weeks after the week it describes.** No working
> notes from this week survive — my session record with Claude begins on
> 2026-08-28 — so this entry rests only on the files in this folder and the
> commit history. It is thin because the record is thin; nothing below is filled
> in from memory. Drafted with Claude from those files.

**Working on.** My first Brutalist explainer, for Lyrical Literacy: a spectrogram
as a map of energy over time and frequency, the STFT window trade-off, and what it
hides (phase, overlap, the noise floor). Paired with *Sample Rate and the Nyquist
Limit* the same week.

**Tried, and expected.**
- Manim teaching scenes (`scenes.py`) with Remotion bookends; Kokoro `af_bella` at 0.95.
- What I expected going in was not written down — which is the gap this log exists to close.

**Where it resisted, and what I did next.**
- `BUILD-LOG.md` records one rebuild: a named intro, "AI" respelled *ay-eye* so
  the voice says the letters, and expanded teaching beats (waveform, harmonics,
  STFT window, when to use it and when not).
- My PR [#32](https://github.com/nikbearbrown/humanitarians-youtube/pull/32), opened 2026-08-22, was closed unmerged on
  2026-08-27. This folder reached `main` that day in the program's repository
  snapshot [`e6e678c`](https://github.com/nikbearbrown/humanitarians-youtube/commit/e6e678c), not through my own PR.
- No QC contact sheet exists for this reel. I only learned why in week 3: on
  Windows `compile.py --review` could not finish, so the step that makes the
  sheet never ran (`../2026-09-04-unblocking-the-team/BUILD-LOG.md` §7).

**What Claude contributed — accepted, changed, rejected.**
- Claude authored the beat sheet, the Manim scenes and the docs, and ran the renders.
- Beyond the one rebuild, what I accepted or pushed back on is not recorded.

**Understand now / still don't.**
- Now: why this reel has no contact sheet (found in week 3).
- Still open: its frames were never checked against one, and have not been re-checked since.

**Evidence:** [`beat_sheet.json`](./beat_sheet.json) · [`scenes.py`](./scenes.py) ·
[`BUILD-LOG.md`](./BUILD-LOG.md) · [`CHECKS-REPORT.md`](./CHECKS-REPORT.md) · [`e6e678c`](https://github.com/nikbearbrown/humanitarians-youtube/commit/e6e678c) · PR [#32](https://github.com/nikbearbrown/humanitarians-youtube/pull/32)

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
