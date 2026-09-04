# QUESTION.md

**Question (as redone for hai-simple):** What does Claude actually mean by a
"legal briefing" — is it just a news digest, or something else?

**Source:** redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-brief`
(a rendered Teardown-register `claude-liam` reel walking through the `brief`
Anthropic skill — a legal-work briefing generator).

**Asker:** nobody named — the source reel framed this as a general skill teardown,
not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a SKILL.md
instruction file (a "skill" = a folder Claude reads before acting); execution is
linear — read the file, work each step in order, return the result; the skill
covers exactly three situations — (1) a daily scan of legal-relevant items across
email, calendar, and contracts, (2) research on one legal question across internal
sources, (3) rapid context for a developing situation (data breach, litigation
threat, regulatory inquiry); the boundary is that only what the instruction file
specifies gets covered — same input, same output, every run.
