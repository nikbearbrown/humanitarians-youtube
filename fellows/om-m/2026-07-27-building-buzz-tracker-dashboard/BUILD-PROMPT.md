# Build prompt — Turning Hacker News Talk Into an AI Attention Signal

Use the brutalist-art `cli-explainer`/workflow-explainer style on this folder — this is a
progress showcase of a real, working system (the "Mycroft" n8n agent), not a research explainer
about an external topic.

1. Read `beat_sheet.json`, `SOURCES.md`, and `FACTCHECK.md` before touching narration.
2. This is a **real fellow, real project** — unlike the fictional `maya-r/` example series, do
   not add a fictional-person disclosure. Do, however, keep every claim about the private
   n8n/Postgres/Groq system limited to what the author (Om Mali) can actually confirm — see the
   author-asserted claims table in `FACTCHECK.md`.
3. Om Mali selected Kokoro `am_onyx` for this report. Confirm that choice is still current before
   generating new audio; a change is an explicit, documented re-voice decision, not a per-episode
   default.
4. Before any new render: get the author's sign-off on the 13 rows in `FACTCHECK.md` — these are
   specific, falsifiable claims about a private system (bug counts, point thresholds, a real
   misattribution incident) that only the author can verify.
5. All 19 beats are already filled from the original build (4 Remotion cards/graphics, 15
   screenshot stills). No new asset generation should be needed unless content changes.
6. If narration changes: regenerate only the affected beat's audio, remeasure, and update
   `beat_sheet.json`'s `actual_duration_s` — do not hand-edit timing.
7. Never publish without the author's explicit go-ahead. The rendered MP4 and per-beat mp3/mp4
   files live in the original build location, not in this repo copy — see `README.md`.
