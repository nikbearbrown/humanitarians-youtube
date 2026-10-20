#!/usr/bin/env python3
"""Compile the Short once: silent 4K portrait video + narration -> master; loudness to -14 LUFS / -1.5 dBTP; captions.
Run: /opt/homebrew/bin/python3.12 short/compile_short.py"""
import json, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).parent; ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
NAME = "the-birthday-paradox-three-things-short"
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: raise SystemExit(r.stderr[-1500:])
    return r
raw = HERE / "_video" / "short-mux.mp4"
VD = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(HERE / "_video" / "short-silent.mp4")]).stdout)
# audio padded to the exact video length (the old -shortest trimmed 4 frames off the end)
run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(HERE / "_video" / "short-silent.mp4"), "-i", str(HERE / "mp3" / "narration.wav"),
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", f"apad=whole_dur={VD:.4f}", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-t", f"{VD:.4f}", str(raw)])
TI, TP = -14.0, -1.5
def measure(p):
    r = run(["ffmpeg", "-i", str(p), "-af", f"loudnorm=I={TI}:TP={TP}:LRA=11:print_format=json", "-f", "null", "-"])
    return json.loads(re.search(r"\{[^{}]*input_i[^{}]*\}", r.stderr, re.S).group(0))
b = measure(raw); final = HERE / f"{NAME}.mp4"
run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-c:v", "copy", "-af",
     f"loudnorm=I={TI}:TP={TP}:LRA=11:measured_I={b['input_i']}:measured_TP={b['input_tp']}:measured_LRA={b['input_lra']}:measured_thresh={b['input_thresh']}:offset={b['target_offset']}:linear=true",
     "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-t", f"{VD:.4f}", str(final)])
a = measure(final)
print(f"loudness {float(b['input_i']):+.1f} -> {float(a['input_i']):+.1f} LUFS, true peak {float(a['input_tp']):+.1f} dBTP, LRA {float(a['input_lra']):.1f}")
# captions: one cue per phrase (split at commas), timed on the Whisper clock
import importlib.util
spec = importlib.util.spec_from_file_location("bm", ROOT / "build_motion.py"); bm = importlib.util.module_from_spec(spec); spec.loader.exec_module(bm); ma = bm.ma
tm = json.loads((HERE / "mp3" / "timings_short.json").read_text()); ref, t = bm.times_for(tm)
ends = {i: w[2] for i, w in enumerate(tm["words"])}
phrases, tokens_i = [], 0
for ln in tm["lines"]:
    for sent in re.split(r"(?<=[.?!])\s+", ln["text"]):
        for ph in re.split(r"(?<=,)\s+", sent):
            n = len([x for x in (ma.norm(w) for w in ph.split()) if x]); phrases.append((ph.strip(), tokens_i, tokens_i + n)); tokens_i += n
def ts(x, vtt=False):
    h, m, s = int(x // 3600), int(x % 3600 // 60), x % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", "." if vtt else ",")
cues = []
for k, (txt, i0, i1) in enumerate(phrases):
    st = t[i0]; en = (t[phrases[k + 1][1]] - 0.05) if k + 1 < len(phrases) else min(tm["narration_end_s"], tm["duration_s"])
    cues.append((st, max(en, st + 0.6), txt))
(HERE / f"{NAME}.srt").write_text("".join(f"{i}\n{ts(s)} --> {ts(e)}\n{x}\n\n" for i, (s, e, x) in enumerate(cues, 1)))
(HERE / f"{NAME}.vtt").write_text("WEBVTT\n\n" + "".join(f"{ts(s, True)} --> {ts(e, True)}\n{x}\n\n" for s, e, x in cues))
d = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(final)]).stdout)
print(f"{final.name}: {d:.2f} s, {len(cues)} caption cues")
