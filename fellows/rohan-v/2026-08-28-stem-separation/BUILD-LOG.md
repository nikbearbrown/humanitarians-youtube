# BUILD-LOG — "Stem Separation: Estimation, Not Extraction"

Session date: 2026-08-28 · Toolkit: `brutalist.art` · Cost: $0.00

---

## v1 build (original — superseded)

7 beats, all existing library components (`ClaudeComposerAsk`, `ClaudeWindow` ×3,
`ClaudeVerdictArtifact` ×2, `OutroCTA`). No waveform motion graphics.
Delivered at 2:21. **Superseded by v2.**

---

## v2 build (current)

### Changes from v1

| What changed | Why |
|---|---|
| B01: `ClaudeWindow` → `StemSepMixCollapse` | New purpose-built scene: 4 colored waveform tracks collapsing into one mixed signal |
| B02: `ClaudeVerdictArtifact` → `StemSepStemOutput` | New purpose-built scene: mixed waveform splitting into 3 estimated stem waveforms with dashed "PROBABILITY" borders |
| B04: `ClaudeVerdictArtifact` → `StemSepBleedViz` | New purpose-built scene: vocal stem with ghost drum bleed + clean-vs-bleed comparison strip |
| B06: `OutroCTA` → `ClaudeTitleOutro` | Matches first video's outro style (title · handle · presenter subline on cream ground) |
| B00 narration: added "for Humanitarians AI" | Matches first video's intro convention |
| B06 narration: "I'm Rohan V., for Humanitarians AI" | Matches first video's outro narration |
| B01/B02/B04 narration: references the visual directly | New narration written to match what's on screen |

### New components built

Three new TSX files in `runtime/remotion/src/scenes/`:
- `StemSepMixCollapse.tsx` — spring stagger-in for 4 tracks, `interpolate` collapse
- `StemSepStemOutput.tsx` — split-arrow fan, dashed-border stem boxes
- `StemSepBleedViz.tsx` — pulsing bleed ghost, annotation arrow, comparison strip

All three registered in `Root.tsx` under the `stem-separation-explainer` folder.
Waveform rendering uses a deterministic 4-harmonic sine path generator (seed-based,
reproducible across renders).

### Phase 1 — audio

`generate_audio_kokoro.py`, voice `af_bella`, 7 beats regenerated from
updated narration.

### Phase 2 — render

`remotion_scenes.py --force` — all 7 beats rendered with new scene assignments.
Post-render mux: narration audio merged into each `media/B*.mp4`.

### Phase 3 — compile 16:9

`compile.py --height 2160`: 7/7 slots filled, all VIDEO, zero slates.

### Phase 4 — build 9:16

FFmpeg letterbox pass (all 7 beats, 2160×3840 4K, cream letterbox bars).

### Status

Built · compiled · QC'd · **not published**.
