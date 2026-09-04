# Current render manifest — canonical 03:00 portrait cut

`src/CanAIDiscoverQuantumMaterials9x16.tsx` and this document describe what
actually renders in the 9:16 cut. The frame map is **identical** to the 16:9
master; only the layout inside each scene differs.

## Timeline

Frames are derived from the same measured Kokoro durations as the 16:9 cut
(`../Can-AI-discover-new-quantum-materials-16x9/mp3/timings.json`), rounded to
whole frames at 24 fps. Nothing is hand-tuned.

| Scene | Beats | Frames | Time | Portrait content |
|---|---|---:|---:|---|
| 01 | B00 | 0–301 | 00:00–00:12 | Executive summary · answer stated first · **vertical** Search→Rank→Synthesize→Measure→Confirm stack |
| 02 | B01, B02 | 301–850 | 00:12–00:35 | Tc definition · 860 px measured Tc chart · **CLAIM reveal as a 3+2 grid** |
| 03 | B03, B04 | 850–1448 | 00:35–01:00 | Citation → 2×2 stats → features → exclusions, all full-width stacked |
| 04 | B05, B06 | 1448–1823 | 01:00–01:15 | ±9.5 K at 200 px, three stacked supporting cards, interpolation reframe |
| 05 | B07, B08 | 1823–2279 | 01:15–01:34 | Screening funnel (label column + proportional block) · illustrative disclosure |
| 06 | B08b | 2279–2669 | 01:34–01:51 | Inside/outside distribution **stacked** · 1986 cuprates · 2008 pnictides |
| 07 | B09, B10 | 2669–3130 | 01:51–02:10 | **Vertical** five-link confirmation chain · human boundary |
| 08 | B11, B12 | 3130–3684 | 02:10–02:33 | **LK-99 stacked top/bottom** — claimed above, replication below, both held together |
| 09 | B12b | 3684–3992 | 02:33–02:46 | CLAIM rubric scored against LK-99 |
| 10 | B13 + hold | 3992–4320 | 02:46–03:00 | Viewer scaffold · decision rule · title close |

Total: **4320 frames = exactly 180.000 s.** The last 14 frames (0.58 s) are a
silent title hold.

## Audio

All sixteen beats play: B00, B01, B02, B03, B04, B05, B06, B07, B08, B08b,
B09, B10, B11, B12, B12b, B13. Every beat ID is unique.

The MP3s are **reused** from the 16:9 project, not copied into this folder.
`scripts/sync-to-remotion.ps1` reads them from
`../Can-AI-discover-new-quantum-materials-16x9/mp3/` and stages them into the
shared `public-quantum-materials` namespace.

## Rendering contract

- Composition ID: `CanAIDiscoverQuantumMaterials9x16`
- 4320 frames at 24 fps
- 2160 × 3840, 9:16 portrait, H.264, CRF 18
- Public dir: `public-quantum-materials` (shared with the 16:9 cut)
- No external image, stock footage, generated clip, or captured screenshot.

## The one chart

`TcChart` plots the same published, measured critical temperatures as the 16:9
cut, from the same `TC_DATA` table. Two portrait-specific changes:

1. **Height raised from 452 px to 860 px.** Portrait provides the vertical
   room, and a squashed chart would have compressed the 1986–1993 cluster
   further.
2. **The `YBCO 92K` label is left-anchored** rather than centred above its
   point. In portrait the plot is narrower, which pushed that centred label
   underneath the unlabelled BSCCO point. Caught in preflight and fixed before
   the master; see `FINAL-QA.md`.

High-pressure records (H₃S, LaH₁₀) remain accent-coloured points with their
pressures stated in a callout, never as point labels — the same decision, and
for the same reason, as the 16:9 cut.
