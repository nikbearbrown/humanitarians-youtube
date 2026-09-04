# Same Data, Same Packet. — The Client-Review Skill (Anthropic Skills)

Does a repeatable, finance-specific Claude capability mean there's a
built-in portfolio analysis app under the hood? No — a Claude skill is a
folder with one file, SKILL.md, written in plain language with no hidden
logic. This one is client-review: it preps a portfolio performance
summary, allocation analysis, talking points, and action items before
quarterly reviews, annual checkups, or ad-hoc client meetings. Claude reads
the file, runs each step in the Steps section in order, and returns the
result — linear, no branching unless a step itself says so. The file
spells out exactly what to produce, so the same account data builds the
same meeting-ready packet every time. Ask for something the file doesn't
cover, and there's no instruction to fall back on — Claude reasons past the
file on its own.

**Topic:** CLIENT REVIEW · CLAUDE SKILLS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-client-review

---

## Chapters

0:00 The naive framing: "does the app analyze the portfolio?"
0:13 A skill is a folder
0:25 Read, execute, return
0:35 Spec it, or Claude reasons past it
1:01 Carry-out
1:13 Your turn
1:31 Outro

---

## YOUR TURN

Paste this into Claude: write a SKILL.md for a recurring meeting you prep
for. List exactly what must appear every time, then list what would be
left to my judgment because the file doesn't cover it.

Read back what Claude wrote — the first list is what repeats identically
every run; the second is where it's reasoning past the file, not following
it.

---

## Deliberately not claimed

No claim about how Claude decides which skill to dispatch among several
candidates — the source Skill doesn't document that mechanism, and this
video doesn't guess. No claim that every Claude skill is structured exactly
like client-review; the read-execute-return pipeline and the plain-language
SKILL.md format are properties of this specific Skill, generalized only as
far as "a skill is a file Claude reads," which the source itself states.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #FinancialServices #LLM #HumanitariansAI #ProfessorBear

---
