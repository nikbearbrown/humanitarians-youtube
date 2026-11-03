# SHOTLIST — 2026-09-28-laya-rlcd-implementation (Fine-Tuning Platform)

8 beats. Landscape 3840x2160 (composed 1920x1080 @ scale 2).

| Beat | Pattern | What lands on screen |
|---|---|---|
| B00 | ClaudeComposerAsk | Greeting `Ciao, Liam` over the composer; the ask types in: "Explain the new Reinforcement Learning with Calibrated Decisions implementation for Laya."; output lines cascade (modular RL pipeline / GRPO / proper scoring rewards). |
| B01 | BrutalistHesitantWriter | Writer types the initial framing, hesitates, backspaces, and retypes the self-contained RLCD runtime goal for Laya. |
| B02 | NikBearBrownTerminalAsk | Terminal view walking through the four core modules (`helper.py`, `models.py`, `reward_strategies/`, `rl_training.py`). |
| B03 | NikBearBrownTerminalAsk | Terminal view showing the Brier proper scoring rule reward implementation and monotonicity check. |
| B04 | NikBearBrownTerminalAsk | Terminal view showing `LayaRLTrainer` GRPO Gaussian logit perturbations ($G=4$) and hybrid policy-gradient update. |
| B05 | NikBearBrownTerminalAsk | Terminal view showing post-training L-BFGS temperature scaling on the held-out calibration split (`temperature.pt`). |
| B06 | ClaudeComposerAsk | Composer `Your turn.` Prompt types in: running `smoke_tests.py` to trace GRPO perturbations and Brier score updates. |
| B07 | ClaudeTitleOutro | Closing title card for the Laya & RLCD implementation report. |
