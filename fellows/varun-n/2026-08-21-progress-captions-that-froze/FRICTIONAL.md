# Frictional Log -- Week 3: Captions That Froze

## Entry: 2026-09-30

**What I was working on:** Week 3 (August 15-21, 2026): adding a 9:16 Shorts version (subtitled, title at start, under 3 min) alongside the 16:9 long-form.

**What I tried, and what I expected:** 08-17: one script now renders both orientations (detected from pixel dimensions); portrait title card and burned-in captions; title overflow fixed; font chosen (Open Sans, captions at 0.925 height).

**Where it resisted, and what I did next:** Captions froze at 0:23 and drifted out of sync. Cause: Manim's frozen-frame optimization skips updaters during long waits. Fix: frozen_frame=False plus a precomputed caption schedule.

**What Claude contributed, and what I accepted, changed or rejected:** Claude Code diagnosed the Manim internals bug and built the dual-orientation logic; I found the sync bug by watching and chose font and position.

**What I understand now, and what I still don't:** Still unclear: not recorded.
