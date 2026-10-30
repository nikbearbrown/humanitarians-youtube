# Week 1: Groundwork, Pi Agent Architecture Deep Dive, and Memory Scoping

> **Project:** RL Environment
> **Reporting Window:** September 21, 2026 – September 27, 2026  
> **Team Focus:** Episodic & Causal Memory Architectures (Kriti Shahi)  
> **Primary Systems Investigated:** Pi Coding Agent (`earendil-works/pi`), arkenOS Runtime, Frozen-Model Memory Scoping

---

## 1. Executive Summary & Engineering Scope

Week 1 established the technical and organizational foundation for the memory architecture research program at Humanitarians AI Inc. Following formal onboarding and the execution of the volunteer agreement, the engineering focus centered on an exhaustive reverse-engineering of the upstream Pi coding agent (`earendil-works/pi`) and reading the memory architectures document.

Pi was selected as the reference research platform due to its minimalist, inspectable, four-package modular design, which eschews opaque monolithic agent frameworks in favor of an explicit event loop. The week's key deliverable was the decomposition of Pi's agent lifecycle—specifically tracing how prompts are compiled, where LLMs are called, how tools are dispatched via a deterministic while-loop, and where context windows are budgeted. This analysis directly informed the initial scoping document for equipping frozen LLM agents with episodic and causal memory subsystems.

---

## 3. Codebase Architecture & File Manifest

### Directory Layout
```text
/Users/kritishahi/Desktop/Humanitarians AI/test/
├── pi-repo/                          # Upstream Pi reference repository (cloned)
│   ├── packages/
│   │   ├── ai/                       # Unified LLM provider interface and streaming
│   │   ├── agent/                    # Core agent loop and state machine
│   │   ├── coding-agent/             # CLI, session persistence, tool implementations
│   │   └── tui/                      # Terminal user interface
├──Initial_Memory_Scoping.docx        # Created document after brainstorming with GPT, Optimus and Claude 
```

---

## 4. Technical Implementation Details & Architectural Insights

### 4.1 The Pi Agent Event Loop
Unlike heavy frameworks that wrap execution in complex Directed Acyclic Graph (DAG) abstractions, Pi structures agentic behavior as a transparent procedural loop:
```text
User Message -> Context Assembly -> LLM Stream -> Tool Calls Emitted?
                      ^                                 |
                      |----------- Tool Results <-------| (loop until final text)
```
Key architectural invariants documented during Week 1:
* **Pre-tool execution hooks:** Pi provides insertion points right before a tool call is executed, making it ideal for intercepting risky actions and injecting memory prompts.
* **Append-only trajectory records:** Every user prompt, tool call, raw tool output, and assistant thought is preserved sequentially, creating high-fidelity raw trajectories for episodic mining.

### 4.2 Experimental Parameter Definition
From research notes established in `Notes.docx`:
* **Context Budget:** Total limit = 128,000 tokens; max task context = 8,192 tokens; fixed memory budget = 1,000 tokens; max scratchpad = 7,192 tokens.
* **Evaluation Seeds:** Pinned to `[42, 137, 2026, 31415, 99999]` to guarantee deterministic multi-run evaluations.

---

## 5. Execution Guide & Reproducibility

### Inspecting Pi Codebase Components
To verify the four core packages in the Pi repository:
```bash
cd pi-repo
npm run build
npm test
```

---

## 6. Generated Deliverables & Output Artifacts

1. **`Pi_Agent_Architecture_Deep_Dive_optimus.pdf`:** Comprehensive reverse-engineering report detailing initialization, LLM calling conventions, tool handling, hooks, and session persistence.
2. **`Initial_Memory_Scoping.docx`:** 5-phase engineering roadmap for evaluating memory systems in frozen coding agents.

---

## 7. Downstream Dependencies & Week 2 Handoff

* **Prerequisites Delivered:** Complete architectural understanding of Pi hooks, context assembly, and trajectory structure.
* **Handoff to Week 2:** Move from static code analysis to **Phase 0 implementation**—pinning the Pi repository, setting up an isolated local environment (`pi_test/iacon_pi/`), configuring model endpoint URLs, and establishing the comparative taxonomy for Episodic and Causal memory architectures.
