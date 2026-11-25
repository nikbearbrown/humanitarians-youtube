# BUILD-LOG — Bayes' Theorem: The Positive That's Usually Wrong

## 2026-11-22 — planning (side session, film #4 of 7)

**Brief and scope**
- Plan film #4, Bayes' theorem, as a `tldr` film and stop at the narration gate.
- Branding is the default claude-liam / @NikBearBrown: Liam in for Bear, Kokoro `am_onyx`, the Claude palette, and the locked `ClaudeTitleOutro`.
- Greeting: **"Salaam, Liam"**. It is in the composer lexicon (Arabic/Farsi), and film 1 used Ciao.

**Hard limits observed.** This session did none of the following:
- generate audio or run `generate_audio_kokoro.py` other than `--phonemize`
- run any render: no manim, no `remotion_scenes.py`, no `./art run` or `./art final`
- edit anything under `C:\Users\anant\brutalist.art`
- touch other films' folders
- call a paid API

Web searches were used only to verify the citations.

**Read in full**
- `STEM-VIDEO-GUIDE.md`
- `skills/make/tldr/SKILL.md`, and `reference/` (`pedagogy.md`, `sectioning.md`, the example sheet)
- `docs/MATH-TYPESETTING.md`, `docs/EXECUTABLE-EVIDENCE.md`, `OUTRO-LOCK.md`
- Film 1's `gd_demo.py`, `make_sheet.py`, paperwork and the `scenes.py` clock pattern

**Doc quirks followed per the brief**
- The tldr spine code block omits B02 (THE QUESTION); the SKILL text includes it.
- `sectioning.md` beat numbers are stale. It says "B01 corrected text" and "terms → B02", where the SKILL text has B02 and B03.

**Source.** `SOURCE.md` was written for the film with 7 references. Casscells 1978 was confirmed through the Manrai 2014 replication's report of it.

**GATE S.** `tldr-sections-bayes.md` proposes one card, S1 "Count the Positives", marked **PENDING**.
- It lives in the film folder, not in the shared `youtube/` root, to keep this session inside its own folder.
- Move it to `youtube/` if the series wants the sections files together.

**Evidence**
- `demo/bayes_demo.py` (standard library, `Fraction`, seeded `random`) was executed and asserts every relation.
- `make_sheet.py` asserts every spoken number against `evidence.json`.
- The simulation of 100,000 people gives PPV 0.1669 against the exact 1/6, within 1 SE.

**DOUBLE-CHECK corrections** (FACTCHECK #1–#5)
1. "99%-accurate" was corrected to "catches 99% of cases". With 99% sensitivity and 95% specificity, overall accuracy is 95.04%.
2. The title moved from the test being usually wrong to **the positive** being usually wrong.
3. A 1,000-person grid gives 9.9 and 49.5 people, so the population is **10,000**. The grid is 125 × 80, not 100 × 100, for the ±3.2 vertical band.
4. B01 "this exact puzzle" became "this kind of puzzle", because Casscells used a prevalence of 1/1,000 and 5%.

**Narration fixes from checks**
- B18 was trimmed from 62 to 51 words (the LEARN ceiling is 60, and the pace ceiling 20 s).
- B18 "You're" phonemized as "your", so it now reads "You are".
- B01 was trimmed from 67 to 65 words.

**Gates at plan time**
- `bookend_check` PASS.
- `beat_lint` clean.
- `math_layout_check` exit 0.
- `pace_check` advisories only (CHECKS-REPORT).

**Status:** waiting at **GATE S** (pick S1) and **GATE P** (narration approval). Nothing past planning was started.

## Design rules for the build session (record; binding on `scenes.py`)

**GATE A (stub-safe code)**
- GATE A pre-flights an isolated copy of `scenes.py`, so the code must be stub-safe.
- Use film 1's `_load()` fallback: `HERE`, then `ART_REEL` (`C:/Users/anant/stem-films/youtube/tldr-bayes-theorem`).
- Use the `P()` / `V()` float-vector guards around every `c2p` / `get_corner`.
- Don't put a fake `class Bxx_` line in a docstring. run.sh's regex picks it up as a scene.

**Frame clock**
- Count frames as **ceil(run_time·fps)**. Reuse film 1's `Clock` (`at` floors waits to whole frames, `play` ceils run_time).
- Cue reveals from `mp3/words.json` (align.py).
- End every scene with `c.end()` at the measured duration.

**Spotlights:** use box spotlights, not underlines, on "=", "−", "≠" and "|". In film 1 an underlined "−" read as "=", and an underlined "=" read as "≡". The B17 tangent's moving spotlight is a `SurroundingRectangle` with a minimum height.

**GATE V needs ≥ 55% canvas fill**
- The grid is 8.5 × 5.44 u plus a counter column.
- Equation beats (B15–B17) set MathTex at ≥ 96 pt, with the glossary spread across the side band.
- Bookend Remotion cards follow film 1's lessons: large type, and 4 or 6 verdict lines (BVDT has 4).

**Safe area:** keep all text within **±6.0 × ±3.2** (film 1's B02 label failed GATE B below the safe area).

**Palette (tldr LEARN)**
- Cream `#F2F0E9`, ink `#3D3929`, terracotta `#D97757` (one moment per beat), dim `#8B8F96`, ghost `#D9D4C7`.
- Healthy squares are dim and sick squares ink. Cleared and negative squares fade to ghost.
- Terracotta marks only the sentence's current focus. Per GATE T, never use a thin terracotta horizontal rule.

**Grid performance**
- Build each category as **one** VMobject with many square subpaths, not 10,000 `Square`s.
- Animate category-level opacity and fill.
- The B14 regroup moves only the 594 positives, which can be individual `Square`s.

**False-positive positions:** seed them with `random.Random("tldr-bayes-theorem-fp")`, taking 495 of the 9,900 healthy cells. Assert that the count is 495 against `evidence.json`.

**Transform, don't cut (state factory)**
- One section-level factory rebuilds the grid, the "you" square and the positives block at each beat's start state.
- B10's last frame is B11's first frame, and so on.
- B18 must use the same "you" object construction as B10.

**MathTex everywhere:** 99/100, 99/594, 1/6, P(+|D)P(D)/P(+), P(A|B) = P(B|A)P(A)/P(B), 1/100 → 1/6. Use `\mid` for the bar.

**Simplification caption, once (B14):** "each square = one person; expected counts".

**B17 values claim:** caption the "≠" as true **here**. P(B|A) = P(A|B) when P(A) = P(B) (FACTCHECK algebra).

## Notes for the main session (before audio)

1. **Cues:** after audio, rewrite B00 and B01 `cues` and `durationSeconds`, and B03 `durationSeconds`, from the measured `actual_duration_s` and `words.json`. The current values are 2.6 w/s estimates.
2. **TRANSFORM length:** B15 is 21 words (about 8 s). `compile.py` sizes a beat from its measured narration and does not honour a silent hold field. If the morph needs more than about 8 s, lengthen B15 with more short, non-descriptive sentences, not with silence fields.
3. **Outro tail:** check that the BOUT `tail_silence_s: 1.0` is honoured. Film 1 did it, but no tail logic turned up in `generate_audio_kokoro.py` on a quick grep.
4. **Unknown keys:** the `ClaudeTitleOutro` schema has no `handle` or `subline` key. Both are passed because `bookend_check` reads them, and zod strips unknown keys, as it did in film 1.
5. **Pronunciation:** `metadata.pronounce` pins "Salaam" to /səlˈɑːm/. This makes B00 synthesize from phonemes. A listening check is still needed on first audio.

## 2026-11-22 — GATE S + GATE P approved; build to low-res previews

**Approvals.** The main session relayed these. The user's words were **"approve all six"**, given in the main session; this session did not see the message itself. They cover:
- **GATE S:** S1 "Count the Positives" is picked. `tldr-sections-bayes.md` stays in this film folder.
- **GATE P:** the narration is approved as drafted (SCRIPT.md, 860 words).
- **Title:** "Bayes' Theorem: The Positive That's Usually Wrong" is approved.

**Scope of this step**
- Do: audio, silence padding, a whisper check, alignment, `scenes.py`, gates A, W and B, and low-res (`-ql`) previews.
- Do not: render at 4K, run `remotion_scenes.py`, or run `./art run` or `./art final`.

### Audio (GATE 0 prep)
- **Kokoro:** `generate_audio_kokoro.py` ran with Kokoro am_onyx, 17 beats, $0.
- **Silence padding:** `stem-films/tools/pad_silence.py` added B02 lead 0.8 s, BVDT lead 0.5 s, and BOUT tail 1.0 s.
- **Measured total: 265.98 s (4:26).** The 2.6 w/s estimate was 5.5 min; Kokoro ran faster.
- **Whisper "base" diff:** every difference was digit normalisation (or a spelling variant: "Salam", "Nick", "forbear") except three:
  - **"Bayes" heard as "base" or "bass"** (B00, B16, BVDT, BOUT). Whisper "small" hears "Bayes' theorem" in B00, B16 and BOUT with no prompt; base hears it too when prompted. The Kokoro phonemes are /bˈeɪz/ (correct), so this is whisper's language-model prior. **No pronounce entry was added.**
  - **"sick" right after a number heard as "six".** B15 "Ninety-nine sick." became "996", and B13 "one hundred sick tested" became "106". This was a real listener risk in a film about counts, so the narration was reworded (below).
  - **B17 "…zero five nine four: one sixth"** ran together as "0.059416". The colon became a full stop. The new audio is heard as "0.0594. 1.6", which is digit normalisation of "one sixth".
- **"Salaam":** heard as "Salam" (same word). The `metadata.pronounce` pin /səlˈɑːm/ is kept.

### Narration changes after GATE P — FLAGGED for the human reviewer
These were made for audibility and visual accuracy; no facts changed. Each was regenerated with `--only`, re-padded and re-aligned. `make_sheet.py`, `beat_sheet.json` and SCRIPT.md are all in sync; `make_sheet.py` was not re-run.
1. **B13:** "ninety-nine of the one hundred sick tested positive" → "ninety-nine of the one hundred **who are** sick tested positive" (the "106" fix).
2. **B13:** "And it's true, for this **row**:" → "for this **block**:". At 480p the sick, drawn as a 100-cell row, read as a hairline, so they are now a 10 × 10 block (see scenes).
3. **B15:** "Ninety-nine sick." → "Ninety-nine **have the disease**." A first fix, "are sick", was still heard as "or six".
4. **B17:** "…zero five nine four: one sixth." → "…zero five nine four. One sixth."

### Alignment and props
- **`align.py`:** 17/17 aligned, 0 fallback. B13 was re-aligned after its regeneration.
- **B00/B01 `cues` and `durationSeconds`, and B03 `durationSeconds`,** were written from the measured audio and `words.json` (the tldr-attention precedent):
  - B00: [2.29, 7.33, 12.08, 16.25] / 20.35 s
  - B01: [0.58, 6.17, 10.54, 15.58] / 19.2 s
  - B03: 13.72 s
- `bookend_check` PASS and `beat_lint` clean after these edits.

### scenes.py (house pattern from claude-liam-backpropagation)
- **Structure:** 10 scenes, B10_YouArePositive … B19_BaseRateDial.
- **Helpers:** `_load` with the REEL fallback, `cue()`, a frame-quantised `Clock`, `V`, and `box()`.
- **Continuity:** every scene opens on the previous scene's end state, built by shared factories (transform, don't cut).
- **Grid:** 10,000 people as 80 row-VMobjects (one subpath per mark), plus individual squares only for the 100 sick and 495 false positives.
  - Seeds: `random.Random("tldr-bayes-theorem-fn")` picks the missed sick person; `random.Random("tldr-bayes-theorem-fp")` samples 495 of the 9,900 healthy cells.
  - Counts are asserted against `evidence.json`.
- **Colour (main-session rule):** terracotta is never on text or arrows. It appears only on non-text shapes:
  - the B10 stamp outline, the B11 missed-person ring, and the B12/B13 false-positive cells flashing
  - outlines round B14's question, B15's 1/6, B16's theorem, B17's ≠ and B18's 9,900
  - the B19 curve marker
- **Fill:** late layouts are ghosted (GHOST) from t = 0.2 in B10, B16 and B17.
- **Palette deviations:**
  - DIM is #7A7E86, not the skill's #8B8F96. At preview size the 10,000-mark grid at #8B8F96 anti-aliased to 0.277 luminance separation, below GATE V's 0.30.
  - Cleared negatives use CLEAR #E6E2D8, lighter than the GHOST scaffold, so the 495 lit marks read.
- **Fixes found by looking at frames:**
  - B17 equation clipped at the left edge → new layout: equation centred top, glossary left, sentence/worked/claim right.
  - B19 y-axis drawn at the right (x = log₁₀ ≤ 0) → x = log₁₀ + 3.
  - B10 stamp touching P(sick); B16 ghost mismatch and spotlight crossing the fraction bar; B18 HOOK square re-entering over the block.
  - Stub-unsafe `isinstance(Mobject)` and VGroup slicing (GATE A).
  - Counters and chip outside ±6.0 (GATE B).

### Gates (per scene, final run)
| Scene | A (isolated copy) | W | B (--curve-strict) | clip vs audio | V frame check 50% / 85% |
|---|---|---|---|---|---|
| B10_YouArePositive | 0 | 0 | 0 | +1.1% | 61.1 / 61.2% clean |
| B11_TenThousand | 0 | 0 | 0 | +0.7% | 74.8 / 74.8% clean |
| B12_FalseAlarms | 0 | 0 | 0 | +0.4% | 74.6 / 75.2% clean |
| B13_WrongCrowd | 0 | 0 | 0 | +0.2% | 75.4 / 76.0% clean |
| B14_OnlyThePositives | 0 | 0 | 0 | +0.7% | 66.5 / 76.1% clean |
| B15_OneInSix | 0 | 0 | 0 | +0.5% | 66.5 / 70.6% clean |
| B16_BuildBayes | 0 | 0 | 0 | +0.0% | 61.0 / 61.2% clean |
| B17_ReadTheLine | 0 | 0 | 0 | +0.8% | 69.6 / 69.9% clean |
| B18_BackToYou | 0 | 0 | 0 | +0.7% | 62.8 / 63.4% clean |
| B19_BaseRateDial | 0 | 0 | 0 | +0.5% | 80.3 / 81.1% clean |

**How the V column was measured:** `final_frame_check.analyze_frame` (GATE V's own function, imported read-only) on 480p preview frames. It covers edge-bleed, fill ≥ 55% and contrast ≥ 0.30. The real GATE V runs later on the compiled cut.

**Previews**
- `manim -ql --fps 24 --disable_caching`, media in this session's scratchpad (outside the film folder).
- Frames were inspected by eye at 15/50/85/99% of every scene.
- **Residual:** two cues run 0.11 s late (B14 "ninety-nine who", B18 "these five").

**Other notes**
- Gate B leaves a MathTex cache in `media/Tex/` and `layout_audit.*` in the film folder; there are no `media/<beat>.mp4` slots.
- **Not done (by instruction):** 4K render, `remotion_scenes.py`, `./art run`, `./art final`. The bookend Remotion beats have not been rendered.

## 2026-11-23 — resume check (after the usage-limit reset)
- The main session asked for the scenes and previews to be finished. They had already been finished in the previous turn; this pass re-verified them against the current `scenes.py`.
- **Gates:** A (isolated copy), W and B were re-run on all 10 scenes, and all exit 0. B10 and B17 were re-rendered so every preview postdates the latest `scenes.py`.
- **Late cues fixed:** the two 0.11 s late cues are gone. B14's regroup move and B18's opening play were shortened from 0.8 to 0.65 s. B14 and B18 were re-gated (A/W/B = 0) and re-previewed: +0.3% and +0.4% against audio, V frame check clean.
- **Final state:**
  - All 10 previews are within +0.0 to +1.1% of their audio, and no cue is late.
  - The GATE V frame check is clean on all 20 frames sampled at 50% and 85% (fill 61–81%).
  - Measured film duration: 265.98 s (4:26).

## 2026-11-23 — post-GATE-P narration edits approved
- The human approved all four narration edits listed above (B13 ×2, B15, B17). They wrote "Approve the edits" in the main session.

## Final QC pass 1 — B12 hidden-marks fix (2026-11-23)
- First final passed every gate (V, T, strip 133/133, master, loudness −24.66 LUFS) but hand QC of the contact sheets caught a real defect in B12_FalseAlarms: from ~45% to the end of the beat the grid was blank. The sick block, "you" badge, scan bar and all 495 false-alarm marks were invisible, so "light up" showed nothing.
- Cause: ManimCE's `play()` adds the `LaggedStart` Group of row animations to the top of the draw order, so the cleared rows were painted over everything added earlier.
- Fix: `set_z_index(1)` on sick, badge, fps, bar before the sweep. Low-res check: marks flash terracotta at "light up", dim to grey, and the end state matches B13's first frame. Stale clips moved to `_superseded/` (B12_hidden_marks.mp4, B12_manim_hidden_marks.mp4). Full queue re-run.

## FINAL — delivered (2026-11-23)
- exports/landscape/tldr-bayes-theorem.mp4 — 266.3 s (4:26), 3840×2160, 24 fps, h264/yuv420p
- GATE V 34 frames BLOCKER 0 MAJOR 0 · GATE T PASS (B12 midpoint included) · strip/label check PASS 133/133 · master PASS · loudness −24.66 LUFS, tp −3.07 dBTP
- sha256 f07916d9d832968cd8f7372c9d27712cf7733d98599f2026d7072c9b4da63e3a = .verified.json
- Hand QC of all 17 beats (15/50/85% sheets + extra B12/B15 frames): B12 marks visible and continuous into B13; B15 morphs settle cleanly.
- Advisories only (not gates): §8.10 card-recital on B00/B01/BVDT and the TL;DR cold-open skin lint. Both are inherent to the tldr format and also appear on tldr-attention.

## Format conversion → ai-explainer (2026-11-24)
- **Why:** the user asked for this film to match the other five (ai-explainer spine), with no footer.
- **Approval (GATE P, chat, 2026-11-24):** the user approved the new B00 cold open and B01 hesitant-writer narration as previewed, with "Hello" as the greeting (chosen for all three converted films).
- **Change:** TL;DR B00–B03 (What, Why, Question, Terms) were retired to `_superseded/format-tldr/`. They are replaced by B00 `ClaudeComposerAsk` and B01 `BrutalistHesitantWriter` (lead 0.8 s, fontSize 145, lineSpacing 3.3).
  - The Terms card defined sensitivity and base rate. Those definitions now sit in B00's on-screen answer lines, and B01's narration defines base rate.
  - Body B10–B19 (including the B12 z-order fix), BVDT, BHTF and BOUT are unchanged.
- **B01 sizing:** fontSize 145 measured 49% fill before render, so the beat was re-rendered at 160 (59% fill). The fontSize 145 clip is in `_superseded/b01_underfill/`.
- **FINAL (ai-explainer), 2026-11-24:** 223.7 s, 3840×2160. GATE V 0/0, GATE T PASS, bookend PASS, strip check 112/112, master PASS, −24.61 LUFS. sha256 c01206b09541201566217d4d971accf9bd9a573318b018cbb94c68623b58d422 matches .verified.json. Hand QC of all 15 beats is clean. Copied to the user's "Footer removed" folder.
- **Docs refreshed (2026-11-24):**
  - SCRIPT.md, SHOTLIST.md and CHECKS-REPORT.md were regenerated from the current beat sheet with `stem-films/tools/refresh_converted_docs.py`. Each keeps its pre-conversion content verbatim under a History heading. The originals are backed up in `_superseded/format-*/docs/`.
  - FACTCHECK.md has a dated conversion section appended that checks every new spoken and on-screen line; the earlier rows are unchanged.
