# SOURCES — `ai-data-quality` · "The Rule, Not The Report."

## External sources

**None cited, and none needed.** This reel argues a mechanism, not a finding.
Its worked example is declared as such on screen and audited claim by claim in
`FACTCHECK.md`. Nothing in the narration reports a study, a benchmark, a
market figure, or a vendor capability.

One naming standard is referenced by name because the example's rule uses it:

| Reference | Used for | URL |
|---|---|---|
| ISO 3166-1 alpha-2 | the allowed set in the example expectation (`US`, `GB`, …) | <https://www.iso.org/iso-3166-country-codes.html> |

## Corrections applied (DOUBLE-CHECK LAW)

Logged in full in `FACTCHECK.md` § "Corrections applied during scripting".
In summary:

1. **An arithmetic error was caught and fixed before audio.** The first draft
   of B02 asserted "roughly eleven person-years" from 3,988 columns × 40
   minutes. The true figure is ~332 eight-hour days (≈1.3 person-years) — the
   claim was wrong by about 8×. The script now says "three hundred and thirty
   working days", and the multiplication was moved **on screen** so a viewer
   can check it rather than take it.
2. **The 41 in B00 and the 41 in B06 were disambiguated.** They are two
   different facts about the same example (columns with no inferable rule vs.
   proposals rejected on review); B06's lane note was rewritten to
   "a rule the business never had" so they don't read as the same number
   twice.
3. **A green success tick was cut from B01's score card.** The Claude palette
   permits exactly one accent per beat; a second colour would have stolen the
   focal moment from the terracotta strike.

## Provenance of the visuals

Every frame is generated in this repository. Nothing is a screenshot, a
stock image, a lifted figure, or an AI-generated still (REBUILD LAW).

| Beat | Source of the image |
|---|---|
| B00 B04 B10 | `ClaudeComposerAsk` — house scene, `runtime/remotion/src/scenes/` |
| B09 | `ClaudeVerdictArtifact` — house scene |
| B11 | `ClaudeTitleOutro` — house scene |
| B01 B02 B03 B05 B06 B07 B08 | `DataQualityIllus.tsx` — written for this reel; see its header for the WHAT/WHEN/ADAPTED-FROM of each component |

`DqPipelineGate` adapts `SourceFlow` from
`runtime/remotion/src/illustrations/structural.tsx` (source → destination),
adding the gate and the second, diverting outcome. `DqWhereItBites`
re-proportions `ChipGrid` from peer chips into three argument cards. The other
five are new patterns and are documented as such in the file header, per the
starter-template contract in `ILLUSTRATIONS.md`.

## Determinism

No seeds are needed: none of these scenes use randomness. Every component is a
pure function of `useP()` (normalised beat progress), with fixed index-derived
positions where a scattered look was wanted (`spread()` in `DqRuleScale`, the
fixed `FAILS` set in `DqPipelineGate`). Same props → identical frames, every
render, at any `--scale`.

## Voice

Kokoro-82M via `kokoro-onnx`, voice `am_onyx` ("Onyx"), local, Apache-2.0,
no API and no key. Model files ship in the toolkit at
`runtime/models/kokoro/`. Cost of this reel: **$0.00**.

The narrator is the human (Hussain), speaking in the first person, so the
house IN-FOR-BEAR sign-off does not apply here — logged as a deliberate
override in `PEDAGOGY.md` and in the beat sheet's metadata note.
