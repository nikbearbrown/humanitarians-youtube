# FACTCHECK — Small Enough to Stay Offline

Figure by figure: claim → where on screen → how verified → result. Every number is
also asserted by `build_beats.py --check` (it reads `evidence/*.json` / `*.out` directly).
Measurements: MacBook Pro, Apple M2 Pro, 16 GB, macOS 26 (Darwin 25.6), 2026-10-09.

## Hardware and the offline promise (B00, B01, B08)

| Claim | On screen | Verified by | Result |
|---|---|---|---|
| Copilot+ PCs need 16 GB | B01 chip, B08 line 1 | Microsoft Windows 11 specs page, fetched 2026-10-09: "16 GB DDR5/LPDDR5" | ✔ |
| 2024: MacBook Air to 16 GB | B01 chip + narration | Apple Newsroom 2024-10-30: "models with M2 and M3 double the starting memory to 16GB … $999" | ✔ |
| MacBook Neo (2026) has 8 GB | B01 chip, B08 line 1 | Apple Newsroom 2026-03-04: "8GB of unified memory" | ✔ |
| "the best-selling PC laptop it is measured against" has 8 GB | B01 chip ("PC bestseller: 8 GB") | Same page, footnote 1: "Bestselling PC laptop with the latest shipping Intel Core Ultra 5 processor" … "8GB of RAM, 256GB SSD" | ✔ — qualified as *the one it is measured against* |
| Gavia ships for three systems | B01 chip | `gh api …/releases` v0.3.1: aarch64 DMG, x64 setup.exe, amd64 AppImage/deb, x86_64 rpm | ✔ |
| Gavia promises to stay offline | B00, B01 chip | `ROADMAP.md` @ `760e465`: "Gavia stays offline and on your computer." | ✔ |

## The arithmetic (B02) — algebra checks

- **M = N·b/8** (bytes). Checked on the real file: N = 4,205,751,296 (`general.parameter_count`),
  weights layer = 2,648,593,216 B → b = 8 × 2,648,593,216 / 4,205,751,296 = **5.038**
  bits/weight; and 4.21×10⁹ × 5.04 / 8 = 2.65×10⁹ B. Rounds to the on-screen 2.65 GB. ✔
  llama.cpp's own table lists Q4_K_M at 4.89 bpw on Llama-3.1-8B; this file is 5.04
  because some tensors are kept at higher precision. The note names "this Q4_K_M file".
- **r ≤ B/M.** Each decoded token reads every weight once; decoding is memory-bound
  (Yuan et al., arXiv 2402.16363, PDF: "in the decode stage, all computations are
  memory-bound"). A ceiling, not a prediction: it ignores KV-cache reads and overheads.
- **Reproducible numeric case:** 200 GB/s (Apple, M2 Pro) ÷ 2.648593216 GB = **75.51**
  tokens/s → typeset "≈ 75.5", spoken "near seventy-five". Measured 38.8 = 51% of it
  ("half its ceiling", B04). 9B, for comparison (not on screen): registry text weights
  5,629,109,120 B → 35.5 ceiling; measured 25.4 (72%).
- Units: GB = 10⁹ B throughout (bandwidth is quoted in decimal GB/s). 2.65 GB = 2.47 GiB.

## Quantization research (B03)

| Claim | Verified by | Result |
|---|---|---|
| 35,000+ experiments; 4-bit "almost universally optimal for total model bits and zero-shot accuracy" | arXiv 2212.09720 abstract (ICML 2023) | ✔ verbatim |
| Llama 3 8B WikiText2 perplexity 6.1 (FP16), 6.5 (4-bit), 8.2 (3-bit), 210 (2-bit) | arXiv 2404.14047 HTML, Table 1, GPTQ g128 (2-bit printed 2.1×10²) | ✔ |
| Apple on-device ~3B at 3.7 bpw (2024) | arXiv 2407.21075 PDF: "∼3 billion parameter model"; "3.7 bpw in production" | ✔ |
| Gemini Nano 1.8B and 3.25B, 4-bit | arXiv 2312.11805 PDF: "1.8B (Nano-1) and 3.25B (Nano-2)" … "4-bit quantized for deployment" | ✔ |

The narration's "Apple and Google chose about three billion parameters, at about four
bits": Apple ~3B at 3.7; Google 1.8B/3.25B at 4. Apple's 2025 report moved to 2 bpw *with
quantization-aware training* (arXiv 2507.13575) — a different technique from the
post-training quantization the B03 figures measure; not on screen.

## The run (B04) — `evidence/local_bench.out`

Ollama 0.30.10, Q4_K_M, temperature 0, seed 0, thinking off, 128 generated tokens,
median of 3 (a fourth warm-up run discarded), 244-token prompt with a fresh first line
each run so the prompt cache can't skip it.

| Row | Runs (tokens/s) | Median (on screen) | Cross-check (llama-bench tg128, `llamacpp_constrained.out`) |
|---|---|---|---|
| 4B, graphics chip | 38.5, 38.8, 39.7 | **38.8** | 39.6 ✔ |
| 9B, graphics chip | 25.4, 25.6, 25.0 | **25.4** | — (local 9B file won't load in llama.cpp) |
| 4B, CPU only (`num_gpu 0`) | 26.5, 23.3, 17.0 | **23.3** | 21.7 ✔ |
| 9B, CPU only | 8.3, 4.7, 15.9 | **8.3** | — |

- "keeps pace with the 9B on a GPU": 23.3 vs 25.4 (92%). ✔ (asserted ≥ 90%)
- "swung from five to sixteen": 4.7 and 15.9. ✔ Cause not claimed.
- Spoken roundings: 38.8 → "thirty-nine", 25.4 → "twenty-five", 23.3 → "twenty-three",
  8.3 → "eight". ✔
- Not on screen: the 0.8B (its Ollama tag runs MTP speculative decoding with a draft
  model, so its speed isn't comparable); memory held by Ollama (4.86 GiB for the 4B,
  7.20 GiB for the 9B — includes the vision encoder and a large default context).

## The engine (B05)

| Claim | Verified by | Result |
|---|---|---|
| llama.cpp: Metal, Vulkan, CUDA or plain CPU | llama.cpp README backends table (also HIP, SYCL…) | ✔ |
| Rust: llama-cpp-2, 1.5M downloads | `crates_check.out`: 1,546,983 all-time, 0.1.159, MIT OR Apache-2.0 | ✔ (community crate, utilityai) |
| ONNX Runtime GenAI APIs: Python, C#, C/C++, Java, Obj-C | onnxruntime-genai README API row | ✔ |
| Its only Rust binding: onnx-genai 0.1.0, 140 downloads | `crates_check.out` | ✔ (community crate) |
| Gavia already ships ONNX Runtime | Gavia `Cargo.toml`: `ort = "=2.0.0-rc.13"` | ✔ |
| Linux's web view has no WebGPU yet | WebKit bug 257694 "[GTK] WebGPU support" REOPENED; WebKitGTK 2.54 notes silent; Tauri uses WebKitGTK on Linux | ✔ (research pass; "yet" kept) |
| Ollama is a second app to install | ollama.com installers; runs a server on :11434 | ✔ |
| "kept to Gavia's schema: 40 of 40" | `llamacpp_constrained.out`: valid JSON 20/20 (0.8B) + 20/20 (4B); off-task probes 6/6 still valid actions | ✔ |

## The buttons (B06)

| Claim | Verified by | Result |
|---|---|---|
| best model ≤9B: 46% of OSWorld tasks | `osworld_check.out`: EvoCUA-8B-20260105 46.06% (166.28/361), 2026-01-13; best single model ≤9B with no larger planner | ✔ |
| people: 72% (2024 study) | arXiv 2404.07972 abstract: "over 72.36%" | ✔ |
| TinyAgent 1.1B 80%, GPT-4 Turbo 79% | arXiv 2409.00608 PDF, Table 2: 80.06 (1.1B, with ToolRAG) vs 79.08 | ✔ |
| here, Qwen 4B: 20 of 20 (held to Gavia's list by llama.cpp) | `llamacpp_constrained.out`: right action 12/12, none when none fits 8/8 | ✔ |
| 0.8B got 16 of 20 under it | same: 10/12 + 6/8 | ✔ |

Also measured, not on screen (`local_bench.out`, Ollama native tool calling): 0.8B
11/12 + 8/8 with one malformed call (HTTP 500); 4B 11/12 + 8/8 (it answered "Where can I
read how Gavia works?" in text instead of opening Help); 9B 12/12 + 8/8. Medians 1.00 /
2.17 / 3.56 s per request; llama.cpp constrained 0.26 s (0.8B) / 0.66 s (4B).

The 20 requests are in `local_bench.py` (`CASES`). Gavia's real pages (`check`,
`results`, `settings`, `help` — `desktop/src/types/navigation.ts`), themes (light, dark,
system) and update switch (Settings → Updates) at `760e465`. The tools are a test
harness: Gavia has no assistant.

## Help and IT (B07)

| Claim | Verified by | Result |
|---|---|---|
| Retrieval → more factual (Lewis 2020) | arXiv 2005.11401 PDF: evaluators found "BART was more factual than RAG in only 7.1% of cases, while RAG was more factual in 42.7%" | ✔ |
| "an eight-billion Llama said so only thirty-eight percent of the time" / card "Llama 3.1 8B abstained 38%" | FaithEval (ICLR 2025) Table 4, Unanswerable Context, AVG strict: Llama-3.1-8B-Instruct 0.376 | ✔ |
| "a study of over five thousand support agents … fifteen percent … a person doing the fixing" | QJE 140(2):889–942, Crossref abstract: "5,172 customer-support agents", "by 15% on average", an assistant to human agents | ✔ (draft said "the largest study"; not verifiable, reworded) |
| "CPUs read slowly" | llama-bench pp512 on the 4B: 470 tokens/s GPU vs 48 CPU (`llamacpp_constrained.out`) | ✔ |

## Verdict lines (B08)

Each line re-uses a figure verified above; none starts with a digit (the card eats a
leading number). Line 4's "Small models rarely abstain unprompted" rests on FaithEval
(Phi-3.5-mini 13.1%, Mistral-7B 29.0%, Llama-3.1-8B 37.6%).

## Rendered-frame math review (MATH-TYPESETTING.md) — both aspects

_To be filled after the render: B02 at each row's reveal (2.15 s, 5.84 s, 11.05 s) and at
15/50/85%, in 16:9 and 9:16. Check the fraction bars, the ≤ and ≈ glyphs, "GB/s",
clipping and legibility at 1080p._
