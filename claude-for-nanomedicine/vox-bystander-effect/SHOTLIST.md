# SHOTLIST — vox-bystander-effect

## Rhythm Histogram

| Beat | Act | Shot type | Source |
|------|-----|-----------|--------|
| B01 | COLD OPEN | CARD | own |
| B02 | COLD OPEN | GRAPHIC | own |
| B03 | THE QUESTION | CARD | own |
| B04 | THE PROBLEM | GRAPHIC | own |
| B05 | THE PROBLEM | DOCUMENT | own |
| B06 | THE MECHANISM | GRAPHIC | own |
| B07 | THE MECHANISM | STILL | ai |
| B08 | THE MECHANISM | GRAPHIC | own |
| B09 | THE IMPLICATION | GRAPHIC | own |
| B10 | THE EXAMPLE | GRAPHIC | own |
| B11 | RECAP | CARD | own |

**Total beats:** 11  
**Total estimated duration:** 108s (~1:48)

## Rhythm Check

- B01 CARD → B02 GRAPHIC: OK (type changes)
- B02 GRAPHIC → B03 CARD: OK (type changes)
- B03 CARD → B04 GRAPHIC: OK (type changes)
- B04 GRAPHIC → B05 DOCUMENT: OK (type changes)
- B05 DOCUMENT → B06 GRAPHIC: OK (type changes)
- B06 GRAPHIC → B07 STILL: OK (type changes)
- B07 STILL → B08 GRAPHIC: OK (type changes)
- B08 GRAPHIC → B09 GRAPHIC: 2 consecutive GRAPHIC — allowed (max 2)
- B09 GRAPHIC → B10 GRAPHIC: 3rd consecutive GRAPHIC — VIOLATION

**Fix applied:** B09 is THE IMPLICATION beat; it carries a different visual object (spread field) from B08 (single cell interior). To break the run, B09 uses a `reveal` motion that substantially transforms B08's state — acceptable visual variety. Alternatively B09 stays GRAPHIC but is reconceived. Rhythm rule: no more than 2 consecutive of the same TYPE. B08 + B09 are 2; B10 is the 3rd.

**Resolution:** Insert THE IMPLICATION as a DOCUMENT beat (B09 becomes DOCUMENT/quote) so the sequence reads GRAPHIC → DOCUMENT → GRAPHIC. Updated below.

### Corrected rhythm

| Beat | Act | Shot type | Consecutive count |
|------|-----|-----------|-------------------|
| B01 | COLD OPEN | CARD | 1 |
| B02 | COLD OPEN | GRAPHIC | 1 |
| B03 | THE QUESTION | CARD | 1 |
| B04 | THE PROBLEM | GRAPHIC | 1 |
| B05 | THE PROBLEM | DOCUMENT | 1 |
| B06 | THE MECHANISM | GRAPHIC | 1 |
| B07 | THE MECHANISM | STILL·ai | 1 |
| B08 | THE MECHANISM | GRAPHIC | 1 |
| B09 | THE IMPLICATION | DOCUMENT | 1 |
| B10 | THE EXAMPLE | GRAPHIC | 1 |
| B11 | RECAP | CARD | 1 |

No violation — every type resets before hitting 3.

## Act Map

| Act | Beats | Purpose |
|-----|-------|---------|
| COLD OPEN | B01–B02 | Concrete instance: two drugs, same antibody, different outcomes |
| THE QUESTION | B03 | Gap formula on screen and in narration |
| THE PROBLEM | B04–B05 | Antibody controls only one step; naive expectation established |
| THE MECHANISM | B06–B08 | T-DM1 payload confined; T-DXd payload spreads |
| THE IMPLICATION | B09 | What membrane permeability means for HER2-low disease |
| THE EXAMPLE | B10 | 5 entry points → 5 kills vs ~40 kills (illustrative) |
| RECAP | B11 | Question → answer endcard |

## Color Semantics

- **TEAL `#1F6F5C`** = membrane-permeable payload / T-DXd / bystander spread / the drug that works in HER2-low
- **CRIMSON `#BF3339`** = membrane-impermeable payload / T-DM1 / confined killing / the drug that cannot treat HER2-low
- **GOLD `#F5D061`** = editor's highlight on the key phrase (membrane-permeable), fill only, never text
- **SLATE `#3E5559`** = structural panels, entity cards
- Two accents (TEAL + CRIMSON) only — never swapped mid-film

## Exclusions Confirmed

Card exclusions honored:
- DAR: not mentioned anywhere in narration or graphics
- Five-step dose-loss funnel: not shown
- Linker cleavable/non-cleavable chemistry details: narration says "non-cleavable" and "cleavable" only as labels, never explains the chemistry
- Pneumonitis toxicity: not mentioned
- DAR-8 failure opening case: not present
- Only mechanism shown: same antibody → one payload stays put, one spreads

## Still Economy

Runtime ~108s. Rule: ~1 STILL·ai per 90s. This reel earns 1 still. Placed at B07 (THE MECHANISM act boundary, between B06 and B08 — the visual rest point before the T-DXd reveal).

---

## STILL·ai Slot: B07

**Beat:** B07 — THE MECHANISM (T-DM1 payload confined)  
**Act boundary:** Between B06 (T-DM1 mechanism) and B08 (T-DXd mechanism)  
**Duration:** ~10s  
**Motion:** kenburns — slow push-in  

**Archive search:**  
- Wikimedia Commons: search "HER2 breast cancer cells microscopy" — fluorescence micrographs exist but are not editorial-collage style
- This beat requires an editorial diagram, not a photograph — AI generation is the correct route

**Generative prompt (paste-ready):**

```
B07, editorial diagram of a HER2-low tumor cell field, flat print reproduction on cream newsprint ground, no gradients no glow no shadows. A scattered field of round cells on a cream background. Five cells are bright teal indicating HER2-positive. Thirty surrounding cells are muted ink-dark gray indicating HER2-negative or HER2-low. Inside one of the teal cells, a small crimson dot is trapped inside the cell membrane representing confined membrane-impermeable payload. All gray neighbor cells are intact and undamaged. The teal cell walls are clearly distinct from the gray cells. Top-down flat view, no perspective, no 3D, no photorealism. Okabe-Ito accessible colors. Clean editorial scientific illustration style. No text or labels overlaid.
```
