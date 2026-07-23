# SHOTLIST — vox-channel-reset

## Rhythm check
13 beats | estimated ~210s ≈ 3:30 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · DOCUMENT · GRAPHIC · DOCUMENT · GRAPHIC · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow |
| B02 | COLD OPEN | GRAPHIC | own | compare | Discord: caught in ch1, trusted in ch2 |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | compare | Suspicion lives in session context only |
| B05 | THE PROBLEM | GRAPHIC | own | compare | Displayed vs verified identity |
| B06 | THE MECHANISM | STILL | ai | kenburns | Slate — two chat panels: flagged left, trusted right (see PROMPTS.md) |
| B07 | THE MECHANISM | GRAPHIC | own | trace | Two channels: ID discrepancy visible ch1, invisible ch2 |
| B08 | THE MECHANISM | DOCUMENT | own | highlight | Quote: "trust context does not transfer…effectively reset" |
| B09 | THE IMPLICATION | GRAPHIC | own | compare | Identity in infrastructure vs session context |
| B10 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "displayed identity…primary authority signal" |
| B11 | THE IMPLICATION | GRAPHIC | own | trace | Validate across channel boundaries |
| B12 | THE EXAMPLE | GRAPHIC | own | compare | Support tickets #47 (flagged) → #48 (fresh session, export runs) |
| B13 | RECAP | CARD | own | endcard | "Suspicion in session context. Fresh channel resets everything." |

## Color semantics
- TEAL = verified owner / legitimate identity / caught correctly
- CRIMSON = impersonator / spoofed identity / the attack succeeds
- GOLD = the architectural insight / trust doesn't transfer
- SLATE = session context / prior interaction history
- Never swapped mid-film ✓

## STILL economy
~210s → 1–2 stills allowed (1 per 90s); used: 1 (B06, THE MECHANISM entry) ✓

## Exclusions honored
- No cryptographic-credential redesign ✓
- No post-compromise file-wiping aftermath ✓
- No generalization to prompt injection ✓
- No failure taxonomy ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS two chat interface panels — flagged on left, fresh and trusted on right.
Wrong = single chat window, generic messaging app without the split panel contrast.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=chat+interface+split+panel&title=Special:MediaSearch&type=image
Drop the result in `pantry/` as `B06-<anything>.jpg`; set `shot.focus` toward
the contrast between the two panels after intake.
