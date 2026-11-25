# Week 1: Groundwork, Memory Types, and Experimental Design (Pi Memory) — script (narration as rendered)

Voice: Kokoro `am_onyx` · Persona: Kriti (voiced by Liam, Kokoro am_onyx)

Narration copied word for word from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

### B00 · cold open
> Hello, this is Kriti, sharing the weekly update on evaluating memory architectures for Pi.

### B01 · overview (BLUF)
> Week one was the groundwork: the team, the tools, the theory, and a first plan for testing memory in Pi.

### B02 · body — onboarding
> First, onboarding. I joined Discord, introduced myself, caught up on past conversations, and got access to ArkenOS to start exploring.

### B03 · body — six memory types
> Then the theory: six kinds of agent memory. Each answers a different question, from how to do something to how sure the agent is.

### B04 · body — Pi architecture
> Next, the Pi architecture: startup, model calls, tool runs, hooks, session storage, config, and context. These are the seams memory plugs into.

### B05 · body — the plan
> The draft plan has five steps: pin one Pi version, build baselines, implement six memory architectures, combine them, and run experiments.

### B06 · body — baselines
> Baselines come first. The same agent with no memory and with memory, so every gain is measured against something.

### B07 · body — benchmarks + budget
> Experiments run on public benchmarks like SWE-bench and LongMemEval, with a token budget capping storage, writes, retrieval, and context.

### B08 · body — scorecard
> And the scorecard: cost, latency, token overhead, grounded factual memory, and memory relevance.

### B09 · verdict
> Week one: onboarded, grounded in the theory, and a plan with controls, budgets, and metrics.

### B10 · your turn handoff
> Your turn: 'Help me design a fair experiment comparing memory architectures for a coding agent. What baseline, budget, and metrics would you use?' The word fair is doing the work: baselines and budgets make the comparison honest.

### B11 · outro
> Pi Memory, Week One. At Nik Bear Brown.
