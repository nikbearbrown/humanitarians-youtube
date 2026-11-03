# Claude Doesn't Join Your Zoom Calls — It Builds the Bot

Someone assumes "build a Zoom bot" means Claude itself dials in and sits
on your calls. It doesn't. It's a scan of one instruction file — a
SKILL.md — that Claude follows to assemble exactly one of three things: a
meeting bot that joins a call, a recorder that captures the session, or a
real-time media workflow that processes audio and video as it happens.
Each is built from the same three pieces: Zoom's Meeting SDK, its
real-time media streams (RTMS), and your own backend. Ask for anything
outside those three and there's no mode that covers it.

**Topic:** BUILD ZOOM BOT · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-build-zoom-bot

---

## Chapters

0:00 Can Claude be my Zoom meeting bot?
0:11 A skill is a folder
0:28 How it runs
0:37 Exactly three build targets
0:59 Carry-out
1:11 Your turn
1:26 Outro

---

## YOUR TURN

"I want to build a Zoom bot that joins a call and saves the transcript.
Walk me through the pieces I'd need — the Meeting SDK, real-time media
streams, and my own backend — before writing any code."

That's the whole idea: Claude builds the bot, in whichever of three fixed
shapes fits the job — it never joins the call itself.

---

## Deliberately not claimed

This reel never claims Claude itself dials into or attends a live Zoom
call — every beat keeps the boundary that Claude writes and assembles the
bot's code, which you then run. It also isn't a claim that this replaces
a developer's own Zoom API setup: the boundary (only what the instruction
file specifies gets built) is stated as fact, not argued with.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AIagents #AgenticAI #ZoomAPI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
