# QUESTION.md

**Question (as redone for hai-simple):** When Claude "does content strategy,"
is that Claude writing your posts for you, or something else?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-content-strategy`
(a rendered Teardown-register `claude-liam` reel walking through the
`content-strategy` Anthropic skill — the `small-business` plugin's
sales-to-content-plan tool). The source sheet's own narration had unfilled
`>` template gaps in its design-tell and handoff beats (batch-build defect,
2026-07-25) and its `source_skill` path does not exist in this local tree,
so the actual facts were re-sourced directly from the real, public skill
file: `anthropics/knowledge-work-plugins/small-business/skills/content-strategy/SKILL.md`
on `github.com/anthropics/knowledge-work-plugins` (fetched this invocation).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a SKILL.md
instruction file (a "skill" = a folder Claude reads before acting);
execution is linear — pre-flight check, clarify priorities and metrics,
pull 90 days of sales data from QuickBooks, PayPal, or Square, layer in
seasonality, build the brief, then owner approval; it ranks products/
services into top 3–5 performers, bottom 3–5 slow movers, and trending
up/down; the output is a 30-day content brief with exactly six sections —
executive summary, push hard, hold steady, reposition or pause, seasonal
opportunities, recommended offers (200–400 words); the output is strategic
only — no calendar, no creative assets — and only feeds into a separate
skill (`canva-creator`) after the owner approves it.
