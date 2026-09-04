# Claude, Earnings Analysis — What One Skill File Actually Does

Does Claude need to be trained to do earnings analysis? No — it needs
briefing. A Claude skill is a folder Claude reads before it acts: this one
is called earnings-analysis, and its SKILL.md holds plain-language
instructions, no hidden code. The instructions live in a Steps section
Claude reads and executes in order — linear, no branching unless a step
calls for it. This particular skill has one job: turn a company's
quarterly numbers into a written earnings update — eight to twelve pages,
a few summary tables, several charts. That's the whole brief; anything
outside it isn't part of what the file does. A skill doesn't make Claude
smarter — it gives Claude one job, done the same way, every time.

**Topic:** EARNINGS-ANALYSIS · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-earnings-analysis

---

## Chapters

0:00 The naive framing: "does Claude need to be trained?"
0:10 A skill is a folder
0:21 Read, then execute
0:29 One job, stated plainly
0:44 Carry-out
0:52 Your turn
1:12 Outro

---

## YOUR TURN

Paste this into Claude: "I want a professional equity-research earnings
update — eight to twelve pages, three to five thousand words, covering
beat-or-miss, updated estimates, and the revised thesis. Read the
earnings-analysis skill first, and walk me through what you'll do before
you do it."

That clause matters — asking Claude to explain its plan before running it
surfaces the real constraints the skill file sets. Run it today on any
skill you have installed.

---

## Deliberately not claimed

No claim about whether earnings-analysis (or any specific skill) ships by
default with a given Claude plan — the video describes the general
mechanism (a folder, a SKILL.md, a Steps section) that any Claude Agent
Skill follows, not a promise about availability. No claim about report
quality or accuracy of any output the skill produces, since that depends
on the data supplied at run time, not the file's structure. The page/word/
table/chart figures (8-12 pages, 3,000-5,000 words, 1-3 tables, 8-12
charts) are this specific skill's stated scope, not a general property of
Claude skills.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudeCode #AnthropicSkills #LLM #HumanitariansAI #ProfessorBear

---
