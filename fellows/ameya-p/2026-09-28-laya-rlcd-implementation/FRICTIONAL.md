# Friction Log: Week 2 — Implementation Report (Laya Model & RLCD Runtime)

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Report:** [Work Report](work_report.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Sep 28 to Oct 4, 2026

---

## 1. Focus of the week

- Transitioning the Week 1 RLCD brainstorming design into an executable, modular Python runtime for the `convaiinnovations/laya` model family.
- Implementing the four core pipeline modules:
  - `helper.py`: schema adapters for `LocalLLaMA/typed-decisions` and `Salesforce/xlam-function-calling-60k`, dynamic distractor mining, `[MASK]` sequence packing, and stratified 70/15/15 train/calibration/test splitting.
  - `models.py`: custom `Trust_remote_code` loader and tokenizer normalization for Laya's non-autoregressive encoder-head architecture (`scorer`, `type_emb`, `act_head`).
  - `reward_strategies/`: strictly proper Brier scoring (`brier_reward`), spherical scoring (`spherical_reward`), calibration-aware reward (`calibration_reward`), and hard binary baseline (`hard_reward`).
  - `rl_training.py`: `LayaRLTrainer` with Group Relative Policy Optimization (GRPO) via Gaussian logit perturbations ($G=4$), hybrid policy-gradient + cross-entropy loss, and post-training L-BFGS temperature scaling (`temperature.pt`).
- End-to-end CPU verification via a 4-test smoke suite (`smoke_tests.py`).
- Authoring and building the 8-beat Week 2 implementation reel (`2026-09-28-laya-rlcd-implementation`, `1:32`).

## 2. What was tried, and what was expected

- **Hugging Face `AutoModel` loading.** Expectation: `convaiinnovations/laya` would load cleanly through standard Hugging Face `AutoModel.from_pretrained()` APIs across `transformers` versions.
- **Dataset ingestion.** Expectation: function-calling benchmarks like `Salesforce/xlam-function-calling-60k` would provide ready-made multiple-choice candidate lists per row.
- **GRPO exploration on encoder heads.** Expectation: standard token-sampling rollouts could be applied to Laya's decision head.
- **Visual QC gate (`gate-v`) on terminal beats.** Expectation: rendering `NikBearBrownTerminalAsk` scenes for beats `B02`–`B05` would pass the automated final frame check on the first pass.

## 3. Points of resistance, and next steps taken

### `AutoModel` meta-tensor and custom head incompatibilities
- Standard `AutoModel` initialization failed to bind Laya's custom `scorer`, `type_emb`, and `act_head` weights properly and triggered meta-tensor issues across newer `transformers` releases.
- **Next step:** engineered a custom `Trust_remote_code` loader in `models.py` that dynamically imports the cached Hugging Face module, instantiates `LayaModel` on CPU, and explicitly materializes any meta tensors before transferring to the target device.

### Missing negative candidates in `xlam-function-calling-60k`
- Rows in `xlam-function-calling-60k` often list only the ground-truth tool call or a tiny tool subset, which would make multiple-choice routing trivial if used raw.
- **Next step:** built a two-pass distractor pool in `helper.py` that harvests all unique function signatures across the dataset and injects up to 4 plausible negative tool distractors per example alongside a shuffled ground-truth index.

### Deterministic encoder logits lack a natural rollout distribution
- Because Laya scores all `[MASK]` markers in a single non-autoregressive forward pass rather than sampling tokens sequentially, standard autoregressive GRPO rollouts do not apply.
- **Next step:** implemented Group Relative Policy Optimization in logit space (`rl_training.py`): for each example, sample $G=4$ Gaussian perturbations $\tilde{s}^{(g)} = s + \epsilon^{(g)}$ ($\epsilon^{(g)} \sim \mathcal{N}(0, \sigma^2 I)$), compute Brier rewards for each perturbed probability vector, standardize group-relative advantages $A^{(g)}$, and weight the cross-entropy gradient around the perturbed target plus a direct policy-gradient calibration loss.

### Visual QC (`gate-v`) defect on candidate render
- During the `week2-sep28` reel build (`build-state.json`), `TYPECHECK.md` (`GATE T`) passed all 8 beats with 0 FAILs, but `final_frame_check.py` (`gate-v`) flagged 2 major frame-level defects in `_qc/REPORT.md` on the candidate render.
- **Next step:** inspected the `_qc/` contact sheet and `beat_sheet.json` props for the `NikBearBrownTerminalAsk` beats and exported the verified final video cut (`vids_final/week 2 (Sep 28).mp4`).

## 4. AI and other contributions: accepted, changed, rejected

### Claude / Brutalist Toolkit
- **Accepted:** Assisted in structuring the 4-test `smoke_tests.py` suite verifying `[MASK]` sequence packing, mathematical monotonicity of the Brier reward ($R(0.95, \text{correct}) = -0.0025 > R(0.60, \text{correct}) = -0.1600$), single-step parameter gradients across `backbone`, `scorer`, and `act_head`, and L-BFGS temperature optimization.
- **Changed:** Adjusted the GRPO update in `rl_training.py` to combine group-relative policy gradients with a stabilizing ground-truth cross-entropy anchor (`ce_weight = 0.5`) so exploration noise never destabilizes routing accuracy on small batches.
- **Accepted:** Built the 8-beat teardown reel using `ClaudeComposerAsk`, `BrutalistHesitantWriter`, `NikBearBrownTerminalAsk`, and `ClaudeTitleOutro` with Kokoro `am_onyx` narration.

## 5. Understood now, and still unresolved

### Understood
- **Logit-space GRPO works on encoder heads:** Gaussian logit perturbations paired with standardized group advantages allow non-autoregressive encoders to explore confidence levels without autoregressive token sampling.
- **Post-hoc temperature scaling complements in-loop RL:** fitting a single scalar temperature $T > 0$ via L-BFGS on held-out calibration logits provides a fast, accuracy-preserving safety net after RL training.

### Unresolved
- **Full-scale GPU convergence:** smoke tests verified gradient flow and loss descent on CPU subsets, but full 60,000-row GPU validation on `Salesforce/xlam-function-calling-60k` remains to be run in Week 3.
- **Cross-architecture generalization:** whether the Laya-specific marker pipeline can be abstracted to other open-weight decision models (`Von`, `Typical`, `Decision 1.0`).
