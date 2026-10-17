# FACTCHECK - rag-eval-production

Grounded in PRODUCTION_NOTES.md §6/§7:
- Offline eval = fixed golden set before deploy; correctness computable (hit@k, MRR, faithfulness).
- Golden set in CI blocks deploy on MRR/faithfulness drop (regression gate).
- Online monitoring: no labels on live traffic; watch proxies - score distributions (alert when mean top-1 declines), refusal rate, latency, cost, user feedback.
- Trace (LangSmith-style): per-request - retrieved chunks+scores, prompt sent, response, latency per stage, tokens+cost.
- Debug retrieval first.
Verdict: PASS - all claims trace to PRODUCTION_NOTES.md.
