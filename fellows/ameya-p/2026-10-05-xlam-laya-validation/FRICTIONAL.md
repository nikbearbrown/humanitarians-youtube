# Friction Log: Week 3 — End-to-End Validation Report (xLAM Dataset & Laya Model)

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Report:** [Work Report](work_report.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Oct 5 to Oct 11, 2026

---

## 1. Focus of the week

- Executing full-scale end-to-end GPU validation of the Reinforcement Learning with Calibrated Decisions (RLCD) pipeline on the 60,000-row `Salesforce/xlam-function-calling-60k` benchmark using `convaiinnovations/laya`.
- Evaluating held-out test split routing accuracy and Expected Calibration Error (ECE) before and after RLCD fine-tuning.
- Documenting the live GPU training logs and metrics in `docs/PIPELINE_VALIDATION_REPORT.md` and `work_report.md`.
- Producing the 5-beat Plain-register validation reel (`2026-10-05-xlam-laya-validation`, `1:00`, `humanitarians` brand palette `#F0EAD6`, Kokoro `af_bella` narration).

## 2. What was tried, and what was expected

- **Full 60k xLAM ingestion and training.** Expectation: scaling from the Week 2 CPU smoke-test subset (8 rows) to all 60,000 function-calling examples on GPU would significantly improve Laya's tool-selection accuracy without degrading confidence calibration.
- **Proper scoring rule under sharp accuracy gains.** Expectation: the hybrid Brier + cross-entropy objective would allow accuracy to climb toward $>95\%$ while keeping ECE under $2\%$.
- **Reel build on the `humanitarians` brand preset.** Expectation: switching the Week 3 reel to the `humanitarians` Plain register (`#F0EAD6` ground, `EB Garamond` / `Montserrat`, `af_bella` voice) would compile cleanly in a single pass.

## 3. Points of resistance, and next steps taken

### Scaling sequence packing and distractor generation to 60,000 rows
- Transforming 60,000 raw JSON tool-calling records into `[MASK]`-delimited candidate sequences with mined negative distractors required careful truncation and offset accounting so candidate `[MASK]` tokens were never clipped at the 512-token boundary.
- **Next step:** enforced dynamic context-budget reservation in `helper.py` so the full candidate option suffix and its `[MASK]` positions are always preserved inside `max_length`.

### Preventing overconfidence as routing accuracy approached 99%
- As Laya's tool-selection accuracy climbed from the $\sim 73\%$ baseline to **$99.10\%$** on the xLAM benchmark, pure cross-entropy updates tended to push logits too hot on the remaining $0.9\%$ of ambiguous tool calls.
- **Next step:** the Brier proper scoring reward + post-training temperature calibration (`temperature.pt`) regularized the output distribution, bringing final held-out Expected Calibration Error down to **$0.83\%$**.

### Windows file-descriptor `[Errno 22] Invalid argument` during final reel wrapper
- After all 5 beats (`B00`–`B04`) rendered cleanly (`clips/B00.mp4`–`B04.mp4`, `59.6s` total) and passed `GATE T` (`TYPECHECK.md`: 5 beats checked, 0 FAILs), the automated `./art` post-build wrapper recorded `[Errno 22] Invalid argument` in `build-state.json` on Windows path/stream handling.
- **Next step:** verified the rendered clips and audio timings directly (`mp3/timings.json`, `clips/manifest.json`) and exported the clean final master to `vids_final/week 3 (Oct 5).mp4`.

## 4. AI and other contributions: accepted, changed, rejected

### Claude / Brutalist Toolkit
- **Accepted:** Mapped the concise Week 3 validation report into a focused 5-beat Plain-register reel (`B00` `ClaudeComposerAsk`, `B01` `BrutalistHesitantWriterSq`, `B02` `ClaudeDefinitions`, `B03` `NikBearBrownTerminalAsk`, `B04` `ClaudeTitleOutro`) matching the 1-minute runtime target (`59.6s`).
- **Accepted:** Used `ClaudeDefinitions` in `B02` to contrast the two core validation metrics side by side ($73\% \to 99.10\%$ routing accuracy vs. $0.83\%$ Expected Calibration Error).

## 5. Understood now, and still unresolved

### Understood
- **RLCD scales on masked decision encoders:** on a 60,000-row function-calling benchmark, Laya's bidirectional `[MASK]` readout head pairs naturally with Brier-score RL fine-tuning, achieving both near-ceiling routing accuracy ($99.10\%$) and sub-$1\%$ calibration error ($0.83\%$ ECE).

### Unresolved
- **Single-model and single-schema coupling:** `helper.py` and `models.py` still rely on explicit dataset adapters (`typed-decisions`, `xlam`) and Laya-specific model loading.
- **Multi-architecture and multi-primitive behavior:** whether causal/autoregressive small language models (`Typical-small`, `Decision 1.0`, `Von`) and non-categorical primitives (`noul` binary safety pairs and `score` ordinal ratings) calibrate just as cleanly under RLCD (investigated in Week 4).
