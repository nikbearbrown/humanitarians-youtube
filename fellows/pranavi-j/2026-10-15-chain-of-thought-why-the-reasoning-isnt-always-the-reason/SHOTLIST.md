# SHOTLIST — Chain-of-Thought: Why the Reasoning Isn't Always the Reason
## Total: 134.83s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.06s | Silent title card: "Chain-of-Thought: Why the Reasoning Isn't Always the Reason" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 12.38s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_ChainHook (scenes.py) | 14.02s | A confident, well-formatted 4-step reasoning chain ending in an answer, then a question-mark overlay: "...or is it?" |
| B03 | FRAMEWORK | manim | GRAPHIC | B03_ThreeTestsFramework (scenes.py) | 25.58s | All 3 tests (Swap a Step / Hide a Hint / Strip It Out) shown together, before any example |
| B04 | WORKED-EXAMPLE | manim | GRAPHIC | B04_HintVsReasoning (scenes.py) | 24.67s | A multiple-choice prompt with an embedded authority hint on one side, the model's stated reasoning on the other — visibly never mentioning the hint despite the answer matching it |
| B05 | FALSIFIABILITY | manim | GRAPHIC | B05_PerturbedStepFalsifiability (scenes.py) | 23.54s | A 3-step arithmetic chain run twice: original, then with one intermediate step's number changed — the final answer visibly changes to match, a checkmark where B04 had a mismatch |
| B06 | SCAFFOLDED-TASK | manim | GRAPHIC | B06_AuditChecklist (scenes.py) | 18.62s | The 3 tests restated as a concrete, actionable checklist to try today — distinct composition from B03's framework card |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 10.44s | Statement card: a reasoning trace that reads well isn't the same as one that's true — test whether the steps are load-bearing |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." — short card matching this beat's short approved narration |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py`. No
  pantry stills, no Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`)
  copied from this fellow's sibling reel
  `2026-10-06-lost-in-the-middle-why-more-context-isnt-better` (same fellow,
  same voice, same series, built this session with the same toolkit version)
  for house-style consistency. The reasoning-chain helpers (`chain_step()`,
  `small_arrow()`, `build_chain()`) are new to this reel, built for its
  specific mechanism (a vertical chain of numbered reasoning-step boxes
  connected by arrows, ending in an answer box), and reused across
  B02/B04/B05.
- This is a general AI/STEM topic explainer, not a report of real engineering
  work — the worked example (B04's hint-vs-reasoning agronomy scenario) and
  its falsifiability case (B05's perturbed arithmetic chain) are both fully
  generic/hypothetical, no real model, vendor, or disclosed benchmark is
  named or resembled (see FACTCHECK.md, SOURCES.md). No fabricated
  percentage/statistic is shown anywhere.
- B03 is this reel's framework beat: all 3 tests are shown together, fully,
  before any worked example — matching the Legibility Contract.
- B04/B05 are a matched pair: identical 3-step chain structure and answer-box
  idiom, differing only in content and resolution (B04 ends in a gold
  "HINT NEVER MENTIONED" mismatch tag; B05 ends in a teal "ANSWER CHANGED, AS
  PREDICTED" checkmark tag) — a visibly distinct resolution, not a restated
  assertion.
- B06's checklist is a concrete action (3 checkbox rows, distinct
  composition), not a second copy of B03's framework card.

## Vertical companion
`vertical/scenes.py` holds the native-portrait redesign of all 9 beats,
built for `./art vertical` — see that file's module docstring for the
per-beat side-by-side -> stacked notes (B04's prompt/reasoning and B05's
original/perturbed chains restacked top/bottom for the narrow canvas).

## QC status
See `BUILD-LOG.md` for GATE A/V results and per-beat visual-inspection
findings from the render pipeline.
