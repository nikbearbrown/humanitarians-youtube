# CARRY-OUT — financial-services--claude-liam-cim-builder

**The line (written first, GATE C):**

> cim-builder doesn't write your CIM — it runs the SKILL.md's fixed steps
> on it, the same way every time.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(spec execution vs. authorship/judgment over deal content), not the topic
(what a CIM is, or M&A process generally).

**The wrong guess it defeats:** that asking Claude to build a CIM means it
is exercising the kind of judgment a banker would — deciding what the deal
story should emphasize, drafting narrative from its own sense of what
matters. It isn't. `cim-builder` is a folder Claude reads before it works;
the SKILL.md inside it is the full instruction set, executed step by step,
in order, with no branching unless a step says so. Give it the same
company information twice and it produces the same structure twice.
Whatever isn't covered by the file's steps simply isn't part of the job —
it will not invent judgment calls the spec doesn't specify.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope ("a skill is a folder," "the file is the
program," "same input → same output, every run," "know the limit: only
what the file says"); this line compresses it into the reel's carry-out.
