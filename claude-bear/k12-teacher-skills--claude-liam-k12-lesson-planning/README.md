# Claude, K12 Lesson Planning. — The K12 Lesson Planning Skill

When Claude plans a lesson, it isn't improvising in the moment — it's
reading a Skill. A Skill is a folder with one instruction file, SKILL.md,
written in plain language: no hidden logic, no freeform judgment. Claude
reads it, then executes each step in order — read the file, execute the
steps, return the result — linear, no branching unless a step says
otherwise. This particular skill isn't only prose: alongside SKILL.md, the
folder ships a references folder and a scripts folder — supporting
material and runnable code the skill uses directly. Where a step can run
as code, it does, so the same step produces the same result, not a
freshly-reasoned answer typed out each time. Claude isn't improvising the
lesson plan. It's following the skill's written steps, the same way every
time — and ask for something those steps don't cover, and you get Claude's
own judgment, not the skill's playbook.

**Topic:** K12-LESSON-PLANNING · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/k12-teacher-skills--claude-liam-k12-lesson-planning

---

## Chapters

0:00 The naive framing: "does Claude improvise?"
0:11 A Skill is a folder
0:25 Read, execute, return
0:37 Not only prose
0:56 Carry-out
1:09 Your turn
1:23 Outro

---

## YOUR TURN

Paste this into Claude: I teach a seventh grade science class and need a
full lesson plan on the water cycle. Read the k12-lesson-planning skill,
and before you build anything, walk me through the steps you'll follow and
what you'll hand back.

Run that today, on your own class and your own topic, not the video's
example.

---

## Deliberately not claimed

No claim about what any specific lesson plan's content will say — the
mechanism (a named folder, one instruction file, a linear pipeline,
reference material and scripts alongside the prose) holds regardless of
subject or grade level. No claim that Claude replaces a teacher's own
judgment about what the lesson should contain; the video states the
opposite throughout — Claude follows the file, and the file is the limit.
The source skill's own SKILL.md was not available to re-verify while
building this video (see BUILD-LOG.md); every specific claim here is drawn
either from the locked source script's own file listing or from how Claude
Skills work generically, never invented.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudeForEducation #K12 #LLM #HumanitariansAI #ProfessorBear

---
