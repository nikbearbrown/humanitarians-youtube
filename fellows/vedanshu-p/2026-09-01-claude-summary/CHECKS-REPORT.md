# CHECKS-REPORT — claude-rag-the-right-text

Written before the first compile, per ai-explainer PROOF GATE.

## Beat classification

8 SHOW / 1 CARD (outro, exempt) / 0 justified-HOLD / 0 PUNT-flagged

| Beat | Class | On-screen artifact |
|---|---|---|
| B00 | SHOW | composer types the ask; four result lines print (one per chapter + the through-line) |
| B01 | SHOW | the overview is written, `more` reconsidered in terracotta, deleted, `the right` typed in |
| B02 | SHOW | two cards + terracotta arrow: frozen snapshot → retrieved passage |
| B03 | SHOW | real transcript prints; the RETRIEVED line is visibly the vacation paragraph; verdict lands |
| B04 | SHOW | plot card; two terracotta phrasings joined by a connector, two ink phrasings far apart |
| B05 | SHOW | two vectors draw from the origin; the arc between them appears |
| BVDT | SHOW | artifact page; five verdict lines print in narration order |
| BHTF | SHOW | the viewer's prompt types itself in full |
| BOUT | CARD | title restate — the outro, exempt by OUTRO LAW |

No beat is a bare CARD carrying a factual claim. No two consecutive body beats
share a visual scheme (cards → transcript → scatter → vector diagram), so the
PPT TEST and the slideshow smell are both clear.

## Teaching arc

| Item | Status | Where |
|---|---|---|
| FRAMEWORK before examples | ✓ | B01 states the whole claim in one breath before any specific |
| WORKED EXAMPLE | ✓ | B03 is a real run of the failing scan, with its actual output |
| FALSIFIABILITY | ✓ | B03 shows the *obvious fix failing*; B04 gives the counterexample (four shared words, far apart) |
| SCAFFOLDED TASK | ✓ | BHTF asks the viewer to rank three passages both ways and locate the disagreement |
| BOOKENDS | ✓ | cold open (B00) · BLUF (B01) · verdict (BVDT) · handoff (BHTF) · title outro (BOUT) |
| NO-SOURCE-NO-VERDICT | ✓ | every number and figure is carried from the three source beat sheets — see SOURCES.md |

## ILLUSTRATE LAW

The Claude UI appears in exactly five beats, all of them sanctioned: the cold
open, the verdict artifact, the handoff, and the outro card. B02–B05 illustrate
their concepts instead. Zero composer wallpaper.

## Typing rule

Typing appears in exactly three beats, each for a different reason:
B00 (the *ask*), B01 (the *overview being thought through*), BHTF (the
*viewer's prompt*). No inner beat types.

## Notes / deviations

- **`lead_silence_s: 0.8` is written on B01 but is inert** — nothing in
  `runtime/scripts/` reads that key. Its intent (a window long enough for the
  correction to land) is met by narration length instead: B01's measured audio
  is **10.35s**, over the doctrine's 9s floor.
- **B01's trigger is one word, not a phrase.** `BrutalistHesitantWriter`
  matches triggers per whitespace token, so a multi-word trigger can never
  fire. The misconception is carried by `more` → `the right`, which corrects
  the whole sentence ("Retrieval means giving the model **the right** text.")
  rather than repairing one noun and leaving the framing wrong.
