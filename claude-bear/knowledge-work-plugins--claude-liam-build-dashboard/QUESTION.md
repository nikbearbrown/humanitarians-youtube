# QUESTION.md

**Question (as redone for hai-simple):** When Claude "builds a dashboard," is
that a live app, or something else?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-dashboard`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-dashboard` Anthropic skill).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill builds an
interactive HTML dashboard with charts, filters, and tables; it applies to
four situations — (1) an executive overview with KPI cards, (2) turning
query results into a shareable self-contained report, (3) a team monitoring
snapshot, (4) multiple charts with filters bundled in one browser-openable
file; a "skill" is a folder Claude reads before it works, and the SKILL.md
inside is the whole instruction set; execution is linear — read the file,
work each step in order, return the result; the boundary is that only what
the instruction file specifies gets covered — same input, same output,
every run. The output artifact is a single self-contained HTML file that
opens directly in a browser — this is stated directly in the source's own
trigger conditions ("shareable self-contained report," "browser-openable
file"), not invented.
