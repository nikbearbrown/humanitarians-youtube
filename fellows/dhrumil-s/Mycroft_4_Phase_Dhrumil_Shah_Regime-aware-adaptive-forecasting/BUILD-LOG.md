# BUILD-LOG — Mycroft Phase 4 (9:16)

| Item | Value |
|---|---|
| Build date | 2026-09-30 |
| Builder | Claude (Claude Code) for Dhrumil Shah |
| Plan | `PRODUCTION-PLAN.md` (14 scenes, deliverables 1–14) |
| Source material | `Mycroft_Phase4_Regime_Aware.ipynb` + its executed output (`docs/NOTEBOOK-OUTPUT.txt`) |
| Style reference | `Mycroft_Thesisguard_9x16_4k(Dhrumil_Shah).mp4` — **style only**, no content reused |
| Composition | `MycroftPhase4-9x16` · cover `MycroftPhase4Cover9x16` (registered in `runtime/remotion/src/Root.tsx`, folder Mycroft-Phase-4) |
| Remotion namespaces | `src/mycroft-phase4-9x16/`, `public-mycroft-phase4-9x16/` — no other film touched |
| Design canvas | 1080 × 1920, native 9:16 |
| Master method | `--scale=2` → 2160 × 3840, H.264 CRF 16, AAC 320 kbps; smaller masters Lanczos-downscaled |
| FPS | 30 |

## Audio is the clock

| Item | Value |
|---|---|
| Engine / voice | Kokoro-82M (kokoro-onnx) · **`am_onyx`** · speed 1.0 · 24 kHz |
| Voice rationale | The film opens "Hi, I am Dhrumil Shah" — a male voice matches the presenter |
| Words | 491 |
| Narration duration | 182.91 s (measured, no stretching) |
| End-card hold | 2.00 s |
| Video duration | **184.91 s (3:05)** |
| Music / SFX | code-synthesised bed, 14 SFX cues, side-chain ducked under narration |
| Final mix | −14 LUFS target · peak −1.4 dBFS · 48 kHz stereo |

Measured beat durations (s): S01 13.05 · S02 9.92 · S03 10.39 · S04 11.15 · S05 12.39 ·
S06 14.83 · S07 12.90 · S08 15.16 · S09 13.16 · S10 11.88 · S11 16.38 · S12 11.41 ·
S13 13.63 · S14 16.65

The plan estimated 196 s from a words-per-minute guess; the measured narration came in at 182.91 s.
The beat sheet now carries the **measured** values, not the estimates.

## Captions

`captions/VALIDATION.md`: measured per-sentence cues → burned-in captions, 0 overlaps,
**0 single-word captions**, longest wrapped line 27 characters (2 lines max), last caption ends at
182.51 s. Cue times come from per-sentence measured audio, character-proportional inside a
sentence — never from a words-per-minute estimate.

## Claim discipline in the finished film

Every figure on screen is quoted from the author's executed notebook run; the notebook was not
re-run and the dataset is not in this package, so **nothing was recomputed**. Cross-checked
against `docs/FACTCHECK.md` (F1–F37, W1–W5):

- **The overall result is stated as weak, twice.** S10 carries a full-width terracotta card:
  "Regime awareness did not make the model predictive." S14 opens "Not a better score. A better map."
- **`calm_bull` is drawn below the 0.50 chance line**, in terracotta, because it is 0.4909.
- **`stressed_bear`'s absence is stated on screen** in S11: "stressed_bear had fewer than 100 test
  rows and was not scored."
- **Only `calm_bull`'s threshold (0.50) appears**, in the S13 source line — it is the only one
  printed in the executed output. No number is shown for the other three regimes.
- **Feature importance is described as "≈ 0.017 AUC — small in absolute terms"** alongside the
  "roughly 11×" comparison, so the lead is not mistaken for a large effect.
- **The two figures are the notebook's own output**, extracted from the `.ipynb` display data and
  carried over unchanged. The negative bars in the importance chart are not cropped.
- **S03's two sparklines are labelled** `illustrative shapes — not plotted data` in the source line.
- **Terracotta is reserved for honest limits** — never used to celebrate a result.
- The advisory line appears in S13 and again on the S14 end card.

## QC issues found and fixed

| # | Stage | Issue | Fix |
|---|---|---|---|
| 1 | Audio | The music generator needs `music_section` per beat and `sound_design.sfx[].type`; the authored sheet had neither | Sections mapped per beat; the sfx key renamed to `type` |
| 2 | Captions | One stranded single-word caption ("twenty-twenty-six.") | Caption merger widened for captions under 3 words, so a short tail folds into the previous cue |
| 3 | Storyboard | S05's connector arrow appeared ~1.2 s before the box it points at | Arrow timing tied to the **next** box's reveal |
| 4 | Storyboard | S13's queue rows arrived only on the final sentence, leaving the frame empty mid-scene | Rows cued to "enter the research queue" instead |
| 5 | Storyboard | S11's bars read small for the scene that carries the finding | Bar scale 6200 → 7600 px per AUC point, taller rows, block lowered |

Storyboard pass: 14 scenes at 70% of each beat. Review cut (540 × 960): 184.96 s, clean.
Late-reveal sheet (`_qc/late_sheet.png`, 95% of every beat): all 14 scenes complete, nothing
clipped, captions inside the bottom band.

## Final render and output probe

See `_qc/OUTPUT-PROBE.md`. Decode = a full `ffmpeg -f null` pass with no errors.

## Reproduce

```bash
python scripts/generate_narration.py    # Kokoro, per sentence, measured
python scripts/build_captions.py
python scripts/generate_music_sfx.py
python scripts/mix_audio.py
python scripts/sync_to_remotion.py
python scripts/render_masters.py storyboard | review | late | master | cover | qc
```

Rendering needs the `brutalist.art-main` workspace: Remotion renders from its composition
registry, so a standalone copy of this folder is a complete source package but not a render
environment.

## Human review still required

| Gate | Status |
|---|---|
| Re-run the notebook and re-verify `docs/FACTCHECK.md` F1–F37 on the publish date | ⏳ |
| Move the regime-label assignment to train-only statistics (W2) and re-check the names | ⏳ |
| Narration read aloud against the animatic (Gate P) | ⏳ |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
