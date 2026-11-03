# QUESTION.md

**Question (as redone for hai-simple):** When Claude "creates an asset," is
that a generic template it invents on its own, or something built from your
specific deal?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-create-an-asset`
(a rendered Teardown-register `claude-liam` reel walking through the
`create-an-asset` Anthropic skill — a sales-asset drafting tool).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a SKILL.md
instruction file inside a folder Claude reads before acting (source anatomy
lists three files: `QUICKREF.md`, `README.md`, `SKILL.md`); execution is
linear — read the file, work each step in order, return the result; the
skill generates tailored sales assets across exactly four types — landing
pages, decks, one-pagers, and workflow demos — from your deal context: you
describe your prospect, audience, and goal, and get back a polished,
branded asset ready to share with customers; the trigger for using it is
needing a sales asset built around a specific deal, not a generic template;
the boundary is that only what the instruction file specifies gets
covered — same input, same output, every run.
