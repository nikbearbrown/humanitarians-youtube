# SHOTLIST - Grounding and Retrieval

## Total: 2:37 (157.66s) · 8 content beats · 9:16 derivative cut

Typed work order, one row per beat. Durations are the measured length of the generated narration, not estimates: the audio is the clock and every beat is conformed to it. Patterns are read from the beat sheet.

| Beat | Act | Pattern | Duration (s) | Carries |
|---|---|---|---|---|
| B00 | COLD OPEN | `ClaudeComposerAsk916` | 15.40 | structure |
| B01 | ACT 1 — WHAT A CITATION NEEDS | `ClaudeScienceLayerStack916` | 16.90 | Three checks. Two are free. |
| B03 | ACT 1 — WHAT A CITATION NEEDS | `ClaudeWindow916` | 15.49 | Two citations pass the automatic checks |
| B05 | ACT 2 — THE ONE IT CANNOT CATCH | `ClaudeWindow916` | 15.17 | Real source. Verbatim quote. False claim. |
| B08 | ACT 3 — WHAT TO ACTUALLY DO | `ClaudeScienceLayerStack916` | 17.11 | Cheap, cheap, then human. |
| BVDT | VERDICT | `ClaudeVerdictArtifact916` | 31.21 | A citation proves reading, not understanding |
| BHTF | YOUR TURN | `ClaudeComposerAsk916` | 25.86 | handoff |
| BOUT | OUTRO | `ClaudeTitleOutro916` | 16.02 | Grounding and Retrieval |
| END |  | `(silent endcard)` | 4.50 |  |

## Open slots

None. Every beat is a Remotion composition rendered from props in `beat_sheet.json`; there is no slate, stock shot or hand-filled slot in this cut. `PROMPTS.md` records that too.

## What this cut drops, and why

See `PEDAGOGY.md` in this folder for the signed cut plan. The code beat is dropped on purpose: portrait is 1080 wide, these functions run 70 to 86 characters per line, and code cannot reflow, so type sized to the longest line is not readable on a phone. Kept beats carry the parent's narration unchanged, so their durations match the long cut exactly; only the outro is new.
