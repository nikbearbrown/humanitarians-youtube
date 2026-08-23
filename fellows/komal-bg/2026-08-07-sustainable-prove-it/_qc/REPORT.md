# Visual QC REPORT — Sustainable, Prove It. (Komal cut)

Master: `claude-liam-eu-green-claims.mp4`  
Probe: **3840×2160** · **157.14s** · h264 + aac · no review burn-ins  
Sampled: per-beat ~15/50/85/92% frames under `_qc/frames/` (Read + audited)

## Rubric (9-point)

| Check | Result |
|---|---|
| Edge bleed / clipping | PASS — content inside cream stage |
| Title-safe margins | PASS — spark lines + cards inset |
| Container overflow | PASS after BanList row tighten (5/5 BANNED visible late) |
| Collision | PASS |
| Offscreen anchors | PASS |
| Legibility | PASS — serif/sans contrast on cream |
| Brand bug / beat chips | PASS — **no** bottom-left `B00` review labels; composer footer shows `Komal` by design |
| Aspect | PASS — 16:9 4K |
| Canvas fill | PASS — stacks/cards occupy middle; atmosphere wash present |

## Fixes applied during build
1. **Animation clock:** Remotion comps were 30s; trim cut motion mid-flight. `remotion_scenes.py` now **time-compresses** full renders into the audio window so `useP` reaches 1.
2. BanList row spacing tightened so all five blacklist rows land on screen.
3. `ClaudeTitleOutro` durationInFrames raised to 300 for freeze-pad headroom.

## BLOCKER / MAJOR
None remaining after re-render + recompile.

## Notes
- Pantry-cap warning (100% Remotion) is expected for this ai-explainer; not a defect.
- Spoken sign-off: Liam, in for Komal. Folder chip / outro handle: Komal.
- Never publish from toolkit — human decision.
