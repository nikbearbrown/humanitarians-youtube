# SHOTLIST — Cortex, In The Warehouse.

Reel: `hussain-snowflake-cortex-triage` · 11 beats · 1m59s measured audio (tightened cut)
Presenter: Mohammed Hussain (narrating as himself — no channel persona)
Masters: 3840x2160 (16:9) + 2160x3840 (9:16), both native.

| Beat | Act | Lane | Composition | 9:16 twin | Seconds | What the viewer watches |
|---|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | 13.23 | Composer types the ask; send arms; three output lines land. Cold open, the ask answered. |
| B01 | BLUF | remotion | `BrutalistHesitantWriter` | `BrutalistHesitantWriter916` | 11.13 | Overview typed and corrected live: `platform` → `SQL function`, `travels` → `stays put`. |
| B02 | PROBLEM | remotion | `CortexTicketPile` | `CortexTicketPile916` | 11.65 | Structured columns tick; `body` fills with grey free text and never ticks; COUNT(*) lands; the unanswerable question holds. |
| B03 | MECHANISM | remotion | `CortexInWarehouse` | `CortexInWarehouse916` | 13.38 | Pipeline lane draws and detaches a data copy (warn); lane dims; boundary box draws; model slides inside. |
| B04 | ASK | remotion | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | 6.21 | Micro-beat, spark only (no greeting). The triage ask types. Receipt is B05. |
| B05 | RESULT | remotion | `ClaudeCodeBeat` | `ClaudeCodeBeat916` | 12.48 | `triage.sql` reveals block by block; the WHERE clause lands last and holds. |
| B06 | OUTPUT | remotion | `CortexTriageTable` | `CortexTriageTable916` | 10.15 | Result grid fills; billing chips terracotta; sentiment bars grow; grid re-sorts angriest-first. |
| B07 | JUDGMENT | remotion | `CortexWhereItBites` | `CortexWhereItBites916` | 12.25 | Three cost cards fill in narration order; all three hold. |
| B08 | VERDICT | remotion | `ClaudeVerdictArtifact` | `ClaudeVerdictArtifact916` | 8.11 | Artifact page; four verdict lines stagger in. |
| B09 | HANDOFF | remotion | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | 17.51 | "Your turn." The prompt types, is read aloud verbatim, then discussed. |
| B10 | OUTRO | remotion | `CortexTitleOutro` | `CortexTitleOutro916` | 3.88 | Title restate, terracotta period, "Mohammed Hussain" beneath. |

## Lane histogram

11 remotion · 0 manim · 0 vox · 0 slate. No beat is unfilled; nothing is punted.

## ILLUSTRATE LAW audit

Claude UI appears at B00 (cold open), B04 (ask micro-beat), B08 (verdict
artifact), B09 (handoff) — the four sanctioned slots — plus B05, which is a code
card, not app chrome. B02, B03, B06, B07 illustrate their own concepts. No two
consecutive body beats share a visual scheme.

## Typing audit (HANDOFF LAW)

Typing appears in exactly three beats and for three different reasons:
B00 the ask · B01 the overview being thought through · B09 the viewer's prompt.
B04's composer shows a short ask as a micro-beat receipt-opener, not a fourth
typing set piece.

## Dual-aspect note

Every pattern above resolves to a `916` composition, so `./art vertical` rewires
rather than blocks, and nothing is centre-cut. The five `Cortex*` components are
single files that branch on `height > width` and reflow: columns become stacked
cards, node chains rotate from row to column, and type scales UP in portrait
(`tu = u * 1.62` in `cortexKit.tsx`).

## As-built note

Both masters were compiled and frame-verified directly rather than promoted via
`./art final`, which refuses on GATE V `underfill`. Zero BLOCKER defects remain in
either aspect. Full accounting: `QC-STATUS.md`.
