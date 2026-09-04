# Runs the Steps. Doesn't Write the CIM.

Ask Claude to build a Confidential Information Memorandum and it's tempting
to picture it drafting the deal story itself — the way a banker would.
That's not what's happening. Anthropic's `cim-builder` skill is a folder
Claude reads before it works: the SKILL.md inside is the full instruction
set, in plain language, with no hidden logic. The instructions live in a
Steps section, and Claude reads each step in order and runs it — linear,
one after another, unless a step itself says to branch. The skill's job is
specific: structure and draft a CIM for a sell-side deal, organizing
company information into one investor-ready document with consistent
formatting and a narrative that holds together, the same way on every run.
What isn't in the SKILL.md's steps isn't part of the job. cim-builder
doesn't write your CIM — it runs the file's fixed steps on it, the same
way every time.

**Topic:** CIM-BUILDER · FINANCIAL SERVICES SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-cim-builder

---

## Chapters

0:00 The naive framing: "does it write my CIM?"
0:10 A skill is a folder
0:23 One step at a time
0:32 Structure, every time
0:49 Carry-out
0:56 Your turn
1:14 Outro

---

## YOUR TURN

Paste this into Claude: "I want to structure and draft a confidential
information memorandum for a sell-side M&A process. Read the cim-builder
skill and walk me through what you will do before you do it."

That last clause matters — asking Claude to explain first surfaces the
actual steps it's about to run, before it runs them.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-cim-builder`) in the Plain register for a general audience.
The underlying facts are unchanged from the source: the skill structures
and drafts a CIM by executing a fixed set of steps from its SKILL.md — it
does not exercise independent judgment about deal content, invent
information not given to it, or decide what belongs in the document beyond
what the steps specify. This script makes no claim about any specific
deal, company, or CIM beyond the general mechanism (a written procedure
Claude reads and executes) and its one stated limit (only what the file
says).

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #FinTech #MandA #InvestmentBanking #AIagents #HumanitariansAI #ProfessorBear #ClaudeBasics

---
