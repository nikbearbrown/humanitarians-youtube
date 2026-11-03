# Frictional log — How Facial Recognition Actually Works (And When It Shouldn't)

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

A template brief called for a 5-minute deep-explainer on facial recognition; the fellow scoped it down to a 3-minute `ai-explainer` instead: an 8-beat, first-person, deliberately balanced script (Hook / Mechanism / Benefits / Harms / Evidence / Framework / Takeaway / Sign-off) that states both the legitimate uses and real harms of the technology, cites NIST's own demographic-bias data, and closes on a "scrutiny should scale with stakes" thesis rather than a policy verdict. The plan was to verify the one claim with real stakes — NIST's demographic-accuracy finding — directly against the primary source before the narration was even drafted, not patch it after the fact.

## Where it resisted

- The later 4K/two-new-opening-beats rebuild (program feedback, 2026-08-25/26) required re-renumbering all beats, which risked stale beat-ID-keyed clips silently filling the wrong new slots — avoided by clearing every compile-derived artifact and renaming mp3s in descending order to avoid clobbering.
- GATE V's automated pass (which checks the watermarked review `-slate.mp4` by default) repeatedly reported dozens of false BLOCKER defects from the review timecode burn-in; every real check had to be run against the true clean master directly instead.
- A genuine, previously-latent bug was found this way: B04's caption used a `Write()` letter-tracing animation whose window straddled GATE V's 50%-of-beat sample point, producing a frame with garbled overlapping glyphs — fixed by swapping to `FadeIn()` and tightening the timing so the caption settled well before the sample point.
- A `run.sh` re-render pass was killed mid-mux by an environment timeout, corrupting the in-progress master file (`moov atom not found`); recovered by re-running only the final compile step (not a full re-render) in the background.
- Several MAJOR "underfill" and "low-contrast" GATE V findings needed per-case investigation rather than blanket fixes: some were confirmed false positives (direct WCAG computation on the palette gave 11.99:1 ink-on-cream contrast, nearly 3x the AAA bar, versus a whole-frame-luminance heuristic that penalizes sparse cream frames), while others (B01/B05/B06/B11 sparse layouts) were judged intentional by eye.
- Building the 9:16 Short required dropping a beat to fit the 180s cap. The automated planner's first choice was to drop B07 — the only cited primary-source evidence in the whole script — which was explicitly overridden (`--keep B07`) in favor of dropping B09 (a worked example) instead, since losing a worked example was judged a smaller loss than losing the only hard evidence.
- The portrait rebuild hit the same Manim CLI frame-width quirk documented elsewhere in this fellow's work (portrait `-r` doesn't shrink `frame_width`, so a first authoring pass rendered at 5-8% canvas fill on every beat) — fixed via the toolkit's own documented frame-width-recompute patch, and this also explained a related GATE A false alarm about an arrow being "outside the frame."
- B03's thesis-text animation in the Short hit the identical straddled-sample-point glyph-garbling bug as B04 in the parent cut, fixed the same way.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) drafted the beat sheet and script, authored all 12 (then 11 for the Short) Manim scenes, generated Kokoro narration, ran and interpreted every GATE A/W/B/V pass, diagnosed the false-positive watermark and contrast findings against real extracted frames rather than trusting the automated report at face value, and found/fixed the real animation-timing bugs. The fellow scoped the format (5-minute brief down to 3-minute explainer), approved the 8-beat script before any audio was generated (Gate P), and the sign-off beat explicitly credits the fellow by name per the fellowship's compliance requirement. The exec-summary beat's narration text in the rebuild was supplied verbatim by the program, not by Claude. No factual corrections were needed from the fact-check process — the original draft, verified before lock, matched NIST's NISTIR 8280 numbers exactly.

## Still open / understood now

- Four MAJOR "underfill" findings (B01/B05/B06/B11 in the long cut) were reviewed by eye and judged intentional sparse/centered layouts, not accidents — left as-is.
- A known gap in the self-assessment against PROOF.md's rubric (10/12): the video's 3-question framework is never shown failing or straining against a genuinely ambiguous case — every worked example resolves cleanly to one stakes-bucket — logged as a future punch-list item, not fixed in this rebuild.
- The Short's endcard carries 2 underfill findings tied to the toolkit's own `shorts.py`-generated `endcard_png()` layout, which is outside this task's scope (the shared toolkit is read-only).
- Publishing was not authorized for either the long-form or the Shorts cut as of the last BUILD-LOG entry — separate human fellowship sign-off is required.
