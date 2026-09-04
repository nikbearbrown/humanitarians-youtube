# QUESTION.md

**Question (as redone for hai-simple):** Does "Contact Center, web" mean
Claude drops a ready-made chat widget onto your site — or does it mean
something else?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-contact-center/web`
(a rendered Teardown-register `claude-liam` reel walking through the
`contact-center/web` Anthropic skill — a partner-built Zoom skill).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a SKILL.md
instruction file (a "skill" = a folder Claude reads before acting); the
folder holds 6 items — RUNBOOK.md, SKILL.md, and folders for concepts,
examples, references, and troubleshooting; execution is linear — read the
file, work each step in order, return the result; the skill covers the Zoom
Contact Center SDK for Web, specifically: web chat/video/campaign embeds,
engagement event handling, app-context integrations, and Smart Embed
postMessage workflows; the boundary is that only what the instruction file
specifies gets covered — same input, same output, every run.
