# Claude, Enrich Lead.

"Lead enrichment" sounds like it needs a near-complete profile already in
hand before Claude can do anything with it. It doesn't. The Anthropic skill
`enrich-lead` is one instruction file — a `SKILL.md`, plain language, no
hidden logic — and its whole job runs off a single identifying detail: a
name, a company, a LinkedIn URL, **or** an email. Drop just one of those
and it hands back a full contact card: email, phone, title, company intel,
next actions. The pipeline lives in a Steps section, read top to bottom,
executed in order. Ask about the same lead twice and you get the same
card both times; ask for something the file doesn't cover, and the skill
has nothing to say about it — it's a specification, not custom code.

**Topic:** CLAUDE BASICS · ENRICH-LEAD SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-enrich-lead

---

## Chapters

0:00 Enrich-lead needs a full PROFILE to start. Right?
0:10 A skill is a folder
0:22 The pipeline
0:30 The interesting constraint
0:51 Carry-out
1:01 Your turn
1:18 Outro

---

## YOUR TURN

"I have a lead — just a first name, nothing else. Read the enrich-lead
skill in this folder and walk me through exactly which steps you'll run,
in order, before you actually run them."

Why it's worth running: it forces Claude to state its own steps before
acting, on the thinnest possible input — the same "explain first" clause
the source reel's own handoff used to surface a skill's real constraint
logic.

---

## Deliberately not claimed

Not "you need a LinkedIn profile to use enrich-lead" — a name, a company,
a LinkedIn URL, or an email each work on their own; the source's "or" is
the operative word. No field added to the contact card beyond what the
source itself names (email, phone, title, company intel, next actions).
No verdict on whether the enrich-lead skill is well designed — that's
Teardown territory; this reel states the one-file, same-input/same-output
mechanism and stops.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
