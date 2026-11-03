# Frictional log — Hallucination: Why Sounding Sure Isn't the Same as Being Right

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

This general-AI-topic explainer teaches a reusable 3-question rubric — Checkable? / Would it hedge? / Does confidence track difficulty? — for telling a model's genuine certainty apart from fluent-sounding phrasing that merely resembles it. The plan was a 9-beat explainer: the framework shown fully before any example, a worked example (a fabricated citation delivered in exactly the same confident tone as a real one), a falsifiability stress-test using a genuinely true, easy fact so the rubric doesn't collapse into "confident tone always means hallucination," and a closing audit task. Both illustrative examples were planned as fully generic and hypothetical from the outset, confirmed by fact-check before narration lock.

## Where it resisted

The BUILD-LOG documents ten distinct real bugs found and fixed during this build, more explicitly itemized than in most of this fellow's other reels:

1. Inline timing-comment arithmetic for two beats' final wait values was mis-tallied by a second or more; the compile pipeline's automatic center-cut silently absorbed the error rather than erroring, so it was only caught by independently re-deriving each beat's real timing sum and comparing it against the measured audio duration, not by trusting the authored comments.
2. A sequential card-reveal design caused a real underfill failure because the automated sample point landed before all three cards were on screen — fixed by showing all three together up front with emphasis pulses instead of sequential fades.
3. A result row sized to exactly the safe-area width, with no real margin, bled past the edge once a tracking box was drawn around it.
4. Three separate closing lines in the landscape cut had their real rendered bottom edge outside the safe area — caught by the post-render pixel audit, not a guessed margin.
5. The same class of edge-clipping bug recurred across five beats in the portrait redesign, since multi-line text is taller relative to the narrower portrait safe width.
6. Fixing one portrait beat's title margin inadvertently caused its closing text to start overlapping a panel's own rounded-corner curve — a real collision requiring a different fix (shrinking the panels to free space) rather than a larger buff, since a larger buff moved both edges together without creating separation.
7. The most significant bug: the default final-render command silently produces the wrong resolution for a 9:16 reel (1216×2160 instead of the required native 2160×3840) because its hardcoded default height assumes 16:9 reels. The resulting aspect mismatch triggered a crop during compilation that tipped several already-tight beats over the safe edge as real BLOCKER defects — even though the native Manim clips were independently confirmed clean. Root-caused by comparing the automated report against a direct check on the untouched native clips, and fixed by always passing the explicit correct height for this reel's vertical export.
8. After fixing the resolution bug, four beats still had smaller real issues (oversized decorative frames narrowly exceeding the true portrait safe width, and one beat underfilling at 39%) requiring two more rounds of measured adjustment.
9. A stale render-cache issue recurred across multiple rounds: the render pipeline doesn't detect scene-source changes and silently reuses old cached clips, requiring an explicit clean-and-rebuild discipline (delete caches, re-render, verify every clip's modification time postdates the source) before trusting any render as current.
10. The review-cut's debug timecode overlay produced the same known false-positive edge-bleed BLOCKER on every beat in both aspects — confirmed as a slate-only artifact that never affected the true final export.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) authored the beat sheet, narration, and both the landscape and native-portrait Manim scenes, generated Kokoro audio, and found and fixed all ten bugs above through direct measurement, frame extraction, and hash/timestamp verification rather than trusting automated reports or authored comments at face value — including re-deriving timing sums independently and re-extracting frames that looked like rendering artifacts in a quick spot-check to confirm they were sampling-timing coincidences rather than real defects. The fellow approved the beat sheet and narration before any audio was generated (Gate P), and in the fact-check review confirmed both illustrative examples should stay fully generic with no resemblance to any real disclosed incident, model, or paper.

## Still open / understood now

- This video does not benchmark any real model's hallucination rate and names no specific real model, vendor, or product — a deliberate scope boundary stated plainly in the README.
- Both masters were personally re-verified frame-by-frame from the shipped deliverables as a final check, including re-confirming that an apparent rendering artifact caught in a quick spot-check was a sampling-timing coincidence rather than a real defect.
- Publishing is marked ready-for-review in the beat sheet's gate record, not approved — it requires separate fellow/PM sign-off per the toolkit's submission spec.
