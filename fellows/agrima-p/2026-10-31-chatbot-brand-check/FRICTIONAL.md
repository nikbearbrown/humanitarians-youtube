# FRICTIONAL - Have You Asked the Chatbot About Your Brand Lately? (AI explainer)

**Built and delivered 2026-10-31.** Written from the build record in this folder (CHECKS-REPORT.md, FACTCHECK.md, beat_sheet.json). Append your own entries below; do not rewrite earlier ones.

## What was tried and expected

- Asked for a "Deep Explainer" at exactly 4:00 with no footage. The toolkit's deep-explainer skill targets 5-10 minutes and needs ~20-25% archival stills, so neither the length nor the no-footage condition could be met by it.
- From the weekly Substack article. Warm, simple, friendly, positive but fair.

## Where it resisted, and what was done next

- Built on the ai-explainer chassis instead, and said so in beat_sheet.json (metadata.note) and CHECKS-REPORT.md rather than substituting silently.
- Three bugs fixed before rendering: a NameError in B08, the B08 question chips running past the safe area, and a '$' label sitting on a line in B05.
- First narration pass was 255 s. It was trimmed to 239.3 s to land on 4:00; rounded numbers are spoken (1,704 / 32,556 / 3,848) while exact figures stay on screen.
- Every figure kept, spread over six stat scenes, each labeled with its source and the set labeled industry-reported, because most sources sell marketing, PR or brand-monitoring services.
- While preparing the weekly recap's 9:16 version, a setup script pointed at this reel's short folder and overwrote its END card, beat sheet and paperwork. The originals were restored by re-running this reel's own prep script; the delivered video was never touched.
- The 9:16 (2:54) FACTCHECK says it keeps 9 of 11 content beats and drops three, which does not add up.

## What Claude contributed, and what Agrima decided

- Claude: build, the overwrite and its repair. Agrima: topic, tone, the number allowance.

## What is understood, and what is still open

- Reconcile the beats-dropped count in the 9:16 FACTCHECK.
- Pushed to GitHub (agrima-p/all-reels, commit fd11dbfe) and merged into main.

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
