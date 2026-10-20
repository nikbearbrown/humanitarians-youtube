# VISUAL-PLAN — "Match It, Prove It, Skip It" (week-12)

AI-explainer (`claude-hai`), 1920×1080, 30fps. Audio-first; pure `useP()`. **PROOF: framework-first** (B01
the three properties before any count). Two-skin. Grounded only in `sources/`.

## Palette contract

| Where | Palette |
|---|---|
| UI beats B00/B08/B09 | **claude** (cream, warm ink, terracotta) |
| Body beats B01–B07 | **humanitarians** (CREAM, INK, TEAL, CRIMSON, SLATE, GOLD, SAGE) |

**TEAL = pass / advance; GOLD = the scoring method / key example; SLATE = scale / counts / opt-out;
SAGE = built / live; CRIMSON = draft / caveats / malformed / miss.** (Colors consistent across body beats.)

## Components (B01–B07 net-new; `Week12Matching.tsx`)

| Beat | Pattern | Accent | What's shown (real, sourced) |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | terracotta | the ask; 3 result lines (formative check / method / 0 skipped) |
| B01 | `ThreeProperties` | SLATE+TEAL+SAGE | **opt-in / can advance / never graded** — before any count |
| B02 | `DroppedType` | CRIMSON | a matching question = a mapping (4 prompt→option rows); 186 skipped stamp |
| B03 | `ScoringMethod` | GOLD | s = correct/prompts; worked 3/4 = 0.75; bar 0.75 vs ~4% chance |
| B04 | `BijectionSubtlety` | TEAL / GOLD | 157 bijection (0.75 = perfect) vs 22 distractor (genuine partial) |
| B05 | `InTheGate` | TEAL/CRIMSON/SLATE | 4/4 advance · 2/4 remediate · opt-out hold; knowledge_check stamp |
| B06 | `PassVsMiss` | TEAL / CRIMSON | two self-check screens: pass 4/4 (green) vs miss 2/4 (red); 0 skipped note |
| B07 | `MatchingHonestBoundary` | SAGE built / CRIMSON draft | built+tested vs draft (0.75 default, 8 recovered) + stamp |
| B08 | `ClaudeComposerAsk` | terracotta | "Your turn." — score by parts → inform not grade → recover don't discard |
| B09 | `ClaudeTitleOutro` | terracotta | title + handle + sign-off |

## Per-beat show design
- **B01:** three property cards (OPT-IN · SLATE; CAN ADVANCE · TEAL; NEVER GRADED · SAGE), each gloss + behavior, then a rule band "It can move you forward — but it is never a grade."
- **B02:** a matching card (stem + 4 prompt→option rows with connector dots/arrows), then a CRIMSON stat band "186 skipped" + the point that a single-answer gate can't read a four-link mapping.
- **B03:** the method name + a formula chip `s = correct pairs / prompts`, a worked example `3 of 4 → 0.75`, and two small stat chips (bar 0.75 vs ~4% chance), GOLD accent.
- **B04:** two cards — **4×4 BIJECTION** (157, TEAL: can't miss one → 0.75 = perfect) vs **SPARE DISTRACTOR** (22, GOLD: genuine partial like 2/3) — point "named, not hidden."
- **B05:** three outcome rows — `4/4 → advance` (TEAL), `2/4 → remediate` (CRIMSON), `opted out → hold` (SLATE), each with a detail; a stamp strip "every result recorded as a knowledge-check — never a grade."
- **B06:** two window-chrome mini-screens of the self-check — PASS 4/4 (green rows, "skip this and what it builds on") vs MISS 2/4 (two red rows, "keep this in your plan"); footer "per-pair feedback + explanation + Continue · 0 skipped (was 186)."
- **B07:** two columns — **BUILT + TESTED** (SAGE ✓: 62 tests, 178 live, 0 skipped) vs **STILL A DRAFT** (CRIMSON ✗: 0.75 default; 8 malformed recovered & set aside → needs Evin) + crimson stamp "BUILT & TESTED — NOT YET VERIFIED · NEEDS FACULTY."

## PROOF production gate (binding at QC)
1. Legible at assertion (186→0, s=correct/prompts, 0.75 vs ~4%, 157/22, the gate rows, the two demo screens, held ≥2s). 2. Framework-first (B01 before counts). 3. Side-by-side (B04 bijection vs distractor; B06 pass vs miss; B07 built vs draft). 4. Caveats shown (B07). 5. Sources on screen (every figure traces to `sources/`). 6. A formative check never framed as a grade. 7. Colors consistent (TEAL pass / GOLD method / SLATE scale / SAGE built / CRIMSON draft).

## Render + assembly (binding)
- **Render:** `TMPDIR/TEMP/TMP=d:/_remotion_tmp`, `ART_REMOTION_SCALE=2`, concurrency 2 (low RAM); top up transient Chrome timeouts with `--only BXX` at concurrency 1; last resort `npx remotion render ... --timeout=120000`.
- **Assembly:** BOTH video and audio via the concat **FILTER**. Verify the **video stream** duration + volumedetect ≈ −20 dB.

## QC (under PYTHONUTF8=1)
Sample settled frames → rubric + two-skin + production gate + no-source-no-verdict + audio present + **video
full length**. Confirm B01 three properties before counts; B02 the mapping + 186; B03 the formula + 0.75 vs
~4%; B04 157 vs 22; B05 the three gate rows + knowledge-check; B06 pass vs miss + 0 skipped; B07 built vs
draft + stamp; colors consistent; nothing frames a formative check as a grade or claims a learning gain.
Log to `_qc/REPORT.md`.
