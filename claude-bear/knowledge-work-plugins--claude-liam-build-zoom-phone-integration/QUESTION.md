# QUESTION.md

**Question (as redone for hai-simple):** Can Claude actually answer or route my
Zoom phone calls itself — or does "build Zoom phone integration" mean something
else?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-phone-integration`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-phone-integration` Anthropic skill).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a SKILL.md
instruction file (a "skill" = a folder Claude reads before acting); execution
is linear — read the file, work each step in order, return the result; this
is a reference skill for Zoom Phone, used after a request has already routed
to a phone workflow; it covers implementing OAuth, the Phone APIs, webhooks,
Smart Embed events, URI schemes, CRM or CTI dialer integration, and call
handling automation; the boundary is that only what the instruction file
specifies gets covered — same input, same output, every run.
