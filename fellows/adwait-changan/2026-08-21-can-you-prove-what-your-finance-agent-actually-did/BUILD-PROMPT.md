# Build prompt — Can You Prove What Your Finance Agent Actually Did?

Use `brutalist.art` `cli-explainer`. Venv: `source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate`.

1. Read `beat_sheet.json`, `SOURCES.md`, `FACTCHECK.md`.
2. Actual code/artifacts only — excerpts trimmed verbatim from `bundle.py`, the schema, and
   `test_bundle.py` (PR #17). Do not paraphrase code.
3. Keep the disclosures exact (SHA-256 = integrity not approval; DRAFT; BLOCKED_PENDING_HUMAN_REVIEW; five gates).
4. Gate P signed. Audio → render → compile → visual QC (`_qc/`) → re-render. Never publish.

```bash
REEL="/Users/adwaitchangan/Study/Brutalist/humanitarians-youtube/fellows/adwait-changan/2026-08-21-can-you-prove-what-your-finance-agent-actually-did"
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL"
./art run "$REEL"; ./art final "$REEL"
```
