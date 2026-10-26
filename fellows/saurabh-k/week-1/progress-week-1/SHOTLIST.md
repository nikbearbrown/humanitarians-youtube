# SHOTLIST — hai-brutalist-week-1

**No open slots.** Every beat renders from a registered Remotion composition; there is no
`pantry/` and no captured media. The two code cards show real output from this week's builds.

| Beat | Act | Composition | Content | Status |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Fellow intro + AI-voice disclosure + the week's question | rendered |
| B01 | BLUF | `BrutalistHesitantWriter` | Four lines: shipped with it, and found a silent gate | rendered |
| B02 | WHAT | `ClaudeTldrWhat` | Beat sheet in, 4K master out, refuses bad frames | rendered |
| B03 | TERMS | `ClaudeDefinitions` | Beat sheet / lane / gate / master | rendered |
| B04 | EVIDENCE | `ClaudeCodeBeat` | **Real** shipped count and durations (ffprobe-verified) | rendered |
| B05 | FINDING | `ClaudeCodeBeat` | **Real** GATE T output: skipped → FAIL 8/10 | rendered |
| B06 | JUDGE | `ClaudeTldrWhy` | Silence is not success; portrait is its own design | rendered |
| B07 | YOUR-TURN | `ClaudeComposerAsk` | Make your most-trusted check fail on purpose | rendered |
| B08 | OUTRO | `ClaudeTitleOutro` | Title restate + channel card | rendered |

## Constraints honoured

- **B05 is the spine of the film.** It must stay verbatim toolkit output — it is the one
  beat where the evidence is a failure of my own build, not an illustration.
- **B02 / B06 openers avoid `W` and `A`.** A heavy serif's left side-bearing paints ~2px
  outside the title-safe box when a run starts at `SAFE.x`, which GATE T §8.2 flags.
- **B04 / B05 are real code, not prose.** GATE T §8.12 rejects a code card whose every line
  is prose, so both cards show actual JSON rather than a sentence list.
