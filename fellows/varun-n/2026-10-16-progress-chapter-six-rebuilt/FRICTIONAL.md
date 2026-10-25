# Frictional Log -- Week 11: Chapter Six Rebuilt

## Entry: 2026-10-24

**What I was working on:** Week 11 (October 10-16, 2026): putting the approved intro and outro into the pipeline and rebuilding chapter 6.

**What I tried, and what I expected:** 10-15: supplied the final intro and outro clips (4 files: 9:16 and 16:9, native 4K, 24 fps; intro 3.0 s, outro 4.83 s). Decisions: use them for future Shorts only; long-forms get no intro or outro. Then: continue with chapter 6. Rebuilt centripetal-friction, static-friction and terminal-velocity in the approved format; medhavy_common.py brought up to the approved format (PT Sans 15 pt, question_card(), no separate title card, crisp_text()).

**Where it resisted, and what I did next:** Centripetal friction: narration drifted about 4.5 s out of sync, a car clipped at the frame edge, a label was left behind. Static friction: the legend labels ran together and a needle poked through a label. Terminal velocity: labels sat over afterimages. Small text still broke words, which led to the crisp_text() helper.

**What Claude contributed, and what I accepted, changed or rejected:** Claude Code rebuilt the three videos and fixed the defects, then checked the static-friction legend and the centripetal short's question card and seams. I decided where the intro and outro apply and told it to continue with chapter 6.

**What I understand now, and what I still don't:** Still open: the remaining concepts (21 at the time of the next count) and the ball-and-feather long-form. Next: build all remaining videos.
