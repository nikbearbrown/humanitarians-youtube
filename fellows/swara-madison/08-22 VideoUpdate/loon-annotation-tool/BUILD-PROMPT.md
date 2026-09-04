# BUILD-PROMPT - loon-annotation-tool

Build both aspect-ratio cuts from the supplied `beat_sheet.json`.

## Landscape 16:9

```bash
cd runtime/remotion
npx tsc --noEmit
cd ../..
python3 runtime/scripts/generate_audio_kokoro.py videos/loon-annotation-tool
python3 runtime/scripts/remotion_scenes.py videos/loon-annotation-tool --force
python3 runtime/scripts/compile.py videos/loon-annotation-tool --height 1080 --fps 24 --force
```

Output: `videos/loon-annotation-tool/loon-annotation-tool.mp4`

## Portrait 9:16

Copy the landscape sheet and audio into `videos/loon-annotation-tool-vertical/`, set metadata aspect ratio to `9:16`, use the portrait scene IDs listed in the vertical sheet, then run:

```bash
python3 runtime/scripts/generate_audio_kokoro.py videos/loon-annotation-tool-vertical
python3 runtime/scripts/remotion_scenes.py videos/loon-annotation-tool-vertical --force
python3 runtime/scripts/compile.py videos/loon-annotation-tool-vertical --height 1920 --fps 24 --force
```

Output: `videos/loon-annotation-tool-vertical/loon-annotation-tool-vertical.mp4`

Review frames from both outputs before delivery. Never publish automatically.
