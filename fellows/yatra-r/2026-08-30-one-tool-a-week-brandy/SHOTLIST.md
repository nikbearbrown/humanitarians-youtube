# SHOTLIST — One Tool a Week. (Brandy)

Durations are MEASURED Kokoro lengths — audio is the master clock.

Total: **10 beats · 145.7s · 2:25.7**

| Beat | Dur | Frames | motion | Composition | Act |
|---|---|---|---|---|---|
| B00 | 12.50s | 375 | type-on | `ClaudeComposerAsk` | ASK |
| B01 | 15.72s | 472 | populate | `RcpWeeks` | THE SERIES (BLUF) |
| B02 | 15.49s | 465 | card | `RcpCard` | THE TOOL |
| B03 | 13.48s | 404 | stagger | `RcpStatus` | WHAT SHIPPED |
| B04 | 16.13s | 484 | card | `RcpCard` | ARTICLE ONE |
| B05 | 18.11s | 543 | ledger | `RcpSplit` | ARTICLE TWO |
| B06 | 16.41s | 492 | chips | `RcpTeam` | WHAT'S AHEAD |
| B07 | 17.13s | 514 | stagger | `ClaudeVerdictArtifact` | VERDICT |
| B08 | 16.21s | 486 | type-on | `ClaudeComposerAsk` | HANDOFF |
| B09 | 4.57s | 137 | fade | `ClaudeTitleOutro` | OUTRO |

## Human slots: NONE

Every beat is machine-renderable; no pantry request, no archive card.

## Composition sharing

`RcpCard` backs two beats (B02, B04). Its `durationInFrames` is set to the **shorter** of
the two, so the longer beat freeze-holds its completed frame rather than having its tail
trimmed — `remotion_scenes.py` extends losslessly, `compile.py` trims lossily.

## Formats

- **16:9** — 3840×2160, 2:25.8.
- **9:16** — 1080×1920, 2:30.2 including the silent endcard. Derived with
  `./art shorts --drop` (explicit empty drop plan) so no beats are cut. Under the 3:00 cap,
  so it posts natively on Instagram Reels and LinkedIn.

## Reused vs new scenes

| Composition | Source |
|---|---|
| `RcpCard` | NEW — `scenes/OneToolAWeek.tsx`. Renders `lines` verbatim; no summary field. |
| `RcpTeam` | NEW — same file. Requires a `status`, rendered in the accent. |
| `RcpWeeks` / `RcpStatus` | REUSED from `scenes/EveryToolEveryWeek.tsx` |
| `RcpSplit` | REUSED `JdgSplit` from `scenes/JudgmentIsTheJob.tsx` |
