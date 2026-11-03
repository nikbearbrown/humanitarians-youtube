# FRICTIONAL — Why Your Track Gets Turned Down

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-11 — Why your track gets turned down (week 4, STEM)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's `BUILD-LOG.md`, the commit history and my dated session record with
> Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** Loudness normalisation: why pushing a track louder buys nothing on
a streaming platform, and what it permanently costs.

**Tried, and expected.**
- Picked loudness from two suggestions on one condition: most viewers are not
  audio professionals and won't know what a master or a squeezed mix is.
- Measure first, with ffmpeg's EBU R128 scanner. Expected the squeezed version to
  measure louder.

**Where it resisted, and what I did next.**
- The first squeezed version measured 3.5 LU *quieter* — steady tones have no
  peaks for a limiter to trade away. Rebuilt the signal with decaying hits; then
  it behaved like music (`BUILD-LOG.md` §2).
- The first cut ran 2:26 against a two-minute brief; trimmed beat by beat to 2:02.
- The factcheck caught "sounds nearly nine times louder": 8.7 LU is a difference
  on a logarithmic scale, not a ratio. Rewritten and re-voiced (§6).
- A later script clobbered B01's new duration back to the stale one; caught by
  probing the mp3 against the sheet.
- Gate V blocked the final twice — a measurement span too faint on cream, and a
  library card filling 21% of the frame against a 55% floor. Built `HaiApplyCard` (§7).
- Same wrong-channel outro and the same corrupted shorts as the sibling reel ([`ff1cb46`](https://github.com/nikbearbrown/humanitarians-youtube/commit/ff1cb46)).

**What Claude contributed — accepted, changed, rejected.**
- Claude designed and ran the experiment, wrote every label for non-professionals
  ("tallest single moment", "how loud it actually sounds", "the gap"), and ran the factcheck.
- Changed: my condition took "master", "mix", "compression", "limiter" and
  "headroom" out of the reel entirely.
- Rejected: both shorts as first delivered.

**Understand now / still don't.**
- Now: applying the same gain to both files moves their loudness and leaves the
  gap between quiet and loud untouched — gain cannot give back range. I've seen it measured.
- Still open: one synthetic signal, and −14 LUFS is the commonly published
  platform target; targets differ between platforms and change.

**Evidence:** [`8d9c765`](https://github.com/nikbearbrown/humanitarians-youtube/commit/8d9c765) · [`ff1cb46`](https://github.com/nikbearbrown/humanitarians-youtube/commit/ff1cb46) · [`MEASUREMENTS.txt`](./MEASUREMENTS.txt) ·
[`BUILD-LOG.md`](./BUILD-LOG.md) · [`FACTCHECK.md`](./FACTCHECK.md)

## 2026-09-24 — Repository compliance pass

**Working on.** Checking this folder against the fellows page and the repository's
`fellows/README.md` before my renewal review.

**Tried, and expected.** Expected the folder to pass as committed. It didn't.

**Where it resisted, and what I did next.**
- My surname appeared in `PEDAGOGY.md`, `PROMPT.md`, `PROMPTS.md`, `README.md`,
  `SHOTLIST.md`, `beat_sheet.json`, `description.txt`. The repository allows a first
  name, a last initial and a GitHub id only, and names beat sheets explicitly, so it
  is now "Rohan V." throughout —
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
