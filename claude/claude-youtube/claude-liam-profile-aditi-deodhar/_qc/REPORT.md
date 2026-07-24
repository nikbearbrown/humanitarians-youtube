# Visual QC Report — claude-liam-profile-aditi-deodhar

**Date**: 2026-07-17  
**Cut**: previz / review cut  
**Duration**: 279.6 s (~4:40)  
**Frame sample**: 140 frames at 0.5 fps + beat-boundary spot checks

## 8-Point Rubric Results

| Check | Result | Notes |
|---|---|---|
| Edge bleed / clipping | PASS | All content within frame bounds |
| Title-safe margins | PASS | Eyebrows, chips, and spark lines sit inside 5% inset |
| Container overflow | PASS | Card text wraps correctly in all beats |
| Collision | PASS | No overlapping elements in any beat |
| Offscreen anchors | PASS | All positioned elements resolve on-screen |
| Legibility | PASS | All text readable at 1080p; font sizes scale correctly |
| Brand bug placement | PASS | @HumanitariansAI folder chip renders in B00 and B09; outro shows handle |
| Aspect ratio | PASS | 1920×1080 16:9 confirmed |

## Beat-Level Findings

| Beat | Scene | Finding | Severity |
|---|---|---|---|
| B00 | ClaudeComposerAsk | "Hei, Kore" greeting, correct. @HumanitariansAI chip visible. | PASS |
| B01 | ProfileAditiFig1Pivot | Fork timeline renders cleanly — green stem → THE PIVOT badge → dashed grey arm + terracotta arm → FinFluent label. User question bubble animates in. | PASS |
| B02 | ProfileAditiFig2Stack | Constraint chip + arrow + "Her Own Machine" boundary box + 4-layer stack assembly all correct. | PASS |
| B03 | ProfileAditiFig3Builds | 4-card grid, FinFluent highlighted terracotta. Award badges (2nd·Confluent AI Day 2025, DreamAI 2025 finalist) visible. | PASS |
| B04 | ProfileAditiFig4Community | Network nodes + edges render; "invisible until it's absent" quote in terracotta appears at mid-beat; 4 right-side chips correct. Fray state visible when facilitator node removed. | PASS |
| B05 | ProfileAditiFig5Record | 3.717 center badge (terracotta), 5 orbital chips animate in on dashed lines. "held alongside all of the above" subtitle. | PASS |
| B06 | ProfileAditiFig6Quote | FinFluent card correct. 4 trace lines (MediPedia/Jutly/MIT Women's Health/Pitch practice) visible. Direct quote verbatim and correctly attributed. | PASS |
| B07 | ProfileAditiCredit | Name, institution, recognitions correct. Public-presence labels-only (no invented URLs). "Labels only — article names these but provides no handle URLs." disclaimer visible. Article credit correct. | PASS |
| B08 | ClaudeVerdictArtifact | Thesis card full-width. 4 numbered lines correct and match prompt spec. | PASS |
| B09 | ClaudeComposerAsk | "Your turn." greeting. Full Your Turn prompt in composer (verbatim from spec). @HumanitariansAI chip. | PASS |
| B10 | ClaudeTitleOutro | "The Cost of the Pivot." with terracotta period. @HumanitariansAI handle. "Humanitarians AI Fellows Series" subline. | PASS |

## Motion histogram warning (from compiler)

All 11 beats use `fade` transition (100%). The compiler warns >40% pantry cap. This is expected: the `fade` refers to the *beat transition* declared in the beat sheet, not the internal motion of each scene — each Remotion component has its own spring-animated motion (stems, nodes, cards, orbits, etc.). Not a visual defect.

## BLOCKER defects: 0  
## MAJOR defects: 0  
## MINOR defects: 0

**Status: READY FOR REVIEW**
