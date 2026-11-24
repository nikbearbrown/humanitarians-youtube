# Attention, One Head at a Time — one attention head on a four-word sentence, worked with real numbers

**Week:** 25–31 Oct (Drive Week 1) · logged 2026-11-24

**Project:** STEM AI explainer series

**Toolkit:** brutalist.art

- **Drive:** https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `tldr-attention.mp4` (16:9, 4:21)

## What this film is for

The cold open asks how a transformer lets each word use the words around it, with no hype and one attention head with real numbers. The film follows "chase" in "cats chase small dogs": it lands somewhere new when cats is swapped for kids, although its own numbers have not changed. The body shows why — a weighted mix of value points, weighted by how well a request matches each offer — then names query, key and value, reads the equation term by term, and ends on the limit: attention alone can't tell who chased whom.

## What was built

| Part | What it does |
|---|---|
| Script and narration | 15 beats in `beat_sheet.json` (via `make_sheet.py`), Kokoro `am_onyx`, $0. Whisper diff on every beat; `align.py` wrote `mp3/words.json`. |
| B00 `ClaudeComposerAsk` | Cold open: "Hello, Liam", the ask types in, three answer lines (the mix, chase's 0.53 on cats, the word-order limit). |
| B01 `BrutalistHesitantWriter` | "picks the one word it needs" corrected to "blends every word around it"; fontSize 145, lineSpacing 3.3, lead 0.8 s. |
| `B10_ChaseMoves` | Chase's dot lands, then moves when cats → kids; two ghost landings. |
| `B11_MixingPoints` | A blend dot sweeps along a segment, then glides inside the hull of four value points. |
| `B12_RequestMeetsOffer` | Chase's request docks on each offer; products become scores (3, 2, −1, −1); the asker changes to small. |
| `B13_EqualWeights` | The shortcut: equal weights collapse all four words onto one point. |
| `B14_HeatMap` | Score grid → ÷ 2 → softmax heat map; predict hold. |
| `B15_LetTheMatchMix` | Heat-map weights move chase's dot onto B10's landing. |
| `B16_NameIt` | Request, offer, point → Q, K, V grids → softmax(QKᵀ/√d_k)V. |
| `B17_Tangent` | The equation read zone by zone with a box spotlight, chase's row worked, and why the division is there. |
| `B18_Payoff` | B10's dot with pull lines; the cats → kids swap replayed with re-weighting. |
| `B19_OrderBlind` | Reordered sentence: heat-map cells permute, outputs stay still; a position signal moves cats. |
| Remotion bookends | BVDT `ClaudeVerdictArtifact` (6 lines), BHTF `ClaudeComposerAsk` (prompt plus three checks), BOUT `ClaudeTitleOutro`. |
| Evidence demo | `demo/attention_demo.py` (numpy, seed 290537) writes `demo/evidence.json` and `demo/RUN-LOG.txt`; `scenes.py` and `make_sheet.py` take every number from it. |

## Results

| Measure | Value |
|---|---|
| Master | 3840×2160, 24 fps, h264, yuv420p, 261.0 s (4:21) — MASTERCHECK PASS |
| Slots | 15/15 filled: 10 Manim, 5 Remotion/bookend video |
| GATE V | 30 frames, BLOCKER 0, MAJOR 0 |
| GATE T | PASS, 15 beats, 0 FAILs; one §8.10 advisory (BVDT narration recites the card, 0.84) |
| Bookend check | PASS |
| Label / bottom-strip check | PASS — 131 frames sampled every 2.0 s; label corner and bottom band max off-background 0.000, 0 hits |
| Loudness | PASS — −24.72 LUFS integrated (window −28 to −18), true peak −2.98 dBTP (ceiling −1.0); every narration beat has audio |
| Hand QC | All 15 beats checked; clean |
| Checksum | sha256 `cfeaaee78f194ab8…` matches `.verified.json` (`ready`) |

## Problems found by running it

1. **The renderer has no hold field.** `compile.py` sizes each beat from its measured audio; `lead_silence_s` / `tail_silence_s` were not read anywhere. → The main session added `stem-films/tools/pad_silence.py`, which pads the mp3s (BVDT 0.5 s lead, BOUT 1.0 s tail).
1. **A unicode "−" inside a MathTex** `bmatrix` **broke LaTeX** in B16. → Fixed in `scenes.py`.
1. **Frame QC at preview size** found captions crossing the value-plane frame (B11, B12, B19), a values-claim row overflowing and raw "d_k" in B17, weights reading "0.6" (B14, B18, B19), and outputs indistinguishable from values (B19). → Two-line captions, MathTex, two decimals everywhere, hollow output points.
1. **The local GATE V check failed six beats:** underfill on B12, B16, B17 and low contrast on B13, B14, B15, B19. Pale strokes and tints counted as ink and dragged the contrast down. → Structural strokes GHOST → SOFT, tint scale 0.55·w → 0.45·w, early ghost outlines for fill. All 20 samples clean, minimum coverage 0.67.
1. **The 4K build failed GATE T §8.3** on B10, B12, B15, B17: wide terracotta boxes were read as accent text at 2.74:1. → Those boxes became ink; the terracotta moment moved to compact marks. 4K midpoints then measured 7.65–10.02:1.
1. **The rebuild failed §8.6b on B17:** an ink spotlight ring wider than 1.5× its height read as a text run. → `box()` now keeps rings at most 1.4× as wide as tall; every Manim clip was re-rendered.
1. **After the ai-explainer conversion, GATE V failed B01 on underfill** (45% at fontSize 130). → Re-rendered at fontSize 145, lineSpacing 3.3: 59% fill. The old clip is in `_superseded/b01_underfill/`.

## Evidence

- `FACTCHECK.md` — 34 claims; five draft lines corrected (#2, #3, #5, #10, #31).
- `SOURCES.md` — Vaswani et al., "Attention Is All You Need" (NIPS 2017), arXiv:1706.03762, §3.1, §3.2.1, §3.2.2, §3.5.
- `demo/attention_demo.py`, `demo/evidence.json`, `demo/RUN-LOG.txt` — script sha256 `7f79b621…`, evidence sha256 `b48f90c9…`; the reorder check prints "outputs permuted identically = True".
- `exports/landscape/tldr-attention.verified.json` — sha256 of the master and of every input clip and mp3.
- `final.log`, `TYPECHECK.md`, `LOUDNESS.md`, `MASTERCHECK.md`, `_qc/` (Gate B reports, 4K GATE T frames, contact sheets).
- `_superseded/format-tldr/` — the retired TL;DR B00–B03.
- Drive: https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE (Drive copy to be replaced with the clean master)
