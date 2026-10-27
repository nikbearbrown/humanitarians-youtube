# BUILD-LOG — hai-agents-on-their-own

## Toolkit

Built against **brutalist.art** at commit `4115560` (2026-10-14).
Engine `kokoro`, voice `am_onyx`, palette `claude`, ground `#FAF9F5`.

**Every beat renders from Remotion.** No Manim scenes and no `scenes.py` in this reel — the
`manim/` and `pantry/` directories are empty by design. 7 distinct Remotion patterns
carry 10 beats.

## Final build

| | |
|---|---|
| Status | `ready` |
| Beats filled | 10 of 10 |
| Slates remaining | none |
| Skin warnings | none |
| Narration total | 133.9s |
| Master duration | 134.04s |
| Master sha256 | `1560e91911cca03690e7b005f76af8bb…` |
| Built at | 2026-10-19T03:54:48.966889+00:00 |
| Vertical cut | yes — separate 2160x3840 build with its own gate run |

Audio is the master clock: each beat's final length is however long its own Kokoro mp3 runs,
so `estimated_duration_s` is a planning figure and `actual_duration_s` is the truth.

## Per-beat record

| Beat | Act | Remotion pattern | Estimated | Actual | Status |
|---|---|---|---:|---:|---|
| B00 | ASK | `ClaudeComposerAsk` | 20s | 13.99s | VIDEO |
| B01 | BLUF | `BrutalistHesitantWriter` | 18s | 13.65s | VIDEO |
| B02 | WHAT | `ClaudeTldrWhat` | 22s | 15.27s | VIDEO |
| B03 | TERMS | `ClaudeDefinitions` | 22s | 14.61s | VIDEO |
| B04 | EVIDENCE | `ClaudeCodeBeat` | 20s | 13.59s | VIDEO |
| B05 | GUARDRAIL | `ClaudeCodeBeat` | 22s | 15.49s | VIDEO |
| B06 | REFUSAL | `ClaudeCodeBeat` | 24s | 16.94s | VIDEO |
| B07 | JUDGE | `ClaudeTldrWhy` | 24s | 14.70s | VIDEO |
| B08 | YOUR-TURN | `ClaudeComposerAsk` | 20s | 12.22s | VIDEO |
| B09 | OUTRO | `ClaudeTitleOutro` | 8s | 3.41s | VIDEO |

## Honesty note

Narration is AI-generated (Kokoro `am_onyx`) and the reel discloses this on screen.
The configuration, the evidence and the work shown are the fellow's own.
