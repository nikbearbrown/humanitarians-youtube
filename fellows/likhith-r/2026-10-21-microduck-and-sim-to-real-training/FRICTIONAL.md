# Frictional Log — Microduck and Sim-to-Real Training

> Append dated entries as you go; never rewrite an earlier one.

## 2026-10-21 — Build a 60-second explainer on Microduck and sim-to-real training, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I gave eight points, from the keynote moment to sim-first becoming the standard, and expected the story to be that simulation now transfers cleanly. I wanted the training numbers on screen to come from code, so a small seeded simulation produced the fall counts.

- **Where it resisted, and what I did next:**
  The fact-check corrected several of my points: the robot trains on slopes, stairs and rough terrain rather than obstacles, Isaac Lab is one path rather than the only one, and the on-stage falls have no known cause. A toy "real transfer" result looked too clean, so it was removed instead of tuned. The drawn duck also kept being read as text by the type check, so it was redrawn.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, built a reusable drawn duck and the scenes, checked the claims against Pollen's pages and the coverage, ran the toy simulation, and fixed the layout and type-check issues. I accepted the corrections to my brief, and the change to "becoming the standard" instead of "is".

- **What I understand now, and what I still do not:**
  I understand why simulation makes practice cheap and why the transfer still isn't perfect. I don't know what actually made the ducks fall on stage, and I haven't run the real training stack.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
