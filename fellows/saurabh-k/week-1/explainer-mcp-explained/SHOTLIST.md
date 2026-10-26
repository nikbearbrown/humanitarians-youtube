# SHOTLIST — hai-mcp-explained

Typed work order. **No open slots** — every beat renders from a registered Remotion
composition; nothing is slated and nothing is waiting on supplied media. `pantry/` is empty
by design.

| Beat | Act | Composition | Lane | Source of content | Status |
|---|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | remotion | Required fellow intro + AI-narration disclosure + the question the film answers | rendered |
| B01 | BLUF | `BrutalistHesitantWriter` | remotion | Six short typed lines; the correction is the pedagogy | rendered |
| B02 | WHAT | `ClaudeTldrWhat` | remotion | Two-sided protocol, three lines | rendered |
| B03 | WHY | `ClaudeTldrWhy` | remotion | Integration arithmetic, spelled out (no numerals — GATE T ink floor) | rendered |
| B04 | TERMS | `ClaudeDefinitions` | remotion | Host / client / server / tool | rendered |
| B05 | EVIDENCE | `ClaudeCodeBeat` | remotion | **Real** `~/.claude.json`, two servers, two transports | rendered |
| B06 | ANATOMY | `ClaudeCodeBeat` | remotion | **Real** `list_browser_targets` tool schema | rendered |
| B07 | RESULT | `ClaudeCodeBeat` | remotion | **Real** call + real five-tab result | rendered |
| B08 | JUDGE | `ClaudeTldrWhy` | remotion | When to use it, when to look twice (HAI spine question) | rendered |
| B09 | YOUR-TURN | `ClaudeComposerAsk` | remotion | Suggested prompt for the viewer to run | rendered |
| B10 | OUTRO | `ClaudeTitleOutro` | remotion | Title restate + channel card | rendered |

## Constraints discovered during this build

- `eyebrow` on the Tldr scenes is a **≤5 character display mark**, not a phrase — the
  greeting block begins 470px in and anything longer collides with it.
- `ClaudeCodeBeat`'s `title` is echoed as the language badge, so it must read as a
  **filename**.
- `cues` on `ClaudeTldrWhy` is `z.array(z.number())` — **seconds**, not labels.
- `folderLabel` defaults to `@NikBearBrown` and must be set to `@HumanitariansAI` on every
  scene that accepts it.
- Isolated numerals and thin glyphs (`→`) measure under GATE T's 41px ink floor at body
  sizes. Spell numbers out; avoid arrows in headings.
