# Friction Log: Week 1 — Brainstorming & Project Overview

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Report:** [Work Report](work_report.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Sep 21 to Sep 25, 2026

---

## 1. Focus of the week

- Architecture and system brainstorming for a general-purpose fine-tuning platform targeting the Jev and Laya decision model families (`convaiinnovations/laya`).
- Designing a declarative job configuration schema (`job_config.json`) driving a 5-stage Training Runtime Worker: pre-flight guard, data ingestion & tokenization, model loading & PEFT setup, training execution, and evaluation & export.
- Formulating the Reinforcement Learning with Calibrated Decisions (RLCD) problem: training models whose stated confidence scores match their empirical accuracy.
- Evaluating three candidate RLCD reward formulations:
  1. Per-episode Brier / log proper scoring rules ($R = -(c - y)^2$).
  2. Two-stage learned empirical calibration reward model ($g_\phi(\text{context}, \text{decision}, c) \to \hat{p}_{\text{correct}}$).
  3. Batch-level differentiable soft-binned Expected Calibration Error (ECE) loss.
- Producing the 8-beat `project-overview` Brutalist video reel (`1:28`, 16:9 4K master) from `work_report.md`.

## 2. What was tried, and what was expected

- **Declarative worker design.** Expectation: a single JSON/YAML job specification could cleanly parameterize both standard Supervised Fine-Tuning (SFT) and RL calibration workflows without per-model custom scripts.
- **Standard RL reward design.** Expectation: a binary correctness reward ($+1$ for right, $-1$ for wrong) would suffice to train decision models via GRPO or PPO.
- **Batch-level ECE optimization.** Expectation: computing empirical accuracy across confidence bins inside a mini-batch would directly optimize calibration during policy updates.
- **Video reel production.** Expectation: the 5-stage architecture and the Brier scoring rule equation could be rendered directly through standard Brutalist Remotion scenes and a single locally typeset math asset.

## 3. Points of resistance, and next steps taken

### Binary rewards incentivize extreme overconfidence
- Standard binary $+1 / -1$ correctness rewards push policy logits toward $\pm\infty$, driving stated confidence toward $1.0$ or $0.0$ even on ambiguous tasks where true accuracy is only $\sim 60\%$.
- **Next step:** reformulated the RL reward around strictly proper scoring rules—specifically the Brier score $R = -(c - y)^2$ and spherical scoring—where the expected reward is uniquely maximized only when stated confidence $c$ equals the true probability of correctness $p^*$.

### Cold-start instability in two-stage and batch-ECE rewards
- The learned calibration regressor (Idea 2) suffers from a non-stationary cold start because the policy's confidence distribution shifts every N steps, invalidating earlier empirical bins.
- Batch-level soft-binned ECE (Idea 3) requires large mini-batches so that all $M$ confidence bins remain populated; sparse bins produce high-variance gradients.
- **Next step:** selected per-episode Brier score (Idea 1) as the primary Week 2 implementation baseline, paired with post-training temperature scaling on a held-out calibration split.

### Non-autoregressive encoder-head architecture in Laya
- Unlike standard causal LLMs trained with `trl.SFTTrainer`, Laya (`convaiinnovations/laya`) is a non-autoregressive masked encoder (~76M parameters) with custom `scorer`, `type_emb`, and `act_head` modules operating at `[MASK]` marker positions.
- **Next step:** scoped dedicated sequence-packing and marker-gathering modules (`helper.py` and `models.py`) rather than relying on off-the-shelf causal LM trainers.

### Outro lock warning on personal project overview reel
- During the `project-overview` reel build, `B07` triggered a skin warning (`palette=claude` with `TitleRestateOutro` instead of `ClaudeTitleOutro`).
- **Next step:** retained `TitleRestateOutro` intentionally because `OUTRO-LOCK.md` scopes the `@NikBearBrown` channel handle card to `claude-liam` channel releases rather than fellow project-overview reels.

## 4. AI and other contributions: accepted, changed, rejected

### Claude / Brutalist Toolkit
- **Accepted:** Used `ClaudeComposerAsk`, `BrutalistHesitantWriter`, `SkillTeardownPipeline`, `BarChart`, `TypesetMath`, `ClaudeVerdictArtifact`, and `TitleRestateOutro` to map the brainstorming report into an 8-beat explainer reel (`87.8s`) with Kokoro `am_onyx` narration.
- **Accepted:** Structured the mathematical comparison of Brier score, log score, and soft-binned ECE in the brainstorming report and rendered the Brier equation via local matplotlib mathtext (`TypesetMath`) to satisfy `GATE T` (`TYPECHECK.md` 0 FAILs).
- **Rejected:** Rejected using unverified generative AI diagrams for the 5-stage worker architecture; used deterministic Remotion props (`SkillTeardownPipeline`) instead.

## 5. Understood now, and still unresolved

### Understood
- **Calibration requires proper scoring rules:** accuracy and calibration are distinct objectives; a strictly proper scoring rule penalizes overconfident errors quadratically and gives the policy a direct gradient toward honest uncertainty.
- **Architecture dictates trainer design:** non-autoregressive decision encoders require marker-index gathering (`marker_pos`) and group logit perturbations rather than autoregressive token sampling.

### Unresolved
- **Exploration mechanism for deterministic encoder heads:** how best to sample candidate probability distributions from Laya's deterministic scoring head during GRPO rollouts (resolved in Week 2 via Gaussian logit perturbations).
- **Generalization across decision primitives:** how a single pipeline will unify categorical `choice`, binary `noul`, and continuous `score` tasks.
