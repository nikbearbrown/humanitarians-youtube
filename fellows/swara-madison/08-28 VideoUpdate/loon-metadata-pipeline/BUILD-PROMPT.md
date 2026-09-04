# BUILD-PROMPT - loon-metadata-pipeline

Build both aspect-ratio cuts from this folder's `beat_sheet.json`. The narration is the timing authority.

## Landscape 16:9

```bash
python3 runtime/scripts/generate_audio_kokoro.py videos/loon-metadata-pipeline
python3 runtime/scripts/remotion_scenes.py videos/loon-metadata-pipeline --force
python3 runtime/scripts/compile.py videos/loon-metadata-pipeline --height 1080 --fps 24 --force
```

Output: `videos/loon-metadata-pipeline/loon-metadata-pipeline.mp4`

## Portrait 9:16

Use the portrait sheet in `videos/loon-metadata-pipeline-vertical/`, then run the same audio, Remotion, and compile sequence with `--height 1920`.

Output: `videos/loon-metadata-pipeline-vertical/loon-metadata-pipeline-vertical.mp4`

Review frames from both outputs before delivery. Never publish automatically.