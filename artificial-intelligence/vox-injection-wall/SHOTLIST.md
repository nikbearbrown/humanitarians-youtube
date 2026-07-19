# SHOTLIST — vox-injection-wall

**Title:** Why Prompt Injection Can't Be Patched
**Total beats:** 13 | **Est. duration:** ~2:45 | **Slug:** vox-injection-wall

---

## Rhythm check

13 beats | ~165s ≈ 2:45 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · DOCUMENT · GRAPHIC · DOCUMENT · GRAPHIC · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow; B01_Title |
| B02 | COLD OPEN | GRAPHIC | own | morph | Agent reads doc; injected line executes |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | compare | Contingent bug vs. structural feature |
| B05 | THE PROBLEM | GRAPHIC | own | trace | Token equality: user instruction = injected = same |
| B06 | THE MECHANISM | STILL | ai | kenburns | Text on screen with hidden instructions highlighted |
| B07 | THE MECHANISM | GRAPHIC | own | trace | Patch fails: auth, filtering, sanitization — structural cause unchanged |
| B08 | THE MECHANISM | DOCUMENT | own | highlight | Quote: "structural feature … not a fixable bug" |
| B09 | THE IMPLICATION | GRAPHIC | own | compare | What you CAN do: monitor, gate, constrain |
| B10 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "raises the cost of exploitation without closing it" |
| B11 | THE IMPLICATION | GRAPHIC | own | trace | Fundamental vs. contingent taxonomy |
| B12 | THE EXAMPLE | GRAPHIC | own | accumulate | Support ticket AI: injected line closes 47 tickets; no filter flags it |
| B13 | RECAP | CARD | own | endcard | "Instructions and data are identical tokens." |

---

## Color semantics
- TEAL = legitimate instructions / trusted commands
- CRIMSON = injected instructions / adversarial content
- GOLD = the single token stream / the architectural limit
- SLATE = document content / external data
- Never swapped mid-film ✓

## STILL economy
~165s → 1–2 stills allowed (1 per 90s); used: 1 (B06, THE MECHANISM entry) ✓

## Exclusions honored
- No jailbreak string examples ✓
- No constitution-attack case detail ✓
- No defense-in-depth survey ✓
- No instruction-hierarchy research tangent ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS text on a screen with some lines visibly highlighted in red, suggesting hidden instructions embedded in document content.
Wrong = abstract network diagram, any image without visible text and highlighted lines.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=code+text+screen+red+highlight&title=Special:MediaSearch&type=image
Drop the result in `pantry/` as `B06-<anything>.jpg`.
