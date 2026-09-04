# QUESTION.md

**Question (as redone for hai-simple):** What does it actually mean to have Claude
"check" a pitch deck before it goes out to a client?

**Source:** redo of `anthropics/financial-services/youtube/claude-liam-ib-check-deck`
(a rendered Teardown-register `claude-liam` reel walking through the `ib-check-deck`
Anthropic skill — an investment-banking presentation quality checker).

**Asker:** nobody named — the source reel framed this as a general skill teardown,
not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a SKILL.md
instruction file (a "skill" = a folder Claude reads before acting); execution is
linear — read the file, work each step in order, return the result; the check
itself covers exactly four things — (1) number consistency across slides, (2)
data-narrative alignment, (3) language polish against IB standards, (4) visual and
formatting QC; the boundary is that only what the instruction file specifies gets
checked.
