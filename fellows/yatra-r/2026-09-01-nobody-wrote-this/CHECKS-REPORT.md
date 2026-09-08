# CHECKS-REPORT — `yatra-nobody-wrote-this`

Written BEFORE the first slate compiled, per the PROOF GATE in
`skills/make/ai-explainer/SKILL.md`.

```
14 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification (nopunt § SHOW / HOLD / CARD)

| Beat | Class | Scene | Why it is SHOW |
|---|---|---|---|
| B00 | SHOW | `ClaudeComposerAsk` | the composer is the subject; the ask lands answered with three result lines |
| B01 | SHOW | `LnkBluf` | the reframe is performed — the wrong description is struck through and replaced on the spoken beat, not narrated over a static card |
| B02 | SHOW | `LnkFrame` | three bins draw on cue; the framework is a drawn artifact, not a claim |
| B03 | SHOW | `LnkStat` | the figure with its citation held on screen |
| B04 | SHOW | `ClaudeComposerAsk` | ask micro-beat of the reel's one ask→result pair |
| B05 | SHOW | `LnkLadder` | five bars stagger in; the dashed cross-platform reference drops on the spoken comparison |
| B06 | SHOW | `LnkDisproportion` | two tracks plus the dashed proportional reference — the overshoot is visible, not asserted |
| B07 | SHOW | `LnkAllOrNothing` | B02's bins fill; the 4.3% sliver is legible as almost-nothing |
| B08 | SHOW | `LnkContradiction` | two drives grow toward each other and stall |
| B09 | SHOW | `LnkFalsify` | three stress-tests stagger in with their reasons |
| B10 | SHOW | `LnkPressure` | two tagged blocks over a date axis; the marker lands on the spoken date |
| B11 | SHOW | `ClaudeVerdictArtifact` | the artifact page; four lines land per spoken clause |
| B12 | SHOW | `ClaudeComposerAsk` | the handoff prompt types itself as it is read aloud |
| B13 | SHOW | `ClaudeTitleOutro` | title restate |

No beat is a bare CARD, and no beat is a PUNT. Every beat that names a visual in
its narration renders that visual.

## Teaching-arc checklist (nopunt § Whole-sheet)

- **FRAMEWORK beat — ✓ B02.** The three-bin classification is presented before
  any figure appears, and the bins are deliberately EMPTY so the framework is not
  smuggled in alongside its first result.
- **WORKED EXAMPLE — ✓ B05.** All five platforms run through the framework while
  it is on screen, with the cross-platform rate drawn as a reference line. B07 is
  a second pass: the same framework, the same platform, now filled.
- **FALSIFIABILITY — ✓ B09.** A full beat, not a caveat in passing: detection is
  probabilistic, the same scan produced a low floor elsewhere, and the beat names
  what a rescan would have to show to overturn the read.
- **SCAFFOLDED TASK — ✓ B12.** A real prompt plus a three-item rubric
  ("does it point at facts only you have?" / "does it cut the lines any model
  could write?" / "is the rewrite shorter AND more specific?").
- **FOUR BOOKENDS — ✓.** Cold open B00 · verdict B11 · your turn B12 · title
  restate B13.
- **NO SOURCE, NO VERDICT — ✓.** Every beat making a factual claim carries its
  citation in frame: B02, B03, B05, B06, B07, B08 and B11 render `Source:` lines;
  B10 carries a per-block citation and explicitly tags its non-sourced half
  `INTERPRETATION`. B09's closer is a judgment about the sourced figures already
  shown. B01, B12 and B13 are exempt (BLUF and handoff recapitulate; the outro
  asserts nothing).

## Legibility contract

- Every SHOW beat names its artifact in `shot.show`.
- Negative space held in the ~15–35% band by design; verified at frame level in
  `_qc/REPORT.md` after the render (GATE V fails any beat under 55% ink coverage
  of SAFE).
- No un-highlighted element drops below ~40% opacity: the dimmest resting state
  in these scenes is `0.35 + 0.65 * g` on ladder labels and `opacity: 0.3` on the
  brand bug, which is chrome and not content.
- The comparisons that matter (B05 five platforms, B06 two tracks, B07 three
  bins, B08 two policies, B10 two pressures) are all side-by-side and all hold
  well past 2s at their measured beat lengths.

## Notes for the reviewer

- **Duration is 2:48 (168.4s), an output not a target.** It lands inside the
  1–3 minute brief without padding or compression, and leaves headroom under the
  hard 3:00 Shorts cap so the vertical is the complete video rather than an
  auto-shortened cut.
- **Manim is not installed in this environment** (`./art doctor` reports it
  blocked; Kokoro, Remotion, Pillow and the caption pipeline are all ready). No
  beat in this reel needs it — every beat is Remotion — so `run.sh` skips the
  Manim stage cleanly. This is recorded so the skip is not mistaken for a
  silently dropped beat.
