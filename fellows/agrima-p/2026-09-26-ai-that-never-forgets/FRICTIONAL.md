# FRICTIONAL - The AI That Never Forgets: How Marketing Is Learning to Read Your Mind (AI explainer)

**Built and delivered 2026-09-26.** Written from the build record in this folder (CHECKS-REPORT.md, FACTCHECK.md, beat_sheet.json). Append your own entries below; do not rewrite earlier ones.

## What was tried and expected

- Asked for a "Deep Explainer" at exactly 4:00 with no footage. The toolkit's deep-explainer skill targets 5-10 minutes and needs ~20-25% archival stills, so neither the length nor the no-footage condition could be met by it.
- A neutral, balanced, observational tone: a fair explainer, not a warning.

## Where it resisted, and what was done next

- Built on the ai-explainer chassis instead, and said so in beat_sheet.json (metadata.note) and CHECKS-REPORT.md rather than substituting silently.
- Two layout checks hard-blocked the first run: B03's cards were plain text so the checker saw no shape change (fixed with a small accent dot on each card), and B05 revealed three buttons in one animation so only one state was recorded (fixed by revealing them one at a time, which also paced better).
- A real bug the gates missed: B05's "Memory" panel title collided with its own border. It was found only by looking at a rendered frame and fixed by sizing the panel from its content.
- B03's stat line sat just outside the bottom safe area and was moved up.
- Estimated 3:52 against the 4:00 target; real length 3:49. The 9:16 auto-dropped the two densest beats and the outro and end card were rewritten by hand.

## What Claude contributed, and what Agrima decided

- Claude: build, fixes, frame review. Agrima: topic, neutral register. Two industry-blog stats are narrated as 'one analysis found', not as settled fact.

## What is understood, and what is still open

- The video is 11 seconds short of an exact 4:00.

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
