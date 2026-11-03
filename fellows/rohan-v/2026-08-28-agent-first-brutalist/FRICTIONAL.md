# FRICTIONAL — Your Weekly Video, Handled.

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-08-28 — Agent-first guide to Brutalist (week 2, progress / tutorial)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's `BUILD-LOG.md`, the commit history and my dated session record with
> Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** A 4-minute walkthrough for fellows: set up Brutalist and deliver a
week of videos by talking to an agent, not by typing commands. Built the same day
I first cloned the toolkit.

**Tried, and expected.**
- Wanted a fellow with no coding background to get from nothing to a submitted
  week by conversation alone. Asked for 3–5 minutes, animated mockups rather than
  screen recordings, the exact links on screen, and the four-files-a-week rule
  (two topics × 16:9 and 9:16, all 4K).
- Expected Claude to do the whole GitHub push itself.

**Where it resisted, and what I did next.**
- Remotion could not render on Windows at all — the toolkit called bare `npx`.
  Fixed; a concurrency override then cut a 4K render from ~4 hours to ~30 minutes
  (`BUILD-LOG.md`, Phase 4).
- Every em-dash came out as `â€"`, burned into the video. The probe and every gate
  passed; it was visible only in a frame. Traced to a cp1252 read of the beat
  sheet (Phase 6).
- The first short was not 4K and had no audio; sent it back.
- The push stalled: the branch didn't appear, and it took several attempts from
  Claude before it went through. I had expected it to be one step.

**What Claude contributed — accepted, changed, rejected.**
- Claude built the beat sheet, ten new components, the renders and the docs, and
  fixed both Windows render bugs in the toolkit.
- Changed: no fancy greeting — my name and Humanitarians AI only; no personal
  references to the program lead in the narration; the title reframed as an
  agent-first guide; a beat added on how the weeks *after* setup work, and I asked
  for it in the audio as well as on screen.
- Changed: one folder per video, holding the beat sheet and docs — not the whole codebase.
- Set by me: a branch and a PR (I'm a collaborator on the repo); only docs under
  25 MB go to GitHub, the videos to Drive. Claude had read the submission rules the same way.

**Understand now / still don't.**
- Now: a clean probe and a passing gate say nothing about whether the text on
  screen is readable. Looking at frames is the check.
- Still open: this reel's 9:16 cut was made before the portrait fix of week 3
  (`../2026-09-04-unblocking-the-team/BUILD-LOG.md` §11) and is not a native
  portrait render. Its beat sheet also still names `ClaudeTitleOutro`, since locked
  to another channel, so a rebuild today would change its end card.

**Evidence:** [`b90a6c4`](https://github.com/nikbearbrown/humanitarians-youtube/commit/b90a6c4) · [`beat_sheet.json`](./beat_sheet.json) · [`BUILD-LOG.md`](./BUILD-LOG.md) ·
[`FACTCHECK.md`](./FACTCHECK.md) · [`SOURCE-brief.md`](./SOURCE-brief.md)

## 2026-09-24 — Repository compliance pass

**Working on.** Checking this folder against the fellows page and the repository's
`fellows/README.md` before my renewal review.

**Tried, and expected.** Expected the folder to pass as committed. It didn't.

**Where it resisted, and what I did next.**
- My surname appeared in `FACTCHECK.md`, `PROMPT.md`, `README.md`, `SHOTLIST.md`,
  `SOURCE-brief.md`, `SOURCES.md`, `beat_sheet.json`, `description.txt`. The
  repository allows a first name, a last initial and a GitHub id only, and names
  beat sheets explicitly, so it is now "Rohan V." throughout —
  [`c77c339`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c77c339).
- In the beat sheet that meant the presenter field, the end-card subline and the
  spoken sign-off, so a rebuild would no longer match the Drive masters exactly —
  those still carry my full name as they were rendered.
- Two program staff were named in full where their program-wide emails are cited as
  sources; now first name and last initial.
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
