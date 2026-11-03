# Frictional log — The Alert That Waited for a Second Item

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

This weekly report covers a one-character-class bug in the alert-email path of the regulatory intelligence pipeline: the `Generate Email` node's `hasData` guard required strictly more than one qualifying item before building an alert, so a run with exactly one new high-priority item — the single scenario this alert system exists to catch — silently produced no alert at all, with no error or log line. The underlying engineering (finding the bug, the one-character-class fix from `> 1` to `> 0`, and a live Node.js verification harness run before and after the patch, then re-run against the real patched file) was the fellow's own prior work on Project 29. The plan was a 9-beat report showing the real verbatim guard line, the traced dead end, the exact diff, a real before/after harness table for 0/1/2 items, and two honest limits kept at full weight: that this was caught by code review rather than a live incident, and that a related but separate compatibility gap was found and flagged, not fixed.

## Where it resisted

- A recurring stale render-cache issue (the render pipeline doesn't detect scene-source changes) required deleting all cached render artifacts and verifying file modification times before trusting any render as current, for every re-render that followed a scene edit in both the landscape reel and its portrait companion.
- The post-render layout checker flagged two intentional design choices as false "label on a curve" errors — a highlight box deliberately boxing only a substring of a longer code line, and a genuine strike-through line deliberately crossing struck-out code — both resolved using the checker's own documented escape hatch for intentional overlaps rather than redesigning away from the intended visual.
- Real canvas-fill underfill was found on one beat where a counter composition's width looked fine but its height badly undershot the safe-area floor — a genuine vertical spacing problem, not a false positive, fixed by enlarging padding and buffs.
- A separate underfill was traced to animation timing rather than layout: a beat's closing caption landed on screen too late to be present at the automated 50% sample point. The first attempt to fix the timing introduced its own arithmetic slip that made the clip noticeably too long, silently absorbed by the compile pipeline's automatic trimming — caught only by independently re-summing every timing value in both scene files against each beat's measured audio duration before re-rendering, which also confirmed every other beat's timing was exact.
- The portrait companion had a real safe-area overflow where two independently-chained closing captions didn't leave enough room below a content card — fixed by tightening the card's own height cap.
- The review cut's debug timestamp overlay produced the same uniform false-positive edge-bleed finding on literally every sampled frame across every beat, confirmed as review-chrome rather than real content, with the true final export (which carries no such overlay) passing cleanly on its own merits.

## What Claude contributed, what was accepted/changed/rejected

This folder's own README documents the division of labor explicitly: the underlying engineering decisions, the bug discovery, the fix, and the live verification numbers were the fellow's own prior work on Project 29, carried into this video unchanged. Claude (via Claude Code) authored all 9 Manim scenes in both aspect ratios, generated the Kokoro narration audio, ran the full render/compile/QC pipeline, and found and fixed every layout, timing, and cache-staleness defect documented above — including catching its own arithmetic error in a timing fix by independently re-deriving every beat's real timing sum rather than trusting the first correction. The README states plainly that nothing in the pipeline fabricated or altered the underlying code, numbers, or verification results, and that there was nothing to reject or correct this session since the beat sheet and fact-check were already approved before the build began.

## Still open / understood now

- Fact-check requires the narration state plainly that there is no evidence this specific bug ever caused an actual missed alert on a real run — the pipeline isn't instrumented to log per-run item counts at that granularity, and the script states this limitation explicitly rather than implying it was caught by an incident.
- A related `source_feed` compatibility gap in a downstream component was confirmed live as a real latent issue (not yet triggered in practice because the frontend doesn't currently pass that parameter) and is explicitly flagged as identified-but-not-yet-fixed, not resolved.
- As of the last BUILD-LOG entry, both deliverables were GATE V clean and personally frame-checked, with PM review, YouTube processing, and a publication decision all still pending.
