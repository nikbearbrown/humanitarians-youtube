# Claude, Customer Research. — What a "Skill" Actually Does

A skill isn't a new power Claude has — it's a written set of steps. The
`customer-research` Anthropic skill is one file, SKILL.md, that tells
Claude how to turn a customer question into multi-source, attributed
findings. Claude reads the file, runs the steps in order — pull sources,
attribute them, hand back findings — and does that the same way every
time. Ask it to skip the sources and just guess, and there's no
instruction for that; the skill only does what its steps describe.

**Topic:** CUSTOMER-RESEARCH · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-customer-research

---

## Chapters

0:00 The naive framing: "Claude already knows my customer"
0:09 A skill is a folder
0:24 Read, execute, return
0:34 Same every run, not everything
0:49 Carry-out
1:00 Your turn
1:19 Outro

---

## YOUR TURN

Paste this into Claude: "Read the customer-research skill and walk me
through what you're about to do before you do it. Then use it on this:
[paste the customer's question here] — research it across the sources
I've given you, and attribute what you find." That first line matters —
watching Claude explain the plan before it runs shows you exactly which
step in the skill is doing the work.

---

## Deliberately not claimed

No claim that Claude has any built-in memory or knowledge of your
customers — `customer-research` only looks up and attributes the sources
you give it. No verdict on whether a fixed-steps design is the right
trade-off for this task; that's a design judgment, and this video states
the underlying behavioral fact (consistent output, uncovered requests
aren't improvised around) without ruling on it.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #CustomerResearch #LLM #HumanitariansAI #ProfessorBear

---
