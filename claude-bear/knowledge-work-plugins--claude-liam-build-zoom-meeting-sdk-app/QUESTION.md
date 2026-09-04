# QUESTION.md — knowledge-work-plugins--claude-liam-build-zoom-meeting-sdk-app

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-build-zoom-meeting-sdk-app`, a
skill-teardown walk through the Anthropic `build-zoom-meeting-sdk-app`
Claude Skill from the `knowledge-work-plugins` book's Zoom partner-built
plugin) into the Plain register for @HumanitariansAI, per hai-simple's
redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When Claude builds a Zoom meeting into an app, does it design that
> integration on its own, or is it following a file that already has the
> platform's rules written down?

**The naive framing (what B00 types and corrects):** "Does Claude design a
whole Zoom meeting app?" — the newcomer's assumption is that Claude
improvises the integration itself, the way a person designs something new.
It doesn't. `build-zoom-meeting-sdk-app` is a reference skill: it's read
only after a build has already been routed to a meeting-embed workflow,
and it supplies the platform's exact steps — real meeting joins,
platform-specific SDK behavior, auth and join flows, waiting-room
handling, meeting-bot patterns — one platform folder at a time. It
doesn't decide to build a Zoom integration; it follows the steps for one
already decided. That correction ("design" → "follow steps for") is the
wrong-guess pedagogy per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-meeting-sdk-app/beat_sheet.json`,
the source's own SKILL.md path not present on this machine — the source's
own `beats[*].narration_text` served as the locked script, same as
several `financial-services--*` siblings): a skill is a folder Claude
reads before it works, containing `RUNBOOK.md` and `SKILL.md` plus one
subfolder per platform — android, electron, ios, linux, macos,
react-native (8 files total); the instructions run as steps, in order —
read the SKILL.md, execute each step, return the result — linear, no
branching unless a step says so; this specific skill is a reference for
Zoom's Meeting SDK, used after routing to a meeting-embed workflow, for
real meeting joins, platform-specific SDK behavior, auth/join flows,
waiting-room issues, or meeting-bot patterns; it gets repeatable results
right and bites on anything outside the spec; same input produces the
same output every run; the skill only handles what its file specifies.
