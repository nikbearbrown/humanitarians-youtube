# SHOTLIST — vox-qubit-teleport
# How to Move a Qubit Without Ever Copying It

## Histogram

| Type | Count |
|------|-------|
| CARD/own | 5 (B01, B03, B07, B10, B15) |
| GRAPHIC/own | 8 (B02, B04, B06, B08, B09, B11, B12, B14) |
| STILL/ai | 2 (B05, B13) |

## Rhythm check

CARD · GRAPHIC · CARD · GRAPHIC · STILL · GRAPHIC · CARD · GRAPHIC · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · CARD

Max consecutive same type: 2 ✓ (B08-B09, B11-B12)

## Act map

```
COLD OPEN   B01-B02
QUESTION    B03
PROBLEM     B04-B06
MECHANISM   B07(section)  B08-B09  B10(section)  B11-B12
IMPLICATION B13
EXAMPLE     B14
RECAP       B15
```

## Color law

TEAL (#1F6F5C) = the quantum state |ψ⟩ / the Bell pair resource / the restored qubit after correction — "the good thing we're preserving"
CRIMSON (#BF3339) = blocked quantum channel / measurement that destroys the state / Bob's scrambled qubit before correction — "the problem"
SLATE (#3E5559) = structural elements (wires, panels, section cards), classical channel, gate boxes
GOLD (#F5D061) = NOT USED (never as text; zero role in this film)
INK (#2F2A26) = all running text, annotations, serif labels

## Exclusion confirmations

- No three-qubit amplitude bookkeeping (|Ψ₀⟩, |Ψ₁⟩, |Ψ₂⟩ expansions)
- No correction-table algebra (full 4-row table not shown; only outcome 10→Z in the worked example)
- No dense-coding dual (candidate 09)
- No ρ_B = I/2 matrix displayed (mentioned in narration B13, visual is the STILL)

---

## Open slots — fill-in beats

---

### B05 — STILL · ai — Bell pair distribution

**Context:** Alice and Bob met at some earlier time and distributed a Bell pair. Alice holds qubit A, Bob holds qubit B. The visual should feel like a moment of trust and resource-sharing, not a laboratory procedure.

**Archive search:**
- Wikimedia Commons: "quantum optics laboratory" — may yield real lab photos but not right style
- archive.org: no suitable archival image; this is a schematic editorial illustration

**Generative prompt:**
```
B05, two physicists Alice and Bob in a clean quantum optics laboratory, each holding a small glowing glass sphere representing a quantum device, an optical fiber cable connecting their two devices, shaking hands in agreement, flat editorial illustration style, cream and teal color palette on cream background, no text or labels, dramatic overhead lighting, 16:9 format
```

PROMPT LAW checklist:
- Object: glowing glass spheres (quantum devices) ✓
- Count: two people, two spheres, one fiber cable ✓
- Geometry: fiber cable connects the two spheres ✓
- Material: glass sphere, glowing ✓
- Camera angle: standard front or slight 3/4 angle ✓
- Light source: overhead dramatic ✓
- Exclusions: no text, no equations, no labels ✓

---

### B13 — STILL · ai — Bob waiting, qubit is maximally mixed

**Context:** Before Alice's phone call, Bob's qubit shows no information — it looks like pure noise. Bob is waiting. The visual should convey "information is locked until the phone call arrives."

**Archive search:**
- No suitable archival image; this is a contemporary editorial illustration

**Generative prompt:**
```
B13, a physicist Bob alone in a modern quantum computing laboratory, holding a small rectangular quantum device with a static noise pattern displayed on its small screen, a vintage telephone handset resting on the workbench beside him, a clock on the wall behind him showing time passing, expression of patient waiting, flat editorial illustration style, cream and slate color palette on cream background, no text or labels, 16:9 format
```

PROMPT LAW checklist:
- Object: quantum device with noise display, telephone, clock ✓
- Count: one person, one device, one phone, one clock ✓
- Geometry: device in hand, phone on bench, clock on wall ✓
- Material: clean lab aesthetic ✓
- Camera angle: slightly elevated front view ✓
- Light source: implied overhead lab lighting ✓
- Exclusions: no text, no equations, no Alice ✓
