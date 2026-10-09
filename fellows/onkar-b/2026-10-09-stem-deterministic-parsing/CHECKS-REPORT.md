# CHECKS-REPORT — The Tokenization Problem

Reel: `claude-stem-tokenization-problem` · 9 beats · **measured 135.6s (2:16)** vs 2:45 target
**GATE V (16:9): 18 frames · 0 BLOCKER · 0 MAJOR ✓**

## Deliverables

| | File | Format |
|---|---|---|
| 16:9 master | `claude-stem-tokenization-problem-slate.mp4` | 3840×2160 @ 24fps |
| 9:16 companion | `vertical/claude-stem-tokenization-problem-vertical-slate.mp4` | 1080×1920 @ 24fps |

## Per-beat classification

| Beat | Class | Measured | Pattern |
|---|---|---|---|
| B00 | SHOW | 19.93s | ClaudeComposerAsk |
| B01 | SHOW | 13.50s | BrutalistHesitantWriter — ≥9s ✓ |
| B02 | SHOW | 18.54s | ThreeStageBand (two stages) |
| B03 | SHOW | 16.04s | ThreeStageBand — failure mode |
| B04 | SHOW | 8.92s | ClaudeComposerAsk — clears the ≥7s typing floor |
| B05 | SHOW | 22.29s | GuardrailCompare — passing stamp |
| B06 | SHOW | 12.89s | ClaudeCodeBeat |
| BHTF | SHOW | 17.15s | ClaudeComposerAsk |
| BOUT | SHOW | 6.25s | HaiTitleOutro |

**9 SHOW / 0 HOLD / 0 PUNT.** Slots 9/9. No slates. **Zero new components.**

## The script's Scene 4 result needs a mapping parser — the reel builds one

Scene 4 says the regex layer turns `$5.0M` into `5000000.0`. A strip-based regex returns
`5.0`; the `M` is non-numeric and goes with the noise. The parser shown maps `K/M/B` to
multipliers, which is what actually produces the stated output — **verified by running
it**. The narration makes this the teaching point rather than papering over it.

Also verified by execution: `int('$5.0M')` raises
`ValueError: invalid literal for int() with base 10: '$5.0M'` — the message shown in B03
is exactly what CPython emits.

Same error class as Week 5's STEM script. Both described a stripping normalizer and
claimed an output stripping cannot produce.

## Defect found and fixed

| Beat | Defect | Fix |
|---|---|---|
| B05 | The verdict stamp faded in, so white text sat on a **part-transparent** terracotta fill over cream — below the contrast floor. Because clips are trimmed to measured audio, the fade occupied most of the stamp's visible life. GATE V flagged this on the sibling reel. | Filled stamps never fade: they slide in at full opacity, and arm at p≈0.60 so they are solid long before the cut. Fixed in `GuardrailCompare`, which also improves the Week 4 STEM reel. |

This is the third distinct way clip-trimming has caused a defect — after tails being cut
outright, and a label ramping later than its own fill.

## Teaching arc

```
FRAMEWORK ✓      B01 BLUF + B02 why output varies, before any failure.
WORKED EXAMPLE ✓ B03 the pipeline breaking · B05 the same string surviving.
FALSIFIABILITY ✓ B03 — the type boundary is where prompt engineering stops helping.
SCAFFOLDED TASK ✓ B06's four inputs must agree; BHTF hunts confidently wrong parses.
BOOKENDS ✓       B00 cold open · B01 BLUF · BHTF handoff · BOUT restate.
NO-SOURCE-NO-VERDICT ✓ every factual claim on screen was executed, not reasoned.
```

## Open items

1. **Runtime 2:16 vs 2:45 target.** Not padded; duration is an output.
2. **Lane-mix warning (not blocking).** `remotion` carries 9/9 beats.
3. **SKIN LINT warning (expected).** `BOUT` uses `HaiTitleOutro`.
4. **Paperwork.** Built with `ART_FACTS=0`.
5. **`./art final` not run** — no label-free master yet.
