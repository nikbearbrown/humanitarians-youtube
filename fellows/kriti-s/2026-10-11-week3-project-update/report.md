# Week 3: Phase 1 Benchmarking Harness, SWE-Bench Trajectories, and Multi-Arm Evals

> **Project:** RL Environment
> **Reporting Window:** October 05, 2026 – October 11, 2026  
> **Team Focus:** Episodic & Causal Memory Architectures (Kriti Shahi)  
> **Primary Systems Investigated:** Pinned Pi Runtime, SWE-bench OpenHands Trajectories (`nebius/SWE-rebench-openhands-trajectories`), Multi-Arm Evaluation Harness, Contrastive Scoping

---

## 1. Executive Summary & Engineering Scope

Week 3 focused on the implementation and validation of **Phase 1**—building an empirical evaluation harness to measure agent performance across diverse memory conditions. The week commenced with the formal ingestion and scoping of the Contrastive Episodic Memory (CEM) system.

Before deploying expensive benchmark runs, a deterministic verification suite of algorithmic Python tasks was constructed to validate that the pinned Pi agent executed tools accurately and yielded reproducible outputs. Following sanity checks, the open-source Nebius SWE-bench trajectory dataset (`SWE-rebench-openhands-trajectories`) was integrated to supply realistic multi-turn software engineering tasks. Multi-arm comparative benchmarking (Arm 0: No Memory vs. Arm 1: Flat RAG vs. Arm 3: Contrastive Episodic Memory) was initiated across a 5-seed evaluation battery (`[42, 137, 2026, 31415, 99999]`). A pivotal finding emerged on October 9: Arm 3 initially yielded zero improvement over Arm 1 due to the *semantic embedding similarity trap*, leading directly to the mathematical re-architecture of contrastive trajectory harvesting.

## 3. Codebase Architecture & File Manifest

### Directory Layout
```text
/Users/kritishahi/Desktop/Humanitarians AI/test/
├── Phases_Memory.md                  # Master technical tracking document for Phases 0-4
├── Notes_Self_Understanding.md       # Empirical observations and telemetry notes
├── generate_contrastive_scoping_artifacts.py # Generator for CEM scoping artifacts
├── .arkenos/artifacts/
│   ├── Pi_Agent_Contrastive_Episodic_Memory_Scoping.pdf
│   └── Pi_Agent_Contrastive_Episodic_Memory_Scoping.docx
└── research/
    └── pi_baseline/
        ├── harness/
        │   ├── eval_runner.py        # Multi-arm evaluation orchestrator
        │   ├── dataset_loader.py     # Nebius SWE-bench trajectory ingestion
        │   └── tests/
        │       └── test_pi_sanity.py # Sanity verification test battery
        └── logs/
            └── calibration_battery.json # Multi-seed baseline calibration records
```

### Module Responsibilities
| Script / Module | Responsibility | Technology |
|---|---|---|
| `test_pi_sanity.py` | Validates that pinned Pi executes deterministic Python algorithmic tasks correctly. | Python, PyTest |
| `eval_runner.py` | Orchestrates multi-arm benchmark evaluations across evaluation seeds with timeout guards. | Python, Asyncio |
| `dataset_loader.py` | Parses HuggingFace SWE-rebench parquet/JSON files into normalized trajectory episodes. | Python, Pandas, JSONL |
| `generate_contrastive_scoping_artifacts.py` | Builds PDF and DOCX technical briefs detailing the revised CEM architecture. | Python, ReportLab, python-docx |

---

## 4. Technical Implementation & Multi-Arm Benchmark Setup

### 4.1 Multi-Arm Benchmark Design
```text
                          [ SWE-Bench Task Instance ]
                                      |
         +----------------------------+----------------------------+
         |                            |                            |
       Arm 0                        Arm 1                        Arm 3
    [No Memory]                  [Flat RAG]               [Contrastive Memory]
  Raw task context            Dense top-k semantic       Dual trajectory pairs:
   + system prompt             trajectory retrieval        (tau+, tau-) retrieval
         |                            |                            |
    Pi Agent Run                 Pi Agent Run                 Pi Agent Run
         |                            |                            |
  Pass Rate: ~18%              Pass Rate: ~22%              Pass Rate: ~22% (Initial)
                                                            [Bottleneck: Cosine Trap]
```

### 4.2 Benchmark Configuration Matrix
* **Evaluation Seeds:** `[42, 137, 2026, 31415, 99999]`
* **Task Timeout:** 60 seconds per task attempt
* **Retry Budget:** Maximum 3 retries per instance
* **Memory Budget Limit:** Strictly capped at 1,000 tokens
* **Task Context Window Limit:** 8,192 tokens

---

## 5. Execution Guide & Reproducibility

### 1. Running Deterministic Sanity Tests
```bash
# Execute the basic verification battery
python3 -m unittest research/pi_baseline/harness/tests/test_pi_sanity.py
```

### 2. Ingesting SWE-Bench Trajectories
```bash
# Load and preprocess sample trajectories
python3 research/pi_baseline/harness/dataset_loader.py \
    --dataset "nebius/SWE-rebench-openhands-trajectories" \
    --output_dir "research/pi_baseline/data/trajectories/"
```

### 3. Generating the Contrastive Scoping Artifacts
```bash
# Compile the scoping document
python3 generate_contrastive_scoping_artifacts.py
```

---

## 6. Generated Deliverables & Output Artifacts


1. **`test_pi_sanity.py`:** Complete, reproducible algorithmic test harness proving Pi agent determinism.
2. **Issue `TEST-1`:** Structured issue thread tracking baseline telemetry cleanups.

---

## 7. Downstream Dependencies & Week 4 Handoff

* **Empirical Bottleneck Diagnosed:** Identified that standard semantic retrieval cannot distinguish subtle logic errors in programming agent trajectories.
* **Handoff to Week 4:** Initiate **Phase 2 Engineering**—formalize the mathematical theory of counterfactual learning, implement Pi subsystem hooks (`pi_hook_manager.py`, `context_injector.py`, `contrastive_harvester.py`), and test automated trap avoidance across contrastive trajectory forks.
