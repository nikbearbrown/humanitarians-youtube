# Claude, Meeting SDK/Linux.

A Zoom meeting bot sounds like it needs a screen somewhere — a window a
person could watch it work in. It doesn't. The Anthropic skill
`meeting-sdk/linux` is one instruction file — a `SKILL.md`, plain
language, no hidden logic — that specifies a C++ bot connecting to Zoom
through the Meeting SDK, running **headless**, on a Linux **server**: no
window, nobody watching. From there it has raw access to the call's audio
and video, enough to transcribe it, record it, and hand any of that to
further AI steps — server-side automation, start to finish. The pipeline
lives in a Steps section, read top to bottom, executed in order. Same
input, same behavior, every run; ask for something the file doesn't
cover, and the skill has nothing to say about it — it's a specification,
not custom code.

**Topic:** CLAUDE BASICS · MEETING-SDK/LINUX SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--linux

---

## Chapters

0:00 meeting-sdk/linux needs a SCREEN to run the bot on. Right?
0:10 A skill is a folder
0:23 The pipeline
0:31 The interesting constraint
0:51 Carry-out
1:01 Your turn
1:19 Outro

---

## YOUR TURN

"I want a Zoom meeting bot running headless on Linux. Read the
meeting-sdk/linux skill in this folder and walk me through exactly which
steps you'd run, in order, before you run any of them."

Why it's worth running: it forces Claude to state its own steps before
acting, on a request that only makes sense headless — the same "explain
first" clause the source reel's own handoff used to surface a skill's
real constraint logic.

---

## Deliberately not claimed

Not "the bot has no video access" — raw audio/video access,
transcription, and recording are all real, stated capabilities; what's
corrected is the *screen* a newcomer assumes the bot needs, not the
audio/video access itself. No field added beyond what the source names:
C++, headless, Linux server, raw audio/video access, transcription,
recording, AI integration, server-side automation. No verdict on whether
the meeting-sdk/linux skill is well designed — that's Teardown territory;
this reel states the headless/server-side, same-input/same-output
mechanism and stops.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
