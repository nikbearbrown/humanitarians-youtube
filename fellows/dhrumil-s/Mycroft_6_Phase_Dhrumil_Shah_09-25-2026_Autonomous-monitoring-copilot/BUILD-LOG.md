# BUILD-LOG — Mycroft Phase 6 (9:16)

| Item | Value |
|---|---|
| Build date | 2026-09-30 |
| Builder | Claude (Claude Code) for Dhrumil Shah |
| Source | `source/Mycroft_Phase6_Autonomous_Monitoring.ipynb` + executed output |
| Style reference | `mycroft_phase3_4k_9x16.mp4` — **style only**, content entirely new |
| Composition | `MycroftPhase6-9x16` · cover `MycroftPhase6Cover9x16` (folder Mycroft-Phase-6) |
| Design canvas | 1080 x 1920, mastered at 2160 x 3840 via `--scale=2` |
| FPS | 30 |

## Audio is the clock

| Item | Value |
|---|---|
| Engine / voice | Kokoro-82M · `am_onyx` · speed 1.0 · 24 kHz |
| Words | 628 |
| Narration | 229.33 s (measured, no stretching) |
| End hold | 2.00 s |
| Video | **231.33 s (3:51)** — inside the requested 2–4 min |
| Music / SFX | code-synthesised bed, 14 cues, side-chain ducked |
| Final mix | −14 LUFS target · peak −1.5 dBFS · 48 kHz stereo |

Measured beats (s): S01 14.03 · S02 12.94 · S03 14.55 · S04 15.62 · S05 15.04 · S06 14.64 · S07 14.10 · S08 16.07 · S09 16.79 · S10 12.83 · S11 16.73 · S12 16.25 · S13 23.33 · S14 26.41

## Captions

0 overlaps · 0 single-word captions · shortest 1.01 s · longest wrapped line 29 characters ·
last caption ends at 228.93 s. Cue times from per-sentence measured audio.

## Claim discipline

Every figure is quoted from the executed notebook; nothing was recomputed. Cross-checked against
`docs/FACTCHECK.md` (F1–F41, W1–W5).

- **S13 bounds the claim.** It shows the notebook's own priority-vs-large-move figure, the four
  headline rates (17.8% / 34.4% / 39.4% / 40.6%), **names the dips at 3, 5 and 7**, names the small
  sample (n = 64 at priority 9), and closes on "A historical diagnostic, not a forecast."
- Agent E is described as "the only machine-learning model here" — accurate: A–D are deterministic
  rules and rank thresholds.
- The isolation forest is stated as **fit on training dates only**, which the code does.
- The priority score is presented as ranking attention, never outcomes.
- No profitability, performance or prediction-accuracy claim appears anywhere.
- The advisory string the notebook writes into every queue row appears in the S01 source line, the
  S12 strip and the end card.
- `human_decision` / `human_rationale` are shown as `null`, captioned "left empty by design".

## QC

Storyboard pass: 14 scenes at 70%. Late-reveal sheet (95% of every beat): all 14 complete, nothing
clipped, captions inside the bottom band. QC sheet: 14 stills pulled from the 1080 x 1920 master.

## Final render and output probe

4K render 1046 s (`--scale=2`, concurrency 8), then Lanczos downscales. Decode = full
`ffmpeg -f null` pass, no errors.

| File | Size | Resolution | FPS | Duration | Video | Audio | Decode |
|---|---|---|---|---|---|---|---|
| Mycroft-Phase-6-4k(9x16)_Dhrumil_Shah.mp4 | 31.2 MB | 2160x3840 | 30/1 | 231.38 s | h264 | aac 48000 Hz | PASS |
| Mycroft-Phase-6-1080x1920(9x16)_Dhrumil_Shah.mp4 | 13.6 MB | 1080x1920 | 30/1 | 231.38 s | h264 | aac 48000 Hz | PASS |
| Mycroft-Phase-6-720x1280(9x16)_Dhrumil_Shah.mp4 | 9.6 MB | 720x1280 | 30/1 | 231.38 s | h264 | aac 48000 Hz | PASS |
| Mycroft-Phase-6-proxy-540x960(9x16)_Dhrumil_Shah.mp4 | 5.9 MB | 540x960 | 30/1 | 231.38 s | h264 | aac 48000 Hz | PASS |

## Human review still required

| Gate | Status |
|---|---|
| Re-run the notebook and re-verify F1–F41 on the publish date | ⏳ |
| Confirm the ticker examples are still appropriate to show | ⏳ |
| Narration read aloud against the animatic | ⏳ |
| Publishing | **Not authorised.** A rendered master is not permission to upload. |
