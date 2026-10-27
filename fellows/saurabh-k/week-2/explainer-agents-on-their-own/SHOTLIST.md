# SHOTLIST — hai-agents-on-their-own

**No open slots.** Every beat renders from a registered Remotion composition; `pantry/` is
empty by design.

| Beat | Act | Composition | Content | Status |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Required fellow intro + AI disclosure + the question | pending |
| B01 | BLUF | `BrutalistHesitantWriter` | Five lines, 160px, steady typing (see constraints) | pending |
| B02 | WHAT | `ClaudeTldrWhat` | The loop; the vanishing pause | pending |
| B03 | TERMS | `ClaudeDefinitions` | Tool / loop / autonomy / guardrail | pending |
| B04 | EVIDENCE | `ClaudeCodeBeat` | **Real** background task event, exit 0 | pending |
| B05 | GUARDRAIL | `ClaudeCodeBeat` | **Real** verbatim "not a message from the user" rule | pending |
| B06 | REFUSAL | `ClaudeCodeBeat` | **Real** gate refusals from the companion build | pending |
| B07 | JUDGE | `ClaudeTldrWhy` | When to let it run, when to look twice | pending |
| B08 | YOUR-TURN | `ClaudeComposerAsk` | Stop-condition prompt | pending |
| B09 | OUTRO | `ClaudeTitleOutro` | Title restate + channel card | pending |

## Constraints carried over from the first build

`eyebrow` ≤5 characters · `ClaudeCodeBeat.title` must be a filename · `folderLabel` set to
`@HumanitariansAI` everywhere it is accepted · `cues` omitted (it takes seconds, not labels)
· no thin glyphs such as `→` in headings · numerals spelled out in body lines · hesitant
writer at 160px / 5 lines / `charMs` 18 with hesitation disabled, so the block is complete
before QC samples it.
