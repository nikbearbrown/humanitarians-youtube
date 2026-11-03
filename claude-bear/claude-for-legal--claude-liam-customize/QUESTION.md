# QUESTION — claude-for-legal--claude-liam-customize

**Question:** Claude, Customize.

**Who asked / where:** Redo-mode build. `SUBJECT.json` points at
`anthropics/claude-for-legal/youtube/claude-liam-customize/beat_sheet.json` as the
source — a Teardown-register skill-teardown of an Anthropic skill named `customize`,
built in a 2026-07-25 batch (`PEDAGOGY.md`: "Batch build — skill teardown format",
verdict PASS).

**Source defect found on read:** the source's narration carries a literal unfilled
`>` character in four of its seven beats, sitting exactly where `customize`'s own
concrete content should have been substituted — B00 ("The skill is customize.
**>**."), B03 ("Claude's job: **>**."), BVDT ("The SKILL.md is the spec —
**>**."), BHTF ("I want to **>**. Read the customize skill…"). The
`metadata.source_skill` path (`/Users/bear/Documents/CoWork/bear-textbooks/books/
anthropics/claude-for-legal/ai-governance-legal/skills/customize/SKILL.md`) does not
exist on this machine — it is a path from the original build machine, unreachable
here. This is the identical batch template-substitution bug already found and logged
on this family's `auto-updater`, `clearance`, `cease-desist`, `board-minutes`,
`bar-prep-questions`, `ai-inventory`, and `ai-tool-handoff` siblings (all seven
checked directly: every one carries the same unresolved `>` placeholder count in the
same four beat slots). It is a defect in the original pipeline, not a stylistic
choice, and not unique to this reel.

**What this redo keeps, and what it does not invent:** every fact the source's
*readable* text establishes is kept and generalized — a Skill is a folder Claude
reads before it works; the `SKILL.md` file is the full instruction set in plain
language, not hidden logic ("the file is the program"); the pipeline lives in a
Steps section, read top to bottom, executed in order, no branching unless a step
says so; run the same request through it twice and the same steps produce the same
result; the guarantee holds only for what the file specifies, nothing outside it.
Per hai-simple's "when in doubt, describe behavior generically" rule, this reel
never invents what `customize` specifically customizes — it uses `customize` only
as the *name* of the example skill folder, and states only the generic, true
mechanism of how any Claude Skill works. The one inference this reel does make,
stated plainly rather than hedged, is the ordinary reading of the word itself:
a skill named "customize" governs how Claude's *output* is shaped to a spec (not a
change to Claude's own personality or behavior generally) — that reading is what
the wrong-guess correction in B00 exists to make explicit and then correct.

**Carry-out it's built to defeat:** the newcomer's guess that "Claude, customize"
means changing something about Claude itself. The correction: it's a spec for one
task's output, applied the same way every time, and nothing outside that spec.
