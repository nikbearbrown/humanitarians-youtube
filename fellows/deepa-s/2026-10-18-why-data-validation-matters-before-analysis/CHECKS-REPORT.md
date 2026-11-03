# Final-video checks

Verified 2026-10-19. **PASS — landscape and portrait.**

| Check | Landscape | Portrait |
| --- | --- | --- |
| Required 4K dimensions; H.264/yuv420p; 24 fps | PASS | PASS |
| Gate T typography, text size, safe areas, contrast and clipping | PASS — 8/8 beats | PASS — 8/8 beats |
| Gate V final-frame visual checks | PASS — 0 blockers/major findings | PASS — 0 blockers/major findings |
| Beat lint, shape gate and source validation | PASS | PASS |
| Filled visual slots / placeholder slates | 8/8 video; no placeholders | 8/8 video; no placeholders |
| Narration audibility and loudness/true peaks | PASS | PASS |
| Frame-aligned clock duration | PASS | PASS |
| Beat-by-beat narration synchronization | PASS | PASS |
| Scene order, motion-phase samples and cut boundaries | PASS | PASS |
| Full video/audio decode with ffmpeg error checking | PASS | PASS |
| Black frames ≥ 2 frames / silence ≥ 2 seconds | None detected | None detected |
| Final-file SHA-256 matches export receipt | PASS | PASS |

## Methods and boundaries

`art final` ran Gate T before export, then required preflight and final-frame gates before atomic promotion. `master_check.py` and `loudness_check.py` passed. The installed toolkit lacks `clock_check.py`; its skipped clock subcheck was covered independently by comparing ffprobe duration with the sum of frame-aligned beat durations (within one frame), rather than treating a skipped check as evidence.

All frames and audio were decoded. At three motion phases per beat and both sides of cuts, final frames were compared with the corresponding scene source. Contact sheets from every beat were visually inspected. Text motion is bounded translation with fixed type/layout; portrait uses stacked cards, larger type, shorter labels and a 14% bottom safe area. These automated checks and sampled visual inspection do not claim a human watch-through approval.

Decoded final audio was compared against each approved source beat at its timeline position. Minimum waveform correlation across both formats: 0.989327; detected lag: 0 seconds at the checked beat segments. Narration wording, voice, speed and recording hashes remain unchanged.

Detailed machine receipts, frame comparisons and contact sheets are retained in ignored `_qc/` folders for both formats. [TYPECHECK.md](TYPECHECK.md), [portrait TYPECHECK.md](vertical/TYPECHECK.md), [MASTERCHECK.md](MASTERCHECK.md), [portrait MASTERCHECK.md](vertical/MASTERCHECK.md), [LOUDNESS.md](LOUDNESS.md) and [portrait LOUDNESS.md](vertical/LOUDNESS.md) retain the tool results.

## Corrections

Enlarged small landscape text; removed low-opacity text; enlarged and reflowed portrait typography and moved branding inside its safe area. Rerendered affected scenes. Week 5 STEM landscape B06 replaced arrow glyphs with equivalent words after a minimum-size failure. Earlier failed/preliminary outputs remain in ignored QC storage. A browser launch/cache issue and a last-frame sampling boundary issue were corrected; no validation threshold was disabled.

[Final files, exact durations and hashes](DELIVERY.md). Human narration approval is recorded; final human cut approval, upload and publication are not claimed.
