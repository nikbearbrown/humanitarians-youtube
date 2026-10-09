Can a desktop app have an AI assistant and still work with no internet? Only if the model fits the smallest computer the app ships to.

This week on Gavia, the offline loon-detection app, there was no release. It was research: what would it take to put an assistant inside Gavia without breaking its promise to stay offline? We looked at four questions: which computers, which model size, which engine, and which jobs.

The machines. Microsoft's Copilot+ PCs require 16 GB of memory, and in 2024 Apple raised the MacBook Air's starting memory to 16 GB. But 8 GB has not gone away. Apple's MacBook Neo (2026) ships with 8 GB, and so does the best-selling Core Ultra 5 PC laptop Apple compares it with. Gavia ships for macOS, Windows and Linux, so an assistant has to fit the 8 GB machine.

The arithmetic. A model's weights take N × b / 8 bytes. Writing each token reads every weight once, so decode speed is capped by memory bandwidth divided by that size. Qwen3.5 4B at 5.04 bits per weight is 2.65 GB. On an M2 Pro, which has 200 GB/s of bandwidth, that gives a ceiling of about 75.5 tokens per second.

The bits. Dettmers & Zettlemoyer ran over 35,000 experiments and found 4-bit precision "almost universally optimal for total model bits and zero-shot accuracy." Below 4 bits, quality breaks down. Llama 3 8B's perplexity is 6.1 at 16 bits, 6.5 at 4, 8.2 at 3 and 210 at 2 (Huang et al., 2024). Apple's on-device model is about 3B parameters at 3.7 bits per weight. Gemini Nano is 1.8B and 3.25B parameters at 4 bits.

The run, on one laptop (M2 Pro, 16 GB):

- Qwen3.5 4B wrote 38.8 tokens per second on the GPU and 23.3 on the CPU alone.
- Qwen3.5 9B wrote 25.4 on the GPU and 8.3 on the CPU. Its CPU runs swung between 4.7 and 15.9.

The engine. ONNX Runtime is the engine Gavia already ships. Its GenAI add-on has no official Rust API, and the only community Rust binding has 140 downloads. llama.cpp runs on Metal, Vulkan, CUDA or a plain CPU, and its Rust binding (llama-cpp-2) has about 1.5 million downloads. A model running in the app's web view fails on Linux, where the web view has no WebGPU yet. Ollama is a second app the user would have to install.

The jobs.

- Small models driving a screen by its pixels are not there yet. The best model of 9B or under completes 46% of OSWorld-Verified tasks; people completed 72% in the 2024 OSWorld study.
- Given an app's own actions instead, TinyAgent-1.1B scored 80% against GPT-4-Turbo's 79%.
- We gave Qwen Gavia's own actions: its pages, its themes and its update switch. We added 8 requests Gavia can't handle, and "none" as an allowed answer. With llama.cpp holding answers to that list, the 4B got all 20 right. The 0.8B got 16: the list guarantees the form of the answer, not the judgment.
- For chat help and IT support, retrieval makes answers more factual (Lewis et al., 2020). But small models rarely admit when the answer isn't in the page. In FaithEval, Llama 3.1 8B did so only 38% of the time. And in a study of 5,172 support agents, the 15% productivity gain came with a person doing the fixing (Brynjolfsson, Li & Raymond, QJE 2025).

Try it yourself: if you're adding an assistant to an app that has to stay offline, start from your users' smallest machine, not yours. Ask what model fits there at 4 bits, next to your app, and how fast it reads a page on the CPU alone. Then list your app's own actions and give the model "none" as an allowed answer.

Chapters:
0:00 Can Gavia have an assistant and stay offline?
0:16 The small machine: 16 GB floor, 8 GB still sold
0:37 The arithmetic: size and speed ceiling
0:58 Why 4 bits, not 16
1:24 Timed on this laptop: 4B and 9B
1:43 Which engine: llama.cpp vs ONNX Runtime GenAI
2:06 What it should do: Gavia's own buttons
2:29 Chat help and IT support
2:48 Verdict
3:06 Your turn: start from the smallest machine
3:21 Outro

Sources:
Dettmers & Zettlemoyer, "The case for 4-bit precision: k-bit Inference Scaling Laws," ICML 2023 — https://arxiv.org/abs/2212.09720
Huang et al., "An Empirical Study of LLaMA3 Quantization: From LLMs to MLLMs," Visual Intelligence 2024 — https://arxiv.org/abs/2404.14047
Apple, "Apple Intelligence Foundation Language Models," 2024 — https://arxiv.org/abs/2407.21075
Gemini Team, "Gemini: A Family of Highly Capable Multimodal Models" — https://arxiv.org/abs/2312.11805
Yuan et al., "LLM Inference Unveiled: Survey and Roofline Model Insights" — https://arxiv.org/abs/2402.16363
Xie et al., "OSWorld," NeurIPS 2024 — https://arxiv.org/abs/2404.07972 · OSWorld-Verified results — https://os-world.github.io/
Erdogan et al., "TinyAgent: Function Calling at the Edge," EMNLP 2024 Demo — https://arxiv.org/abs/2409.00608
Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," NeurIPS 2020 — https://arxiv.org/abs/2005.11401
Ming et al., "FaithEval," ICLR 2025 — https://arxiv.org/abs/2410.03727
Brynjolfsson, Li & Raymond, "Generative AI at Work," QJE 2025 — https://doi.org/10.1093/qje/qjae044
Microsoft, Windows 11 specifications (Copilot+ PC) — https://www.microsoft.com/en-us/windows/windows-11-specifications
Apple Newsroom, MacBook Neo (2026) — https://www.apple.com/newsroom/2026/03/say-hello-to-macbook-neo/
llama.cpp — https://github.com/ggml-org/llama.cpp · llama-cpp-2 — https://crates.io/crates/llama-cpp-2
ONNX Runtime GenAI — https://github.com/microsoft/onnxruntime-genai
Gavia — https://github.com/nikhil-kunapareddy/gavia

Hosted by Sai. Voice: Kokoro am_onyx, free and local, no account. AI-generated narration. Motion graphics were built with Remotion, and the equations were typeset locally as outlined SVG. Every speed and tool-call figure comes from scripts run for this video on one MacBook Pro (M2 Pro, 16 GB). We used Ollama 0.30.10 and llama.cpp 0.4.0 with Qwen3.5 0.8B, 4B and 9B, at temperature 0 and a fixed seed. The 20 requests are a demo, not a benchmark. Gavia has no assistant yet: this is research. Every paper and vendor figure was checked at its original source. No image was generated. No human-performed audio or video in this production.

Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: Gavia, local LLM, on-device AI, offline AI, small language models, quantization, 4-bit, GGUF, llama.cpp, Ollama, ONNX Runtime, Qwen3.5, memory bandwidth, function calling, tool calling, AI agents, RAG, Tauri, Rust, desktop app, Humanitarians AI, weekly progress, Computational Skepticism

#LocalLLM #OnDeviceAI #llamacpp #Quantization #AIAgents #Rust #HumanitariansAI #ComputationalSkepticism
