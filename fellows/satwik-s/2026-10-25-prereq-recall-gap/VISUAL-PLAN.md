# VISUAL-PLAN — "The Links That Weren't There" (week-13)

AI-explainer (`claude-hai`), 1920×1080, 30fps. Audio-first; pure `useP()`. **PROOF: framework-first** (B01 the
named failure mode before the counts). Two-skin. Grounded only in `sources/`, reconciled in FACT-CHECK.md.

## Palette contract
| Where | Palette |
|---|---|
| UI beats B00/B09 | **claude** (cream, warm ink, terracotta) |
| Body beats B01–B08 | **humanitarians** (CREAM, INK, TEAL, CRIMSON, SLATE, GOLD, SAGE) |

**CRIMSON = the gap / under-connected / dead-end; GOLD = the method; SLATE = diagnosis / scale; TEAL = recovered / fixed; SAGE = prevention.** (Consistent across body beats.)

## Components (B01–B08 net-new; `Week13RecallGap.tsx`)
| Beat | Pattern | Accent | What's shown (real, sourced) |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | terracotta | the ask; 3 result lines (failure mode / 13 of 19 / 146-proposal fix) |
| B01 | `KnownFailure` | CRIMSON + SLATE | **recall problem + generality bias** — before the counts |
| B02 | `Diagnosis` | SLATE / CRIMSON | ruled out (reduction; "fewer later") + two failures (mis-tier, missing) |
| B03 | `GapChart` | SLATE/CRIMSON/TEAL | bar chart: required cross-chapter prereqs per chapter; floor=2 |
| B04 | `WhyItHappened` | SLATE | four root causes |
| B05 | `ContentMethod` | GOLD | concept → home chapter → credit by specificity; the Warburg→Metabolism example |
| B06 | `ThreeIterations` | CRIMSON→TEAL | v1 ✗ · v2 ✗ · v3 ✓ + sibling-contamination fix |
| B07 | `TheResult` | TEAL | 146 (127/10/9) · 13→0 · Ch23 recovers Metabolism + Principles of Therapy |
| B08 | `PreventionBoundary` | SAGE / CRIMSON | gap-check (25 issues) vs proposal-not-approved (+ TME still missed) + stamp |
| B09 | `ClaudeTitleOutro` | terracotta | title + handle + sign-off |

## Per-beat show design
- **B01:** two cards — THE RECALL PROBLEM (CRIMSON) and THE GENERALITY BIAS (SLATE), each gloss + behavior; a citation line; a rule band.
- **B02:** a "ruled out" strip (two struck items: the reduction; "fewer later" 1.82 vs 1.67) then two CRIMSON failure cards (mis-tiering, missing edges).
- **B03:** a 38-bar chart; foundational (1-19) SLATE, applied under-connected (0-1) CRIMSON, applied OK (≥2) TEAL; a dashed coverage-floor line at 2; caption "13 of the 19 applied chapters: 0-1 required."
- **B04:** four stacked cause rows (chunked authoring / over-strict required / lexical vs conceptual / integrative).
- **B05:** a 3-chip chain (a concept the chapter uses → its home chapter → credit it, by specificity), GOLD accent, with the real Warburg→Metabolism(Ch11)→required example + a reproducibility note.
- **B06:** three version rows (v1 raw overlap ✗, v2 specificity ✗, v3 concentration-home ✓) + a fix band (restrict to foundational half).
- **B07:** stat cards (146 / 127 add / 10 promote / 9 exists) + a big 13→0 + the Ch23 recovery rows (Metabolism required·added; Principles of Therapy required·promoted) + "a proposal, for faculty."
- **B08:** two columns — PREVENTION (SAGE ✓: gap-check, 25 issues, gates build) vs STILL A PROPOSAL (CRIMSON ✗: needs_review, faculty set tier; the TME still missed) + stamp "A REVIEWABLE PROPOSAL — NOT APPLIED · FACULTY DECIDE THE TIER."

## PROOF production gate (binding at QC)
1. Legible at assertion (the chart; 1.82 vs 1.67; 13; 146/127/10/9; 13→0; Ch23 rows; 25 issues; held ≥2s). 2. Framework-first (B01 before counts). 3. Side-by-side (B02 ruled-out vs failures; B06 fail vs work; B08 prevention vs proposal). 4. Caveats shown (B08). 5. Sources on screen (every figure traces to `sources/`; fact-checked). 6. The fix never framed as approved; the TME is shown as missed, never as recovered. 7. Colors consistent.

## Render + assembly (binding)
- **Render:** `TMPDIR/TEMP/TMP=d:/_remotion_tmp`, `ART_REMOTION_SCALE=2`. **Free RAM first (close apps)** — last week's 25s Chrome-connect failures were caused by memory pressure. Concurrency 1 under low RAM; top up with `--only BXX`; last resort direct `npx remotion render`.
- **Assembly:** BOTH video and audio via the concat **FILTER**. Verify the **video stream** duration + volumedetect ≈ −20 dB.

## QC (under PYTHONUTF8=1)
Sample settled frames → rubric + two-skin + production gate + no-source-no-verdict + audio present + **video
full length**. Confirm B01 failure mode before counts; B03 the chart; B06 the three iterations; B07 the result;
B08 the proposal/boundary; colors consistent; the fix never framed as approved; no learning-outcome claim; the
"11 of 21" and TME-for-Ch23 claims are absent (per FACT-CHECK.md). Log to `_qc/REPORT.md`.
