# Frictional log — The Link That Pointed Nowhere

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

Fifth report in the Layer 1 hardening series: the pipeline's Google News link classifier stored only dead-end redirect links, because the old `url=([^&]+)` regex never matched modern Google News redirect link formats. The real fix required reverse-engineering how the redirect page itself resolves the article — a signed id/timestamp/signature POSTed to an internal, undocumented Google endpoint. The plan was a 10-beat, ~2.7-minute report walking through the dead-end setup, the discovery of the real resolution mechanism, a subtler classification-ordering near-miss caught before it shipped, three escalating rounds of live verification, and two honestly-flagged limitations. This was also the first video built under the toolkit's new submission spec: deliverables named `ProjectName_VolunteerName.mp4` with no date/aspect suffix, landscape and vertical masters in separate `deliverables/` subfolders, and — notably — a true 4K, full-length, native-portrait vertical rebuild via `./art vertical` rather than the earlier Shorts-style crop/reformat approach used in this fellow's prior videos.

## Where it resisted

- Fact-check flagged that the reverse-engineered resolution mechanism needed stronger framing so it wouldn't read as a stable, documented API — resolved by adding an explicit on-screen caveat label ("reverse-engineered — not a documented/official API") held for the whole beat, rather than a brief disclaimer.
- Two separate render handoffs were interrupted mid-process: the landscape master's render agent backgrounded the compile step and stalled without reporting completion, and the vertical master's render agent hit a transient network error partway through. In both cases the follow-on work verified the already-completed scenes/clips were real and valid on disk before resuming only the remaining beats, rather than discarding progress and re-rendering everything from scratch.
- A later documentation/verification pass personally extracted and inspected real frames (not just the beat sheet's description) from the two most safety-critical beats — the reverse-engineered-mechanism caveat and the dual call-order diagram — specifically because FACTCHECK had flagged those as the places most likely to overstate certainty. One cosmetic tightness was noted (the vertical caveat box's bottom border sitting close to its own text baseline) but judged not to warrant a re-render since every character remained legible and GATE V measured 0 BLOCKER/0 MAJOR.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) authored the beat sheet, narration, and both the landscape and native-portrait vertical Manim scenes (a full redesign, not a crop), generated Kokoro audio, managed the render pipeline across two interrupted handoffs, and ran the GATE V checks and direct frame-level verification on both masters. The fellow approved the plan and resolved both fact-check open items before narration lock: she required the stronger on-screen caveat for the reverse-engineered mechanism, and she explicitly kept both of the script's honest limitations (unverified against her live n8n instance; ~400 extra requests per run) at full weight rather than softening either.

## Still open / understood now

- `B3-VERIFICATION.md` is explicit that this fix is verified only against the workflow file and a full local re-implementation, not against the fellow's actual live n8n instance — the script is deliberately scoped to avoid any claim of production verification.
- The fix adds roughly 400 extra requests per run, run sequentially by deliberate choice rather than parallelized — presented as a real, unsoftened tradeoff, not a resolved issue.
- One cosmetic tightness in the vertical caveat box's text fit was noted during the documentation pass but left as-is, since it doesn't affect legibility.
- Publishing was not authorized for either deliverable as of the last BUILD-LOG entry.
