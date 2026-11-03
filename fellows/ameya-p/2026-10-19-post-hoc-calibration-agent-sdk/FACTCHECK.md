# FACTCHECK — 2026-10-19-post-hoc-calibration-agent-sdk (Fine-Tuning Platform)

Every claim the narration makes, mapped to the source document:
`work_report.md`
("Fine-Tuning Platform: Post-Hoc Calibration Bake-Off & Autonomous Agent SDK/Skill Packaging").

## B00 — Cold open

- **"Last week we saw that sharp accuracy gains on multi-class tasks could occasionally trigger post-training calibration spikes."**
  Source §1: "Following last week's finding that sharp multi-class accuracy gains during fine-tuning can occasionally trigger Expected Calibration Error (ECE) spikes on subjective tasks..."
- **"Can we automatically eliminate post-training overconfidence, and can an AI agent run the entire fine-tuning platform on its own?"**
  Source §1 objectives 1 & 2: engineering an automated Post-Hoc Calibration Bake-Off module (`training.py`, `helper.py`, `run_post_hoc_calibration.py`) and packaging the platform into an installable Python SDK (`rlcd`), CLI (`rlcd-fine-tune`), and autonomous agent skill (`skills/rlcd-fine-tune/SKILL.md`).

## B01 — BLUF

- **"By adding an automated post-hoc calibration tournament at the end of training, we cut calibration error by 73% in under 2 seconds on CPU while keeping 100% of our fine-tuned accuracy—and packaged the whole workflow into a single skill any agent can run."**
  Source §2 ("Bake-Off Results Across Subjective Tasks"): "Every single task had its ECE slashed from ~17%–18% down below 5% (an average 73% reduction in calibration error) in under 2 seconds on CPU while preserving 100% of fine-tuned accuracy." Source §3: packaged into `rlcd`, `rlcd-fine-tune`, and `skills/rlcd-fine-tune/SKILL.md`.

## B02 — Automated Post-Hoc Calibration Bake-Off

- **"Right after fine-tuning, RLTrainer evaluates four candidate calibrators on the held-out calibration split: raw logits, temperature scaling, Platt vector scaling, and matrix scaling."**
  Source §2: "After fine-tuning, the pipeline automatically evaluates candidate post-hoc calibrators on the held-out calibration split—comparing Baseline (Raw Logits), Temperature Scaling (Softmax(z / T)), Platt / Vector Scaling (Softmax(A * z + b)), and Matrix Scaling (Softmax(W * z + b))—and saves the winning calibrator (`calibrator.pt`) based on validation ECE and Brier score."
- **"Smooth log-space L-BFGS finds the optimum without hitting hard clamp boundaries, and saves the winner to calibrator.pt."**
  Source §2: "Smooth Log-Space L-BFGS Optimization: Parameterized temperature T in [T_min, T_max] smoothly in unconstrained space so L-BFGS optimization never steps into a zero-gradient hard clamp boundary."

## B03 — Bake-Off Results Across Subjective Tasks

- **"On Von tweet sentiment, Von Anthropic RLHF, and Decision 1.0 tweet sentiment, post-hoc calibration slashed ECE from around 18% down below 5% every single time."**
  Source §2 table:
  - `wfzyx/von` — Tweet Sentiment (26K, 3-Class `choice`): Raw ECE `17.24% -> 4.85%` (-12.39%), accuracy preserved at `80.53%`.
  - `wfzyx/von` — Anthropic RLHF (60K, Pairwise `noul`): Raw ECE `18.46% -> 4.92%` (-13.54%), accuracy preserved at `62.03%`.
  - `Decision 1.0 (600M)` — Tweet Sentiment (26K, 3-Class `choice`): Raw ECE `17.38% -> 4.76%` (-12.62%), accuracy preserved at `79.50%`.
  Values on the bar chart are rounded to the nearest integer (`17 -> 5`, `18 -> 5`, `17 -> 5`).

## B04 — Why Different Calibrators Won

- **"Platt vector scaling won on 3-class sentiment by correcting class-prior imbalances, while single-parameter temperature scaling won on pairwise RLHF by softening confidence without breaking binary symmetry."**
  Source §2 ("Why Different Strategies Won"): "Platt / Vector Scaling won on 3-Class Sentiment (`Von` ECE 17.24% -> 4.85%; `Decision 1.0` ECE 17.38% -> 4.76%) by correcting class-prior imbalances, whereas Temperature Scaling (T* = 1.85) won on Pairwise Anthropic RLHF (`Von` ECE 18.46% -> 4.92%) by softening overconfidence while preserving binary choice symmetry."

## B05 — Autonomous Agent SDK & Skill Verification

- **"Packaged the entire codebase into the installable rlcd Python SDK, the rlcd-fine-tune CLI, and a plug-and-play agent skill. In autonomous testing, an isolated AI agent read SKILL.md and passed all three verification phases on local GPU hardware with zero human edits."**
  Source §3: "Validated the SDK + skill package by having an isolated AI agent autonomously read `SKILL.md` and execute a 3-phase verification suite on local GPU hardware without human intervention or code edits—passing all smoke tests (Phase 1), default `xLAM` tool-selection fine-tuning (Phase 2), and blind multi-primitive runs across `choice`, `noul`, and `score` datasets with automatic post-hoc calibration (Phase 3)."

## B06 — Your Turn Handoff

- Suggested prompt for the viewer to point an agent at `skills/rlcd-fine-tune/SKILL.md` and run `rlcd-fine-tune` on a dataset.

## B07 — Outro

- Title restate only (`week5 (Oct 19).` / `Fine-Tuning Platform`).
