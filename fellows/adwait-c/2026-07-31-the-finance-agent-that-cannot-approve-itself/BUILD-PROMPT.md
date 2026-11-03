# Build prompt — The Finance Agent That Cannot Approve Itself (this week)

Use the `brutalist.art` `cli-explainer` workflow on this folder. Run from the Python 3.12 venv:
`source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate`.

1. Read `beat_sheet.json`, `SOURCES.md`, `FACTCHECK.md`.
2. Actual code and artifacts only — excerpts are trimmed verbatim from `review.py`, the schema,
   and `test_review.py` under the Mycroft project root. Do not paraphrase code.
3. Keep the disclosures intact (local / no external LLM / sample request OPEN / nothing
   fabricated). Voice `am_onyx`, persistent for this fellow.
4. Gate P is signed in `PEDAGOGY.md`. Generate audio (master clock), render Remotion beats,
   compile, run frame-level visual QC (`_qc/`), fix root causes, re-render.
5. Never publish. A successful render is not authorization to upload.

```bash
REEL="/Users/adwaitchangan/Study/Brutalist/humanitarians-youtube/fellows/adwait-changan/2026-07-31-the-finance-agent-that-cannot-approve-itself"
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL"
./art run "$REEL"      # review cut + QC
./art final "$REEL"    # 4K master
```
