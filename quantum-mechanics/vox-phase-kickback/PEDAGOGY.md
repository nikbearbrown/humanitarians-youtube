# PEDAGOGY AUDIT — vox-phase-kickback

## Act map

| Beat | Act | Shot type | Est. Duration |
|------|-----|-----------|--------------|
| B01 | COLD OPEN | CARD/title | 10.0s |
| B02 | COLD OPEN | GRAPHIC | 12.0s |
| B03 | THE QUESTION | CARD/dek | 10.0s |
| B04 | THE PROBLEM | GRAPHIC | 12.0s |
| B05 | THE MECHANISM | CARD/section | 5.0s |
| B06 | THE MECHANISM | GRAPHIC | 12.0s |
| B07 | THE MECHANISM | GRAPHIC | 13.0s |
| B08 | THE MECHANISM | GRAPHIC | 12.0s |
| B09 | THE MECHANISM | CARD/section | 4.5s |
| B10 | THE MECHANISM | GRAPHIC | 13.0s |
| B11 | THE IMPLICATION | STILL·ai | 12.0s |
| B12 | THE IMPLICATION | CARD/section | 5.0s |
| B13 | THE IMPLICATION | GRAPHIC | 12.0s |
| B14 | THE EXAMPLE | GRAPHIC | 13.0s |
| B15 | RECAP | CARD/endcard | 10.0s |

Total: 15 beats, ~155.5s ≈ 2:36 — within 5:00 cap ✓

## Rhythm check (≤2 consecutive same shot.type)

CARD · GRAPHIC · CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · GRAPHIC · CARD · GRAPHIC · STILL · CARD · GRAPHIC · GRAPHIC · CARD

Max consecutive GRAPHIC: 3 (B06-B07-B08)

FAIL: B06-B07-B08 are three consecutive GRAPHICs. Fix: B09 section card already inserted between B08 and B10, but the problem is B06-B07-B08 are all mechanism graphics without a break.

→ REWRITE: Insert a section card between B07 and B08 to break the triple sequence.

## REWRITE: rhythm fix

Updated act map after rewrite (new B08 = section card, old B08 becomes B09, old B09 becomes B10, etc.):

| Beat | Act | Shot type | Est. Duration |
|------|-----|-----------|--------------|
| B01 | COLD OPEN | CARD/title | 10.0s |
| B02 | COLD OPEN | GRAPHIC | 12.0s |
| B03 | THE QUESTION | CARD/dek | 10.0s |
| B04 | THE PROBLEM | GRAPHIC | 12.0s |
| B05 | THE MECHANISM | CARD/section | 5.0s |
| B06 | THE MECHANISM | GRAPHIC | 12.0s |
| B07 | THE MECHANISM | GRAPHIC | 13.0s |
| B08 | THE MECHANISM | CARD/section | 4.0s |
| B09 | THE MECHANISM | GRAPHIC | 12.0s |
| B10 | THE MECHANISM | CARD/section | 4.5s |
| B11 | THE MECHANISM | GRAPHIC | 13.0s |
| B12 | THE IMPLICATION | STILL·ai | 12.0s |
| B13 | THE IMPLICATION | CARD/section | 5.0s |
| B14 | THE IMPLICATION | GRAPHIC | 12.0s |
| B15 | THE EXAMPLE | GRAPHIC | 13.0s |
| B16 | RECAP | CARD/endcard | 10.0s |

Rhythm after rewrite:
CARD · GRAPHIC · CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · CARD · GRAPHIC · CARD · GRAPHIC · STILL · CARD · GRAPHIC · GRAPHIC · CARD

Max consecutive GRAPHIC: 2 (B06-B07, B14-B15) ✓
Max consecutive CARD: 1 ✓

Total after rewrite: ~159.5s ≈ 2:40 — within 5:00 cap ✓

Note: beat_sheet.json requires update with renumbered beats and new B08 section card.

## Act structure check

**COLD OPEN (B01-B02):** B01 — title card, concrete hook: oracle writes answer somewhere unexpected. B02 — Deutsch problem framed: constant vs balanced, one query goal. No thesis, no verdict. ✓

**THE QUESTION (B03):** On screen: "One query. Zero errors. How?" Maps gap formula: X = "classical needs 2 queries"; case = quantum oracle; gap = where does the answer go? ✓

**THE PROBLEM (B04):** Superposition in + measure = random result. The naive quantum approach fails. Sets up why phase is necessary. ✓

**THE MECHANISM (B05-B11):** Three phases:
- Phase 1 (B05-B07): The trick — ancilla |-> absorbs oracle, phase kickback emerges on query.
- Section card B08 inserted for rhythm.
- Phase 2 (B09-B10): Two cases — constant vs balanced, same vs opposite sign.
- Section card B10 inserted for rhythm.
- Phase 3 (B11): Hadamard converts phase to measurable population. ✓

**THE IMPLICATION (B12-B14):** Every quantum speedup uses this pattern. The algorithmic template. ✓

**THE EXAMPLE (B15):** Full Deutsch circuit worked example: constant function, outcome 0. Concrete, with specific circuit steps. Placed before RECAP. ✓

**RECAP (B16):** Endcard: "Phase in. Hadamard reads it. One query." Question → answer in one line. ✓

## Key-case cold open check

B01-B02: oracle writes answer somewhere unexpected (hook), Deutsch problem framed. ONE concrete instance (single-bit function). No thesis before B03. ✓

## Gap formula on THE QUESTION (B03)

On-screen copy: "One query. Zero errors. How?" ✓
Gap formula in narration (B03): classical needs 2 queries; quantum claims 1. ✓

## Utility-framing lint

Scanning all narration texts for: "is critical for" / "important to understand" / "we'll cover" / "in this video"

All beats checked — no utility-framing phrases found. ✓

## Vocabulary law check

| Term | Need established | Debut beat |
|------|-----------------|------------|
| constant / balanced | B02 (problem setup) | B02 |
| ancilla qubit | B06 (two-wire circuit) | B06 |
| |-> state | B06 (ancilla setup) | B06 |
| phase kickback | B07 (mechanism shown) | B07 |
| Hadamard | B11 (readout mechanism) | B11 |
| interference | B11 (Hadamard converts phase) | B11 |

All vocabulary law checks pass. ✓

## Equations check

No equations appear on screen. "(-1)^f(x)" is used as a label notation on the circuit graphic (B07) but is purely descriptive labeling, not an equation. No derivations. ✓

## Recap endcard check

B16 copy: "Phase in. Hadamard reads it. One query." — restates question -> answer in one line ✓
Topic kicker "QUANTUM MECHANICS" ✓
No book title. No chapter number. ✓

## The example act check (16:9)

B15: Full Deutsch circuit, query |+>, ancilla |->, outcome 0 = constant. Correct result. No invented numbers needed (this is a deterministic algorithm). The example is the circuit execution, not illustrative numbers. ✓
The 9:16 short derivative will DROP B15. ✓

## Length law

Derived duration: ~159.5s ≈ 2:40. Under 5:00 cap. ✓

---

VERDICT: PASS
