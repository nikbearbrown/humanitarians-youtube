# Feedback: "Inkling, Encoder-Free at Scale?" — Ritik B., film 11

PROOF self-review of the beat sheet before audio (PROOF-1), then of the rendered frames (PROOF-2, appended after the render).
Each beat's narration + on-screen props are treated as the frame. Reveal timing comes from the pattern code:
ReelFramework rows fade in at 14% + 11% × row of the beat (fully visible by 32% + 11% × row), keepNote at 76–94%;
BlipLadder bars grow from 11% + 9.5% × bar, the dashed reference at 62–76%, the `exception` caption at 80–94%.

## PROOF-1, round 1 (first draft of the sheet, 12 beats, 351 words, est 2:04)

**Verdict:** unlisted-until-fixed. Teaching 10/12. Production gate FAIL.
"This film attempts a reusable config-first audit of Inkling but delivers it with four voiced claims that aren't on screen
when they're said, and a step 4 that names no result that would break anything."

### Rubric
| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Shown as a structure before the examples | **2** — B01 puts READ / COMPUTE / CHECK / BREAK on screen at ~0:10, before any Inkling fact; every body beat's spark names its step. |
| Reusable rubric | A viewer could apply it to a new case | **2** — four steps + the verified / ambiguous / trust labels; B10 hands the same steps over for any open model. |
| Worked example | One case walked through, reasoning visible | **1** — B05 computes the KV cache, but the per-layer arithmetic sits in BlipLadder's `exception`, which fades in at 80% of the beat while the narration states it in the first half. The viewer sees results before the reasoning. |
| Falsifiability / edge | Stress-tested against a counterexample or ambiguous case | **1** — B07's AMBIGUOUS row (975B stated vs ≈952B implied by the checkpoint) is a real stress test of the three-bin rubric. But step 4 (B08) only lists the lab's caveats; it never names a result that would prove a claim wrong — the step the method promises isn't demonstrated. |
| Active task | A structured CTA, not "ask Claude" | **2** — B10: run the four steps on any open model, with GOOD / FLAG outcomes on screen. |
| Friction | A tension the viewer has to resolve | **2** — B06: the six-fold cache saving is real, yet the weights are 1.9 TB (sparse compute ≠ sparse memory); B07's ambiguous parameter count. |
| **Total** | | **10/12** |

### Production gate — FAIL
- **Legibility at the moment of assertion — FAIL (B05).** "Eight heads × 128 × 2 × 2 bytes × a million" is voiced at 7–45% of the beat; its on-screen version appears at 80%.
- **Sources on screen — FAIL (B00, B06, B09).** B00 voices "975 billion parameters … no separate encoder" with nothing on screen showing it.
  B06 voices "one point nine terabytes" while the bar reads 1904.6 (GB) with no conversion shown. B09 voices "open weights, not open data",
  which is not on the verdict card.
- **Side-by-side at comparison — PASS.** B03 local vs global rows, B05 bars, B07 claim + receipt in one row, all held for the whole beat.

### The problem
B05: the one worked example shows its answer before its reasoning. The method's credibility rests on "compute it from the config", so the arithmetic has to be on screen as it's spoken.

### Do X next
1. [EDIT] B05 → ReelFramework that walks the arithmetic row by row: one layer (8 × 128 × 2 × 2 B × 1,048,576 = 4.29 GB) → all 66 global (283 GB) → Inkling's 11 (47 GB) → the 55 local layers (0.23 GB). Each row is visible before it's voiced.
2. [EDIT] B06 → four bars ordered as narrated (KV all-global, KV Inkling, weights one token uses, all weights), the weights bar sub-labelled "≈ 1.9 TB", narration re-ordered to match the bar schedule, closing line timed to the 80% caption.
3. [EDIT] B08 → add a TEST row: swap each image or clip for noise; if the answers hold, the decoder isn't perceiving. That's step 4 shown, not described. Keep RANK, CONTAMINATION, CHECKPOINT; move DATA to the verdict.
4. [EDIT] B00 → add a `CLAIMS 975B · image + audio · no encoder` output line, so the hook's claims are on screen.
5. [EDIT] B09 → verdict line 4 carries "training data described, not released", so "open weights, not open data" is on screen.
6. [EDIT] Trim B00, B04, B09, B10 so the added words keep the cut near 2:05.

### What works
The method lands first and every body beat is labelled with its step — the viewer always knows which step of the audit they're watching.
The AMBIGUOUS row is the strongest moment: the rubric needed a third bin, and the film shows why with arithmetic.

## PROOF-1, round 2 (after the six [EDIT]s, plus B02 → bar chart for visual variety; 12 beats, 364 words, est 2:09)

**Verdict:** clear to render. Teaching 12/12. Production gate PASS on the sheet (frames checked in PROOF-2).
"This film teaches a four-step config-first audit, shows each step on Inkling with its receipt in the frame, and stress-tests
its own rubric with a claim that is neither verified nor pure trust."

### Rubric
| Criterion | Round 1 | Round 2 | Why |
|---|---|---|---|
| Explicit framework | 2 | **2** | Unchanged: B01 at ~0:08, before any example. |
| Reusable rubric | 2 | **2** | Unchanged; B10 applies it to any open model. |
| Worked example | 1 | **2** | B05 now walks the arithmetic row by row — one layer (4.29 GB) → all-global (283) → Inkling (47) → local (0.23). Each row is fully visible (32/43/54/65% of the beat) before the narration reaches it (≈ 10/55/65/75%). |
| Falsifiability / edge | 1 | **2** | B08 row 1 names the result that would break "the decoder perceives" (noise swap — answers that hold mean it isn't perceiving). B07's AMBIGUOUS row stays as the rubric's own stress case. |
| Active task | 2 | **2** | Unchanged. |
| Friction | 2 | **2** | B06 now puts the saving (283 → 47) and the 1.9 TB of weights on one axis. |
| **Total** | 10 | **12/12** | |

### Production gate — PASS (on the sheet)
- **Legibility at assertion:** every voiced number now has an on-screen element that is visible before or as it's said
  (checked against the reveal schedule for B02 bars, B05 rows, B06 bars; the B06 closing line lands with its 80% caption).
- **Sources on screen:** B00's claims are an output line; B06's bar reads "≈ 1.9 TB"; B09's line 4 carries the licence and the data
  point. Every ReelFramework row that states a number has a receipt; every BlipLadder/ReelFramework beat has a source line.
- **Side-by-side:** B03, B05, B06, B07 — the compared items share the frame for the whole beat.
- Residual risk for PROOF-2: long rows (B05 row 1, B08 rows) wrapping or clipping in 9:16; the B06 bars at 2.4% / 4.1% of the axis
  being too thin to read; the outro title (48 characters) filling ≥ 55% in 9:16.

## PROOF-2 (rendered frames, both cuts — GATE V contact sheets + end frames of every beat)

**Verdict:** ship. Teaching 12/12 holds on the frames. Production gate PASS after two fixes.

- **GATE V:** 0 BLOCKER, 0 MAJOR in 16:9 and 9:16 (24 frames each), before and after the fixes. Masters 127.55 s, identical audio.
- **Found by eye, missed by GATE V (16:9):** two ReelFramework labels wider than the label column ran into their detail text —
  B03 row 4 `CONVOLUTION`, B08 row 3 `CONTAMINATION`. [FIXED] Renamed `CONV` / `LEAKAGE` in both sheets (9:16 was fine but kept
  identical), re-rendered B03 + B08 in both cuts, recompiled, GATE V re-run clean. Rule for the toolkit: labels ≤ 10 characters.
- **Residual risks from round 2, checked:** B05 row 1 (the arithmetic) fits on one line in both cuts and is fully visible before it is
  voiced; B06's thin bars (47.2, 80.8→82.0) read by their value labels, and the 1904.6 bar carries "≈ 1.9 TB"; the 48-character outro
  title fills the frame in 9:16 (breaks at "Encoder-").
- **Legibility at assertion / sources on screen / side-by-side:** confirmed on frames for B00 (claims line), B05, B06, B07, B08, B09.
