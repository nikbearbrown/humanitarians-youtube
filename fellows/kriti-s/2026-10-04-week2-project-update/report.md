# Week 2: Phase 0 Environment Setup, Memory Taxonomy, and Episodic/Causal Scoping

> **Project:** RL Environment
> **Reporting Window:** September 28, 2026 – October 04, 2026  
> **Team Focus:** Episodic & Causal Memory Architectures (Kriti Shahi)  
> **Primary Systems Investigated:** Pi Agent Runtime (`pi_test/iacon_pi/`), Structural Causal Models (SCMs), Contrastive Trajectories, Remotion Explainer Pipeline

---

## 1. Executive Summary & Engineering Scope

Week 2 marked the transition from conceptual architecture to concrete system engineering. The week began with the implementation of **Phase 0**—establishing an isolated, reproducible execution environment for the Pi agent. Crucially, in response to researcher feedback regarding execution transparency, the test harness was migrated from ephemeral temporary directories to a permanent, auditable virtual environment under `pi_test/iacon_pi/`.

In the second half of the week, research focused on formalizing a taxonomy of cognitive memory systems for frozen language agents. The researcher and assistant mapped out six cognitive memory systems (Procedural, Semantic, Episodic, Causal, Prospective, and Metacognitive), rated their implementation complexity, and conducted an in-depth comparison between Pi's existing baseline (unindexed flat sliding-window history) and proposed novel architectures. By the end of Week 2, full formal engineering specifications were locked for both **Causal Memory** (Structural Causal Models with dynamic graph invalidation) and **Episodic Memory** (contrastive trajectory harvesting).

---

## 3. Codebase Architecture & File Manifest

### Directory Layout
```text
/Users/kritishahi/Desktop/Humanitarians AI/
├── pi_test/
│   └── iacon_pi/                     # Permanent, auditable Pi execution environment
│       ├── bin/                      # Virtual environment binaries (activate, python, pip)
│       └── lib/                      # Pinned Python package dependencies
├──├── Episodic and Causal Memory Architectures.docx # Canonical master document
└── Iacon/
    └── brutalist.art/
```

### Module Responsibilities
| Module / Script | Responsibility | Technology |
|---|---|---|
| `pi_test/iacon_pi/` | Permanent isolated sandbox housing pinned Pi agent binaries, logging wrappers, and test inputs. | Python 3.9 venv, Bash |

---

## 4. Technical Implementation & Comparative Architecture

### 4.1 Pi Baseline vs. Proposed Memory Architectures

| Dimension | Pi Baseline (Current) | Proposed Episodic Memory | Proposed Causal Memory |
|---|---|---|---|
| **Storage Primitive** | Unindexed raw message array in SQLite/JSONL | Structured trajectory store of success/failure pairs ($\tau^+, \tau^-$) | Structural Causal Model DAG ($\mathcal{G} = \langle \mathcal{V}, \mathcal{E} \rangle$) |
| **Retrieval Mechanism** | Recency sliding-window truncation | Contrastive dual-sided cosine similarity with negative avoidance | Causal parent/child traversal and intervention condition checks |
| **Token Cost** | $O(N)$ linear growth until context overflow | Fixed 1,000 token budget injected into system context | Variable (150–500 tokens) injecting minimal causal path subgraphs |
| **Failure Recovery** | Susceptible to repeating previous tool errors | Direct injection of negative pivot points: "Do not call $a^-$" | Interventional pruning: $P(Y \mid do(X))$ |


---

## 5. Execution Guide & Reproducibility

### 1. Activating the Permanent Sandbox
```bash
# Activate the auditable test environment
source "/Users/kritishahi/Desktop/Humanitarians AI/pi_test/iacon_pi/bin/activate"

# Verify environment isolation and Python path
which python
python --version
```

### 2. Validating Video Generation Pipeline
```bash
# Run AST linter and prop validator
cd "/Users/kritishahi/Desktop/Humanitarians AI/Iacon/brutalist.art"
python3 runtime/scripts/type_check.py
```

---

## 6. Generated Deliverables & Output Artifacts

1. **`pi_test/iacon_pi/`:** Fully initialized, auditable testbed preventing ephemeral data loss.
2. **`Episodic and Causal Memory Architectures.docx`:** Canonical master specification defining data schemas, algorithms, and subsystem integrations.

---

## 7. Downstream Dependencies & Week 3 Handoff

* **Prerequisites Delivered:** Permanent auditable execution sandbox, frozen-model baseline definition, and mathematical specifications and architectures for Episodic and Causal from research papers
* **Handoff to Week 3:** Initiate **Phase 1 Implementation**—building the deterministic benchmark harness, ingesting SWE-bench trajectory datasets (`SWE-rebench-openhands-trajectories`), validating baseline execution determinism on simple tasks, and conducting initial multi-arm memory evaluations.
