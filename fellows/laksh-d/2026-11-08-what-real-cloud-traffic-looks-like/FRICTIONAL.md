# Frictional Log

## 2026-11-08: What real cloud traffic looks like

- **Work and expectation:** explain, with real measurements, why test traffic for an autoscaler has to look like real traffic. I expected the numbers from my project's analysis to carry over to the video unchanged.
- **What I tried:** recomputed every number on screen from the repository with one script (`evidence/make_evidence.py`) instead of copying figures from notes.
- **Where it resisted:**
  - The figure "5% of bursts would repeat by chance" did not reproduce. Placing the same bursts at random times gives about 10% to 17%. The video states the real 73% for one app and says only that random timing gives far fewer.
  - "About a third of bursts rise in the minute before" needs a definition. I used: the previous minute is more than 15% (one noise width) above the trailing 30-minute median. That gives 33%.
  - My first made-up generator was replaced before the first commit, so the chart of it is redrawn from its settings (5% noise, a 10-minute ramp) and labelled "redrawn".
- **AI and other contributions:** Claude Code wrote the narration and scenes and rendered the video; the measurements come from my project. Narration is an AI voice (Kokoro `af_bella`).
- **What I understand now:** noise level, bursts per day and how fast bursts peak are three numbers anyone can measure from their own logs. If test traffic does not match them, a test can pass against traffic that does not exist.
- **Evidence:** [README](README.md#watch-and-review), [FACTCHECK.md](FACTCHECK.md), [evidence/evidence.json](evidence/evidence.json)
