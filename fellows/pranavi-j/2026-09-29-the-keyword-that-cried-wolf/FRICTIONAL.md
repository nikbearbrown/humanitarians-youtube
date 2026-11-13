# Frictional log — The Keyword That Cried Wolf

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

This weekly report covers a real fix to the pipeline's keyword scorer: two named noise patterns — a routine Medicare payment rule scored 10/Critical because "emergency" appeared in a law's proper name, and a boilerplate Nasdaq filing scored 9/Critical because of the phrase "Immediate Effectiveness" — are now caught by a local-LLM second-opinion review before triggering an alert, without touching the original scorer and with an explicit fail-open path if the model itself breaks. The plan was a 9-beat report: the exact scoring rule quoted verbatim, both real trigger words shown in their actual harmless context, the fail-open design shown explicitly (not just the happy path), and live verdicts for all three test cases — including a genuine true positive that correctly should not be reviewed at all.

## Where it resisted

- Fact-check caught a subtle framing risk before narration lock: the draft script said the true-positive SEC case was "left alone," which is accurate, but risked being misread as "the AI reviewed it and approved it" when in fact its urgency score never crossed the threshold to be sent to the model at all. Resolved by adding an explicit on-screen label ("not reviewed — below alert threshold") rather than relying on narration wording alone to carry that distinction.
- Both of the build's real technical bugs were already-known issues from prior sibling builds, applied here proactively rather than rediscovered: a stale render-cache issue (the render pipeline doesn't detect scene-source changes and will silently reuse old cached clips, requiring explicit cache-clearing and modification-time verification before trusting any render) and a Manim/Pango small-font text-rendering artifact (phantom gaps appearing inside words at small font sizes) that was avoided from the start by using an established safe-text helper for every string in both aspect ratios, rather than discovered and retrofitted after the fact as happened on an earlier sibling project.
- The build spanned several agent sessions due to repeated transient network disconnects, not logic failures — each resumption required re-verifying actual on-disk state (file timestamps, process list, deliverable hashes) before continuing, rather than trusting a prior session's self-report of what it had completed.
- The vertical cut shipped with two minor MAJOR findings on the brand/sign-off card, right at the borderline of the canvas-fill floor — personally confirmed via direct frame extraction to be fully legible and well-composed, the same accepted minor-cosmetic category as brand cards across this fellow's other reels.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) authored the beat sheet, narration, both the landscape and native-portrait Manim scenes, generated Kokoro audio, and applied the established playbook for the two known bug classes proactively. Each agent session resumption independently re-verified real on-disk state rather than trusting self-reported progress from a prior session, and the final masters were personally re-inspected frame-by-frame directly from the shipped deliverables, specifically confirming the SEC case's on-screen label read "not sent to model" / "UNTOUCHED" exactly as fact-check required. The fellow approved the plan and narration before any audio was generated (Gate P), and in the fact-check review she specifically required the added on-screen clarity label for the true-positive case and kept the honest-limits beat at full weight with no softening.

## Still open / understood now

- This video deliberately does not claim to be a comprehensive benchmark evaluation of the scorer — it targets only the two specific patterns already named and measured in the source findings document, not a general claim about all possible misfires.
- Fact-check requires the narration never imply the model "checked and approved" the true-positive case — it was correctly excluded from review entirely, which the on-screen label now makes explicit.
- Two minor underfill findings remain on the vertical cut's brand card, confirmed legible and accepted as cosmetic.
- Publishing was not authorized for either deliverable as of the last BUILD-LOG entry.
