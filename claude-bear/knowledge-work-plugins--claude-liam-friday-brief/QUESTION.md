# QUESTION.md

**Question (as redone for hai-simple):** What does Claude's "Friday Brief" actually
check — outside market news, or something else?

**Source:** redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-friday-brief`
(a rendered Teardown-register `claude-liam` reel walking through the `friday-brief`
Anthropic skill — a small-business end-of-week pulse generator).

**Asker:** nobody named — the source reel framed this as a general skill teardown,
not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a SKILL.md
instruction file (a "skill" = a folder Claude reads before acting); execution is
linear — read the file, work each step in order, return the result; the skill
delivers a Friday end-of-week pulse for a small business covering exactly four
things — revenue measured against the prior week, top sellers, wins, and watches;
it accepts an optional lookback window of 7 or 14 days; the boundary is that only
what the instruction file specifies gets covered — same input, same output, every
run.
