# Frictional log — Adversarial Inputs

## 2026-10-02 — the project update, in two aspect ratios

**What I was working on.** A STEM AI explainer breaking down why LLMs fail to format their own output and how deterministic normalizers act as a defense layer against prompt injection.

**What I tried, and what I expected.** 
- I attempted to rely on system prompts to force the model to output clean integers for financial data.
- I expected the LLM to consistently obey the prompt constraints when returning data to the backend.

**Where it resisted, and what I did next.** 
- The LLM acts as a text predictor, not a code executor. Under adversarial conditions, it easily bypassed its instructions and outputted strings like `"approx five million"` or `"null"`, which immediately broke downstream math functions and crashed the application.
- I pivoted the architectural design away from prompt engineering entirely, relying instead on a strict Python equality gate (`if claim != ledger_truth`) to safely trap and fail any malicious or hallucinated strings.

**What Claude contributed, and what I did with it.** 
- Mine: The core concept of the "System Prompt Fallacy" and the strict evaluation logic.
- Claude's: Helping structure the script narrative to connect data type errors directly to thread exhaustion, showing how a simple string error can trigger a C++ memory fault. I adopted this dual-threat framing for the video.

**What I understand now, and what I still do not.**
- Understood: You cannot secure an LLM with natural language. Security must be handled deterministically downstream by the application framework itself.