# Humanitarians AI — Final Capstone Summary Video Script (Week 6)

**Project:** Autonomous Fine-Tuning Pipeline for Pure Decision Models (RLCD Strategy 1)  
**Fellow:** Priya Adlakha (in collaboration with Ameya Padwad, mentored by Prof. Nik Bear Brown & Dev Shah)  
**Speaker Voice:** Bella (`af_bella` — Kokoro TTS)  
**Visual Theme:** Canonical Brutalist Cream (`#F4EFEA`), Espresso Ink (`#2A241D`), Terracotta Accent (`#D97757`)  
**Resolution:** 1080p (1920x1080) | 30 FPS  
**Target Duration:** ~3.5 to 4.0 Minutes (Comprehensive Capstone Walkthrough)  
**Artifact Link:** `https://priya413.substack.com/p/your-model-got-more-accurate-after`  
**Autonomous Agent Skill:** `skills/rlcd-fine-tune/SKILL.md`

---

## Visual & Slide Asset Mapping

| Scene | Primary On-Screen Graphic Asset | Secondary Badges / Cards |
| :--- | :--- | :--- |
| **Scene 1** | Brutalist Title Card + Substack Article Header | `@HumanitariansAI` • `Final Capstone` • `RLCD Strategy 1` |
| **Scene 2** | `pipeline_concept_workflow.png` (Doodle Pipeline Workflow) | `Any Format (Any Domain)` • `Bidirectional Decision Models` |
| **Scene 3** | `model_dataset_pairing_matrix.png` (Model-Dataset Pairing Matrix) | `Laya 421M` • `Von ~150M` • `Decision 1.0 600M` |
| **Scene 4** | `baseline_only_benchmark_results.png` (Pre-Training Baseline Scorecard) | `Coin-Flip Baselines` • `Zero-Shot Evaluation` |
| **Scene 5** | `clean_7col_benchmark_results.png` (Initial Post-Training Scorecard) | `Accuracy Surges (+14% to +93%)` • `*Red ECE Spikes (~17%-18%)` |
| **Scene 6** | `cross_entropy_code_snippet.png` (Cross-Entropy Logit-Pushing Code) | `Math Root Cause: -log(p)` • `Logits -> +Infinity` |
| **Scene 7** | `post_calibration_bakeoff_perfect.png` (Post-Hoc Calibration Bake-Off) | `Platt/Vector Scaling (A·z+b)` • `Temperature Scaling (T)` |
| **Scene 8** | `final_complete_benchmark_calibrated.png` (Before vs After Scorecard) | `3 Rescued Rows Frame` • `Sub-5% ECE Across All 8 Rows` |
| **Scene 9** | `loss_function_decision_matrix.png` & `model_capacity_vs_loss_heuristics.png` | `The Softening Rule` • `Baseline Preservation Rule` |
| **Scene 10** | `skills/rlcd-fine-tune/SKILL.md` UI Mockup + Substack Live Link Card | `Autonomous Agent Skill` • `https://priya413.substack.com` |

---

### Scene 1: The Central Research Paradox (~25s)

- **On-Screen Visuals:**
  - Background: Canonical Brutalist Warm Cream (`#F4EFEA`) with crisp hairline borders (`#2A241D`).
  - Top Badge: Terracotta Pill Badge (`#D97757` text on `#FCEEE9`): `@HumanitariansAI Fellowship • Final Capstone Summary`.
  - Main Headline (Serif): **Your Model Got More Accurate After Fine-Tuning.**
  - Sub-Headline (Italic): *"Can you actually trust its confidence?"*
  - Lower Right Callout Card: Thumbnail of published Substack article with live URL badge: `priya413.substack.com`.
- **Narration (Bella):**
  > "Welcome to the final capstone summary of our Humanitarians AI fellowship. Over the past six weeks, in partnership with Ameya Padwad and under the guidance of Professor Nik Bear Brown and Dev Shah, we set out to build a generalized, model-agnostic fine-tuning pipeline for pure decision models. But as our models began learning, our benchmarks revealed a critical paradox: a model can achieve massive double-digit accuracy gains, while simultaneously becoming completely untrustworthy about when it is right and when it is wrong."

---

### Scene 2: Designing a Generalized Decision Pipeline (~25s)

- **On-Screen Visuals:**
  - Display: `pipeline_concept_workflow.png` centered on screen with subtle drop shadow.
  - Highlight Overlays: Pulsing callouts over the three core modules:
    - 1. *Universal Dataset Ingestion:* Any tabular schema $\to$ Auto-inferred to `choice`, `score`, or `noul` primitives.
    - 2. *Bidirectional Model Wrapper:* Simultaneous candidate scoring via marker tokens (`[MASK]`).
    - 3. *RLCD Strategy 1 Training Loop:* Negative Brier score reward optimization.
- **Narration (Bella):**
  > "Unlike generative chatbots that generate tokens sequentially, pure decision architectures evaluate all candidate choices simultaneously in a single forward pass using bidirectional marker representations. We engineered an autonomous pipeline that takes any dataset—whether function calling, medical triage, or toxicity moderation—and automatically maps it into one of three core decision primitives: discrete choice, continuous scoring, or pairwise ranking, training under a calibrated negative Brier score reward."

---

### Scene 3: The Empirical Benchmark Matrix (~20s)

- **On-Screen Visuals:**
  - Display: `model_dataset_pairing_matrix.png` filling the screen.
  - Card Highlights:
    - Left Column: Diverse open-weight decision backbones: `Laya (421M ModernBERT Large)`, `Von (~150M dedicated decision)`, and `Decision 1.0 (600M Lex backbone)`.
    - Right Column: 5 diverse datasets spanning 60,000 function-calling schemas, emergency clinical triage, multi-class tweet sentiment, safety moderation, and Anthropic RLHF human preference pairs.
- **Narration (Bella):**
  > "To rigorously prove model and data agnosticism, we evaluated three open-weight decision backbones across five distinct task domains on cloud GPUs. We paired ModernBERT Large in Laya at 421 million parameters, the lightweight Von model at 150 million parameters, and the 600-million parameter Decision 1.0 architecture against 60,000 function-calling queries, moderation ratings, and nuanced human preferences."

---

### Scene 4: The Pre-Training Baseline (~20s)

- **On-Screen Visuals:**
  - Display: `baseline_only_benchmark_results.png` (Clean 4-column pre-training scorecard).
  - Visual Indicators:
    - Gray text highlighting near-random baselines:
      - Von on Toxic-Chat: **1.28%** baseline accuracy.
      - Decision 1.0 on Toxic-Chat: **9.65%** baseline accuracy.
      - NexusRaven: **15.87%** to **25.40%** baseline accuracy.
      - Anthropic RLHF: **49.03%** (Pure coin-flip baseline).
- **Narration (Bella):**
  > "Before fine-tuning, zero-shot decision models struggle severely on specialized schemas. Toxic-chat baseline accuracy sat at just 1.28% on Von and 9.6% on Decision 1.0, while complex Python API code extraction hovered below 26%, and pairwise preference ranking performed no better than a random coin flip."

---

### Scene 5: The Post-Training Surprise: The Calibration Spike (~30s)

- **On-Screen Visuals:**
  - Display: `clean_7col_benchmark_results.png` (The initial 7-column post-training scorecard).
  - Left Visual Cue: Vibrant green callouts on Accuracy Gains:
    - **+93.60%** on Toxic-Chat (surging to 94.88%).
    - **+65.08%** on NexusRaven (surging to 80.95%).
    - **+35.19%** on Tweet Sentiment (surging to 80.53%).
  - Right Visual Cue (The Drama): Coral red callouts with red exclamation badges on Final ECE:
    - Row 4 (Tweet Sentiment): **17.24%* ECE** (Red).
    - Row 5 (Anthropic RLHF): **18.46%* ECE** (Red).
    - Row 7 (Decision 1.0 on Tweet Sentiment): **17.38%* ECE** (Red).
- **Narration (Bella):**
  > "After fine-tuning, the accuracy numbers were staggering. Accuracy leaped by over 93% on toxic chat and over 65% on NexusRaven. But look closely at the Expected Calibration Error on rows 4, 5, and 7. On sentiment routing and human preference ranking, calibration error exploded to over 17% and 18%. While the models were getting substantially more answers right, they had transformed into confident bluffers—boasting near-100% certainty on highly ambiguous edge cases."

---

### Scene 6: The Mathematical Diagnosis: Cross-Entropy Logit Pushing (~25s)

- **On-Screen Visuals:**
  - Display: `cross_entropy_code_snippet.png` showing lines 199–206 of `training.py`.
  - Math Callout Box:
    $$\mathcal{L}_{\text{CE}} = -\sum y_i \log p_i \quad \Longrightarrow \quad z_i \longrightarrow +\infty$$
  - Diagram: Highlighting how target vectors `[1.0, 0.0, 0.0]` force logits to extreme positive values, clashing with natural annotator ambiguity (e.g., subjective sentiment where true human consensus is split 60/40).
- **Narration (Bella):**
  > "Why did this happen? The mathematical culprit was standard Cross-Entropy loss. Because Cross-Entropy minimizes negative log probability, the optimizer can only drive training loss toward zero by pushing output logits toward positive infinity. When training on subjective human annotations with hard one-hot targets, the model is penalized for acknowledging ambiguity, forcing it to output 99% certainty on subjective boundary cases."

---

### Scene 7: The Solution: Post-Hoc Calibration Engine (~25s)

- **On-Screen Visuals:**
  - Display: `post_calibration_bakeoff_perfect.png` (The empirical post-hoc comparison scorecard).
  - Comparison Cards:
    - *Baseline:* 9.49% ECE | Brier: -0.6059.
    - *Temperature Scaling ($T=1.34$):* Fast scalar adjustment preserving accuracy and antisymmetry.
    - *Platt / Vector Scaling ($A \cdot z + b$):* **5.29% ECE** (Cut by 44%) | **Brier: -0.5189** (Winner for multi-class choice).
    - *Matrix Scaling ($W \cdot z + b$):* Risk of over-parameterization on modest validation samples.
- **Narration (Bella):**
  > "Rather than discarding the models or initiating expensive training reruns, we engineered a post-hoc calibration engine. We ran an empirical bake-off comparing Temperature Scaling, Platt Vector Scaling, and Matrix Scaling. For multi-class choice tasks, 6-parameter Platt Vector Scaling emerged as the clear winner—cutting calibration error by 44% and significantly improving proper Brier scores in just 70 milliseconds."

---

### Scene 8: The Capstone Scorecard: Before vs. After Calibration (~30s)

- **On-Screen Visuals:**
  - Display: `final_complete_benchmark_calibrated.png` (The 8-row capstone scorecard).
  - Visual Focus: Clean red rectangular bounding boxes framing Rows 4, 5, and 7:
    - *Row 4 (Von on Tweet Sentiment):* Raw ECE **17.24%* $\longrightarrow$ 4.85%** (Slashed by 72%).
    - *Row 5 (Von on Anthropic RLHF):* Raw ECE **18.46%* $\longrightarrow$ 4.92%** (Slashed by 73%).
    - *Row 7 (Decision 1.0 on Tweet Sentiment):* Raw ECE **17.38%* $\longrightarrow$ 4.76%** (Slashed by 73%).
  - Bottom Callout: Every single benchmarked task now operates with **sub-5% ECE** and **100% preserved accuracy**.
- **Narration (Bella):**
  > "Here is our complete before-and-after capstone scorecard. Notice the three red-framed rows. Through post-hoc scaling, Von's sentiment calibration error dropped from 17.2% to 4.85%. On Anthropic RLHF, Temperature Scaling cut ECE from 18.5% down to 4.92%. And Decision 1.0 dropped from 17.4% to 4.76%—slashing overconfidence by more than 70% while keeping every single percent of accuracy completely intact."

---

### Scene 9: Architectural Heuristics & Rules of Thumb (~25s)

- **On-Screen Visuals:**
  - Display: Side-by-side view of `loss_function_decision_matrix.png` and `model_capacity_vs_loss_heuristics.png`.
  - Highlighted Takeaways:
    - *Rule 1 (The Softening Rule):* High-capacity models (400M–600M+) need Label Smoothing or Brier scoring to physically block logits from driving to infinity.
    - *Rule 2 (Baseline Preservation):* Lightweight edge models (~150M) risk capacity collapse under Focal Loss; preserve majority baselines first.
    - *Rule 3 (Post-Hoc Efficiency):* Edge models calibrate on CPU in seconds with zero deployment footprint.
- **Narration (Bella):**
  > "From these findings, we synthesized two foundational engineering heuristics: First, the Softening Rule for high-capacity models—use target regularization like Label Smoothing to physically prevent parameter headroom from causing overconfidence bluffing. And second, the Baseline Preservation Rule for edge models—protect compact 150M architectures from capacity collapse by securing majority baselines first, then resolving residual calibration errors post-hoc."

---

### Scene 10: Packaging the Pipeline & Read the Full Article (~20s)

- **On-Screen Visuals:**
  - Split-Screen Display:
    - Left Card: `skills/rlcd-fine-tune/SKILL.md` repository file preview with agent workflow execution diagram.
    - Right Card: Clean editorial preview of the published Substack article:
      - Title: **"Your Model Got More Accurate after Fine-tuning. Can You Trust Its Confidence?"**
      - Direct Link Pill Badge: `priya413.substack.com/p/your-model-got-more-accurate-after`
  - Footer: `Humanitarians AI • Northeastern University • Open-Source Release`
- **Narration (Bella):**
  > "To ensure complete reproducibility, we packaged the entire pipeline into an autonomous AI agent skill under `skills/rlcd-fine-tune/SKILL.md`, enabling autonomous agents to execute, benchmark, and calibrate decision models end-to-end. Our complete technical write-up, mathematical proofs, and interactive code are now live on Substack. Check out the link below, and thank you for supporting Humanitarians AI!"

---

## Audio Production Checklist (Kokoro TTS)

1. **TTS Voice Model:** `af_bella` (Kokoro v0.19 ONNX / PyTorch)
2. **Speed Multiplier:** `1.05x` (natural conversational cadence)
3. **Audio File Destinations:**
   - Script File: `/Users/priyaadlakha/Desktop/fine-tuning-model/video_script_week6_final_summary.md`
   - Fellowship Repo Copy: `/Users/priyaadlakha/projects/humanitarians-youtube/fellows/priya-a/2026-10-23-final-capstone-and-substack-publication/video_script.md`
