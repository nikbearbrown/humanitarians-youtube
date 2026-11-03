# ASSET PROVENANCE — 9:16 vertical cut

| Asset | Origin | Licence / note |
|---|---|---|
| Narration, 16 beats | Generated locally by `runtime/scripts/generate_audio_kokoro.py` for the 16:9 cut, voice `am_onyx`, and **reused here unchanged** | Apache-2.0 model, run locally. No account, no API call, no cost. |
| `src/CanAIDiscoverQuantumMaterials9x16.tsx` | Written for this project | Original portrait recomposition |
| Tc scatter chart | Computed in-component from `TC_DATA`, published measured critical temperatures | Every value cited in `SOURCES.md` |
| Typography, cards, tokens, funnel blocks, rubric rows | Drawn in-composition with layout primitives | Original |
| Palette | The workspace Claude preset — `#FAF9F5` page, `#3D3929` ink, `#D97757` accent | Identical to the 16:9 cut so the two read as one series |

## What is NOT in this film

- No photograph, stock image, or archival still.
- No AI-generated video clip.
- No captured screenshot of a paper, notebook, terminal, or web page.
- No plotted model output, because no model was run for this film.
- **No duplicated audio.** The narration is read from the 16:9 project.

Because there is no human-supplied or third-party media, the human-media
ownership rules and SHA-256 preservation requirements do not apply.

## A note on evidence style

This film reviews published literature rather than a local project, so it
cannot honestly screenshot its sources. It displays **typeset citations** —
full author, year, title, journal, volume, pages — held on screen at the
moment of the claim they support. That is a visible source, and it is honest
about what it is.

In portrait the source plate spans the full safe width at 27 px with a 1.32
line-height, so a long citation wraps to two lines rather than clipping. That
is the only source-tag change from the 16:9 cut.

## Reproducibility

From this directory:

```powershell
.\scripts\render-4k.ps1
```

No audio regeneration is needed. If you do regenerate it, do so in the 16:9
project and then update `AUDIO_BEATS` in both compositions.
