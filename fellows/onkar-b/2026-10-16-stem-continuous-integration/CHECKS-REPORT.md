# CHECKS-REPORT — The Regression Problem

Reel: `claude-stem-ci-for-ai` · 9 beats · **measured 127.7s (2:08)** vs 2:45 target
**GATE V (16:9): 18 frames · 0 BLOCKER · 3 MAJOR (underfill, deliberate — see below)**

## Deliverables

| | File | Format |
|---|---|---|
| 16:9 master | `claude-stem-ci-for-ai.mp4` | 3840×2160 @ 24fps |
| 9:16 companion | `vertical/claude-stem-ci-for-ai-vertical.mp4` | 1080×1920 @ 24fps |

**Built straight to `./art final`** — no review cut was ever produced, so no beat chip
and no timecode is drawn in any frame. This also means GATE V ran on both aspects; the
`--review` path skips the gate entirely, which is how edge-bleed went undetected in
earlier portrait cuts.

## Per-beat classification

| Beat | Class | Measured | Pattern |
|---|---|---|---|
| B00 | SHOW | 20.59s | ClaudeComposerAsk |
| B01 | SHOW | 10.94s | BrutalistHesitantWriter — ≥9s ✓ |
| B02 | SHOW | 19.33s | ThreeStageBand (two stages) |
| B03 | SHOW | 18.69s | ThreeStageBand (three stages) |
| BASK | SHOW | 8.09s | ClaudeComposerAsk — clears the ≥7s typing floor |
| B04 | SHOW | 17.51s | CiGateSplit — held MERGE BLOCKED |
| B05 | SHOW | 11.14s | ClaudeCodeBeat |
| BHTF | SHOW | 13.95s | ClaudeComposerAsk |
| BOUT | SHOW | 7.23s | HaiTitleOutro |

**9 SHOW / 0 HOLD / 0 PUNT.** Slots 9/9. No slates. **Zero new components.**

## The 3 MAJORs are deliberate, and here is the reasoning

| Frame | Fill | Verdict |
|---|---|---|
| B01 (×2) | 14% | accepted |
| BOUT | 48% | accepted |

B01's type was raised from the 52–58px used on earlier reels to **92px**, which moved it
from 5% to 14%. Reaching the 55% floor would need roughly four lines at ~170px spanning
most of the frame — that converts a deliberately sparse "writer thinking aloud" beat into
a wall of text and destroys what the beat is for.

`FILL-THE-CANVAS LAW` permits deliberate negative space as a design choice; what it
targets is *accidental* dead space under **undersized** type. At 92px the type is not
undersized. Same reasoning for the outro poster card at 48%.

Recorded as an accepted warning rather than silently ignored. If you'd rather these pass
the gate outright, it is a prop change plus two re-renders.

## Corrections carried into the reel

1. **Branch protection (B05).** Scene 4 claims the pipeline "physically locks the
   repository". True only when the Actions check is marked **required** — otherwise CI
   reports red and the merge button still works. The reel says so.
2. **"mathematical certainty" softened.** CI gives enforcement and repeatability, not a
   proof. Narration says "the difference between hoping your guardrails held and knowing
   they did".

## Teaching arc

```
FRAMEWORK ✓      B01 BLUF + B02 what is assertable, before any pipeline.
WORKED EXAMPLE ✓ B03 the pipeline · B04 a real PR that cannot merge.
FALSIFIABILITY ✓ B04 — the deleted regex is caught in isolation.
SCAFFOLDED TASK ✓ B05 a runnable workflow + the required-check setting.
BOOKENDS ✓       B00 cold open · B01 BLUF · BHTF handoff · BOUT restate.
NO-SOURCE-NO-VERDICT ✓ no accuracy, decay rate or suite size claimed as measured.
```

## Open items

1. **PR #58 and the 41-of-64 counts are illustrative** — no repository was supplied.
2. **Runtime 2:08 vs 2:45 target.** Not padded; duration is an output.
3. **Lane-mix warning (not blocking).** `remotion` carries 9/9 beats.
4. **SKIN LINT warning (expected).** `BOUT` uses `HaiTitleOutro`.
