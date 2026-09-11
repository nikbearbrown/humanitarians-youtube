# VISUAL-PLAN — "Test Before You Advance" (week-07, Test-to-Advance Gate)

AI-explainer (`claude-hai`), 1920×1080, 30fps. Audio-first; pure `useP()`. **PROOF: framework-first**
(B01 the three moves before any file/item/learner); production gate designed in (real figures,
side-by-side, caveats shown). Two-skin contract. Grounded only in `source/test_to_advance_gate.tex`.

## Palette contract (two skins)

| Where | Palette |
|---|---|
| UI beats B00/B07/B08/B09 | **claude** (cream, warm ink, terracotta) — fidelity |
| Body beats B01–B06 | **humanitarians** (CREAM, INK, TEAL, CRIMSON, SLATE, GOLD, SAGE) |

Source-figure colors map to tokens: proc/light-blue → **SLATE**; term/advance/green → **TEAL**;
gate/remediate/pink → **CRIMSON**; side/prune/descend/cream → **GOLD**; soft/diagnostic/grey-dashed →
**SAGE**. **GOLD is reserved for the connection-item idea** (move 1, the key insight). **CRIMSON = the
gate holding / a failed connection / remediate.**

## Components (B01–B06 net-new; `TestToAdvanceGate.tsx`)

| Beat | Pattern | Accent | What's shown (real, sourced) |
|---|---|---|---|
| B00 | `ClaudeComposerAsk` | terracotta | the ask; 3 result lines (three moves / connection / drafts) |
| B01 | `ThreeMoves` | TEAL + GOLD + CRIMSON | **the 3 moves (test the edge / prune + descend / hard-gate soft-diagnose) — before any detail** |
| B02 | `SixFileModel` | SLATE | 4 authored CSVs → engine → 2 derived CSVs; "faculty can open & correct" |
| B03 | `TestTheEdge` | **GOLD** | concept item (node) vs connection item (edge); the false-positive it catches |
| B04 | `PruneDescend` | TEAL | naive-closure → top-down / prune / descend-on-fail; cost ∝ gap near goal (KST) |
| B05 | `TwoLearners` | CRIMSON hold / TEAL advance | STU001 (nodes pass, connection e1 FAIL → hold) vs STU002 (pruned → advance) + counts |
| B06 | `HonestBoundary` | SAGE real / CRIMSON draft | real (engine, deterministic) vs draft (typing, items, needs_review); MC-first / open-ended phase-two |
| B07 | `ClaudeVerdictArtifact` | terracotta | 5 lines: order+gate; test the link; stay short; hard-only; drafts |
| B08 | `ClaudeComposerAsk` | terracotta | "Your turn." — one target → direct hard prereqs → one connection item each → run |
| B09 | `ClaudeTitleOutro` | terracotta | title + handle + sign-off |

## Per-beat show design

- **B00:** "Hello, fellows" + spark → the ask types in → 3 result lines → @HumanitariansAI overlay.
- **B01:** three move-cards land (1→3): **TEST THE EDGE** (GOLD), **PRUNE + DESCEND** (TEAL), **HARD GATES,
  SOFT DIAGNOSE** (CRIMSON/SLATE) → the rule line "test the edge, prune and descend, let hard block and soft report."
- **B02:** 4 authored file-chips (concepts/dependencies/items/students, SLATE) → **engine** pill → 2 derived
  chips (responses/gate_result; gate_result CRIMSON-edged) → footer "every file is a spreadsheet faculty can correct."
- **B03:** two question cards side by side — **CONCEPT ITEM** (node, neutral) vs **CONNECTION ITEM** (edge, GOLD);
  each with its "asks" + example; then the catch strip "ace both endpoints, still fail the connection" →
  GOLD point "knowing two facts ≠ knowing one is built on the other."
- **B04:** a tall dependency chain (naive: every node lit = "100 questions", muted CRIMSON) →
  collapses to **direct prereqs only** (TEAL), one node PRUNED (GOLD, "skip — known"), one FAILED node
  descends one level (CRIMSON) → point "questions ∝ the gap near the goal, not the chain" + KST caption.
- **B05 (falsifiability):** two panels. **STU001** (CRIMSON header GATE HOLD): CH16-S05 node PASS, CH27-S06
  node PASS, **connection e1 FAIL** (CRIMSON), CH10-S04 soft WEAK (SAGE, "diagnostic") → remediate → CH16-S05;
  counts "5 tested · 0 pruned." **STU002** (TEAL header GATE OPEN): CH27-S06 **PRUNED** (GOLD), CH16-S05+e1 ✓,
  e2 ✓ → advance; counts "4 tested · 1 pruned." Bottom GOLD line: "a node-only quiz would have advanced STU001."
- **B06:** two columns — **REAL** (SAGE ✓: engine runs; deterministic grade) vs **DRAFT** (CRIMSON: hard/soft
  typing needs_review; six items llm_proposed, none faculty-approved) → format row: **NOW** multiple-choice
  (TEAL) / **LATER** open-ended → LLM-as-judge vs gold set (muted) → stamp "A WORKING BASELINE — NOT A FINISHED SYSTEM."
- **B07:** artifact page; 5 lines stagger; terracotta on "drafts awaiting faculty."
- **B08:** "Your turn." → the 4-step scaffold types in → 3 output lines → holds.
- **B09:** poster-serif title restate + terracotta period → @HumanitariansAI + full mark → sign-off.

## PROOF production gate (binding at QC)

1. **Legible at assertion:** each figure readable, held ≥2s, at its claim.
2. **Framework-first:** B01 lands the three moves before any file/item/learner.
3. **Side-by-side at comparison:** B03 concept vs connection; B05 STU001 (hold) beside STU002 (advance).
4. **Caveats shown, not just voiced:** B06 (real vs draft; needs_review; none faculty-approved); B07 drafts.
5. **Sources on screen:** every number traces to `source/test_to_advance_gate.tex`.

## Audio assembly (Windows fix — binding)

Build master audio with the **concat FILTER**, not the demuxer:
`ffmpeg -i b00.mp3 … -filter_complex "[0:a][1:a]…concat=n=N:v=0:a=1[a]" -map "[a]" -c:a aac -b:a 192k out.m4a`
then mux `-map 0:v:0 -map 1:a:0 -c copy +faststart`. The concat *demuxer* (`-f concat -c:a aac`) yields a
**SILENT** track from 24 kHz-mono Kokoro mp3s on this ffmpeg build (mean_volume −91 dB). **Verify with
`volumedetect` (mean ≈ −20 dB) before finalizing.** Video: stream-copy concat (`-c copy -fflags +genpts`).

## QC (run under PYTHONUTF8=1)

Sample settled frames → read PNGs → 9-point rubric + two-skin + **PROOF production gate** + no-source-no-verdict
+ **audio present (volumedetect ≈ −20 dB, not −91)**: confirm `·`/`→`/`≠`/`✓` clean; B01 three-moves before any
detail; B03 concept vs connection; B05 STU001 hold beside STU002 advance with counts; B06 real-vs-draft +
needs_review; nothing frames the drafts as approved or claims a learning gain. Log to `_qc/REPORT.md`.
