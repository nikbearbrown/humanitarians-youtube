# CARRY-OUT — financial-services--claude-liam-financial-plan

**The line (written first, GATE C):**

> A financial plan from Claude is its skill running fixed steps over the
> inputs you gave it — not a judgment about what's best for you. Change the
> input, and the plan updates; that's all that happened.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land (a
fixed procedure that turns inputs into a plan vs. an advisor's independent
judgment about what's best for a client), not the topic (financial planning
generally).

**The wrong guess it defeats:** that a Claude financial plan reflects its own
judgment about what's best for the client — the way a human advisor who has
gotten to know someone's full situation reaches a conclusion. It doesn't. The
`financial-plan` skill reads a written SKILL.md and only recognizes the cases
it names (new client onboarding, an annual review, a scenario request), only
producing the four things it names (retirement projections, education
funding, estate planning, cash flow analysis). Ask for something outside that
list and there's no independent expertise underneath to fall back on —
there's simply no step for it.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's B00 narration already
states the skill's scope in full; this line compresses it into the reel's
carry-out.
