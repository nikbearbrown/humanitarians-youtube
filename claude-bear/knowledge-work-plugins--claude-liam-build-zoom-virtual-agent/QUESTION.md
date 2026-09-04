# QUESTION.md

**Question (as redone for hai-simple):** Does "build a Zoom virtual agent" mean
Claude itself becomes the AI that chats with my customers — or does it mean
something else?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-virtual-agent`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-virtual-agent` Anthropic skill).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a SKILL.md
instruction file (a "skill" = a folder Claude reads before acting); the folder
holds 8 items — RUNBOOK.md, SKILL.md, and folders for android, concepts, ios,
references, scenarios, troubleshooting; execution is linear — read the file,
work each step in order, return the result; the skill is a *reference* skill
for Zoom Virtual Agent, used after routing to a virtual-agent workflow, scoped
to five things: web embeds; Android or iOS wrapper integrations;
knowledge-base sync; lifecycle handling; and troubleshooting; it fits code
around Zoom's existing Virtual Agent product rather than replacing it; the
boundary is that only what the instruction file specifies gets covered — same
input, same output, every run.
