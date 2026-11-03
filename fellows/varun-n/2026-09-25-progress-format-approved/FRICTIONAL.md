# Frictional Log -- Week 8: Format Approved

## Entry: 2026-09-30

**What I was working on:** Week 8 (September 19-25, 2026): fixing captions and outro until the format was approved; testing GPU rendering; beginning Medhavy AI channel maintenance.

**What I tried, and what I expected:** 09-21: captions 18 -> 15 pt; in-word gaps traced to Manim/Pango with Open Sans -> switched to PT Sans. Supplied "4K" outro was actually 478x850 -> upscaled. 09-22: assigned Medhavy AI YouTube channel maintenance by faculty reviewers; about ten videos unlisted as not explainer-style (my count). 09-25: format approved by faculty reviewers. 09-25 GPU test: RTX 5050 visible in WSL; NVENC encodes ~2x faster; Manim OpenGL ~23% slower than Cairo -> renderer not switched. Pedagogy research.

**Where it resisted, and what I did next:** Font rendering bug; a mislabeled studio file (lesson: check with ffprobe, not filenames); GPU expected to help and didn't for Manim.

**What Claude contributed, and what I accepted, changed or rejected:** Claude Code made the font comparison, resolution check and benchmarks. I spotted caption gaps, picked the font, made the GPU call, and did the unlisting.

**What I understand now, and what I still don't:** Still unclear: OpenGL memory behavior inconclusive. Playlists not started. Next: rebuild chapters 4-5 in the approved format; organize channel playlists.
