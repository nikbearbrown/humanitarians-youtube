# Rebuild instructions

Use Node, FFmpeg/ffprobe, and the existing Brutalist toolkit Python environment with Kokoro ONNX and its model/voices. Dependencies are pinned in package.json; install with `npm install` if a compatible runtime is not already available. Generated dependencies and media must not be committed.

From the project directory:

```bash
ART_HOME=/path/to/brutalist.art /path/to/brutalist.art/.venv/bin/python src/generate_audio.py .
REMOTION_MODULES=/absolute/path/to/node_modules node src/render.cjs . --preview
REMOTION_MODULES=/absolute/path/to/node_modules node src/render.cjs . --render
```

The existing local runtime defaults to `~/Downloads/brutalist.art-main/runtime/remotion/node_modules`. Set CHROME_BIN if Chromium is elsewhere. The renderer needs permission to bind a local preview port. WAV sentence caches avoid repeating unchanged TTS work. Do not regenerate reviewed narration without reason.

Audio is the clock: each scene rounds up to a 24 fps frame boundary. No atempo/time stretching is used. `captions.json` contains measured sentence boundaries, not ASR word timings. Rendered video is H.264; the mux uses AAC audio with FFmpeg loudnorm target −18 LUFS and −2 dBTP, then trims to the exact frame duration. Actual measurements belong in QC.md.

The revised renderer writes candidate silent renders and muxed MP4s to `_qc/redesigned-final/`, preserving active final outputs. It reuses candidate files if present: archive those candidates before an intentional source revision. Previous exports are backed up under `_qc/pre-redesign/`. After successful candidate QC, promote only validated MP4s to the landscape/portrait paths listed in README. Do not treat existence alone as QC completion. Re-run full decode, ffprobe, audio, scene/caption and visual checks. `_qc/` and media remain local.

## Validation commands

```bash
/path/to/brutalist.art/.venv/bin/python src/qc.py . _qc/redesigned-final
/path/to/brutalist.art/.venv/bin/python /path/to/brutalist.art/runtime/qc/beat_lint.py .
/path/to/brutalist.art/.venv/bin/python /path/to/brutalist.art/runtime/qc/content_check.py .
/path/to/brutalist.art/.venv/bin/python /path/to/brutalist.art/runtime/qc/final_frame_check.py . --mp4 mp4/FINAL_NAME.mp4
/path/to/brutalist.art/.venv/bin/python /path/to/brutalist.art/runtime/qc/final_frame_check.py . --sheet vertical/beat_sheet.json --mp4 vertical/mp4/FINAL_NAME.mp4
```

Replace FINAL_NAME with the exact export name in README.md. Final-frame Gate V samples each beat; source compilation and custom measured-audio/caption checks supplement the toolkit checks. Manim-only AST gates do not apply to these React/SVG sources. Template frame checks alone cannot validate custom SVG geometry. Human full-video review is still required.
