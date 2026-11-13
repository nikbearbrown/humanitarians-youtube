# Frictional log — Tokenization: Why AI Can't Count the Letters in Its Own Words

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

This general-AI-topic explainer covers why language models unreliably count letters in their own words: they read text as sub-word tokens, not individual characters, so a word's token split often doesn't align with its actual letters. The plan was a 9-beat explainer using a deliberately generic "how many R's in strawberry"-style worked example — chosen because it plausibly splits into three sub-word chunks and has a repeated letter worth counting, without naming or benchmarking any specific real model — showing the token-level miscount (2) against the true count (3), then a falsifiability case using the same word and same model with only the spelling-out changed (each letter its own token, now counting correctly).

## Where it resisted

- Two beats' hand-computed final wait values had arithmetic errors (a dropped addend in the running tally), causing their rendered clips to run longer than their measured Kokoro audio — caught by independently comparing each scene's own timing sum against the measured duration via a small script, not by trusting the inline comments, and fixed in both beats.
- The post-render layout checker caught a real margin violation where a checkmark line, placed via a width-dependent conditional branch, landed outside the safe area — fixed by removing the conditional branch and always placing it in the position that cleared the margin.
- The first "true" (non-review-overlay) candidate build measured real underfill across four beats, requiring a mix of fixes: adding generously sized bordered frames to two sparse beats, enlarging a checklist card to a fixed size independent of its own tight content bounds, and bumping font sizes and spacing on the closing brand card (the same fix already proven on sibling reels). Enlarging the checklist card then took two more rounds to get right, since the first enlargement pushed its bottom corner under the line below it, and the correction pushed its top corner under the title above — ultimately requiring a shorter, origin-centered size that cleared both with real margin.
- The portrait redesign hit a real off-hard-frame coordinate (not just a soft margin violation) caused by chaining five relative `next_to()` calls, where accumulated positioning error landed an element entirely outside the hard frame boundary — fixed with a more robust pattern of grouping every element first, capping the total height, and positioning the whole block with a single call rather than chaining relative offsets.
- A separate portrait beat had a closing line landing directly on a panel's own rounded corner because a scale-down ceiling was set just high enough that a borderline-sized group never actually triggered the cap — fixed by lowering the ceiling so the group reliably scaled down with real clearance.
- The familiar stale render-cache issue recurred (the render pipeline doesn't detect scene-source changes and silently reuses old cached clips) and was handled with the established clean-rebuild-and-verify-timestamps discipline.
- Both the landscape and vertical review-cut builds failed the automated visual check with uniform BLOCKER findings on every beat — confirmed as the same known review-overlay artifact documented across this fellow's other reels (the debug timecode sits outside the checker's exclusion zone), verified non-blocking by building a clean candidate with no overlay and re-checking directly.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) authored the beat sheet, narration, both the landscape and native-portrait Manim scenes, generated Kokoro audio, and found and fixed every bug above through independent timing verification, direct frame measurement, and cache-timestamp checks rather than trusting authored comments or automated reports alone. The fellow approved the beat sheet and narration before any audio was generated (Gate P), and in the fact-check review confirmed the worked example should stay fully generic with no specific real model named or benchmarked — fact-check also specifically required the narration avoid claiming the letter-by-letter fix works universally or for every model, phrasing it instead as succeeding for this illustrative case.

## Still open / understood now

- This video is explicitly not a benchmark or disclosed test of any specific real model's tokenizer — the worked example is kept intentionally hypothetical and generic, since real tokenizer behavior changes between model versions.
- Fact-check requires the narration frame the letter-by-letter fix's improvement as an expected effect of the mechanism shown, not a universal guarantee across all models.
- Both masters were personally re-verified by extracting and viewing real frames from the shipped deliverables as a final check.
- Publishing was not authorized for either deliverable as of the last BUILD-LOG entry.
