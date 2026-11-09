# Week 10 Summary: HARNESS² — Recursive Agent Harnessing for an Open World

In this paper teardown, we examine **HARNESS²** (*Recursive Agent Harnessing for an Open World*, `arXiv:2610.14224v1`, by Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu, Bhavana Dalvi Mishra, Yifei Ming, Han Yu, Rujun Han, Chen-Yu Lee, and Tomas Pfister at Northwestern University & Google Cloud AI Research).

While an LLM agent's capabilities depend heavily on its **execution harness**—the prompts, guardrails, memory, skills, scripts, subagents, and middleware plugins surrounding a frozen model ($\text{Agent} = \text{Model } \mathcal{M} + \text{Harness } \mathcal{H}$)—evolving harnesses in the open world faces two critical roadblocks:

1. **No Ground-Truth Verifiers**: Open-world tasks arrive unseen at test time without answer keys, unit tests, or reward labels to supervise online edits.
2. **Task-Distribution Drift**: Directly carrying a tailored execution harness from one task to the next introduces noisy regressions when task requirements shift, even though the *refinement process itself* yields highly transferable diagnostic insights.

**HARNESS²** solves both challenges by coupling **Task-Level Recursion** (refining the current task's execution harness $\mathcal{H}$ via a contrastive **Propose–Probe–Compose** step) with **Harnessing-Level Recursion** (updating a continual **improvement harness** $\mathcal{R}_t$ and its indexed `EXPERIENCE.md` library across tasks).

## Video Links

- [9:16 video](https://drive.google.com/file/d/1VBUZb-NMxAoKXNZ0ztnmC0PI_OpbApAM/view?usp=sharing)
- [16:9 video](https://drive.google.com/file/d/1FuHXb5F76U08jhcEM8od00z1rfNBvmts/view?usp=sharing)
---

## Key Architectural & Methodological Contributions

- **File-Level Execution Harness ($\mathcal{H} = (c^1, \dots, c^8)$)**:
  - **Context Construction**: `C1` `systemprompt.md` (always-on persona/procedure), `C2` `guardrails.md` (standing hard constraints), `C3` `LongTermMEMORY.md` (durable domain facts), and `C6` `skills/<n>/SKILL.md` (specialist workflows loaded on demand via the `skill` tool).
  - **Tool Interface**: `C4` `tool_descriptions/tool_guidance.md` (always-on tool instructions) and `C7` `scripts/<name>.py` (deterministic Python helpers invoked via `bash`).
  - **Orchestration**: `C5` `sub_agents/<n>/AGENT.md` (delegated workers running in isolated inference contexts via the `task` tool).
  - **Middleware Control**: `C8` `plugin/<name>.ts` (TypeScript hooks interposed inside the tool loop outside the model's discretion).

- **Task-Level Recursion — Contrastive Propose–Probe–Compose ($\Phi(q_t, \mathcal{H}, \mathcal{E}; \mathcal{R}_t)$)**:
  - **Propose**: After sampling a reference rollout $e^0 \sim \mathcal{A}(q_t; \mathcal{M}, \mathcal{H})$, two scoped editors propose executable candidate harnesses:
    - **Invariant (`INV`) Editor**: Targets cross-domain agentic deficiencies (tool errors, mechanical repetition, missing output verification, runaway loops).
    - **Domain (`DOM`) Editor**: Encodes practitioner knowledge, artifact contracts, source hierarchies, and reconciliation rules.
  - **Probe**: Executes both candidates on $q_t$ under matched configurations and compares trajectories against $e^0$ to extract **behavioral contrasts** without ground-truth labels.
  - **Compose & Scaling ($k$)**: Selectively merges contrast-supported edits into $\mathcal{H}'$. Scales with exploration budget $k$ via **Parallel Recursion** ($k$ base runs, $2k$ candidates, $k$ parallel compositions) or **Sequential Recursion** ($k$ chained contrastive steps), followed by an anonymized blind selector ($\mathcal{H}_t^\star$).

- **Harnessing-Level Recursion — Continual Library Evolution ($\mathcal{R}_{t+1} = \text{Update}(\mathcal{R}_t, \mathcal{H}_t^\star, \mathcal{D}_t)$)**:
  - An **Experience Reflector** audits the full improvement record $\mathcal{D}_t$, labeling each component diff (`helped`, `hurt`, `no observed effect`, or `confounded`) and writing an `EXPERIENCE.md` entry (`cue`, `lesson`, `evidence`, `confidence`) alongside the adopted tree $\mathcal{H}_t^\star$.
  - Every subsequent task starts cleanly from $\mathcal{H}_0$ and selectively reuses or adapts relevant library components.

---

## Headline Empirical Results (Tables 1–3, 6–7)

- **WorkBuddy-Bench (Code, Web, Office)**:
  - **GLM-5 (OpenCode)**: Single contrastive step ($k=1$) jumps **+11.5 points** (`64.2 → 75.7`), surpassing base Gemini 3.5 Flash (`72.4`), and reaches **79.6%** (`+15.4`) with parallel recursion at $k=5$.
  - **Gemini 3.5 Flash (OpenCode)**: Climbs from **72.4%** to **77.5%** ($k=1$) and **80.8%** ($k=5$: Code `80.8%` [+7.4], Web `78.3%` [+8.4], Office `83.4%` [+9.4]) while cutting average execution steps from `25.4` to `21.1`.
- **JobBench (End-to-End Professional Deliverables)**:
  - **Gemini 3.5 Flash (OpenCode)**: Rises from **31.5** to **36.0** (`+4.5` at $k=1$) and **39.0** (`+7.5` at $k=5$).
  - **Case Study (`task1` Producers)**: Adding `guardrails.md`, `SKILL.md`, `tool_guidance.md`, and `scripts/verify_outputs.py` (`check_xlsx`) lifts the task score from **43.1 to 77.8 (+34.7 points)**.
- **Harvey Legal Agent Benchmark (LAB — Partial Pass Rate)**:
  - **GLM-5 (OpenCode)**: Surges **+11.8 percentage points** at $k=1$ (`59.6% → 71.4%`) and **+18.5 pp** at $k=5$ (`78.1%`).
  - **Gemini 3.5 Flash**: Reaches **84.5%** under OpenCode (`79.9% → 81.9% → 84.5%`) and **78.5%** under Codex (`71.6% → 75.6% → 78.5%`).
- **Ablations, Tool Reliability & Self-Improvement**:
  - Removing the library (`-3.1` WB / `-1.8` JB), removing `INV`/`DOM` scoping (`-2.9` WB / `-3.7` JB), or skipping composition (`-1.6` WB / `-1.9` JB) degrades accuracy (Table 3).
  - Removing retained on-demand skills costs **-5.3 points** and removing scripts costs **-3.7 points** on WorkBuddy-Bench (Table 6).
  - Tool-call error rates drop by **37.5%** on WorkBuddy (`0.8% → 0.5%`), **36.8%** on JobBench (`14.4% → 9.1%`), and **20.0%** on LAB (`2.0% → 1.6%`) (Table 7).
  - **Same-Model Executor & Editor ($k=2$)**: All 5 tested models improve themselves, including **Claude Opus 5** (`+3.3` WB, `+5.5` JB, `+3.0` LAB; `72.0 → 100.0` on JobBench Social-Science RAS via `plugin/deliverable_watchdog.ts`) and **GLM-5** (`+13.7` LAB).

---

## Chapters

0:00 - Introduction: HARNESS² & Open-World Recursive Agent Harnessing
0:15 - Why Open-World Harness Evolution Fails Without Contrastive Probes
0:31 - Architecture: 8 Runtime Files (C1–C8) & Coupled Dual-Level Recursion
0:48 - Task-Level Recursion: Scoped Invariant (INV) & Domain (DOM) Probes
1:04 - JobBench Case Study (43.1 → 77.8): verify_outputs.py & Reconciliation Skill
1:21 - Benchmark Results: WorkBuddy-Bench (+11.5), JobBench (+7.5) & Harvey LAB (+11.8 pp)
1:41 - Harnessing-Level Recursion: Why Direct Editing Fails (-10.2) & Library Transfer Wins
1:58 - Component Ablations (Library, Scoping, Skills, Scripts) & Tool-Error Drop (-36.8%)
2:15 - Opus 5 Self-Improvement (72.0 → 100.0): C8 Middleware Plugin (deliverable_watchdog.ts)
2:32 - Practical Harness Engineering Hierarchy: Skills, Scripts, Subagents & Hooks
2:45 - Outro

---

## Paper & References

- **Paper**: Ruiyao Xu et al., *"HARNESS²: Recursive Agent Harnessing for an Open World"*, Northwestern University & Google Cloud AI Research (`arXiv:2610.14224v1`, October 2026)
- **Project & Code**: [GitHub repository](https://github.com/google-research/harness2) · [project site](https://harness2.github.io)
- **Evaluated Harnesses & Benchmarks**: OpenCode (`SST, 2024`), Codex CLI (`OpenAI, 2025`), WorkBuddy-Bench (`Team et al., 2026`), JobBench (`Li et al., 2026`), Harvey Legal Agent Benchmark (`Harvey AI, 2026`)
- **Pipeline Automation**: Built, rendered, and Gate V verified with Swamp (`@hspsat/brutalist-reel` / `week10-reel`)

---
*Created by Hrishikesh for RamanEffect.*
*Tags: #AI #Agents #LLM #RecursiveSelfImprovement #HARNESS2 #GoogleResearch #MachineLearning #SoftwareEngineering #RamanEffect*
