# FRICTIONAL — Use the Tool First.

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-11 — Use the Tool First (week 4, progress report)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's `BUILD-LOG.md`, the commit history and my dated session record with
> Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** The progress report for a week spent almost entirely on the
Midjourney tutorial series: using Midjourney myself, researching prompting
techniques, capturing the interface, and planning the six parts.

**Tried, and expected.**
- One video on the week plus one STEM topic, both about two minutes, with the
  best animation quality I could get.
- Told the week through what the screenshots overturned in my plan — five
  assumptions the captures proved wrong — rather than as a list of activities.

**Where it resisted, and what I did next.**
- The end card came out with another channel's handle and mascot. `ClaudeTitleOutro`
  is locked to that channel and silently ignores the handle and presenter props;
  nothing errored. Switched to `HaiTitleOutro` (`BUILD-LOG.md` §5). A duration and
  dimension check would have passed it.
- The toolkit's own lint then advised switching back — it keyed on palette, not
  channel. Fixed.
- Finals were refused with "beat sheet changed during rendering" — another
  encoding mismatch, this time in the change-guard. Fixed (§7).
- After the merge I found odd accents above the letter "a" in both shorts; the
  16:9 cuts were fine. `shorts.py` had read the parent sheet in the wrong encoding
  and written the corruption back. Both vertical cuts re-rendered in [`ff1cb46`](https://github.com/nikbearbrown/humanitarians-youtube/commit/ff1cb46).

**What Claude contributed — accepted, changed, rejected.**
- Claude measured what was actually on disk (six masters totalling 18:59, 29
  captures, an 863-line UI spec) and found two inconsistencies in my plan
  document, then built three components with portrait siblings and reused the
  roadmap outright.
- Accepted: the "what the screenshots overturned" framing.
- Rejected: both shorts as first delivered.

**Understand now / still don't.**
- Now: a component that ignores a prop fails silently — the render looks finished.
- Still open: the week-2 beat sheets still name the locked outro, so a rebuild of
  either would put the wrong channel on its end card.

**Evidence:** [`8d9c765`](https://github.com/nikbearbrown/humanitarians-youtube/commit/8d9c765) · [`ff1cb46`](https://github.com/nikbearbrown/humanitarians-youtube/commit/ff1cb46) · [`BUILD-LOG.md`](./BUILD-LOG.md) ·
[`FACTCHECK.md`](./FACTCHECK.md) · [`qc-sheet-9x16.png`](./qc-sheet-9x16.png)

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
