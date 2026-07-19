# SHOTLIST — vox-bias-pipe

## Rhythm check
13 beats | estimated ~108s ≈ 1:48 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · DOCUMENT · GRAPHIC · GRAPHIC · DOCUMENT · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow |
| B02 | COLD OPEN | GRAPHIC | own | trace | Three teams: two barely moved it, one cut tenfold |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | compare | Naive expectation: fix the model, fix the bias |
| B05 | THE PROBLEM | GRAPHIC | own | trace | Three parallel paths from attribute to outcome |
| B06 | THE MECHANISM | STILL | ai | kenburns | Slate — causal diagram on whiteboard (see PROMPTS.md) |
| B07 | THE MECHANISM | GRAPHIC | own | drawon | Pipe graph with three concurrent flow paths |
| B08 | THE MECHANISM | DOCUMENT | own | highlight | Quote: "block one path — leave proxy and context fully open" |
| B09 | THE MECHANISM | GRAPHIC | own | block | Model path blocked — flow reroutes, bias barely moves |
| B10 | THE MECHANISM | GRAPHIC | own | block | Review/context path blocked — disparity falls 90% |
| B11 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "wrong leverage point — disparity will persist" |
| B12 | THE EXAMPLE | GRAPHIC | own | compare | Lending: 22-pt gap, model fix → 7pts, zip code still carries 18 |
| B13 | RECAP | CARD | own | endcard | "The model is never the only pipe." |

## Color semantics
- TEAL = high-leverage intervention / effective block / tenfold reduction
- CRIMSON = bias flow / low-leverage fix / rerouted flow
- GOLD = key insight / section title
- Never swapped mid-film ✓

## STILL economy
~108s → 1 still allowed (1 per 90s); used: 1 (B06, THE MECHANISM entry) ✓

## Exclusions honored
- No Pearl do-calculus notation ✓
- No ten-mechanism taxonomy ✓
- No fairness metrics ✓
- Graph capped at ≤6 nodes (5 nodes: Protected Attr, Model, Proxy, Review, Outcome) ✓
- Three teams one sentence each in B02 ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS the causal diagram on a whiteboard — arrows connecting pipeline stages.
Wrong = generic whiteboard, stock photo meeting room with no visible diagram.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=whiteboard+diagram+causal&title=Special:MediaSearch&type=image
Drop the result in `pantry/` as `B06-<anything>.jpg`; set `shot.focus` toward the
diagram arrows after intake.
