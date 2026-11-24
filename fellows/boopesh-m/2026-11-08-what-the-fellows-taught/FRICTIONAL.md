# FRICTIONAL — What the Fellows Taught

_Drafted by Claude (Claude Code) from the build session; Boopesh to read, correct and add his own entries._

## 2026-11-08
- **Tried:** reuse last week's `week_stats.py` as is. **Resisted:** it hard-coded one window and a fixed UTC−4
  offset, but daylight saving ended on Nov 1, so this week starts at UTC−4 and ends at UTC−5. **Did:** one
  `week()` function on `America/New_York` (`zoneinfo`), run for both weeks; the script asserts last week still
  reproduces its published 30 PRs / 84 folders / 22 fellows / 72 frictional logs, so the comparison is like for like.
- **Resisted:** the brief's "about 80 commits and 28 merges" vs the film's 26 pull requests. Both are right: the
  plain date window has 80 commits and 28 two-parent merges, but 3 of those merges are not pull requests (a direct
  merge and two "merge main into my branch" commits) and one PR (#366) was squash-merged, so it has one parent.
  25 + 1 = 26 merged PRs. Explained in FACTCHECK.md.
- **Resisted:** "what did they teach" is not in git. A subject sort by keywords first put most of one fellow's
  backlog under "making videos with AI", because the README *metadata* lines mention a narrator voice. **Did:**
  the sort now reads only the folder name, the title and the README's one-line description; said as "I sorted"
  / "my rough sort" in the film.
- **Resisted:** last week's kind rule treats any folder name containing `work-` as a progress video, which caught
  `how-ai-pms-work-with-llms` (a lesson). And one folder (`hrishikesh-p/2026-11-06 - RamanEffect`) has no README;
  its beat sheet is a "Week 10 Summary", not a Raman-effect explainer. **Did:** `work-` only right after the date,
  and the beat-sheet title stands in for a missing README. Checked that last week's split is unchanged (42/30).
- **Resisted:** 45 of the 74 "new" folders carry older dates (backlogs filed this week, one fellow alone adds 21
  folders). Shown as 28 dated this week / 45 older, instead of implying all 74 were made this week.
- **Resisted:** example titles. I first picked one dated Oct 30; switched to six that are dated Nov 1–7 and
  asserted it in the script.
- **Resisted:** wording about my own videos. Drive submission of last week's videos is unconfirmed, so the film
  says "made" and "delivered for review", never "submitted to Drive".
- **Resisted:** fill/edge pre-check — the B20 legend and B30 subject labels crossed the title-safe edge at 1080p;
  shrank and moved them; the dated-strip labels overlapped and were restacked.
- **Resisted:** GATE B (strict layout audit) blocked twice: the landscape comparison footnote sat 0.09 units below
  the safe area, and the Short's subject labels started 0.05 units left of it. Moved both inside.
- **Resisted:** GATE T on the Short: labels were below the 72 px text floor (a long title was auto-shrinking its
  whole card; "last/this" labels; words with no ascenders such as "new" measure only their x-height). Enlarged
  them, dropped the play icon from the Short's video cards, and re-rendered (the build skips filled beats, so
  the stale clips had to be removed first).
- **Resisted:** Gate V on the review cuts flags `edge-bleed` on every frame — the burned-in review timestamps.
  The clean final's frame check is what counts (0 BLOCKER / 0 MAJOR).
- **AI contribution:** Claude adapted and ran `code/week_stats.py`, drafted script, sheets and scenes, rendered.
  Kokoro `am_onyx` speaks the narration.
- **Still open:** my own folder is not on GitHub: the fork attempt failed; pull request pending. The subject and
  kind sorts are heuristics. Pronunciation (e.g. "RAG", "Goodhart's") checked by phonemes only — needs a human listen.

---

## 2026-11-24 — Submission note for the week of Nov 1–7 (written later than the week it describes)

**Record provenance:** added on 2026-11-24 by Claude (Claude Code) at Boopesh's request, when this folder was
first committed. The entries above were drafted during the build, in the week of the work.

- **Why this commit is late:** the films and this source were delivered in the week of Nov 1–7. They could not
  be committed then: Boopesh's fork of the repository failed, and push access only arrived on 2026-11-24.
  This folder is restored unchanged from the source archive delivered that week.
- **Who did what:** Boopesh gave the prompts and instructions for the week (the topic direction, and
  the voice approval on 2026-10-24) and reviewed the delivered videos and code. Claude did the research,
  code, scenes, narration script and rendering.
- **Still open:** the Drive link for each film goes in this folder's README; Boopesh to add any notes of
  his own on what he checked, changed or rejected.
