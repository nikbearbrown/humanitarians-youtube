# Friction Log: Week 5 — Post-Hoc Calibration Bake-Off & Autonomous Agent SDK/Skill Packaging

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Report:** [Work Report](work_report.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Oct 19 to Oct 25, 2026

---

## 1. Focus of the week

- Engineering an automated **Post-Hoc Calibration Bake-Off** module directly inside the training pipeline (`training.py`, `helper.py`, `run_post_hoc_calibration.py`) to eliminate post-fine-tuning multi-class and pairwise overconfidence ("red ECE rows" from Week 4) without sacrificing accuracy or requiring GPU retraining.
- Evaluating four candidate calibrators on the held-out calibration split:
  - Baseline (Raw Logits): $\text{Softmax}(z)$
  - Temperature Scaling: $\text{Softmax}(z / T)$
  - Platt / Vector Scaling: $\text{Softmax}(A \cdot z + b)$
  - Matrix Scaling: $\text{Softmax}(W \cdot z + b)$
- Packaging the entire RLCD platform into an installable **Python SDK (`rlcd`)**, **CLI entry point (`rlcd-fine-tune`)**, and **autonomous AI agent skill (`skills/rlcd-fine-tune/SKILL.md`)**.
- Executing a 3-phase end-to-end autonomous agent verification suite (`tests/test_agent.md`, `results/SDK_agent_testing_report.md`) on local GPU hardware.
- Producing the 8-beat Week 5 explainer reel (`2026-10-19-post-hoc-calibration-agent-sdk`, `2:29` 4K master cut, Kokoro `af_bella` narration).

## 2. What was tried, and what was expected

- **Single post-hoc temperature scalar.** Expectation: fitting a single scalar temperature $T$ after training would suffice to bring Expected Calibration Error (ECE) below $5\%$ across all subjective multi-class and pairwise tasks.
- **Clamped L-BFGS optimization.** Expectation: bounding temperature $T \in [T_{\min}, T_{\max}]$ via a hard clamp during L-BFGS optimization would converge cleanly.
- **Matrix scaling on 3-class sentiment.** Expectation: full Matrix Scaling ($12$ parameters for 3 classes) would outperform simpler diagonal vector scaling because of its higher expressiveness.
- **Autonomous agent execution from `SKILL.md`.** Expectation: an isolated AI agent reading `skills/rlcd-fine-tune/SKILL.md` would be able to run smoke tests, fine-tune on `xLAM`, and calibrate multi-primitive datasets without human code edits.

## 3. Points of resistance, and next steps taken

### Scalar temperature scaling could not fix class-prior imbalances on 3-class sentiment
- On 3-class `mteb/tweet_sentiment`, single-parameter Temperature Scaling reduced raw ECE only partially—from $17.24\% \to 11.82\%$ on `wfzyx/von` ($T = 1.34$) and from $17.38\% \to 11.45\%$ on `Decision 1.0` ($T = 1.36$)—still well above the $<5\%$ target.
- Meanwhile, full Matrix Scaling ($12$ parameters) overfitted the validation calibration split ($17.24\% \to 9.75\%$ ECE).
- **Next step:** built an automated multi-strategy tournament that evaluates Raw Logits, Temperature Scaling, Platt/Vector Scaling, and Matrix Scaling on the held-out calibration split and selects the winner (`calibrator.pt`) by validation ECE and Brier score.
- **Result:** **Platt / Vector Scaling** ($6$ parameters, $\text{Softmax}(A \cdot z + b)$) won on 3-class sentiment by correcting per-class bias and scale, slashing ECE from $17.24\% \to \mathbf{4.85\%}$ on `Von` ($-72\%$) and from $17.38\% \to \mathbf{4.76\%}$ on `Decision 1.0` ($-73\%$) while preserving $100\%$ of fine-tuned accuracy ($80.53\%$ and $79.50\%$). Conversely, **Temperature Scaling** ($T^* = 1.85$) won on symmetric pairwise `Anthropic/hh-rlhf` (`noul`), slashing `Von` ECE from $18.46\% \to \mathbf{4.92\%}$ ($-73\%$) at $62.03\%$ accuracy.

### L-BFGS zero-gradient stalls at hard clamp boundaries
- Hard-clamping $T$ into $[T_{\min}, T_{\max}]$ inside the optimization step caused L-BFGS line searches to step into flat zero-gradient regions whenever initial logits were sharply peaked.
- **Next step:** re-parameterized temperature smoothly in unconstrained log/sigmoid space over $[T_{\min}, T_{\max}]$ so L-BFGS always receives smooth, non-zero gradients and converges in under 2 seconds on CPU.

### Packaging for zero-touch autonomous agent execution
- Early scripts required manual imports and dataset-specific configuration flags that an external coding agent could easily misconfigure when handed an unseen dataset.
- **Next step:** consolidated all 32 training, model, schema, and calibration parameters into `rlcd.fine_tune()` (`__init__.py`) and the `rlcd-fine-tune` CLI (`pyproject.toml`), and documented exact dataset-inspection, `column_map` override, and artifact-verification protocols (`model.safetensors`, `calibrator.pt`, `test_evaluation_metrics.json`) in `skills/rlcd-fine-tune/SKILL.md`.

## 4. AI and other contributions: accepted, changed, rejected

### Autonomous Test Agent (`tests/test_agent.md`)
- **Accepted:** Used an isolated AI agent to validate `skills/rlcd-fine-tune/SKILL.md` end-to-end across three phases without human intervention: Phase 1 (smoke tests), Phase 2 (default `xLAM` tool-selection fine-tuning), and Phase 3 (blind multi-primitive runs across `choice`, `noul`, and `score` with automatic post-hoc calibration).

### Claude / Brutalist Toolkit
- **Accepted:** Built the 8-beat Week 5 explainer reel (`148.9s` / `2:29` 4K master cut) using `ClaudeComposerAsk`, `BrutalistHesitantWriter`, `SkillTeardownPipeline`, `BarChart`, `ClaudeDefinitions`, `ClaudeVerdictArtifact`, and `TitleRestateOutro` with Kokoro `af_bella` narration (`GATE T` 8/8 PASS, 0 FAILs).

## 5. Understood now, and still unresolved

### Understood
- **Calibration strategy must match decision structure:** symmetric pairwise preference tasks (`noul`) only need a single scalar temperature $T$ to soften confidence while preserving pair symmetry, whereas multi-class subjective tasks (`choice`) require per-class vector scaling ($A \cdot z + b$) to absorb class-prior shifts.
- **In-loop RLCD + post-hoc tournament is complementary:** in-loop Brier RL shapes the encoder representations and prevents catastrophic overconfidence during training, while the $<2\text{s}$ CPU post-hoc calibration tournament guarantees sub-$5\%$ final ECE without sacrificing accuracy.

### Unresolved
- **Final project wrap-up:** final polish and packaging review for end-of-fellowship delivery.
