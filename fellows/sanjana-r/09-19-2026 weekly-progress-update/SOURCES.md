# SOURCES — Two-Week Progress Review

Per the DOUBLE-CHECK LAW: no fabrication. Every on-screen number is computed from
Sanjana's own tracker, "Humanitarians AI Video Reviews.xlsx", sheet
"September Videos", filtered to the two-week window **Sep 6–19, 2026**.

## Derivation (the pandas shown in B04/B07 reproduces these)
- `df.dropna(subset=["Number of Videos reviewed"])`, `Date.between("2026-09-06","2026-09-19")`
- `Number of Videos reviewed`.sum() → **172**
- distinct `Person - ProjectName` → **38 fellows** (39 submission rows)
- group by `Sent for Approval? `:
  - Yes → **119** (uploaded for the Professors to approve)
  - Needs Modifications → **50** (changes requested)
  - No → **3** (blocked)
  - (119 + 50 + 3 = 172 ✓)
- `Code on Github?` == Yes → **146 / 172 ≈ 85%**
- project split (Mycroft vs Other): **Mycroft 77 · Other 95** (= 172 ✓)
- week split (Date < Sep 10 = Week 1):
  - **Week 1 = 87** videos (other projects)
  - **Week 2 = 85** videos (Mycroft 77 + 8 other)
  - (87 + 85 = 172 ✓)

Per the creator's instruction, the reel presents the breakdown by **week**
(Week 1 = 87, Week 2 = 85), not by individual review date. The date window is used
only as the filter mechanism (shown in the code); no per-review calendar dates
appear in the graphics.

## Honesty notes (stated on screen in B09)
- The count is **videos reviewed, not hours worked**.
- "Changes requested" (50) is the quality gate working, not rework waste; it keeps
  turning into "changes made" over the following days (the tracker shows several
  fellows already revised and re-uploaded).
- No individual fellow is named or ranked on screen; the reel reports aggregates.
- No model version numbers or drifting external counts — nothing dates the video.

The dataset is Sanjana's real work log; figures are aggregates of her own entries.
The reel passes its own "no source, no verdict" rule: the generating code (B04, B07)
reads the same sheet the numbers come from.
