# Claude, Irac Practice.

Someone asked whether practicing IRAC with Claude means Claude hands you the
finished answer. It doesn't — it walks you through the steps. The
`irac-practice` skill is a folder Claude reads before it acts: one file,
SKILL.md, holds the whole instruction set for drilling IRAC, written in
plain language, no hidden logic. Claude reads it, then works through its
Steps in order — pose the hypo, wait for your Issue, your Rule, your
Application, in that order. One check inside it is specific: stating the
right Conclusion without showing the Application earns nothing — the
Application is where the Rule actually meets the facts, one fact at a
time. A Conclusion that skips it is a guess wearing the right answer.
Claude isn't grading your Conclusion — it's checking whether you showed
the Application, one fact at a time, on the way to it.

**Topic:** IRAC-PRACTICE · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-for-legal--claude-liam-irac-practice

---

## Chapters

0:00 The naive framing: "does Claude give me the answer?" — corrected on screen to "the steps"
0:10 A Skill is a folder — one file, SKILL.md, holds the instructions
0:24 Pose, pause, check — a linear pipeline, no skipping ahead
0:36 The specific check: Conclusion, or Application
0:50 Carry-out
0:56 Your turn
1:10 Outro

---

## YOUR TURN

Paste this into Claude:

> Give me a short fact pattern, one paragraph. Read the irac-practice
> skill, and don't give me the answer — ask me for my Issue first, then
> my Rule, then my Application, and only check my Conclusion after I've
> given all three.

Run that today, against a hypo you actually want to practice.

---

## Deliberately not claimed

This reel does not describe the full contents of the `irac-practice`
skill's own SKILL.md — that file lives in a law-student skills collection
not reachable from this build, and the source script this reel redoes
never filled in its skill-specific detail either (its own beat sheet still
carries unfilled `>` placeholders in three spots). Rather than invent a
specific checklist, this reel states one concrete, well-established fact
about IRAC itself that is the actual reason "IRAC practice" is a task
worth having a skill for: the difference between a Conclusion that skipped
the Application and one that earned it. See BUILD-LOG.md for the full
account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
