# SHOTLIST — vox-error-cascade

## Rhythm check
13 beats | estimated ~165s ≈ 2:45 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · DOCUMENT · GRAPHIC · DOCUMENT · GRAPHIC · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow |
| B02 | COLD OPEN | GRAPHIC | own | accumulate | Three agents cleared; pipeline ships at 30% wrong |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | compare | Isolation vs pipeline: clean inputs never arrive |
| B05 | THE PROBLEM | GRAPHIC | own | accumulate | Each agent treats prior output as ground truth |
| B06 | THE MECHANISM | STILL | ai | kenburns | Slate — chain of links, rust spreading (see PROMPTS.md) |
| B07 | THE MECHANISM | GRAPHIC | own | accumulate | Cascade trace: 1% × 1% × 1% ≠ 3% |
| B08 | THE MECHANISM | DOCUMENT | own | highlight | Quote: "validated each at 1%; compound fails at 30%" |
| B09 | THE IMPLICATION | GRAPHIC | own | compare | What to validate: interaction patterns, handoff gates |
| B10 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "validate interaction patterns — not just individual agents" |
| B11 | THE IMPLICATION | GRAPHIC | own | trace | Necessary vs sufficient: individual + system validation |
| B12 | THE EXAMPLE | GRAPHIC | own | accumulate | Customer service: 3 cleared agents → wrong order delivered confidently |
| B13 | RECAP | CARD | own | endcard | "Error doesn't add. It cascades." |

## Color semantics
- TEAL = correct/valid output / individual agent passing
- CRIMSON = error / wrong output / compounded failure
- GOLD = the key insight / cascading dynamic
- SLATE = pipeline structure / agent boxes
- Never swapped mid-film ✓

## STILL economy
~165s → 1–2 stills allowed (1 per 90s); used: 1 (B06, THE MECHANISM entry) ✓

## Exclusions honored
- No authority-laundering variant ✓
- No resource-exhaustion cases ✓
- No identity-confusion case ✓
- No compound-probability derivation beyond one multiplication ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS a chain of mechanical links with damage spreading link-to-link.
Wrong = abstract network diagram, any image without the visual chain and spreading damage.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=chain+links+rust+damage&title=Special:MediaSearch&type=image
Drop the result in `pantry/` as `B06-<anything>.jpg`; set `shot.focus` toward
the damaged/rusted links after intake.
