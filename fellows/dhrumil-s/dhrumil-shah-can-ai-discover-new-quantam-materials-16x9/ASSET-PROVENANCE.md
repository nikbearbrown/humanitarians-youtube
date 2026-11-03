# ASSET PROVENANCE

| Asset | Origin | Licence / note |
|---|---|---|
| `mp3/beat-*.mp3` (16 files) | Generated locally by `runtime/scripts/generate_audio_kokoro.py` using Kokoro-82M via kokoro-onnx, voice `am_onyx` | Apache-2.0 model, run locally. No account, no API call, no cost. |
| `mp3/timings.json` | Measured from the generated MP3s by the same script | Ground truth for all composition timing |
| `src/CanAIDiscoverQuantumMaterials.tsx` | Written for this project | Original |
| Tc scatter chart | Computed in-component from `TC_DATA`, a table of published measured critical temperatures | Every value cited in `SOURCES.md` |
| Typography, cards, tokens, funnel bars, rubric rows | Drawn in-composition with layout primitives | Original |
| Palette | The workspace Claude preset — `#FAF9F5` page, `#3D3929` ink, `#D97757` accent | Matches the house style of the sibling Mycroft film |

## What is NOT in this film

- No photograph, stock image, or archival still.
- No AI-generated video clip.
- No captured screenshot of a paper, notebook, terminal, or web page.
- No plotted model output, because no model was run for this film.

Because there is no human-supplied or third-party media, the human-media
ownership rules and SHA-256 preservation requirements do not apply to any beat.

## A note on evidence style

The sibling Mycroft film satisfies its source-on-screen requirement with
captured screenshots of a real notebook and report. This film cannot do that:
it reviews published literature, not a local project, and fabricating
screenshots of papers would be exactly the sin the film accuses others of.

Instead it displays **typeset citations** — full author, year, title, journal,
volume and pages — held on screen at the moment of the claim they support. That
is a visible source, and it is honest about what it is. Where a value could not
be verified at build time, it is flagged in `FACTCHECK.md` rather than given a
citation it does not have.

## Reproducibility

Deleting `mp3/` and `output/` and running the following reproduces the master
from source:

```powershell
python runtime/scripts/generate_audio_kokoro.py <this folder>
.\scripts\render-4k.ps1
```

Kokoro is deterministic for a fixed voice and text, so the measured durations —
and therefore the whole timeline — regenerate identically.
