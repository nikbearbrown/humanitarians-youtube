# Claude, Reorder Policy — A Rule, Not a Judgment Call

You'd guess Claude is weighing this the way a person would — supplier
trust, seasonal demand, gut feel about the market. It isn't. A Claude
skill is a folder Claude reads before it acts, and this one, called
"reorder-policy," has one file inside: `SKILL.md` — plain language, no
hidden logic. Open it and there's no weighing anything: a Steps section,
a numbered list Claude runs top to bottom. No step on that list says
"use your judgment." Claude reads each step in order and runs it — no
branching, unless a step itself says to branch. Feed it the same stock
numbers twice and it hands back the identical recommendation both
times — that repeatability is real. But ask it something the list never
covers, and there's no step left to run. The list only ever does what's
written on it.

**Topic:** CLAUDE SKILLS · ANTHROPIC
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--claude-liam-reorder-policy

---

## Chapters

0:00 The naive framing: "Claude just knows"
0:10 The folder, one file: reorder-policy/SKILL.md
0:21 The wrong guess: a judgment call?
0:33 The anchor: the Steps section, no judgment step
0:46 The mechanism: read, run, next step
0:54 The anchor returns: same input, uncovered case
1:12 Carry-out
1:20 Your turn
1:30 Outro

---

## YOUR TURN

I'm going to hand you a short instruction file with numbered steps in it.
Before you run it, tell me which step you're on and what you'll do next —
before you act on it.

Run that with any short numbered procedure you have on hand — a
checklist, a short doc — not the video's reordering example.

---

## Deliberately not claimed

No claim that Claude never uses judgment anywhere — only that *this
skill's* recommendation comes from running the numbered steps in its
file, not from Claude weighing market factors itself. No verdict on
whether "reorder-policy" is a *well-built* skill: the reel states what
the file contains and what Claude does with it, and stops there. No
claim about what the specific steps compute — the source narration never
specified the business logic beyond "linear, no branching unless the
step says so," and the reel doesn't invent it.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics), including the Remotion writer-performance cold open. No
human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AnthropicSkills #AIExplained #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
