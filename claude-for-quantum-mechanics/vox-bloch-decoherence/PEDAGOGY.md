# PEDAGOGY AUDIT — vox-bloch-decoherence

## Act map

| Beat | Act | Shot type | Est. Duration |
|------|-----|-----------|--------------|
| B01 | COLD OPEN | CARD/title | 10.0s |
| B02 | COLD OPEN | GRAPHIC | 11.0s |
| B03 | COLD OPEN | GRAPHIC | 10.0s |
| B04 | THE QUESTION | CARD/dek | 10.0s |
| B05 | THE PROBLEM | STILL·ai | 12.0s |
| B06 | THE MECHANISM | CARD/section | 5.0s |
| B07 | THE MECHANISM | GRAPHIC | 12.0s |
| B08 | THE MECHANISM | GRAPHIC | 13.0s |
| B09 | THE MECHANISM | GRAPHIC | 11.0s |
| B10 | THE MECHANISM | CARD/section | 5.0s |
| B11 | THE MECHANISM | GRAPHIC | 12.0s |
| B12 | THE IMPLICATION | GRAPHIC | 11.0s |
| B13 | THE IMPLICATION | STILL·ai | 11.0s |
| B14 | THE EXAMPLE | GRAPHIC | 13.0s |
| B15 | THE IMPLICATION | CARD/section | 9.0s |
| B16 | RECAP | CARD/endcard | 12.0s |

Total: 16 beats, ~175s ≈ 2:55 — within 5:00 cap ✓

## Rhythm check (≤2 consecutive same shot.type)

CARD · GRAPHIC · GRAPHIC · CARD · STILL · CARD · GRAPHIC · GRAPHIC · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · CARD · CARD

Max consecutive GRAPHIC: 3 (B07-B08-B09).

FAIL: B07-B08-B09 are three consecutive GRAPHICs. Must fix by inserting a section card between B08 and B09.

→ REWRITE: Insert a section CARD between B08 and B09 to break the triple sequence. Promote "WHEN THE ARROW REACHES ZERO" as a short section card.

## REWRITE: rhythm fix

Updated act map after rewrite (B09 becomes new CARD, original B09 becomes B10, original B10 becomes B11, etc.):

| Beat | Act | Shot type | Est. Duration |
|------|-----|-----------|--------------|
| B01 | COLD OPEN | CARD/title | 10.0s |
| B02 | COLD OPEN | GRAPHIC | 11.0s |
| B03 | COLD OPEN | GRAPHIC | 10.0s |
| B04 | THE QUESTION | CARD/dek | 10.0s |
| B05 | THE PROBLEM | STILL·ai | 12.0s |
| B06 | THE MECHANISM | CARD/section | 5.0s |
| B07 | THE MECHANISM | GRAPHIC | 12.0s |
| B08 | THE MECHANISM | GRAPHIC | 13.0s |
| B09 | THE MECHANISM | CARD/section | 4.0s |
| B10 | THE MECHANISM | GRAPHIC | 11.0s |
| B11 | THE MECHANISM | CARD/section | 5.0s |
| B12 | THE MECHANISM | GRAPHIC | 12.0s |
| B13 | THE IMPLICATION | GRAPHIC | 11.0s |
| B14 | THE IMPLICATION | STILL·ai | 11.0s |
| B15 | THE EXAMPLE | GRAPHIC | 13.0s |
| B16 | THE IMPLICATION | CARD/section | 9.0s |
| B17 | RECAP | CARD/endcard | 12.0s |

Rhythm after rewrite:
CARD · GRAPHIC · GRAPHIC · CARD · STILL · CARD · GRAPHIC · GRAPHIC · CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · CARD · CARD

Max consecutive GRAPHIC: 2 (B02-B03, B07-B08, B12-B13) ✓
Max consecutive CARD: 2 (B16-B17 — IMPLICATION section + RECAP endcard) ✓

Total after rewrite: ~184s ≈ 3:04 — within 5:00 cap ✓

Note: beat_sheet.json requires update with renumbered beats and new B09 section card. Updating now in file.

## Act structure check

**COLD OPEN (B01-B03):** B01 — title card, concrete hook: every qubit has a timer. B02 — Bloch sphere introduced as the visualization object (arrow = quantum state). B03 — precession shown, establishing unitary free evolution. No thesis, no verdict stated. ✓

**THE QUESTION (B04):** On screen: "The qubit is alone. The quantum is not." AND in narration: "The environment... entangles with the qubit, recording which state it is in." Maps gap formula: X = "isolated qubit precesses forever as a pure superposition"; case = real qubits couple to an environment; gap = the arrow must shrink. ✓

**THE PROBLEM (B05):** Shows environment entangling with qubit. Viewer sees the coupling but does not yet know how the arrow responds — sets up mechanism. ✓

**THE MECHANISM (B06-B12):** Two sections separated by cards:
- Section 1 (B06-B08): WHY the arrow shrinks — overlap of environment branches = coherence.
- Section card B09 inserted for rhythm.
- Section 2 (B10-B12): WHAT the arrow does — T2, exponential decay curve. ✓

**THE IMPLICATION (B13-B14):** Cat decoherence time; why macroscopic superpositions are unobservable. ✓

**THE EXAMPLE (B15):** Transmon qubit, T2=200µs, arrow from equator to center. Concrete, illustrative numbers, placed before RECAP. ✓

**RECAP (B16/B17):** Endcard: "Surface = quantum. Center = classical. The environment pulls the arrow in." Topic kicker "QUANTUM MECHANICS". ✓

## Key-case cold open check

B01-B03 show: every qubit has a timer, the arrow is the quantum state, free precession keeps it on the surface. ONE concrete instance (a single qubit, the arrow, the environment). No thesis before B04. ✓

## Gap formula on THE QUESTION (B04)

On-screen copy: "The qubit is alone. The quantum is not." ✓
In narration (B04): "The environment — stray fields, neighboring atoms, vibrating crystal — entangles with the qubit, recording which state it is in." ✓

## Utility-framing lint

Scanning all narration texts for: "is critical for" / "important to understand" / "we'll cover" / "in this video"

All beats checked — no utility-framing phrases found. ✓

## Vocabulary law check

| Term | Need established | Debut beat |
|------|-----------------|------------|
| Bloch sphere / arrow | B01 (hook: "arrow on a sphere") | B02 |
| pure state / surface | B02 (arrow shown on surface) | B02 |
| precession | B02 (arrow introduced; free evolution needed) | B03 |
| environment coupling | B04 (question beat names the cause) | B05 |
| superposition | B02 (surface of sphere = superposition) | B02 |
| overlap / coherence | B07 (branching picture shown, overlap defined) | B07 |
| maximally mixed | B10 (arrow reached center, need name for endpoint) | B10 |
| T2 / coherence time | B10 (center reached, time for name) | B11 |

All vocabulary law checks pass. ✓

## Equations check

No equations appear on screen. T2 is introduced as a label and time axis marker, not as a formula. The T2 = 1/(2T1)+1/Tphi formula is excluded by card and appears nowhere. ✓

## Recap endcard check

B17 copy: "Surface = quantum. Center = classical." — restates question → answer in one line ✓
B17 sub: "The environment pulls the arrow in." — names the mechanism ✓
Topic kicker "QUANTUM MECHANICS" as LabelChip ✓
No book title on screen. No chapter number. ✓

## The example act check (16:9)

B15: Transmon qubit starts on equator (|+⟩), T2=200µs, arrow shrinks to dot at center. Concrete, small countable elements. Numbers labeled ILLUSTRATIVE in FACTCHECK. Placed before RECAP (B17). ✓
The 9:16 short derivative will DROP B15. ✓

## Length law

Derived duration: ~184s ≈ 3:04. Under 5:00 cap. ✓

---

VERDICT: PASS
