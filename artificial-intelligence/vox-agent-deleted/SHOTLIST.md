# SHOTLIST — vox-agent-deleted

## Rhythm check
13 beats | estimated ~168s ≈ 2:48 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · GRAPHIC · DOCUMENT · GRAPHIC · DOCUMENT · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow; title in DISPLAY |
| B02 | COLD OPEN | GRAPHIC | own | trace | Ash case: ASH AGENT → REPORT → SERVER: EMAIL EXISTS |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | compare | Two worlds: agent's local client vs. user's mail server |
| B05 | THE PROBLEM | GRAPHIC | own | trace | Four-step trace: no tool → reset → approved → gap |
| B06 | THE MECHANISM | STILL | ai | kenburns | Slate — person at laptop, green checkmark, puzzled (see PROMPTS.md) |
| B07 | THE MECHANISM | GRAPHIC | own | compare | Agent's 'DELETE' vs User's 'DELETE' — two operations, no flag |
| B08 | THE MECHANISM | GRAPHIC | own | trace | False-success trace: COMPLETED → REPORT → gap → SERVER UNCHANGED |
| B09 | THE MECHANISM | DOCUMENT | own | highlight | Quote: "a false success report that nothing caught" |
| B10 | THE IMPLICATION | GRAPHIC | own | compare | Trust the report (wrong) vs. Check world state (right) |
| B11 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "agent had no model of either its own scope…" |
| B12 | THE EXAMPLE | GRAPHIC | own | compare | Scheduling case: your calendar vs. three attendees' calendars |
| B13 | RECAP | CARD | own | endcard | "The agent wasn't lying. It reported what happened in its world." |

## Color semantics
- TEAL = agent's world / local state / what the agent sees
- CRIMSON = user's world / server state / the gap
- GOLD = the word DELETED / the completion report / key insight
- SLATE = infrastructure / structural elements
- Never swapped mid-film ✓

## STILL economy
~168s → 1–2 stills allowed (1 per 90s); used: 1 (B06, THE MECHANISM entry) ✓

## Exclusions honored
- No SHAP/LIME material ✓
- No Wittgenstein biography ✓
- No provider-side technical detail (only "Proton Mail server" spoken once in B04) ✓
- No radiologist second example ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS the contradiction: green success indicator visible on screen while
the actual state (second monitor / other view) shows the task is unfinished.
Wrong = a smiling person, a generic laptop photo, no visible contradiction.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=person+laptop+confused+checking&title=Special:MediaSearch&type=image
- https://www.flickr.com/search/?text=person+computer+confused
Drop the result in `pantry/` as `B06-<anything>.jpg`; set `shot.focus` on the
contradiction (the two screens) after intake.
