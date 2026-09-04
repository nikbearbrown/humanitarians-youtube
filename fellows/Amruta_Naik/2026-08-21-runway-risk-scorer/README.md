# Runway-Risk Scorer — Weekly Progress (Week 2)

Weekly project-progress explainer for the AI-Vendor Runway-Risk Scorer. This week
covers hardening the rough prototype into a proper pipeline: splitting the logic
into three named steps (ingest, validate-shape, score) and adding a second output.

## The teach
"Two customers" (P5): one run should serve both a human and a machine. The scorer
now produces a human-readable brief *and* a machine-readable JSON from the same run.
The human reads the brief; other tools can consume the JSON. Same facts, two shapes.
The recipe status is earned by evidence, advancing DRAFT → SPECIFIED only because a
logged run backs it up.

## Production notes
- **Voice:** Kokoro `am_onyx` (fellow-documented voice for this series).
- **Series:** Weekly Progress  ·  **Channel:** @HumanitariansAI
- Rebuilt locally with the brutalist.art toolkit (audio-first). Rendered MP3/MP4
  are intentionally not committed (root .gitignore).

## Files
- `beat_sheet.json` — the source of truth for this video
- `README.md` — this file
