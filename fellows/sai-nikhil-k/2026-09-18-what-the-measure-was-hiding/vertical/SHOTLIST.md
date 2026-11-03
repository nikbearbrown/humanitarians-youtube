# SHOTLIST — What the Measure Was Hiding

Typed work order. Nine beats, one deliverable, **no open slots**: every beat is a
registered Remotion composition rendered from props in `beat_sheet.json`. Nothing
is waiting on generation, purchase, a pantry still or an approval. There is no
user media in this reel at all.

**Lane key** — `remotion` = rendered by `remotion_scenes.py`.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | THE OBJECT | remotion | `ClaudeScienceChipGrid` | illustrate | yes → `ClaudeScienceChipGrid916` |
| B02 | THE FLOOR | remotion | `TypesetMath` | illustrate | yes → `TypesetMath916` |
| B03 | TWO KINDS | remotion | `DivergentFates` | illustrate | yes → `DivergentFates916` |
| B04 | THE INSTRUMENT | remotion | `ExecutedData` | illustrate | yes → `ExecutedData916` |
| B05 | THE FORK | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B06 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B07 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B08 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

All nine `916` siblings were confirmed as real `<Composition id=…>` registrations
in `Root.tsx`, not read off `scenes.json`, which lags it. `ClaudeScienceLayerStack`
and `ClaudeScienceSourceFlow` — the guide's default B01/B02 patterns — still have
no portrait sibling, which is the only reason they are not used here.

Because there is no user media, `shorts.py --vertical` rewires every beat with no
prop edits and no hand-composed plate.

---

## B02 — the equation beat

The three rows are outlined SVG produced locally by
`runtime/scripts/typeset_math.py` (matplotlib mathtext, STIX, `svg.fonttype=path`)
and embedded in `beat_sheet.json` as base64 data URIs. `TypesetMath`'s schema
requires `data:image/svg+xml;base64,` — there is no text fallback path, by design.

| Row | Expression | Reveal |
|---|---|---|
| 1 | NP(k) = (1/nk) Σᵢ₌₁ⁿ \|N_k^H(i) ∩ N_k^L(i)\| | 0.6s |
| 2 | LCMC(k) = NP(k) − k/(n−1) | 6.5s |
| 3 | k/(n−1) = 10/89 ≈ 0.1124 | 12.0s |

Algebra read from `evaluation/projection.py`, not the changelog, and checked
numerically — see FACTCHECK.md. **Portrait stacks the rows independently**, so
the vertical cut needs its own look at the fraction bars, the summation limits
and the sized delimiters.

The composition is 450 frames (15s) and the beat is 19.1s, so the final state
freeze-holds for ~4s. That is intended: row 3 is the number to sit with.

## B04 — the measured table

`ExecutedData` in `table` mode, four rows, the schema maximum. Values come from
`evidence/coverage_exclusion.py`, whose stdout is preserved beside it in
`evidence/coverage_exclusion.out`. **These are recorded measurements, not an
illustration of one**, which is why the `note` prop names the tool, its version
and the script. Composition is 15s against a 21.5s beat, so the completed table
holds for ~6.5s.

---

## Retiming applied at render

`remotion_scenes.py` retimed six beats so the full animation lands inside the
measured narration: B00 1.58×, B01 1.53×, B03 1.56×, B05 1.63×, B06 2.41×,
B07 1.54×, B08 1.54×. B02 and B04 were not retimed — they are shorter than their
beats and freeze-extend instead, as described above.

B06's 2.41× is the steepest. Check in QC that the four artifact lines are still
readable as they land rather than flicking past.

---

## Coverage to measure at QC

GATE V's only automatic check is `underfill`, and centred title/verdict cards
trip it routinely. Record the real ink spans here after the first pass and
compare against them before changing anything. Look at the frames first — B00,
B06 and B08 are centred by design.
