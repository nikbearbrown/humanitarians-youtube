# SHOTLIST — "Stem Separation: Estimation, Not Extraction"

7 beats · ~2:22 · 16:9 4K (3840×2160) · Kokoro `af_bella`
Presenter: Rohan V. · Channel: @HumanitariansAI

Three purpose-built waveform scenes (B01, B02, B04), two shared-library
artifact cards (B03, B05), one shared opener (B00), one shared outro (B06).
**No slates, no pantry slots.**

| Beat | Act | Component | Measured | What is on screen |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | ~21s | Claude composer. Greeting "Hi, Rohan". Topic "HUMANITARIANS AI · AUDIO CONCEPTS". Ask types in. Three output lines: "one flat file in — originals are gone" / "the model estimates, it does not recover" / "bleed and artifacts are normal — calibrate your trust". |
| B01 | BLUF | `StemSepMixCollapse` | ~20s | **4 colored track rows** (Vocals/blue, Drums/terracotta, Bass/purple, Keys/green), each showing an animated waveform. At ~55% through, they collapse into a single gray "MIXED FILE" waveform with overlapping ghost traces. Spark line: "Every instrument summed. The individual contributions are gone." |
| B02 | FRAMEWORK | `StemSepStemOutput` | ~24s | One gray mixed waveform at top (MODEL INPUT). Dashed split-arrows fan to 3 output boxes below — each with a colored dashed border (PROBABILITY), a waveform, and a subtle ghost bleed from an adjacent stem. Spark line: "The outputs look confident. They are probabilities." |
| B03 | MECHANICS | `ClaudeWindow` | ~22s | Artifact view. Title "Why unbaking is impossible". Heading "Estimation, not extraction". Four text lines on additive mixing + statistical prediction. Spark line: "You cannot unbake the cake. The model knows what cakes tend to taste like." |
| B04 | LIMIT | `StemSepBleedViz` | ~22s | Large waveform frame: **vocal stem** (blue, solid) with a **drum bleed ghost** (terracotta, translucent, pulsing) underneath. Annotation arrow pointing at the ghost: "DRUM BLEED / ghost of another source". Bottom comparison strip: "CLEAN STEM" vs "WITH BLEED" side by side. Spark line: "A ghost of another source — the expected cost of estimation." |
| B05 | APPLY | `ClaudeWindow` | ~23s | Artifact view. Title "The trust test". Heading "Good enough vs. lying to you". Three lines: pass criteria, fail criteria, confidence note. Spark line: "It is not giving you the vocal. It is giving you its best guess at the vocal." |
| B06 | OUTRO | `ClaudeTitleOutro` | ~10s | **Matches first video's outro exactly.** Cream ground, serif title in warm ink, terracotta period: "Stem Separation: Estimation, Not Extraction." Handle "@HumanitariansAI" below. Subline "Rohan V.". |

## Lane histogram

| Lane | Beats | Share |
|---|---|---|
| Purpose-built Remotion (this reel) | 3 (B01, B02, B04) | 43% |
| Shared Claude chassis (window / outro / composer) | 4 (B00, B03, B05, B06) | 57% |
| Manim | 0 | — |
| Slates / pantry (human-owed) | **0** | — |

## Consistency with first video

| Element | First video | This video |
|---|---|---|
| Opener | `ClaudeComposerAsk` — "Hi, I'm Rohan, for Humanitarians AI" | `ClaudeComposerAsk` — "Hi, I'm Rohan, for Humanitarians AI" ✓ |
| Outro | `ClaudeTitleOutro` — title · handle · presenter subline | `ClaudeTitleOutro` — title · handle · presenter subline ✓ |
| Ground color | `#FAF9F5` cream | `#FAF9F5` cream ✓ |
| Accent | Terracotta `#D97757` | Terracotta `#D97757` ✓ |
| Type | Tiempos serif + system sans | Same ✓ |
| Voice | Kokoro `af_bella` | Kokoro `af_bella` ✓ |

## New components registered

All three are registered in `Root.tsx` under the `stem-separation-explainer`
folder and live at `runtime/remotion/src/scenes/StemSep*.tsx`. They follow
the same CLAUDE token set, layout conventions (spark line at `bottom * 0.058`,
eyebrow + title top-left), and animation patterns (spring stagger, `interpolate`
opacity) as all other scenes in the library.
