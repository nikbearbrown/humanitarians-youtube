# CHECKS-REPORT — Three Ways To Be Wrong.

Written before Gate D1 (the previz compile), per PROOF GATE.

28 SHOW / 0 justified-HOLD / 0 PUNT-flagged (body beats) + 4 bookend SHOW
(B00, BVDT, BHTF, BOUT — all animate real events, none are bare cards)

Lane histogram (body, 28 beats): CARD 3 (10.7%) · VOX 8 (28.6%) · MANIM 8
(28.6%) · REMOTION 9 (32.1%). All four lanes land inside their lint bands
(vox 15–30% / manim 25–40% / remotion 30–45% per SKILL.md THE BEAT-MIX
CONTRACT) — no WARN, no FAIL.

## Per-lane claim/subject check

- **CARD (B05, B16, B25)** — pure act-opening segment cards, no factual
  claim to gate; correctly classified CARD, not a PUNT.
- **VOX (B02/B03, B06/B07, B11, B17, B21, B27)** — every still names its
  subject in `shot.show` and is a metaphor for a stated claim (established
  in SOURCES.md), not a claim-carrying beat itself — narration in these
  beats carries the actual claim, the still illustrates it. No PUNT: each
  still's role is illustrative connective tissue between claim-bearing
  beats, exactly as the genre's vox lane is designed to work.
- **MANIM (B08, B10, B12, B13, B18, B19, B22, B28)** — every scene names
  its mechanic in `graphic.production_viz.mechanic` and is a justified SHOW
  (a real animated diagram of the claim, not a text card); B10/B19/B20
  additionally carry an explicit "no invented numbers" note, verified
  against FACTCHECK.md.
- **REMOTION (B01, B04, B09, B14, B15, B20, B23, B24, B26)** — 7 of 9 reuse
  already-registered, already-QC'd patterns from the sibling ai-explainer
  build (props-only reuse, per ILLUSTRATIONS.md's starter-template
  contract); B04 and the three CARD-lane `DeepActCard` beats are the only
  genuinely new components this reel introduces.

## Continuity check (vox-run contract)

R1 (B02→B03) and R2 (B06→B07): both length 2 (≤ max 3), neither crosses an
act boundary, both openers (B02, B06) carry a `handoff` block the closer's
first frame will reproduce. No run chains across more than 2 consecutive
vox beats; no run spans an act boundary. Compliant with SKILL.md
CONTINUITY.

Teaching arc:
FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓

No violations to log. Full rationale in PEDAGOGY.md. GATE P is PENDING —
this report covers beat authoring only; no audio, Manim render, or compile
exists yet.
