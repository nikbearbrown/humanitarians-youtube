# FRICTIONAL - This Week: Written, Made, Saved, Planned (weekly recap)

**Built and delivered 2026-11-13.** Written from the build record in this folder (CHECKS-REPORT.md, FACTCHECK.md, beat_sheet.json) and the build session. Append your own entries below; do not rewrite earlier ones.

## What was tried and expected

- Asked for a "CLI Explainer" weekly recap (1-3 minutes, no longer than 3), opening with "Hi, I'm Agrima", in four parts: the Substack article "Real Art, New Light", four video files from two videos in two formats, files pushed to GitHub, and the CatBot and DogBot proposal as an early-stage plan (about 40 seconds). Hard limits: do not say the demo is built, do not say any shelter has agreed. Professional, polite and simple, a real update and not overhyped. Built on a real script (v1) revised into v2, both actually run so the on-screen output is real.

## Where it resisted, and what was done next

- **The honest revision:** earlier weeks added roles or statuses like "ongoing". This week the fourth part is a plan, so v2 adds a status to each part (published, produced, saved, planning) and prints "3 parts done, 1 in planning", which keeps the plan visible without calling it finished.
- **The 40-second target:** the CatBot and DogBot part needed two beats (the idea and first step, then what comes next). The first cut measured 46.3 s; one trim (dropping "before it goes out" and rewording the photo-days line) brought it to 44.1 s. I stopped there rather than drop details you listed, and disclosed the 4-second overshoot in CHECKS-REPORT.md.
- **Keeping the hard limits visible:** the section carries an "Early-stage plan" label in both beats, the next steps carry "planned" tags, and the map is labeled "generic map -- not to scale", so nothing on screen can be read as built or agreed.
- **Static-check failure:** the two new-project scenes failed the "shapes never change" check at first because everything was revealed by changing opacity; I switched them to plain fade-ins.
- **Layout:** previews showed the "made with Brutalist" chip running into the B05 heading, the B07 bottom row's cards touching, the CatBot and DogBot labels at different heights and the B08 subtitle crowding the heading. After the full render, the frame check then flagged two blocking edge-bleed defects in B08 (the left cards crossed the safe edge); I narrowed them, re-rendered that scene and re-encoded.
- **Pipeline stalls:** the render script stopped once after the scene clips and the composer step needed a re-run; the next runs used a tracked background job so they could not be cut off.

## What Claude contributed, and what Agrima decided

- Claude: the two scripts and their real output, the beat sheet, eight scenes in 16:9 and eight in 9:16, timing to the narration, the paperwork and the fixes above.
- Agrima: the four parts, the early-stage-plan framing and its two hard limits, the illustrated-only visuals (cat, dog, generic map) and the no-logos rule. Accepted as written.

## What is understood, and what is still open

- Every item is Agrima's own account; none was verified.
- The video says her files were pushed to GitHub; when it was built, this week's new files had not yet been pushed from this toolkit.
- The CatBot and DogBot description comes from the proposal as Agrima summarized it; the video adds nothing to it.
- The frame check still lists "content fills too little of the screen" notes; accepted since there are no blocking defects.
- Pushed to GitHub with this log (code and paperwork only, no video).

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
