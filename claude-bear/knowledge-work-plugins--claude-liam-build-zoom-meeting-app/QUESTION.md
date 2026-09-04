# QUESTION.md

**Question (as redone for hai-simple):** Does Claude write a whole new
video-calling engine when you ask it to "build a Zoom meeting app," or
does "build Zoom meeting app" mean something else?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-meeting-app`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-meeting-app` Anthropic skill).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a
SKILL.md instruction file (a "skill" = a folder Claude reads before
acting); execution is linear — read the file, work each step in order,
return the result; the skill's job is to "build or embed a Zoom meeting
flow"; it applies when implementing Meeting SDK joins, web or mobile
meeting embeds, meeting lifecycle flows, or when deciding between the
Meeting SDK and the Video SDK; the boundary is that only what the
instruction file specifies gets covered — same input, same output, every
run.
