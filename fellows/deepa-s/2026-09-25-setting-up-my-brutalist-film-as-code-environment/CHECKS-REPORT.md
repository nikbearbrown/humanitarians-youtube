# Narration technical QC

- Nine beat MP3s: decode PASS; non-silence PASS; no full-scale PCM samples.
- Joined review WAV: decode PASS; 68.843 seconds; 48 kHz stereo 16-bit PCM; peak -4.54 dBFS.
- Requested approximate 60–90 seconds: PASS.
- Exact user opening and closing: preserved.
- Landscape/portrait narration: identical text and independently copied, hash-matched MP3 files.
- Both Beat Sheets: runtime structural/voice checks PASS.
- Content evidence: user-supplied historical account, current receipts explicitly labeled; no fabricated terminal results.
- Human listening/wording/pronunciation approval: PENDING.
- Visual/frame/typography/video QC: not started; visual production awaits narration approval.

Machine-readable details: audio-review/audio-checks.json.

## Render and review-cut QC — Content #4

- Narration human approval: recorded as passed; source WAV and all beat MP3 SHA-256 hashes match the approved hash manifest.
- Final review cuts: landscape 3840×2160 and portrait 2160×3840; both H.264/yuv420p, 24 fps, 69.0 seconds, with one AAC narration track.
- Complete decode: PASS for both MP4s (`ffmpeg -xerror`).
- Master technical QC: PASS for both (dimensions, frame rate, codecs, pixel format, duration).
- Loudness QC: PASS for both; -23.73 LUFS integrated, -4.52 dBTP true peak; all nine beats non-silent.
- Visual/frame gate: PASS; 18 samples per cut, zero blockers and zero major findings.
- Typography and safe area: PASS; all 18 native scene layouts per format audited; no text outside 5% frame inset and no DOM text overflow. Portrait was composed at 1080×1920 and rendered at 2160×3840, not cropped from landscape.
- Human watch-the-cut gate: pending.
