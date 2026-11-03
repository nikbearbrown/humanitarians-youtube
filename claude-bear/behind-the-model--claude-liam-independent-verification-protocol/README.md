# "Verified" Isn't Evidence — YouTube metadata

**Channel:** @HumanitariansAI
**Playlist:** Behind the Model
**AI disclosure:** This video uses AI-generated narration (Kokoro text-to-speech, voice
"Liam") and AI-assisted animation (Manim, Remotion). No AI-generated video or imagery.

## Title

"Verified" Isn't Evidence — How to Build a Real Verification Protocol with Claude

## Description

When an agent says a task is "verified," that word can mean the agent double-checked its
own reasoning — not that anything independent was actually confirmed. A citation-matching
check that runs on the same process that made the original error can re-confirm a wrong
citation as "verified," because the check never leaves the agent's own say-so. The fix
isn't more scrutiny after the fact — it's naming the evidence artifact before the task
starts: the output type, the independent evidence that would confirm it worked, the
specific check for the likeliest failure, and the artifact that has to exist afterward.
That same four-field structure holds across completely different tasks — a research
summary and a code change get the same shape, with entirely different fills.

From Humanitarians AI: short, plain explanations of how Claude actually works, for a
general audience meeting Claude for the first time. Liam, in for Professor Bear.

In this one: the natural shortcut of asking an agent to re-check its own work; why that
check can't catch its own error; a four-field verification protocol (output type,
independent evidence, key check, required artifact) planted on a research task and paid
off again on a code-change task; and the two-sided limit of any single check — a pass
only proves what it specifically covers, and a different fill on a different task isn't
a verdict on the agent overall.

Try it yourself — the video ends with a paste-ready prompt for building an independent
verification protocol for your own agent workflow.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/behind-the-model--claude-liam-independent-verification-protocol

This is an educational explainer, not sponsored by or affiliated with Anthropic.

## Tags

Claude, Claude AI, Anthropic, agentic AI, AI verification, AI agents, LLM agents, AI
safety, model behavior, AI basics, Humanitarians AI, prompt engineering, AI for
beginners, Claude tutorial

## Chapters (approx., from beat timings)

0:00 Cold open — does "verified" mean true, or checkable?
0:12 The four-field protocol — planted on a research task
0:29 The natural shortcut — ask the agent to check itself
0:40 The break — a self-check can't catch its own error
0:57 Designed before the task starts, not checked after
1:11 A pass only proves what it checks
1:23 The protocol returns — same structure, a code task
1:40 Carry-out
1:47 Your turn
2:07 Outro
