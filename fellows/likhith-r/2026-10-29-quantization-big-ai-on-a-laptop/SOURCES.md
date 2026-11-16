# SOURCES — Quantization: Big AI on a Laptop

## Executable evidence (every on-screen number)
- `evidence/quant_toy.py` → `evidence/quant_toy.out.txt` + `evidence/quant_toy.json` (numpy 2.5.3, seed 2026).
  Toy 512×4096 layer, Student-t(df=4) weights scaled to std 0.02; symmetric round-to-nearest (RTN) quantization.
  - B02: 70e9 × 2 bytes = 140 GB; 140 / 16 GB laptop = 8.75×
  - B03: patch of row 0 (24 weights); weight #1 = +0.0172 → float16 bits 0 01001 0001100111; 7e9 × 2 B = 14 GB
  - B04: eight weights → q = −1 +3 +1 0 −2 −2 −7 −2 with s = 0.00673 (4-bit grid, q ∈ −8…7)
  - B05: 2⁸ = 256, 2⁴ = 16 levels; 4-bit error 43.3 % (one scale per row) vs 13.1 % (a scale per 32 weights)
  - B06: 14 / 7 / 3.5 GB; tokens/s upper bound at an illustrative 100 GB/s = 7.1 / 14.3 / 28.6
  - B07: rounding-error histogram (48.5 % rounded up); aligned worst case 6.62 vs actual net 0.134 → 49× smaller (mean over 32,768 outputs); one outlier in a group of 32: 4/31 neighbours keep a non-zero level, 21/31 when it is set aside
  - B08: weight error vs bits (per-32 scales) 8: 0.7 · 6: 3.0 · 5: 6.2 · 4: 13.1 · 3: 29.4 · 2: 65.7 %
  - Honesty note: real 4-bit files also store the scales (one fp16 per 32 weights → 3.94 GB for 7B), hence "about 3.5 GB".

## Literature
- GPTQ — Frantar, Ashkboos, Hoefler, Alistarh, "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers", ICLR 2023, arXiv:2210.17323. Quantizes weights one column at a time and updates the not-yet-quantized weights to compensate the error (second-order / Hessian information).
- AWQ — Lin et al., "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration", MLSys 2024, arXiv:2306.00978. ~1 % of weights are salient (chosen by activation magnitude) and are protected by per-channel scaling.
- Outliers — Dettmers et al., "LLM.int8()", 2022, arXiv:2208.07339 (outlier features dominate quantization error).
- 4-bit sweet spot — Dettmers & Zettlemoyer, "The case for 4-bit precision: k-bit Inference Scaling Laws", ICML 2023, arXiv:2212.09720.
- Task/size sensitivity — Li et al., "Evaluating Quantized Large Language Models", 2024, arXiv:2402.18158; Liu et al., "Quantization Hurts Reasoning? An Empirical Study on Quantized Reasoning Models", 2025, arXiv:2504.04823.
- llama.cpp (github.com/ggml-org/llama.cpp): GGUF k-quant types incl. Q4_K_M; logo from the repo's `media/llama1-logo.png`.
- Ollama (ollama.com/library): default model tags ship 4-bit (Q4_K_M) GGUF weights.

## Corrections applied (DOUBLE-CHECK LAW)
1. Brief point 6 said "GPTQ and AWQ protect the few outlier weights that matter most". Only AWQ protects salient weights; GPTQ compensates the rounding error as it goes. Narration: "GPTQ corrects them; AWQ guards the key weights."
2. "Errors cancel" is stated as the measured toy result (net error 49× below the aligned worst case), not as a guarantee: relative layer error still tracks weight error.
3. "Below 4 bits quality drops" is shown with a toy weight-error curve captioned "a proxy for quality, not a benchmark"; the small-models / maths / code ordering is attributed to the literature above, softly.
4. "In 2026" kept off screen as a date claim; the close says llama.cpp and Ollama made 4-bit the local default (true of their default tags), without a version count that would date.
