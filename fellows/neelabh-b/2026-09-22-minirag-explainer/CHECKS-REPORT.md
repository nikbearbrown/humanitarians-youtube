# CHECKS-REPORT — claude-liam-minirag

Written before the first compile, per `ai-explainer` § PROOF GATE.

```
16 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

Every beat names a real renderable component in `shot.remotion.pattern`, so all
16 classify **SHOW**. No beat is a bare CARD whose narration names a visual it
cannot show; no beat is left unfilled.

| Beat | Class | Component | Why it is SHOW, not CARD |
|---|---|---|---|
| B00 | SHOW | `ClaudeComposerAsk` | The composer types the ask and answers it on screen |
| B01 | SHOW | `BrutalistHesitantWriter` | The misconception is written, then visibly corrected |
| B02 | SHOW | `MiniRagStackToday` | Three stages draw; the dependency band lights them |
| B03 | SHOW | `ReqBars` | Five bars carry the numbers the voice speaks |
| B04 | SHOW | `FormACard` | The paper's three RQs are the legible artifact |
| B05 | SHOW | `ClaudeComposerAsk` | The actual generation prompt, typed |
| B06 | SHOW | `MiniRagPipeline` | Figure 1 rebuilt; a pulse walks the path |
| B07 | SHOW | `MiniRagHeteroGraph` | Nodes and both edge families build on cue |
| B08 | SHOW | `MiniRagWorkedQuery` | Two systems side by side, answers resolving |
| B09 | SHOW | `ReqBars` | Paired bars, MiniRAG over LightRAG |
| B10 | SHOW | `MiniRagAblationDrop` | Structure strips away as the counter falls |
| B11 | SHOW | `ReqBars` | The reversal between accuracy and error is visible |
| B12 | SHOW | `FormACard` | Three consequences with the storage figure on screen |
| B13 | SHOW | `ClaudeVerdictArtifact` | The one-page recap artifact |
| B14 | SHOW | `ClaudeComposerAsk` | The viewer's prompt, typed and read |
| B15 | SHOW | `ClaudeTitleOutro` | Title restate |

## Teaching-arc checklist (`nopunt` § whole-sheet)

- [x] **FRAMEWORK before the first example** — B02 presents RAG's three stages
      and the hidden LLM dependency. It precedes every result beat.
- [x] **WORKED EXAMPLE through the framework** — B08 runs one real query from
      Table 3 through both systems while the mechanism is on screen.
- [x] **FALSIFIABILITY / edge case** — B11 is a full beat, not a caveat: on
      MultiHop-RAG, MiniRAG's error rate (28.44%) is more than double
      LightRAG's (11.78%). This is the paper's own data, and the paper does not
      discuss it.
- [x] **SCAFFOLDED viewer task** — B14 gives a three-part experiment prompt
      *and* a three-part rubric for judging the answer ("does it separate
      accuracy from error rate; does it name a baseline; does it say what would
      prove the claim wrong").
- [x] **Four bookends** — B00 cold open · B13 verdict · B14 your turn ·
      B15 title-restate outro.
- [x] **No source, no verdict** — every claim beat carries its evidence on
      screen. B03/B09/B11 show the figures as bars with a source colophon;
      B10 shows the ablation ladder; B08 quotes Table 3 verbatim; B04 and B12
      carry `meta` colophons. B13 and B14 recapitulate rather than assert and
      are exempt.

## Legibility contract

- Every SHOW beat names its artifact in `shot.show`.
- Comparisons (B08, B09, B11) are side-by-side and hold well past 2s — the
  shortest of the three is B09 at 20.97s.
- Nothing is faded below ~40% opacity except deliberately-retired ablation
  layers in B10, where disappearance *is* the content.
- All components position from the 5% title-safe inset (`SX=96`, `SY=54`).

## Audio lock — the master clock

16 beats, **277.25s (4:37)**. Kokoro `am_onyx`, local, **$0.00**.

B01 measured **12.84s**, clearing the ≥9s floor the hesitant-writer beat needs
for its correction to land before the cut.

## ILLUSTRATE LAW audit

Claude UI appears in 5 of 16 beats, all sanctioned: B00 cold open, B05 the ask
of the single ask→result pair, B13 verdict, B14 handoff, B15 outro. The eleven
inner beats each illustrate their own concept. No two consecutive beats share a
visual scheme — B06/B07/B08 are all reel-local components but structurally
unalike (three-panel pipeline / node-edge graph / two-column comparison), and
are flagged for specific attention in visual QC.

## Open item carried into QC

`SCENE-DOC-TODO.md` reports 118 scenes running on derived search text. The five
new `MiniRag*` components ship with header docblocks, so they are not among
them; no action for this reel.
