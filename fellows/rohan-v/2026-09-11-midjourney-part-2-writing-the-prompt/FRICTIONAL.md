# FRICTIONAL — Midjourney, Part Two — Writing the Prompt

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-07 — Midjourney, Part Two (Lyrical Literacy tutorials)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's plan and factcheck, the series' build playbook and my dated session record
> with Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** How to write a good prompt, using Midjourney's own seven documented
elements as the spine and a real prompt from my captures as the worked example.

**Tried, and expected.**
- This part was not in the plan. I asked for a proper section on writing a good prompt,
  and it went in as Part 2 — teaching the dials before the words is backwards.
- Expected it to slot in cleanly.

**Where it resisted, and what I did next.**
- Inserting it cost a re-cut of Part 1, which had already promised that Part 2 was the
  action rail, and shifted every later part by one (`PLAN.md`, "Why this part exists").
- The worked example is a real prompt, and it does one thing the docs call unreliable —
  six exclusions written as plain text. B07 says so, and says no more than that
  (`FACTCHECK.md` §2).
- Checking cues against the word clock found four problems before any render,
  including an anchor orphaned by a trimmed word (`PLAN.md`).

**What Claude contributed — accepted, changed, rejected.**
- Claude built the seven-element structure from Midjourney's documentation, scored the
  real prompt against it and re-cut Part 1.
- Changed: the series order, at my request.

**Understand now / still don't.**
- Now: a series that never says how many parts it has can take a new part in the middle.
- Still open: `FACTCHECK.md` §7 lists an ear-check — the word "subject" as a noun — with
  no recorded result.
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
