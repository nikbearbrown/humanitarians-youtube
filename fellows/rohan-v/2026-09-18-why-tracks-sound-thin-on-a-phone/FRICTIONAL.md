# FRICTIONAL — Why Your Track Sounds Thin On A Phone

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-18 — Why tracks sound thin on a phone (week 5, STEM)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's `BUILD-LOG.md`, the commit history and my dated session record with
> Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** Why a mix that sounds full in headphones can come back thin on a
phone speaker, and the ten-second check that catches it. Paired with the bit-depth
reel. I made two STEM videos this week and no progress-update video.

**Tried, and expected.**
- Two experiments, both measured before the script. The second was *predicted*
  first: a 0.6 ms delay should cancel at odd multiples of 833 Hz.
- Expected: if the picture of cancellation is right, the notches fall where
  predicted. They did, at all four positions.

**Where it resisted, and what I did next.**
- The first measurement pass returned nothing: `-v error` silences ffmpeg's
  `volumedetect`, which prints at info level. Removed it (`BUILD-LOG.md` §1).
- The same "too abrupt" and "too detailed" corrections as the sibling reel; the
  frequency table — the strongest result in either reel — was cut for this audience.
- In the door analogy both figures' arrows pointed the same way during the
  "pushing against each other" beat, contradicting the narration. Found in a frame.
- Gate V passed B03 while it printed "unchanged" beside the wide layer for seven
  seconds, as the narration said that layer had dropped 49.5 dB. The worst defect
  in either reel; no gate could have caught it (§6).
- The door read as a horizontal bar, not a door, and the portrait cut had three
  text collisions in the same beat. Both fixed and re-rendered.
- Retitled from *Why Your Track Vanishes On One Speaker* to a plain title.

**What Claude contributed — accepted, changed, rejected.**
- Claude built the test signals, made the prediction and ran both measurements,
  built four components and four native portrait siblings, and wrote the docs.
- Changed: as for the sibling reel, a background beat on what stereo is — two
  sides, and one speaker that has to add them — before any talk of cancelling.
- Accepted: the door analogy; volunteering the caveat ("holes, not silence")
  before the evidence.
- Rejected: the frequency table on screen; the poetic title.

**Understand now / still don't.**
- Now: one speaker has to add the two sides before it can move, so whatever sits
  in the centre survives and anything the sides disagree on is thinned or lost.
- Still open: this week had no progress-update video, against the one-STEM,
  one-progress rule for the weekly pair.

**Evidence:** [`b36bced`](https://github.com/nikbearbrown/humanitarians-youtube/commit/b36bced) · [`MEASUREMENTS.txt`](./MEASUREMENTS.txt) · [`build_mono_signals.py`](./build_mono_signals.py) ·
[`BUILD-LOG.md`](./BUILD-LOG.md) · [`qc-sheet-9x16.png`](./qc-sheet-9x16.png)

## 2026-09-24 — Repository compliance pass

**Working on.** Checking this folder against the fellows page and the repository's
`fellows/README.md` before my renewal review.

**Tried, and expected.** Expected the folder to pass as committed. It didn't.

**Where it resisted, and what I did next.**
- My surname appeared in `PROMPT.md`, `README.md`, `SOURCE-brief.md`,
  `beat_sheet.json`, `description.txt`, `short/beat_sheet.json`. The repository
  allows a first name, a last initial and a GitHub id only, and names beat sheets
  explicitly, so it is now "Rohan V." throughout —
  [`c77c339`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c77c339).
- In both beat sheets (landscape and `short/`) that meant the presenter field, the
  end-card subline, the spoken sign-off and the build note, so a rebuild would no
  longer match the Drive masters exactly — those still carry my full name as they
  were rendered.
- The README linked the **2026-08-28** Drive folder, so a reader following it found
  the wrong week's videos — an error made when this folder was written on
  2026-09-17. It now links `2026-09-18/` —
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
