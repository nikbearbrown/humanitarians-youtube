# Frictional notes

## 2026-11-14

The toolkit requires the human voice record for its silent still preflight. Static storyboards provide a visual review at this stage. The benchmark comparisons also needed two different qualifiers. The household chart uses the best of six prompts for both methods, and the shopping chart uses the paper’s success-rate column.

- What was hard: The research tool required a sign-in.
- What I tried: I verified the claims directly against the paper, the authors' project page, the Google Research article, and primary references. I moved unsupported claims to the dropped list.
- Result / still open: The research ledger gives a source and location for each claim in the script.

- What was hard: The paper reports different metrics, averages, and best-of-six results.
- What I tried: I used reported success rates and matched the comparison conditions within each benchmark. I kept the question-answering comparison where reasoning alone scored higher.
- Result / still open: The household figures are labeled best of six, and the shopping figures use the paper's success-rate column.

- What was hard: The voice gate also applies to silent toolkit renders.
- What I tried: I prepared storyboard stills and a claim ledger for review before generating any audio.
- Result / still open: The script, sources, and storyboards passed human review. The voice record needs the actual review time before production can begin.

- What was hard: A layout designed for a wide screen loses readability on a phone.
- What I tried: I laid out the portrait version independently with stacked cards and larger type.
- Result / still open: The two storyboards are ready. Final-frame readability will be checked on both exports.

- What was hard: A long experiment batch was running on the production laptop.
- What I tried: I used a temporary system wake request and worked in isolated video staging.
- Result / still open: The episode review went ahead while the experiment continued.

- What was hard: The recorded narration ran shorter than the draft estimate.
- What I tried: I measured the generated speech and allowed extra reading time on the diagram, examples, and results.
- Result / still open: Both cuts use the same measured 3:04.250 timeline, with the approved words and pace.

- What was hard: The third comparison card was cued after the measured beat end, and six icon names needed available assets.
- What I tried: I reset that reveal to the measured timeline and used matching icons from the bundled library.
- Result / still open: All three cards appear in order and every scene slot is filled.

- What was hard: An overview in portrait and four card captions in landscape fell below the typography gate's minimum.
- What I tried: I enlarged the portrait overview and increased the three-card subtitles in the isolated layout. I checked chart contrast at the text regions.
- Result / still open: Both layouts passed the typography check with the approved wording.

- What was hard: The portrait final-frame check found a duplicate footer below the safe area. The stock master checker also lacked its duration helper.
- What I tried: I kept the footer already inside the opener and omitted the duplicate assembly overlay. I verified frame count and audio timing independently with ffprobe.
- Result / still open: Both masters passed final-frame and audio checks. Each measures exactly 4,422 video frames.

- What was hard: An early Whisper check spelled the presenter name differently. The full transcripts disagreed with a few phrases and reported extra words during the silent credit.
- What I tried: I transcribed both masters independently, joined a split decimal token, and compared the remaining words and timestamps against the script. I checked the audio during the extra words.
- Result / still open: Both full transcripts recognized the presenter name. The credit interval was silent. The remaining differences are in the listening review.

## 2026-11-15

- What was hard: The first cut ran longer than the Nov 7 reference episodes.
- What I tried: I used the shorter supplied narration, five card beats and one takeaway slide.
- Result / still open: The revised plan targets about 2:25. Actual time depends on the approved narration.

- What was hard: Whisper heard the first cut’s Room A as “rumour.”
- What I tried: I kept Room A on screen and marked it for a fresh transcription check.
- Result / still open: Check it after voice approval. If it recurs, adjust the pronunciation in synthesis and leave the card copy intact.

- What was hard: Whisper added words over the first cut’s silent credit.
- What I tried: I checked the flagged interval against the decoded audio.
- Result / still open: The interval contained only zero-valued samples. Check the new credit before counting any words Whisper reports there.

- What was hard: The first measured narration was shorter than the reference pacing.
- What I tried: I kept Kokoro synthesis at speed 1 and applied a 0.89× pitch-preserving pace edit with pauses tied to the spoken phrases.
- Result / still open: Both 2:22 cuts use the approved narration and preserve the card order.

- What was hard: The loop's Repeat subtitle ran past its card, and the portrait study-room heading was below the typography minimum.
- What I tried: I increased the loop card height and enlarged the portrait heading in the isolated ai-explainer layout.
- Result / still open: The full copy and linking arrows fit both layouts, and both passed typography.

- What was hard: The first final assembly stopped at the paperwork gate because the episode documents had not been copied into staging.
- What I tried: I copied the approved fact check, shot list, and prompts into each build. I checked frame duration independently because the stock master checker lacked its duration helper.
- Result / still open: Both masters passed the stock final checks and the independent 3,408-frame check.

- What was hard: The first final ReAct transcripts heard the second Room A as “rumor.”
- What I tried: I stressed the letter A with a voice-only pronunciation, regenerated the one spoken beat, and rerendered its matching scene in both layouts.
- Result / still open: Each final transcript recognizes both Room A mentions. There are no remaining word mismatches after normalizing equivalent number and acronym forms.
