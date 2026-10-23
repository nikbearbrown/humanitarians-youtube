# CHECKS-REPORT — bulk-ingestion-at-scale

PROOF GATE, written **before** the first slate compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
11 beats:  7 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the ask and lands three answer lines — motion is the type-on and the result reveal. The interface IS the subject (COLD OPEN LAW). |
| B01 | SHOW | Claim: scale changes what is visible. Enacted — the two cards are different SIZES and the 80,571,213 counter races up, so the size gap makes the argument before the words finish. |
| B02 | SHOW | Claim: 80.5M → 22M → 5,806, every stage reconciling. Each bar draws and each counter races on its spoken clause; the third bar visibly COLLAPSES (log-scaled from a 1,000-row floor, which is what keeps that collapse readable). |
| B03 | SHOW | Claim: 33 period ends, and the shape is a staircase. The step path draws left to right across the beat from the real 33 medians; the flats hold and the risers snap, so "flat for months, then a jump" is enacted. |
| B04 | SHOW | Claim: 7 independent managers, one price, and 24 registrations are not 24 managers. Seven plates land per named manager, connectors converge on $259.14, and 24 ticks visibly GROUP into 7. |
| B05 | SHOW | Claim: the archive is keyed to filing date and runs ~56 days late. The mechanism performs itself — two dated chips, a brace measuring the gap, then the archive band drawing only as far as 30 Apr while the $589 mark sits outside the boundary. |
| B06 | SHOW | Claim: one manager counted as five. Five cards stand apart, then slide together into one; the counter strikes 5 and resolves to 1. |
| B07 | SHOW | Claim: two prices exactly 10x apart inside one filing. Six real rows land, the EC prices set in ink, the EP prices set terracotta on the spoken contrast, and a brace joins the two bands with "× 10". |
| B08 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B09 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B10 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 11)
- ~15–35% negative space ✓ — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is the collapsed
  Fidelity cards, which fade only as they merge into the card that replaces them
- Comparisons shown side-by-side, held ≥2s ✓ — B01's two cards, B07's two price bands and
  B06's 5 → 1 counter all persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B02 — the funnel (what the data IS) before any conclusion drawn from it
WORKED EXAMPLE ✓ B03/B04 — one company's full price history, then the seven-manager check on
                 a single step of it
FALSIFIABILITY ✓ B05 — the author's own week-1 result cannot be reproduced from this data, and
                 the beat explains why rather than explaining it away;
                 B06/B07 — two defects caught, one in the code, one in the filed data
SCAFFOLDED TASK ✓ B09 — pull two filings, measure the gap between period-end and acceptance,
                 then reason about what the gap invalidates
BOOKENDS ✓       B00 cold open · B01 BLUF · B08 verdict · B09 handoff · B10 outro
NO-SOURCE-NO-VERDICT ✓ every figure is a prop traced to a FACTCHECK.md row; the 33-point series
                 is injected programmatically from figdata_week2.json rather than transcribed
```

**0 violations.** Two authoring judgment calls are logged in `BUILD-LOG.md` rather than passed
silently: splitting the script's two combined shots into four beats, and rebuilding B05 as a
mechanism beat instead of an annotation on the staircase.
