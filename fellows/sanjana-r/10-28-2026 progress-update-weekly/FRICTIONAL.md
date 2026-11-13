# FRICTIONAL.md — running diary (what I did, and what didn't work)

*Not graded. Required weekly. Append a dated entry each week; keep the friction in — the point
is the honest record, not a clean one.*

---

## 2026-11-13 — Week of Oct 25 progress reel

**What I did**
- Produced the weekly-progress ai-explainer ("Week of Oct 25") in 16:9 and 9:16 4K.
- Aggregated the week's task log into stats only, with **no names** (explicit ask): 22 hours,
  47 videos handled, ~10 creators, 22 reviewed → approval, 25 uploaded to YouTube.
- Built a new `WeekBoard` component (tiles / bars / flags) for the stat beats, since this is a
  progress report, not a concept explainer — no CLI loop.
- Framed the quality exceptions as *catches* (value added), not failures: 8 videos below 4K,
  4 missing the @HumanitariansAI watermark, GitHub code status tracked per project.

**The week's actual friction (the org work this report is about)**
- Videos keep arriving **below 4K** (1080×1920) — caught only at review, i.e. too late to be
  cheap. This happened on two projects this week (6 videos on one, 2 Shorts on another).
- Two sets of week-updates shipped **without the @HumanitariansAI watermark** — had to send
  them back. This is a recurring, mechanical miss that should never reach a human reviewer.
- **Code-on-GitHub** status was inconsistent ("Yes" / "No" / "Need to ask") — chasing it per
  project is manual and slow.
- The **pre-review pipeline** (quality gate on Drive, before upload) is still coordinated by
  hand with the dev team; it does not yet auto-check resolution or watermark.

**What didn't work / next week**
- The whole review stage is reactive: humans flag 4K + watermark after the fact. Next week's
  focus is to push those two checks **upstream into the pre-review pipeline** so they fire in
  Drive before anything enters the upload queue. Every hour spent flagging a 1080p render is an
  hour the pipeline should have saved.

**On producing this report**
- `style: ai-explainer` with no code beats; the hours split (8/7/4/3) is an allocation of the
  reported 21+ total across tracks — the video counts are exact from the log (see FACTCHECK.md).
