# SHOTLIST — prompt-is-a-wish-spec-is-a-contract

**Why "Write Me a Login Function" Is Not a Prompt**
Source: `claude-code-for-students/chapters/04-conducting-not-prompting.md`
Topic kicker: CLAUDE CODE

---

## Histogram & Rhythm Check

| Beat | Type | Source | Motion | Act |
|------|------|--------|--------|-----|
| B01 | CARD | own | hold | COLD OPEN |
| B02 | CARD | own | hold | THE QUESTION |
| B03 | GRAPHIC | own | drawon | THE PROBLEM |
| B04 | CARD | own | hold | THE PROBLEM |
| B05 | GRAPHIC | own | drawon | THE MECHANISM |
| B06 | GRAPHIC | own | drawon | THE MECHANISM |
| B07 | STILL | ai | kenburns | THE MECHANISM |
| B08 | GRAPHIC | own | drawon | THE EXAMPLE |
| B09 | CARD | own | hold | THE MECHANISM (kicker) |
| B10 | GRAPHIC | own | drawon | THE PRACTICE |
| B11 | CARD | own | hold | THE IMPLICATION |
| B12 | CARD | own | hold | RECAP / ENDCARD |

**Type histogram:** CARD x 6, GRAPHIC x 4, STILL x 1. No >2 consecutive same-type (B05→B06→B07 breaks from GRAPHIC to STILL). Rhythm: clean.

**Act map:**
- COLD OPEN: B01 (Seth's one-sentence prompt → broken function)
- THE QUESTION: B02 (request was clear — why was output broken?)
- THE PROBLEM: B03–B04 (prompt-as-wish mechanism; training distribution fills blanks)
- THE MECHANISM: B05–B07 (specification-as-contract; six sentences; Claude's clarifying question)
- THE EXAMPLE: B08 (Tomas: prompt vs spec comparison)
- THE MECHANISM KICKER: B09 (the decision is the work)
- THE PRACTICE: B10 (four steps: decide, read, name boundary, write handoff condition)
- THE IMPLICATION: B11 (time vs quality: boondoggle vs something to put your name on)
- RECAP: B12 (prompt is a wish; spec is a contract)

**Color law:** CRIMSON = prompt / boondoggle / vague wish. INK = specification / contract / verified output. Single accent. Never swap.

**Exclusions confirmed:** no OAuth flows, no security audit methodology, no prompt engineering tricks, no password hash history.

**Estimated duration:** ~150s = 2:30.

---

## Open Slot: B07 (STILL · ai)

### B07 — Claude asks a clarifying question

**Beat:** B07 — developer pausing when Claude asks a question they hadn't thought to ask.

**Generative prompt:**
```
B07, a developer at a desk reading a chat interface on their laptop screen, one question visible from the AI assistant, the developer pausing with pen in hand — thoughtful expression, editorial flat desaturated treatment, warm desk lamp, centered composition, no readable text on screen
```

---

## Non-fill beats (own Manim scenes)

B01, B02, B03, B04, B05, B06, B08, B09, B10, B11, B12 — rendered by vox_scenes.py.
