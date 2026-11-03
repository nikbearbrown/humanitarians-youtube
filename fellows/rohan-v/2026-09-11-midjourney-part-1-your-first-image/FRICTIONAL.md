# FRICTIONAL — Midjourney, Part One — Your First Image

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-06 → 2026-09-07 — Midjourney, Part One (Lyrical Literacy tutorials)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's plan and factcheck, the series' build playbook and my dated session record
> with Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** The first Midjourney training video: getting in, the sidebar, the
imagine bar, the three progress states, the rail beside a row, and hover.

**Tried, and expected.**
- The same framework as the Suno series, planned in full before any build, with my own
  captures of every screen. Asked for research into how many parts the tool needed.
- Expected 4K — not the 720p default the plan mentioned — and two to three minutes a
  part, with three minutes as a guide rather than a cap.
- Access for volunteers is through the Humanitarians AI Discord, same as Suno.

**Where it resisted, and what I did next.**
- Gate V passed frames that were wrong. Pulling 4K stills found ten defects: clipped
  hover buttons, nav labels truncated in the very beat about those labels, an empty
  card held for 14.5 seconds, two progress figures that disagreed, text below its own
  card, a gear drawn where Midjourney shows a sliders icon, and an emoji rendering as
  a missing-character box (`PLAN.md`; `FACTCHECK.md`, corrections).
- Four bugs came from typed-in coordinates; all four are now derived from the layout.
- When prompt writing became Part 2, three of this part's beats were re-cut.
- A review capture I took on 2026-09-07 ([`review-capture-part-1-bug-1.png`](./review-capture-part-1-bug-1.png)) shows white bars over the Step 3 card
  at 0:34. Nothing records how it was resolved; a frame pulled from the delivered
  master at 0:34 on 2026-09-24 does not show them.
- The render was slow enough that I asked why, and had it retried.

**What Claude contributed — accepted, changed, rejected.**
- Claude wrote the interface spec from my captures, built a Midjourney scene kit and
  the part's scenes, and wrote this part's checker (`check_beats.py`).
- Changed: 4K throughout; access described as the Discord login.
- Accepted: the series plan — five parts rather than four (the sixth came later).

**Understand now / still don't.**
- Now: a gate can pass a frame a viewer would call broken. Looking at stills is the check.
- Still open: the end card uses `ClaudeTitleOutro`, which was later locked to
  another channel and now ignores the handle it is given. The delivered master is
  correct — it was rendered before the lock — but a rebuild today would put the
  wrong channel on its end card.

**Evidence:** [`beat_sheet.json`](./beat_sheet.json) · [`PLAN.md`](./PLAN.md) · [`FACTCHECK.md`](./FACTCHECK.md) · [`qc-sheet-16x9.png`](./qc-sheet-16x9.png) · [`check_beats.py`](./check_beats.py)

## 2026-09-24 — First commit to the fellows repository

**Working on.** Moving this piece of work into the fellows repository beside the rest,
as the renewal requirements ask, with a frictional log.

**Tried, and expected.** Expected to copy it across as it was. It needed more than that.

**Where it resisted, and what I did next.**
- This folder had never been committed to the fellows repository — the work lived
  only in my Lyrical Literacy workspace. Committed today, three weeks after it was
  built —
  [`fa99475`](https://github.com/nikbearbrown/humanitarians-youtube/commit/fa99475).
- My surname appeared in `FACTCHECK.md`, `PLAN.md`, `PROMPTS.md`, `SHOTLIST.md`,
  `beat_sheet.json`, `check_beats.py`; the repository allows a first name and last
  initial only. Now "Rohan V." on screen and "Rohaan" spoken, so a rebuild would no
  longer match the Drive master exactly — that still carries my full name.
- `check_beats.py` enforced "full name spoken exactly once", so it would have failed
  against the redacted beat sheet. It now checks the sign-off instead. Run on the
  original and on the redacted copy, its output differs only in that one line.
- Added a README, since the folder had none, and promoted the existing QC contact
  sheet as `qc-sheet-16x9.png`.
- Added this log.

**What Claude contributed — accepted, changed, rejected.** Claude assembled the folder,
checked every file and capture for personal data, and proposed the changes as their own
commits in the same pull request as the rest of my compliance pass.

**Understand now / still don't.**
- Now: a piece of work that only exists in a private workspace is not on the record.
- Still open: none of this was written while the work happened. From here on the log is
  kept during the build.

**Evidence:** [`fa99475`](https://github.com/nikbearbrown/humanitarians-youtube/commit/fa99475)
