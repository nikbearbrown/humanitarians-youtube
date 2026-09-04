# Claude Doesn't Build a New Video App — It Wires In Zoom's SDK

Someone assumes "build a Zoom meeting app" means Claude writes its own
video-calling engine from scratch. It doesn't. It's a scan of one
instruction file — a SKILL.md — that Claude follows to wire Zoom's own
Meeting SDK into an app you already have, for exactly one of four jobs: a
Meeting SDK join, a web or mobile embed, the lifecycle around a meeting,
or the call on when to reach for the Video SDK instead. Ask for anything
outside those four and there's no mode that covers it.

**Topic:** BUILD ZOOM MEETING APP · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-build-zoom-meeting-app

---

## Chapters

0:00 Does Claude write a new video calling system?
0:12 A skill is a folder
0:29 How it runs
0:38 Exactly four situations
0:58 Carry-out
1:10 Your turn
1:27 Outro

---

## YOUR TURN

"I want to add a 'Join Meeting' button to my web app using Zoom's Meeting
SDK. Walk me through the pieces I'd need — the SDK, the meeting lifecycle
events, and when I'd reach for the Video SDK instead — before writing any
code."

That's the whole idea: Claude wires in Zoom's own SDK for whichever of
four fixed jobs fits — it never invents the video-calling engine itself.

---

## Deliberately not claimed

This reel never claims Claude writes its own video-calling engine —
every beat keeps the boundary that Claude wires Zoom's own Meeting SDK
(or Video SDK) into an app that already exists. It also isn't a claim
that this replaces a developer's own Zoom API account or setup: the
boundary (only what the instruction file specifies gets covered) is
stated as fact, not argued with.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AIagents #AgenticAI #ZoomAPI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
