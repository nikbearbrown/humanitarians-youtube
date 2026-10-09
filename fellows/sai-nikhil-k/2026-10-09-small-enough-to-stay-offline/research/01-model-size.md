# Research 1 — model size for most desktops (agent report, accessed 2026-10-09)
- Steam HW survey Sep 2026 (combined): RAM 8GB 6.47%, 16GB 37.82%, 32GB 42.22%; <=8GB ~7.6%, >=16GB 89.2%. VRAM 8GB 26.71%. OS Win 95.03 / OSX 1.92 / Linux 3.05. Mac-only: 8GB 28.66%, 16GB 43.55%. Linux-only 8GB 6.09%, 16GB 40.85%. Gamer bias.
- Apple newsroom 2024-10-30: base Macs (M2/M3) to 16GB. Apple newsroom 2026-03-04 MacBook Neo $599, 8GB; footnote: "Bestselling PC laptop ... Intel Core Ultra 5 ... 8GB of RAM, 256GB SSD".
- Microsoft Copilot+ PC: 40+ TOPS NPU, 16 GB DDR5/LPDDR5. microsoft.com/windows/windows-11-specifications
- Chrome built-in AI (Gemini Nano desktop): >4GB VRAM or 16GB RAM + 4 cores; 22GB free. developer.chrome.com/docs/ai/get-started (2025-05-20)
- Dettmers & Zettlemoyer, ICML 2023, PMLR 202:7750-7774, arXiv 2212.09720: "{4-bit} precision is almost universally optimal for total model bits and zero-shot accuracy." 35,000+ experiments, 19M-176B.
- Huang et al., arXiv 2404.14047, Visual Intelligence 2:36 (2024) DOI 10.1007/s44267-024-00070-x: 4-bit ~2% drop; LLaMA3-8B wikitext2 ppl FP16 6.1, 4-bit GPTQ 6.5, 3-bit 8.2, 2-bit 210.
- Zheng et al., arXiv 2505.02214: Qwen3 degrades more at <=3-bit; Qwen3-14B ~1% MMLU drop 4-bit GPTQ, Qwen3-0.6B ~10%.
- Ouyang et al. arXiv 2411.17691; Kumar et al. arXiv 2411.04330 (PTQ degradation grows with training data).
- llama.cpp quantize: Llama-3-8B ppl delta Q8_0 +0.0026, Q4_K_M +0.1754, Q3_K_M +0.6569, Q2_K +3.5199. bpw (Llama-3.1-8B): Q4_K_M 4.8944, Q8_0 8.5008, F16 16.0005.
- Apple AFM 2024 arXiv 2407.21075: ~3B on-device, 3.7 bpw in production. Apple 2025 arXiv 2507.13575: 3B, 2 bpw QAT, KV 8-bit; MMLU 67.8 -> 64.4.
- Gemini 1.0 arXiv 2312.11805: Nano-1 1.8B, Nano-2 3.25B, 4-bit.
- Phi Silica (Windows blog 2024-12-06): Phi-3.5-mini derivative, 4-bit; 3.3B UNVERIFIED (press only). Being replaced by Aion Instruct (MS Learn 2026-10-02), size unpublished.
- Candidates: Qwen3.5-2B/4B/9B (2.27/4.66/9.65B, Apache, Feb 2026); Qwen3-4B; Gemma 4 E2B/E4B (Apache, Mar 2026); Granite 4.2 3B/8B (Apache, 2026-08-25); Ministral 3 3B/8B (Apache); SmolLM3-3B; Phi-4-mini (MIT); Llama 3.2 (community licence — restrictions, conflicts with AGPL's no-further-restrictions if bundled). Gemma 3n under Gemma ToU.
- KV cache: PagedAttention (Kwon et al., SOSP 2023, arXiv 2309.06180) "2 (key and value vectors) x 5120 x 40 x 2 (bytes per FP16)" = 800 KB/token for 13B. GQA arXiv 2305.13245.
- Qwen3-4B: 36 layers, 8 kv heads, head_dim 128 -> 144 KiB/token; 8K ctx 1.125 GiB. Qwen3.5-4B hybrid: 8 of 32 full-attn layers, 4 kv heads, head_dim 256 -> 32 KiB/token.
Conclusion: default 3-4B at Q4_K_M, 4-8K ctx; 7-9B tier for >=16GB; 1-2B fallback for 8GB.
