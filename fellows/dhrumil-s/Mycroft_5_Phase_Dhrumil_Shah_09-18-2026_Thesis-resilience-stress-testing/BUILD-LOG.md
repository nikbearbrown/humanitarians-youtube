# BUILD-LOG — Mycroft Phase 5 (9:16)

| Item | Value |
|---|---|
| Build date | 2026-09-30 |
| Builder | Claude (Claude Code) for Dhrumil Shah |
| Source | `source/Mycroft_Phase5_Thesis_Resilience.ipynb` + executed output (`docs/NOTEBOOK-OUTPUT.txt`) |
| Style reference | `mycroft_phase3_4k_9x16.mp4` — **style only**, content entirely new |
| Composition | `MycroftPhase5-9x16` · cover `MycroftPhase5Cover9x16` (folder Mycroft-Phase-5 in `runtime/remotion/src/Root.tsx`) |
| Design canvas | 1080 x 1920, mastered at 2160 x 3840 via `--scale=2` |
| FPS | 30 |

## Audio is the clock

| Item | Value |
|---|---|
| Engine / voice | Kokoro-82M · `am_onyx` · speed 1.0 · 24 kHz |
| Words | 614 |
| Narration | 226.86 s (measured, no stretching) |
| End hold | 2.00 s |
| Video | **228.86 s (3:49)** — inside the requested 2.5–4 min |
| Music / SFX | code-synthesised bed, 14 cues, side-chain ducked |
| Final mix | −14 LUFS target · peak −1.5 dBFS · 48 kHz stereo |

Measured beats (s): S01 13.60 · S02 10.90 · S03 17.43 · S04 17.97 · S05 17.87 · S06 15.54 · S07 12.78 · S08 19.81 · S09 17.72 · S10 16.21 · S11 15.81 · S12 12.23 · S13 16.94 · S14 22.06

**Runtime correction during the build.** The first narration pass measured 257.11 s (4:17),
over the 4-minute ceiling. Six scenes (S02, S04, S08, S10, S12, S14) were rewritten shorter and
the audio regenerated — speech was never stretched or sped up to hit a target.

## Captions

0 overlaps · 0 single-word captions · shortest 1.16 s · longest wrapped line 29 characters ·
last caption ends at 226.46 s. Cue times come from per-sentence measured audio.

## Claim discipline

Every figure is quoted from the executed notebook; the notebook was not re-run and the dataset is
not in this package, so nothing was recomputed. Cross-checked against `docs/FACTCHECK.md`
(F1–F35, W1–W5).

- **S13 exists to bound the claim.** It shows the flagged large-move rate (21.9%, n = 62,831)
  against the unflagged rate (19.1%, n = 120,707), states the difference is real but small, notes
  the flag fires on about a third of all rows, and ends on **"This is a diagnostic, not a forecast."**
- **No profitability, performance or prediction-accuracy claim appears anywhere.**
- The S10 loss-distribution *shape* is schematic and its source line says so; only ORCL's VaR
  (−46.1%) and CVaR (−51.7%) are real values.
- Beta is described as being to the **equal-weighted dataset market**, not an external index.
- The advisory — research decision support, not financial advice, not an autonomous trading
  system — appears in the S01 source line, on the S12 strip and on the end card.
- Both charts are the notebook's own matplotlib output, carried over unchanged.

## QC issues found and fixed

| # | Stage | Issue | Fix |
|---|---|---|---|
| 1 | Authoring | A shell heredoc broke on apostrophes in the narration | Beat sheet authored as `scripts/make_beat_sheet.py` instead |
| 2 | Runtime | First pass ran 4:17, over the brief's 4-minute ceiling | Six scenes rewritten tighter, narration regenerated (not stretched) |

Storyboard pass: 14 scenes at 70%. Late-reveal sheet (`_qc/late_sheet.png`, 95% of every beat):
all 14 complete, nothing clipped, captions inside the bottom band.

## Final render and output probe

4K render 1035 s (`--scale=2`, concurrency 8), then Lanczos downscales. Decode = full
`ffmpeg -f null` pass, no errors.

| File | Size | Resolution | FPS | Duration | Video | Audio | Decode |
|---|---|---|---|---|---|---|---|
| Mycroft-Phase-5-4k(9x16)_Dhrumil_Shah.mp4 | 33.8 MB | 2160x3840 | 30/1 | 228.93 s | h264 | aac 48000 Hz | PASS |
| Mycroft-Phase-5-1080x1920(9x16)_Dhrumil_Shah.mp4 | 14.3 MB | 1080x1920 | 30/1 | 228.93 s | h264 | aac 48000 Hz | PASS |
| Mycroft-Phase-5-720x1280(9x16)_Dhrumil_Shah.mp4 | 9.8 MB | 720x1280 | 30/1 | 228.93 s | h264 | aac 48000 Hz | PASS |
| Mycroft-Phase-5-proxy-540x960(9x16)_Dhrumil_Shah.mp4 | 6.0 MB | 540x960 | 30/1 | 228.93 s | h264 | aac 48000 Hz | PASS |

## Human review still required

| Gate | Status |
|---|---|
| Re-run the notebook and re-verify `docs/FACTCHECK.md` F1–F35 on the publish date | ⏳ |
| Confirm the ticker examples are still appropriate to show | ⏳ |
| Narration read aloud against the animatic | ⏳ |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
