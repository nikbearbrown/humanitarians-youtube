# Frictional Log: Config Architecture & Test Hierarchy

**Date:** 2026-10-02  
**Fellow:** Priya Adlakha  

### 1. What was attempted and expected
Following Dev's scope correction (focusing on Laya/Jev ModernBERT decision models rather than causal LM SFT), the goal was to build a declarative Pydantic configuration engine and a 6-tier test suite to decouple pipeline execution from raw data formats.

### 2. Where the system resisted
- The original SFT config schema assumed causal language models (LoRA ranks, response masking, chat templates), which failed conceptually for non-generative bidirectional decision encoders.
- Python test environments on local CPU lacked GPU packages, requiring all heavy PyTorch and model imports to be deferred into function bodies to allow offline unit testing.

### 3. What was done about it
- Rebuilt `JobSpec`, `DatasetSpec`, `TrainingSpec`, and `OutputSpec` around Laya's decision primitives (`choice`, `score`, `noul`) and RLCD parameters.
- Authored `docs/test_plan.md` defining 6 test tiers.
- Implemented 49 automated unit tests verifying Brier score math, advantage normalization, schema validation, and corrupted line handling. All 49 passed.

### 4. What was learned
- Decoupling configuration from training execution allows testing pipeline guardrails in milliseconds on any machine before launching expensive compute jobs.
