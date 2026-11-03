# SHOTLIST — state-space-models-and-mamba
## Total: 3:35.3 (215.31s) · 12 beats · 16:9 · Kokoro am_onyx

Deliverable: `StateSpaceModelsAndMamba_UdaySonawane_2026-08-27.mp4`
Channel: `claude-hai` — @HumanitariansAI, Pragmatist register, student audience.

Durations are the MEASURED Kokoro audio. Manim run-times were written to match
them; never the other way round.

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | INTRO | bookend | REMOTION | ClaudeComposerAsk | 5.29s | Cold open; name spoken; greeting "Hej, HAI" |
| B01 | BLUF | manim | MANIM | `B01_CostCurves` | 17.69s | EXECUTIVE-SUMMARY LAW; quadratic vs linear curves |
| B02 | FRAMEWORK | manim | MANIM | `B02_ThreeAxes` | 17.88s | **The rubric** — STATE/UPDATE/COST. Starts 22.98s, before any scoring |
| B03 | WORKED EXAMPLE | manim | MANIM | `B03_ScoreIncumbents` | 21.29s | RNN + Transformer scored; both columns held together |
| B04 | MECHANISM | manim | MANIM | `B04_SSMRecurrence` | 19.61s | SSM equations as plain Text (no LaTeX) + fixed-state chain |
| B05 | MECHANISM | manim | MANIM | `B05_S4Fixed` | 22.21s | Same A B C per token; cites arXiv:2111.00396 |
| B06 | MECHANISM | manim | MANIM | `B06_MambaSelection` | 22.10s | Per-token Δ B C; cites arXiv:2312.00752 |
| B07 | EVIDENCE | manim | MANIM | `B07_PaperNumbers` | 20.78s | 4 sourced claim cards; citation on screen |
| B08 | FALSIFIABILITY | manim | MANIM | `B08_CopyingCeiling` | 27.11s | Side-by-side, held; cites arXiv:2402.01032 |
| B09 | VERDICT | manim | MANIM | `B09_Verdict` | 18.39s | Mamba scored + USE IT / BE CAREFUL |
| B10 | YOUR TURN | bookend | REMOTION | ClaudeComposerAsk | 18.99s | Scaffolded task + GOOD/BAD discriminator |
| B11 | OUTRO | bookend | REMOTION | ClaudeTitleOutro | 3.97s | Title restate; name in subline |

## Lane histogram

```
MANIM     9 beats  187.06s  (86.9%)   every middle beat — ILLUSTRATE LAW
REMOTION  3 beats   28.25s  (13.1%)   bookends only
PANTRY    0 beats    0.00s  (  0.0%)
SLATE     0 beats    0.00s  (  0.0%)
```

**ILLUSTRATE LAW check:** the Claude UI appears in exactly three beats — the
cold open, the handoff, and the outro. Every middle beat illustrates its own
concept. That is the correct split for an ai-explainer; the previous reel was a
cli-explainer, where the interface IS the subject and the ratio inverts.

## Open slots

**None.** Nine Manim scenes from `scenes.py`, three registered Claude components.

## Citation coverage

Four beats carry a visible source line: B05, B06, B07, B08. Every numeric or
attributed claim in the reel sits in one of those four.
