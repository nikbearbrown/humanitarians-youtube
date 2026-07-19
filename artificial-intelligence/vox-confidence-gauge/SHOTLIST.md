# SHOTLIST — vox-confidence-gauge

## Rhythm check
13 beats | estimated ~105s ≈ 1:45 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · GRAPHIC · DOCUMENT · GRAPHIC · DOCUMENT · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow |
| B02 | COLD OPEN | GRAPHIC | own | trace | Ash report: clean prose, accepted without verification |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | compare | Old heuristic: clear writing = clear thinking (now broken) |
| B05 | THE PROBLEM | GRAPHIC | own | transform | Form and content generated independently |
| B06 | THE MECHANISM | STILL | ai | kenburns | Slate — person reading clean AI response, nodding (see PROMPTS.md) |
| B07 | THE MECHANISM | GRAPHIC | own | trace | First pump: fluency raises confidence in output |
| B08 | THE MECHANISM | GRAPHIC | own | transform | Second pump: confidence in output raises confidence in own evaluation |
| B09 | THE MECHANISM | DOCUMENT | own | highlight | Quote: "fluency is an evaluation booster" |
| B10 | THE IMPLICATION | GRAPHIC | own | trace | Popperian fix: pre-specify what wrong looks like |
| B11 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "specify what a wrong answer would look like — not vaguely — specifically" |
| B12 | THE EXAMPLE | GRAPHIC | own | compare | Developer: AI diagnoses wrong bug, fluently — committed and test still fails |
| B13 | RECAP | CARD | own | endcard | "Fluency is form. Form is not content." |

## Color semantics
- TEAL = pre-specified anchor / reliable heuristic / the Popperian fix
- CRIMSON = false confidence pumped by fluency / the broken heuristic / wrong evaluation
- GOLD = the key insight
- Never swapped mid-film ✓

## STILL economy
~105s → 1–2 stills allowed (1 per 90s); used: 1 (B06, THE MECHANISM entry) ✓

## Exclusions honored
- No Botspeak framework or pillar vocabulary ✓
- No LLM architecture explanation ✓
- No prompt-engineering tips ✓
- No Ash case retelling beyond one beat (B02 only) ✓
- One reader, one sentence ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS a person reading a clean AI response and finding it convincing.
Wrong = empty desk, phone, any image without a readable screen and a person reacting.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=person+reading+laptop+nodding&title=Special:MediaSearch&type=image
Drop the result in `pantry/` as `B06-<anything>.jpg`; set `shot.focus` toward
the person's face and the laptop screen after intake.
