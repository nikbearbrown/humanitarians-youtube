# FRICTIONAL - Your Foundation Search Is Doing Market Research (AI explainer)

**Built and delivered 2026-11-11.** Written from the build record in this folder (CHECKS-REPORT.md, FACTCHECK.md, beat_sheet.json) and the build session. Append your own entries below; do not rewrite earlier ones.

## What was tried and expected

- Asked for a "Deep Explainer" at exactly 4:00 with no footage, from the article "Your Foundation Search Is Doing Market Research" (Arbelle and PwC Malaysia as sources), opening with "Hi, I'm Agrima", warm and simple, with company-reported numbers and illustrations clearly labeled. The toolkit's deep-explainer skill targets 5-10 minutes and needs archival stills, so neither the length nor the no-footage condition could be met by it.
- Built on the ai-explainer chassis instead and said so in beat_sheet.json (metadata.note) and CHECKS-REPORT.md.

## Where it resisted, and what was done next

- **Length:** the first narration pass measured 262 s. It took five rounds of trimming connective phrases and lead-ins (no figure, source, hedge or label removed) to reach 239.9 s. Each round meant regenerating all 13 audio files, because the sentence-level rewrites moved the timing less than the word counts suggested.
- **Reveal timing bug:** the first full render had cards whose contents appeared all at once instead of on the narration (B02, B03, B07). It was found only by sampling frames from the finished video, not by any gate. Fixed by hiding each row until its sentence, then re-rendering those three clips.
- **Edge overflow:** the frame check flagged two blocking edge-bleed defects in B03 (the PwC card ran past the right title-safe edge). The scene gates had passed it. Card moved and narrowed, B03 re-rendered; the re-run had no blockers.
- **Two overlaps caught by the layout gates:** B01 (the "new text" bubble over the phone's face) and B06 (a source chip over a label).
- **Pipeline stall and a misleading file:** the render script stopped once after the scene clips and needed a re-run; the final mp4 also showed up as a 48-byte file while it was still being written, so I waited for the file size to stop changing before trusting it.
- **9:16 cut:** the toolkit's automatic plan wanted to drop the host intro and the handoff to fit the 3:00 cap. I rejected that and chose the beats to drop by hand: B02 (the quiet conversation), B03 (from a tap to a product) and B06 (back to the shelf), keeping the intro, the privacy beat, the sources note and the handoff. A static check in the portrait B07 flagged text overlapping text because a faded-out label was still in the scene; fixed by removing it and moving a heading.

## What Claude contributed, and what Agrima decided

- Claude: the beat sheet, narration trims, all ten scenes in 16:9 and seven in 9:16, the gates, the paperwork and the fixes above.
- Agrima: the article, the tone, the labels (illustration, company-reported, example), the no-logos and no-real-faces rule, and the revision prompt for later changes. Accepted as written; nothing was rejected.

## What is understood, and what is still open

- The cosnova numbers are company-reported by Arbelle; the video says so on screen and in narration, and the sources card repeats it. They were not independently checked.
- The 9:16 does not cover three beats of the article (what Arbelle says brands can see, the three decisions the data guides, and the shelf trimming). It points to the full video on its end card.
- The frame check still lists "content fills too little of the screen" notes on a few frames; they are accepted.
- Pushed to GitHub with this log.

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
