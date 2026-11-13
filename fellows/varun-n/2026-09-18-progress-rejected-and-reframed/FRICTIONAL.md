# Frictional Log -- Week 7: Rejected and Reframed

## Entry: 2026-09-30

**What I was working on:** Week 7 (September 12-18, 2026): finishing chapter 6, then responding to a faculty-reviewer rejection of all shorts by rebuilding one short in a new format.

**What I tried, and what I expected:** 09-14: outro added (letterbox rejected as not clean; center-crop approved; blur-fill dropped for a visible seam). Shared module medhavy_common.py created to cut build time. Chapter 6 built (centripetal-friction, static-friction, terminal-velocity); overlaps at 0:51 and 1:34 and a wrong background fixed. 09-17: reviewer feedback -- disjointed transitions, text overlaps, missing title; each video should be a question answered by the video. Rebuilt ball-and-feather: question beat B00Q, opaque label backings, one title/question card, real crossfades. Old ch.3-6 renders deleted (scripts kept).

**Where it resisted, and what I did next:** A QC report claimed the static-friction fix was done when it wasn't -- caught by watching. Agents stopped mid-render repeatedly. self.time doesn't exist in this Manim version (use self.renderer.time). Intro/outro resolution mismatch broke concatenation. Brutalist's explainer skills were reviewed; none fit the format.

**What Claude contributed, and what I accepted, changed or rejected:** Claude Code built ch.6, the module, the outro crop and the new sample. I rejected the letterbox and the false QC claim and scoped the rebuild to one short.

**What I understand now, and what I still don't:** Still unclear: not recorded. Next: get the new format approved.
