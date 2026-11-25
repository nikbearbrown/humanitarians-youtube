# FRICTIONAL — One Week of Fellows

_Drafted by Claude (Claude Code) from the build session; Boopesh to read, correct and add his own entries._

## 2026-11-01
- **Tried:** count "what the fellows shipped" with a plain `git log --since/--until`. **Found:** that misses
  commits authored before the window but merged inside it, and mixes time zones (some merges are stamped −0700).
  **Did:** counted everything that landed on main between `c9fca929` (main when the week began) and `bc722c05`,
  bucketed by US Eastern time, and asserted every mainline commit falls inside Oct 25–31.
- **Resisted:** the coordinator's quick count was 29 merges / 35 names for Oct 24–31. With the exact Oct 25–31
  window there are 29 "Merge pull request" commits **plus one squash-merged PR (#312)** that the grep missed → 30.
  The film says 30 and explains the split.
- **Resisted:** "contributors" is not one number. 37 author names; one person often commits under a full name on
  one machine and a handle on another. Merged only mechanical matches (same email, same GitHub noreply account,
  name = handle, same letters) → 27. Two more look-alike pairs left separate on purpose (film says so). 4 of the 27
  only ever appear on merge commits (they merged others' work) → 23 wrote the work.
- **Resisted:** "93 new folders" over-counts: 9 are one fellow's existing videos renamed to dated folder names
  (files moved R100, plus a new FRICTIONAL.md). Counted 84 new work folders.
- **Resisted:** many "new" folders carry September/early-October dates — older work filed this week (a new fellow
  folder arriving with its backlog). Shown on screen as 27 dated this week / 33 older / 24 undated, instead of
  implying all 84 were made this week.
- **Resisted:** the STEM-vs-progress split is a heuristic on folder names and README openings; said "my rough sort".
- **Resisted:** privacy. Git author names include full surnames and emails. `results.json` and the film show only
  fellow folder names (e.g. `jash-s`) and "First L."; the narration names no fellow.
- **Resisted:** the hesitant-writer beat first rendered without the correction (trigger words ended in a period
  the component didn't match). Fixed and re-rendered; checked the last frame.
- **Resisted:** the Short's "My part" beat used screenshots of last week's videos; they failed the contrast check,
  then the minimum-text-size check (tiny text inside the screenshots). Replaced them with plain cards (title, type,
  durations, 4K). The landscape keeps the real frames, where they pass.
- **AI contribution:** Claude wrote `code/week_stats.py`, ran it, drafted script, sheets and scenes, rendered.
  Kokoro `am_onyx` speaks the narration.
- **Still open:** my own folder is not on GitHub: the fork attempt failed; asking the maintainer for access.
  Drive upload status is from Boopesh, not checkable from git. Pronunciation (e.g. "R L H F") needs a human listen.

---

## 2026-11-24 — Submission note for the week of Oct 25–31 (written later than the week it describes)

**Record provenance:** added on 2026-11-24 by Claude (Claude Code) at Boopesh's request, when this folder was
first committed. The entries above were drafted during the build, in the week of the work.

- **Why this commit is late:** the films and this source were delivered in the week of Oct 25–31. They could not
  be committed then: Boopesh's fork of the repository failed, and push access only arrived on 2026-11-24.
  This folder is restored unchanged from the source archive delivered that week.
- **Who did what:** Boopesh gave the prompts and instructions for the week (the topic direction, and
  the voice approval on 2026-10-24) and reviewed the delivered videos and code. Claude did the research,
  code, scenes, narration script and rendering.
- **Still open:** the Drive link for each film goes in this folder's README; Boopesh to add any notes of
  his own on what he checked, changed or rejected.
