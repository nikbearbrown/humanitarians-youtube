# Frictional Log

## 2026-11-22: When history misleads

- **Work and expectation:** explain what happens to an autoscaling agent when the history it reads is wrong. I expected the agent to fall back to roughly what HPA does.
- **What I tried:** replayed every test day with yesterday or last week changed before the agent sees it (20% of its load, 3 times its load, or zero), while the day being served stays real, and compared each run with HPA at the same cost. Then trained the same agent with misleading history in 30% of its training episodes.
- **Where it resisted:**
  - The agent trained on normal history does worse than HPA in 42% of the cases, and in the worst case has 93% more late requests. It trusts the past completely.
  - It is also fooled by a misleading last week, not only by yesterday, because it reads both.
  - Training with misleading history raises the share of wins to 76% and cuts the worst case to 64% more late requests, but HPA, which reads no history, still cannot be fooled at all.
- **AI and other contributions:** Claude Code wrote the test and the evidence script and made the video under my direction; I chose the topic and reviewed the results. Narration is an AI voice (Kokoro `af_bella`).
- **What I understand now:** an agent that learns from history must also train on history that is wrong. The test cases here are the same kinds the agent trained on, so real irregular days are the stronger test.
- **Evidence:** [README](README.md#watch-and-review), [FACTCHECK.md](FACTCHECK.md), [evidence/evidence.json](evidence/evidence.json)
