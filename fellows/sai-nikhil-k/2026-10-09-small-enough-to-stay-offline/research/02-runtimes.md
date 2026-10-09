# Research 2 — runtimes (agent report, accessed 2026-10-09)
- llama.cpp: MIT; backends Metal, CUDA, HIP, Vulkan, SYCL, WebGPU, CPU...; release v0.6.0 2026-10-05; b11534 prebuilt macos-arm64 AND macos-x64, Windows CPU/CUDA/Vulkan/ROCm/SYCL/OpenVINO, Ubuntu CPU/Vulkan/CUDA/ROCm/SYCL. README: "Plain C/C++ implementation without any dependencies"; "Apple silicon is a first-class citizen".
- llama-cpp-2 crate (utilityai/llama-cpp-rs) 0.1.159 2026-10-07, MIT OR Apache-2.0, features cuda/metal/vulkan/rocm/opencl/llguidance; "does not follow semver meaningfully".
- ORT GenAI: MIT; Linux/Windows/Mac/Android; CPU, CUDA, DirectML, NvTensorRtRtx, OpenVINO, QNN, WebGPU; constrained decoding; NO Rust API (third-party onnx-genai 0.1.0 only); CoreML not documented; v0.17.0 2026-09-28 osx-arm64 only.
- MLX: Apple silicon + Linux CUDA/CPU; no Windows. MIT.
- candle: MIT/Apache, CPU/CUDA/Metal/WASM, no Vulkan/DirectML. v0.11.0 2026-06-26.
- mistral.rs: MIT, v0.9.4 2026-09-24 (crate 0.8.1 lags); prebuilt CPU on Windows.
- Ollama: MIT, v0.40.2 2026-10-08, separate install, server :11434; README "Supported backends: llama.cpp"; 2026-03-30 blog: Apple silicon on MLX (preview). LM Studio proprietary, no Intel Mac.
- Webview: WebView2 = Chromium (WebGPU on D3D12 since Chrome 113); Safari 26.0 ships WebGPU (WebKit blog 2025-09-15); WebKitGTK no WebGPU (bug 257694 REOPENED; 2.54 notes silent). WebLLM arXiv 2412.15803: "up to 80% native performance"; M3 Max Llama-3.1-8B 41.1 vs 57.7 tok/s (71.2%).
- Decode memory-bound: arXiv 2402.16363 (LLM Inference Unveiled, roofline): "in the decode stage, all computations are memory-bound".
- Bandwidth: M1 ~67 (implied), M1 Pro 200, M2 100, M2 Pro 200 (newsroom 2023/01), M3 100, M3 Pro 150, M4 120, M4 Pro 273, M5 153, M5 Pro 307 GB/s; DDR5-5600 dual channel 89.6 GB/s (Intel ARK i9-13900K); RTX 4060 272 GB/s (third-party only).
- Tool calling: llama.cpp GBNF / json_schema; llama-server "Function calling / tool use for ~any model" (--jinja default). ORT GenAI grammar tool calling. mistral.rs grammar enforcement.
Recommendation: llama.cpp via llama-cpp-2, GGUF; Metal / Vulkan / CUDA; Intel Mac too. ORT GenAI no Rust, no Mac GPU doc. WebGPU ruled out on Linux.
