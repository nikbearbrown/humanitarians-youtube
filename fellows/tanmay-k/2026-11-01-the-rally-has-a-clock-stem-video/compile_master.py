#!/usr/bin/env python3
"""One compile: concat the 14 beat videos (stream copy, no re-render), build the narration track beat by beat (each padded/trimmed to
its video's exact frame count so no drift), two-pass loudnorm to -14 LUFS / -1.5 dBTP, mux. Output: the-rally-has-a-clock.mp4"""
import json, subprocess, re
from pathlib import Path
HERE = Path(__file__).parent; OUT = HERE / "the-rally-has-a-clock.mp4"; W = HERE / "_compile"; W.mkdir(exist_ok=True)
beats = [f"B{n:02d}" for n in range(14)]
def run(*a, **k): return subprocess.run(a, check=True, capture_output=True, text=True, **k)
def dur(p): return float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)).stdout)
# video
(W / "v.txt").write_text("".join(f"file '{(HERE/'_beats'/f'{b}.mp4').as_posix()}'\n" for b in beats))
run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(W / "v.txt"), "-c", "copy", str(W / "video.mp4"))
# audio: pad/trim every beat to its video duration
parts = []
for b in beats:
    d = dur(HERE / "_beats" / f"{b}.mp4"); p = W / f"{b}.wav"
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(HERE / "mp3" / f"beat-{b}.wav"), "-af", f"apad=whole_dur={d:.6f}", "-t", f"{d:.6f}", "-ar", "48000", "-ac", "1", str(p)); parts.append(p)
(W / "a.txt").write_text("".join(f"file '{p.as_posix()}'\n" for p in parts))
run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(W / "a.txt"), "-c", "copy", str(W / "narration.wav"))
# two-pass loudnorm
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(W / "narration.wav"), "-af", "loudnorm=I=-14:TP=-2.0:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True)
m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S).group(0))
af = (f"loudnorm=I=-14:TP=-2.0:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}"
      f":offset={m['target_offset']}:linear=true")
run("ffmpeg", "-y", "-loglevel", "error", "-i", str(W / "narration.wav"), "-af", af, "-ar", "48000", "-ac", "1", str(W / "master.wav"))
run("ffmpeg", "-y", "-loglevel", "error", "-i", str(W / "video.mp4"), "-i", str(W / "master.wav"), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", "-shortest", str(OUT))
print("video", round(dur(W / "video.mp4"), 3), "audio", round(dur(W / "master.wav"), 3), "out", round(dur(OUT), 3), "input loudness", m["input_i"], "LUFS")
