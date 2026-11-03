# FRICTIONAL — Midjourney, Part Four — The Settings Panel

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-07 — Midjourney, Part Four (Lyrical Literacy tutorials)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's plan and factcheck, the series' build playbook and my dated session record
> with Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** The settings panel: its four cards, aspect ratio, stylization, weirdness
and variety, model and Raw, speed and stealth, and the two video settings.

**Tried, and expected.**
- The panel exactly as my `prompt settings.png` capture shows it, with each setting's
  documented behaviour fetched from Midjourney's docs on 2026-09-07.

**Where it resisted, and what I did next.**
- An earlier cut drew a dark fill on all four sliders. Cropping the capture showed only
  Stylization has one; the faint hairlines between rows had been left out; the handle
  is a solid dot. All corrected (`FACTCHECK.md` §1).

**What Claude contributed — accepted, changed, rejected.**
- Claude built the panel scenes and cross-checked every figure against the docs.
- Accepted: settling the slider rendering by cropping the capture, not by memory.

**Understand now / still don't.**
- Now: the slider positions in a capture are evidence in their own right.
- Still open: `FACTCHECK.md` §6 lists an ear-check — how "Raw" lands — with no recorded result.
- Still open: the end card uses `ClaudeTitleOutro`, which was later locked to
  another channel and now ignores the handle it is given. The delivered master is
  correct — it was rendered before the lock — but a rebuild today would put the
  wrong channel on its end card.

**Evidence:** [`beat_sheet.json`](./beat_sheet.json) · [`FACTCHECK.md`](./FACTCHECK.md) · [`qc-sheet-16x9.png`](./qc-sheet-16x9.png) · [`check_beats.py`](./check_beats.py)

## 2026-09-24 — First commit to the fellows repository

**Working on.** Moving this piece of work into the fellows repository beside the rest,
as the renewal requirements ask, with a frictional log.

**Tried, and expected.** Expected to copy it across as it was. It needed more than that.

**Where it resisted, and what I did next.**
- This folder had never been committed to the fellows repository — the work lived
  only in my Lyrical Literacy workspace. Committed today, three weeks after it was
  built —
  [`fa99475`](https://github.com/nikbearbrown/humanitarians-youtube/commit/fa99475).
- My surname appeared in `FACTCHECK.md`, `PROMPTS.md`, `SHOTLIST.md`,
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
