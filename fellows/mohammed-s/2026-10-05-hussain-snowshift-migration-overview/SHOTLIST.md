# SHOTLIST — Compiling Is Not Migrating.

Reel: `hussain-snowshift-migration-overview` · 13 beats · 3:20 measured audio
Presenter: Mohammed Hussain (narrating as himself — no channel persona)
Masters: 3840×2160 (16:9) + 2160×3840 (9:16), both native.

| Beat | Act | Composition | 9:16 twin | Seconds | What the viewer watches |
|---|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | 13.29 | "Salaam, Hussain"; the migration ask types; three result lines land. |
| B01 | BLUF | `BrutalistHesitantWriter` | `BrutalistHesitantWriter916` | 10.46 | Overview typed and corrected: `translation` → `proof`, `done` → `starting`. |
| B02 | PROBLEM | `SnowMonolith` | `SnowMonolith916` | 17.30 | Main.sql counter to 1,244; drift tag; 8 stage folders fill with file counts; "32 of 32" verdict. |
| B03 | LINT | `SnowLintCatch` | `SnowLintCatch916` | 17.47 | "27" rules; four T-SQL habits struck beside their fixes; the real TOP 10 catch. |
| B04 | ASK | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | 8.45 | "The ask," — the deploy prompt types. Receipt is B05. |
| B05 | RESULT | `SnowDeployRail` | `SnowDeployRail916` | 17.58 | Six stages tick in order; optional stages dashed; replay: FAIL, then skipped; the rule. |
| B06 | PARITY | `SnowParity` | `SnowParity916` | 17.92 | Aggregates side by side, ticked; the FLOAT drift row diverges; two lenses. |
| B07 | GAP | `SnowConstraintGap` | `SnowConstraintGap916` | 16.26 | Real UNIQUE constraint types; run 2 rejected vs stored; budget 1× → 2×. |
| B08 | FIX | `SnowSmokeProof` | `SnowSmokeProof916` | 18.52 | Four checks tick; three smoke runs land; "budget unchanged". |
| B09 | TEARDOWN | `CortexWhereItBites` | `CortexWhereItBites916` | 15.98 | Three cards: not run live · concurrent imports · placeholders. |
| B10 | VERDICT | `ClaudeVerdictArtifact` | `ClaudeVerdictArtifact916` | 17.18 | One-page verdict, four lines. |
| B11 | HANDOFF | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | 20.44 | "Your turn." The prompt types, is read aloud, then discussed. |
| B12 | OUTRO | `CortexTitleOutro` | `CortexTitleOutro916` | 4.25 | Title restate, terracotta period, "Mohammed Hussain". |

## Lane histogram

13 remotion · 0 manim · 0 vox · 0 slate. Nothing is punted; no pantry media is requested.

## ILLUSTRATE LAW audit

Claude UI appears only at B00 (cold open), B04 (ask micro-beat), B10 (verdict),
B11 (handoff). B02, B03, B05–B09 illustrate their own concepts; no two
consecutive body beats share a visual scheme.

## Terracotta ledger (one moment per beat)

B02 the verdict rule · B03 the TOP 10 strike · B05 the rule dash · B06 the ≠ drift ·
B07 the 2× total · B08 "budget unchanged" · B09 the house card accents.

## Dual-aspect note

Every pattern resolves to a registered `916` composition, so `./art vertical`
rewires rather than blocks; nothing is centre-cut. The six `Snow*` components
live in `runtime/remotion/src/scenes/SnowshiftIllus.tsx` and branch on
`height > width`.
