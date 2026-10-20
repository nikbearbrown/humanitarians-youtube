# Frictional log — The All-Clear That Wasn't All There

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

This weekly report covers a small, honestly-scoped display bug: the pipeline's routine "all clear" status email had a static, hand-written "Monitored Sources" grid that listed only 4 of the pipeline's 5 real RSS feeds — Investment Advisor Rules, a real working source node, was simply never added to the card. The plan was a 9-beat, ~1.8-minute report recreating the email's real shipped grid verbatim, showing the real workflow's 5 feed-node names against the 4 actually displayed, the fix (an added card verified one-for-one against the workflow), and a brief honest aside confirming an older unrelated item from a prior findings document was already fixed rather than needing a new patch. This was the second video built under the toolkit's new submission spec, with a true full-length 4K native-portrait vertical companion rather than a cropped Shorts cut.

## Where it resisted

- The one fact-check open item was about framing, not facts: making sure the brief B06 aside (the stale findings-document note) read as a confirmed-closed check rather than a new fix shipped in this video — kept exactly as drafted.
- The vertical companion's render-agent session was interrupted by a network error partway through; picking it up cold required first reading the existing `vertical/scenes.py` in full to confirm it already carried two known required fixes (a safe-text helper working around a small-font rendering artifact, and a portrait frame-width patch for a known Manim CLI quirk) before touching anything.
- A real stale-render-cache bug was confirmed: every vertical clip's file timestamp predated the scene source file's last edit, meaning the render pipeline had no way to detect that the source had changed — fixed by deleting all cached vertical render artifacts and rebuilding fresh, then confirming every new clip's timestamp postdated the source.
- The rebuilt vertical render then failed GATE V with BLOCKER edge-bleed on literally every single sampled frame — a 100% uniform failure across completely unrelated beat content was itself the tell that this was a tooling artifact, not a real defect. It was traced to the review cut's own debug timecode overlay sitting outside the checker's known exclusion zone, confirmed by extracting and visually inspecting the actual flagged frame (real content sat well inside the safe area; only the debug overlay crossed the edge) and by running the same check directly against the raw, overlay-free clips, which came back completely clean. No toolkit file was edited; the fix was simply to rely on the final export path, which carries no debug overlay, as the actual ship-decision gate.
- While investigating, an older, already-written QC report for the landscape master was found to still show a stale false-positive reading from an earlier review-slate run — re-checked against the real landscape deliverable and confirmed clean, with the landscape content itself verified unchanged by hash before updating the stale report.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) authored the beat sheet, narration, both the landscape and native-portrait Manim scenes, generated Kokoro audio, and diagnosed and resolved the stale-cache bug and the false-positive GATE V failure through direct frame extraction and hash verification rather than trusting either the cache state or the automated report at face value. The fellow approved the plan and narration before any audio was generated (Gate P), and in the fact-check review she confirmed the one framing-sensitive aside (the stale findings-document note) should stay exactly as drafted — a short, clearly scoped side-finding, not expanded into something larger than it was.

## Still open / understood now

- The fact-check table is explicit that this is a display-only fix to a status email — no scoring, classification, or alert-routing logic was touched, and the narration deliberately does not imply otherwise.
- The B06 aside is deliberately framed as a confirmed-already-fixed check (via git history, predating the findings document itself) rather than a new fix shipped in this video — a distinction fact-check required be preserved.
- Both deliverables were verified byte-identical by SHA-256 against their `.verified.json` receipts after the stale-cache rebuild.
- Publishing was not authorized for either deliverable as of the last BUILD-LOG entry.
