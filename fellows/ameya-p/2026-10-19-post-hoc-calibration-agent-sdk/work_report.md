# Fine-Tuning Platform: Post-Hoc Calibration Bake-Off & Autonomous Agent SDK/Skill Packaging

---

Volunteer Name: Ameya Padwad  
Report Week: Oct 19 to Oct 25, 2026

## 1. Introduction

Following last week's finding that sharp multi-class accuracy gains during fine-tuning can occasionally trigger Expected Calibration Error (ECE) spikes on subjective tasks, this week focused on two core objectives:

1. Engineering an automated **Post-Hoc Calibration Bake-Off** module directly inside the training pipeline (`training.py`, `helper.py`, `run_post_hoc_calibration.py`) to resolve post-training overconfidence and bring ECE below 5% without sacrificing accuracy.
2. Packaging the entire platform into an installable **Python SDK (`rlcd`), CLI entry point (`rlcd-fine-tune`), and autonomous agent skill (`skills/rlcd-fine-tune/SKILL.md`)** so that any AI agent can autonomously fine-tune and calibrate a decision model on arbitrary datasets.

## 2. Automated Post-Hoc Calibration Bake-Off

To eliminate post-training overconfidence on subjective multi-class and pairwise preference tasks without requiring GPU retraining, a multi-strategy post-hoc calibration tournament was integrated into the end of the `RLTrainer` workflow:

- **Multi-Strategy Calibration Tournament:** After fine-tuning, the pipeline automatically evaluates candidate post-hoc calibrators on the held-out calibration split—comparing **Baseline (Raw Logits)**, **Temperature Scaling** ($\text{Softmax}(z / T)$), **Platt / Vector Scaling** ($\text{Softmax}(A \cdot z + b)$), and **Matrix Scaling** ($\text{Softmax}(W \cdot z + b)$)—and saves the winning calibrator (`calibrator.pt`) based on validation ECE and Brier score.
- **Smooth Log-Space L-BFGS Optimization:** Parameterized temperature $T \in [T_{\min}, T_{\max}]$ smoothly in unconstrained space so L-BFGS optimization never steps into a zero-gradient hard clamp boundary.

### Bake-Off Results Across Subjective Tasks

All candidate strategies were evaluated across the three subjective tasks that previously exhibited post-fine-tuning overconfidence ("red ECE rows"). Every single task had its ECE slashed from $\sim 17\%\text{–}18\%$ down below $5\%$ (an average **73% reduction in calibration error**) in under 2 seconds on CPU while preserving **100% of fine-tuned accuracy**:

| Model & Task Domain                                                 | Candidate Strategy                                                                                      | Formula & Params                                                                                                                                                           |                       Accuracy                       |                                             Raw ECE $\to$ Calibrated ECE ($\Delta$)                                              | Calibration Outcome                                                                                                      |
| :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------- |
| **`wfzyx/von`** — Tweet Sentiment (26K, 3-Class `choice`)           | Baseline (Raw Logits)<br>Temperature Scaling<br>**Platt / Vector Scaling [SELECTED]**<br>Matrix Scaling | 0 Params \| $\text{Softmax}(z)$<br>1 Scalar \| $\text{Softmax}(z / 1.34)$<br>**6 Params \| $\text{Softmax}(A\cdot z + b)$**<br>12 Params \| $\text{Softmax}(W\cdot z + b)$ | $80.53\%$<br>$80.53\%$<br>**$80.53\%$**<br>$80.80\%$ | $17.24\%$ (Baseline)<br>$17.24\% \to 11.82\%$<br>**$17.24\% \to \mathbf{4.85\%}$ ($\mathbf{-12.39\%}$)**<br>$17.24\% \to 9.75\%$ | Overconfident (CE Loss)<br>Softened (Partial Gain)<br>**Selected: Slashes ECE by 72%**<br>Over-Parameterized for 3-class |
| **`wfzyx/von`** — Anthropic RLHF (60K, Pairwise `noul`)             | Baseline (Raw Logits)<br>**Temperature Scaling [SELECTED]**<br>Platt Scaling                            | 0 Params \| $\text{Softmax}(z)$<br>**1 Scalar \| $\text{Softmax}(z / 1.85)$**<br>2 Params \| $\text{Sigmoid}(A\cdot \Delta z + b)$                                         |       $62.03\%$<br>**$62.03\%$**<br>$62.03\%$        |             $18.46\%$ (Baseline)<br>**$18.46\% \to \mathbf{4.92\%}$ ($\mathbf{-13.54\%}$)**<br>$18.46\% \to 5.80\%$              | Overconfident on Preferences<br>**Selected: Slashes ECE by 73% & Preserves Symmetry**<br>Redundant for Symmetric Pairs   |
| **`Decision 1.0 (600M)`** — Tweet Sentiment (26K, 3-Class `choice`) | Baseline (Raw Logits)<br>Temperature Scaling<br>**Platt / Vector Scaling [SELECTED]**                   | 0 Params \| $\text{Softmax}(z)$<br>1 Scalar \| $\text{Softmax}(z / 1.36)$<br>**6 Params \| $\text{Softmax}(A\cdot z + b)$**                                                |       $79.50\%$<br>$79.50\%$<br>**$79.50\%$**        |             $17.38\%$ (Baseline)<br>$17.38\% \to 11.45\%$<br>**$17.38\% \to \mathbf{4.76\%}$ ($\mathbf{-12.62\%}$)**             | Overconfident on 600M Model<br>Softened (Partial Gain)<br>**Selected: Slashes ECE by 73%**                               |

- **Why Different Strategies Won:** **Platt / Vector Scaling** won on 3-Class Sentiment (`Von` ECE $17.24\% \to 4.85\%$; `Decision 1.0` ECE $17.38\% \to 4.76\%$) by correcting class-prior imbalances, whereas **Temperature Scaling** ($T^* = 1.85$) won on Pairwise Anthropic RLHF (`Von` ECE $18.46\% \to 4.92\%$) by softening overconfidence while preserving binary choice symmetry.

## 3. RLCD SDK, CLI & Autonomous AI Agent Skill Package

To make the RLCD pipeline usable out of the box by both developers and autonomous coding/research agents, the repository was restructured into a self-contained **SDK + Agent Skill package**:

- **Installable Python SDK (`rlcd`) & CLI (`rlcd-fine-tune`):** Packaged the codebase via `pyproject.toml` and `__init__.py` to expose a single high-level `rlcd.fine_tune()` SDK function (with 32 configurable training, model, schema, and calibration parameters) alongside the `rlcd-fine-tune` command-line executable.
- **Plug-and-Play Skill for Any AI Agent (`skills/rlcd-fine-tune/SKILL.md`):** Authored a complete agent skill specification that teaches any AI agent how to inspect datasets, invoke the `rlcd-fine-tune` CLI or `rlcd` Python SDK, configure `column_map` overrides when needed, and verify output checkpoints (`model.safetensors`, `calibrator.pt`, and `test_evaluation_metrics.json`).
- **End-to-End Autonomous Agent Verification (`tests/test_agent.md`, `results/SDK_agent_testing_report.md`):** Validated the SDK + skill package by having an isolated AI agent autonomously read `SKILL.md` and execute a 3-phase verification suite on local GPU hardware without human intervention or code edits—passing all smoke tests (Phase 1), default `xLAM` tool-selection fine-tuning (Phase 2), and blind multi-primitive runs across `choice`, `noul`, and `score` datasets with automatic post-hoc calibration (Phase 3).

## 4. Next Steps

- **Final Touches, End-to-End Testing & Project Wrap-Up:** Complete final polish, documentation review, and end-to-end verification tests to wrap up the project for final delivery.
