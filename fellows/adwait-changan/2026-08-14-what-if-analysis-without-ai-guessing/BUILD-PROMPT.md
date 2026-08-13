# Build prompt — What-If Analysis Without AI Guessing

Use `brutalist.art` `cli-explainer`. Venv: `source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate`.

1. Read `beat_sheet.json`, `SOURCES.md`, `FACTCHECK.md`.
2. Actual code/artifacts only — excerpts trimmed verbatim from `scenario.py`, `sample-scenarios.json`,
   the schema, and `test_scenario.py`. Do not paraphrase code.
3. Keep the labels exact (SIMULATION_NOT_FORECAST / Recommendation NONE / Decision HUMAN_REQUIRED / PENDING_HUMAN_REVIEW).
4. Gate P signed. Audio → render → compile → visual QC (`_qc/`) → re-render. Never publish.

```bash
REEL="/Users/adwaitchangan/Study/Brutalist/humanitarians-youtube/fellows/adwait-changan/2026-08-14-what-if-analysis-without-ai-guessing"
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL"
./art run "$REEL"; ./art final "$REEL"
```
