# BUILD-PROMPT - loon-metadata-pipeline-vertical-short

Build the Shorts derivative as a portrait 9:16 cut from this folder's `beat_sheet.json`. It is under YouTube's 3:00 Shorts cap, so keep all beats and use the dedicated 916 scenes. Narration is the timing authority.

```bash
python3 runtime/scripts/generate_audio_kokoro.py videos/loon-metadata-pipeline-vertical
python3 runtime/scripts/remotion_scenes.py videos/loon-metadata-pipeline-vertical --force
python3 runtime/scripts/compile.py videos/loon-metadata-pipeline-vertical --review --height 1920 --fps 24 --force
```

Output: `videos/loon-metadata-pipeline-vertical/loon-metadata-pipeline-vertical.mp4`

Review frames before delivery. Never publish automatically.