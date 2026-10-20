# Frictional log — The Pipeline That Was Lying to Me

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

The plan was to take one real fix from the Project 29 (Financial Regulatory Intelligence System) Layer 1 handoff — a silent content filter that had been dropping empty-description filings with no error or log — and turn it into a single-insight ~90s `ai-explainer`: a 7-beat Hook/Setup/Discovery/Proof/Fix/Takeaway/Sign-off arc. Two other candidate fixes (parameterized inserts, feed isolation) were scoped out for future episodes. The expectation going in was that Kokoro narration (voice TBD), a handful of Manim/Remotion-style beats, and the pipeline's own measured before/after count (297 → 370, +73 recovered items) would be enough to carry the proof.

## Where it resisted

- The suggested voice `af_kore` didn't exist in the installed toolkit (only `am_onyx`/`af_bella` were shipped); the fellow confirmed Bella (`af_bella`) instead.
- Two of the planned Remotion components (`ClaudeCodeDiffView`, `HumanitariansResearchReport`) didn't exist in the installed toolkit, and building them would have meant adding to the shared `brutalist/` repo, which was out of scope — all five non-Manim beats were rebuilt as self-contained Manim scenes instead.
- A toolkit slate-label truncation bug (hard 80-char cut, no word-wrap) was worked around without touching the toolkit, via a short `new_visual_element` field.
- GATE V repeatedly flagged the review cut's own timecode watermark as a false-positive "edge-bleed" defect — resolved each time by checking the true clean master instead of the watermarked `-slate.mp4`.
- The later 4K/program-feedback rebuild (2026-08-26) surfaced more friction: the toolkit's `run.sh` now hardcoded 4K render resolution regardless of flags; renumbering all 7 beats by +2 to add two new front beats required clearing every compile-derived artifact folder so nothing stayed keyed to old beat IDs; the new `B01_ExecSummary` beat tripped GATE A for having only one static shape; two new beats came back with genuine MAJOR "underfill" defects, fixed by measuring real Manim text metrics rather than guessing; and a frame grabbed for the self-assessment at an imprecise timestamp briefly showed the wrong count ("366" instead of settled "370") before a frame-accurate re-extraction confirmed the real number.
- Building the 9:16 Shorts derivative (2026-08-28) found a Manim CLI quirk that silently breaks portrait renders toolkit-wide (`-r` sets pixel dimensions but not `frame_width`, so content renders at roughly a third of its intended size) — root-caused and fixed in this reel's own `short/scenes.py` without touching the shared toolkit. The portrait redesign of the pipeline diagram and the before/after counter also went through three real GATE-B-caught layout bugs (title/row collisions, callouts and captions landing outside safe margins) before clearing.
- One MAJOR underfill defect was left unresolved on purpose: the toolkit's own auto-generated silent endcard has a fixed layout not editable without changing the shared `brutalist/` repo, which was out of scope — flagged as a human design call rather than silently forced or silently accepted.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) did the hands-on build: drafting the beat sheet and narration, authoring the Manim scenes, generating Kokoro audio, running the GATE A/W/B/V checks, diagnosing the false-positive watermark issue, tracing and fixing the portrait-frame CLI bug, and measuring/fixing underfill defects. The fellow made the calls that mattered: choosing which Layer 1 fix to feature, confirming the voice, reviewing the fact-check table and explicitly electing to keep one flagged phrasing ("verified the output against the production database") as-is rather than take the proposed correction, and watching the rendered 7-beat master before approving it (2026-07-27). The fellow had not yet re-reviewed the rebuilt 9-beat 4K cut's narration at the point this log was written, and publishing was explicitly withheld pending separate authorization.

## Still open / understood now

- The fellow's narration re-review of the specific 9-beat 4K cut (as opposed to the original 7-beat cut) was not yet recorded as of the last build-log entry.
- Exact filing URLs for the four named recovered filings were never pulled into `SOURCES.md` — flagged as open but non-blocking since this toolkit doesn't publish externally.
- 11 MAJOR cosmetic defects (underfill on several cards, mild low-contrast on one beat) remain accepted as polish-only, not correctness, on the long-form cut.
- One MAJOR underfill defect remains on the Shorts endcard, understood to require either a hand-authored replacement image or a shared-toolkit change that was out of scope.
- Self-assessment against `PROOF.md`'s rubric scored 4/12, understood as a genre mismatch (PROOF targets framework-teaching explainers; this is a single-insight case study) rather than a defect to chase.
- Publishing was not authorized for either the long-form or the Shorts cut as of the last entry in this folder's BUILD-LOG.md.
