#!/usr/bin/env python3
"""Compile once: beat videos (copy) + frame-padded beat audio -> master, captions, loudness to -14 LUFS / -2 dBTP.
Run: /opt/homebrew/bin/python3.12 compile_master.py"""
import json, math, re, subprocess
from pathlib import Path
HERE = Path(__file__).parent
FPS = 30
NAME = "the-birthday-paradox-three-things"
timings = json.loads((HERE / "mp3" / "timings.json").read_text())
ids = sorted(timings)
def run(cmd): 
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: raise SystemExit(r.stderr[-1500:])
    return r
# 1. audio padded to the exact frame-quantised beat duration, concatenated
parts, starts, t = [], {}, 0.0
for b in ids:
    dur = math.ceil(timings[b]["duration_s"] * FPS) / FPS
    out = HERE / "mp3" / f"beat-{b}.pad.wav"
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(HERE / "mp3" / f"beat-{b}.wav"), "-af", f"apad=whole_dur={dur:.4f}", "-t", f"{dur:.4f}", str(out)])
    parts.append(out); starts[b] = t; t += dur
(HERE / "_beats" / "audio.txt").write_text("".join(f"file '{p}'\n" for p in parts))
(HERE / "_beats" / "video.txt").write_text("".join(f"file '{HERE / '_beats' / (b + '.mp4')}'\n" for b in ids))
run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(HERE / "_beats" / "audio.txt"), "-c", "copy", str(HERE / "_beats" / "master_audio.wav")])
run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(HERE / "_beats" / "video.txt"), "-c", "copy", str(HERE / "_beats" / "master_video.mp4")])
# 2. mux, then loudness measured and normalised (video copied)
raw = HERE / "_beats" / "master_mux.mp4"
run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(HERE / "_beats" / "master_video.mp4"), "-i", str(HERE / "_beats" / "master_audio.wav"),
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", str(raw)])
def measure(p):
    r = run(["ffmpeg", "-i", str(p), "-af", "loudnorm=I=-14:TP=-2:LRA=11:print_format=json", "-f", "null", "-"])
    return json.loads(re.search(r"\{[^{}]*input_i[^{}]*\}", r.stderr, re.S).group(0))
before = measure(raw)
final = HERE / f"{NAME}.mp4"
run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-c:v", "copy", "-af",
     f"loudnorm=I=-14:TP=-2:LRA=11:measured_I={before['input_i']}:measured_TP={before['input_tp']}:measured_LRA={before['input_lra']}:measured_thresh={before['input_thresh']}:offset={before['target_offset']}:linear=true",
     "-c:a", "aac", "-b:a", "256k", "-ar", "48000", str(final)])
after = measure(final)
print(f"loudness: {float(before['input_i']):+.1f} -> {float(after['input_i']):+.1f} LUFS, true peak {float(after['input_tp']):+.1f} dBTP, LRA {float(after['input_lra']):.1f}")
# 3. captions from sentence timings
def ts(x, vtt=False):
    h, m, s = int(x // 3600), int(x % 3600 // 60), x % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", "." if vtt else ",")
cues = []
for b in ids:
    for s in timings[b]["sentences"]:
        cues.append((starts[b] + s["start"], starts[b] + s["end"] + 0.1, s["text"]))
(HERE / f"{NAME}.srt").write_text("".join(f"{i}\n{ts(a)} --> {ts(e)}\n{tx}\n\n" for i, (a, e, tx) in enumerate(cues, 1)))
(HERE / f"{NAME}.vtt").write_text("WEBVTT\n\n" + "".join(f"{ts(a, True)} --> {ts(e, True)}\n{tx}\n\n" for a, e, tx in cues))
json.dump(starts, open(HERE / "_beats" / "beat_starts.json", "w"), indent=1)
d = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(final)]).stdout)
print(f"master {final.name}: {d:.2f} s ({d/60:.2f} min), {len(cues)} caption cues")
