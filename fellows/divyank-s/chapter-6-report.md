# Report: Claude, Packaged. — Chapter 6 (Export to Canvas), Two Cuts

**Topic:** AI1 CLI Chapter 6 — Export to Canvas (Common Cartridge packaging, the one-command build path, import failure modes, module order as pedagogy)
**Skill:** `deep-explainer` (brutalist.art toolkit)
**Location:** `humanitarians-youtube/fellows/divyank-s/2026-09-20-chapter-6/`
**Cost:** $0.00 (Kokoro TTS, local Remotion rendering, no API keys)

## 1. Deliverables

| | 16:9 master | 9:16 Short |
|---|---|---|
| **File** | `claude-liam-export-to-canvas.mp4` | `short/claude-liam-export-to-canvas-short.mp4` |
| **Resolution** | 3840×2160 (4K UHD) | 2160×3840 (4K UHD, vertical) |
| **Duration** | 356.55s (5:56.6) | 168.82s (2:48.8) — includes the full verdict beat |
| **Beats** | 32 | 12 |
| **Gate** | `PEDAGOGY.md` — `VERDICT: PASS` | derived from the signed-off parent; outro narration hand-rewritten and regenerated |
| **Signed** | "Liam, in for Divyank" / `@DivyankSingh` throughout, including the outro card and the Short's silent end card | same |

Both are real, rendered, playable files. Neither is published or authorized for publication.

## 2. Source and how it's covered

Source: `ai1-cli/chapters/06-export-to-canvas.md`, read in full and
cross-checked against its matching research doc and the actual
`build-canvas.sh` script in the book's repo. The chapter's own shape
(Overview → Exercise → Worked Example → What Can Go Wrong → Bridge) maps
to 4 acts:

| Act | Content | Beats |
|---|---|---|
| **I — What You're Actually Exporting** | Common Cartridge standard, `.imscc` = ZIP + XML manifest, the 1EdTech (formerly IMS Global) rebrand, v1.3 profile, why "export to Canvas" really means "any conforming LMS" | `A1-1`–`A1-6` |
| **II — One Command, One Path** | `build-canvas.sh` wraps `build-imscc-standard.py`; inspecting the package by renaming it to `.zip`; what actually gets packaged (chapters→pages, quizzes→quiz objects, chapter order→module order) | `A2-1`–`A2-6` |
| **III — Import, and the Silent Failure** | Importing into a real LMS; the chapter's own warning that an import can finish with zero errors and still show an empty course | `A3-1`–`A3-6` |
| **IV — Order Is an Argument** | The chapter's own worked example (a course imported alphabetically, *Offers* landing before *Foundations*); the discipline of checking against the signed plan, never memory; the chapter's full "what can go wrong" table | `A4-1`–`A4-6` |

## 3. Sourcing and fact-check method

Per `FACTCHECK.md`, every claim is tagged either **Cited** (the Common
Cartridge standard, the 1EdTech rebrand, the v1.3 profile, and the
chapter's own worked example and failure-table rows — all traced to the
chapter's footnotes or its own text) or **General/stable** (the
`build-canvas.sh` → `build-imscc-standard.py` wrapper relationship,
verified directly by reading the actual script in the repo, not assumed
from the chapter text). No version numbers, benchmarks, or import-UI
specifics are asserted beyond what the chapter itself states — the
chapter explicitly flags LMS import UIs as "perishable."

## 4. The archival imagery — used as metaphor, not evidence

| Beat | Image | Stands in for |
|---|---|---|
| A1-1 | Narrow and Standard Gauge Track, Blaenau Ffestiniog Railway Station | one shared standard many systems can run on |
| A1-4 | British Parcels Post — sorting parcels for foreign mail | a package built for any destination, not one platform |
| A2-1 | A Merlin Is Made — Rolls Royce Factory, 1942 (IWM, public domain) | one repeatable build process, same shape every time |
| A3-1 | Empty apartment room with corner windows | something that looks intact from outside, empty inside |
| A4-1 | Card Catalog 2 | order and sequence making a collection findable |

All 5 are real Wikimedia Commons photographs (public domain or
CC-licensed), sourced and sidecar'd per image.

## 5. Two bugs found and fixed during this build

**A silent master, caught before delivery.** The first compile of the
16:9 master logged `audio: silent` instead of the expected `audio:
per-beat narration` — the 4 act-card beats (`A1C`–`A4C`) had been
authored with empty narration text and the wrong Remotion prop shape,
which made `compile.py`'s all-or-nothing audio check fail across the
whole 32-beat timeline. Fixed by giving each card a real spoken act
announcement ("Act one: what you're actually exporting.") and the
correct `{title, index}` prop shape, then re-rendering those 4 beats and
recompiling both passes. Confirmed the fix by checking the compile log
explicitly for `audio: per-beat narration` and an AAC audio stream via
`ffprobe` before calling the master done.

**The Short's silent end card showing the wrong handle.** `shorts.py`
bakes its derived end-card PNG's handle in at generation time via a
`--handle` flag (default `@nikbearbrown`), rather than reading it from
the beat sheet's `card.handle` field at compile time — so editing that
JSON field had no visible effect. Caught visually in the Short's QC
contact sheet, fixed by regenerating that one PNG directly with the
correct handle and recompiling.

## 6. Building the two aspect ratios

Signed for Divyank from the first draft throughout, including the outro
card (using the `handle` override added to `ClaudeTitleOutro` /
`ClaudeTitleOutro916` earlier this session).

Portrait coverage was planned into the beat sheet up front: one
`BinaryBranch`/`DivergentFates` hero beat per act (`A1-5`, `A2-3`,
`A3-3`, `A4-4`). The first manual Short plan (all 5 VOX stills + all 4
hero beats + the full verdict beat) landed at 186.8s — over the 3:00
cap — so the act-4 VOX still (`A4-1`) was dropped in favor of keeping
every hero beat and the full verdict, landing at 177.0s. The recurring
auto-rewritten-outro bug (raw narration fragments stitched into a broken
sentence) appeared again and was hand-fixed before its audio was
generated.

## 7. Known limitations

- **No frame-level Visual QC** was run on either cut (`ART_QC=0`, this
  session's standing agreement).
- **`shorts.py`'s auto-planner still has no concept of portrait-composition
  support or the verdict beat's outsized duration** — two manual
  `--drop` iterations were needed before the Short fit the cap.
- **Neither video is published or authorized for publication.**
