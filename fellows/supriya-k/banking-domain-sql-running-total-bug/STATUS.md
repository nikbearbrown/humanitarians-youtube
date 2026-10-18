# STATUS — banking-sql-running-total-bug

12/12 beats filled and compiled. Derived from `beat_sheet.json` — edit the sheet, not this file.

| beat | status | fill method | who | slot |
|---|---|---|---|---|
| B00 | filled | Remotion `ClaudeComposerAsk` | machine | `media/B00.mp4` |
| B01 | filled | Manim `B01_RunningBalanceStakes` | machine | `manim/B01.mp4` |
| B02 | filled | Manim `B02_FilterOrderSplit` | machine | `manim/B02.mp4` |
| B03 | filled | Remotion `ClaudeComposerAsk` | machine | `media/B03.mp4` |
| B04 | filled | Remotion `ClaudeCodeBeat` | machine | `media/B04.mp4` |
| B05 | filled | Manim `B05_TruncatedBalance` | machine | `manim/B05.mp4` |
| B06 | filled | Remotion `ClaudeComposerAsk` | machine | `media/B06.mp4` |
| B07 | filled | Remotion `ClaudeCodeBeat` | machine | `media/B07.mp4` |
| B08 | filled | Manim `B08_CorrectedBalance` | machine | `manim/B08.mp4` |
| B09 | filled | Manim `B09_TheLesson` | machine | `manim/B09.mp4` |
| B10 | filled | Remotion `ClaudeComposerAsk` | machine | `media/B10.mp4` |
| B11 | filled | Remotion `ClaudeTitleOutro` | machine | `media/B11.mp4` |

**Outputs:** `banking-sql-running-total-bug-slate.mp4` (review cut, 167.74s) and
`banking-sql-running-total-bug.mp4` (clean master, 167.74s), both 3840×2160.

## Render-gate fixes applied (all human-reviewed, logged here for the trail)

- **B06** had an empty composer "spark line" (a real SPARK-LINE LAW violation per
  `cli-explainer/SKILL.md`) — fixed to `"The revision,"`.
- **B00/B03/B06/B10** were rendering the shared `ClaudeComposerAsk` component's hardcoded default
  `folderLabel: "@NikBearBrown"` and `modelLabel: "Fable 5"` — neither was ever set explicitly in
  this reel's props, so the compliance-required "no channel branding" decision was silently
  violated by the component's own defaults. Fixed by setting `folderLabel: "Banking Domain Data
  Analyst Interview Prep"` and `modelLabel: "Claude"` explicitly on all four composer beats.
- **B00** had a genuine `edge-bleed` BLOCKER from Gate V: `compile.py`'s `metadata.channel_title`
  feature overlays that text at a fixed 40px from the frame's bottom edge, which clears the hard
  frame but violates Gate V's title-safe margin for a string this long at 4K. Since the same
  attribution is already carried by both the spoken narration ("in for Supriya") and the composer's
  `folderLabel` chip (both unflagged), `channel_title` was cleared rather than patching the shared
  compile script.
- **B09** had a `underfill` MAJOR (53% vs. min 55%) — increased checklist/note font sizes and
  spacing (verified geometrically before re-rendering) to raise content density.
- **B08** had 6 `label on a curve/line` errors from Gate B — these were the *deliberate*
  strike-through lines over the superseded wrong balances; marked
  `strikes._qc_intentional = True` per the documented convention rather than removing the effect.

## Accepted, not fixed (human sign-off — 2026-08-10)

- **B11** (`ClaudeTitleOutro`) fills only 19% of the safe area per Gate V — this is a fixed-pixel
  property of the shared Remotion component itself (72px/38px/22px text, centered, on a 4K canvas;
  confirmed by reading `ClaudeTitleOutro.tsx` directly — no prop controls density). Fixing it would
  mean editing shared infrastructure other reels also use. The human reviewed the actual card and
  accepted it as-is rather than have that edit made. Final compile therefore did not re-run Gate V
  in strict mode after this decision — the two MAJOR findings in `_qc/REPORT.md` are this known,
  accepted exception, not an unreviewed defect.
