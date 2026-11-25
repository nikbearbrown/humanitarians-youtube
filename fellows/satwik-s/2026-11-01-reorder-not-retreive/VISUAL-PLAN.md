# VISUAL-PLAN — "Reordering, Not Retrieval" (week-14)

AI-explainer (`claude-hai`), 1920×1080, 30fps. Audio-first; pure `useP()`. **PROOF: framework-first** (B01 two
arms + B02 metrics before any number). Two-skin. Grounded only in `sources/`, verified in FACT-CHECK.md.

## Palette contract
| Where | Palette |
|---|---|
| UI beats B00/B09 | **claude** (cream, warm ink, terracotta) |
| Body beats B01–B08 | **humanitarians** (CREAM, INK, TEAL, CRIMSON, SLATE, GOLD, SAGE) |

**CRIMSON = retrieval / broken order; TEAL = graph method / zero violations; SLATE = insertion / scale; GOLD = the reorder (Kendall tau); SAGE = robustness.** (Consistent across body beats.)

## Components (B01–B08 net-new; `Week14Reorder.tsx`)
| Beat | Pattern | Accent | What's shown (real, sourced) |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | terracotta | the ask; 3 result lines (two arms / 34·31 + breaks 0 / reshuffle + robust) |
| B01 | `TwoArms` | CRIMSON / TEAL | retrieval vs method — only difference is the graph |
| B02 | `FourMetrics` | SLATE/CRIMSON/GOLD/TEAL | the four metrics, before any number |
| B03 | `Insertion` | SLATE | 34 / 31 prerequisite sections inserted + the foundations |
| B04 | `OrderBroken` | CRIMSON / TEAL | the figure: retrieval 20/14 broken (17/12 + 3/2) vs method 0/0 |
| B05 | `ReorderTau` | GOLD | Kendall tau −0.44 / 0.00 + overturns week 5 |
| B06 | `Personalizes` | TEAL / SLATE | core Jaccard 0.25 vs 0.615 with foundations |
| B07 | `Robust` | SAGE | K-sweep table {10,20,30}; method 0 at every K |
| B08 | `AblationHonestBoundary` | SAGE / CRIMSON | measured+swept vs the limits (embedder, draft edges) + stamp |
| B09 | `ClaudeTitleOutro` | terracotta | title + handle + sign-off |

## Per-beat show design
- **B01:** two cards — RETRIEVAL (CRIMSON: top-K by similarity) vs METHOD (TEAL: core + prereq closure, topo sort) — + a rule band "only difference is the graph."
- **B02:** four numbered metric cards (insertion SLATE, broken deps CRIMSON, reordering GOLD, personalization TEAL) + a note "reachability and order, not just overlap."
- **B03:** two big SLATE stat numbers (34 LNP-siRNA / 31 photothermal) + a caption + a short list of inserted foundation sections (CH01…) + the "nanoparticle delivery ≠ cell cycle" note.
- **B04:** the figure — two project groups, each a tall CRIMSON "retrieval" bar (20 / 14) next to a flat TEAL "method = 0" marker; decomposition label (missing 17/12 + mis-ordered 3/2); a baseline.
- **B05:** a Kendall-tau scale (−1 reversed … 0 unrelated … +1 same) with two markers at −0.44 (LNP-siRNA) and 0.00 (photothermal), GOLD; an "overturns week 5" band.
- **B06:** two Jaccard figures (0.25 core focus / 0.615 with shared foundations) + the "different frontiers, shared groundwork" point.
- **B07:** a 3-column (K=10/20/30) × 3-row (method breaks / graph inserts / Kendall tau) table, SAGE header; a subnote that photothermal holds too; "the effect is the structure, not the setting."
- **B08:** two columns — MEASURED (SAGE ✓: measured+swept, structural not tuned) vs THE LIMITS (CRIMSON ✗: general embedder, draft edges) + stamp "MEASURES THE MECHANISM — NOT APPROVED CONTENT · NO LEARNING CLAIM."

## PROOF production gate (binding at QC)
1. Legible at assertion (34/31; 20/14 + 0/0; −0.44/0.00; 0.25/0.615; the K-sweep; held ≥2s). 2. Framework-first (B01–B02 before numbers). 3. Side-by-side (B01 retrieval vs method; B04 retrieval vs method bars; B08 measured vs limits). 4. Caveats shown (B08). 5. Sources on screen (every figure traces to the JSON). 6. Draft edges never framed as approved; no learning claim. 7. Colors consistent.

## Render + assembly (binding)
- **Render:** `TMPDIR/TEMP/TMP=d:/_remotion_tmp`, `ART_REMOTION_SCALE=2`. **Free RAM first (close apps)** — the week-12/13 renders failed repeatedly on the 25s Chrome connect under memory pressure. Concurrency 1 under low RAM; top up with `--only BXX`; last resort direct `npx remotion render`.
- **Assembly:** BOTH video and audio via the concat **FILTER**. Verify the **video stream** duration + volumedetect ≈ −20 dB.

## QC (under PYTHONUTF8=1)
Sample settled frames → rubric + two-skin + production gate + no-source-no-verdict + audio present + **video
full length**. Confirm B01 two arms; B02 metrics before numbers; B04 the figure (retrieval tall, method 0);
B05 the tau reorder + overturns-week-5; B07 the K-sweep; B08 the limits; colors consistent; draft edges never
approved; no learning claim. Log to `_qc/REPORT.md`.
