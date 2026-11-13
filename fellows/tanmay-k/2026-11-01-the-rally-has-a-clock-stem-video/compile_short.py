#!/usr/bin/env python3
"""One compile of the Short: the silent 2160x3840 scene + the narration, two-pass loudnorm to -14 LUFS / -1.5 dBTP, AAC 48 kHz, video stream-copied.
Output: the-rally-has-a-clock-short.mp4"""
import json, re, subprocess
from pathlib import Path
HERE = Path(__file__).parent; OUT = HERE / "the-rally-has-a-clock-short.mp4"; W = HERE / "_compile"; W.mkdir(exist_ok=True)
def run(*a): return subprocess.run(a, check=True, capture_output=True, text=True)
def dur(p): return float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)).stdout)
vid = HERE / "_video" / "short-silent.mp4"; d = dur(vid)
run("ffmpeg", "-y", "-loglevel", "error", "-i", str(HERE / "mp3" / "short.wav"), "-af", f"apad=whole_dur={d:.6f}", "-t", f"{d:.6f}", "-ar", "48000", "-ac", "1", str(W / "narration.wav"))
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(W / "narration.wav"), "-af", "loudnorm=I=-14:TP=-2.0:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True)
m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S).group(0))
af = f"loudnorm=I=-14:TP=-2.0:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true"
run("ffmpeg", "-y", "-loglevel", "error", "-i", str(W / "narration.wav"), "-af", af, "-ar", "48000", "-ac", "1", str(W / "master.wav"))
run("ffmpeg", "-y", "-loglevel", "error", "-i", str(vid), "-i", str(W / "master.wav"), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", "-shortest", str(OUT))
print("video", round(d, 3), "out", round(dur(OUT), 3), "input loudness", m["input_i"], "LUFS")
