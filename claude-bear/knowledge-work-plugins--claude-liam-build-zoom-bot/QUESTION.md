# QUESTION.md

**Question (as redone for hai-simple):** Can Claude actually be my Zoom bot —
join my meetings itself — or does "build Zoom bot" mean something else?

**Source:** redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-bot`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-bot` Anthropic skill).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a
SKILL.md instruction file (a "skill" = a folder Claude reads before
acting); execution is linear — read the file, work each step in order,
return the result; the skill builds a Zoom meeting bot, a recorder, or a
real-time media workflow; it applies when joining meetings
programmatically, processing live media or transcripts, or combining
Zoom's Meeting SDK, RTMS (real-time media streams), and backend services;
the boundary is that only what the instruction file specifies gets
covered — same input, same output, every run.
