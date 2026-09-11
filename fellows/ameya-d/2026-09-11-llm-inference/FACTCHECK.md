# FACTCHECK — llm-inference

Every on-screen figure verified against the project or a published default:

- In the project the model dominated latency (~1288 ms) vs vector search (~4 ms, 0.2%). (PRODUCTION_NOTES.md §4)
- Generation is autoregressive: one token = one forward pass, in sequence. The KV cache reuses past keys/values → O(n²) becomes O(n), at a memory cost. (field-standard)
- Batching trades per-user latency for throughput; quantization (int8/int4) shrinks the model; speculative decoding uses a draft model verified by the target in one pass — identical output. (field-standard)
- Streaming changes perceived latency (TTFT), not total time. Optimise order: stream, route, batch, quantize, prompt-cache. (§4/§5)

Verdict: PASS — no unverifiable numbers on screen; general-knowledge beats are field-standard.
