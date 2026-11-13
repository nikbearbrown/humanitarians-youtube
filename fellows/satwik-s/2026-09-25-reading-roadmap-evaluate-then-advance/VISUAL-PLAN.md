# VISUAL-PLAN — "Evaluate, Then Advance" (week-09, Evaluation Pipeline)

AI-explainer (`claude-hai`), 1920×1080, 30fps. Audio-first; pure `useP()`. **PROOF: framework-first** (B01
the rule before any example). Two-skin. Grounded only in `sources/`.

## Palette contract

| Where | Palette |
|---|---|
| UI beats B00/B07/B08/B09 | **claude** (cream, warm ink, terracotta) |
| Body beats B01–B06 | **humanitarians** (CREAM, INK, TEAL, CRIMSON, SLATE, GOLD, SAGE) |

**TEAL = pass / advance / prune; CRIMSON = fail / hold / remediate + the draft caveats; GOLD = the upgrade
(evaluate-don't-assume) + hard emphasis; SAGE = soft / diagnostic; SLATE = the pipeline / scale.**

## Components (B01–B06 net-new; `EvaluationPipeline.tsx`)

| Beat | Pattern | Accent | What's shown (real, sourced) |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | terracotta | the ask; 3 result lines (rule / two learners / scale) |
| B01 | `EvalThreeMoves` | GOLD+TEAL+CRIMSON | **the rule in 3 moves — before any example** |
| B02 | `EvalLoop` | TEAL/CRIMSON | top-down loop: node → connection → prune (pass) / descend (fail) → advance/remediate; cost ∝ gap |
| B03 | `EvaluateDontAssume` | **GOLD** | before (declared knows-list ✗) → now (earned by a pass ✓) |
| B04 | `ItemPools` | SLATE/TEAL | one pool → sample one item per learner; MCQ live / open-ended seam |
| B05 | `TwoLearnersEval` | CRIMSON hold / TEAL advance | STU-A (hold, immunology pass→prune, treatment fail→descend→gap) vs STU-B (advance); counts |
| B06 | `AtScaleBoundary` | SLATE scale / CRIMSON draft | 220/248/536 → 5 items seen (gap Mutations); REAL (engine, MCQ) vs DRAFT (stub items, open seam, faculty) |
| B07 | `ClaudeVerdictArtifact` | terracotta | 5 lines: runs end to end; nothing assumed; descend on fail; measures the gap; MCQ live/rest next |
| B08 | `ClaudeComposerAsk` | terracotta | "Your turn." — test before you trust → prune/descend → one pool → measure the gap |
| B09 | `ClaudeTitleOutro` | terracotta | title + handle + sign-off |

## Per-beat show design

- **B01:** three move-cards (EVALUATE NEVER ASSUME · GOLD; PASS→PRUNE FAIL→DESCEND · TEAL; HARD GATES SOFT DIAGNOSE · CRIMSON) + rule line.
- **B02:** vertical flow — GOAL → grade NODE → grade CONNECTION → [pass] PRUNE subtree (teal) / [fail] DESCEND (crimson) → decision ADVANCE/HOLD; a soft "diagnostic only" side note; bottom point "cost ∝ the gap, not the chain."
- **B03:** two panels — **EARLIER DEMO** (crimson, "pruned against a declared knows-list", ✗) vs **NOW** (gold, "every skip earned by a passing answer", ✓) → point "trust is earned, not declared."
- **B04:** one **POOL** card (several items) → arrows to 3 learner chips each sampling a *different* item → note "one per learner, deterministic, no two identical"; a grading row (MCQ live TEAL / open-ended seam muted).
- **B05:** two panels. **STU-A** (crimson HOLD): immunology PASS→prune, basics-of-treatment FAIL→descend, →what-cancer-is PASS→gap, tumor-microenvironment soft weak → remediate → basics of cancer treatment; counts "6 administered · 2 pruned · closure 6." **STU-B** (teal ADVANCE): both hard PASS→prune → advance; "5 administered · 3 pruned · closure 6." Bottom GOLD line "foundations never tested — the topics above passed."
- **B06:** top scale row (220 concepts · 248 edges · 536 pool, SLATE) + headline "a learner saw 5 of 536 items — gap: Mutations"; then two columns **REAL** (SAGE ✓: engine runs; MCQ grading) vs **DRAFT** (CRIMSON ✗: item text stubs; open-ended off + edges pending faculty) + stamp "THE ENGINE IS REAL — THE QUESTIONS & SIGN-OFF ARE NEXT."

## PROOF production gate (binding at QC)

1. Legible at assertion (counts held ≥2s). 2. Framework-first (B01 before examples). 3. Side-by-side (B03 before/after; B05 hold vs advance). 4. Caveats shown (B06 real-vs-draft). 5. Sources on screen (every figure traces to `sources/`).

## Render + assembly (binding)

- **Render:** `TMPDIR/TEMP/TMP=d:/_remotion_tmp`, `ART_REMOTION_SCALE=2`, concurrency 2 (low RAM); top up transient Chrome timeouts at concurrency 1.
- **Assembly:** BOTH video and audio via the concat **FILTER** (beats span sessions → stream-copy `-c copy` concat silently truncates; demuxer re-encode balloons duration):
  - video: `ffmpeg -i b00.mp4 … -filter_complex "[0:v]…concat=n=N:v=1:a=0[v]" -map "[v]" -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p -r 30 v.mp4`
  - audio: `ffmpeg -i b00.mp3 … -filter_complex "[0:a]…concat=n=N:v=0:a=1[a]" -map "[a]" -c:a aac -b:a 192k a.m4a`
  - mux: `-map 0:v:0 -map 1:a:0 -c copy -shortest +faststart`. **Verify VIDEO stream duration (not just format) + volumedetect ≈ −20 dB.**

## QC (under PYTHONUTF8=1)

Sample settled frames → read PNGs → rubric + two-skin + production gate + no-source-no-verdict + audio present
+ **video full length**: confirm B01 rule before examples; B05 hold vs advance with counts; B06 real-vs-draft;
`→ ✓ ✕ ·` clean; nothing frames stubs as real or claims a learning gain. Log to `_qc/REPORT.md`.
