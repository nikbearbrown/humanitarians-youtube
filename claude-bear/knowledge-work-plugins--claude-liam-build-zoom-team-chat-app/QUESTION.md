# QUESTION.md

**Question (as redone for hai-simple):** Does asking Claude to "build Zoom
Team Chat App" mean it designs a brand-new chat application, or does
"build" mean something narrower here?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-team-chat-app`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-team-chat-app` Anthropic skill).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a
SKILL.md instruction file (a "skill" = a folder Claude reads before
acting); execution is linear — read the file, work each step in order,
return the result; it is a reference skill for Zoom Team Chat, used
**after** something has already routed the task to a chat workflow; its
coverage is one list — user-scoped messaging integrations, chatbot
experiences, rich cards, buttons, slash commands, and chat webhooks; the
boundary is that only what the instruction file specifies gets covered —
same input, same output, every run.
