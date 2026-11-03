# FRICTIONAL — Unblocking the Team.

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-04 — Unblocking the Team (week 3, progress report)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's `BUILD-LOG.md`, the commit history and my dated session record with
> Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** My weekly progress report. Early in the week I ran a workshop on
Brutalist for the marketing team — non-technical, creative people who were stuck
at putting their code on GitHub, which I had already worked out. Also in the
report: the agent-first setup video, the three-part Suno tutorial series for new
members, and signup documentation in progress (Discord, Suno, Midjourney, Adobe
Creative Cloud).

**Tried, and expected.**
- A two-minute reel, in 16:9 and 9:16 at 4K.
- Expected my name pronounced the way I had already asked for, and a vertical cut
  that re-lays itself out for a phone.

**Where it resisted, and what I did next.**
- The voice mispronounced my name at the start and the end. The phonetic spelling
  had been set up during the Suno series and never carried over. Fixed; audio
  regenerated and every duration re-stamped (`BUILD-LOG.md` §10).
- The 9:16 was the 16:9 master shrunk onto a tall frame — small, compressed, hard
  to read. I rejected it. Root cause: `shorts.py` read its component registry in
  the wrong encoding, swallowed the error, and reported every portrait component
  as missing, so the letterbox looked like the sanctioned path. Fixed, and four
  native portrait siblings written (§11).
- Asked whether the Drive upload could be automated. It became `./art drive`,
  now a step in every build.
- Six toolkit bugs in all, four of them the same Windows encoding fault.

**What Claude contributed — accepted, changed, rejected.**
- Claude checked the brief against what was on disk (probed the three Suno
  masters, found the series plan's runtime estimates were stale), built four
  components and their portrait siblings, and fixed the toolkit.
- Rejected: the letterboxed vertical; the mispronunciation.
- Changed: the weekly submission email — "too much detail, just give the links."
- Accepted: automating the Drive upload.

**Understand now / still don't.**
- Now: the native-portrait path existed all along; an exception handler that
  returns an empty string turned an encoding error into a wrong answer about what
  the library contained.
- Still open: the two week-2 reels' vertical cuts came out of the same broken path
  and have not been rebuilt.
- Correction to the record: `BUILD-LOG.md` gives the build date as 2026-08-29;
  my session record shows this reel was built on 2026-09-04.

**Evidence:** [`4774875`](https://github.com/nikbearbrown/humanitarians-youtube/commit/4774875) · [`beat_sheet.json`](./beat_sheet.json) · [`BUILD-LOG.md`](./BUILD-LOG.md) ·
[`FACTCHECK.md`](./FACTCHECK.md) · [`qc-sheet-9x16.png`](./qc-sheet-9x16.png)

## 2026-09-24 — Repository compliance pass

**Working on.** Checking this folder against the fellows page and the repository's
`fellows/README.md` before my renewal review.

**Tried, and expected.** Expected the folder to pass as committed. It didn't.

**Where it resisted, and what I did next.**
- My surname appeared in `BUILD-LOG.md`, `PROMPT.md`, `PROMPTS.md`, `README.md`,
  `SHOTLIST.md`, `SOURCES.md`, `beat_sheet.json`, `description.txt`. The repository
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
