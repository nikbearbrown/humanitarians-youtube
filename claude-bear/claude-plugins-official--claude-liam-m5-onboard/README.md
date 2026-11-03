# The One Step No Script Can Skip. — The m5-onboard Skill (Claude Code Plugins)

A Claude Code skill can run an M5Stack ESP32 board's entire cold-start
provisioning — detect, identify, flash, install — through one command:
`onboard.py --apps buddy`. Detect finds the board over USB and confirms the
chip. Identify checks hardware signatures for a likely firmware variant, but
the final choice is always stated explicitly, never guessed — two boards
share the exact same USB signature, so getting it wrong boot-loops the
device. The run takes two to three minutes, so it goes in the background
with its output streamed to a log file. And the flash step itself has one
exception baked in: on boards that connect over native USB, there's no
software line the script can pulse to force a reset, so a person has to
hold one button, tap reset while still holding it, hold a beat longer, then
let go. That physical step isn't universal — boards that connect through a
separate USB-to-serial bridge get the same software reset working normally,
and the whole flash step runs through hands-off.

**Topic:** M5-ONBOARD · CLAUDE CODE PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-m5-onboard

---

## Chapters

0:00 The naive framing: "zero exceptions?"
0:11 One command, four stages
0:47 The button dance
1:22 Native USB vs. bridge
1:51 Carry-out
2:01 Your turn
2:20 Outro

---

## YOUR TURN

Paste this into Claude: I'm using the m5-onboard skill to set up a new
M5Stack board. Before you run anything, tell me exactly which stage needs
me to physically touch the device, and what that button sequence actually
is.

Then watch: does Claude name the button dance before it starts, or does it
just launch the script and wait?

---

## Deliberately not claimed

No claim that every ESP32 board or every Claude Code onboarding skill works
this way — the four-stage pipeline, the variant ambiguity, the background
run pattern, and the native-USB button dance are all specific to this one
Skill's documented build. No claim about the buried gotchas the source
teardown also names (an NVS write-mode boot-loop bug, an opaque Bluetooth
error code, platform-specific permission and PATH quirks) — this video
keeps the single most generally teachable fact from that list and drops the
rest as assuming hands-on ESP32 debugging experience this channel's general
audience doesn't have, not as a verdict on the skill's quality.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
