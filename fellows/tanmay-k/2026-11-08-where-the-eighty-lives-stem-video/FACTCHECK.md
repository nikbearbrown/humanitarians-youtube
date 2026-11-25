# FACTCHECK — Where the Eighty Lives (long film and Short), 2026-11-08

**Status: every correction below is applied.** The narration lines were re-signed at Gate P (draft 3), the audio, captions and both videos were rebuilt, and the measured checks pass on the rebuilt files. The table shows each claim's verdict and what it was before the correction.

Every claim in the signed narration and on screen, with its verdict and source. Our own numbers come from `MEASUREMENTS.md` (compiled C: `measure_dependency.c`, `measure_scalar.c`, `measure_reuse.c`); the library film's claims come from its folder, `claude-for-computer-science/claude-liam-lstm-ops`, and are attributed on screen as reported there.

Verdicts: **VERIFIED** (derived or measured here), **VERIFIED-LIB** (stated by the library film, attributed, not reproduced), **QUALIFY** (true with a limit the film should state), **CORRECTED** (the figure in the film did not survive the check and was changed).

## What this check found
**Our own comparison was not like for like, and the first numbers were too big.** In the first measurement run the recurrent side evaluated five gate functions per hidden unit per step and the parallel side two. The multiply-add arithmetic was equal; the elementwise work was not. Re-reading the code against the claim "same arithmetic" caught it before anything was published. With the parallel side doing the same five, the headline numbers move:

| | In the first films | Like for like (full step, equal gate work): **now in the films** | Matrix products only |
|---|---|---|---|
| Plain loops (B05, S06) | 6.91 vs 6.73 ms, 1.03x | 6.11 vs 6.37 ms, 0.98x | 6.07 vs 6.01 ms, 1.00x |
| 8 rows per weight load (B06, B07) | 1.40x | 1.34x (1.28 to 1.37) | 1.38x |
| Optimized multiply, 100 steps (B07, S07, S09) | 0.484 vs 0.085 ms, **5.7x** | 0.362 vs 0.098 ms, **3.7x** (2.9 to 3.7 over runs) | about **6.3x** (6.2 to 6.6) |
| Ratio across 25 to 400 steps (B08) | 4.8x to 5.7x | 3.3x to 3.8x | not measured |
| "Most I could make" (B09, S09) | about 6x | about 4x (3.8x at 400 steps) | about 6x |
| Recurrent time, 25 to 400 steps (B08) | 0.09 to 1.5 ms (16x) | 0.090 to 1.454 ms (16.2x): **unchanged** | |

The shape of the result is unchanged and stronger for being tested: nothing to overlap gives 1.0x; weight reuse gives about 1.3x; an optimized multiply gives a few times more; the gap belongs to model and chip together; and it is nowhere near eighty. The size of the optimized-multiply gap depends on whether the gate work (equal on both sides, about half of the recurrent step's time at that speed) is counted. The earlier 5.7x sat near the matrix-only figure by coincidence, and repeats of that first program gave 5.2x to 6.5x.

## Long film
| Beat | Claim | Verdict | Evidence |
|---|---|---|---|
| B00 | A small model runs about eighty times slower than a bigger one. | VERIFIED-LIB | Library film B00 and B03: the LSTM "ran nearly eighty times slower" than the CNN. On screen: its title and "as reported there". Not reproduced. |
| B00 | By its parameter count the small one should be the fast one. | VERIFIED-LIB | Library film: LSTM 0.2M parameters against the CNN's 1.4M. Stated as a heuristic. |
| B01 | We built two tiny models that share the same weights. | VERIFIED | One matrix, 390 by 512 (128 hidden units, 262 inputs, four gates), used by both programs. |
| B01 | "Everything you see comes from my own measurements." | QUALIFY | The title card and "80x" in B00 and the memory-map source in B09 are the library film's, labelled on screen. Our own figures are everything else. |
| B02 | About 200,000 operations per step, one for each weight. | VERIFIED | 4 x 128 x (128 + 262) = 199,680 multiply-adds per step; biases (512) and gate functions not counted. |
| B02 | "That multiplication is the whole cost." | **CORRECTED 2026-11-08** | True of the counted operations. In time it is true only of slow code (scalar loops: gates add about 1%). With the optimized multiply the gate work is about half of the recurrent step (0.19 to 0.30 ms matrix-only against 0.362 ms with gates). Suggest "most of the cost" or "the part we count". |
| B03 | The same block is applied at every position; nothing waits for anything. | VERIFIED | One matrix product over 100 independent rows; for one convolution layer positions do not depend on each other. |
| B04 | A hundred positions is 20 million operations on each side. | VERIFIED | 100 x 199,680 = 19,968,000 for both. |
| B05 | Plain loops, one thing at a time. | QUALIFY | Compiled with vectorisation off; the core still pipelines instructions, so "one thing at a time" is an approximation. |
| B05 | The recurrent model took 6.9 ms, the other 6.7; the same within three percent. | **CORRECTED 2026-11-08** | Like for like: 6.11 vs 6.37 ms (the parallel side 4% slower; range 0.96x to 1.02x). "The same, within about five percent" holds; the figures do not. |
| B05 | With nothing to overlap, the eighty is not there. | VERIFIED | Ratio 1.0x (0.96 to 1.02). |
| B06 | The parallel side loads a weight once for many positions; the recurrent side cannot, so it fetches the weights again at every step. | VERIFIED | By construction (one matrix-vector product per step against one blocked product). QUALIFY: the 0.8 MB block fits this machine's cache, so "fetch" means read through the cache hierarchy again, not from slow memory. |
| B06 | "What turning the dial up buys is mostly one specific thing." On screen: 1 row 1.03x, 4 rows 1.36x, 8 rows 1.40x. | **CORRECTED 2026-11-08** (figures), QUALIFY (wording) | Full step: 1 row 1.00x, 4 rows 1.33x, 8 rows 1.34x, 16 rows 1.34x. The optimized multiply's gain also includes cache blocking and the matrix unit; not attributed to reuse alone. |
| B07 | 8 positions per weight load: "one point four times". | **CORRECTED 2026-11-08** | 1.34x (1.28 to 1.37): "one point three". |
| B07 | Optimized matrix multiply: "five point seven times". On screen: 0.484 ms vs 0.085 ms. | **CORRECTED 2026-11-08** | 3.7x full step (0.362 vs 0.098 ms; 2.9 to 3.7 over runs), or about 6.3x on the matrix products alone. |
| B07 | Same weights, same twenty million operations; the arithmetic never changed. | VERIFIED | Multiply-adds equal; after the fix the gate work is equal too. |
| B08 | 25 to 400 steps is 16 times the steps, and the recurrent time grew 16 times. | VERIFIED | 0.090 ms to 1.454 ms = 16.2x. |
| B08 | The ratio stayed in the same range (on screen: 4.8x to 5.7x; 4.8, 4.8, 5.7, 5.4, 5.5). | **CORRECTED 2026-11-08** | Full step: 3.3, 3.5, 3.7, 3.8, 3.8 (25, 50, 100, 200, 400 steps): a rise from 3.3 to 3.8, still a narrow range. |
| B09 | Not one number lives in the model; the gap lives between the model and the chip. | VERIFIED | The same model gives 1.0x on one kernel and about 3.7x on another. |
| B09 | "On my laptop, the most I could make was about six times." | **CORRECTED 2026-11-08** | About four times (3.8x at 400 steps, full step). About six only on the matrix products alone. |
| B09 | On a small chip, where weights may sit in slow memory and be read every step, "I would expect more room". | QUALIFY | An expectation, hedged in the line and on screen ("NOT MEASURED ON A CHIP"). Library film's memory beat: weights live in flash, activations in SRAM. Not measured. |
| B10 | Parameters store, operations compute, overlap waits. On screen: 0.2M, 20M, "1.0x to 5.7x". | **CORRECTED 2026-11-08** (the range) | 1.0x to about 3.7x. |
| B11 | My laptop, not a microcontroller; a dense recurrent model, one input at a time; my ratios are smaller than eighty; no claim about any chip or product. | VERIFIED | Still true (3.8x at most). |
| B12 | The cost of one step is 4 x h x (h + x); 64 and 64 give 32,768 per step, about 3.3 million over 100 steps. | VERIFIED | 4 x 64 x 128 = 32,768; x 100 = 3,276,800. |
| B12 | A recurrent model across time has steps that wait; one convolution across positions does not. | VERIFIED | One layer. Stacked layers depend on each other layer by layer; the claim is about positions in one layer. |

## Short
| Line | Claim | Verdict | Evidence |
|---|---|---|---|
| S01 | A small model ran eighty times slower than a bigger one; I made the arithmetic exactly equal. | VERIFIED-LIB, VERIFIED | As B00; multiply-adds equal (and, after the fix, gate work equal). |
| S02 to S04 | What a recurrent model is; two tiny models with the same weights; the first waits for itself, the second has all its inputs up front. | VERIFIED | As B01 to B03. |
| S05 | Over a hundred steps, twenty million operations each; an operation is one multiply and one add. | VERIFIED | 19,968,000 each. |
| S06 | "The first took six point nine milliseconds. The second, six point seven. The same." On screen: 6.9 ms, 6.7 ms. | **CORRECTED 2026-11-08** | 6.1 and 6.4 ms; "the same" holds. |
| S07 | "One point four times slower. Then five point seven." On screen: 1.4x, 5.7x. | **CORRECTED 2026-11-08** | 1.3x, then 3.7x. |
| S08 | The arithmetic never changed; the first fetches its weights again every step. | VERIFIED, QUALIFY | As B06 (cache, not slow memory). |
| S09 | "My gap is smaller than eighty." On screen: "5.7x, NOT 80x". | VERIFIED (words), **CORRECTED 2026-11-08** (screen) | 3.7x. |
| S10 | Parameters store, operations compute, overlap waits. On screen: "1.0x to 5.7x". | **CORRECTED 2026-11-08** (the range) | 1.0x to about 3.7x. |
| S11 | The full film's title. | VERIFIED | Exact title of the long film. |

## YouTube text
Both description files were updated to the corrected figures (and the long one states that the gate work is equal on both sides and about half of the recurrent step's time with the optimized multiply). Chapter times were regenerated from the rebuilt audio.

## Totals
Long film: 25 claims; 12 verified (derived or measured here), 2 verified against the library film, 3 qualify, 8 were corrected (B02's "whole cost", the B05 figures, the B06 figures, B07's 1.4x and 5.7x, B08's band, B09's "about six", B10's range). Short: 9 rows covering the 11 lines; 5 verified, 4 were corrected (S06, S07, S09 on screen, S10 on screen). Every correction traces to one cause, the unequal gate work in the first run, except B02's wording, which the same check exposed.

## What does not change
The angle (equal arithmetic, unequal time, the dial of how much the chip can do at once), the structure of both films, the formula and exercise in B12, the 16x sequence-length result, and the boundaries in B11. The corrections change four figures and two lines of wording.

## Status
1. Corrected set chosen by Tanmay K., 2026-11-08: the full step with equal gate work (1.0x, 1.3x, 3.7x). The matrix-only set (about 6.3x) stays in `MEASUREMENTS.md` as the explanation of the earlier figure; its sequence-length sweep was not run because it was not chosen.
2. Done: Gate P re-signed on draft 3 (B02, B05, B07, B09, S06, S07); audio, captions, both videos and both YouTube files regenerated; measured checks and PROOF measurements re-run.
3. Still stated as limits, not corrected: B01's "everything you see comes from my own measurements" (the library film's title card and memory-map source are labelled on screen); B05's "one thing at a time"; B06/S08's "fetches the weights again" (cache, not slow memory); B09's slow-memory expectation.
