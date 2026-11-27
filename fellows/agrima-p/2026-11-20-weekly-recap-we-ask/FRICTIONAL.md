# FRICTIONAL - This Week: Written, Made, Synced, Continued (weekly recap)

**Built and delivered 2026-11-24.** Written from the build record in this folder (CHECKS-REPORT.md, FACTCHECK.md, beat_sheet.json) and the build session. Append your own entries below; do not rewrite earlier ones.

## What was tried and expected

- Asked for a "CLI Explainer" weekly recap (about 3 minutes, no longer), opening with "Hi, I'm Agrima", in four parts of roughly 30-40 seconds each: the Substack article "We Ask the AI Now", video production with Brutalist (two videos in two formats, four files), the weekly team meeting, and Homes of Hope (promotion and outreach with Yatra, ongoing, no other detail). Then a short closing line summing up the week. Professional, polite, simple. Visuals: a mock article header with a search bar and chat bubble, a two-videos-by-two-formats graphic, a calendar icon, an abstract outreach graphic. No logos, no photos of children or real people. Built on a real script (v1) revised into v2, both actually run so the on-screen output is real.

## Where it resisted, and what was done next

- **The part lengths:** the brief asked for about 30-40 s per part. Measured: writing 37.9 s, video production 21.6 s, weekly meeting 9.4 s, Homes of Hope 20.1 s. Only the writing part has enough material (the summary) to fill its slot. The other three are shorter because the summaries are two to three sentences and Homes of Hope was to carry no detail beyond "ongoing". I did not pad them; padding is what the revision prompt warns against. Disclosed in CHECKS-REPORT.md.
- **Staying under 3 minutes:** the earlier recaps' PROBLEM beat was dropped so the total (146.1 s, 2:26) stays inside the limit.
- **The honest revision:** v2 adds a status to each part (published, produced, attended, ongoing) and prints "3 parts done, 1 ongoing", so Homes of Hope is visibly not finished.
- **"Two videos, four files":** the wording is kept exact on screen and in narration; it never says "four videos".
- **Layout:** previews showed the "mock article header" caption sitting on the takeaway chip (B03) and the "Supports marginalized girls in India" line touching the three support chips (B06); both were moved. In the 9:16 the cards could not all fit at once, so each part replaces the previous stage (the article card fades out before the summary chips stack, the process chips appear one at a time).
- **Pipeline stalls and a corrupt file:** the render script stopped once after the Manim stage and an interrupted run left a corrupt `clips/master.m4a`; I deleted it and re-ran as a tracked background job.

## What Claude contributed, and what Agrima decided

- Claude: the two scripts and their real output, the beat sheet, six Manim scenes in 16:9 and in 9:16, timing to the narration, the paperwork and the fixes above.
- Agrima: the four parts and their summaries, the "ongoing, no other detail" limit for Homes of Hope, the generic-icon visuals and the no-logos / no-photos rule. Accepted as written.

## What is understood, and what is still open

- Every item is Agrima's own account; none was verified. No outside statistics are used.
- The Homes of Hope description (safe home, education and support for marginalized girls in India) is as Agrima gave it; the video adds nothing to it.
- The frame check lists "content fills too little of the screen" notes on the 16:9 (5) and 9:16 (7); accepted since there are no blocking defects (BLOCKER=0).
- Optional: a screenshot of her own Substack post, with anything personal blurred, could replace the mock article header.
- Pushed to GitHub with this log (code and paperwork only, no video).

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
