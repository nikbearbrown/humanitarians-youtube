# Report: Claude, Converted. — Chapter 9 (Convert What Survives), Two Cuts

**Topic:** AI1 CLI Chapter 9 — Convert What Survives (conversion maps, directed agent transformation, the real three-way worked example, GATE 3)
**Skill:** `deep-explainer` (brutalist.art toolkit)
**Location:** `humanitarians-youtube/fellows/divyank-s/2026-10-13-chapter9/`
**Cost:** $0.00 (Kokoro TTS, local Remotion rendering, no API keys)

## 1. Deliverables

| | 16:9 master | 9:16 Short |
|---|---|---|
| **File** | `claude-liam-convert-what-survives.mp4` | `short/claude-liam-convert-what-survives-short.mp4` |
| **Resolution** | 3840×2160 (4K UHD) | 2160×3840 (4K UHD, vertical) |
| **Duration** | 345.64s (5:45.6) | 169.98s (2:50.0) — includes the full verdict beat |
| **Beats** | 32 | 12 |
| **Gate** | `PEDAGOGY.md` — `VERDICT: PASS` | derived from the signed-off parent; outro narration hand-rewritten and regenerated |
| **Signed** | "Liam, in for Divyank" / `@DivyankSingh` throughout, including the outro card and the Short's silent end card | same |

Both are real, rendered, playable files. Neither is published or authorized for publication.

## 2. Source and how it's covered

Source: `ai1-cli/chapters/09-convert-what-survives.md` — flagged as a
"hard chapter" in the book's own `chapters-spec.md` — read in full and
cross-checked against its matching research doc. The chapter's shape
maps to 4 acts:

| Act | Content | Beats |
|---|---|---|
| **I — Genre Transformation Isn't Freehand** | The four conversion maps (Profile→case study, Proposal→sales page/pitch, Evaluation/review→product review, Rhetorical analysis→ad teardown), what each keeps vs. adds, and the FTC legal edge stated once (case studies/reviews become testimonials once incentivized) | `A1-1`–`A1-6` |
| **II — Convert Two, Directed Not Delegated** | Step 1 of the exercise: directing an agent conversion by naming the map, the reader, and the specific proof, rather than handing the agent the wheel | `A2-1`–`A2-6` |
| **III — The Human Rewrite, and the Signature No Agent Can Give** | The chapter's real three-way worked example (original → live agent conversion → deliberately blank human-rewrite slot), the read-aloud test, and GATE 3 — the one signature no agent may ever give | `A3-1`–`A3-6` |
| **IV — What Can Go Wrong** | The chapter's own 4-row failure table (generic conversion, no-proof claims, signing agent prose, the agent "offering" to sign), bridging to Chapter 10 | `A4-1`–`A4-6` |

## 3. An honesty constraint carried through deliberately

The chapter is explicit that its worked example's agent-conversion
sentence is **real and live** — not fabricated for the book — but that
it **deliberately does not supply a fake human rewrite**, because
inventing one would be the exact dishonesty the chapter exists to
prevent. This build's narration (beats A3-2 and A3-3) preserves that
constraint rather than smoothing over it: it quotes the real original
sentence and the real agent-converted sentence verbatim, and narrates
the human-rewrite slot as intentionally blank — never inventing content
to fill it.

## 4. Sourcing and fact-check method

Per `FACTCHECK.md`, the four conversion maps and the chapter's own
failure-table rows are tagged **Cited** (traced to the chapter's own
text and its one footnote — the FTC's 2023 Endorsement Guides and 2024
final Rule, verified against the Federal Register per the research doc).
The research doc itself flags genre-structure specifics as practitioner
consensus connected to already-sourced copywriting classics (Ogilvy,
Reeves), not independently new research, and `FACTCHECK.md` preserves
that distinction rather than overstating it.

## 5. The archival imagery — and an unusually rocky sourcing pass

| Beat | Image | Stands in for |
|---|---|---|
| A1-1 | Production of aluminium pot (sand mold), a small foundry | one mold shape producing a related but different object each time |
| A2-1 | U.S. Navy air traffic control center | directing a process without personally performing it |
| A3-1 | A hand signing a legal contract | a signature carrying personal accountability |
| A4-1 | Vintage rubber office stamps | an official marking that certifies, or withholds certifying |

All 4 are real Wikimedia Commons photographs (public domain or
CC-licensed), sourced and sidecar'd per image. This build's image search
was the roughest of the session: a "stencil" metaphor candidate turned
out, on full review, to be vulgar graffiti and was rejected outright; a
ship's-wheel candidate turned out to be a decorative chandelier rather
than a usable helm photograph; a conductor photo was rejected for
depicting an identifiable named individual (consistent with this
session's standing rule against decorative use of named real people);
and the Wikimedia Commons API itself returned a rate-limit error
mid-session, requiring a short wait before retrying. Rather than force a
weak fifth image to hit the usual quota, the build settled on 4 VOX
images (14.3% of 28 body beats, slightly under the usual 15–30% band) —
flagged explicitly in `PEDAGOGY.md` and `SOURCES.md` rather than
silently under-delivering against the established pattern.

## 6. Building the two aspect ratios

Signed for Divyank from the first draft throughout, including the outro
card. Portrait coverage was planned into the beat sheet up front: one
`BinaryBranch`/`DivergentFates` hero beat per act (`A1-5`, `A2-4`,
`A3-4`, `A4-4`). The first manual Short plan (all 4 VOX stills + all 4
hero beats + the full verdict beat) landed at 188.4s — over the 3:00 cap
— so the Act IV VOX still (`A4-1`) was dropped, landing at 178.1s. The
recurring auto-rewritten-outro bug (raw narration fragments stitched
into a broken sentence) appeared again and was hand-fixed before its
audio was generated. `shorts.py` was called with `--handle
@DivyankSingh` explicitly (the lesson carried forward from the Chapter
6/7 builds), and both the outro card and the Short's end card showed the
correct handle on the first compile.

## 7. Known limitations

- **No frame-level Visual QC** was run on either cut (`ART_QC=0`, this
  session's standing agreement).
- **The VOX quota landed at 14.3%, slightly under the usual 15–30%
  band** — a deliberate call given this build's sourcing difficulties,
  documented rather than patched over with a weak image.
- **`shorts.py`'s auto-planner still has no concept of portrait-composition
  support or the verdict beat's outsized duration** — manual `--drop`
  iteration was needed before the Short fit the cap.
- **Neither video is published or authorized for publication.**
