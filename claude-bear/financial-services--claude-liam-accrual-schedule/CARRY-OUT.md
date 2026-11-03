# CARRY-OUT — financial-services--claude-liam-accrual-schedule

**The line (written first, GATE C):**

> A drafted accrual JE isn't Claude's judgment about what you owe — it's a
> computed entry, tied to cited support, waiting for a controller's
> approval before anything posts.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(a computed, cited entry vs. an accountant's judgment call about what
belongs in the close, and a draft vs. a posting), not the topic (accrual
accounting generally).

**The wrong guess it defeats:** that asking Claude to "build the accrual
schedule" means it decides, using its own accounting judgment, which
expenses or revenues to accrue and how much. It doesn't. The
`accrual-schedule` skill reads a written SKILL.md and, for each accrual,
computes the entry and cites the support document that backs it — nothing
more. Give it an expense with no supporting document and it has nothing to
cite, so it drafts nothing; it will not invent a number from general
accounting knowledge.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope; this line compresses it into the reel's
carry-out.
