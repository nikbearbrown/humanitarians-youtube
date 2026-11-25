# Weekly hours — Kriti S.

Logged weekly, in the week it happened. Every reported week has 20 hours: 16 on engineering and research, 4 on reporting (progress video, explainer and documentation).

| Week | Project work | Eng. hrs | Topic explainer | Reporting hrs | Total |
|---|---|---|---|---|---|
| 21–27 Sep | [Week 1 — groundwork, memory types, experimental design](2026-09-27-week1-project-update/README.md) | 16 | [Pi agent architecture](2026-09-27-pi-agent-architecture/README.md) | 4 | 20 |
| 28 Sep – 4 Oct | [Week 2 — pinned baseline, persistent logging, six memory designs](2026-10-04-week2-project-update/README.md) | 16 | [Causal memory](2026-10-04-pi-agent-causal-memory/README.md) | 4 | 20 |
| 5–11 Oct | [Week 3 — SQLite WAL store, SWE-rebench evaluation](2026-10-11-week3-project-update/README.md) | 16 | [Contrastive episodic memory](2026-10-11-contrastive-episodic-memory/README.md) | 4 | 20 |
| 12–18 Oct | [Week 4 — subsystem hooks, in-flight backtracking](2026-10-18-week4-project-update/README.md) | 16 | [Counterfactual learning](2026-10-18-mathematical-counterfactual-learning/README.md) | 4 | 20 |
| 19–25 Oct | [Week 5 — clean E1–E7 ablation, leakage audit](2026-10-25-week5-project-update/README.md) | 16 | [Novelty dampening](2026-10-25-novelty-dampening/README.md) | 4 | 20 |
| 26–31 Oct | [Week 6 — Carry the Couch Milestone 1, physics verification](2026-10-31-week-6-project-update/README.md) | 16 | [Deep Sets in MARL](2026-10-31-deep-sets/README.md) | 4 | 20 |
| **To date** | | **96** | | **24** | **120** |

**Eng. hrs** is engineering and research on the memory architectures and multi-agent physics simulations. **Reporting hrs** is the weekly progress report, explainer production and documentation.

Evidence for each week's work (reports, videos, Frictional logs) is in [README.md](README.md).

## Weekly breakdown

### Week 1 · 21–27 Sep

| Activity | Hours | Record / artifact |
|---|---|---|
| Deconstruct Pi agent architecture, event loop, and pre-tool execution hooks | 4 | [Architecture deconstruction](2026-09-27-week1-project-update/README.md#41-the-pi-agent-event-loop) |
| Define experimental parameters, context window limits, and 5-seed evaluation plan | 4 | [Parameter definition](2026-09-27-week1-project-update/README.md#42-experimental-parameter-definition) |
| Draft initial memory scoping and 5-phase engineering roadmap for frozen LLMs | 4 | [Memory scoping roadmap](2026-09-27-week1-project-update/README.md#6-generated-deliverables--output-artifacts) |
| Inspect Pi codebase packages (`ai`, `agent`, `coding-agent`, `tui`) and verify local build | 4 | [Codebase inspection](2026-09-27-week1-project-update/README.md#3-codebase-architecture--file-manifest) |
| Weekly progress reports and explainer adaptation | 2 | [Progress report & beat sheet](2026-09-27-week1-project-update/beat_sheet.json) |
| Organize links and documentation | 2 | [Evidence index](2026-09-27-week1-project-update/README.md) |
| **Total** | **20** | **16 engineering + 4 reporting hours** |

### Week 2 · 28 Sep – 4 Oct

| Activity | Hours | Record / artifact |
|---|---|---|
| Establish Phase 0 isolated environment and permanent logging sandbox under `pi_test/iacon_pi/` | 4 | [Phase 0 Sandbox](2026-10-04-week2-project-update/README.md#1-executive-summary--engineering-scope) · [Module Manifest](2026-10-04-week2-project-update/README.md#3-codebase-architecture--file-manifest) |
| Formalize 6-paradigm cognitive memory taxonomy and comparative dimensions against Pi baseline | 4 | [Comparative Architecture](2026-10-04-week2-project-update/README.md#41-pi-baseline-vs-proposed-memory-architectures) · [Master Document](2026-10-04-week2-project-update/Episodic%20and%20Causal%20Memory%20Architectures.docx) |
| Scope 3 Episodic Memory designs: Contrastive Pairs ($\tau^+/\tau^-$), Subtask Milestone DAGs, and Closed-Loop Retrieval | 4 | [Episodic Architecture](2026-10-04-week2-project-update/README.md#41-pi-baseline-vs-proposed-memory-architectures) · [Episodic Spec](2026-10-04-week2-project-update/Episodic%20and%20Causal%20Memory%20Architectures.docx) |
| Scope 3 Causal Memory designs: SCM Dependency Graphs, Interventional Pruning ($P(Y \mid do(X))$), and Failure-Repair Graphs | 4 | [Causal Architecture](2026-10-04-week2-project-update/README.md#41-pi-baseline-vs-proposed-memory-architectures) · [Causal Spec](2026-10-04-week2-project-update/Episodic%20and%20Causal%20Memory%20Architectures.docx) |
| Weekly progress reports and explainer adaptation | 2 | [Progress report & beat sheet](2026-10-04-week2-project-update/beat_sheet.json)  |
| Organize links, evidence indexing, and documentation | 2 | [Evidence index](2026-10-04-week2-project-update/README.md) · [Deliverables](2026-10-04-week2-project-update/README.md#6-generated-deliverables--output-artifacts) |
| **Total** | **20** | **16 engineering + 4 reporting hours** |


### Week 3 · 5–11 Oct

| Activity | Hours | Record / artifact |
|---|---|---|
| Build and validate deterministic algorithmic Python test harness across 5 pinned seeds | 4 | [Deterministic harness](2026-10-11-week3-project-update/README.md#1-executive-summary--engineering-scope) |
| Implement high-performance SQLite WAL memory store with transactional CRUD and conflict pruning | 4 | [SQLite WAL memory store](2026-10-11-week3-project-update/README.md#1-executive-summary--engineering-scope) |
| Ingest Nebius SWE-rebench trajectories and execute 3-arm comparative evaluations | 4 | [Multi-arm evaluation](2026-10-11-week3-project-update/README.md#41-multi-arm-benchmark-design) |
| Diagnose semantic embedding similarity trap and formulate counterfactual re-architecture | 4 | [Embedding trap analysis](2026-10-11-week3-project-update/README.md#42-benchmark-configuration-matrix) |
| Weekly progress reports and explainer adaptation | 2 | [Progress report & beat sheet](2026-10-11-week3-project-update/beat_sheet.json) |
| Organize links and documentation | 2 | [Evidence index](2026-10-11-week3-project-update/README.md) |
| **Total** | **20** | **16 engineering + 4 reporting hours** |

### Week 4 · 12–18 Oct

| Activity | Hours | Record / artifact |
|---|---|---|
| Mathematical formalization of counterfactual divergence and pivot step ($k^*$) | 4 | [Mathematical formulation](2026-10-18-week4-project-update/README.md#1-executive-summary--engineering-scope) |
| Implement Pi subsystem lifecycle hooks and in-flight backtrack buffers | 4 | [Subsystem hooks](2026-10-18-week4-project-update/README.md#41-in-flight-step--backtrack-tracking-architecture) |
| Develop true online autonomous harvesting of divergent pivot steps | 4 | [Autonomous harvesting](2026-10-18-week4-project-update/README.md#1-executive-summary--engineering-scope) |
| Ingest 40 OpenHands trajectories and run 3-arm benchmark in swe-rigrous-eval | 4 | [Benchmark suite](2026-10-18-week4-project-update/README.md#43-the-40-trajectory-benchmark-suite-matrix) |
| Weekly progress reports and explainer adaptation | 2 | [Progress report & beat sheet](2026-10-18-week4-project-update/beat_sheet.json) |
| Organize links and documentation | 2 | [Evidence index](2026-10-18-week4-project-update/README.md) |
| **Total** | **20** | **16 engineering + 4 reporting hours** |

### Week 5 · 19–25 Oct

| Activity | Hours | Record / artifact |
|---|---|---|
| Investigate evaluation leakage and implement ground-truth isolation | 4 | [Leakage audit](2026-10-25-week5-project-update/README.md#1-executive-summary--engineering-scope) |
| Design 5-phase applicability filtering and novelty dampening mechanism | 4 | [Phase architecture](2026-10-25-week5-project-update/README.md#42-execution-phase-retrieval-matrix) |
| Execute and evaluate clean E1–E7 ablation matrix (N=200 tasks) | 5 | [Ablation matrix](2026-10-25-week5-project-update/README.md#41-the-e1e7-clean-ablation-matrix--experimental-analysis) |
| Formalize McNemar's paired test and compute statistical significance | 3 | [Statistical protocol](2026-10-25-week5-project-update/README.md#44-statistical-significance-protocol-mcnemars-paired-test) |
| Weekly progress reports and explainer adaptation | 2 | [Progress report & beat sheet](2026-10-25-week5-project-update/beat_sheet.json) |
| Organize links and documentation | 2 | [Evidence index](2026-10-25-week5-project-update/README.md) |
| **Total** | **20** | **16 engineering + 4 reporting hours** |

### Week 6 · 26–31 Oct

| Activity | Hours | Record / artifact |
|---|---|---|
| Implement 2D multi-body planar physics in VMAS (`src/env/couch_transport.py`) | 4 | [Simulation physics](2026-10-31-week-6-project-update/README.md#41-simulation-architecture--physical-mechanics) |
| Integrate Deep Sets pooling and private stochastic symmetry-breaking noise | 4 | [Coordination architecture](2026-10-31-week-6-project-update/README.md#observation-space-24d) |
| Author unit test suite (Tests 1–6) including coupled differential thrust/rotation | 4 | [Verification suite](2026-10-31-week-6-project-update/README.md#43-verification-suite--test-results) |
| Design 6-category action taxonomy and integrate `ActionTracker` bout metrics | 4 | [Action diagnostics](2026-10-31-week-6-project-update/README.md#actiontracker-diagnostics) |
| Weekly progress reports and Deep Sets explainer adaptation | 2 | [Progress report & beat sheet](2026-10-31-week-6-project-update/beat_sheet.json) |
| Organize links and documentation (`PROJECT_PLAN`, `Phases`, `Self_Notes`) | 2 | [Evidence index](2026-10-31-week-6-project-update/README.md) |
| **Total** | **20** | **16 engineering + 4 reporting hours** |
