# Reproduction and review

The production toolkit was inspected at `~/Downloads/brutalist.art-main` and copied to `/tmp/deepa-weeks5-6-toolkit` for this build. Existing toolkit projects were not edited. The isolated copy uses the installed Remotion dependencies, Kokoro model and fonts.

## Scene installation

Copy `src/DeepaContinuation.tsx` into the isolated toolkit's `runtime/remotion/src/scenes/`, `src/humanitarians.ts` into `src/tokens/`, and `src/Root.tsx` into `runtime/remotion/src/`. Retain the toolkit's HAI outlined wordmark and EB Garamond/Montserrat font assets. Register both compositions through the supplied Root. The frame count comes from each beat's measured narration.

## Build

Use the toolkit virtual environment on PATH and its local Chrome executable. Run the normal `runtime/scripts/remotion_scenes.py <project>` wrapper, then `art final <project> --height 2160 --out <project>/mp4`. Repeat for `<project>/vertical`, using `--height 3840`. The wrapper renders native compositions at scale 2; portrait is not cropped from landscape. The final command runs Gate T, beat lint, chart-shape checks, source validation, and final-frame validation before atomic promotion.

## Additional checks

Run `master_check.py` and `loudness_check.py` against each explicit master path. Fully decode each final file with ffmpeg, verify dimensions/fps and frame-clock duration with ffprobe, and compare decoded audio against each locked source beat at its actual timeline position. Inspect extracted frames from every beat and transition. Keep human cut review distinct from technical QC.

Generated audio, beat renders, masters, previews and detailed machine logs stay in ignored media/QC folders. No upload or publication command belongs to this build.

For the current correction, the user explicitly requested rendering before reviewing the videos. The new narration and cuts remain pending human approval; earlier approval is not inherited.
