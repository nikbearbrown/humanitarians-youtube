# CHECKS-REPORT — verifying-private-ai-valuations

PROOF GATE, written **before** the first slate compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
10 beats:  6 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the ask and lands three answer lines — motion is the type-on and the result reveal. The interface IS the subject (COLD OPEN LAW), so it is not a punt. |
| B01 | SHOW | Names no visual in narration but makes a structural claim ("no ticker, no earnings call, no public price"). Enacted: three chips land per spoken name, three absences strike through on the word. |
| B02 | SHOW | Claim: value ÷ shares = price. The two tags lift out of the filing card and perform the division; the quotient resolves on "price per share". |
| B03 | SHOW | Claim: six managers, one price, then a repricing. Dots land per spoken manager; the line thickens on "identical, to the cent"; the dashed jump draws on "a new round repriced it". |
| B04 | SHOW | Claim: 5 of 6 dropped silently. The filter bar sweeps, five rows desaturate and slide, and the error console renders zero — the silence is the visual. |
| B05 | SHOW | Claim: 606,028 not ~3,000, then a ~600x reduction. The counter races to the figure on the spoken number; the two pipeline stages physically swap. |
| B06 | SHOW | Claim: 15/15, frozen at six, Cohere removed. Counter ticks, bars grow in rank order, SpaceX pulses, the Cohere callout resolves last. |
| B07 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B08 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B09 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 10)
- ~15–35% negative space ✓ — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is the dropped
  manager rows at 0.48 and the below-floor strip at 0.72
- Comparisons shown side-by-side, held ≥2s ✓ — B05's planned/actual bars and B04's kept/dropped
  split both persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B02 — the mechanism (value ÷ shares) before any evidence
WORKED EXAMPLE ✓ B03 — 19 positions, 6 named managers, arithmetic done by hand
FALSIFIABILITY ✓ B04/B05 — the author's own plan wrong twice, with causes;
                 B06 — Cohere REMOVED because the match was wrong
SCAFFOLDED TASK ✓ B08 — run the same division on one position you choose,
                 then state what would make it wrong
BOOKENDS ✓       B00 cold open · B01 BLUF · B07 verdict · B08 handoff · B09 outro
NO-SOURCE-NO-VERDICT ✓ every figure traces to a FACTCHECK.md row (all 20 CONFIRMED);
                 B02 shows tag names rather than invent a numerator/denominator
```

**0 violations.** Nothing was silently passed; the one judgment call (compressing the four
below-floor companies in B06 to a single muted strip, since the narration never names them and
one-idea-per-beat holds) is logged in `BUILD-LOG.md`.
