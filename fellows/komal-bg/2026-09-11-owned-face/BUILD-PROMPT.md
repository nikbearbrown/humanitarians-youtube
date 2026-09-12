# BUILD-PROMPT.md

Paste-ready rebuild (never publishes).

```bash
export ART_HOME=/Users/komalganapathy/Desktop/brutalist.art
REEL="$ART_HOME/renders/owned-face"
cd "$ART_HOME"

./art scenes --check OwnedFaceRoles OwnedFaceInventory OwnedFaceLuxury OwnedFaceOutro \
  ClaudeComposerAsk BrutalistHesitantWriter ClaudeVerdictArtifact

.venv/bin/python runtime/scripts/generate_audio_kokoro.py "$REEL"

# B01 needs ≥9s with a written 0.8s head start for the typing
ffmpeg -y -i "$REEL/mp3/beat-B01.mp3" -af "adelay=800|800" "$REEL/mp3/beat-B01-pad.mp3"
mv "$REEL/mp3/beat-B01-pad.mp3" "$REEL/mp3/beat-B01.mp3"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$REEL/mp3/beat-B01.mp3")
python3 - <<PY
import json, pathlib
p = pathlib.Path("$REEL/beat_sheet.json")
s = json.loads(p.read_text())
for b in s["beats"]:
    if b["beat_id"]=="B01":
        b["actual_duration_s"] = round(float("$DUR"), 2)
p.write_text(json.dumps(s, indent=2)+"\n")
PY

.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL" --force
./art final "$REEL" --height 2160

./art vertical "$REEL"
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL/vertical" --force
./art final "$REEL/vertical" --height 3840
```

QC: sample frames at ≥2 fps into `_qc/frames/`, read them, log `_qc/REPORT.md`.
The mp4 probe is a file check, not visual QC.
