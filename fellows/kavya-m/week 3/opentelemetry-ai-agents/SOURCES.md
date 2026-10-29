# SOURCES — kavya-opentelemetry-ai-agents

| Source | Used for | Notes |
|---|---|---|
| `demo/otel_demo.py` (this folder) | Every figure in B00, B03, B04 and B06 | Python stdlib only, synthetic clock, deterministic. No network, no keys, no model calls, no OpenTelemetry SDK |
| `demo/otel_demo_output.txt` | Verbatim stdout shown in B03/B04 | Regenerate with `python -I demo/otel_demo.py > demo/otel_demo_output.txt` |
| OpenTelemetry project (CNCF): tracing concepts and the GenAI semantic conventions | B01, B02 framing; span names (`invoke_agent`, `chat`, `execute_tool`) and `gen_ai.*` attribute keys in the demo | General documented knowledge of the open standard; not quoted. The GenAI conventions are marked "development" and may change |
| `youtube/claude-liam-opentelemetry-ai-agents/beat_sheet.json` | Failure scenario (an empty, too-fast retrieval leading to a made-up citation) | Unrendered draft in this repo with authored figures. Rebuilt as running code under Kavya's name |

No external articles, images or footage are used. The research question, index and answer are synthetic.

## Seeds and determinism

- `BrutalistHesitantWriter` seed: `kavya-otel-agents-5821`
- Trace id derives from a SHA-256 of the question, so it is identical on every run (`5b7c0316…`).
