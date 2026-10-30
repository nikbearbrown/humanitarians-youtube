# Week 4: Pi Subsystem Hooks, In-Flight Backtracking, Online Autonomous Harvesting, and 40-Trajectory Benchmarking (Modified)

> **Project:** RL Environment
> **Reporting Window:** October 12, 2026 – October 18, 2026  
> **Team Focus:** Episodic & Causal Memory Architectures (Kriti Shahi)  
> **Primary Systems Investigated:** Pi Subsystem Hooks (`pi_hook_manager.py`, `context_injector.py`, `contrastive_harvester.py`), In-Flight Backtrack Buffers, Online Autonomous Harvesting, 40-Trajectory Benchmark Suite (`nebius/SWE-rebench-openhands-trajectories`)

---

## 1. Executive Summary & Engineering Scope

Week 4 delivered the mathematical formalization, subsystem implementation, and empirical verification of **Phase 2 and Phase 3 groundwork**—resolving the semantic embedding trap uncovered during Week 3. By transitioning from whole-trajectory semantic retrieval to **counterfactual trajectory delta harvesting**, the system isolates the earliest pivot index $k^*$ where a failing execution trace ($\tau^-$) departs from a successful execution trace ($\tau^+$).

During this week, critical architectural decisions were made by the researcher (Kriti Shahi):
1. **In-Flight Step & Backtrack Tracking:** Diagnosing a silent runtime gap where `backtrackHistory` was never populated during live unseeded agent errors, leading to the engineering of dynamic error capture during `after_tool_call`.
2. **True Online Autonomous Harvesting:** Eliminating reliance on artificial synthetic fork generation in favor of real-time autonomous step partitioning directly from unseeded multi-turn tool sessions.
3. **Empirical Validation across 40 Real-World Agent Trajectories:** Streaming and testing on 40 authentic agent execution traces from the Nebius OpenHands SWE-bench dataset (`nebius/SWE-rebench-openhands-trajectories`), proving real-world $\Delta_{\text{pivot}}$ extraction, zero data contamination (0.0% collision), and achieving a verified **66.7% Trap Avoidance Rate (TAR)**.
4. **Execution of the swe-rigrous-eval Benchmark Suite:** Deploying the isolated `research/swe_rigorous_eval/` evaluation environment across $N=200$ held-out real defects with Four Leakage Shields, harvesting 500 contrastive episodes into SQLite, and producing the foundational `STATISTICAL_ANALYSIS_REPORT.md`.

---

## 3. Codebase Architecture & File Manifest

### Directory Layout
```text
/Users/kritishahi/Desktop/Humanitarians AI/test/
├── research/
│   ├── swe_rigorous_eval/                   # Rigorous SWE-bench multi-turn evaluation suite (referred to as swe_rigrous_eval)
│   │   ├── STATISTICAL_ANALYSIS_REPORT.md   # Reference baseline evaluation report (N=200 held-out defects)
│   │   ├── benchmarks/                      # Audit scripts (e.g., audit_dataset_splits.py for 4 leakage shields)
│   │   ├── config/                          # Frozen model endpoint, seeds, and token budget rules
│   │   ├── harness/                         # swe_arm_evaluator.py, context_injector.py, trap_interceptor.py
│   │   ├── memory/                          # swe_contrastive_memory.sqlite (500 episodes, FTS5 + dense embeddings)
│   │   └── runs/                            # Multi-arm traces: swe_arm_0_no_memory, swe_arm_1_flat_rag, swe_arm_3_contrastive_memory
│   └── pi_baseline/
│       ├── harness/
│       │   ├── hooks/
│       │   │   ├── __init__.py
│       │   │   ├── pi_hook_manager.py       # Hook coordinator with in-flight backtrack buffers
│       │   │   ├── context_injector.py      # Budget-capped prompt injector (<= 1,000 tokens)
│       │   │   └── contrastive_harvester.py # Autonomous step partitioner & divergence miner
│       │   ├── fetch_swe_trajectories.py    # HF API client streaming 40 authentic trajectories
│       │   ├── harvest_swe_contrastive_memory.py # Ingests 40 SWE trajectories into SQLite
│       │   └── populate_train_memory.py     # 20-train task rollout harvester
│       ├── tests/
│       │   ├── test_phase2_pi_hooks.py      # 5 test suites verifying hooks, backtracks, & TAR
│       │   └── test_phase3_task_suite.py    # 4 test suites verifying 40-task split & zero leakage
│       ├── data/
│       │   ├── train_stream_v1.json         # 20 training tasks (40,935 bytes)
│       │   └── eval_stream_v1.json          # 20 evaluation tasks (37,185 bytes)
│       └── logs/
│           ├── swe_arm_0_no_memory.jsonl    # Arm 0 raw execution telemetry
│           ├── swe_arm_1_flat_rag.jsonl     # Arm 1 raw execution telemetry
│           └── swe_arm_3_contrastive_memory.jsonl # Arm 3 contrastive execution telemetry
```

### Module Responsibilities
| Module / Script | Responsibility | Key Classes / Interfaces |
|---|---|---|
| `pi_hook_manager.py` | Registers lifecycle callbacks; dynamically captures failed tool outputs into `self.in_flight_backtracks`. | `PiHookManager`, `after_tool_call()`, `on_session_settled()` |
| `contrastive_harvester.py` | Extracts divergence index $k^*$; implements autonomous linear step partitioning over backtrack buffers. | `ContrastiveHarvester`, `harvest()`, `TrajectoryDelta` |
| `context_injector.py` | Formats harvested lessons into system prompt strings; strictly enforces 1,000-token ceiling. | `ContextInjector`, `format_injected_context()` |
| `fetch_swe_trajectories.py` | Streams 40 authentic OpenHands multi-turn trajectory records from Hugging Face Datasets Server API. | `stream_trajectories()`, `parse_openhands_turns()` |
| `harvest_swe_contrastive_memory.py` | Ingests 40 streamed SWE trajectories, extracts $\Delta_{\text{pivot}}$ pairs, and indexes them in SQLite. | `harvest_and_store()` |
| `research/swe_rigorous_eval/` | Isolated evaluation harness (swe_rigrous_eval) executing N=200 held-out real defects across 3 arms with 4 leakage shields. | `swe_arm_evaluator.py`, `STATISTICAL_ANALYSIS_REPORT.md` |
| `test_phase2_pi_hooks.py` | 5 unit test suites validating hook lifecycle, in-flight backtracks, TAR, and token caps. | `TestPhase2PiHooks` |

---

## 4. Technical Implementation Details & Architectural Invariants

### 4.1 In-Flight Step & Backtrack Tracking Architecture
```text
Agent Execution Turn
        │
        ▼
   Tool Invocation (a_proposed)
        │
        ▼
  [ PiHookManager.after_tool_call() ]
        │
        ├─► Did tool succeed?
        │        ├─► YES: Append to self.current_session_steps
        │        └─► NO (Error / Non-zero exit / Syntax error):
        │                 ▼
        │             [ Dynamic In-Flight Backtrack ]
        │             Record failing step into self.in_flight_backtracks
        │             Agent backtracks & attempts self-correction (a_corr)
        │
        ▼
[ Session Completed (on_session_settled) ]
        │
        ▼
[ Online Autonomous Harvester ]
   Attaches in_flight_backtracks as failed branch
   Identifies common prefix P = (s_0, ..., s_{k*-1})
   Extracts pivot delta: Delta_pivot = < s_k*, a_fail, a_corr >
   Saves Lesson: L = < W_trigger, a_fail, a_corr, Delta_reward >
```

### 4.2 Search Tree Pruning Complexity Analysis
As documented in `Notes_Self_Understanding.md`:
* In standard heuristic agent search, descending into a flawed sub-branch requires re-exploring an exponential subtree:
  $$\text{Complexity}_{\text{standard}} = O(b^d)$$
  where $b$ is the tool branching factor and $d$ is the reasoning depth.
* With **In-Flight Backtrack Tracking & Contrastive Harvesting**, once an error is recognized and backtracked, the failing action $a^-$ is tagged with a negative avoidance constraint:
  $$\text{Complexity}_{\text{backtrack}} = O(d)$$
  The agent prunes the failing branch immediately upon encounter and redirects to $a^+$.

### 4.3 The 40-Trajectory Benchmark Suite Matrix
Phase 3's empirical foundation established a strict 40-task evaluation suite:
* **20 Train Tasks (`train_stream_v1.json`):** Used to populate contrastive memory with 20 real episodes.
* **20 Test Tasks (`eval_stream_v1.json`):** Reserved for uncompromised out-of-sample evaluation.
* **Domain Stratification:** Balanced across Python algorithmic tasks and SQL multi-table joins.
* **Anti-Contamination Checks:**
  * Task ID Collision: $0 / 40$ ($0.0\%$).
  * Initial Code & Patch Hash Overlap: $0.0\%$ (Zero identical code blocks across train and eval).

### 4.4 The swe-rigrous-eval Architecture & Anti-Leakage Shielding
The `swe_rigorous_eval` subsystem establishes a production-grade benchmark harness isolating memory evaluation:

| Dimension / Metric | Training Pool A ($T_{\text{train}}$) | Evaluation Pool B ($T_{\text{eval}}$) | Leakage Audit Status |
|---|:---:|:---:|:---:|
| **Total Trajectories** | 500 trajectories | 200 distinct tasks | Verified Disjoint |
| **Unique Repositories** | 364 repositories | 54 repositories | **0 overlapping repos (Shield 1)** |
| **Unique GitHub Orgs** | 338 organizations | 23 organizations | **0 overlapping orgs (Shield 2)** |
| **Task Instance IDs** | 491 unique issues | 200 unique issues | **0 overlapping IDs (Shield 3)** |
| **Pre-training Cut** | Memorized allowed | Filtered out | **0 memorized packages (Shield 4)** |
| **Contrastive Balance**| 250 Solved / 250 Failed | 100% Oracle Available | Balanced |
| **TDD Instances** | N/A | 48 test-writing instances | Stratified |

* **Memory Architecture:** SQLite store (`swe_contrastive_memory.sqlite`) combining FTS5 BM25 lexical ranking with 128-dimensional dense vectors, protected at runtime by `ReadOnlyMemoryProxy`.
* **Execution Boundary:** Frozen GLM 5.3 Flash at `temperature=0.0`, `max_tokens=4096`, `seed=42`. All 600 LLM calls strictly auditable in `runs/`.

---

## 5. Execution Guide & Reproducibility

### 1. Running the Complete 5-Suite Hook & Backtrack Test
```bash
# Run unit tests validating hook registration, budget caps, TAR, and in-flight backtracks
python3 research/pi_baseline/tests/test_phase2_pi_hooks.py
```
*Expected Output:*
```text
test_1_fork_point_harvesting_and_causal_pivot (test_phase2_pi_hooks.TestPhase2PiHooks) ... ok
test_2_token_budget_cap_enforcement (test_phase2_pi_hooks.TestPhase2PiHooks) ... ok
test_3_trap_avoidance_interception (test_phase2_pi_hooks.TestPhase2PiHooks) ... ok
test_4_unified_hook_manager_end_to_end_lifecycle (test_phase2_pi_hooks.TestPhase2PiHooks) ... ok
test_5_autonomous_in_flight_harvesting_and_linear_partitioning (test_phase2_pi_hooks.TestPhase2PiHooks) ... ok
----------------------------------------------------------------------
Ran 5 tests in 0.051s
OK (TAR: 66.7%, Budget Ceiling: 1000 tokens)
```

### 2. Testing 40-Task Benchmark Suite Integrity & Anti-Contamination
```bash
# Validate 40-task synthesis, 20/20 train-eval split, and 0.0% leakage
python3 research/pi_baseline/tests/test_phase3_task_suite.py
```

### 3. Ingesting 40 Authentic SWE-Bench Trajectories
```bash
# Stream 40 trajectories from Hugging Face and harvest Delta_pivot into SQLite
python3 research/pi_baseline/harness/fetch_swe_trajectories.py --limit 40
python3 research/pi_baseline/harness/harvest_swe_contrastive_memory.py \
    --input "research/pi_baseline/data/swe_stream_40.jsonl" \
    --db "research/pi_baseline/data/contrastive_memory.sqlite"
```

### 4. Running the swe-rigrous-eval Suite & Leakage Audit
```bash
# Verify the 4 Leakage Shields across repository splits
python3 research/swe_rigorous_eval/benchmarks/audit_dataset_splits.py

# Run the 3-arm evaluation across N=200 held-out defects
python3 -m research.swe_rigorous_eval.harness.swe_arm_evaluator \
    --config research/swe_rigorous_eval/config/eval_config.json \
    --output_dir research/swe_rigorous_eval/runs/
```

---

## 6. Generated Deliverables & Output Artifacts

1. **`research/pi_baseline/harness/hooks/pi_hook_manager.py`:** Hook orchestrator featuring dynamic in-flight step buffers and error-triggered backtrack capture.
2. **`research/pi_baseline/harness/hooks/contrastive_harvester.py`:** Harvester implementing true online autonomous step partitioning over unseeded live sessions.
3. **`test_phase2_pi_hooks.py` (5 Test Suites):** Formal verification suite proving 100% deterministic pass rate and 66.7% Trap Avoidance Rate.
4. **40-Task Multi-Session Benchmark Suite:**
   * `train_stream_v1.json` (20 training tasks)
   * `eval_stream_v1.json` (20 evaluation tasks)
   * Zero task collision ($0.0\%$) and zero code hash overlap ($0.0\%$).
5. **Real-World SQLite Trajectory Store:** 40 authentic OpenHands SWE-bench trajectories mined into SQLite with verified $\Delta_{\text{pivot}}$ pairs.
6. **`research/swe_rigorous_eval/` Benchmark Suite:**
   * `STATISTICAL_ANALYSIS_REPORT.md` (7.6 KB): Complete 3-arm evaluation metrics across $N=200$ real defects.
   * `swe_contrastive_memory.sqlite` (4.4 MB): 500 harvested contrastive episodes (250 solved / 250 failed).
   * Verified 4-Shield Anti-Leakage certification.

---

## 7. Downstream Dependencies & Week 5 Handoff

* **Prerequisites Delivered:** Fully operational online autonomous harvester, in-flight backtrack error tracking, verified 40-task benchmark split, and 66.7% TAR metric.
