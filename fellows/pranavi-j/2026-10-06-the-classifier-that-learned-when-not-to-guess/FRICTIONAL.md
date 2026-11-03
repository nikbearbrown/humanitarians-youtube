# Frictional log — The Classifier That Learned When Not to Guess

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

This weekly report is a continuation of the ongoing B2 source-classification fix: of 21 headlines that had been falling through the keyword/pattern classifier to "Unknown Source," prior fixes had already resolved 13, leaving a genuine residual of 8 generic headlines that no fixed keyword list could resolve without false-positiving on unrelated content. The underlying engineering — a local-LLM (Ollama) fallback classification node, its conditional gate, fail-open design, and the live verification harness measuring 21/13/8 and 0 mutated/1 resolved/7 declined/0 errors — was the fellow's own prior work on Project 29, done before this video-build session. The plan was a 9-beat report presenting that work honestly, including framing the modest 1-of-8 result as a correct outcome (the model declining to guess on ambiguous content) rather than a shortfall.

## Where it resisted

- A recurring stale render-cache issue required deleting all cached render artifacts and verifying file modification times before trusting any render as current, each time a scene edit followed a prior render.
- The static pre-flight checker produced real "shapes never change" flags on three text-only beats that had only a single static shape created once — fixed by adding a second shape-creation event to each, following the pattern already used elsewhere for diagram beats but not yet applied to pure-text statement cards.
- Several beats' title/caption margins were initially too tight and landed just outside the safe area on the real rendered frame — standardized to a wider buff value across both aspect ratios after the pattern repeated on multiple beats.
- Three portrait beats had a real text-on-text overlap (not a QC false positive, measured at 41-67% overlap) because closing captions were positioned independently from a beat's main content, which could grow tall enough to physically collide with it — fixed by building the whole rest-of-beat content as one grouped unit with a shared height cap, rather than positioning pieces independently.
- Canvas-fill underfill recurred on several beats for two different real reasons: content genuinely clustered in one quadrant of the frame (fixed by centering the composition), and a card's frame sized purely from its own modest content rather than a generous minimum (fixed with a fixed-minimum frame size).
- Real edge-bleed was found on two beats: a tile row sized wider than the safe width (shrunk), and a brand card where padding calculated from an already-wide handle string pushed the frame itself past the safe edge (fixed with a reduced width cap and modest fixed padding instead).
- Several render passes were interrupted mid-build by the environment's tool timeout due to heavy concurrent CPU load from an unrelated process running elsewhere on the same machine — each resumption verified actual on-disk render state before continuing, rather than re-rendering unnecessarily or trusting a prior session's self-report.

## What Claude contributed, what was accepted/changed/rejected

This folder's own README documents the division of labor directly: the fellow's decisions, the underlying engineering implementation, and the live verification numbers (21/13/8, 0 mutated/1 resolved/7 declined/0 errors) were all her own prior work on Project 29, carried into this video unchanged. Claude (via Claude Code) authored all 9 Manim scenes in both aspect ratios, generated the Kokoro narration audio, ran the full render/compile/QC pipeline, and found and fixed every layout, timing, and canvas-fill defect documented above. The README states plainly that nothing in the pipeline fabricated or altered the underlying numbers or quoted headlines, and that there was nothing to reject or correct this session since the beat sheet and fact-check were already approved before the build began — the work was focused on authoring visuals accurately against already-approved claims.

## Still open / understood now

- This video is explicitly scoped as a report on one specific 8-item residual, not a general claim that LLM fallback classification resolves "Unknown Source" items at scale.
- Fact-check required the 1-of-8 result be framed as the model correctly declining to guess, not as an underperforming fix — kept at full weight with no softening.
- As of the last BUILD-LOG entry, both deliverables were GATE V clean and personally frame-checked, with PM review, YouTube processing, and a publication decision all still pending.
