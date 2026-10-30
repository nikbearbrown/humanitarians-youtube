# SHOTLIST - Guardrails and Evals

## Total: 2:25 (145.08s) · 8 content beats · 9:16 derivative cut

Typed work order, one row per beat. Durations are the measured length of the generated narration, not estimates: the audio is the clock and every beat is conformed to it. Patterns are read from the beat sheet.

| Beat | Act | Pattern | Duration (s) | Carries |
|---|---|---|---|---|
| B00 | COLD OPEN | `ClaudeComposerAsk916` | 16.38 | structure |
| B01 | ACT 1 — THE HOURS DO NOT EXIST | `ClaudeScienceLayerStack916` | 12.67 | Ninety seconds, every run. |
| B02 | ACT 1 — THE HOURS DO NOT EXIST | `ClaudeWindow916` | 15.13 | Human hours per day, at ninety seconds a run |
| B04 | ACT 2 — SAMPLING IS NOT THE ANSWER | `ClaudeWindow916` | 14.57 | What a clean sample is compatible with |
| B09 | ACT 3 — SO SAMPLE MORE? | `CwcConceptCard916` | 13.42 | They Catch What You Thought Of |
| BVDT | VERDICT | `ClaudeVerdictArtifact916` | 37.82 | You cannot read your way to confidence |
| BHTF | YOUR TURN | `ClaudeComposerAsk916` | 18.84 | handoff |
| BOUT | OUTRO | `ClaudeTitleOutro916` | 11.75 | Guardrails and Evals |
| END |  | `(silent endcard)` | 4.50 |  |

## Open slots

None. Every beat is a Remotion composition rendered from props in `beat_sheet.json`; there is no slate, stock shot or hand-filled slot in this cut. `PROMPTS.md` records that too.

## What this cut drops, and why

See `PEDAGOGY.md` in this folder for the signed cut plan. The code beat is dropped on purpose: portrait is 1080 wide, these functions run 70 to 86 characters per line, and code cannot reflow, so type sized to the longest line is not readable on a phone. Kept beats carry the parent's narration unchanged, so their durations match the long cut exactly; only the outro is new.
