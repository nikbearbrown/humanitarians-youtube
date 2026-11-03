# BUILD-PROMPT — Meet Muse

From the Brutalist toolkit root. Set `REEL` to the `claude-liam-meet-muse` folder and `BRUTALIST_HOME` to the toolkit root.

```bash
# 1. Beat sheet, narration, exact timing
python3 "$REEL/make_sheet.py" author
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 "$REEL/make_sheet.py" finish

# 2. Landscape: drawn scenes + Remotion bookends (B00, B01, B15) + master
(cd "$REEL" && python3 scenes.py landscape "$REEL")
python3 runtime/scripts/remotion_scenes.py "$REEL"
./art final "$REEL"

# 3. Vertical: portrait sheet, then fix it up
./art vertical "$REEL"
#    In $REEL/vertical/beat_sheet.json:
#    - set metadata width/height to 2160/3840;
#    - point each audio_file at audio/beat-<id>.wav (copy $REEL/audio/*.wav into vertical/audio/);
#    - set B01 props fontSize 150, lineSpacing 1.5.
(cd "$REEL" && python3 scenes.py portrait "$REEL/vertical")
python3 runtime/scripts/remotion_scenes.py "$REEL/vertical"
./art final "$REEL/vertical" --height 3840   # native 4K portrait; the default 2160 downscale fails Gate V
```

Masters are written to `renders/`, then renamed `muse_yeshwanth_16x9.mp4` and `muse_yeshwanth_9x16.mp4` for Drive.
