# Week of Nov 4 — weekly progress video

A short **weekly-progress ai-explainer** made for **Sanjana**, produced with the Brutalist
video toolkit and watermarked **@HumanitariansAI**. Reports the week's video-QA work as
**stats only, with no names**. Narrated by **Liam** (local Kokoro `am_onyx` voice).

---

## The files

| File | What it is | Use |
|---|---|---|
| `WeeklyProgress-Nov04-16x9-4K.mp4` | 16:9 landscape master, 3840 × 2160 (4K) | main video |
| `WeeklyProgress-Nov04-9x16-4K.mp4` | 9:16 vertical master, 2160 × 3840 (4K) | Shorts / Reels |
| `BEATSHEET-16x9.json` / `BEATSHEET-9x16.json` | Shot-by-shot scripts | Source / re-edit |
| `PROOF-REVIEW-RESULTS.md` | Self-review (production gate, no-fabrication, privacy) | QA record |
| `FRICTIONAL.md` | The week's running diary — what was done and what didn't work | Weekly log |
| `README.md` | This file | — |

- 24 fps · AAC stereo · H.264 (`yuv420p`, `+faststart`). Force **2160p** on YouTube for true 4K.

## What's in the video (stats only — no names)

Opening line: *"Hi, this is Liam for Sanjana, and this is the progress report for the week of
November 4th…"* Then:

1. **The week at a glance** — **22 hours · 28 videos reviewed · ~9 creators · 2 new reviewers.**
2. **What's new** — the **4K auto-check (AppScript) is now live** (built + tested with the dev
   team), closing last week's flagged gap; and **2 new reviewers** onboarded and trained.
   - **Under the hood** — the real `4KVideoChecker` logic (reads each video's width/height →
     PASS/FAIL) and a representative check **log** (resolution → PASS/FAIL) are shown on screen,
     rebuilt as clean native graphics from the AppScript screenshots (name-free).
3. **Where the time went** — review→approval 9h · 4K auto-check build & test 6h · onboarding 4h · revisions & coordination 3h.
4. **Review outcomes** — 24 cleared for approval; 4 sent back (not in 4K), followed up by mail.
5. **Quality exceptions** — 4 not-4K; 1 non-standard project name (cleared to upload); code tracked per project — lighter than last week, by design.
6. **Next week** — extend the auto-check to the watermark; ramp the new reviewers onto live videos.

Every video count is exact from the week's task log (see `../FACTCHECK.md`); the 22-hour figure
is a self-reported allocation (≥ 21h). The referenced AppScript screenshot wasn't received, so
the film states only that the check works — no result numbers are shown.

## Branding & privacy

- **@HumanitariansAI** in the intro composer, a corner watermark throughout, and the outro card.
- **No personal names** anywhere — only counts and activity types.

## Source

- `../beat_sheet.json`, `../FACTCHECK.md`, `../SOURCES.md`, `../SHOTLIST.md`, `../FRICTIONAL.md`, `../vertical/`
