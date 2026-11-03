# Fan Out: Coordinating Dozens of Agents in Parallel Without Blocking

You might picture fifty separate chats, each running its own analyst, all
somehow going at once. That's not how it works. One agent calls a single
custom tool — dispatch analysts — and the server intercepts that call. It
spawns independent analyst sessions, each with its own full context window,
each running in parallel, while the head agent waits without blocking your
terminal. When all the sessions finish, the server resumes the head with
the accumulated results. Watch it work on a concrete example: sweep NVDA,
AMD, and MU, rank by margin durability — three sessions spawn, each reads
filings independently, and the head synthesizes one ranked report from the
results. The payoff scales: fifty analysts run serially take twenty-five
minutes; fanned out in parallel, they finish in about the time the slowest
one takes — roughly thirty seconds. None of it works without a fixed
contract on both sides — a schema in, a schema out — so one broken session
gets rejected cleanly instead of corrupting the merged report.

**Topic:** CLAUDE MANAGED AGENTS · ORCHESTRATION
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--dispatch-analysts-parallel-orchestration

---

## Chapters

0:00 The naive framing: "fifty separate conversations"
0:11 The question: coordinate dozens without blocking
0:21 The wrong guess: three chats, copied by hand
0:30 The mechanism: a custom tool the server intercepts
0:52 The anchor: NVDA, AMD, MU — one flow
1:29 The mechanism: isolated sessions, server as coordinator
1:43 The anchor returns: fifty analysts, 25 minutes to 30 seconds
2:02 Fan-in: the aggregator deduplicates, ranks, merges
2:22 Both directions: the schema contract, kept and skipped
2:43 Carry-out
2:51 Your turn
3:05 Outro

---

## YOUR TURN

Fan this workload out across parallel sub-agents, then merge their results
into one ranked decision.

Run that on any workload with independent sub-tasks — research questions,
files to summarize, options to compare — not just the SEC-filing example in
the video. Watch what happens if one sub-task fails, and whether the merge
waits for the slowest session before it hands back an answer.

---

## Deliberately not claimed

No claim that parallel fan-out always finishes in exactly thirty seconds —
that number is this video's worked example, not a fixed constant; the real
claim is that wall-clock time collapses to roughly the slowest single
session, not the sum of all of them. No verdict on whether this specific
tool-intercept pattern is a *well-engineered* way to orchestrate agents —
the video states what the schema contract does and what happens without
it, and stops there. No claim that every parallel-agent setup uses this
exact mechanism — this is one worked pattern (custom tool → server
intercept → spawned sessions → aggregator), not the only way to
parallelize agents.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics), including the Remotion writer-performance cold open. No
human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeAgents #AgentOrchestration #AIExplained #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
