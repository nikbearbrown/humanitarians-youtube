# SHOTLIST — The Judgment Is the Job.

Typed work order. `shot.type` is locked; `shot.source` is late-bound. Durations are
MEASURED Kokoro lengths — audio is the master clock.

Total: **10 beats · 149.4s · 2:29**

| Beat | Dur | Frames | type | source | motion | Composition | Fills from | Status |
|---|---|---|---|---|---|---|---|---|
| B00 | 12.10s | 363 | GRAPHIC | remotion | type-on | `ClaudeComposerAsk` | pipeline | machine |
| B01 | 16.73s | 502 | GRAPHIC | remotion | diverge | `JdgDiverge` | pipeline | machine |
| B02 | 17.66s | 530 | GRAPHIC | remotion | ledger | `JdgSplit` | pipeline | machine |
| B03 | 6.44s | 193 | GRAPHIC | remotion | type-on | `ClaudeComposerAsk` | pipeline | machine |
| B04 | 15.77s | 473 | GRAPHIC | remotion | populate | `JdgOptions` | pipeline | machine |
| B05 | 18.09s | 543 | GRAPHIC | remotion | branch | `JdgBranch` | pipeline | machine |
| B06 | 15.30s | 459 | GRAPHIC | remotion | reveal | `JdgStakes` | pipeline | machine |
| B07 | 19.03s | 571 | GRAPHIC | remotion | stagger | `ClaudeVerdictArtifact` | pipeline | machine |
| B08 | 21.46s | 644 | GRAPHIC | remotion | type-on | `ClaudeComposerAsk` | pipeline | machine |
| B09 | 6.83s | 205 | GRAPHIC | remotion | fade | `ClaudeTitleOutro` | pipeline | machine |

## Human slots: NONE

No `pantry/` shopping list, no archive request card. Every beat is machine-renderable.
Correct under `nopunt`'s one rule: a HOLD is legitimate only for a genuine archival
PHOTOGRAPH of a real person, place, document or event. This reel argues from a model and
has no such beat, so a stock image anywhere here would be a PUNT, not a HOLD.

Specifically **not** requested: generated ad imagery for B04. See FACTCHECK.md § REBUILD
LAW note — the wall is native concept cards carrying angle labels, which keeps the beat
free-path and stops anything on screen from posing as a real generated ad.

## Provenance

No sidecars required — no `archive` or `ai` sourced media. Every frame is a deterministic
render of committed scene source, so the reel rebuilds identically from the repo alone.

## Lane histogram

```
remotion (claude UI, bookends)   5 beats  B00 B03 B07 B08 B09   65.86s  44%
remotion (illustration, C2/new)  5 beats  B01 B02 B04 B05 B06   83.55s  56%
manim                            0 beats
vox / pantry stills              0 beats
```

Motion languages: type-on 3 · diverge 1 · ledger 1 · populate 1 · branch 1 · reveal 1 ·
stagger 1 · fade 1 — no language exceeds MOTION.md's ~40% cap. (The previous reel tripped
that cap by labelling five distinct motions "illustrate"; the labels here describe what
each beat actually does.)

## Scene provenance

| Composition | Source | Note |
|---|---|---|
| `JdgDiverge` | REUSED `deckPatterns.DivergentFates` | Qualitative, verified working on the previous reel. Wrapped in `SafeStage`. |
| `JdgBranch` | REUSED `deckPatterns.BinaryBranch` | Same. Long strings kept short — the previous reel's QC found this component overflows fixed-width boxes. |
| `JdgSplit` | NEW — `scenes/JudgmentIsTheJob.tsx` | Two-column ledger. |
| `JdgOptions` | NEW — same file | The wall + one terracotta ring. Carries the thesis. |
| `JdgStakes` | NEW — same file | N named items with a one-line why each. |

The three quantitative deckPatterns scenes (`ScaleComparison`, `AttritionChain`,
`Threshold`) are deliberately **not used** — the previous reel's QC established that they
crash or print measured-looking figures, both fatal under this reel's no-numbers rule.
