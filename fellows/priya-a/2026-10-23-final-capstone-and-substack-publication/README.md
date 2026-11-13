# Week 6: Master Capstone, Post-Hoc Calibration & Substack Publication (2026-10-19 to 2026-10-23)

**Fellow:** Priya Adlakha  
**Mentors:** Prof. Nik Bear Brown, Dev Shah  
**Branch:** `priya-a` | **PR:** #232 (`nikbearbrown/humanitarians-youtube`)  
**Weekly Hours:** 20.0 hours (Completed)

---

## Executive Summary & Milestones

Week 6 represents the culmination of the month-one Humanitarians AI fellowship research program on generalized fine-tuning for pure decision models (RLCD Strategy 1 — Negative Brier Score Reward). The primary focus was resolving post-training calibration divergence (Cross-Entropy overconfidence), conducting head-to-head post-hoc scaling experiments, verifying pipeline agnosticism across model architectures and data schemas, packaging the workflow into an autonomous AI agent skill (`skills/rlcd-fine-tune/SKILL.md`), and publishing the comprehensive technical article on Substack.

- **Published Technical Article:** [Your Model Got More Accurate after Fine-tuning. Can You Trust Its Confidence?](https://priya413.substack.com/p/your-model-got-more-accurate-after)
- **Autonomous Agent Skill:** [`skills/rlcd-fine-tune/SKILL.md`](https://github.com/AmeyaPadwad/fine_tuner/blob/SDK%2Bskill/skills/rlcd-fine-tune/SKILL.md)
- **Post-Hoc Calibration Engine:** `rlcd/run_post_hoc_calibration.py` (L-BFGS Temperature, Platt/Vector, and Matrix Scaling)
- **Month-One Fellowship Renewal Report:** [`fellows/priya-a/renewal-requests/2026-10-22-renewal-request.md`](../renewal-requests/2026-10-22-renewal-request.md)

---

## Weekly Hour Log Breakdown (20.0 Hours Total)

### 1. Collaborative Architecture Sync & Code Review with Ameya Padwad (1.0 hr)
- Sync calls to coordinate modular SDK packaging on the `SDK+skill` branch:
  - Reviewed the decoupled directory architecture separating model wrappers (`models.py`), auto-preprocessing schema inference (`processing.py`), and the core training loop (`training.py`).
  - Aligned on the implementation and testing of the autonomous AI agent skill (`skills/rlcd-fine-tune/SKILL.md`), ensuring that agents can autonomously trigger decision model fine-tuning with objective verification criteria.
  - Coordinated git hygiene and non-destructive PR management across `AmeyaPadwad/fine_tuner`, `adlakhapriya95/humanitarians-ai-volunteer`, and `humanitarians-youtube`.

### 2. Brutalist Video Setup, Narration & Asset Configuration (1.0 hr)
- Configured the Brutalist video generation framework for the final capstone summary:
  - Formatted 1080p slide layouts in canonical Brutalist warm cream (`#F4EFEA`), espresso ink (`#2A241D`), and terracotta accent (`#D97757`).
  - Integrated all newly generated benchmark graphics, architectural decision matrices, and post-hoc calibration comparisons into timecoded presentation scenes.
  - Generated narration audio using Kokoro TTS (`af_bella` voice) and embedded direct call-to-actions linking to the published Substack article and autonomous agent skill.

### 3. Model & Data Agnosticism Pipeline Testing & Bug Fixing (2.0 hrs)
- Executed rigorous end-to-end tests across decision backbones and task primitives:
  - *Smoke Test Suite Verification:* Ran `smoke_tests.py --all` across helper utilities, model wrappers, preprocessing adapters, and training steps on local CPU with 100% pass rate.
  - *Hardware Portability:* Tested `main.py` CLI dynamic device selection (`--device cpu` / `--device cuda`) on Apple Silicon and Linux environments, confirming batch loops execute without assertion crashes.
  - *Data Primitive Validation:* Verified schema auto-inference across all three task primitives:
    - `choice`: Function calling, tool routing, 3-class sentiment.
    - `score`: Safety moderation, toxicity probability.
    - `noul`: Pairwise preference ranking (Anthropic RLHF).
  - *Mini Pipeline End-to-End Test:* Ran full training and calibration on `wfzyx/von` with `NexusRaven` (318 rows) on CPU: baseline Acc 26.98% surged to **77.78%** (+50.79%), Brier improved by +0.3770, and post-hoc temperature calibration fitted in 0.16s ($T=0.501$).

### 4. Capstone Technical Article: Research, Graphics, Fact-Checking & Substack Publication (16.0 hrs)
- Dedicated the primary focus of the week to comprehensive technical writing, empirical calibration experiments, graphic asset production, editorial fact-checking, and publishing the capstone fellowship article:
  - *Mathematical Root Cause Analysis & Empirical Discovery:*
    - Formulated the fundamental question of the fellowship: *Can a model get more accurate while becoming worse at knowing when to trust its decisions?*
    - Diagnosed why Expected Calibration Error (ECE) widened on subjective tasks (Tweet Sentiment and Anthropic RLHF) despite massive accuracy surges (+32% to +35%): standard Cross-Entropy loss ($-\log p$) drives output logits toward $+\infty$ on hard one-hot targets (`[1.0, 0.0, 0.0]`), conflicting with natural annotator ambiguity.
  - *Post-Hoc Calibration Engine & Empirical Bake-Off:*
    - Developed a standalone, reproducible post-hoc calibration engine (`rlcd/run_post_hoc_calibration.py`) supporting Temperature Scaling, Platt/Vector Scaling, and Matrix Scaling with L-BFGS optimization.
    - Executed an empirical bake-off on held-out calibration splits:
      - *Platt / Vector Scaling ($A \cdot z + b$):* Won on multi-class choice tasks, cutting ECE from $9.49\% \to 5.29\%$ (44% reduction) and improving Brier score from $-0.6059 \to -0.5189$.
      - *Temperature Scaling ($T^*$):* Proved mathematically optimal for pairwise preference tasks (Anthropic RLHF), preserving logit antisymmetry without introducing positional bias.
  - *Rescuing the Three Subjective Failure Rows:*
    - *Row 4 (`Von` on Tweet Sentiment):* Slashed ECE from $17.24\%^* \to \mathbf{4.85\%}$ (72% reduction) via Platt/Vector Scaling while keeping 80.53% accuracy 100% invariant.
    - *Row 5 (`Von` on Anthropic RLHF):* Slashed ECE from $18.46\%^* \to \mathbf{4.92\%}$ (73% reduction) via Temperature Scaling ($T=1.85$) while keeping 62.03% accuracy 100% invariant.
    - *Row 7 (`Decision 1.0` on Tweet Sentiment):* Slashed ECE from $17.38\%^* \to \mathbf{4.76\%}$ (73% reduction) via Platt/Vector Scaling while keeping 79.50% accuracy 100% invariant.
  - *Publication-Grade Graphic Asset Design:*
    - Restored Priya's original doodle artwork with pixel-level precision into `pipeline_concept_workflow.png`.
    - Synthesized the clean 7-column benchmark scorecard (`clean_7col_benchmark_results.png`) and baseline-only scorecard (`baseline_only_benchmark_results.png`).
    - Rendered the capstone scorecard (`final_complete_benchmark_calibrated.png`) showing all 8 benchmark rows with red highlighted callouts strictly framing the three rescued rows.
    - Created Excel-style Times New Roman reference cards: `loss_function_decision_matrix.png` and `model_capacity_vs_loss_heuristics.png` with zero wasted white space and high-contrast typography.
    - Synthesized Cross-Entropy code screenshot (`cross_entropy_code_snippet.png`) illustrating the exact logit-pushing implementation.
  - *Article Composition, Editorial Fact-Checking & Live Publication:*
    - Authored and polished the long-form technical article maintaining an objective, third-person perspective (strictly omitting first-person pronouns in the technical body).
    - Incorporated inline pedagogical definitions for key machine learning concepts (epoch, mini-batch, gradient, ECE, probability vector).
    - Rigorously fact-checked every empirical number against the 20% held-out test split records across all models (`Laya 421M`, `Von ~150M`, `Decision 1.0 600M`).
    - Published the completed article on Substack at: `https://priya413.substack.com/p/your-model-got-more-accurate-after`.

---

## Verified Benchmark Scorecard (Before vs. After Calibration)

| Model & Architecture | Dataset & Task Domain | Baseline Acc | Final Acc | Acc Gain (Δ) | Raw Fine-Tuned ECE | Final Production ECE | Status / Resolution |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`Laya (421M)`** | **Salesforce xLAM (60K)** | 84.85% | **99.10%** | **+14.25%** | 0.83% | **0.83%** | Direct: Sub-1% calibration out of the box |
| **`Von (~150M)`** | **lmsys/toxic-chat (5K)** | 1.28% | **94.88%** | **+93.60%** | 3.96% | **3.96%** | Direct: Slashed from 22.34% natively |
| **`Von (~150M)`** | **NexusRaven (318)** | 15.87% | **80.95%** | **+65.08%** | 12.00% | **12.00%** | Direct: Slashed from 18.91% natively |
| **`Von (~150M)`** | **Tweet Sentiment (26K)** | 45.34% | **80.53%** | **+35.19%** | **17.24%*** | **4.85%** | **RESCUED:** Platt/Vector Scaling cuts ECE by 72% |
| **`Von (~150M)`** | **Anthropic RLHF (60K)** | 49.03% | **62.03%** | **+13.00%** | **18.46%*** | **4.92%** | **RESCUED:** Temperature Scaling ($T=1.85$) cuts ECE by 73% |
| **`Decision 1.0 (600M)`** | **lmsys/toxic-chat (5K)** | 9.65% | **94.98%** | **+85.33%** | 4.01% | **4.01%** | Direct: Slashed from 14.78% natively |
| **`Decision 1.0 (600M)`** | **Tweet Sentiment (26K)** | 46.54% | **79.50%** | **+32.96%** | **17.38%*** | **4.76%** | **RESCUED:** Platt/Vector Scaling cuts ECE by 73% |
| **`Decision 1.0 (600M)`** | **NexusRaven (318)** | 25.40% | **58.73%** | **+33.33%** | 12.48% | **12.48%** | Direct: Slashed from 17.84% natively |

*Held-out test split: 20% unseen data across all runs.*
