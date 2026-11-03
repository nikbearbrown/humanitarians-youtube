# QUESTION.md

**Question (as redone for hai-simple):** If Claude "builds a Zoom video SDK
app," does that mean it builds you an app that runs an actual Zoom meeting —
or something else?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-video-sdk-app`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-video-sdk-app` Anthropic skill).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill runs from a
SKILL.md instruction file (a "skill" = a folder Claude reads before
acting); execution is linear — read the file, work each step in order,
return the result; the skill is a reference for Zoom's Video SDK, used
after the work is already routed to a custom-session workflow, when the
user needs full control over the video experience rather than an actual
Zoom meeting; the platform surface is six clients — Android, Flutter, iOS,
Linux, macOS, and React Native; the boundary is that only what the
instruction file specifies gets covered — same input, same output, every
run.
