#!/usr/bin/env python3
"""beat_sheet.json (long) and beat_sheet-short.json (Short) from the signed narration (beats_text.py, short/short_text.py), the measured audio
(mp3/timings.json, short/mp3/timings_short.json) and the cue times (CUES.json). Run: python3 build_beat_sheet.py"""
import json, sys
from pathlib import Path
HERE = Path(__file__).parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "short"))
from beats_text import B
from short_text import S
tim = json.loads((HERE / "mp3" / "timings.json").read_text()); cues = json.loads((HERE / "CUES.json").read_text())
beats, t0 = [], 0.0
for bid, title, narr, visual, status in B:
    d = round(round(tim[bid]["duration_s"] * 30) / 30, 3)
    beats.append({"beat_id": bid, "title": title, "narration_text": narr, "word_count": len(narr.split()), "visual_intent": visual, "status": status,
                  "start_s": round(t0, 3), "duration_s": d, "cues": cues[bid].get("events", [])}); t0 += d
(HERE / "beat_sheet.json").write_text(json.dumps({"title": "The Rally Has a Clock: When Is “No Perfect Defense” True in Pong?", "voice": "Kokoro am_onyx",
    "format": "16:9, 3840x2160, 30 fps", "duration_s": round(t0, 3), "beats": beats}, indent=1, ensure_ascii=False))
st = json.loads((HERE / "short" / "mp3" / "timings_short.json").read_text()); lines = []
for sid, title, narr, visual, status in S:
    l = [x for x in st["lines"] if x["id"] == sid][0]
    lines.append({"line_id": sid, "title": title, "narration_text": narr, "word_count": len(narr.split()), "visual_intent": visual, "status": status, "start_s": l["start"], "end_s": l["end"]})
(HERE / "beat_sheet-short.json").write_text(json.dumps({"title": "In my tiny Pong, a perfect defender loses on the sixth shot", "voice": "Kokoro am_onyx",
    "format": "9:16, 2160x3840, 30 fps, one continuous scene", "duration_s": st["duration_s"], "lines": lines}, indent=1, ensure_ascii=False))
print(len(beats), "beats;", len(lines), "Short lines;", round(t0, 1), "s long")
