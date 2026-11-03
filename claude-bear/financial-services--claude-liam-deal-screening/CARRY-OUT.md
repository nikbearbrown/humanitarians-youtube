# CARRY-OUT — financial-services--claude-liam-deal-screening

**The line (written first, GATE C):**

> deal-screening doesn't decide if you should do the deal — it runs the
> SKILL.md's pass/fail checks against your criteria and hands you a memo,
> the same way every time.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(spec execution / triage vs. the investment decision itself), not the
topic (what a CIM or teaser is, or deal flow in general).

**The wrong guess it defeats:** that asking Claude to screen a deal means
it is exercising the kind of judgment a partner would — weighing the
opportunity and deciding whether the fund should pursue it. It isn't.
`deal-screening` is a folder Claude reads before it works; the SKILL.md
inside it is the full instruction set, executed step by step, in order,
with no branching unless a step says so. Give it the same CIM twice
against the same criteria and it produces the same pass/fail memo twice.
Whatever isn't covered by the file's steps simply isn't part of the job —
it will not make the call on whether to take the first call.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope ("a skill is a folder," "the file is the
program," "same input → same output, every run," "know the limit: only
what the file says"); this line compresses it into the reel's carry-out.
