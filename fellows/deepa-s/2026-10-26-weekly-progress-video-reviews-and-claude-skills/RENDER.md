# Reproduction

Dependencies: Python with Pillow, numpy and kokoro-onnx; FFmpeg/ffprobe. Uses the existing Brutalist toolkit’s Kokoro model and OFL fonts.

The Beat Sheet is the narration and layout source of truth. Generate and measure narration before rendering. Review the recording; no human review is inferred from automated checks.

Render with the toolkit Python environment: python src/render.py /absolute/path/to/project. Use --preview for stills only. The renderer caches completed scene clips, assembles them at 24 fps, and normalizes narration to -18 LUFS with -2 dBTP target. Output is the filename defined in metadata.output_filename under mp4/.

This project uses a native Pillow/FFmpeg renderer, not the Remotion art-final wrapper. Verification must cover final dimensions, duration, decode integrity, audio timing/levels, layout, caption bounds, transitions and closing frame; do not claim unexecuted toolkit gates.

Audio generation: set ART_HOME to the installed Brutalist toolkit, then run python src/generate_audio.py /absolute/path/to/project using its virtual environment. Existing per-scene recordings are reused. Render directories are created as needed.

For the progress film, the measured first pass was 254.625 seconds. A one-time, pitch-preserving 1.08× tempo adjustment brought it to 235.833333 seconds without changing wording. For a fresh regenerated recording only, run python src/pace_audio.py /absolute/path/to/project once before rendering. Do not repeat it on the supplied, already-adjusted recording. Earlier audio is archived locally under _qc/.

## Current final formats — preserved build instructions

The instructions above describe the original landscape pipeline. The final STEM formats and progress portrait use [shared Remotion sources and pinned dependencies](../2026-10-26-how-claude-skills-work/src/cinematic/README.md). The original progress landscape remains unchanged. See [final evidence](SUBMISSION.md) for the authoritative delivery filenames.

For a future authorized rebuild: install the pinned package dependencies in the cinematic source folder; its public/fonts directory includes Montserrat and its OFL license. The historical Pillow renderer also requires the Brutalist toolkit fonts via ART_HOME. Obtain the preserved original audio and original landscape masters locally: generated recordings/masters are intentionally not available in Git. Do not regenerate or re-pace existing narration. Run render.cjs with --render only when a new render is explicitly wanted; finalize.py uses the original mastered audio and produces the three new-format files, while the completed progress landscape is copied unchanged. validate_final.py requires Python/NumPy and FFmpeg/ffprobe.

No build, audio generation, or video processing was executed for this source-only submission. Raw QC images, caches, dependencies and media remain local.
