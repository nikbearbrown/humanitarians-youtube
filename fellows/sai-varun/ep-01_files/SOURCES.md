# SOURCES — The Silent Thief (The Uncertain Eye, S1E01)

Source of record: `brutalist.art/Context/THE_UNCERTAIN_EYE_series.md`, Episode 1
plus the DOUBLE-CHECK LAW verified-facts list (§A).
Project paper: Garimella Narasimha, Brown, Sridhar (2026), CC-BY 4.0.

## Claims on screen or in narration, and their basis

| Claim | Basis | Status |
|---|---|---|
| *glaukos* = pale blue-green/gray; ~2,400 years ago, age of Hippocrates | §A | VERIFIED |
| Leading cause of **irreversible** blindness | §A | VERIFIED |
| ~80M (2020) → ~111M (2040) | §A | VERIFIED |
| Silent until up to ~40% nerve-fiber loss | §A | VERIFIED |
| Optic nerve = "more than a million fibers" | NOT in §A — see correction 3 | ADDED, FLAGGED |

## Corrections applied (DOUBLE-CHECK LAW)

**1. *glaukos* — the word, not the disease name.**
§A states Hippocrates used *glaukosis* for elderly blindness, and that *glaukos*
is the colour term. The episode draft reads "Greek physicians named a kind of
blindness *glaukos*", which quietly promotes a colour adjective to a disease
name. Narration rewritten to: "Greek physicians had a word for the pale,
gray-green shimmer in a failing eye — *glaukos*." The word now attaches to the
appearance, which is what it meant. The dramatic beat is unchanged.

**2. "Color of the sea" — explicitly not used.**
§A bans this gloss. It appears nowhere in the sheet. Confirmed by grep.

**3. "Over a million fibers" — added fact, flagged for your sign-off.**
The episode draft's "cable of over a million fibers" is standard, well-established
anatomy (the human optic nerve carries roughly 1.0–1.2 million retinal ganglion
cell axons), but it is **not** on the §A verified list. I kept your line in its
conservative form — "more than a million" — rather than dropping it, because it
carries the beat. **It is the one claim in this episode not covered by §A, and it
is yours to confirm or cut.** If you want it gone, B03's narration works without
it ("a cable of nerve fibers carrying every image from your eye to your brain")
and only the `countLabel` prop changes.

**4. Hook softened to match §A's wording.**
Draft: "one of the leading causes of blindness on Earth". §A supports "leading
cause of *irreversible* blindness". The hook keeps the soft form ("a leading
cause of blindness on Earth") and B02 states the precise, verified form with
"irreversible" load-bearing. Soft attribution kept soft.

**5. Zero performance figures.**
§B bans second-tier numbers; the season's only permitted performance figure is
~0.85 AUROC (first tier), which does not appear until E03. This episode contains
no AUROC, no accuracy, no sensitivity. B07's caption states plainly: "No
performance claim is made in this episode." This also satisfies the standing
number policy carried over from the sibling reel.

**6. No "rejected", no leakage, no agents.**
§C framing and the E06/E07 content are not touched here — Episode 1 predates
them in the story. Nothing is foreshadowed that would need the banned framing.

## Redraw / rebuild notes (REBUILD LAW)

All figures are native animated Remotion graphics. Nothing is a screenshot or a
lifted image. Three carry an on-screen "Redrawn (simplified)" or "Schematic"
caption because they depict a clinical pattern rather than measured data:
B02 (`HaiGlaucomaStakes`), B03 (`UeNerveBundle`), B04 (`UeSilentWindow`),
B05 (`UeLooksNormal`). No patient data appears anywhere in this episode.

## Library provenance

- `HaiGlaucomaStakes` — built for `hai-only-the-uncertain-cases`
  (`runtime/remotion/src/HaiGlaucoma.tsx`), reused unchanged at B02.
- Index note: the eight `HaiGlaucoma*` components were registered as
  `<Composition>` in `Root.tsx` but were **absent from `scenes.json`**, so
  `./art scenes --check HaiGlaucomaStakes` reported NOT RENDERABLE. Ran
  `./art scene-index` (601 → 609 renderable) to repair the index. Without that,
  this episode would have re-authored a component that already existed.

## Determinism

- `BrutalistHesitantWriter` seed: **4801** (set per reel; never left at default).
- All new components are pure functions of the audio clock via `useP()`.
