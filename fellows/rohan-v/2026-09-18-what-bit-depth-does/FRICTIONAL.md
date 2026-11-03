# FRICTIONAL — 16-bit or 24-bit: What Bit Depth Does

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-18 — What bit depth does (week 5, STEM)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's `BUILD-LOG.md`, the commit history and my dated session record with
> Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** What the 16-or-24-bit choice in an export box controls, for someone
who has never opened an audio editor. Paired with the mono fold-down reel. I made
two STEM videos this week and no progress-update video.

**Tried, and expected.**
- Asked for two STEM topics, about two minutes each, with motion graphics good
  enough to keep a viewer watching.
- Measured first, in float64 numpy: the 8-bit noise floor at −53.14 dBFS, 16-bit at −100.75.
- Expected the first plan to work for a complete beginner. It didn't.

**Where it resisted, and what I did next.**
- The first cut started abruptly — nothing for a viewer who knows no audio. I
  stopped the build and had both plans rebuilt around a background beat and an
  everyday analogy (a ruler).
- The rewrite went too detailed, then too high-level. Settled on keeping the
  mechanism in full and one pair of hard numbers.
- The motion still looked like the old reels. I asked; an audit found only 3 of
  10 researched libraries actually in use, and that no scene had ever loaded a
  font — every reel so far had rendered in a fallback face. Fixed, and I asked for
  a still before the full build.
- ffmpeg reported −∞ for 24-bit — a tool limit (32-bit float internally), not a
  result. Re-measured in numpy.
- Gate V failed four beats for underfill; reading the contact sheet then found
  three defects the gate could not see (`BUILD-LOG.md` §7–8).
- Retitled from *The Quietest Sound Your File Can Hold*: I want plain titles that
  say what the video is, not cryptic ones.

**What Claude contributed — accepted, changed, rejected.**
- Claude researched Remotion libraries, including the three resources I pointed
  it to, built four components and four native portrait siblings, ran the
  measurement and wrote the docs.
- Rejected: the first plan (too abrupt), the second (too detailed), the poetic title.
- Changed: keep the two-minute length and make it simpler, rather than cutting it.
- Accepted: the ruler analogy; measuring first.

**Understand now / still don't.**
- Now: bit depth sets how quiet a sound can get before the file's own hiss takes
  over, and at 16 bits that hiss sits below the room you are listening in.
- Still open: this week had no progress-update video, against the one-STEM,
  one-progress rule for the weekly pair.

**Evidence:** [`b36bced`](https://github.com/nikbearbrown/humanitarians-youtube/commit/b36bced) · [`MEASUREMENTS.txt`](./MEASUREMENTS.txt) · [`measure_bitdepth.py`](./measure_bitdepth.py) ·
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
