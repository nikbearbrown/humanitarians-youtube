# SHOTLIST — claude-liam-context-window-vertical (9:16, 12 beats)
## Total: 1:03 (63.16s) · 12 beats

Full-length portrait companion to the 16:9 reel — same narration, audio
durations, facts and sources, with native portrait graphics (not a crop).
Why each beat differs from the 16:9 version: `BUILD-LOG.md` (portrait-only
decisions). Cut/merge history from the long cut: `../SHOTLIST.md`.

| Beat | Act | Pattern | Duration (s) | Notes |
|---|---|---|---|---|
| B00 | OPEN | `ClaudeComposerAsk916` | 5.50 | Cold open; `largeText: true` |
| B01 | BLUF | Manim `B01_HesitantWriter` | 3.19 | Two lines: "A context window is" / "Claude's memory." → "a fixed budget." Stands in for `BrutalistHesitantWriter` (portrait size floor) |
| B02 | I | `FormBCard916` | 3.89 | System prompt / Tool definitions / Conversation history |
| B03 | I | `FormBCard916` | 4.06 | Your message / Claude's reply |
| B04 | II | Manim `B04_TokenSplit` | 6.02 | Portrait restack: tokens ≠ words, running-total bar in the bottom third |
| B05 | II | `FormBCard916` | 4.68 | Code / Numbers / Jargon / Text in other languages; one-line subs |
| B06 | III | Manim `B06_CeilingClimb` | 7.10 | Room-remaining climb to the fixed ceiling, `ILLUSTRATIVE` on screen; stands in for `AttritionChain` (no portrait variant) |
| B07 | III | `FormBCard916` | 5.04 | Error / Summary / Dropped turns — depends on the app |
| B08 | IV | `FormBCard916` | 5.06 | Small / Medium / Large / Very large — filling more costs more |
| B09 | CLOSE | `ClaudeVerdictArtifact916` | 6.79 | Summary restates the thesis; `qc.sparse_by_design` |
| B10 | CLOSE | `ClaudeComposerAsk916` | 6.07 | YOUR TURN; `largeText: true`, status line dropped |
| B11 | CLOSE | Manim `B11_OutroCard` | 5.76 | `@HumanitariansAI` / "The Context Window Isn't Memory."; stands in for `OutroSeries` (no portrait variant) |

Every `FormBCard916` item carries `icon: "BOX"`.
