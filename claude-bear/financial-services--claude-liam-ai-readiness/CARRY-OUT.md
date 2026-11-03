# CARRY-OUT — financial-services--claude-liam-ai-readiness

**The line (written first, GATE C):**

> A ranked AI-readiness list isn't Claude's judgment about which portfolio
> company is smartest to back — it's a ranking built from what this
> quarter's updates actually say, waiting for an operating partner's call
> before anything gets funded.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land (a
ranking computed from what's actually in the update vs. an operating
partner's judgment call about which company is the better bet, and a
ranked list vs. a funding decision), not the topic (AI adoption across a
portfolio generally).

**The wrong guess it defeats:** that asking Claude to "scan the portfolio
for AI readiness" means it decides, using its own judgment or domain
expertise, which company is most ready for or would most benefit from AI
investment. It doesn't. The `ai-readiness` skill reads a written SKILL.md
and, for each portfolio company, ingests the quarterly update and
financials, identifies the quick wins written there, and stacks them into
one ranked action list — nothing more. Give it a company whose update never
mentions an AI opportunity and it has nothing to rank for that company this
quarter; it will not invent an opportunity from general knowledge of the
industry.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope; this line compresses it into the reel's
carry-out.
