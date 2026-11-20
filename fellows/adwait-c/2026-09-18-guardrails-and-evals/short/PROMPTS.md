# PROMPTS - Guardrails and Evals

`PROMPTS.md` exists to carry a beat-prefixed prompt for every **open slot**: a beat whose picture a human or a generator still has to supply.

**This cut has no open slots.** Every beat is a Remotion composition rendered deterministically from props committed in `beat_sheet.json`, so there is nothing to prompt for and nothing to fill in by hand. Re-running the build reproduces the same frames from the same inputs.

The per-beat work order is below for review; the authoritative copy of each beat's props is the beat sheet.

| Beat | Composition | Source of its content |
|---|---|---|
| B00 | `ClaudeComposerAsk916` | `beat_sheet.json` -> beats[B00].shot.remotion.props |
| B01 | `ClaudeScienceLayerStack916` | `beat_sheet.json` -> beats[B01].shot.remotion.props |
| B02 | `ClaudeWindow916` | `beat_sheet.json` -> beats[B02].shot.remotion.props |
| B04 | `ClaudeWindow916` | `beat_sheet.json` -> beats[B04].shot.remotion.props |
| B09 | `CwcConceptCard916` | `beat_sheet.json` -> beats[B09].shot.remotion.props |
| BVDT | `ClaudeVerdictArtifact916` | `beat_sheet.json` -> beats[BVDT].shot.remotion.props |
| BHTF | `ClaudeComposerAsk916` | `beat_sheet.json` -> beats[BHTF].shot.remotion.props |
| BOUT | `ClaudeTitleOutro916` | `beat_sheet.json` -> beats[BOUT].shot.remotion.props |
| END | `(silent endcard)` | silent endcard, no props |

If a future revision introduces a slate or a stock shot, its prompt belongs here, prefixed with the beat id.
