# The File Is The Program. — The Client-Report Skill (Anthropic Skills)

Does a repeatable, finance-specific Claude capability mean there's a
built-in finance app under the hood? No — a Claude skill is a folder with
one file, SKILL.md, written in plain language with no hidden code. This one
is client-report: it generates client-facing performance reports with
portfolio returns, an allocation breakdown, and market commentary. Claude
reads the file, runs each step in the Steps section in order, and returns
the result — linear, no branching unless a step itself says so. The file
spells out exactly what to produce, so the same input builds the same
report every time. Ask for something the file doesn't cover, and there's no
instruction to fall back on — Claude reasons past the file on its own.

**Topic:** CLIENT REPORT · CLAUDE SKILLS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-client-report

---

## Chapters

0:00 The naive framing: "does the app understand finance?"
0:12 A skill is a folder
0:28 Read, execute, return
0:42 Spec it, or Claude reasons past it
1:06 Carry-out
1:17 Your turn
1:35 Outro

---

## YOUR TURN

Paste this into Claude: write a SKILL.md for a report I create regularly.
List exactly what must appear every time, then list what would be left to
my judgment because the file doesn't cover it.

Read back what Claude wrote — the first list is what repeats identically
every run; the second is where it's reasoning past the file, not following
it.

---

## Deliberately not claimed

No claim about how Claude decides which skill to dispatch among several
candidates — the source Skill doesn't document that mechanism, and this
video doesn't guess. No claim that every Claude skill is structured exactly
like client-report; the read-execute-return pipeline and the plain-language
SKILL.md format are properties of this specific Skill, generalized only as
far as "a skill is a file Claude reads," which the source itself states.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #FinancialServices #LLM #HumanitariansAI #ProfessorBear

---
