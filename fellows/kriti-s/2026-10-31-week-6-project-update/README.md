# Week 6: Carry the Couch Milestone 1 — Simulation Environment, Deep Sets Pooling, Symmetry-Breaking Noise, and Emergent Action Diagnostics

- **Week:** 26–31 Oct 2026 
- **Group:** RL Environment
- **Project:** Carry the Couch
- **Primary systems investigated:** VMAS 2D Planar Physics Substrate, Couch Inertia & Viscous Floor Friction, 8D Relative Couch Perception, Permutation-Invariant Teammate Aggregation (DeepSets), Symmetry-Breaking Private Stochastic Noise ("Whispers"), Physics & Dynamic Verification Suite (Tests 1–8, including Coupled Differential Thrust & Rotation), 6-Category Action Taxonomy Diagnostics (ActionTracker), Bout Duration Metrics, Technical Knowledge Base & Code Walkthrough
- **Code:** [KritiShahi/rl](https://github.com/KritiShahi/rl)
- **Progress video:** [Week 6 Review Cut](https://drive.google.com/file/d/12M1Yt1ivdba0GYSGlkWkJXk74UzJkaD3/view?usp=drive_link)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's explainer:** [Deep Sets in Multi-Agent RL — Order-Free Team Permutation Invariance](../2026-10-31-deep-sets/README.md)
- **Beat sheet:** [beatsheet.md](beatsheet.md) · [beat_sheet.json](beat_sheet.json) · **Narration:** [script.md](script.md)

## Summary

The week completed Milestone 1 of the Carry the Couch cooperative multi-agent reinforcement learning (MARL) project: a custom VMAS 2D simulation of a 40 kg couch with floor friction, moved by identical box creatures through body-frame thrust; a 24D local observation with an 8D couch-centric component, permutation-invariant sum pooling of teammate features, and private stochastic "whisper" noise ($\sigma = 0.05$) to break symmetric deadlocks; a shared team reward; and a 6-category `ActionTracker` with bout-duration metrics to measure role persistence. The verification suite runs 26 tests (8 environment tests plus 18 body-design and budget tests), all passing. Milestone 2, the shared-policy MAPPO baseline across the layout ladder, is next.

## 1. Executive Summary & Engineering Scope

Week 6 marks the design, implementation, and verified completion of **Milestone 1** for the **Carry the Couch Together** cooperative multi-agent reinforcement learning (MARL) project.

### Core Research Question
> **Can a team of homogeneous agents—sharing identical neural network weights, relying strictly on local perception, and lacking agent IDs or predefined roles—learn to cooperatively transport a heavy, couch-shaped load through tight obstacles and corridors, and does a shared policy trained with small teams ($N = 2\text{--}4$) generalize zero-shot to large swarms ($N = 8\text{--}12$) across procedural layouts without retraining?**

My research focuses on developing a decentralized multi-agent reinforcement learning (MARL) system using PyTorch and VMAS (Vectorized Multi-Agent Simulator), where homogeneous agents learn to cooperatively transport a couch-shaped load through tight obstacles, corridors, and narrow passages without pre-assigned roles, unique IDs, or centralized communication. The project investigates whether agents executing shared policy weights with local observations can spontaneously specialize into roles (pushers, steerers, anchors), and whether policies trained on small teams ($N = 2\text{--}4$) can generalize zero-shot to large swarms ($N = 8\text{--}12$) across procedural layouts under a fixed morphological budget.

* **Expected Deliverables:** A 5-level VMAS procedural layout ladder, a parametric body design and budget enforcement module, a shared-policy MAPPO architecture for small teams ($N = 2\text{--}4$), zero-shot scaling evaluations up to $N = 12$, an automated evaluation pipeline, behavioral rollout video clips, and complete documentation via a `SKILL.md` package.

Milestone 1 establishes the complete physics foundation, decentralized coordination mechanisms, unit testing suite, and behavioral action diagnostic infrastructure required before launching large-scale MAPPO training sweeps in Milestone 2.

What was implemented this week in (details in [§4](#4-technical-implementation-details)):
1. **Couch transport scenario:** a VMAS Level 1 open-floor scenario (`CouchTransportScenario`) with a heavy couch, a goal pose and N identical box creatures, stepped as batched environments on CPU.
2. **Body-frame thrust actions:** each creature outputs a 2D action in $[-1, 1]^2$, scaled by its push force and rotated into world coordinates.
3. **24D local observation:** ego state, couch perception, goal guidance, sum-pooled teammate features and private noise, with no global coordinates or agent IDs.
4. **Shared team reward and termination:** progress, alignment, contact and success terms, plus a per-agent effort penalty.
5. **`ActionTracker`:** six behavior categories with step counts, bout counts and average bout duration, updated every step.
6. **Body, swarm and budget modules:** parametric creature bodies, a swarm homogeneity audit and a morphological budget checker.
7. **Verification suite:** 26 tests, including environment Tests 1–8.

---

## 3. Codebase Architecture & File Manifest

### Directory Layout

```text
rl/
├── src/
│   ├── body/
│   │   ├── design.py                 # Parametric box creature morphology and schema
│   │   └── factory.py                # Creature factory and swarm homogeneity engine
│   ├── budget/
│   │   ├── checker.py                # Budget module and automated constraint checking
│   │   └── generator.py              # Body candidate generator and archetype library
│   ├── config/
│   │   └── runtime.py                # Runtime and CPU vectorization configuration
│   └── env/
│       ├── couch_transport.py        # VMAS couch transport scenario + ActionTracker
│       ├── layouts.py                # Procedural layout and entity pose generator
│       └── wrappers.py               # Vectorized environment wrappers and factories
├── tests/
│   ├── test_body.py                  # Body design and creature factory tests
│   ├── test_budget.py                # Budget checker and candidate generator tests
│   └── test_couch_env.py             # Environment Tests 1–8
├── configs/                          # budget_limits.json, default_body.json, runtime_config.json
├── artifacts/flat_floor_render_sample.png
├── run_tests.py                      # Milestone 1 verification runner
├── setup_env.sh                      # Virtual environment setup with pinned dependencies
├── requirements.txt
```

### Module Responsibilities

| Module | Responsibility |
|---|---|
| `src/env/couch_transport.py` | Vectorized multi-agent couch transport scenario for VMAS: couch and agent bodies, body-frame thrust, private whisper noise, and the online `ActionTracker`. |
| `src/env/layouts.py` | Procedural layout and entity pose generation. |
| `src/env/wrappers.py` | Vectorized environment wrappers and factory functions for `CouchTransport`. |
| `src/body/design.py` · `src/body/factory.py` | Parametric box creature morphology; swarm creation and homogeneity audits. |
| `src/budget/checker.py` · `src/budget/generator.py` | Morphological budget validation; archetype library and budget-valid body candidates. |
| `src/config/runtime.py` | Runtime and CPU vectorization configuration. |
| `run_tests.py` | Discovers and runs every `tests/test_*.py` suite. |

---

## 4. Technical Implementation Details

### 4.1 Simulation Architecture & Physical Mechanics

`src/env/couch_transport.py` builds a vectorized 2D VMAS world (`make_world`), using the defaults in `LayoutConfig` (`src/env/layouts.py`) and `BodyDesign`:

| Element | Implementation |
|---|---|
| **World** | VMAS `World` with time step $dt = 0.05\,\text{s}$, 10 physics substeps, a $6\,\text{m} \times 6\,\text{m}$ arena, and no global friction. |
| **Couch** | Movable, rotatable box, $1.2\,\text{m} \times 0.6\,\text{m}$, $40\,\text{kg}$, with floor friction coefficient $0.35$ applied to both linear and angular motion. |
| **Creatures** | $N$ identical agents built from one `BodyDesign` (default $0.4\,\text{m} \times 0.4\,\text{m}$, $5\,\text{kg}$, push force $30\,\text{N}$, sensing range $2.5\,\text{m}$). Each collides as a sphere whose radius is half the body's shorter side. |
| **Goal** | A non-colliding target ($0.25\,\text{m}$ radius) with a target heading, sampled at least $1.5\,\text{m}$ from the couch. |
| **Spawning** | Creatures are placed on a ring about $0.85\,\text{m}$ around the couch, with radial jitter. |

The couch is heavy enough that one creature cannot move it effectively, while two pushing together can. Tests 1 and 2 check exactly this ([§4.3](#43-verification-suite--test-results)).

### 4.2 Agent Interface, Reward and Diagnostics

#### Action model (`PlanarThrustDynamics`)
Each creature outputs a 2D action in $[-1, 1]^2$ in its own body frame. The action is clamped, multiplied by the creature's push force, and rotated into world coordinates by the creature's heading before VMAS applies it as a force.

#### Observation space (24D)
Every observation is local and relative to the creature, with no global coordinates and no agent IDs:

| Component | Size | Contents |
|---|---|---|
| Ego state | 6 | Body-frame velocity, angular velocity, previous action, speed |
| Couch perception | 8 | Body-frame couch position, $\sin$ and $\cos$ of relative heading, relative velocity, contact normal (zero when not touching) |
| Goal guidance | 4 | Body-frame goal position, $\sin$ and $\cos$ of relative goal heading |
| Teammates | 4 | Sum of relative position and velocity $(\Delta p, \Delta v)$ over teammates within sensing range |
| Private noise | 2 | $\boldsymbol{\xi}_i \sim \mathcal{N}(0, \sigma^2 \mathbf{I}_2)$ with $\sigma = 0.05$, drawn fresh for each creature at each step |

- **Sensing range:** couch perception and each teammate's features are zeroed beyond the creature's sensing range.
- **Teammate pooling:** summing teammate features makes the observation independent of teammate order and keeps it at 4 dimensions for any team size (Deep Sets-style sum pooling). The learned encoder $\phi$ applied before the sum belongs to the Milestone 2 actor-critic networks, which are not built yet.
- **Symmetry breaking:** the private noise lets creatures sharing identical policy weights act differently when their situations are mirror images.

#### Reward and termination
A shared team reward is computed once per step and given to every creature:
- **Progress:** $1.0 \times$ the decrease in couch-to-goal distance since the last step.
- **Alignment:** $0.5 \times$ the decrease in heading error since the last step.
- **Contact:** $0.05 \times$ the fraction of creatures touching the couch.
- **Success:** $+50$ when the couch is within $0.2\,\text{m}$ and $0.15\,\text{rad}$ of the goal pose.

Each creature also receives an effort penalty of $-0.01\,\lVert a \rVert^2$. There is no collision penalty. An episode ends on success or after 500 steps.

#### ActionTracker diagnostics
`ActionTracker` runs after every physics step (`post_step`) and reports its metrics through `info()`. Each step it marks which of six behavior categories are active, using speed thresholds of $0.02\,\text{m/s}$ and $0.02\,\text{rad/s}$:

| Category | Active when |
|---|---|
| Translation | A creature touches the couch, and the couch moves but barely rotates |
| Arc steering | A creature touches the couch, and the couch both moves and rotates |
| Opposed couple | A creature touches the couch, and the couch rotates in place |
| Anchoring | A creature stays still in contact while the couch rotates |
| Repositioning | A creature moves without touching the couch, not moving away from it |
| Back off | A creature moves away from the couch |

For each category it records step counts, time in seconds and as a percentage, and bout counts. A new bout starts when a category switches from inactive to active, and average bout duration is time divided by bouts.

#### Body, swarm and budget modules
- **`BodyDesign`** (`src/body/design.py`): a parametric box creature (width, length, mass, push force, per-face grip, sensing range) with bounds checks, serialization and a SHA-256 fingerprint.
- **`CreatureFactory`** (`src/body/factory.py`): builds a swarm from one design and audits it, rejecting heterogeneous bodies and identity inputs.
- **`BudgetChecker`** (`src/budget/checker.py`): costs a body as $1.5 \cdot \text{mass} + 1.0 \cdot \text{force} + 20 \cdot \text{area} + 5 \cdot \sum \text{grip} + 2 \cdot \text{range}^2$ against a total budget of 100 (`configs/budget_limits.json`).
- **Candidate generator** (`src/budget/generator.py`): an archetype library (such as balanced, heavy pusher and compact steerer), random valid bodies, and projection of a body back within budget.

### 4.3 Verification Suite & Test Results

The environment is validated by eight tests in `tests/test_couch_env.py`, run with the body-design and budget suites (`tests/test_body.py`, `tests/test_budget.py`) through `run_tests.py`. Run on 2026-11-02: **26 tests, 0 errors, 0 failures.**

| Test ID | Test Name | Invariant Checked | Result |
|---|---|---|---|
| **Test 1** | Single Agent Inability | A single agent pushing alone cannot achieve effective team transport | **PASS** |
| **Test 2** | Pure Dual Translation | Two agents pushing in parallel along the center line produce pure linear translation | **PASS** |
| **Test 3** | Pure Distal Rotation | Two agents applying opposing tangential forces at distal ends produce pure in-place rotation | **PASS** |
| **Test 4** | Identity Isolation & Permutation Symmetry | Zero identity leakage and strict permutation invariance in the observation space | **PASS** |
| **Test 5** | Vectorized CPU Throughput | 128 parallel environments meet the gate of ≥ 2,500 steps/s (measured 8,561.7 steps/s) | **PASS** |
| **Test 6** | Coupled Differential Thrust & Rotation | Asymmetric forward pushing produces simultaneous translation and rotation | **PASS** |
| **Test 7** | ActionTracker: All Six Categories | `ActionTracker` detects and logs all 6 physical action categories | **PASS** |
| **Test 8** | ActionTracker: Bout Transitions & Average Duration | Rising-edge bout transitions and precision of average bout duration | **PASS** |

---

## 5. Execution Guide & Reproducibility

### 1. Setting Up the Environment
```bash
# Create .venv and install the pinned CPU dependencies from requirements.txt
./setup_env.sh
source .venv/bin/activate
```

### 2. Running the Verification Suite
```bash
# Runs tests/test_body.py, tests/test_budget.py and tests/test_couch_env.py
python3 run_tests.py
```

---

## 6. Generated Deliverables & Output Artifacts

1. **Simulation environment:** `src/env/couch_transport.py`, `src/env/layouts.py`, `src/body/design.py`, `src/budget/checker.py`.
2. **Verification suite:** `run_tests.py` and `tests/test_couch_env.py` (Tests 1–8), with `tests/test_body.py` and `tests/test_budget.py`.

---

## 7. Downstream Dependencies & Milestone 2 Handoff


**Next milestone — Milestone 2 (Shared-Policy MAPPO Baseline & Layout Ladder):**
* Procedurally generate layouts 2 through 5 (Wall Obstacle, Narrow Corridor, Narrow Gate, L-Shaped Corner).
* Build the MAPPO trainer with actor-critic networks using DeepSets pooling.
* Train baseline policies on team sizes $N \in [2, 4]$ across the layout ladder.

## Attribution and Contribution

Work by Kriti S.: technical architecture designed and structured into a 12-beat teardown (`claude-liam-couch-week-six`), custom Remotion scenes constructed (`ClaudeComposerAsk`, `BrutalistHesitantWriter`, contact normal animations, action tracker diagnostic tables), and narration script written, voiced via Kokoro `am_onyx` (Liam in for Kriti). Research and review by Kriti S.: specification of the 6-category action taxonomy, derivation of Test 6, authored conceptual notes and code walkthroughs, and approval of the video review cut.
