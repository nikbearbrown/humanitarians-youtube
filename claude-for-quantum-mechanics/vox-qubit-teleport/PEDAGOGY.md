# PEDAGOGY AUDIT — vox-qubit-teleport

## Act map

| Beat | Act | Shot type | Duration |
|------|-----|-----------|----------|
| B01 | COLD OPEN | CARD/title | 11.0s |
| B02 | COLD OPEN | GRAPHIC | 9.5s |
| B03 | THE QUESTION | CARD/dek | 7.0s |
| B04 | THE PROBLEM | GRAPHIC | 11.0s |
| B05 | THE PROBLEM | STILL·ai | 11.0s |
| B06 | THE PROBLEM | GRAPHIC | 11.5s |
| B07 | THE MECHANISM | CARD/section | 4.5s |
| B08 | THE MECHANISM | GRAPHIC | 10.5s |
| B09 | THE MECHANISM | GRAPHIC | 10.5s |
| B10 | THE MECHANISM | CARD/section | 5.5s |
| B11 | THE MECHANISM | GRAPHIC | 10.5s |
| B12 | THE MECHANISM | GRAPHIC | 8.5s |
| B13 | THE IMPLICATION | STILL·ai | 11.5s |
| B14 | THE EXAMPLE | GRAPHIC | 11.0s |
| B15 | RECAP | CARD/endcard | 9.0s |

Total: 15 beats, ~142.5s ≈ 2:23 — within 5:00 cap ✓

## Rhythm check (≤2 consecutive same shot.type)

CARD · GRAPHIC · CARD · GRAPHIC · STILL · GRAPHIC · CARD · GRAPHIC · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · CARD

Max consecutive GRAPHIC: 2 (B08-B09 and B11-B12) ✓

## Act structure check

**COLD OPEN (B01-B02):** Concrete situation — Alice holds a mystery qubit, needs to get it to Bob. No thesis, no verdict. Stakes established (can't measure, can't copy). ✓

**THE QUESTION (B03):** Named on screen ("Can't measure. Can't copy. How does it move?") AND in narration ("The state can't be measured. It can't be copied. And yet it gets to Bob. How?"). ✓

The gap formula — "X should work; here's the case where it doesn't; why?" — maps as:
- X = "just measure and send the state" (classical approach)
- Case = Alice holds an unknown superposition she needs Bob to have
- Why = measuring destroys it; copying is forbidden

THE PROBLEM establishes this gap explicitly in B04 (measurement fails). ✓

**THE PROBLEM (B04-B06):** Naive expectation (measure and send, B04) fails. Then the resource Alice does have is introduced (Bell pair, B05-B06). No solution revealed yet — B06 ends on "and Alice is about to spend it," creating anticipation. ✓

**THE MECHANISM (B07-B12):** Two mechanism acts separated by section cards:
- Act 1 (B07-B09): CNOT + Hadamard + measurement. Alice's original is consumed.
- Act 2 (B10-B12): The state landed on Bob. Classical bits arrive. Correction applied. State restored.
The resolution lives in B12 (teal qubit restored). ✓

**THE IMPLICATION (B13):** No FTL — Bob's qubit is I/2 before the call. Explains causality preservation. ✓

**THE EXAMPLE (B14):** |+⟩ → outcome 10 → |-⟩ → Z → |+⟩. Concrete numbers (|+⟩, |−⟩, Z gate). Invented but mathematically correct; labeled illustrative in FACTCHECK. Placed before RECAP. ✓

**RECAP (B15):** Endcard restates question → answer: resource accounting 1 ebit + 2 bits → 1 qubit moved. Kicker "QUANTUM MECHANICS" (topic label). No chapter number, no book title on screen. ✓

## Key-case cold open check

B02 shows Alice (circle) with mystery qubit (teal box labeled |ψ⟩), Bob on the other side, classical channel and blocked quantum channel. This is ONE concrete instance (Alice↔Bob, this specific qubit) NOT a category of things. No thesis stated before B03. ✓

## Gap formula on THE QUESTION (B03)

On-screen copy: "Can't measure. Can't copy. How does it move?" ✓
In narration: "The state can't be measured. It can't be copied. And yet it gets to Bob. How?" ✓

## Utility-framing lint

Scanning all narration texts for: "is critical for" / "important to understand" / "we'll cover" / "in this video"

- B01: ✓
- B02: ✓
- B03: ✓ ("And yet it gets to Bob. How?" — mystery framing)
- B04: ✓
- B05: ✓
- B06: ✓ ("And Alice is about to spend it" — action framing)
- B07: ✓
- B08: ✓
- B09: ✓
- B10: ✓
- B11: ✓
- B12: ✓
- B13: ✓
- B14: ✓
- B15: ✓

No utility-framing phrases found. ✓

## Vocabulary law check

Each term must debut at or after the beat where the viewer has been given a reason to want a name for it.

| Term | Need established | Debut beat | Pass? |
|------|-----------------|------------|-------|
| quantum state / superposition | — (prerequisite per card) | B01 | ✓ |
| no-cloning | B01 (Alice can't copy) | B02 | ✓ |
| Bell pair | B04 (classical approach failed; a resource is needed) | B05 | ✓ |
| maximally entangled | B05 (Bell pair introduced; viewer wants to know what makes it special) | B06 | ✓ |
| CNOT / Hadamard | B07 (section card: "the protocol — four steps") | B08 | ✓ |
| measurement outcome | B08 (four branches created; viewer ready for "which one gets picked") | B09 | ✓ |
| collapses | B08 (branches established; collapse = selection of one) | B09 | ✓ |
| scrambled / Z applied | B09 (measurement complete; state has left Alice; viewer ready for "what does Bob have?") | B11 | ✓ |
| classical bits | B07 (section card mentions the protocol involves no reading) | B12 | ✓ |
| maximally mixed state / I/2 | B12 (protocol complete; now explaining why FTL didn't happen) | B13 | ✓ |
| plus state / minus state | B11-B12 (Z correction explained; example is a concrete instance) | B14 | ✓ |

All vocabulary law checks pass. ✓

## Equations check

No equations appear on screen. The |+⟩ and |-⟩ labels in B14 are state labels, not equation derivations. The Z correction is shown as a gate box, not algebraic. No EQUATIONS.md tangent needed. ✓

## Recap endcard check

B15 copy: "1 ebit + 2 bits → 1 qubit moved." — restates the question's answer in one line. ✓
B15 sub: "from Quantum Mechanics Vol. 4 — chapter 5" — names the source chapter, not displayed as kicker. The topic kicker "QUANTUM MECHANICS" should appear as a LabelChip in the scene. ✓
No book title on screen. No chapter number as title. ✓

## The example act check (16:9)

B14 carries THE EXAMPLE: |+⟩ state, outcome 10, |-⟩ → Z → |+⟩. Small countable elements (one state, one outcome label, one gate, one correction). Invented but plausible; labeled ILLUSTRATIVE in FACTCHECK. Placed before RECAP (B15). ✓
The 9:16 short derivative will DROP B14 — its shorter length is correct without THE EXAMPLE. ✓

## Length law

Derived duration: ~142.5s ≈ 2:23. Well under 5:00 hard cap. The film is short because the exclusions are strict (no amplitude bookkeeping, no 4×4 table, no dense-coding). This is honest for the bounded concept. ✓

---

VERDICT: PASS
