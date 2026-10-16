# Frictional Log: Multi-Model Decision Benchmarking (Week 5)

**Date:** 2026-10-16  
**Fellow:** Priya Adlakha  

### 1. What was attempted and expected
Benchmark the generalized RLCD pipeline across multiple open-weight model families (Laya, Typical-small, Decision 1.0, Von, OpenDecision AI) on cloud GPUs across diverse decision tasks (`choice`, `score`, `noul`).

### 2. Where the system resisted
- **Hardware Device Hardcoding:** `main.py` hardcoded `DEVICE="cuda"`, causing local smoke tests on Mac/CPU to fail with `AssertionError: Torch not compiled with CUDA enabled`.
- **Runtime Collision in Multi-GPU Subprocesses:** Intel MKL dynamic linking collisions crashed `torchrun` on Kaggle when spawning subprocesses.
- **Architectural Representation Friction:** `Typical-small` plateaued at 39.54% accuracy on tweet sentiment despite RLCD driving ECE to 0.50%.

### 3. What was done about it
- Implemented dynamic auto-detection (`cuda` if available, else `cpu`) and added `--device` CLI flag to `main.py`.
- Resolved the Intel MKL conflict by setting `USE_MULTI_GPU_TORCHRUN = False` for direct in-process GPU execution on Kaggle.
- Identified the root cause of the sentiment plateau: attaching a uniform bidirectional marker head to a causal Qwen backbone creates attention friction on nuanced natural language, proving that true model agnosticism requires architecture-aware readout heads.

### 4. What was learned
- RLCD solves probability calibration reliably across every backbone, but readout heads must respect the underlying encoder vs causal attention geometry.
