# CHECKS-REPORT — Never Trust The Output

Reel: `claude-stem-ai-guardrails` · 9 beats · **measured 130.6s (2:11)** vs 2:45 target
**GATE V (16:9): 18 frames · 0 BLOCKER · 0 MAJOR ✓**

## Deliverables

| | File | Format |
|---|---|---|
| 16:9 master | `claude-stem-ai-guardrails-slate.mp4` | 3840×2160 @ 24fps |
| 9:16 companion | `vertical/claude-stem-ai-guardrails-vertical-slate.mp4` | 1080×1920 @ 24fps |

## Per-beat classification

| Beat | Class | Measured | Pattern |
|---|---|---|---|
| B00 | SHOW | 18.09s | ClaudeComposerAsk |
| B01 | SHOW | 10.67s | BrutalistHesitantWriter — ≥9s ✓ |
| B02 | SHOW | 18.50s | ThreeStageBand |
| B03 | SHOW | 9.24s | ClaudeComposerAsk — clears the ≥7s typing floor |
| B04 | SHOW | 20.97s | **GuardrailCompare** (new) |
| B05 | SHOW | 16.81s | ThreeStageBand — failure mode |
| B06 | SHOW | 13.80s | ClaudeCodeBeat |
| BHTF | SHOW | 14.95s | ClaudeComposerAsk |
| BOUT | SHOW | 7.38s | HaiTitleOutro |

**9 SHOW / 0 HOLD / 0 PUNT.** Slots 9/9. **No slates** — nothing was blocked on
unsupplied material.

## Dual render

**All 9 beats rewired to `916` compositions — zero flagged, zero centre-cut.**
`GuardrailCompare` stacks its two panels in portrait and sizes code from panel width;
`ThreeStageBand` serializes top-to-bottom.

## Defects found and fixed

| Beat | Defect | Fix |
|---|---|---|
| B05 | **The travelling token did not stop at the failed axis** — it sailed past to stage 03, contradicting the beat's entire claim. `ease()` was applied to the already-scaled travel value, so `ease(0.5)` returned `0.875`. | Ease the normalised progress, then scale. Invisible in every prior use because those had `failIndex` at the last stage (scale = 1), so the Week 1 reel was never affected. |
| B03 | Audio 5.9s — the composer prompt could not finish typing. | Narration lengthened to 9.24s. Fourth reel hitting this; the ≥7s floor for typing beats holds. |

GATE V passed the reel 0/0 with the token bug present. Frame-reading found it.

## Teaching arc

```
FRAMEWORK ✓      B01 BLUF + B02 the three-stage chain, before any code.
WORKED EXAMPLE ✓ B04 — a real failure mode (conversational fluff) rejected on screen.
FALSIFIABILITY ✓ B05 — the guard's own costs: latency tax and false positives.
SCAFFOLDED TASK ✓ B06 runnable function; BHTF turns it into a false-positive audit.
BOOKENDS ✓       B00 cold open · B01 BLUF · BHTF handoff · BOUT restate.
NO-SOURCE-NO-VERDICT ✓ no latency, cost or accuracy figure invented.
```

## Open items

1. **Runtime 2:11 vs 2:45 target.** Not padded — duration is an output
   (`duration-planner`). B02 and B04 have room if the target is firm.
2. **Lane-mix warning (not blocking).** `remotion` carries 9/9 beats against MOTION.md's
   ~40% guidance — every beat is a generated diagram or UI.
3. **SKIN LINT warning (expected).** `BOUT` uses `HaiTitleOutro`; `ClaudeTitleOutro`
   hardcodes `@NikBearBrown` and is scoped by OUTRO-LOCK.md.
4. **Paperwork.** Built with `ART_FACTS=0`; a fully gated run needs `FACTCHECK.md`,
   `SHOTLIST.md`, `PROMPTS.md`.
5. **`./art final` not run** — no label-free master yet.
