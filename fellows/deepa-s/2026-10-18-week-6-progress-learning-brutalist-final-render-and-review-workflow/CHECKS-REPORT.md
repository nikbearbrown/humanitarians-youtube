# Corrected Week 6 Progress — final technical QC

Verified 2026-10-20. **PASS — both formats.**

| Check | Landscape | Portrait |
| --- | --- | --- |
| Native dimensions | 3840×2160 | 2160×3840 |
| Codec / pixel format / fps / audio stream | H.264 / yuv420p / 24 / present | H.264 / yuv420p / 24 / present |
| Gate T typography, minimum size, contrast, clipping and safe areas | PASS, 9 beats | PASS, 9 beats |
| Gate V final-frame checks | PASS, no blockers/major defects | PASS, no blockers/major defects |
| Beat lint, source safety and shape gate | PASS | PASS |
| Filled visual slots; placeholder slates | 9/9; none | 9/9; none |
| Master and audio loudness/peak/audibility checks | PASS | PASS |
| Clock duration and beat audio synchronization | PASS | PASS |
| Scene order, motion-phase samples and cut boundaries | PASS | PASS |
| Full video/audio decode; file hashes | PASS | PASS |
| Black frames ≥ 2 frames / silence ≥ 2 seconds | None detected | None detected |

The corrected narrative was compared with Deepa's explicit task, the Week 6 review-support account and preserved production logs; see [content audit](CONTENT-AUDIT.md). The review work is limited to the two Uday Mycroft submissions. No final team approval, public publication, hours, dates or URLs are invented.

Both outputs ran through `art final`, including typography and final-frame gates. Full streams were decoded; three motion-phase frames per beat and both sides of each cut were compared with source scene renders. Contact sheets were visually inspected. Minimum decoded audio correlation to source beats was 0.989690, with zero detected lag at checked beat segments. The toolkit's missing `clock_check.py` subcheck was independently covered by ffprobe versus summed frame-aligned beat durations, within one frame. No QC threshold was disabled.

The new narration initially exceeded the true-peak ceiling; applying -2 dB gain brought it within the required range. The established corrected layout passed all 18 native-4K preview checks. Narration/scene content was regenerated only for this project; other six deliverables were preserved.

Machine receipts and frame/contact evidence are in ignored `_qc/` folders. [TYPECHECK.md](TYPECHECK.md), [portrait TYPECHECK.md](vertical/TYPECHECK.md), [MASTERCHECK.md](MASTERCHECK.md), [portrait MASTERCHECK.md](vertical/MASTERCHECK.md), [LOUDNESS.md](LOUDNESS.md), and [portrait LOUDNESS.md](vertical/LOUDNESS.md) retain tool results.

Technical QC is separate from human approval. Deepa will review these corrected videos before upload. [Files and hashes](DELIVERY.md).
