#!/usr/bin/env bash
# Audio lock for both week-12 reels: Kokoro -> word clock -> (listening clip) -> cues -> durationSeconds.
W=/d/Rohan/Claude/books/humanitarians-ai/youtube/week-12
R_LIST="$@"
cd /d/Rohan/Claude/HAI/RohanClaudeHAIbrutalist.art || exit 1
export PYTHONIOENCODING=utf-8 PYTHONUNBUFFERED=1
for R in $R_LIST; do
  python runtime/scripts/generate_audio_kokoro.py $R > $R/_audio.log 2>&1 || { echo "kokoro failed $R"; exit 1; }
  python runtime/scripts/align.py $R >> $R/_audio.log 2>&1 || { echo "align failed $R"; exit 1; }
  [ -f $R/mix_listen.py ] && (cd $R && python mix_listen.py >> _audio.log 2>&1)
  python runtime/scripts/sync_cues.py $R >> $R/_audio.log 2>&1 || { echo "sync failed $R"; exit 1; }
  python - $R <<'PY'
import json, sys
from pathlib import Path
p = Path(sys.argv[1]) / "beat_sheet.json"; s = json.loads(p.read_text(encoding="utf-8"))
for b in s["beats"]:
    b["shot"]["remotion"]["props"]["durationSeconds"] = b["actual_duration_s"]
p.write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding="utf-8")
print(p.parent.name, round(sum(b["actual_duration_s"] for b in s["beats"]), 2), "s",
      [(b["beat_id"], b["actual_duration_s"]) for b in s["beats"]])
PY
done
