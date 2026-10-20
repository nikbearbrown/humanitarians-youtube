# SOURCES — Basketball Blaster: The Design Document Came Last

- **The design document:** `basketball-game-godot/GDD.md` v0.1, agent-drafted and unapproved. A byte copy is in `evidence/GDD.md`; its hash is in `gdd-evidence.json`.
- **The game:** `basketball-game-godot-completed/`, snapshot `build_id 8f86cc812e23…` (`../basketball-captures/CAPTURE.md`). It was not modified.
- **The Unity original:** `basketball-game-godot/unity-scripts/scripts/` (29 C# files), read for SOURCE claims.
- **Gameplay:** scripted-input takes `campaign` and `defeat`, copied with hashes into `capture/`. Every clip is an exact-frame cut (`media/`, provenance in `beat_sheet.json`).
- **Stills:** engine frames of the same takes (`evidence/`).
- **Tools:** Kokoro-82M v1.0 `am_onyx` (local), Remotion 4 via `remotion_scenes.py`, ffmpeg, Pillow, Godot 4.7.2. No paid calls.
