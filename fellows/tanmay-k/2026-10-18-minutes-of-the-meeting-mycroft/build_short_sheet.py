#!/usr/bin/env python3
"""beat_sheet-short.json and SHOTLIST-SHORT.md from short/SHORT-SCRIPT.md, the audio clock (mp3/timings_short.json) and the event cues (_video/cues.json).
The Short is one scene; its "beats" are the script's lines S01 to S07. Run: python3 short/build_short_sheet.py"""
import json, re
from pathlib import Path
HERE = Path(__file__).parent
src = (HERE / "SHORT-SCRIPT.md").read_text(); tm = json.loads((HERE / "mp3" / "timings_short.json").read_text()); cues = json.loads((HERE / "_video" / "cues.json").read_text())
HEAD = re.compile(r"^### (S\d+) · ([^·]+?) · ~(\d+) s \(tone: ([^)]*)\)", re.M); ms = list(HEAD.finditer(src)); lines = []
for i, m in enumerate(ms):
    blk = src[m.end(): ms[i + 1].start() if i + 1 < len(ms) else len(src)]
    g = lambda tag: next((l[len(tag):].strip().rstrip("*") for l in blk.splitlines() if l.startswith(tag)), "")
    sents = [s for s in tm["sentences"] if s["line"] == m.group(1)]
    lines.append({"line_id": m.group(1), "title": m.group(2).strip(), "tone": m.group(4),
                  "narration_text": " ".join(l[2:].strip() for l in blk.splitlines() if l.startswith("> ")),
                  "on_screen": g("*On screen:*"), "source_line": g("*Source:*"),
                  "audio_start_s": sents[0]["start"], "audio_end_s": sents[-1]["end"]})
sheet = {"metadata": {"title": "Who Fills the Blank? (the Short)", "role": "trailer for Minutes of the Meeting: What an AI Is Handed",
                      "voice_kokoro": "am_onyx", "master": "2160x3840 @ 30 fps", "duration_s": tm["duration_s"], "shape": "one continuous scene, no cuts",
                      "note": "audio is the clock; cues are on the Whisper word clock; not hand-edited"},
         "lines": lines, "event_cues_s": cues}
(HERE / "beat_sheet-short.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
rows = ["# SHOTLIST-SHORT: Who Fills the Blank?", "", "One scene, rendered frame by frame from a function of time (`build_short.py`); no generated imagery, no stock, no third-party images. "
        "Layout rules (safe area 12% to 75% of the height, type ≥ 30 px at 1080 wide, no cuts, something moving at least every 3 s) are in `SHORT-SCRIPT.md`.", "",
        "| Line | Audio | On screen | Source line |", "|---|---|---|---|"]
for l in lines: rows.append(f"| {l['line_id']} {l['title'].title()} | {l['audio_start_s']:.1f} to {l['audio_end_s']:.1f} s | {l['on_screen']} | {l['source_line'] or 'none needed'} |")
rows += ["", "## Event cues (seconds, on the Whisper word clock)", "", "| Event | At |", "|---|---|"] + [f"| {k} | {v:.2f} |" for k, v in cues.items()]
(HERE / "SHOTLIST-SHORT.md").write_text("\n".join(rows) + "\n")
print(len(lines), "lines;", len(cues), "cues")
