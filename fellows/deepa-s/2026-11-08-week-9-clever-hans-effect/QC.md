# Final redesigned video QC

**Technical QC: PASS. Visual direction: approved by Deepa. Final human video review: pending.**

All replacement renders completed before the continuation on November 10, 2026. This continuation verified their hashes and stream metadata against the completed full QC, inspected encoded scene samples and endings, and promoted the validated copies. No completed render or narration was regenerated.

| Format | Dimensions | FPS | Seconds | Frames | LUFS | True peak dBTP | QC |
|---|---|---:|---:|---:|---:|---:|---|
| Landscape | 1920×1080 | 24 | 183.875000 | 4413 | -18.95 | -1.94 | PASS |
| Portrait | 1080×1920 | 24 | 183.875000 | 4413 | -18.95 | -1.94 | PASS |

## Validation evidence

- Full video/audio decode passed with errors treated as fatal. H.264 video and AAC audio are present. Dimensions, 24 fps, frame counts and durations match both Beat Sheets; all durations are 175–185 seconds.
- Scene-wise decoded-audio correlation against the unchanged original narration exceeded 0.97; every narrated sentence had audible signal. Caption boundaries and narration scripts are unchanged. These checks verify alignment/completeness, not human pronunciation approval.
- Motion was sampled throughout every scene. Final-frame Gate V passed both formats with no blockers or major defects, checking safe areas, frame coverage, empty frames and declared text-region contrast. Illustration colors were not treated as text.
- All encoded scene contact sheets and extracted closing frames were inspected. The approved warm illustrated environments replace the plain blue backgrounds. Headings and caption wrapping were checked using the actual fonts; native portrait compositions stack/reflow rather than crop. No clipping was identified in checked samples.
- TypeScript, JSON, project schema, Beat Sheet timing/lint, content checks and local Markdown links are validated.
- Original narration WAVs, scripts, captions and source-citation JSON match pre-redesign SHA-256 hashes. Original MP4 backups also match their recorded hashes.
- Final full-playback human review remains pending. Technical PASS does not establish publication or approval.

## Final files

- `mp4/Week9_STEM_16x9.mp4`
  - SHA-256: `cee1501eddc919ccf836b8fc78c9bc58e6356120d63bb6a1f57d7d9f74b6646b`
  - Minimum scene audio correlation: 0.988313; minimum sentence RMS: -20.77 dBFS; maximum caption lines: 2.
- `vertical/mp4/Week9_STEM_9x16.mp4`
  - SHA-256: `4bebab9bd3138a88944984b0098e79e517669dbf0ff8616eae32d255e5c50e7d`
  - Minimum scene audio correlation: 0.988313; minimum sentence RMS: -20.77 dBFS; maximum caption lines: 3.

## Preserved history

Original exports and the earlier QC record remain locally under `_qc/pre-redesign/`. The older technical PASS did not constitute acceptance of the blue visual design. New raw QC records, contact sheets, ending frames and candidate exports remain under `_qc/redesigned-final/`. Keep all original MP4 backups until Deepa approves all eight redesigned videos. Media, caches and generated QC artifacts remain excluded from Git. See [RENDER.md](RENDER.md) for reproduction commands.
