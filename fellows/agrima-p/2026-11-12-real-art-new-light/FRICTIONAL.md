# FRICTIONAL - Real Art, New Light (AI explainer)

**Built and delivered 2026-11-12.** Written from the build record in this folder (CHECKS-REPORT.md, FACTCHECK.md, beat_sheet.json) and the build session. Append your own entries below; do not rewrite earlier ones.

## What was tried and expected

- Asked for a "Deep Explainer" at exactly 4:00 with no footage, from the article "Real Art, New Light": the opening scene, three habits, five museum examples (Rembrandt, Dalí and MoMA in full; Harvard and Koblenz one sentence each), ideas anyone could borrow and a closing idea, about 25 seconds per example, a sources note near the end, and no real artworks, likenesses of real people, or logos. The toolkit's deep-explainer skill targets 5-10 minutes and needs archival stills, so neither the length nor the no-footage condition could be met by it.
- Built on the ai-explainer chassis instead and said so in beat_sheet.json (metadata.note) and CHECKS-REPORT.md.

## Where it resisted, and what was done next

- **Length, the other way round:** unlike earlier videos, the first narration pass came in short, at 234.3 s. I added two accurate details from the article (the Harvard marketing director talking with curators first, and the TRT World article showing no date), which overshot to 241.6 s, then tightened two phrases to reach 239.7 s. Three audio generations in all.
- **Pacing request vs. exact 4:00:** the brief said about 25 seconds per example. The Dalí beat is 27 s but Night Watch is 32 s and MoMA 31 s, because three full examples plus the habits, ideas and closing had to land exactly on 4:00. Disclosed in CHECKS-REPORT.md rather than cutting details you listed.
- **A rule that rewrote my wording:** the pipeline's slide gate rejected the on-screen phrase "a new chapter, not mere documentation" (Koblenz) as chapter wording. I changed the slide to "more than mere documentation"; the narration still says "new chapter" in the museum's words. It cost a full re-run.
- **Preview-frame problems the layout gates did not catch:** B05's colour wall rendered blank because its colour blobs were hidden and never faded in; B01's brushstrokes ran outside their screen; B02's third row ran into its tags. All found by viewing preview stills and fixed before the 4K render.
- **Gate findings fixed:** a closing line below the safe area (B01), the guide icon over a painting (B06), a title past the left edge and a "shapes never change" error (B07, fixed by fading rows in as cards), and a TypeError in my first B02 (rebuilt with explicit positions).
- **Pipeline stalls:** the render script stopped after the scene clips twice and needed re-runs; the composer-beat step then ran in a tracked background job so it could not be cut off.
- **9:16 cut:** the toolkit's automatic plan would have dropped the Rembrandt, Dalí and MoMA examples to fit the 3:00 cap. I rejected that and chose the beats to drop by hand: the cold-open ask (B00), the three habits (B02), Harvard and Koblenz (B06) and the ideas (B07), keeping the opening, all three full examples, the closing, the sources note and the handoff. Two portrait layout flags (a text overlap in B05, a label on a line in B08) were fixed before the render.

## What Claude contributed, and what Agrima decided

- Claude: the beat sheet, narration, ten scenes in 16:9 and seven in 9:16, the gates, the paperwork and the fixes above.
- Agrima: the article, the coverage rule (three examples in full, two in one sentence), the tone, the labels (illustration, wire report, 2019 review, suggestions), and the no-real-artwork, no-likeness, no-logos rule. Accepted as written; nothing was rejected.

## What is understood, and what is still open

- The Rijksmuseum story is from a wire report, the Dalí review is from 2019 and the TRT World article shows no date; the video says so. None of the claims were re-checked against the original sources.
- Night Watch and MoMA run longer than 25 s.
- The 9:16 does not cover the habits, the Harvard and Koblenz mentions or the ideas; its end card points to the full video.
- The frame check still lists "content fills too little of the screen" notes on a few frames; they are accepted.
- Pushed to GitHub with this log (code and paperwork only, no video).

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
