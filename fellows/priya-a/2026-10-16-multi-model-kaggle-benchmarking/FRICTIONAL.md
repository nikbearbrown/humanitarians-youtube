# Frictional Log: Multi-Model Decision Benchmarking (Week 5)

**Date:** 2026-10-16  
**Fellow:** Priya Adlakha  

### 1. What was attempted and expected
Benchmark the generalized RLCD pipeline across multiple open-weight model families (Laya, Typical-small, Decision 1.0, Von, OpenDecision AI) on cloud GPUs across diverse decision tasks (`choice`, `score`, `noul`).

### 2. Where the system resisted
- **Hardware Device Hardcoding:** `main.py` hardcoded `DEVICE="cuda"`, causing local smoke tests on Mac/CPU to fail with `AssertionError: Torch not compiled with CUDA enabled`.
- **Runtime Collision in Multi-GPU Subprocesses:** Intel MKL dynamic linking collisions crashed `torchrun` on Kaggle when spawning subprocesses.
- **Architectural Representation Friction:** `Typical-small` plateaued at 39.54% accuracy on tweet sentiment despite RLCD driving ECE to 0.50%.
- **Kaggle 12-Hour Continuous Execution Limit & Interactive Timeout:** Running the full 60,000-example pairwise `Anthropic/hh-rlhf` dataset (~5 hours for 2 epochs) inside an interactive browser session collided with Kaggle's hard 12-hour continuous runtime ceiling and browser idle disconnects when the screen slept. The run completed NexusRaven ($17.46\%$) and Tweet Sentiment ($39.54\%$), but was cut off at Step 8,475/12,000 of Epoch 2 on Anthropic RLHF before held-out test evaluation could execute, wiping temporary session storage.

### 3. What was done about it
- Implemented dynamic auto-detection (`cuda` if available, else `cpu`) and added `--device` CLI flag to `main.py`.
- Resolved the Intel MKL conflict by setting `USE_MULTI_GPU_TORCHRUN = False` for direct in-process GPU execution on Kaggle.
- Identified the root cause of the sentiment plateau: attaching a uniform bidirectional marker head to a causal Qwen backbone creates attention friction on nuanced natural language, proving that true model agnosticism requires architecture-aware readout heads.
- Transitioned the full standardized multi-dataset benchmark execution from fragile interactive browser tabs to headless Kaggle batch execution (**Save Version -> Save & Run All (Commit)**) to bypass local laptop sleep and WebSocket disconnects, providing an uninterruptible 12-hour cloud execution container to complete the full benchmark suite.

### 4. What was learned
- RLCD solves probability calibration reliably across every backbone, but readout heads must respect the underlying encoder vs causal attention geometry.
- Large preference datasets (`Anthropic/hh-rlhf` 60K) must be executed via headless batch commits rather than interactive Jupyter notebook kernels to prevent VM recycling during multi-hour training.
