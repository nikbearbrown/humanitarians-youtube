#!/usr/bin/env python3
"""Compile both films: concat the beat videos (stream copy), build the narration beat by beat (each padded/trimmed to its video's exact duration so
nothing drifts), two-pass loudnorm to -14 LUFS (true peak limit -2.0 so the AAC lands under -1.5), mux. Then re-measure the delivered file.
Outputs: two-customers-one-run-mycroft.mp4 and short/two-customers-one-run-mycroft-short.mp4.   Run: python3 compile_master.py [long|short]"""
import json, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).parent
ORDER = {"long": ["B00", "B00b", "B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B09", "B10", "B11", "B12", "B13"],
         "short": ["S-1", "S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"]}
def run(*a): return subprocess.run(a, check=True, capture_output=True, text=True)
def dur(p): return float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)).stdout)
def measure(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    tail = r[r.rindex("Summary:"):]; return float(re.search(r"I:\s+(-?[\d.]+) LUFS", tail).group(1)), float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", tail).group(1))
def compile_one(fmt):
    base = HERE / ("short" if fmt == "short" else ""); W = base / "_compile"; W.mkdir(exist_ok=True)
    out = base / ("two-customers-one-run-mycroft-short.mp4" if fmt == "short" else "two-customers-one-run-mycroft.mp4"); ids = ORDER[fmt]
    (W / "v.txt").write_text("".join(f"file '{(base / '_beats' / f'{b}.mp4').as_posix()}'\n" for b in ids))
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(W / "v.txt"), "-c", "copy", str(W / "video.mp4"))
    parts = []
    for b in ids:
        d = dur(base / "_beats" / f"{b}.mp4"); p = W / f"{b}.wav"
        run("ffmpeg", "-y", "-loglevel", "error", "-i", str(base / "mp3" / f"beat-{b}.wav"), "-af", f"apad=whole_dur={d:.6f}", "-t", f"{d:.6f}", "-ar", "48000", "-ac", "1", str(p)); parts.append(p)
    (W / "a.txt").write_text("".join(f"file '{p.as_posix()}'\n" for p in parts))
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(W / "a.txt"), "-c", "copy", str(W / "narration.wav"))
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(W / "narration.wav"), "-af", "loudnorm=I=-14:TP=-2.0:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True)
    m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S).group(0))
    af = (f"loudnorm=I=-14:TP=-2.0:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(W / "narration.wav"), "-af", af, "-ar", "48000", "-ac", "1", str(W / "master.wav"))
    run("ffmpeg", "-y", "-loglevel", "error", "-i", str(W / "video.mp4"), "-i", str(W / "master.wav"), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", "-shortest", str(out))
    i, tp = measure(out)
    print(f"{fmt}: video {dur(W/'video.mp4'):.2f} s, audio {dur(W/'master.wav'):.2f} s, file {dur(out):.2f} s; narration was {m['input_i']} LUFS; delivered {i} LUFS, true peak {tp} dBFS")
for f in [a for a in sys.argv[1:] if a in ORDER] or ["long", "short"]: compile_one(f)
