#!/usr/bin/env python3
"""Compile the work-video Short once: the silent 4K portrait video + the narration (am_onyx) -> the master.
Loudness: the narration is normalised ONCE (loudnorm, two-pass, linear) to -14 LUFS with a true-peak limit of -2.0 (the AAC
re-encode adds about 0.1 dB, so the master lands near -1.9 dBTP; the limit is -1.5). The audio is padded or trimmed to the
exact video length. Also a 540x960 review preview. Adapted from the topic video's compile_short.py.
Run: /opt/homebrew/bin/python3.12 short/compile_short.py"""
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
NAME = "the-sum-behind-the-number-short"
TI, TP = -14.0, -2.0


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stderr[-1500:])
    return r


VD = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(HERE / "_video" / "short-silent.mp4")]).stdout)
raw = HERE / "_video" / "short-mux.mp4"
run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(HERE / "_video" / "short-silent.mp4"), "-i", str(HERE / "mp3" / "narration.wav"),
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", f"apad=whole_dur={VD:.4f}", "-c:a", "aac", "-b:a", "256k",
     "-ar", "48000", "-ac", "1", "-t", f"{VD:.4f}", str(raw)])


def measure(p):
    r = run(["ffmpeg", "-i", str(p), "-af", f"loudnorm=I={TI}:TP={TP}:LRA=11:print_format=json", "-f", "null", "-"])
    return json.loads(re.search(r"\{[^{}]*input_i[^{}]*\}", r.stderr, re.S).group(0))


b = measure(raw)
final = HERE / f"{NAME}.mp4"
run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-c:v", "copy", "-af",
     f"loudnorm=I={TI}:TP={TP}:LRA=11:measured_I={b['input_i']}:measured_TP={b['input_tp']}:measured_LRA={b['input_lra']}:"
     f"measured_thresh={b['input_thresh']}:offset={b['target_offset']}:linear=true",
     "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "1", "-t", f"{VD:.4f}", str(final)])
a = measure(final)
print(f"loudness {float(b['input_i']):+.1f} -> {float(a['input_i']):+.1f} LUFS, true peak {float(a['input_tp']):+.1f} dBTP, LRA {float(a['input_lra']):.1f}")
prev = HERE / "_video" / "short-preview.mp4"
run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(final), "-vf", "scale=540:960:flags=lanczos", "-c:v", "libx264",
     "-b:v", "1800k", "-maxrate", "2200k", "-bufsize", "4400k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", str(prev)])
d = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(final)]).stdout)
print(f"{final.name}: {d:.3f} s, video {VD:.3f} s; preview {prev.stat().st_size / 1e6:.1f} MB")
