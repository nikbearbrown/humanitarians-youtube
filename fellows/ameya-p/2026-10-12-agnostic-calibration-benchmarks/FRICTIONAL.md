# Friction Log: Week 4 — Agnostic Model/Dataset Architecture & Multi-Dataset Calibration Benchmarks

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Report:** [Work Report](work_report.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Oct 12 to Oct 18, 2026

---

## 1. Focus of the week

- Engineering a dataset-agnostic ingestion module (`rlcd/processing.py`) with `auto_prepare_dataset()` to automatically inspect arbitrary Hugging Face datasets, infer column roles (context, embedded or JSON candidates, target labels), and map records into `choice`, `noul`, or `score` primitives.
- Engineering a model-agnostic loading router (`rlcd/models.py`) supporting `Laya`, `Von`, `OpenDecision`, `Typical`, and `Decision1` via a unified `MarkerDecisionModelWrapper` (`scorer`, `type_emb`, and `act_head`).
- Running an 8-experiment empirical benchmark suite on Kaggle 2× NVIDIA T4 GPUs (DDP) evaluating **Typical-small** (`OzLabs/typical-small`, ~150M Qwen causal backbone) and **Decision 1.0** (`vllm-sr/Decision-1.0-Lex-0.6B`, 600M Lex backbone) across four benchmarks:
  - `lmsys/toxic-chat` (5,082 rows, `score`)
  - `mteb/tweet_sentiment` (26,732 rows, `choice`)
  - `Anthropic/hh-rlhf` (60,000 rows, `noul`)
  - `NexusRaven_API_eval` (318 rows, `choice`)
- Producing the 8-beat Week 4 benchmark explainer reel (`2026-10-12-agnostic-calibration-benchmarks`, `2:13` 4K master cut, Kokoro `af_bella` narration).

## 2. What was tried, and what was expected

- **Automatic schema inference (`auto_prepare_dataset`).** Expectation: heuristic column inspection could classify diverse Hugging Face datasets into `choice`, `noul`, or `score` without per-dataset custom code.
- **Uniform `MarkerDecisionModelWrapper` across architectures.** Expectation: wrapping any open-weight encoder or causal backbone with the same `[MASK]` marker-gathering decision head would yield both accuracy and calibration gains across all four datasets.
- **Simultaneous accuracy, Brier, and ECE improvements.** Expectation: whenever RLCD improved accuracy and Mean Brier Score on a held-out test split, Expected Calibration Error (ECE) would also decrease monotonically.

## 3. Points of resistance, and next steps taken

### Causal vs. bidirectional backbone bottleneck on `Typical-small`
- While `Typical-small` jumped from $0.39\% \to 94.88\%$ accuracy on `lmsys/toxic-chat` (`score`) and cut ECE across all four tasks, its classification accuracy stayed flat on `mteb/tweet_sentiment` ($39.54\% \to 39.54\%$), `Anthropic/hh-rlhf` ($50.21\% \to 49.79\%$), and `NexusRaven_API_eval` ($15.87\% \to 15.87\%$).
- **Diagnosis:** unlike bidirectional masked encoders (`Laya`), `Typical-small` uses a causal Qwen backbone where each option marker token can only attend leftward. Attaching a uniform bidirectional-style `MarkerDecisionModelWrapper` creates a representational bottleneck on multi-option natural language and multi-function code signatures.
- **Interesting finding:** even when `Typical-small` could not improve accuracy on `tweet_sentiment` or `hh-rlhf`, the RLCD Brier reward slashed ECE from $8.63\% \to 0.50\%$ and $4.67\% \to 0.36\%$, teaching the model to output honest $\sim 50\%/50\%$ uncertainty instead of overconfident guesses.
- **Next step:** prioritized architecture-aware decision heads (causal last-token / option-span pooling vs. bidirectional marker gathering).

### Sharp multi-class accuracy gains can spike ECE (`Decision 1.0` on `tweet_sentiment`)
- Across the 8 benchmark runs, Mean Brier Score improved in **8/8 runs** and ECE dropped in **7/8 runs**. The single exception was `Decision 1.0` on 3-class `mteb/tweet_sentiment`, where accuracy surged from $46.54\% \to 79.50\%$ ($+32.96\%$) and Brier score improved strongly ($-0.6357 \to -0.3687$, $+0.2670$), yet ECE rose from $8.04\% \to 17.38\%$.
- **Diagnosis:** during rapid multi-class accuracy improvements on subjective sentiment labels, the cross-entropy component pushes winning class logits higher faster than a single scalar temperature can soften class-specific prior imbalances.
- **Next step:** designed a multi-strategy **Post-Hoc Calibration Bake-Off** (comparing Temperature Scaling, Platt/Vector Scaling, and Matrix Scaling on the held-out calibration split) to eliminate post-training multi-class overconfidence in Week 5.

## 4. AI and other contributions: accepted, changed, rejected

### Claude / Brutalist Toolkit
- **Accepted:** Structured the 8-beat Week 4 reel (`133.1s`) around the empirical contrast between consistent calibration gains (8/8 Brier, 7/8 ECE) and the causal-head bottleneck (`B03` `BarChart`, `B04` `ClaudeDefinitions`, `B05` `ClaudeVerdictArtifact`).
- **Accepted:** Verified all 8 beats through `GATE T` (`TYPECHECK.md`: 0 FAILs) and compiled the clean 4K master cut (`build-state.json`: `status: "ready"`, `duration_s: 133.08`).

## 5. Understood now, and still unresolved

### Understood
- **Brier RLCD reliably regularizes confidence even when capacity is bottlenecked:** 8/8 runs improved Brier score and 7/8 reduced ECE; when a model lacks the head capacity to separate classes, RLCD forces it to admit uncertainty rather than hallucinate high confidence.
- **Readout head geometry must match attention masking:** bidirectional marker gathering works for masked encoders (`Laya`), whereas causal backbones need causal-aware pooling.
- **Brier improvement does not guarantee lower multi-class ECE:** a large jump in classification accuracy can improve overall Brier score while leaving residual class-wise overconfidence on subjective 3-class tasks.

### Unresolved
- **Eliminating the 3-class ECE spike without losing accuracy:** whether vector/Platt scaling ($A \cdot z + b$) vs. scalar temperature scaling ($z / T$) resolves the $\sim 17\%$ ECE on subjective tasks (resolved in Week 5 via the automated post-hoc calibration tournament).
