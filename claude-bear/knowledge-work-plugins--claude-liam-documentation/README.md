# Claude, Documentation.

You ask Claude to write a runbook for restarting the payment service. The
natural guess is that it drafts it like a person would — improvising
sections, picking whatever length feels right. It doesn't. `documentation`
is a **skill**: a folder Claude reads before it writes, containing one
file, `SKILL.md`, that recognizes five shapes by name (README, runbook,
onboarding guide, API docs, architecture docs) and the phrases that trigger
each. Ask for that runbook twice and the same three sections — prerequisites,
steps, rollback — come back in the same order, because a file decided them,
not a mood. Ask for something the file doesn't name, and that guarantee
ends: you're back to Claude's general judgment, not the spec's.

**Topic:** DOCUMENTATION · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-documentation

---

## Chapters

0:00 Claude, document this — just write whatever sounds good, right?
0:10 Before it writes, something decides what the document contains
0:17 The guess: freeform draft, improvised sections
0:24 Ask again — same sections, same order, every time
0:32 A skill is a folder: one file, SKILL.md
0:41 Anchor planted — write a runbook for restarting the payment service
0:48 Five shapes the file recognizes
0:54 How the skill works: read, execute, return
1:02 Linear, mostly — branches only when a step says so
1:07 Anchor payoff — same runbook, same shape
1:15 A named shape delivered is real signal
1:21 Outside the list, the guarantee ends
1:30 Carry-out: name the shape, get the shape
1:39 Your turn
1:51 Outro

---

## YOUR TURN

"Before you write this runbook, read the documentation SKILL.md and tell
me exactly what you're about to include — the sections, and the phrase
that triggers this shape. Then write it twice and compare."

Watch two things when Claude answers: does it name the shape and its
sections before writing a word, and does the second draft match the first
— same sections, same order?

---

## Deliberately not claimed

Not a verdict on whether five named shapes is the right scope for a
documentation skill — that's Teardown territory; this reel states the
mechanism and its edges, and stops. Not that every skill works this way —
this reel describes `documentation` specifically, not skills in general.
Not a claim that a document in a named shape is complete or accurate —
only that its shape matches what the file promised.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #Documentation #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
