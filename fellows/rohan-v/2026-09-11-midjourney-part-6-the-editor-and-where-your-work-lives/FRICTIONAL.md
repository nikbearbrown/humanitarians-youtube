# FRICTIONAL — Midjourney, Part Six — The Editor, and Where Your Work Lives

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-08 → 2026-09-09 — Midjourney, Part Six (Lyrical Literacy tutorials)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's plan and factcheck, the series' build playbook and my dated session record
> with Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** The editor — three ways in, Move / Resize, Paint and transparency, Smart
Select, Submit Edit — and Organize, where your work lives and how to get files out.

**Tried, and expected.**
- I captured the editor screens for this part, then asked for a proper QC pass to make
  sure nothing overlapped, and checked that it had really rendered before accepting it.

**Where it resisted, and what I did next.**
- "Four separate tools" is a heteronym; now "four different tools". Rewording it
  orphaned its cue anchor, which the sync step caught (`FACTCHECK.md`).
- This part's own checker reported seven filter groups against six — it was counting a
  type declaration. The measurement was fixed rather than the threshold loosened.
- This is the only part ending on the HAI end card, `HaiTitleOutro`, which was built
  during this part.

**What Claude contributed — accepted, changed, rejected.**
- Claude built the editor scenes, fixed its own checker, and ran the QC pass I asked for.
- Accepted: fixing the checker's count instead of trusting a looser number.

**Understand now / still don't.**
- Now: a checker that is wrong about a count is worse than none, because it teaches you
  to ignore it.
- Still open: `FACTCHECK.md` §5 lists three ear-checks with no recorded result. The
  series went to Drive on 2026-09-16.

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
