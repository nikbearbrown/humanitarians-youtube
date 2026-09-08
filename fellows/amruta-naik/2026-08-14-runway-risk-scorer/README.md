# Runway-Risk Scorer — Weekly Progress

A weekly project-progress explainer documenting the build of the AI-Vendor
Runway-Risk Scorer: a recipe that reads a company's validated funding signals,
produces a sourced runway-risk brief, and halts at a human gate for the risk
judgment. The machine computes the signals; a human decides.

## The teach
The distinctive design decision is the **human gate** (Snickerdoodle P1): the tool
surfaces sourced facts — total raised, months since last raise, funding-stage
trend, distress signals, freshness — but never issues a verdict on whether a
vendor is "safe." Execution is automated; judgment stays human.

## Production notes
- **Voice:** Kokoro `am_onyx` (fellow-documented voice for this report series).
- **Series:** Weekly Progress
- **Channel:** @HumanitariansAI
- **Rebuild:** local, audio-first, via the brutalist.art toolkit. The beat sheet
  drives narration; measured audio is the clock; visual beats compile from the
  beat sheet. Rendered MP3/MP4 are intentionally not committed (root .gitignore).

## Files
- `beat_sheet.json` — the source of truth for this video (copy in from your render folder)
- `README.md` — this file
