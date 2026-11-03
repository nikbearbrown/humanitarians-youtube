# FRICTIONAL — Suno, Part One — Your First Song

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-08-29 → 2026-08-31 — Suno, Part One (Lyrical Literacy tutorials)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's plan and factcheck, the series' build playbook and my dated session record
> with Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** The first of three Suno training videos for new Lyrical Literacy
volunteers. New people join constantly, most with no background in music, music
production or AI tools, and there was no onboarding material at all.

**Tried, and expected.**
- Every Suno screen rebuilt as animated mockups — I would not be recording anything —
  planned in full, beat sheet and script, before any build.
- Expected the recreation to match Suno exactly: the navigation, the elements, the cards.

**Where it resisted, and what I did next.**
- Research alone got the interface wrong in three places: an invented "Regenerate"
  button on the song card, a three-item sidebar where Suno has six, and a
  Discord-only sign-in where Suno offers Discord or Google. Corrected 2026-08-29
  (`FACTCHECK.md`, corrections log).
- The first cut came back at 720p, not 4K, with overlapping text and graphics — no QC
  had been run. It also pitched Humanitarians AI's free Pro access far too often; this
  is internal training and should simply show how to get the account. Sent it back.
- The mockups still didn't look enough like Suno, so I captured the real interface
  myself as reference (listed in `../2026-09-04-suno-interface-research/CAPTURES.md`).
- The next cut had no title on the end card, and animations and cards ran ahead of or
  behind the voiceover. Timing every reveal to the measured spoken word fixed it, and
  every video I have made since is built that way.
- "Where the actions live" was read as in *live TV*; the three-dot menu overlapped the
  card below it; the cut into the end card flashed. All three fixed.
- Part 3's captures later showed this part's menu beat was wrong — Extend is not a
  top-level item, and its "+15s or +30s" was invented. B08 rewritten and re-rendered
  on 2026-08-31 (`../2026-09-04-suno-part-3-voices-remixes-and-downloads/PLAN.md`).

**What Claude contributed — accepted, changed, rejected.**
- Claude researched Suno, wrote the plan and beat sheet, rebuilt the interface as
  Remotion scenes, rendered and QC'd, and — when I asked it to keep what it had learnt
  for the later parts — wrote the series playbook (`../2026-09-04-suno-interface-research/SERIES-PIPELINE.md`).
- Accepted: rebuilding the interface instead of recording it.
- Changed: the register (internal training, not promotion), the timing, the pronunciation.
- Rejected: the first cut, and mockups that did not match the real thing.

**Understand now / still don't.**
- Now: a recreated interface is only as good as its reference. The captures fixed
  what research alone had got wrong, including one mistake that had already shipped.
- Still open: the Suno workspace mockup (B04) copied its Staff Picks row straight from
  my Explore capture, so the delivered video shows four real Suno creators' names and
  song titles. They are public picks, and this is internal training — but they are
  other people's names, and a placeholder row would be the cleaner choice.
- Still open: the end card uses `ClaudeTitleOutro`, which was later locked to
  another channel and now ignores the handle it is given. The delivered master is
  correct — it was rendered before the lock — but a rebuild today would put the
  wrong channel on its end card.

**Evidence:** [`beat_sheet.json`](./beat_sheet.json) · [`FACTCHECK.md`](./FACTCHECK.md) · [`CHECKS-REPORT.md`](./CHECKS-REPORT.md) · [`qc-sheet-16x9.png`](./qc-sheet-16x9.png)

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
- In that contact sheet the workspace tile carries four real Suno creators' names
  under the Staff Picks row. Blurred that one line before committing; nothing else
  in the sheet is altered.
- Added this log.

**What Claude contributed — accepted, changed, rejected.** Claude assembled the folder,
checked every file and capture for personal data, and proposed the changes as their own
commits in the same pull request as the rest of my compliance pass.

**Understand now / still don't.**
- Now: a piece of work that only exists in a private workspace is not on the record.
- Still open: none of this was written while the work happened. From here on the log is
  kept during the build.

**Evidence:** [`fa99475`](https://github.com/nikbearbrown/humanitarians-youtube/commit/fa99475)
