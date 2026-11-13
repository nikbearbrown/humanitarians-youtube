# Research 3 — what small local agents can do (agent report, accessed 2026-10-09)
## Small models as agents
- Belcak et al. (NVIDIA) arXiv 2506.02153 (position; v3 2026-09-22): SLMs "sufficiently powerful, inherently more suitable, and necessarily more economical for many invocations in agentic systems"; SLM = fits "onto a common consumer electronic device", "most models below 10bn". 7B 10-30x cheaper. 60/40/70% estimates (not experiments).
- TinyAgent arXiv 2409.00608, EMNLP 2024 Demo, DOI 10.18653/v1/2024.emnlp-demo.9: 16 Mac functions; FT 1.1B 12.71->78.89%, 7B 41.25->83.09%; +ToolRAG 80.06 / 84.95 vs GPT-4-Turbo 79.08. 4-bit 1.1B 0.68 GB, 2.9 s, 80.35%; 7B 4.37 GB 85.14%. MacBook Pro M3. Synthetic test set.
- Octopus v2 arXiv 2404.01744: Gemma-2B, 20 Android APIs, 99.524% vs GPT-4 98.571%; 0.38 s vs 1.02 s; irrelevant_function() escape hatch.
## BFCL
- Patil et al. ICML 2025 PMLR 267:48371-48392: "memory, dynamic decision-making, and long-horizon reasoning remain open challenges"; call with missing info = hallucination.
- Leaderboard data_overall.csv (2026-04-12): Claude-Opus-4.5 77.47/68.38/84.72; GPT-5.2 55.87/28.12/79.42; Qwen3-8B 42.57/41.75/79.07; Qwen3-4B-2507 35.68/22.12/84.93; Llama-3.2-3B 21.95/4.00/52.06; xLAM-2-8b 46.68/70.00/63.28; ToolACE-2-8B irrelevance 90.79; Ministral-8B 11.10/0.00/100 (never calls -> gamed). (overall/multi-turn/irrelevance)
- When2Call (Ross et al., NAACL 2025, arXiv 2504.18851): tool hallucination Llama-3.1-8B 67%, Llama-3.2-3B 52%, Qwen-2.5-7B 21%; after RPO 1.2% (8B), 1.9% (4B). "most community models are unwilling to admit they cannot answer the question."
## RAG / grounding / abstention
- Lewis et al. NeurIPS 2020 arXiv 2005.11401: BART more factual 7.1% vs RAG 42.7%; NQ 44.5 vs T5-11B 34.5.
- Shuster et al. Findings EMNLP 2021 DOI 10.18653/v1/2021.findings-emnlp.320.
- Béchard & Ayala NAACL 2024 Industry DOI 10.18653/v1/2024.naacl-industry.19.
- Vectara HHEM (2026-09-22): Qwen3-8B 4.8%, Qwen3-4B 5.7%, Gemma-3-4B 6.4% (answer rate 67.3%); Claude Opus 4.5 10.9%.
- FaithEval ICLR 2025 arXiv 2410.03727 unanswerable-context abstention: Gemma-2-9B 50.3, Llama-3.1-8B 37.6, Mistral-7B 29.0, Phi-3.5-mini 13.1, Phi-3-mini 6.3; GPT-4o 59.7, Claude-3.5-Sonnet 62.1. "Abstaining is challenging, even when explicitly instructed."
- Sufficient Context (Joren et al., ICLR 2025, arXiv 2411.06037): "the introduction of additional context paradoxically reduces the model's ability to abstain."
- Kalai et al. arXiv 2509.04664: "Under binary grading, abstaining is strictly sub-optimal."
- AbstentionBench arXiv 2506.09038: "scaling models is of little use".
## IT support
- No study of <=9B local models doing end-user IT troubleshooting found.
- Brynjolfsson, Li & Raymond, QJE 140(2):889-942 (2025) DOI 10.1093/qje/qjae044: +15% issues/hour, 5,172 agents; human in loop.
- Xu et al. (LinkedIn) SIGIR 2024 DOI 10.1145/3626772.3661370: RAG+KG over tickets, -28.6% median resolution time.
- ITBench ICML 2025 PMLR 267:27134-27197: SOTA agents resolve 13.8% SRE, 25.2% CISO, 0% FinOps.
## GUI / navigation
- OSWorld NeurIPS 2024 DOI 10.52202/079017-1650: humans 72.36%, best model 12.24%.
- OSWorld-Verified (to 2026-08-01): top 90.19% (framework); <=9B best AutoGLM-OS-9B 48.03%, EvoCUA-8B 46.06%, UI-TARS-1.5-7B 29.6%.
- Ferret-UI Lite arXiv 2509.26539: 3B, OSWorld 19.8%.
- AppAgent CHI 2025 arXiv 2312.13771: GPT-4 2.2% raw actions, 48.9% simplified action space, 95.6% with manual docs.
- AXIS arXiv 2409.17140: API-first in Word -65-70% time, 97-98% accuracy.
- Microsoft arXiv 2405.20347: fine-tuned Phi-3-mini 95.86% vs GPT-4-turbo 75.88-82.00% on internal app commands; OOD F1 100.
## Verdicts
- Chatbot: feasible with constraints (retrieval + fixed "not in the docs" reply). FaithEval.
- IT support: not as autonomous fixer; triage with typed diagnostic tools + human escalation. ITBench.
- Navigation: feasible now via the app's own typed commands + a "none of these" path. TinyAgent / Octopus.
