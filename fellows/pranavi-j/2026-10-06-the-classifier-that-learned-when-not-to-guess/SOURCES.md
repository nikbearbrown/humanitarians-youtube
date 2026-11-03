# Sources — The Classifier That Learned When Not to Guess

All claims in this video trace to this fellow's own work on Project 29 (`mycroft`), verified live
this session — no external sources needed.

1. `mycroft/scripts/regulatory-intel/FINDINGS.md` — original B2 problem statement (2026-07-24).
2. `mycroft/scripts/regulatory-intel/B2-VERIFICATION.md` — both the original 2026-08-30
   `dc:creator` fix and the 2026-10-06 addendum (this video's subject) documenting the live
   verification numbers.
3. `mycroft/logs/RUN_LOG.md` — run-log entries for the 2026-08-30 B2 fix, the 2026-08-30 Unknown
   Source investigation (first identified the 8-item residual), and the 2026-10-06 addendum.
4. `mycroft/scripts/regulatory-intel/workflow.dev.json` — the shipped `Layer 2 - LLM Source
   Classification` node, verified directly by reading the committed code.
5. Live `mycroft_intelligence` Postgres DB (`localhost:5431`) — the real 21 `Unknown Source` rows
   queried directly this session.
6. Local Ollama instance (`llama3.2:3b`) — the model actually called during verification, not a
   simulated/mocked response.
