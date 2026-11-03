```
python runtime\scripts\generate_audio_kokoro.py weekly_updates\08-28
python runtime\scripts\remotion_scenes.py weekly_updates\08-28
python runtime\scripts\compile.py weekly_updates\08-28 --height 2160
python runtime\scripts\shorts.py weekly_updates\08-28
python runtime\scripts\remotion_scenes.py weekly_updates\08-28\short
python runtime\scripts\remotion_scenes.py weekly_updates\08-28 --only B04 --force
python runtime\scripts\remotion_scenes.py weekly_updates\08-28\short --only B04 --force
python runtime\scripts\compile.py weekly_updates\08-28 --height 2160 --force
python runtime\scripts\compile.py weekly_updates\08-28\short --height 1920 --force
```
