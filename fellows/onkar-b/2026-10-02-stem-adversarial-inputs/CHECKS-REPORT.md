# CHECKS-REPORT — The Model Is The Threat

Reel: `claude-stem-adversarial-inputs` · 9 beats · **measured 129.3s (2:09)** vs 2:45 target
**GATE V (16:9): 18 frames · 0 BLOCKER · 0 MAJOR ✓**

## Deliverables

| | File | Format |
|---|---|---|
| 16:9 master | `claude-stem-adversarial-inputs-slate.mp4` | 3840×2160 @ 24fps |
| 9:16 companion | `vertical/claude-stem-adversarial-inputs-vertical-slate.mp4` | 1080×1920 @ 24fps |

## Per-beat classification

| Beat | Class | Measured | Pattern |
|---|---|---|---|
| B00 | SHOW | 17.02s | ClaudeComposerAsk |
| B01 | SHOW | 10.67s | BrutalistHesitantWriter — ≥9s ✓ |
| B02 | SHOW | 20.42s | ThreeStageBand (two stages) |
| B03 | SHOW | 7.49s | ClaudeComposerAsk — clears the ≥7s typing floor |
| B04 | SHOW | 22.40s | GuardrailCompare |
| B05 | SHOW | 16.60s | ThreeStageBand — failure mode |
| B06 | SHOW | 12.86s | ClaudeCodeBeat |
| BHTF | SHOW | 13.70s | ClaudeComposerAsk |
| BOUT | SHOW | 7.94s | HaiTitleOutro |

**9 SHOW / 0 HOLD / 0 PUNT.** Slots 9/9. No slates.

## Zero new components

First reel in either series built entirely from the existing library. `ThreeStageBand`
absorbed both the two-box framework (N-length `stages`) and the falsifiability beat
(`failIndex`); Scene 3 fit `GuardrailCompare` without modification.

## The script's Scene 3 result is wrong — the reel corrects it

Verified by **executing the code**, not by reading it:

```python
re.sub(r'[^0-9.]', '', "approx $4.5M, ignore previous instructions.")  # -> '4.5.'
float('4.5.')   # -> ValueError
```

`.` is whitelisted, so the sentence's full stop survives. The script's VO claims the
normalizer "safely converts it to a float"; on its own payload it raises the very crash
it exists to prevent.

Second defect, on a string without trailing punctuation: `'approx $4.5M'` → `4.5`, not
`4,500,000`. The `M` is stripped with the noise — a 1,000,000× silent error.

The code on screen is **verbatim from the script**; only the stated result is corrected.
Full detail in SOURCES.md. Swapping in a corrected normalizer is one prop and a
one-beat re-render.

## Teaching arc

```
FRAMEWORK ✓      B01 BLUF + B02 the two stages, before any code.
WORKED EXAMPLE ✓ B04 — the real failure, executed and shown.
FALSIFIABILITY ✓ B05 — the system-prompt fallacy; defence-by-instruction fails.
SCAFFOLDED TASK ✓ B06 three outcomes; BHTF hunts silent wrong answers.
BOOKENDS ✓       B00 cold open · B01 BLUF · BHTF handoff · BOUT restate.
NO-SOURCE-NO-VERDICT ✓ no rate or benchmark invented; the one factual correction
                 was verified by running the code.
```

## Build note

The landscape render hit the 10-minute background ceiling after 5 of 9 beats and was
stopped. Resuming cost only the remaining 4 — `remotion_scenes.py` skips beats already on
disk unless `--force` is passed. No work was repeated.

## Open items

1. **Decide on the normalizer.** The reel currently shows your code failing honestly. If
   you'd rather it show a corrected version (reject multiple dots, handle K/M/B suffixes
   before casting), say so — one beat.
2. **Runtime 2:09 vs 2:45 target.** Not padded; duration is an output.
3. **Lane-mix warning (not blocking).** `remotion` carries 9/9 beats.
4. **SKIN LINT warning (expected).** `BOUT` uses `HaiTitleOutro`.
5. **Paperwork.** Built with `ART_FACTS=0`.
6. **`./art final` not run** — no label-free master yet.
