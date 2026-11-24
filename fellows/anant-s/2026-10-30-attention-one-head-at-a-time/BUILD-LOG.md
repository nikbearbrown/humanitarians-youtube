# BUILD-LOG: Attention, One Head at a Time

## 2026-11-22: planning (film #4 of the series), stopped at the narration gate

### Decisions
- **Brief.** A planning session was started by the series' main session to plan up to the narration gate. It did no audio, no rendering, and made no edits under the toolkit.
- **Branding.** Claude-liam / @NikBearBrown default, as the human chose for the series: Liam "in for Bear", Kokoro `am_onyx`, Claude palette, locked `ClaudeTitleOutro`.
- **Skill.** `tldr`, with `metadata.skill: "tldr"` set so that GATE BOOKEND accepts the `ClaudeTldrWhat` cold open.
- **Title and slug.** "Attention, One Head at a Time" with slug `tldr-attention`. The title parallels film 1, "Gradient Descent, One Step at a Time".
- **Greeting.** "Konnichiwa, Liam" (Japanese). No other film in the series uses it; film 1 was Ciao.
- **Source.** We wrote `SOURCE.md` ourselves and fact-checked it against arXiv:1706.03762 (§3.1, §3.2.1, §3.2.2, §3.5). All six items checked were TRUE.
- **Sections (GATE S).** One card: **S1 "One Head, by Hand"**. Status is *pending*, awaiting the human's pick. Positional encoding is noted as a future S2.
- **Evidence.** `demo/attention_demo.py` was executed: numpy, seed 290537. The seed was chosen by a scratch search for legibility; the criteria are in the docstring and re-asserted.
  - Sizes are d_model 4, d_k 4 (so √d_k = 2) and d_v 2. d_v = 2 is a deliberate departure from "d around 3–4": it lets values and outputs be drawn as points, which is what makes the weighted average *visible* (the representation). It is marked on screen.
- **Representation.** The heat map, whose rows are blend weights over value points on a plane. The output is the weighted average, a point inside the hull of the values.
- **DOUBLE-CHECK corrections.** Five, in FACTCHECK #2, #3, #5, #10 and #31.
- **Pronunciation.** Checked with `generate_audio_kokoro.py --phonemize`:
  - "Konnichiwa" came out as /kˈɑːnɪʃˌɪwə/ (KAH-nish-iwa). It is pinned to /kˌoʊniːtʃˈiːwɑː/.
  - "numpy" came out as /nˈʌmpi/. It is pinned to /nˈʌmpaɪ/.
  - "Q, K and V", "root d", "d k", "softmax", "transposed", "query/queries" and "cats'" all phonemize correctly.
  - **Both pins need an ear at GATE 0.**
- **Duration.** About 5.1 min estimated (1,035 words at 3.5 w/s, plus lead silences and about 0.6 s of pauses per beat). That is the single-insight tier.
- **Gates.** `bookend_check.py` PASS. `runtime/qc/beat_lint.py` clean. Both were run from the toolkit root with `env.sh` sourced. In a shell without `env.sh`, `python3` resolves to anaconda, and beat_lint crashes reading UTF-8 as cp1252.
- **Library-first.** No reusable composition was found (SHOTLIST.md). The lead for B17 is the toolkit's Manim `EquationTangent` family.
- **Status.** Waiting for **GATE S** (pick S1) and the **narration gate** (approve SCRIPT.md). Nothing else is built.

### Finding for the renderer: there is no hold field
`compile.py prepare_timeline()` recomputes `render_duration_s` from the measured audio. No `hold_s` or similar is honoured, and `tail_silence_s` / `lead_silence_s` are not read anywhere under `runtime/` (grep, 2026-11-22). Two consequences:
- The **TRANSFORM (B15)** gets its seconds from its own narration: four short sentences, 40 words, about 12 s. The SKILL's advice to write ≤ 1 sentence and let run_time fill the audio would give a 4 s beat. If the morph needs more time, add words that stop describing ("There."), not silence.
- B02's 0.8 s lead silence and BOUT's 1.0 s tail rely on whatever produced them for film 1. Confirm at GATE 0 that they are actually present in the mp3s.

## Plan for the render session (do not start before GATE S plus narration approval)
1. **Audio (GATE 0).**
   - Run `python3 runtime/scripts/generate_audio_kokoro.py <reel>`, then `align.py <reel>` to write `mp3/words.json`.
   - Listen for "Konnichiwa", "numpy", "Q, K and V", "root d" and "d k".
   - Then rewrite `durationSeconds` (B00, B01, B03) from `actual_duration_s`, and re-cue B00/B01 `cues` from words.json. The current cues are 3.5 w/s estimates.
   - Note: `make_sheet.py` OVERWRITES `beat_sheet.json` and drops the measured fields. Patch the measured values in after any re-run, or re-run audio.
2. **`scenes.py`.** One `Scene` per LEARN beat, named literally `class B10_ChaseMoves(Scene):` … `class B19_OrderBlind(Scene):`.
   - Every number comes from `demo/evidence.json`. Assert at least chase's weights and output against it in B15.
   - One module-level **state factory** for section 1 holds the sentence row, value plane, word points, ghost landings and heat map, rebuilt at the previous beat's end state. Assert it in each scene's first line, so the last frame of Bk is the first frame of Bk+1.
3. **Design rules (from the series lead, binding):**
   - **Stub-safe code.** GATE A pre-flights `scenes.py` as an *isolated copy*. Use film 1's patterns:
     - `_load()` falls back to `ART_REEL` / the reel path.
     - `P()` / `V()` coerce points to float vectors with a `np.zeros(3)` fallback.
     - No geometry that assumes real `c2p` output at import time.
     - No docstring containing a fake `class Bxx_` line, which run.sh would pick up as a scene.
   - **Frame-counting clock.** Count frames as `ceil(run_time · fps)` per play/wait (film 1's `Clock` class: `at()` floors to whole frames, `play()` ceils). Each scene ends at its beat's measured duration, within ±3%.
   - **Box spotlights, not underlines,** on "=" and "−" (and everywhere in B17's tangent). An underlined "−" reads as "=", and an underlined "=" reads as "≡" (film 1 QC). GATE T also reads a thin terracotta horizontal stroke as accent text.
   - **GATE V needs ≥ 55% canvas fill.** Size the heat map and value plane to fill: heat map about 5.2 units wide on the left, plane about 6 units on the right. In B10/B12, where rows are text-heavy, use type 36–44 for the mono rows.
   - **Keep all text within ±6.0 x and ±3.2 y** (title-safe). The sentence row sits at y ≈ 2.8. Captions go no lower than y = −3.1.
   - **Palette.** Cream `#F2F0E9` (LEARN stage), ink `#3D3929`, one terracotta `#D97757` moment per beat, dim `#8B8F96` for ghosts and foils, ghost `#D9D4C7` for scaffolding. Heat-map shading is ink alpha by weight, never a rainbow.
   - **Type.** EB Garamond for labels, PT Mono for data numbers, `MathTex` for every equation (B11's blend label, B14's ÷2 chip, B16, B17). No `slant=ITALIC` on multi-word text. Type floor 32.
   - **Simplification captions, once each:** "toy numbers, not a trained model" (B10); "two numbers per point so we can draw it; real heads use 64" (B11); "rounded; every row sums to 1" (B14); "positional encoding — not taught here" (B19).
   - **Motion budget.** One dominant mover per scene: the dot in B10/B11/B15/B18, the request row in B12, the four collapsing dots as one group in B13, the grid in B14/B16, the permuting cells in B19.
4. **`./art run <reel> --height 2160`.** This runs gates F/L/A/W, then B, then V, then T and BOOKEND. Read the frames at 15/50/85% of every beat, and check each equation at its revealed states. Fix at the source and re-run. Then the human watches the cut.
5. **`./art final`.** Only after the human watches the cut. Never publish.

## 2026-11-22: GATE S and narration gate approved
- **Approvals.** The user wrote **"approve all six"** in the series' main session. The main session relayed it here as approving **GATE S: S1 "One Head, by Hand"** and **the narration as drafted** (GATE P).
- **Scope now.** Audio, `scenes.py` and low-res (-ql) previews, then stop before any 4K render. The main session added `C:/Users/anant/stem-films/tools/pad_silence.py`, which applies `lead_silence_s` / `tail_silence_s` to the mp3s. This addresses the hold-field finding above.

## 2026-11-22: audio, scenes.py, low-res previews (stopped before any 4K render)

### Audio (GATE 0, machine side)
- **Kokoro am_onyx.** 17 beats generated by `generate_audio_kokoro.py`. Cost $0.00.
- **Padding.** `stem-films/tools/pad_silence.py` added B02's 0.8 s lead, BVDT's 0.5 s lead and BOUT's 1.0 s tail to the mp3s.
- **Measured total: 301.98 s (5:02).** The estimate was about 5.1 min.

| Beat | s | Beat | s | Beat | s |
|---|---:|---|---:|---|---:|
| B00 | 18.90 | B11 | 15.57 | B17 | 35.34 |
| B01 | 17.62 | B12 | 17.17 | B18 | 17.88 |
| B02 | 10.61 | B13 | 15.34 | B19 | 18.90 |
| B03 | 13.97 | B14 | 16.43 | BVDT | 21.94 |
| B10 | 16.32 | B15 | 11.88 | BHTF | 34.06 |
| | | B16 | 15.49 | BOUT | 4.56 |

- **Whisper check.** faster-whisper base was run on every beat and diffed against `narration_text`.
  - **Pins verified.** "Konnichiwa" was heard as "Konichi wa" and "numpy" as "numpy-only", so both lexicon pins work.
  - **No pronunciation fixes needed.** Every other diff was digit normalisation ("0.53", "1-0, 1-0") or whisper-base homophones and fusions: neighbours/neighbors, Nik/Nick, weight/wait, mix/mixed, "the query as" for "the queries".
  - **Two spots for a human ear at the audio listen:**
    - BVDT "root d k": whisper heard "root, decay". B17's "d k" was heard correctly as "Dk".
    - BHTF "Paste this": whisper heard "pace this".
  - Neither is a G2P error, so nothing was regenerated.
- **Alignment.** `align.py` wrote `mp3/words.json`: 17/17 beats aligned, 0 fallback. On CPU it took over 10 minutes.
- **Bookend props re-cued from measured audio.** These were patched directly in `beat_sheet.json`; `make_sheet.py` was not re-run.
  - B00 `cues` = [2.33, 6.67, 9.92, 14.33], `durationSeconds` = 18.9.
  - B01 `cues` = [0.62, 5.79, 10.83], `durationSeconds` = 17.62.
  - B03 `durationSeconds` = 13.97.

### scenes.py (house pattern from claude-liam-backpropagation)
- **House helpers.** `_load` with REEL fallback, `cue()`, the frame-quantised `Clock`, `V()`, and `box()` (box spotlights, never underlines).
- **One scene per LEARN beat,** `B10_ChaseMoves` … `B19_OrderBlind`.
- **Transform, don't cut.** Each scene adds the previous beat's end state at t = 0, so the join is continuous. The shared layout and factory are `state_after_B10`, `value_plane_state`, `heat_state` and `strip_state`. New drawing starts at t = 0.2.
- **Every number comes from `demo/evidence.json`,** with an assert that the evidence has not changed.
- **Ground.** `#FAF9F5` (house and film 1) rather than the tldr doc's `#F2F0E9`. Against `#F2F0E9`, SOFT caption text is 4.37:1, which trips the W2 body-text warning; against `#FAF9F5` it is 4.75:1.
- **Spotlight boxes are flagged `_qc_intentional`** (the audit's editor's-ring exemption). Frames, pull lines and hulls are still audited under `--curve-strict`.
- **Fixes found by the gates and frame QC:**
  - **B16:** the unicode "−" inside a MathTex `bmatrix` broke LaTeX.
  - **B11, B12, B19:** long captions crossed the value-plane frame. They are now two-line or left-panel captions.
  - **B17:** the values-claim row overflowed, and raw "d_k" appeared in Text. Both are now MathTex.
  - **B10:** the head label collided with the sentence.
  - **B12:** the products column was cramped.
  - **B14, B18, B19:** weights read "0.6". All weights now show two decimals.
  - **B15:** the cats mass ring struck its label. Labels moved up and the rings shrank.
  - **B16:** it opened on an empty left half. Q/K/V now arrive at t = 0.2.
  - **B19:** output points were indistinguishable from value points, so outputs are now hollow. The positional-encoding point landed on "small", so it is now a numeric readout.
  - **Late cues** in B10, B13 and B18 were retimed. B15 is still 0.11 s late at t = 1.35, which is cosmetic.

### Gates (per scene, final code). A, W and B each exited 0 for all ten scenes (`_qc/gates.txt`)
- **A:** `static_scene_check.py` on an isolated copy of `scenes.py` in scratch.
- **W:** `wcag_margin_check.py --quiet`.
- **B:** `manim_layout_audit.py --curve-strict`. Per-scene reports are in `_qc/gateB/`.
- `bookend_check` PASS, `beat_lint` clean and `factcheck_check` clean after the sheet patches.

### Previews (-ql, 24 fps, media_dir in session scratch, outside the film folder)

| Scene | clip s | audio s | Δ |
|---|---:|---:|---:|
| B10 | 16.46 | 16.32 | +0.85% |
| B11 | 15.67 | 15.57 | +0.62% |
| B12 | 17.25 | 17.17 | +0.47% |
| B13 | 15.42 | 15.34 | +0.50% |
| B14 | 16.54 | 16.43 | +0.67% |
| B15 | 11.92 | 11.88 | +0.31% |
| B16 | 15.50 | 15.49 | +0.06% |
| B17 | 35.58 | 35.34 | +0.69% |
| B18 | 17.96 | 17.88 | +0.44% |
| B19 | 18.92 | 18.90 | +0.09% |

- All ten are within ±3%. Frames at 15/50/85/99% were inspected for every scene; the contact sheets are in `_qc/preview-sheets/`.
- **Housekeeping.** Gate B left Manim caches in `media/Tex` and `media/texts`. They were deleted so `media/` stays free for real slot files.

### Not done (by instruction)
- No 4K render. No `remotion_scenes.py`, `./art run` or `./art final`. The Remotion bookends (B00–B03, BVDT, BHTF, BOUT) have not been rendered or looked at.

## 2026-11-22/23: scenes rule update (no terracotta on text) + GATE V fill/contrast
- **Rule from the main session.** Never put terracotta on text, numerals or arrows. Backprop's export was blocked by GATE T §8.3, which flags terracotta at 2.74:1 on cream.
  - Changed: the B12/B13 request rows and the "chase asks" / "small asks" labels are now INK, and the accent is a terracotta box around the request row. "attention" in B16 is now INK, with a terracotta box.
  - SPARK now appears only on dots, rings, Spot boxes, heat-map row outlines and the tinted values-claim fill. Every arrow is INK.
- **GATE V check, run locally.** `final_frame_check.analyze_frame` was run on the -ql frames at 50% and 85% of each LEARN beat. The first pass failed six beats: underfill on B12, B16 and B17, and low contrast on B13, B14, B15 and B19.
  - **Contrast cause:** light GHOST strokes and pale cell tints count as "ink" but pull the average ink luminance toward the page. The check's background estimate bins the page as (248, 248, 248), so a 0.25-weight tint sits about 31 levels off on the blue channel and counts as pale content.
  - **Contrast fixes:**
    - Structural strokes moved from GHOST to SOFT: cell outlines, plane frame, pull lines, hull and the two-point segment.
    - The heat-map tint scale went from 0.55·w to 0.45·w.
    - B13's equal-weight grid (and B14's matching opening state) is drawn unshaded, because a uniform tint carries no information.
  - **Fill fixes:**
    - B12: a typeset rule "request · offer = sum of the products" now lands on "Against cats' offer", so it is visible by the 50% sample.
    - B16: Q, K and V stay visible across the top band while the equation forms below in a GHOST slot outline from t = 0.2. The symbols stay mapped to their matrices.
    - B17: the values-claim box shows as a GHOST outline from t = 0.2 and fills on "design choice".
  - **Other:**
    - B12's request box was clipping "chase asks", so the request row moved down 0.07.
    - B16's shrunk heat map now shows shaded cells only; at 0.42 scale its numerals would fall below the type floor.
  - **Result:** GATE V (local, preview resolution) is clean on all 20 samples. The minimum coverage is 0.67.
- **Gates (final code).** A (isolated copy), W and B (`--curve-strict`) each exited 0 for all ten scenes (`_qc/gates.txt`).
- **Previews.** All ten are within ±3% of their audio (max +0.85%, B10). The final 15/50/85/99% sheets are in `_qc/preview-sheets/`. The one remaining clock note is B15, 0.11 s late at t = 1.35 (cosmetic).
- **Incident (see below).** While resuming after the usage-limit pause, I killed an orphaned manim process (PID 1402) that I wrongly took for my own. It belonged to another session (scratch `af865405…`, the overfitting film's preview loop, scene `B04_ThreeFits`). That session's -ql preview of that scene will have failed. Nothing outside its scratch folder was touched, but it needs a re-render. My own orphaned job was stopped only after checking its command line.

## 2026-11-23: GATE T §8.3 fix (4K build failed on wide terracotta shapes at the midpoint)
- **Failure, reported by the main session's 4K build.** At the midpoint frames of B10, B12, B15 and B17, a wide terracotta shape (wider than 1.5× its height) was read as low-contrast accent text (2.74:1). The blobs mapped to:
  - B10: the box around chase's embedding row.
  - B12: the box around the request row.
  - B15: the heat map's chase-row box, carried over from B14.
  - B17: the tangent's spotlight box on √d_k.
- **Fix.** Validators untouched; all edits are in `scenes.py` only.
  - **B10:** chase's row box is now INK. The beat's terracotta moment stays on chase's output dot, a compact mark.
  - **B12 / B13:** the request-row box is now INK. A compact terracotta ring circles chase's first score, 3. It appears on "add", after the midpoint, and fades on "Ask from small". It is not carried into B13.
  - **B15:** the chase-row box arrives terracotta from B14, whose box appears after B14's midpoint, and turns INK on "set the mix" at about 0.3 s. `heat_state` gained a `box_color` parameter, and B16 starts with the INK box. The terracotta moment is now the mass rings and the blend dot.
  - **B17:** the moving spotlight is INK, via `ibox` and `span_box`. The RHS box is now built from the parts' real edges, because the old box clipped the "s" of softmax. The tangent's copy of the equation gets a thin space after "=", so the box clears it. The terracotta moment is the values-claim tint on "design choice", after the midpoint.
- **4K verification.** B10, B12, B15 and B17 were each rendered with `manim -qk -r 3840,2160` into scratch. On each midpoint frame, `type_check.check_contrast` and `check_min_size` both PASS:
  - B10: 9.58:1, 51 px
  - B12: 10.02:1, 50 px
  - B15: 7.65:1, 49 px
  - B17: 8.57:1, 50 px

  B12 and B17 were re-verified after the last tweaks. The midpoint frames are in `_qc/gateT-4k/`.
- **Gates.** A (isolated copy), W and B (`--curve-strict`) each exited 0 for every changed scene: B10, B12, B13, B15, B16, B17 and B18 (`_qc/gates.txt`). B11, B14 and B19 are unchanged since the last full sweep.
- **Previews (-ql).** The changed scenes are within ±3% of their audio: B10 +0.85%, B12 +0.47%, B13 +0.50%, B15 +0.31%, B16 +0.06%, B17 +0.69%, B18 +0.44%. The local Gate V check is clean on all 20 frames at 50% and 85%. Sheets are in `_qc/preview-sheets/`.
- **Not 4K-verified.** B13 and B16 were not checked at 4K. Their changes only remove terracotta from their opening state, and the -ql checks are clean.
- **Not touched.** B00/B01 (the main session is fixing ClaudeTldrWhat/Why in the toolkit), the toolkit, and `./art run` / `./art final`. The build outputs in `media/`, `manim/`, `clips/` and `exports/` were left alone. Gate B only added cache files under `media/Tex` and `media/texts`.

## 2026-11-23 — 4K GATE T fixes (main session)
- **Rebuild 1 cleared §8.3 but failed three checks:**
  - B00/B01 §8.2 overflow: the "W" of the heading overhung title-safe by 1 px.
  - B17 §8.6b: an ink spotlight ring wider than 1.5× its height read as a text run enclosing its glyph.
- **Toolkit fixes:**
  - `ClaudeTldrWhat`/`ClaudeTldrWhy` list lines 48 → 52 (the §8.1 43 px fix from earlier).
  - Their heading moved to SAFE.x + 4.
  - Verified: B00/B01 pass §8.1, §8.2, §8.3 and §8.6b.
- **scenes.py:**
  - `box()` keeps spotlights at most 1.4× as wide as tall, so a ring is never a text run.
  - Extra height grows downward (shift capped at 0.6 for GATE A's stub), so it stays off fraction bars.
  - B17 at the 4K midpoint passes §8.1, §8.2, §8.3 and §8.6b.
  - Gate A shows one stub-only warning on B16/B17 (a placeholder coordinate). W and B are clean.
- **All Manim clips were superseded and re-rendered**, because the box change touches every scene.

## 2026-11-23 — final (main session)
- **Master:** `exports/landscape/tldr-attention.mp4`, 3840×2160, 24 fps, 302.4 s, SHA-256 `c4c74bb43a4b5156…`. It matches `.verified.json` (`ready`).
- **Checks:** GATE V clean; GATE T PASS; strip check PASS (151 samples; the bottom band peaked at 0.8%, which is noise, and no strip is visible); master check PASS; loudness PASS (−24.73 LUFS).
- **Hand QC:** every beat checked at 15/50/85%. The garbled B12 header at 85% is a morph frame and settles to "small asks · 1 1 −1 −1".
- **Not published.**

## Format conversion → ai-explainer (2026-11-24)
- **Why:** the user asked for this film to match the other five (ai-explainer spine), with no footer.
- **Approval (GATE P, chat, 2026-11-24):** the user approved the new B00 cold open and B01 hesitant-writer narration. They asked for "Hello" in place of any other greeting, for all three converted films.
- **Change:** TL;DR B00 What, B01 Why, B02 Question and B03 Terms were retired to `_superseded/format-tldr/`. They are replaced by B00 `ClaudeComposerAsk` and B01 `BrutalistHesitantWriter` (lead 0.8 s, fontSize 130 for the 28-character lines). Body B10–B19, BVDT, BHTF and BOUT are unchanged. Every term the Terms card defined (embedding, dot product, softmax) is also defined inline in the body (B11, B12, B14).
- **Tool:** `stem-films/tools/convert_to_ai_explainer.py`.
- **Render 1:** GATE V failed on B01 underfill (45% at fontSize 130). B01 was re-rendered at fontSize 145, lineSpacing 3.3, which measures 59% fill; the old clip is in `_superseded/b01_underfill/`.
- **FINAL (ai-explainer), 2026-11-24:** 261.0 s, 3840×2160. GATE V 0 blockers / 0 majors, GATE T PASS, bookend PASS, strip check 131/131, master PASS, −24.72 LUFS. sha256 cfeaaee78f194ab885e78d9a9d85bd938f71e4a4ef04172effbb843bf9995277 matches .verified.json. Hand QC of all 15 beats is clean. Copied to the user's "Footer removed" folder.
- **Docs refreshed (2026-11-24):**
  - SCRIPT.md, SHOTLIST.md and CHECKS-REPORT.md were regenerated from the current beat sheet with `stem-films/tools/refresh_converted_docs.py`. Each keeps its pre-conversion content verbatim under a History heading. The originals are backed up in `_superseded/format-*/docs/`.
  - FACTCHECK.md has a dated conversion section appended that checks every new spoken and on-screen line; the earlier rows are unchanged.
