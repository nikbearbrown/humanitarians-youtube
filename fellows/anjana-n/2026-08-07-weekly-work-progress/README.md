**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 6 — Model Experimentation

**Timeline:** August 2, 2026 – August 8, 2026

**Scope:** Integration of Mistral-7B-Instruct, comparative extraction against Llama 3.1 8B, cross-run signal alignment, and dashboard support for model comparison.

---

## Mistral-7B Configuration
- Mistral-7B-Instruct deployed through Ollama alongside Llama 3.1 8B
- **Architecture review:**
  - Grouped-query attention with sliding-window attention
  - Instruction-tuning approach
  - Expected behaviour on financial text

## Mistral Extraction Run
- Executed on a representative ticker subset with an identical pipeline:
  - Same prompts
  - Same few-shot retrieval
  - Same self-consistency decoding
- **Issue:** JSON output truncated in roughly 10–15% of extractions
- **Mitigation:** explicit closing-bracket reminders and tightened output-schema instructions

## Cross-Model Scorecard Comparison
- **Metrics compared:**
  - Brier score and skill score
  - Calibration curves and Murphy decomposition
  - Self-consistency behaviour
  - Hallucination rate
- **Results:**

| Dimension | Llama 3.1 8B | Mistral-7B |
|---|---|---|
| Calibration | Stronger | Slightly weaker |
| Resolution at the maintained/none boundary | Weaker | — |
| Resolution on hedged language | — | Stronger |
| Explicit numerical guidance | Outperforms | — |
| Qualitative / hedged communication | — | Outperforms |
| Hallucination profile | Temperature-stable; caught by multi-turn verification | Temperature-variable; caught by self-consistency, with more abstentions |

- Per-ticker skill scores diverge, which indicates the two models have complementary strengths

## Cross-Model Signal Alignment
- **Issue:** chunk index was an unreliable join key because preprocessing used a non-deterministic sort
- **Fix:** content hash adopted as the stable join key across runs

## Dashboard and Documentation
- **Model comparison view:** added to the Streamlit dashboard
- **Reader comparison table:** extended with per-model metrics
- **Architecture video overview:** produced with the video tooling introduced during Office Hours with Professor Brown
