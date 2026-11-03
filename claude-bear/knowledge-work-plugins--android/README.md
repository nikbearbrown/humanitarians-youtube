# Does Claude Run Your Contact Center? — The contact-center/android Skill

A skill is a folder Claude reads before it works — this one is
contact-center/android, and its SKILL.md file holds the full instruction
set, in plain language, no hidden logic. The pipeline sits in a Steps
section: Claude reads each step in order, then runs it — linear, no
branching unless a step says so. The scope is specific: contact-center/
android covers the Zoom Contact Center SDK for native Android apps — chat,
video, the virtual agent, scheduled callback integrations, campaign mode,
service lifecycle, and rejoin handling. It doesn't run your contact center.
It writes the Android integration code that connects to one — the same
code, from the same request, every time — and the guarantee holds only for
what the file specifies, nothing outside it.

**Topic:** CLAUDE BASICS · CONTACT-CENTER/ANDROID SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--android

---

## Chapters

0:00 The naive framing: "does Claude run my contact center app?"
0:12 A skill is a folder
0:26 How the skill works — read, execute, return
0:33 The interesting constraint: one SDK, native Android
0:55 Carry-out
1:02 Your turn
1:18 Outro

---

## YOUR TURN

Paste this into Claude: Read the contact-center/android skill in this
folder. Before you run it, tell me exactly which Zoom Contact Center SDK
features it covers and which Android lifecycle pieces it handles. Then help
me wire up one feature in my app.

Run that today, on your own project, not the video's example.

---

## Deliberately not claimed

Not a claim that Claude runs or operates a contact center — the naive
framing in the cold open ("Does Claude RUN my contact center app?") is
stated and corrected in the same beat: the skill is a coding aid that
builds the native Android app talking to Zoom's Contact Center SDK, and
Claude never takes a call itself. No invented "triggers on '...'"
trigger-phrase quote — the source material never gives one for this skill,
so none is fabricated here; the scope statement uses only the SDK feature
areas the source itself names (chat, video, ZVA, scheduled callback,
campaign mode, service lifecycle, rejoin handling). No verdict on the
skill's design — this Plain-register redo describes the scope without
ruling on whether it was well built.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion
graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
