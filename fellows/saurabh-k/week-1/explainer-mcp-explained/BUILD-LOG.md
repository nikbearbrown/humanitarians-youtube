# BUILD-LOG — hai-mcp-explained

## Toolkit

Built against **brutalist.art** at commit `4115560` (2026-10-14).
Engine `kokoro`, voice `am_onyx`, palette `claude`, ground `#FAF9F5`.

**Every beat renders from Remotion.** No Manim scenes and no `scenes.py` in this reel — the
`manim/` and `pantry/` directories are empty by design. 7 distinct Remotion patterns
carry 11 beats.

## Final build

| | |
|---|---|
| Status | `ready` |
| Beats filled | 11 of 11 |
| Slates remaining | none |
| Skin warnings | none |
| Narration total | 160.6s |
| Master duration | 160.79s |
| Master sha256 | `5d803dc2120f86fc3ba1fac36aa12991…` |
| Built at | 2026-10-19T03:52:09.098664+00:00 |
| Vertical cut | yes — separate 2160x3840 build with its own gate run |

Audio is the master clock: each beat's final length is however long its own Kokoro mp3 runs,
so `estimated_duration_s` is a planning figure and `actual_duration_s` is the truth.

## Per-beat record

| Beat | Act | Remotion pattern | Estimated | Actual | Status |
|---|---|---|---:|---:|---|
| B00 | ASK | `ClaudeComposerAsk` | 20s | 16.43s | VIDEO |
| B01 | BLUF | `BrutalistHesitantWriter` | 20s | 14.40s | VIDEO |
| B02 | WHAT | `ClaudeTldrWhat` | 22s | 14.98s | VIDEO |
| B03 | WHY | `ClaudeTldrWhy` | 24s | 18.26s | VIDEO |
| B04 | TERMS | `ClaudeDefinitions` | 22s | 15.00s | VIDEO |
| B05 | EVIDENCE | `ClaudeCodeBeat` | 22s | 16.49s | VIDEO |
| B06 | ANATOMY | `ClaudeCodeBeat` | 22s | 13.87s | VIDEO |
| B07 | RESULT | `ClaudeCodeBeat` | 22s | 15.77s | VIDEO |
| B08 | JUDGE | `ClaudeTldrWhy` | 24s | 16.55s | VIDEO |
| B09 | YOUR-TURN | `ClaudeComposerAsk` | 22s | 15.19s | VIDEO |
| B10 | OUTRO | `ClaudeTitleOutro` | 8s | 3.65s | VIDEO |

## Honesty note

Narration is AI-generated (Kokoro `am_onyx`) and the reel discloses this on screen.
The configuration, the evidence and the work shown are the fellow's own.
