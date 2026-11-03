# Build prompt — How Do You Test a Finance Agent? Break the Books on Purpose

Use `brutalist.art` `cli-explainer`. Venv: `source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate`.

1. Read `beat_sheet.json`, `SOURCES.md`, `FACTCHECK.md`.
2. Actual code/artifacts only — excerpts trimmed verbatim from `evaluation.py`, `cases.json`,
   the schema, and `test_evaluation.py`. Do not paraphrase code.
3. Keep the disclosures (deterministic / no external LLM / only these synthetic cases / PENDING_HUMAN_REVIEW).
4. Gate P signed. Audio → render → compile → visual QC (`_qc/`) → re-render. Never publish.

```bash
REEL="/Users/adwaitchangan/Study/Brutalist/humanitarians-youtube/fellows/adwait-changan/2026-08-07-how-do-you-test-a-finance-agent"
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL"
./art run "$REEL"; ./art final "$REEL"
```
