# FACTCHECK: Markers Gone Does Not Mean Merged Right (report video, week of 10-26-2026)

Format: claim | verdict | source | fix. Written 10-26-2026.
Verdicts: VERIFIED = matches my table-building chat. CONFIRM = check before relying on it.

## Narration

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B00 | The week's video is a how-to on reading a merge conflict | CONFIRM | The video's topic, not a claim about my work that week | Confirm what I did that week |
| B01 | My branch inserted a table directly above a heading whose characters were garbled | VERIFIED | Chat: explanation of the conflict | None |
| B01 | `development` had fixed the garbled characters in that heading | VERIFIED | Same | None |
| B01 | Table 23.4.2 merged cleanly because it was not next to a changed line | VERIFIED | Same | None |
| B02 | The conflict shows three marker lines around the two versions; the fix keeps the table and the clean heading | VERIFIED | Chat: the four things to delete | None |
| B03 | After resolving, the markers were gone and both tables were in the right places | VERIFIED | Chat: check of my resolved file | None |
| B03 | The garbled heading survived, along with old wording from before `development`'s fixes | VERIFIED | Same | None |
| B03 | Committing it would have overwritten `development`'s text fixes | VERIFIED | Same | None |
| B04 | Three searches catch it: the markers, the garbled characters, and a phrase only `development` has (`chlorambucil, Vd ~0.3`) | VERIFIED | Same | None |
| B05 | The fix was to abort the merge and merge again, keeping both parts | VERIFIED | Same | Confirm that is what I did |
| B05 | Pull `development` into the branch before inserting tables | VERIFIED | Chat advice | None |
| B06 | How-to advice | Advice | n/a | None |

## On screen

| Beat | Item | Verdict | Fix |
|---|---|---|---|
| B01 | Before and after heading lines | VERIFIED as paraphrases of the chat | None |
| B02 | The conflict in outline (marker lines and the two sides) | CONFIRM: reconstructed from the chat's description, not copied from the file | None needed; it is labeled as an outline |
| B04 | The three checks | VERIFIED | None |
| B00, B03, B05, B06 | Composer shows model label "Fable 5 High" | Dates the video | Leave, or change to "Claude" |

## Not claimed anywhere
When the conflict happened, that the final merge was clean, or that the other glitches were fixed.
