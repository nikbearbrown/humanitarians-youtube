# QUESTION — claude-for-legal--claude-liam-feature-risk-assessment

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-feature-risk-assessment/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-08-03), but its narration text carries **literal, never-filled template
placeholders** (`>`) at every point where the actual skill-specific fact
should be — `"The skill is feature-risk-assessment. >."`, `"Claude's job: >."`,
`"The SKILL.md is the spec — >."`, `"I want to >."` The `source_skill` field it
names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/product-legal/skills/feature-risk-assessment/SKILL.md`,
does not exist anywhere on this machine (searched the whole `books/` tree —
no `feature-risk-assessment` SKILL.md, no `product-legal` folder). This is
the identical defect class already logged across most `claude-for-legal--*`
siblings in this batch (`ai-inventory`, `ai-tool-handoff`, `client-intake`,
`case-brief`, and others).

**What the source DOES state outright (kept, not reconstructed):** the B00
card's one-line description reads "Deeper risk assessment for a single
feature or product area when the" — itself cut off mid-sentence, but the
un-truncated portion is real: this is a **deeper** pass, scoped to **one**
feature or product area, not a broad audit. B01 (anatomy — one file,
SKILL.md, the instruction set, "the file is the program") and B02 (pipeline
— read SKILL.md, execute each step in order, return the result, linear
execution unless a step branches) are both fully authored, non-placeholder
facts and are carried forward.

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the missing beats (B00's specific framing,
the design-tell, the verdict, the handoff) into a generic, defensible
account of what a scoped, deeper feature-risk-assessment actually returns —
a documented checklist write-up, not a safe/unsafe verdict — using only the
skill's name, its one preserved description fragment, and the two fully
authored beats as ground truth. No fact here is Claude-specific or
unverifiable; it is the general shape of a checklist-driven review as it
applies to any single feature or product area, illustrated with a generic,
uncontroversial anchor (a photo-ID upload feature and four checklist
questions: what, where, how long, who).

**Question this reel actually answers:** You ask Claude to run a
feature-risk-assessment on a new feature before it ships. Does it hand back
a verdict — safe or not-safe — or something else?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
