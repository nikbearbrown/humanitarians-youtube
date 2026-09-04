# Can AI Discover New Quantum Materials? — 9:16 vertical cut

Complete, reproducible source for the **portrait** cut of Dhrumil Shah's
three-minute evidence review of machine learning in superconductor search.

This is a native 2160 × 3840 recomposition of the approved 16:9 master — not a
crop, not a resize, not a letterbox. Every layout was redrawn for a vertical
canvas. The narration, timing, argument, and every cited figure are identical.

## Deliverable

- **Master:** 2160 × 3840, 9:16 portrait, 24 fps, exactly 03:00
- **Renderer:** Remotion / React / TypeScript inside the supplied
  `brutalist.art-main` workspace
- **Narration:** the same 16 Kokoro `am_onyx` beats, reused unchanged from the
  16:9 project — measured durations remain the master clock
- **Evidence:** typeset citations held on screen at the moment of each claim,
  plus one chart computed from published measured critical temperatures

## The argument (unchanged from the 16:9 cut)

**AI does not discover superconductors. It reorders the search queue. The
laboratory still decides.**

Confirmation is a five-link chain — rank, stability, synthesis,
zero-resistance measurement, Meissner effect — and machine learning touches
exactly one link. The film then stress-tests its own rubric against LK-99, the
2023 room-temperature superconductivity claim that collapsed under
replication.

## The framework: CLAIM

Five questions, on screen at 00:26, before any example. Labelled on screen as
the presenter's review framework — not a feature of any dataset or model.

| Axis | Question |
|---|---|
| **C** — Composition | Is there an exact, synthesizable formula? |
| **L** — Labels | Measured Tc, or a computed proxy? |
| **A** — Applicability | Is the candidate inside the training distribution? |
| **I** — Independent | Has another laboratory reproduced it? |
| **M** — Measurement | Zero resistance *and* Meissner — at what pressure? |

## What is different in this cut

Only layout. Documented scene by scene in
[docs/FILMS.md](docs/FILMS.md) and
[config/films-manifest.json](config/films-manifest.json):

- Horizontal token chains became **vertical stacks with down-arrows**
  (Scene 01 pipeline, Scene 07 confirmation chain).
- Two-column comparisons became **top/bottom stacks** (Scene 06, Scene 08).
  In Scene 08 both panels are still on screen *simultaneously* for 11.2 s.
- Side-by-side card pairs became **full-width stacks** (Scenes 03, 04).
- CLAIM became a **3 + 2 grid** instead of one 5-across row.
- The Tc chart got **taller** (860 px vs 452 px) rather than squashed.
- One label re-anchored: `YBCO 92K` cleared the BSCCO point, which portrait
  compression had pushed it onto. Caught in preflight, fixed before the master.

## What is identical

Narration audio, `AUDIO_BEATS` timing, scene order, on-screen copy, every
cited figure, every source tag, the CLAIM framework, and both honesty
disclosures (`PRESENTER FRAMEWORK · CLAIM`, `ILLUSTRATIVE SCHEMATIC`).

## One open item, inherited

The ±9.5 K RMSE in Scene 04 is believed correct but is flagged **VERIFY** in
[FACTCHECK.md](FACTCHECK.md) and must be confirmed against Hamidieh 2018 §4
before public release. It is the same number in both cuts, so verifying it
once clears both. See [PROOF-COMPLIANCE.md](PROOF-COMPLIANCE.md).

## Folder map

```text
Can-AI-discover-new-quantum-materials-9x16/
├── src/CanAIDiscoverQuantumMaterials9x16.tsx  # complete 4K portrait composition
├── config/                                    # video, render, and films manifests
├── docs/                                      # specs, per-film breakdown, rendering
├── scripts/                                   # sync, render, verify, QC stills
├── output/                                    # rendered master (gitignored)
├── _qc/                                       # preflight + final QA stills (gitignored)
├── beat_sheet.json                            # authored source of truth
├── todo.json                                  # machine-readable beat + open-item ledger
├── CURRENT-RENDER-MANIFEST.md                 # canonical 180 s render map for this cut
├── SOURCE-SCRIPT.md                           # exact narration (shared)
├── SHOTLIST.md                                # portrait shot-by-shot legibility contract
├── PROOF-COMPLIANCE.md                        # skeptical review, rubric, ship verdict
├── FACTCHECK.md                               # claim-by-claim verdicts (shared)
├── SOURCES.md                                 # full citations (shared)
├── PEDAGOGY.md                                # narration gate and register audit (shared)
├── ASSET-PROVENANCE.md                        # origin of every asset
├── MEDIA-LEDGER.md                            # beat classification for this cut
├── REFERENCE-ANALYSIS.md                      # what the references informed
├── INTEGRATION.md                             # Remotion registry contract
├── STATUS.md / ToDo.md                        # stage and remaining work
└── FINAL-QA.md                                # rendered-master verification
```

Documents marked *(shared)* are copies of the 16:9 originals and carry a
banner saying so — they describe content, which does not differ by aspect
ratio.

## Dependency on the 16:9 project

This cut **reuses** the narration from
`../Can-AI-discover-new-quantum-materials-16x9/mp3/` rather than keeping a
second copy. Two copies of the same audio are two things that can drift apart.

The 16:9 folder must therefore be present and keep that name for this project
to render. `scripts/sync-to-remotion.ps1` fails with a clear message if it is
not.

## Build

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\render-4k.ps1
```

Full details, including what each script does, in
[docs/RENDERING.md](docs/RENDERING.md).

## Publishing

There is no publishing machinery here and none was used. A rendered master is
not authorization to upload. Resolve the open VERIFY item first.
