# Check the Spec, Not the Vibe. — The Brand Voice Enforcement Skill

A skill is a folder Claude reads before it works — this one is
brand-voice-enforcement, and its SKILL.md file holds the full instruction
set, in plain language, no hidden logic. The instructions are laid out in a
Steps section: Claude reads each step in order and runs it, linear, no
branching unless a step says otherwise. The actual job is checking a piece
of writing against whatever rules the SKILL.md lists — banned words,
preferred phrasing, tone, whatever it actually says — and flagging anything
that doesn't match. It doesn't know your brand's voice. It checks your
writing against whatever the file lists, same input, same output, every
time — and the limit is exactly what the file says, nothing more.

**Topic:** BRAND VOICE ENFORCEMENT · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-brand-voice-enforcement

---

## Chapters

0:00 The naive framing: "does Claude already know?"
0:09 A skill is a folder
0:23 Steps, in order
0:31 Check, don't guess
0:48 Carry-out
1:00 Your turn
1:19 Outro

---

## YOUR TURN

Paste this into Claude: My brand voice rules are — no contractions, no
exclamation points, always say customers, never users. Check this paragraph
against exactly those three rules and tell me which line breaks which one.
Don't flag anything outside that list.

Run that today, on your own paragraph, not the video's example.

---

## Deliberately not claimed

No claim about the actual rule list the Anthropic brand-voice-enforcement
Skill checks against — the source material this reel was built from never
specified it, and this video doesn't invent one. The three example rules in
the Your Turn prompt (no contractions, no exclamation points, "customers"
not "users") are illustrative for the viewer's own exercise, not a
description of what that specific Skill enforces. No claim about how
thoroughly the check catches subtle tone drift versus explicit word-level
rules — the source doesn't document that distinction.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
