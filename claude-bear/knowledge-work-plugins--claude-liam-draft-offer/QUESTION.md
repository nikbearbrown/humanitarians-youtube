# QUESTION.md

**Question (as redone for hai-simple):** When Claude "drafts an offer," is that
just writing the congratulatory letter — or is there more to it?

**Source:** redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-draft-offer`
(a rendered Teardown-register `claude-liam` reel walking through the `draft-offer`
Anthropic skill — an HR offer-letter generator).

**Asker:** nobody named — the source reel framed this as a general skill teardown,
not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a SKILL.md
instruction file (a "skill" = a folder Claude reads before acting); execution is
linear — read the file, work each step in order, return the result; the skill
covers exactly three things once a candidate is ready for an offer — (1)
assembling the total comp package (base, equity, signing bonus), (2) writing the
offer letter text itself, and (3) prepping negotiation guidance for the hiring
manager; the boundary is that only what the instruction file specifies gets
covered — same input, same output, every run.
