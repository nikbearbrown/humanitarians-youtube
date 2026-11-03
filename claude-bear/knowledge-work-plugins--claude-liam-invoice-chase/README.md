# Steps, Not Guesses. — The Invoice-Chase Skill

A Skill is a folder Claude reads before it acts. This one is invoice-chase —
the SKILL.md inside it holds the whole instruction set, plain language, no
hidden code. Claude reads the file, then works through its steps in order:
read, execute, return the result — no branching unless the file says so.
Here's the constraint worth knowing: since the file is the whole program,
Claude can only do what its steps say. Same input, same output, every run —
repeatable. But if a situation doesn't match any step in the file, Claude has
nothing else to reach for. The limit is exactly what the file specifies,
nothing more.

**Topic:** INVOICE-CHASE · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-invoice-chase

---

## Chapters

0:00 The naive framing: "does Claude guess?"
0:11 SKILL.md is the program
0:24 Read, then execute
0:40 The limit is the file
0:57 Carry-out
1:06 Your turn
1:21 Outro

---

## YOUR TURN

Paste this into Claude: I run an invoice-chase process for late-paying
clients. Write me a SKILL.md that spells out the exact steps — no
improvising. Then walk me through what you'll do, before you do it.

That clause matters: explaining first shows you the actual procedure a
Skill runs, not a guess about one.

---

## Deliberately not claimed

This video does not reconstruct the literal step list inside the real
Anthropic `invoice-chase` Skill's own SKILL.md — that file wasn't available
to this production. What's shown instead is the shape every Claude Skill
shares: a folder, a SKILL.md instruction set, steps executed in order, same
input to same output. No specific due-date thresholds, reminder cadence, or
messaging policy is claimed for `invoice-chase` specifically.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
