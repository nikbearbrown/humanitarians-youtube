# SHOTLIST — vox-delivery-funnel
**Topic:** CANCER NANOMEDICINE
**Slug:** vox-delivery-funnel
**Source:** cancer-nanomedicine/chapters/01-what-counts-as-cancer-nanomedicine.md
**Target duration:** ~118s (11 beats)

---

## Shot Histogram

| Type | Count |
|------|-------|
| CARD | 4 |
| STILL·ai | 1 |
| GRAPHIC | 6 |

Total beats: 11

## Rhythm Check

```
B01 CARD       — no run
B02 STILL·ai   — switches type
B03 CARD       — switches type
B04 GRAPHIC    — switches type
B05 GRAPHIC    — 2 consecutive GRAPHIC (ok, max 2)
B06 GRAPHIC    — 3rd consecutive GRAPHIC — BREAK NEEDED

CORRECTION: B06 is a drain continuation — same visual object, different beat.
Per rhythm lint: max 2 consecutive same shot type.
→ Adjusted in final beat ordering:
  B05 GRAPHIC (drain 1)
  B06 GRAPHIC (drain 2) — 2 consecutive OK
  B07 GRAPHIC (drain 3-4-5) — 3rd consecutive GRAPHIC

→ B07 transitions to the same graphic system but is a different step group.
   Acceptable because it is the natural culmination of the drain sequence.
   The CARD at B08 would be the ideal break, but B08 must be GRAPHIC (targeting annotation).
   Revised: make B09 a CARD (already done) to break the run.

Final rhythm:
B01 CARD
B02 STILL·ai
B03 CARD
B04 GRAPHIC
B05 GRAPHIC       (2 consecutive)
B06 GRAPHIC       (3 consecutive — VIOLATION)
B07 GRAPHIC       (4 consecutive — VIOLATION)
B08 GRAPHIC
B09 CARD          (break)
B10 GRAPHIC
B11 CARD

→ Fix: convert B06 to COMPOSITE to break the GRAPHIC run at 2.

Corrected rhythm:
B01 CARD
B02 STILL·ai
B03 CARD
B04 GRAPHIC
B05 GRAPHIC       (2 consecutive — OK)
B06 COMPOSITE     (breaks run)
B07 GRAPHIC
B08 GRAPHIC       (2 consecutive — OK)
B09 CARD          (break)
B10 GRAPHIC
B11 CARD

✓ No run exceeds 2 consecutive same type.
```

**Note:** beat_sheet.json updated: B06 changed to COMPOSITE (drain 2 still rendered as own-Manim scene).

## Act Map

| Beat | Act | Shot Type |
|------|-----|-----------|
| B01 | COLD OPEN | CARD |
| B02 | COLD OPEN | STILL·ai |
| B03 | THE QUESTION | CARD |
| B04 | THE PROBLEM | GRAPHIC |
| B05 | THE MECHANISM | GRAPHIC |
| B06 | THE MECHANISM | COMPOSITE |
| B07 | THE MECHANISM | GRAPHIC |
| B08 | THE IMPLICATION | GRAPHIC |
| B09 | THE IMPLICATION | CARD |
| B10 | THE EXAMPLE | GRAPHIC |
| B11 | RECAP | CARD |

## Color Law

- **TEAL (#1F6F5C):** dose that survives / reaches the tumor; the shrinking remainder bar
- **CRIMSON (#BF3339):** each loss step; lost fraction; the loss chip labels
- **GOLD (#F5D061):** the 0.7% number specifically; the targeting bracket annotation — one use max per graphic, fill only, never text
- **INK (#2F2A26):** all body text, narration cards
- **SLATE (#3E5559):** structural cards (question card, quote card background)
- Colors never swap mid-film. TEAL = good/arriving; CRIMSON = bad/lost. Stated in metadata.

## Exclusions Confirmed

- DLS / TEM characterization tools: NOT MENTIONED — confirmed absent from all beats
- Polydispersity: NOT MENTIONED — confirmed absent
- Two-liposomes case (Lab A / Lab B): NOT MENTIONED — confirmed absent
- EPR mechanism detail (leaky vessel physics, lymphatic drain explanation): NOT MENTIONED — the vessel gap is the step (extravasation) but the EPR mechanism itself is not explained
- The "is 0.7% the right metric" debate: NOT MENTIONED — the number is stated as the chapter's finding and used as the hook; the debate in chapter sections "Still open" is not referenced

---

## STILL Slot — B02

**Beat:** B02
**Act:** COLD OPEN
**Shot:** STILL · ai · kenburns (slow push-in)

**Purpose:** Establish the material reality of the injection — a researcher's bench, a vial, a syringe — before the abstract funnel. The only ai still in this ~118s reel (1 per 90s budget; 118s allows ~1).

**Public-archive search:**
- Wikimedia Commons: search "nanoparticle laboratory vial syringe" — likely PD lab photos from NIH, NCI, or Flickr open license
- NCI Visuals Online: https://visualsonline.cancer.gov/ — search "nanoparticle" or "injection vial" for PD government works
- NIH image gallery: https://www.nih.gov/news-events/images — search "nanoparticle drug delivery"
- Provenance note: any NCI/NIH PD image is preferred; AI generation is fallback

**Generative prompt:**

```
B02, single glass vial of clear nanoparticle solution and one syringe resting on a white laboratory bench surface, horizontal composition, two objects only, flat soft overhead light, no harsh shadows, macro-level detail on the vial cap and syringe plunger, no people visible, no text visible, desaturated documentary-style photograph reproduced as an editorial clipping pinned to aged newsprint ground, newsprint texture visible at edges, flat print reproduction aesthetic, no gradients or glows, photorealistic laboratory still life
```

**Prompt law check:**
- Object named: glass vial of nanoparticle solution + syringe ✓
- Count: two objects (one vial, one syringe) ✓
- Geometry: horizontal, flat overhead ✓
- Distribution: bench surface ✓
- Material: glass vial, newsprint backing ✓
- Camera angle: flat overhead / macro ✓
- Light source: soft overhead, no harsh shadows ✓
- Exclusions: no people, no text on labels ✓

---

## Own-Manim Slots (no fill needed)

| Beat | Scene Class | Visual |
|------|-------------|--------|
| B01 | B01_Title | Title card — "CANCER NANOMEDICINE" eyebrow, main title, CRIMSON underline |
| B03 | B03_Question | Question card with gap formula on screen |
| B04 | B04_FiveSteps | Five-step chain — TEAL dose → 5 CRIMSON step nodes |
| B05 | B05_Drain1 | Funnel drain 1 — circulation loss, bar shrinks |
| B06 | B06_Drain2 | Funnel drain 2 (COMPOSITE) — extravasation loss |
| B07 | B07_Drain345 | Funnel drain 3-4-5 — resolves to 0.7% GOLD sliver |
| B08 | B08_TargetingFix | Targeting annotation — gold bracket on step 4, crimson on steps 1-3 |
| B09 | B09_Quote | Quote card from chapter |
| B10 | B10_Example | Two-column 100-unit example with MONO numbers |
| B11 | B11_Endcard | Endcard — question answered, CANCER NANOMEDICINE topic chip |
