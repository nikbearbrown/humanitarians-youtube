# SHOTLIST — claude-liam-minirag

16 beats. **Zero human media slots** — every beat renders from a registered
Remotion composition, so the first compile is the finished cut, not a previz
awaiting plates.

**VOX LAW applies and resolves to zero.** The evidence in this reel is tables,
a graph structure, and quoted model output. There is no artifact whose
photograph *is* the claim, so there are no STILL slots and no `pantry/`
shopping list. Per the law, that is the correct outcome, not a gap.

## Slot table

| Beat | Act | Component | Registered? | Source of content |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | ✅ existing | — |
| B01 | BLUF | `BrutalistHesitantWriter` | ✅ existing | — |
| B02 | FRAMEWORK | `MiniRagStackToday` | 🔨 new, this reel | §1, §4 |
| B03 | THE-BREAK | `ReqBars` | ✅ existing | Table 1 |
| B04 | QUESTION | `FormACard` | ✅ existing | §3 |
| B05 | ASK-FIGURE | `ClaudeComposerAsk` | ✅ existing | — |
| B06 | ARCHITECTURE | `MiniRagPipeline` | 🔨 new, this reel | Figure 1 |
| B07 | METHOD | `MiniRagHeteroGraph` | 🔨 new, this reel | §2.1 |
| B08 | WORKED-EXAMPLE | `MiniRagWorkedQuery` | 🔨 new, this reel | Table 3 |
| B09 | RESULTS | `ReqBars` | ✅ existing | Table 1 |
| B10 | ABLATION | `MiniRagAblationDrop` | 🔨 new, this reel | Table 2 |
| B11 | FALSIFY | `ReqBars` | ✅ existing | Table 1 |
| B12 | STAKES | `FormACard` | ✅ existing | §3.2, Figure 3 |
| B13 | VERDICT | `ClaudeVerdictArtifact` | ✅ existing | — |
| B14 | HANDOFF | `ClaudeComposerAsk` | ✅ existing | — |
| B15 | OUTRO | `ClaudeTitleOutro` | ✅ existing | — |

## GATE L — library-first, what the search actually returned

Run before authoring, per `ai-explainer` §GATE L.

| Searched for | Result | Decision |
|---|---|---|
| The four bookends | `ClaudeComposerAsk`, `BrutalistHesitantWriter`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro` all RENDERABLE | **Reuse** |
| "bar chart comparing accuracy across models" | `BarChart` RENDERABLE — but Vox palette (`VOX.TEAL` / `VOX.SLATE`) | **Rejected.** Teal accent violates the Claude fidelity brand law (terracotta is the ONE accent) and the brand may not be retinted |
| "claude palette bars comparing two systems…" | `ReqBars` RENDERABLE — cream/ink/terracotta, `{label, value, compare?}`, `seriesA`/`seriesB` | **Reuse ×3** (B03, B09, B11) — the two-series shape is exactly MiniRAG-vs-LightRAG |
| "a pipeline of stages with data flowing through nodes" | `CanvasDesignPipeline`, `BrandGuidelinesPipeline`, `HaiExplainerFig1Pipeline` — all RENDERABLE but reel-local, content hardcoded, `props: sparkLine` only | **Miss.** Not parameterisable |
| `FlowDiagram`, `LayerStack`, `SourceFlow`, `ChipGrid`, `PredictCard` | **NOT RENDERABLE** — present in `src/illustrations/structural.tsx` as starter templates, no `<Composition>` in Root.tsx | **PUNT → design cards.** Authored as reel-local components adapting those templates, then registered — the documented pattern (610 compositions are registered this way) |

## The five new components — `MiniRag.tsx`

Reel-local, registered in `Root.tsx` under folder `MiniRag`, indexed with
`./art scene-index`. Palette fixed at cream `#F2F0E9`, ink `#3D3929`, terracotta
`#D97757`, EB Garamond. **No component hardcodes a statistic** — every number
arrives as a prop from `beat_sheet.json`, so a wrong figure is a beat-sheet fix,
never a component fix.

1. **`MiniRagStackToday`** — three stages left-to-right; a terracotta band sweeps
   beneath and lights all three at once. The band is the beat's whole argument.
2. **`MiniRagPipeline`** — Figure 1 rebuilt. Three panels; a pulse travels the
   discovered path in panel two. Carries the "Redrawn (simplified) from…" credit
   required by REBUILD LAW.
3. **`MiniRagHeteroGraph`** — chunk rectangles, entity circles, then the two edge
   families draw in sequence; one edge expands to show its description.
4. **`MiniRagWorkedQuery`** — query full-width on top, two systems side by side
   below, ground truth revealed last. Held ≥2s per the legibility contract.
5. **`MiniRagAblationDrop`** — the graph loses a structural layer per step while
   a counter ticks down; the 53.29→26.02 gap is bracketed at the end.

## Rhythm check — no two consecutive beats share a visual scheme

```
B00 UI · B01 writer · B02 custom · B03 bars · B04 card · B05 UI
B06 custom · B07 custom* · B08 custom* · B09 bars · B10 custom
B11 bars · B12 card · B13 UI · B14 UI · B15 UI
```

\* B06/B07/B08 are all custom but structurally unalike — a three-panel pipeline,
a node-edge graph build, and a two-column comparison. Flagged here so visual QC
checks them specifically. B13→B14→B15 are the three mandatory closing bookends
and are exempt.
