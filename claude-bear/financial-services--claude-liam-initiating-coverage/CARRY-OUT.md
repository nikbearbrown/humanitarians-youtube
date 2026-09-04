# CARRY-OUT — financial-services--claude-liam-initiating-coverage

**The line (written first, GATE C):**

> Initiating coverage doesn't mean Claude writes a report in one pass — it
> runs five fixed tasks, in order, and each one is blocked until the task
> before it hands over a verified deliverable. A finished report means the
> chain completed end to end, not that a person checked the assumptions
> inside it.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land (a
dependency-gated, five-task pipeline vs. one continuous generation pass,
and chain-completed vs. assumption-verified), not the topic (equity
research generally).

**The wrong guess it defeats:** that asking Claude to "initiate coverage"
on a company means it writes the whole research report in one continuous
pass, choosing whatever order makes sense. It doesn't. The
`initiating-coverage` skill reads a written SKILL.md and runs exactly five
ordered tasks — company research, financial modeling, valuation analysis,
chart generation, final report assembly — each executed individually with
its prerequisite verified first. Ask it to jump straight to valuation
before a financial model exists, and there is nothing to value: task
three's prerequisite isn't there, so it can't run.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's five-task scope and its dependency structure; this line
compresses it into the reel's carry-out.
