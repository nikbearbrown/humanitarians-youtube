# Skill Creator

Is building a Claude skill just writing one good prompt, or does the Skill
Creator run an actual test loop? It runs a five-stage loop — capture intent,
interview and research, write the SKILL.md, test and grade with parallel
with-skill-versus-baseline runs, improve and repeat — plus a separate
description-optimization phase. There's no do-everything prompt; a skill is
proven with a parallel test, and the eval viewer has to reach the human
before the model judges the result itself.

**Topic:** SKILL CREATOR · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-skill-creator

---

## Chapters

0:00 The naive framing: "one good prompt should do it"
0:10 Anatomy — the five-stage loop + description optimization
0:57 The eval loop, verbatim — parallel runs, grading, viewer first
1:46 The mechanism: empirical loop, progressive disclosure, environment limits
2:16 Carry-out
2:31 Your turn
2:53 Outro

---

## YOUR TURN

I want to create a skill that summarizes meeting transcripts into structured
action items. Start from scratch — help me define the skill, write the
SKILL.md, and run the eval loop.

Watch four things: does Claude ask about triggers and output format before
drafting anything? Does it spawn with-skill and baseline runs in the same
turn, not one after the other? Does it generate the eval viewer before it
reads the outputs itself? And afterward, does it offer to run description
optimization?

---

## Deliberately not claimed

No ranking of what the Skill Creator "gets right" or "where it bites" — the
source reel's Teardown-register judgment card is dropped here. The two
environment limits (no subagents on Claude.ai, description optimization
needs the Claude CLI) are stated as fact, straight from the skill's own
specification, not as a verdict on the design.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear #SkillCreator

---
