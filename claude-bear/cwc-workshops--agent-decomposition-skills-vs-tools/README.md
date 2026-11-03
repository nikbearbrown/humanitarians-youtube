# The 402-Line Prompt: How Decomposition Makes Agents 5x Faster

A newcomer's first fix for a slow, expensive agent is to add more — more
tools, more context, more instructions in the system prompt, so it never
misses a case. One measured case shows the opposite: a 402-line prompt with
12 tools took 102 tool calls and 488 seconds to run a daily low-stock sweep,
because every line gets read on every call and every tool gets considered
even when only one applies. The fix isn't less knowledge — it's the same
knowledge split across three levers (tools, skills, subagents) so only the
relevant slice loads per task. Same case, decomposed: 3 scripts, about 100
seconds, same correctness.

This works when the pieces are genuinely separable — a lookup, a policy
check, a template. It flips when the task is one continuous judgment call,
where splitting just adds a boundary to cross.

**Topic:** CLAUDE BASICS · AGENT DECOMPOSITION
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--agent-decomposition-skills-vs-tools

---

## Chapters

0:00 The naive framing: "just add more tools?"
0:11 The wrong guess: add more
0:24 The anchor: 402 lines, 12 tools, low-stock sweep
0:34 Breaking the wrong guess
0:45 Three levers: tools, skills, subagents
1:13 Complexity hides behind the interface
1:29 The one flag
1:40 The anchor returns, decomposed
1:54 Both directions
2:13 Carry-out
2:19 Your turn
2:37 Outro

---

## YOUR TURN

Paste this into Claude: "Here's my agent's system prompt — find the lines
that are decision logic versus the lines that are domain knowledge, split
the knowledge into skills the agent loads on demand, and estimate the token
and latency difference."

Run it on your own agent, and find your split.

---

## Deliberately not claimed

- **Not "always 5x."** The numbers here — five times faster, roughly a
  hundred seconds — are one team's measurement on one workflow, not a
  guaranteed multiplier; how much you gain depends on how cleanly your task
  splits into bounded pieces.
- **No design verdict.** This video states what loading-on-demand buys you
  and stops, rather than judging the three-lever split as correct
  engineering.
- **No invented UI or tool names.** The mechanics are described generically
  (an instruction crossing a boundary) rather than asserting a specific API
  surface Claude exposes today.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AgenticAI #LLM #AIAgents #HumanitariansAI #ProfessorBear

---
