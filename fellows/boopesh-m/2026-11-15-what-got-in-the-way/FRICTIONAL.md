# FRICTIONAL — What Got in the Way

_Drafted by Claude (Claude Code) from the build session; Boopesh to read, correct and add his own entries._

## 2026-11-15
- **Tried:** reuse last week's `week_stats.py` and its check that last week still reproduces (26 PRs / 74 folders /
  18 fellows / 95 frictional logs). **Resisted:** the assert failed: recounted on today's history, Nov 1–7 gives
  27 / 75 / 19 / 95. PR #375 merged on Sat Nov 7 at 21:07 EST, inside last week's window but after last week's data
  was fetched. **Did:** `week()` takes an optional tip; the script asserts the published numbers on `a953b021`
  (main as it was then) *and* uses today's recount for the comparison, with the difference shown on screen.
- **Resisted:** the brief's "about 91 commits and 23 merge commits" vs the film's 19 pull requests. Both are right:
  of the 23 two-parent merges, 3 are direct merges, and one "Merge pull request" (#389) merged main into a fellow's
  branch, so it is not on main's first-parent line. No squash merges this week. Explained in FACTCHECK.md.
- **Resisted:** "what got in the way" is free text in 32 differently shaped logs (bullets, numbered sections,
  long diaries, one log that is really a video description). **Did:** a keyword theme sort, one log counted once
  per theme, on the log minus its contribution / understood-now / expected / link sections. First passes
  mis-sorted: "runtime" (a Kaggle runtime) counted as video length, "the LSTM's memory" as a machine-memory problem,
  "Node vm driver" as a setup problem, sub-headings under "AI contributions" leaked in, and "didn't match the
  narration" counted as a facts problem. Tightened each rule and read every log's matched keywords in `run.log`.
  Said as "my rough sort"; 2 logs fit no theme and are reported, not forced.
- **Resisted:** examples. My first picks used one fellow twice; switched to five fellows, one per theme, and the
  script asserts each paraphrase's source wording is in the log. Paraphrased short, never quoted at length, folder
  names only, and each example shown with its fix, so friction reads as normal work, not blame.
- **Resisted:** "what fixed them" isn't one field either. **Did:** a second rough count — logs where a problem was
  found by watching the cut, viewing frames or re-reading the words (17 of 31) — and wrote the film's takeaway
  from it.
- **Resisted:** wording about my own videos. Drive submission is not claimed; the film says "delivered for review".
  My own obstacle this week is access: the fork attempt failed and my pull request is pending.
- **Resisted:** fill/edge pre-check (1080p): B20's strip caption crossed the right title-safe edge; B60's duration
  lines crossed the left edge while `Indicate` scaled them; B40 at 54% fill on the 50% sample. Shortened the strip,
  shrank the video pair and dropped the scale on `Indicate`, and showed B40's statement and bottom line as dim
  ghosts from the start. Small bold text also collapsed word spaces ("atthe"); text is now set 4× larger and scaled
  down (the Short's trick), which fixed it.
- **Resisted:** the gates, which fits the film's own top theme. GATE A (static stub) choked on `get_y() - 0.6`;
  strict GATE B caught a footnote 0.02 units below the safe area; GATE T failed the landscape B40 (outlined boxes
  read as text runs around their own words) and, twice, the Short's B30 (64 px x-height-only words in card titles,
  under the 72 px floor). Filled panels, bigger titles, caps label; re-rendered. Clean finals: 0 BLOCKER / 0 MAJOR.
- **AI contribution:** Claude adapted and ran `code/week_stats.py`, read all 32 logs, drafted script, sheets and
  scenes, rendered and checked frames. Kokoro `am_onyx` speaks the narration.
- **Still open:** my folder is not on GitHub (fork attempt failed; pull request pending). The theme sort and the
  "found by looking" count are keyword heuristics; a human sort could move a few logs. Pronunciation checked by
  phonemes only — needs a human listen.

---

## 2026-11-24 — Submission note for the week of Nov 8–14 (written later than the week it describes)

**Record provenance:** added on 2026-11-24 by Claude (Claude Code) at Boopesh's request, when this folder was
first committed. The entries above were drafted during the build, in the week of the work.

- **Why this commit is late:** the films and this source were delivered in the week of Nov 8–14. They could not
  be committed then: Boopesh's fork of the repository failed, and push access only arrived on 2026-11-24.
  This folder is restored unchanged from the source archive delivered that week.
- **Who did what:** Boopesh gave the prompts and instructions for the week (the topic direction, and
  the voice approval on 2026-10-24) and reviewed the delivered videos and code. Claude did the research,
  code, scenes, narration script and rendering.
- **Still open:** the Drive link for each film goes in this folder's README; Boopesh to add any notes of
  his own on what he checked, changed or rejected.
