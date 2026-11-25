# FRICTIONAL.md — running diary (what I did, and what didn't work)

*Not graded. Required weekly. Keep the friction in.*

---

## 2026-11-18 — Week of Nov 17 progress reel

**What I did**
- Reviewed 48 videos across 7 creators and 2 projects (Brutalist and a new one, Causal Couture).
  A genuinely clean week: all 48 passed the 4K check and the watermark check, all were uploaded
  for the professors to review, and nothing was sent back.
- Held a meeting to scope the next automation stage: automatic upload to YouTube, triggered once a
  video clears the 4K check — the review gate feeding the publish step with no manual copy.
- Produced the weekly-progress ai-explainer ("Week of Nov 17") in 16:9 and 9:16 4K, stats only,
  no names. Reused the WeekBoard component (tiles / bars / flags) — no new component needed.

**The week's actual friction (the org work)**
- The first fully clean week is good news, but it also hides work: "zero sent back" doesn't mean
  zero effort — it means the 4K gate caught problems upstream before they reached review. Worth
  watching that the clean number doesn't get read as "less to do."
- A new project entered the pipeline (Causal Couture). New project = new naming conventions and a
  new point of contact; the first batch needed an extra eyeball to confirm it matched the process.
- Upload-for-review is still a manual hand-off. Every one of the 48 was copied up by hand — which
  is exactly the step the auto-upload meeting is meant to remove. The plan exists now; the work
  doesn't go away until v1 ships.
- The auto-upload idea raises a real question we flagged in the meeting: where does professor
  review sit relative to the YouTube upload? We kept review as the gate *before* public — automating
  the upload must not automate the publish. That constraint needs to be explicit in v1.

**What didn't work / next week**
- No code to show this week — the milestone was a meeting, not a shipped feature, so the reel
  reports a plan rather than a demo. Next week should turn it into a first working version: on a 4K
  PASS, queue the video for upload, with prof review still gating anything public.

**On producing this report**
- Pre-flagged the outro beat sparse_by_design up front (learned from earlier GATE V underfill on
  bookend cards). Reused WeekBoard end to end, so the build was fast and both cuts passed the gates.
