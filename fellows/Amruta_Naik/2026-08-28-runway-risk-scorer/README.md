# Runway-Risk Scorer — Weekly Progress (Week 3)

Weekly project-progress explainer for the AI-Vendor Runway-Risk Scorer. This week
covers rigor: adding two time-aware metrics, pre-registering predictions before
running, and stress-testing the tool with deliberate bad input.

## The teach
Rigor is a set of moves, not a vibe. Predictions are written and committed *before*
the run, so results can't be reshaped after the fact. Break tests feed the tool
deliberately broken input to prove it fails safely — and in this case they caught a
real crash bug, which was fixed. A source-freshness audit flags stale or dead
citations. Status advances to RUNNABLE-SAMPLE only because the evidence — passing
tests, the audit, a logged run — supports it.

## Production notes
- **Voice:** Kokoro `am_onyx` (fellow-documented voice for this series).
- **Series:** Weekly Progress  ·  **Channel:** @HumanitariansAI
- Rebuilt locally with the brutalist.art toolkit (audio-first). Rendered MP3/MP4
  are intentionally not committed (root .gitignore).

## Files
- `beat_sheet.json` — the source of truth for this video
- `README.md` — this file
