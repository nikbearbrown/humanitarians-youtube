# SOURCES — Small Enough to Stay Offline

## Provenance

- **What Sai supplied (2026-10-09, in words):** the week was research on AI agents in
  Gavia, on local models so the app stays offline: which parameter size suits most
  desktops on every OS, which inference engines can run it, and what agents could do
  (chatbot, in-house IT support, help with app navigation). "All the conclusions should
  be backed by research going on in local LLMs." He chose the ONE idea and title from
  Claude's proposals and asked to drop the line about last week's survey plan.
- **What Claude did at his request:** three research passes (model size, runtimes,
  applications), then re-read every figure used on screen at its original source
  (`evidence/sources_check.out`), and ran the measurements in `evidence/`.
- **LibKey:** the org's scholarly connector was not authenticated in this session, so no
  LibKey access links were generated. Papers were checked on arXiv / PMLR / ACL Anthology
  / publisher pages, and DOIs via Crossref.

## Sources used on screen or in narration

| # | Source | Used for | Beat |
|---|---|---|---|
| 1 | Microsoft, Windows 11 specifications — Copilot+ PC: "16 GB DDR5/LPDDR5", "40+ TOPS" NPU | 16 GB AI-PC floor | B01, B08 |
| 2 | Apple Newsroom, 2024-10-30 — MacBook Air M2/M3 "double the starting memory to 16GB" | 16 GB | B01 |
| 3 | Apple Newsroom, 2026-03-04, "Say hello to MacBook Neo" — "8GB of unified memory", $599; footnote: "Bestselling PC laptop with the latest shipping Intel Core Ultra 5 processor" … "8GB of RAM" | 8 GB is back | B01, B08 |
| 4 | Gavia v0.3.1 release assets (GitHub API) — DMG (aarch64), x64 setup.exe, AppImage, deb, rpm | three systems | B01 |
| 5 | Gavia `ROADMAP.md` at `760e465`, "Not planned": "Gavia stays offline and on your computer." | the offline promise | B00, B01 |
| 6 | Apple Newsroom, 2023-01-17 — M2 Pro "200GB/s of unified memory bandwidth" | B in r ≤ B/M | B02, B04 |
| 7 | Yuan et al., "LLM Inference Unveiled: Survey and Roofline Model Insights", arXiv 2402.16363 — "in the decode stage, all computations are memory-bound" | why r ≤ B/M | B02 |
| 8 | Dettmers & Zettlemoyer, "The case for 4-bit precision: k-bit Inference Scaling Laws", ICML 2023 (PMLR 202:7750–7774), arXiv 2212.09720 | 4-bit near-optimal; 35,000 experiments | B03, B08 |
| 9 | Huang et al., "An Empirical Study of LLaMA3 Quantization: From LLMs to MLLMs", Visual Intelligence 2:36 (2024), DOI 10.1007/s44267-024-00070-x, arXiv 2404.14047, Table 1 | 6.1 / 6.5 / 8.2 / 210 | B03 |
| 10 | Apple, "Apple Intelligence Foundation Language Models", arXiv 2407.21075 — "∼3 billion parameter" on-device, "3.7 bpw in production" | vendor choice | B03 |
| 11 | Gemini Team, "Gemini: A Family of Highly Capable Multimodal Models", arXiv 2312.11805 — Nano 1.8B / 3.25B, "4-bit quantized for deployment" | vendor choice | B03 |
| 12 | llama.cpp README (ggml-org/llama.cpp, MIT) — Metal, CUDA, HIP, Vulkan, SYCL, CPU backends | engine | B05 |
| 13 | `llama-cpp-2` crate (utilityai/llama-cpp-rs), 0.1.159, 2026-10-07, MIT OR Apache-2.0 | Rust binding | B05 |
| 14 | microsoft/onnxruntime-genai README — APIs Python, C#, C/C++, Java; no Rust (only third-party `onnx-genai` 0.1.0 on crates.io) | ORT GenAI | B05 |
| 15 | WebKit bug 257694 "[GTK] WebGPU support" (REOPENED); WebKitGTK 2.54 release notes; Tauri webview docs | no WebGPU on Linux's web view | B05 |
| 16 | Xie et al., "OSWorld", NeurIPS 2024, arXiv 2404.07972 — humans 72.36% | people: 72% | B06 |
| 17 | OSWorld-Verified results file (osworld-v1.xlang.ai, entries to 2026-08-01) — EvoCUA-8B 46.06% | best ≤9B | B06 |
| 18 | Erdogan et al., "TinyAgent: Function Calling at the Edge", EMNLP 2024 Demo, DOI 10.18653/v1/2024.emnlp-demo.9 — 1.1B 80.06% vs GPT-4-Turbo 79.08% | actions work small | B06 |
| 19 | Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", NeurIPS 2020, arXiv 2005.11401 | retrieval → more factual | B07 |
| 20 | Ming et al., "FaithEval", ICLR 2025, arXiv 2410.03727, Table 4 — Llama-3.1-8B-Instruct 0.376 on unanswerable context | 38% | B07, B08 |
| 21 | Brynjolfsson, Li & Raymond, "Generative AI at Work", QJE 140(2):889–942 (2025), DOI 10.1093/qje/qjae044 — 5,172 agents, +15% issues resolved per hour | person fixes | B07 |

Background read but not on screen (research files in `research/`): Steam Hardware Survey
Sep 2026; Qwen3 quantization study (arXiv 2505.02214); NVIDIA "Small Language Models are
the Future of Agentic AI" (arXiv 2506.02153); BFCL (ICML 2025); When2Call (NAACL 2025);
Octopus v2; AppAgent; ITBench; Sufficient Context; Apple 2025 tech report (2 bpw QAT).

## Week-scope commits (Gavia, after 2026-10-02)

| Commit | Author | What | Narrated? |
|---|---|---|---|
| `3099d47` | dependabot[bot] | Bump actions/upload-artifact 4 → 6 (unmerged branch) | No |

No release, no collaborator work. `main` is still `760e465` (v0.3.1).

## Honesty log

- Research pass said "AutoGLM-OS-9B 48.03%" was the best ≤9B OSWorld model; the verified
  results file does not contain it. **Used: EvoCUA-8B 46.06%** (`osworld_check.out`).
- QJE (published) says 5,172 agents and +15%; the 2023 NBER draft says 5,179 and +14%.
  **Used: the published figures.**
- Phi Silica's "3.3B" exists only in press coverage — **not used.**
- "Best-selling PC laptop" is Apple's footnote, qualified as "with the latest shipping
  Intel Core Ultra 5 processor" — the narration says "the best-selling PC laptop it is
  measured against", which is what the footnote supports.
- OSWorld's 72% human figure is from the 2024 paper's task set; the 46% is from the
  later OSWorld-Verified set. The card says "(2024 study)" on the people figure.
- Ollama 0.30.10's `format` (JSON schema) was not enforced for Qwen3.5 (`grammar_probe.out`);
  its scores are not used. The enforced test ran in llama.cpp (`llamacpp_constrained.out`).
- The 9B in this Mac's Ollama store is the older merged file (6.59 GB with the vision
  encoder). The registry's current split text weights are 5.63 GB; B02 works only the 4B.
