# QUESTION.md

**Question (as redone for hai-simple):** Does Claude already know your numbers
every Monday, or does it have to check them?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-monday-brief` (a
rendered Teardown-register `claude-liam` reel walking through the
`monday-brief` Anthropic skill — a Monday-morning business briefing
generator).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** a "skill" is one file
(`SKILL.md`, ~2k, 1 file total) that Claude reads before it works, written in
plain language, with no hidden logic — the file is the program; execution is
linear — read the file, run each step in order, return the result, no
branching unless a step says so; this specific skill generates a one-page
Monday morning briefing covering exactly cash, sales, pipeline, the week
ahead, and the top three to-dos; it accepts optional arguments for a post
destination and a save-to location; the boundary is that only what the file
specifies gets covered — same input, same output, every run.
