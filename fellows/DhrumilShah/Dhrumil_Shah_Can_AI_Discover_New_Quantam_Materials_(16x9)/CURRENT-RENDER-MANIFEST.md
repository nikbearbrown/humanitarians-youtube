# Current render manifest — canonical 03:00 cut

`src/CanAIDiscoverQuantumMaterials.tsx` and this document describe what
actually renders. `beat_sheet.json` is the authored source of truth for
narration and shot intent; the scene geometry lives in the composition.

## Timeline

Frames are derived from the **measured** Kokoro durations in
`mp3/timings.json`, rounded to whole frames at 24 fps. Nothing is hand-tuned.

| Scene | Beats | Frames | Time | Content |
|---|---|---:|---:|---|
| 01 | B00 | 0–301 | 00:00–00:12 | Executive summary · the answer stated first · Search→Rank→Synthesize→Measure→Confirm |
| 02 | B01, B02 | 301–850 | 00:12–00:35 | Tc definition · measured critical-temperature record · **CLAIM framework reveal** |
| 03 | B03, B04 | 850–1448 | 00:35–01:00 | The training table · 81 composition features · what is *not* in the table |
| 04 | B05, B06 | 1448–1823 | 01:00–01:15 | Reported ±9.5 K RMSE · the interpolation reframe |
| 05 | B07, B08 | 1823–2279 | 01:15–01:34 | The screening funnel · illustrative-schematic disclosure |
| 06 | B08b | 2279–2669 | 01:34–01:51 | Inside vs outside the distribution · 1986 cuprates · 2008 pnictides |
| 07 | B09, B10 | 2669–3130 | 01:51–02:10 | The five-stage confirmation chain · the human boundary |
| 08 | B11, B12 | 3130–3684 | 02:10–02:33 | **LK-99 side-by-side**: claimed vs what replication found |
| 09 | B12b | 3684–3992 | 02:33–02:46 | LK-99 scored on the CLAIM rubric |
| 10 | B13 + hold | 3992–4320 | 02:46–03:00 | Reusable viewer scaffold · decision rule · title close |

Total: **4320 frames = exactly 180.000 s.** The last 14 frames (0.58 s) are a
silent title hold.

## Audio

All sixteen beats play: B00, B01, B02, B03, B04, B05, B06, B07, B08, B08b,
B09, B10, B11, B12, B12b, B13. Every beat ID is unique — there is no duplicate
identifier anywhere in the sheet, the timings file, or the composition.

Voice: Kokoro `am_onyx`, generated locally by
`runtime/scripts/generate_audio_kokoro.py`. No account, no API, no cost.

## Rendering contract

- Composition ID: `CanAIDiscoverQuantumMaterials`
- 4320 frames at 24 fps
- 3840 × 2160, 16:9, H.264, CRF 18
- Public dir: `public-quantum-materials`
- No external image, stock footage, gen-AI clip, or captured screenshot is
  used. Every frame is drawn from typeset text, layout primitives, and one
  data-driven SVG chart.

## The one chart

`TcChart` plots published, measured critical temperatures against year. It is
computed in-component from the values in `TC_DATA`, each of which is cited in
`SOURCES.md`. High-pressure records are drawn in accent and their pressures are
stated in a dedicated callout — never implied to be ambient.

The callout exists because the first render placed the LaH₁₀ and H₃S point
labels on top of the 293 K room-temperature line and on top of each other. That
was a legibility defect, and it was fixed before the master render rather than
shipped. See `FINAL-QA.md`.
