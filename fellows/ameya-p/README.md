# Ameya P.

**Role:** ML Engineer  
**Project:** RL Environment  
**GitHub:** [@AmeyaPadwad](https://github.com/AmeyaPadwad/)  
**Organization:** Humanitarians AI (Iacon Optimus Program)  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Video Drive:** [RL_Environment_AmeyaPadwad](https://drive.google.com/drive/folders/1gH4FUFMF_hLI9aItdn7q8SeatKn2BRNc)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Renewal Request:** [Renewal Request](renewal-requests/2026-10-26-renewal-request.md)

## What's in this folder

- `2026-09-21-project-overview/` — Fine-Tuning Platform: Brainstorming Report
  (Project Overview). An AI-explainer / teardown reel sourced from the Week 1
  brainstorming report (`work_report.md`) on the general-purpose fine-tuning
  platform for the Jev and Laya decision model families. Covers the 5-stage
  declarative SFT pipeline (`job_config.json` → pre-flight guard → data
  ingestion → model + PEFT → training → export), the confidence calibration gap
  (60% actual accuracy vs. 95% stated confidence), and the proposed Brier-score
  proper scoring rule ($R = -(c - y)^2$) for Reinforcement Learning with
  Calibrated Decisions (RLCD). Built on the `claude` palette with Remotion
  scenes (`ClaudeComposerAsk`, `BrutalistHesitantWriter`,
  `SkillTeardownPipeline`, `BarChart`, `TypesetMath`, `ClaudeVerdictArtifact`,
  `TitleRestateOutro`) and Kokoro `am_onyx` narration. 16:9 master cut (1:28,
  8 beats).
- `2026-09-28-laya-rlcd-implementation/` — Fine-Tuning Platform: Implementation
  Report — Laya Model & RL Fine-Tuning Runtime (RLCD). A CLI/terminal-backed
  teardown reel sourced from the Week 2 implementation report (`work_report.md`)
  transitioning the RLCD design into an executable training pipeline for
  `convaiinnovations/laya`. Walks through the four core runtime modules
  (`helper.py` for dataset ingestion and `[MASK]` sequence packing, `models.py`
  for non-autoregressive encoder-head loading, `reward_strategies/` for strictly
  proper Brier scoring and calibration rewards, and `rl_training.py` for GRPO
  logit perturbations and policy-gradient updates) plus post-training L-BFGS
  temperature scaling (`temperature.pt`). Built on the `claude` palette with
  `ClaudeComposerAsk`, `BrutalistHesitantWriter`, `NikBearBrownTerminalAsk`,
  and `ClaudeTitleOutro`, narrated in Kokoro `am_onyx` (Liam). 16:9 cut (1:32,
  8 beats).
- `2026-10-05-xlam-laya-validation/` — Fine-Tuning Platform: End-to-End
  Validation Report — xLAM Dataset & Laya Model. A Plain-register validation
  report reel sourced from the Week 3 end-to-end benchmark run (`work_report.md`)
  testing the RLCD runtime on the 60,000-row
  `Salesforce/xlam-function-calling-60k` tool-selection dataset. Documents the
  jump from ~73% baseline routing accuracy to 99.10% post-RLCD accuracy alongside
  a 0.83% Expected Calibration Error (ECE) on the held-out test split, and sets
  up the next phase of multi-model, multi-primitive generalization. Built on the
  `humanitarians` palette (`#F0EAD6` ground) with `ClaudeComposerAsk`,
  `BrutalistHesitantWriterSq`, `ClaudeDefinitions`, `NikBearBrownTerminalAsk`,
  and `ClaudeTitleOutro`, narrated in Kokoro `af_bella` (Kore). 16:9 cut (1:00,
  5 beats).
- `2026-10-12-agnostic-calibration-benchmarks/` — Fine-Tuning Platform: Agnostic
  Model/Dataset Architecture & Multi-Dataset Calibration Benchmarks. An
  AI-explainer report reel sourced from the Week 4 engineering and benchmark
  report (`work_report.md`) covering automatic schema inference in
  `rlcd/processing.py` (`auto_prepare_dataset()` mapping arbitrary Hugging Face
  datasets into `choice`, `noul`, and `score` primitives) and unified model
  loading in `rlcd/models.py` (`MarkerDecisionModelWrapper` across `Laya`,
  `Von`, `OpenDecision`, `Typical`, and `Decision1`). Summarizes the 8-run
  empirical benchmark on Kaggle 2× T4 GPUs (DDP) testing `Typical-small` (~150M)
  and `Decision 1.0` (600M) across `lmsys/toxic-chat`, `mteb/tweet_sentiment`,
  `Anthropic/hh-rlhf`, and `NexusRaven_API_eval`—where Brier score improved in
  8/8 runs and ECE dropped in 7/8 runs—and diagnoses why causal backbones hit an
  accuracy bottleneck under a uniform bidirectional marker head and why sharp
  3-class accuracy gains can spike ECE. Built on the `claude` palette with
  `ClaudeComposerAsk`, `BrutalistHesitantWriter`, `SkillTeardownPipeline`,
  `BarChart`, `ClaudeDefinitions`, `ClaudeVerdictArtifact`, and
  `TitleRestateOutro`, narrated in Kokoro `af_bella` (Bella). 16:9 master cut
  (2:13, 8 beats).
- `2026-10-19-post-hoc-calibration-agent-sdk/` — Fine-Tuning Platform: Post-Hoc
  Calibration Bake-Off & Autonomous Agent SDK/Skill Packaging. An AI-explainer
  report reel sourced from the Week 5 engineering and validation report
  (`work_report.md`) resolving the multi-class post-training ECE spikes
  identified in Week 4 and packaging the platform for autonomous agent use.
  Covers the automated 4-strategy Post-Hoc Calibration Bake-Off (`Raw Logits`,
  `Temperature Scaling`, `Platt / Vector Scaling`, and `Matrix Scaling` via
  smooth log-space L-BFGS) that slashed ECE by an average of 73%—bringing
  `wfzyx/von` Tweet Sentiment (`17.24% → 4.85%`), `wfzyx/von` Anthropic RLHF
  (`18.46% → 4.92%`), and `Decision 1.0` Tweet Sentiment (`17.38% → 4.76%`) all
  below 5% in under 2 seconds on CPU while preserving 100% of fine-tuned
  accuracy—and explains why Platt vector scaling wins on 3-class sentiment while
  scalar temperature scaling wins on symmetric pairwise RLHF. Also documents the
  installable Python SDK (`rlcd`), CLI (`rlcd-fine-tune`), and agent skill
  (`skills/rlcd-fine-tune/SKILL.md`), verified end-to-end by an isolated AI
  agent across a 3-phase GPU test suite with zero human code edits. Built on the
  `claude` palette with `ClaudeComposerAsk`, `BrutalistHesitantWriter`,
  `SkillTeardownPipeline`, `BarChart`, `ClaudeDefinitions`,
  `ClaudeVerdictArtifact`, and `TitleRestateOutro`, narrated in Kokoro
  `af_bella` (Bella). 16:9 master cut (2:29, 8 beats).
- `2026-10-26-vla-adversarial-attack-research/` — Security & Exploitation in Physical AI: Stealthy Trajectory Steering & Spatial Consistency Verification
  in VLA Models. A Week 6 research exploration and experimental design report
  (`work_report.md`) under the Security & Exploitation vertical, extending
  Verifiable Machine Learning principles to Vision–Language–Action (VLA) robot
  foundation models (`OpenVLA-7B` in `LIBERO`). Surveys 23 recent papers
  (2024–2026) to identify why existing test-time visual patches only cause
  untargeted freezing/task failure rather than smooth multi-step steering, and
  finalizes a two-hypothesis, two-engineer experimental plan incorporating peer
  feedback from Dev: (1) Hypothesis 1 compares two coordinate-free 3D coaster
  attacks—Way 1 ("The Attention Magnet Patch" hijacking `Llama-2` text-to-image
  cross-attention) and Way 2 ("The Auto-Feature Copy Patch" using the ~3–4 GB
  VRAM Vision-Encoder Shortcut)—against _TMA_ and _EDPA_ baselines, and (2)
  Hypothesis 2 compares Random 5-View Masking against a Systematic $3 \times 3$
  Covering Grid with a Two-Round Minority Check (extending _PatchCleanser_ to
  closed-loop visuomotor control).

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
