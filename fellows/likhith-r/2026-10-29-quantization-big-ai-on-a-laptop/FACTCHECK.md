# FACTCHECK — Quantization: Big AI on a Laptop

Status: claims checked by Claude Code against SOURCES.md and the evidence run. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | A 70B model at 16 bits needs ~140 GB for weights; 8.75× a 16 GB laptop | PASS | 70e9 × 2 B (quant_toy.out.txt) | "weights alone" on the title |
| 2 | B03 | Weights are numbers, 2 bytes each at 16 bits; 7B → 14 GB | PASS | float16 bits of a real toy weight; 7e9 × 2 B | — |
| 3 | B04 | Quantization rounds each weight onto a small grid, stored in 8 or 4 bits | PASS | RTN on 8 toy weights | — |
| 4 | B05 | 8 bits = 256 levels, 4 bits = 16; a scale maps back; per-group scales cut error | PASS | 2^8, 2^4; 43.3 % vs 13.1 % (toy) | labelled "toy layer" |
| 5 | B06 | 14 → 7 → 3.5 GB; often faster because memory traffic is the bottleneck | PASS | arithmetic; bandwidth bound at an illustrative 100 GB/s | "about": scales add ~0.44 GB (3.94 GB) |
| 6 | B07 | Rounding errors mostly cancel; GPTQ corrects them; AWQ guards key weights | PASS (corrected from brief) | toy 49×; GPTQ / AWQ papers | brief said both protect outliers |
| 7 | B08 | Below 4 bits quality drops; small models, maths and code suffer first | PASS (soft) | toy curve (proxy); Dettmers & Zettlemoyer 2023; Li et al. 2024; Liu et al. 2025 | proxy caption on screen |
| 8 | B09 | llama.cpp and Ollama made 4-bit the local default | PASS | Ollama default tags Q4_K_M; llama.cpp GGUF | — |
| 9 | B10 | Viewer prompt: "Which 4-bit model fits my laptop, and what do I lose?" | EXEMPT | Handoff prompt, not a factual claim | — |
