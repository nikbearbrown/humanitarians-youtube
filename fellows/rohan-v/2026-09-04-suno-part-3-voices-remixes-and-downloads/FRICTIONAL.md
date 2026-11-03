# FRICTIONAL — Suno, Part Three — Voices, Remixes and Downloads

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-08-31 — Suno, Part Three (Lyrical Literacy tutorials)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's plan and factcheck, the series' build playbook and my dated session record
> with Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** The series finale: what you bring into Suno (audio, a voice,
inspiration, sounds) and what you do with what comes out (remix, edit, extend,
download). Everything Part 2 promised lands here.

**Tried, and expected.**
- Planned it methodically and asked for the specific screenshots it needed before
  building. Expected the captures to fill gaps.

**Where it resisted, and what I did next.**
- They overturned the assumed model instead (`PLAN.md`, "What the new captures
  changed"): Remix and Edit reopen the Advanced panel rather than opening dialogs;
  Extend sits under Edit and has a real keep-and-recreate interface; the card menu has
  ten actions, not five; the download tiers are now verified.
- One of those corrections landed on Part 1, which had already shipped a wrong menu.
  Part 1 was corrected and re-rendered the same day.
- The build ran long enough that I asked twice what was taking so long.

**What Claude contributed — accepted, changed, rejected.**
- Claude read the six new captures, wrote the plan, rebuilt the scenes, and traced the
  correction back into Part 1.
- Accepted: fixing Part 1 rather than leaving the error in a shipped training video.

**Understand now / still don't.**
- Now: assumptions about an interface should be treated as wrong until a capture shows them.
- Still open: `PLAN.md` keeps a list of things never captured, which the series
  deliberately does not depict.
- Still open: the end card uses `ClaudeTitleOutro`, which was later locked to
  another channel and now ignores the handle it is given. The delivered master is
  correct — it was rendered before the lock — but a rebuild today would put the
  wrong channel on its end card.

**Evidence:** [`beat_sheet.json`](./beat_sheet.json) · [`PLAN.md`](./PLAN.md) · [`qc-sheet-16x9.png`](./qc-sheet-16x9.png)

## 2026-09-24 — First commit to the fellows repository

**Working on.** Moving this piece of work into the fellows repository beside the rest,
as the renewal requirements ask, with a frictional log.

**Tried, and expected.** Expected to copy it across as it was. It needed more than that.

**Where it resisted, and what I did next.**
- This folder had never been committed to the fellows repository — the work lived
  only in my Lyrical Literacy workspace. Committed today, three weeks after it was
  built —
  [`fa99475`](https://github.com/nikbearbrown/humanitarians-youtube/commit/fa99475).
- My surname appeared in `PROMPTS.md`, `SHOTLIST.md`, `beat_sheet.json`; the
  repository allows a first name and last initial only. Now "Rohan V." on screen and
  "Rohaan" spoken, so a rebuild would no longer match the Drive master exactly —
  that still carries my full name.
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
