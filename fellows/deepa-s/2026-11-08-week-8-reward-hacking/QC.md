# Final redesigned video QC

**Technical QC: PASS. Visual direction: approved by Deepa. Final human video review: pending.**

All replacement renders completed before the continuation on November 10, 2026. This continuation verified their hashes and stream metadata against the completed full QC, inspected encoded scene samples and endings, and promoted the validated copies. No completed render or narration was regenerated.

| Format | Dimensions | FPS | Seconds | Frames | LUFS | True peak dBTP | QC |
|---|---|---:|---:|---:|---:|---:|---|
| Landscape | 1920×1080 | 24 | 179.791667 | 4315 | -18.86 | -1.97 | PASS |
| Portrait | 1080×1920 | 24 | 179.791667 | 4315 | -18.86 | -1.97 | PASS |

## Validation evidence

- Full video/audio decode passed with errors treated as fatal. H.264 video and AAC audio are present. Dimensions, 24 fps, frame counts and durations match both Beat Sheets; all durations are 175–185 seconds.
- Scene-wise decoded-audio correlation against the unchanged original narration exceeded 0.97; every narrated sentence had audible signal. Caption boundaries and narration scripts are unchanged. These checks verify alignment/completeness, not human pronunciation approval.
- Motion was sampled throughout every scene. Final-frame Gate V passed both formats with no blockers or major defects, checking safe areas, frame coverage, empty frames and declared text-region contrast. Illustration colors were not treated as text.
- All encoded scene contact sheets and extracted closing frames were inspected. The approved warm illustrated environments replace the plain blue backgrounds. Headings and caption wrapping were checked using the actual fonts; native portrait compositions stack/reflow rather than crop. No clipping was identified in checked samples.
- TypeScript, JSON, project schema, Beat Sheet timing/lint, content checks and local Markdown links are validated.
- Original narration WAVs, scripts, captions and source-citation JSON match pre-redesign SHA-256 hashes. Original MP4 backups also match their recorded hashes.
- Final full-playback human review remains pending. Technical PASS does not establish publication or approval.

## Final files

- `mp4/Week8_STEM_16x9.mp4`
  - SHA-256: `48ffb0869c794e31d24b67a4cc7b7193a14efb2d235514f9cb0ab39656894df9`
  - Minimum scene audio correlation: 0.988253; minimum sentence RMS: -20.84 dBFS; maximum caption lines: 1.
- `vertical/mp4/Week8_STEM_9x16.mp4`
  - SHA-256: `ec3c7da29c38168ecc96f5d4a18f8bca13a2484427663223482b5728d97039cd`
  - Minimum scene audio correlation: 0.988253; minimum sentence RMS: -20.84 dBFS; maximum caption lines: 2.

## Preserved history

Original exports and the earlier QC record remain locally under `_qc/pre-redesign/`. The older technical PASS did not constitute acceptance of the blue visual design. New raw QC records, contact sheets, ending frames and candidate exports remain under `_qc/redesigned-final/`. Keep all original MP4 backups until Deepa approves all eight redesigned videos. Media, caches and generated QC artifacts remain excluded from Git. See [RENDER.md](RENDER.md) for reproduction commands.
