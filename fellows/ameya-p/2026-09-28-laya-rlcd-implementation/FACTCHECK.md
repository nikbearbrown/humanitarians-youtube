# FACTCHECK — 2026-09-28-laya-rlcd-implementation (Fine-Tuning Platform)

Every claim the narration makes, mapped to the source document:
`work_report.md` ("Fine-Tuning Platform: Implementation Report — Laya Model & RL Fine-Tuning Runtime (RLCD)").

## B00 — Cold open

- **"Ameya Padwad just shipped the implementation of Reinforcement Learning with Calibrated Decisions for the Laya model family."**
  Source §1: "This work transitions the Reinforcement Learning with Calibrated Decisions (RLCD) design into an executable, verified implementation for the Laya model family (`convaiinnovations/laya`)."

## B01 — BLUF

- **"The goal was to build a complete, self-contained RL loop that ingests typed-decision benchmarks, explores confidence calibrations, and updates the policy."**
  Source §1 objectives 1–5: ingesting benchmarks, constructing `[MASK]` sequences, computing proper scoring rewards, executing GRPO policy-gradient updates, and calibrating post-training temperature.

## B02 — Core Architecture (`helper.py` & `models.py`)

- **"The architecture is split into four core modules: `helper.py` for data ingestion, `models.py` for loading the Laya backbone, `reward_strategies/` for scoring, and `rl_training.py` for the training engine."**
  Source §2.1 (`helper.py`), §2.2 (`models.py`), §2.3 (`reward_strategies/brier.py`), and §3 (`rl_training.py`).

## B03 — Brier Score Proper Scoring Rule

- **"Using strictly proper scoring rules, like the Brier score, ensures the model is only rewarded when its stated confidence matches its true empirical accuracy."**
  Source §2.3: $R_{\text{Brier}}(p, y^*) = -\frac{1}{K}\sum_{k=0}^{K-1}(p_k - y_k)^2$, incentivizing honest confidence probabilities.

## B04 — GRPO Logit Perturbations (`rl_training.py`)

- **"The engine (`rl_training.py`) runs the forward pass, applies Group Relative Policy Optimization using Gaussian logit perturbations, and computes policy-gradient updates."**
  Source §3.2: samples $G=4$ Gaussian perturbations $\tilde{s}^{(g)} = s + \epsilon^{(g)}$ in logit space and computes group-standardized advantages $A^{(g)}$.

## B05 — Post-Training L-BFGS Temperature Calibration

- **"Before export, a post-training temperature calibration fits an optimal temperature on a held-out split using L-BFGS optimization (`temperature.pt`)."**
  Source §3.3: optimizes scalar temperature $T > 0$ via `torch.optim.LBFGS` on the 15% calibration split and saves `temperature.pt`.

## B06 — Your Turn Handoff

- Suggested prompt for the viewer to run `smoke_tests.py` and trace the GRPO perturbations and Brier score updates.

## B07 — Outro

- Title restate (`Implementation Report: Laya & RLCD`).
