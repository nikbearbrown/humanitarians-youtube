# BUILD-LOG — Overfitting, When a Perfect Score Lies

## 2026-11-22 — planning (film 3 of 7; planning session, stops at GATE P)
- **Choices:** topic, skill (ai-explainer) and branding (default claude-liam / @NikBearBrown) were chosen by the human for the series.
- **Greeting:** "Namaste, Liam", one word from the lexicon, unique in the batch (film 1 used Ciao). Liam never takes "Wagwan".
  - espeak phonemizes "Namaste" as /nˈæmæst/, dropping the last syllable. It is pinned in `metadata.pronounce` to /nˈʌməstˌeɪ/, verified through the script's own `apply_lexicon`.
- **Title and slug:** "Overfitting, When a Perfect Score Lies", slug `claude-liam-overfitting`. The title parallels film 1's "Topic, Phrase" shape.
- **Evidence:** `demo/overfit_demo.py` was executed, about 7 s, and its output is the only source of on-screen numbers.
  - `make_sheet.py` asserts every spoken figure against `evidence.json`.
  - It also asserts the length budget: B01 20–35 words, body 45–70, verdict 4 or 6 lines.
- **DOUBLE-CHECK corrections:** three, in FACTCHECK #1, #20 and #22.
- **Duration:** 677 words. Estimated 3.2 min at Kokoro's measured 3.5 words/s (film 1); the 2.6 w/s planning figure gives 4.3 min.
- **ASK→RESULT:** applied at the cold open only, following the film 1 precedent.
- **Gates passed:** `bookend_check` PASS; `beat_lint` clean.
- **Not done in this session, by design:**
  - no audio;
  - no `scenes.py`;
  - no render;
  - no `BUILD-PROMPT.md` (the main session writes it with the render plan);
  - nothing written under the toolkit (scene searches used `--no-log`).
- **Status:** waiting for narration approval (GATE P), then audio (GATE 0).

## Plan for the render session (after GATE P)
1. **Audio:** `python3 runtime/scripts/generate_audio_kokoro.py <film>`.
   - Then run `align.py` to get `mp3/words.json`.
   - Listen for "Namaste" (pinned), "NumPy" (/nˈʌm pˈaɪ/, expected fine) and "sine of pi x".
2. **scenes.py:** copy film 1's chassis: `_load` with the isolated-copy fallback, `cue()`, `Clock`.
   - Six scenes: `B02_Setup`, `B03_ErrorMeasure`, `B04_ThreeFits`, `B05_TheU`, `B06_MoreData`, `B07_PeekedScore`.
   - Every number and every curve is read from `demo/evidence.json`:
     - `grid` and `truth_curve`;
     - `worked.*.curve`;
     - `data.train` and `data.test_preview`;
     - `more_data_200.curve`;
     - `sweep`, `more_data` and `selection`.
   - **B06 refit frames:** `evidence.json` has the degree-15 curve only for n = 16 and n = 200. Either add n = 20 / 100 / 1,000 curves to the demo (preferred: re-run the demo and `make_sheet`, then re-hash), or refit inside the scene from the nested pool. Refitting inside the scene breaks "numbers only from evidence", so extend the demo.
   - **B07 trial grids:** the 10×10 grids need per-trial outcomes. Add a 100-trial outcome list to `evidence.json` (or the full 1,000 as a bitstring) rather than inventing a pattern that merely matches 70%.
3. **Design rules (carry over from film 1's QC):**
   - **GATE A** pre-flights `scenes.py` as an isolated copy, so the code must be stub-safe:
     - load files through the `HERE`-then-`REEL` fallback;
     - make arrow and point centers explicit;
     - put no fake `class X(Scene)` text in docstrings, because run.sh greps for classes.
   - **Frame counting:** the clock counts frames as ceil(run_time·fps). Manim renders that many, so `Clock.play` rounds up and `Clock.at` floors.
   - **Spotlights:** use box spotlights with a minimum height, never underlines, especially on "=" and "−" in B03. An underlined "−" reads as "=".
   - **GATE V needs ≥55% canvas fill.** Size the three B04 panels and the B05 chart to the safe area.
   - **Text bounds:** keep all text within ±6.0 x / ±3.2 y in Manim units.
   - **B04/B06 degree-15 curve:** it reaches |f| ≈ 1,303. Clip it to the panel with an explicit clip rectangle and an exit arrow. Never let it draw off-canvas.
   - **B05 test curve:** it exits the 0–0.6 axis at degree 11. The exit chips (1.83 · 26.4 · 5,807.1 · 8,251.1 · 9,882.6) sit inside the text bounds.
   - **One terracotta moment per beat:**
     - B04: the 9,882.6 counter.
     - B05: the climbing test curve.
     - B06: the meeting ring.
     - B07: the optimistic cells.
4. **Verdict:** keep it at six lines (4 or 6, never 5).
5. **Outro:** the title is 38 characters with a comma, so the locked `ClaudeTitleOutro` may wrap it as "Overfitting, When a Perfect / Score Lies.". That is the same known cosmetic issue as film 1. The component has no layout props, and the outro lock forbids altering the title.

## 2026-11-22 — GATE P: narration approved
- The human approved the narration as drafted, all 11 beats, in the main session with "approve all six" (one approval for the six planned films). It was relayed to this session by the main session.
- **Demo extended before audio** (no RNG use, existing evidence values byte-for-byte unchanged, checked by a key-by-key diff):
  - `more_data[*].curve` and `pool_preview`, for the B06 refits;
  - `selection.grid100_peek` and `grid100_untouched`, the per-trial outcomes of the first 100 trials, for the B07 grids. 68 of the first 100 trials are optimistic under peek and 59 untouched; the counters show the 1,000-trial 69.6% / 55.2%.
- `make_sheet.py` was re-run before audio, so nothing was lost.
- New hashes: script `4cb1d91f…f9d5`, evidence `988d991c…381c`.

## 2026-11-22 — audio, scenes and low-res previews (stopped before any 4K render)
- **GATE 0 (audio):** Kokoro am_onyx, 11 beats, total **198.5 s (3:18.5)** after padding (`pad_silence.py`: B01 lead 0.8 s, BVDT lead 0.5 s, BOUT tail 1.0 s).
  - Per beat: B00 9.00, B01 11.00, B02 16.45, B03 17.92, B04 21.46, B05 18.43, B06 20.52, B07 19.29, BVDT 20.47, BHTF 39.01, BOUT 4.97.
- **Whisper check (faster-whisper base):** no real mispronunciations, so no regeneration.
  - "Namaste" (pinned to /nˈʌməstˌeɪ/) transcribes correctly.
  - Every other diff is one of: digit normalization; homophones ("too"/"2", "U"/"you", "Nik"/"Nick", "for Bear"/"forbear"); B03 "and"→"in" (reduced /ən/ in "real value and the model's guess"); B07 "Say"→"So". **Both flagged for a human listen.**
- **Align:** `align.py` aligned 11/11 beats with 0 fallbacks → `mp3/words.json`.
- **Show text:** `shot.show` text for B02, B03, B05 and B07 was synced to what the scenes draw, edited in both `make_sheet.py` and `beat_sheet.json` without re-running `make_sheet.py`. A temp-dir regeneration matches the sheet apart from the audio fields.
- **scenes.py:** six Manim scenes on the house chassis (`_load` with REEL fallback, `cue()`, frame-quantised `Clock`, `V`, `box`), plus a numpy `Plot` mapper so all geometry is stub-safe. Every number and curve is read from `demo/evidence.json`.
- **Gates (final), per scene:**

  | Scene | A | W | B |
  |---|---|---|---|
  | B02_Setup | 0 | 0 | 0 CLEAN |
  | B03_ErrorMeasure | 0 | 0 | 0 CLEAN |
  | B04_ThreeFits | 0 | 0 | 0 CLEAN |
  | B05_TheU | 0 | 0 | 0 CLEAN |
  | B06_MoreData | 0 | 0 | 0 CLEAN |
  | B07_PeekedScore | 0 | 0 | 0 CLEAN |

- **Previews:** `manim -ql --fps 24`, rendered to a scratch media dir outside the film folder. Clip vs audio: B02 +0.56%, B03 +0.91%, B04 +0.38%, B05 +1.06%, B06 +0.31%, B07 +0.44%, all within ±3%. Frames at 15/50/85/99% were inspected by eye.
- **Fixes made on the way to clean:**
  - **B03:**
    - Worked-term MathTex ran off the right edge and collided with its label; restacked and centred.
    - Equation 104→92 pt to sit inside ±6.0.
    - Spotlight padding 0.08→0.2 per side, because the stroke sat on the "−".
    - Signed numbers braced so LaTeX doesn't space the minus as a binary operator.
  - **B05:**
    - Monospace exit-value line ran off-frame; now serif.
    - "Lowest test error" label crossed the training line; shortened to "best: degrees 3 to 6" and moved.
    - Two run times trimmed (the clock had run 0.1–0.3 s late).
  - **B06:** monospace table columns collided; now a serif table with wider columns and a narrower plot.
  - **B07:**
    - Grid titles overlapped; shortened.
    - The opening was underfilled; the split strip now starts large mid-frame and parks at the top when the grids arrive.
    - Grids enlarged and spread.
  - **B02:**
    - The opening was underfilled (≈47%); the plot now starts full-width and shrinks left when the test set arrives.
    - "locked away" now leaves before "grade on these" lands, so there is no morph.
- **Known, accepted:** B07's opening ~2 s has content to about 57% height before the "keep the best" line lands, which is above the 55% bar. GATE V on the compiled cut is the real check.
- **Not done (main session):** Remotion beats (B00, B01, BVDT, BHTF, BOUT), `./art run`, GATE V/T, the 4K render and final.

## 2026-11-22 — terracotta rule and 50%-frame fill (main-session rule update)
- **Rule:** never put SPARK on text or arrows, because GATE T §8.3 reads terracotta text and arrow tips as 2.74:1 on cream. Terracotta now appears only on non-text shapes:
  - **B02:** "grade on these" is ink; the test-set box outline turns terracotta on "We grade".
  - **B03:** spotlight boxes (unchanged).
  - **B04:** the 9,882.6 counter is ink, ringed by a terracotta `box()`.
  - **B05:** exit arrows and exit values are ink; the test-error dots and curve stay terracotta (shapes).
  - **B06:** the meeting ring (unchanged).
  - **B07:** the optimistic grid cells (filled squares, unchanged).
- **GATE V 50% frame:** B07's right grid was empty at mid-beat. Both grids now appear as GHOST outlines when the grid stage opens, and each fills on its own cue. The other five beats were already full at 50%.
- **Re-gated all six:** A 0 / W 0 / B 0 (CLEAN) each.
- **Re-rendered B02, B04, B05, B07 at -ql** and looked at frames 15/50/85/99%.
  - Previews vs audio are unchanged: +0.56 / +0.91 / +0.38 / +1.06 / +0.31 / +0.44 %.
  - The first B04 render was killed externally (exit 143) and re-run clean.

## 2026-11-23 — B03 GATE T fix (main session)
- **Problem.** GATE T §8.1 failed on B03: "smallest text run 38px < 41px".
- **Cause.** Running GATE T's own blob code on the midpoint frame showed the 38 px run was the **hat accent on f̂** in the MSE formula. Enlarging the formula enough to fix it pushed the formula past title-safe (GATE V edge-bleed). The tighter spotlight box also fused with the glyphs and triggered §8.3.
- **Fix.**
  - The prediction is written as f(xᵢ), without the hat. The on-screen tag "model's guess" names it, and the narration is unchanged.
  - The worked-term line is enlarged from 48 to 60.
  - The formula keeps its original 92 pt and position.
- **Result.** The 4K midpoint now measures a smallest run of 56 px (PASS). Gates A, W and B pass.
- **Follow-up.** GATE T §8.3 then flagged the wide terracotta spotlight box at the midpoint, because a wide accent outline reads as an accent text run. The moving spotlight is now INK, and terracotta appears only on the final "MSE = 0" box, which lands after the midpoint. A 4K midpoint test passes on size (56 px) and contrast (10.04:1).
- **Hand-QC fix.** The B03 spotlight box on "MSE" overlapped the "=". It is tightened with pad 0.16, and the settled frame is verified clean.

## 2026-11-23 — final (main session)
- **Master:** `exports/landscape/claude-liam-overfitting.mp4`, 3840×2160, 24 fps, 198.8 s, SHA-256 `254049bbf9e9b97a…`. It matches `.verified.json` (`ready`).
- **Gates and checks:**
  - GATE V: clean.
  - GATE T: PASS.
  - Strip check (label corner + full bottom band): PASS, 99 samples.
  - Master check: PASS.
  - Loudness: PASS, −24.69 LUFS.
- **Hand QC:** every beat checked at 15/50/85%.
- **Not published.**
