# Review, Not Repair. — The Accessibility Review Skill

A skill is a folder Claude reads before it works — this one, a single
SKILL.md file, about four kilobytes, plain language, no hidden logic.
Its job, word for word: run a WCAG 2.1 AA accessibility audit on a design
or page. It triggers on requests like auditing accessibility, checking
a11y, or asking if a design is accessible — or before handing off work
that touches color contrast, keyboard navigation, touch target size, or
screen reader behavior. Once triggered, Claude reads the Steps section and
runs them in order. That's an audit, not a repair: the skill checks a
design against WCAG 2.1 AA and reports exactly where it fails — the same
way every time — but it never rewrites the design to fix what it finds,
and anything outside that standard is outside what it sees.

**Topic:** ACCESSIBILITY REVIEW · KNOWLEDGE WORK PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-accessibility-review

---

## Chapters

0:00 The naive framing: "will Claude fix my design?"
0:11 A folder, not a program
0:27 How it gets picked up
0:50 An audit, not a repair
1:10 Carry-out
1:20 Your turn
1:36 Outro

---

## YOUR TURN

Paste this into Claude: I want to audit a design for accessibility — read
the accessibility-review skill and walk me through what you will do before
you do it. That clause matters: having Claude explain itself first, before
it acts, is how you actually see the instructions it's following, not just
the result.

Run that today, on a design you're actually working on, not the video's
example.

---

## Deliberately not claimed

No claim about how Claude's underlying dispatch mechanism matches a
request against a description (pattern-match vs. model judgment) — the
source Skill's SKILL.md doesn't document that internal mechanism, and this
video doesn't guess. No claim about what the audit's WCAG 2.1 AA checks
cover beyond the four criteria the source names (color contrast, keyboard
navigation, touch target size, screen reader behavior) — those are the
named triggers, not asserted as the full checklist.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #Accessibility #WCAG #LLM #HumanitariansAI #ProfessorBear

---
