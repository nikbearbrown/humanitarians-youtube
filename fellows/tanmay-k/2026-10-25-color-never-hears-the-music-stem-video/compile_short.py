#!/usr/bin/env python3
"""Compile the Short once: silent 4K portrait video + the mixed track (narration, voice am_onyx, with the tunes under it)
-> master; loudness to -14 LUFS, true peak limit -2.0 (lands about -1.8 after AAC) (loudnorm, two-pass, linear); a 540x960 review preview; captions.
The audio is padded/trimmed to the exact video length. Adapted from Week 27's compile_short.py.
Run: /opt/homebrew/bin/python3.12 short/compile_short.py"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
NAME = "color-never-hears-the-music-short"


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stderr[-1500:])
    return r


VD = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                str(HERE / "_video" / "short-silent.mp4")]).stdout)
raw = HERE / "_video" / "short-mux.mp4"
run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(HERE / "_video" / "short-silent.mp4"), "-i", str(HERE / "mp3" / "short.mix.wav"),
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", f"apad=whole_dur={VD:.4f}", "-c:a", "aac", "-b:a", "256k",
     "-ar", "48000", "-t", f"{VD:.4f}", str(raw)])
TI, TP = -14.0, -2.0   # the AAC re-encode adds about 0.1 dB to the peak; -2.0 lands at about -1.8 dBTP (Week 27 sibling: -1.9)


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

# 540x960 review preview, about 2 Mbps
prev = HERE / "_video" / "short-preview.mp4"
run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(final), "-vf", "scale=540:960:flags=lanczos", "-c:v", "libx264",
     "-b:v", "1800k", "-maxrate", "2200k", "-bufsize", "4400k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", str(prev)])

# captions: one cue per sentence on the Whisper clock (the Short is read muted too: the headline carries the argument)
tm = json.loads((HERE / "mp3" / "timings_short.json").read_text())


def ts(x, vtt=False):
    h, m, s = int(x // 3600), int(x % 3600 // 60), x % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", "." if vtt else ",")


cues = []
sents = tm["sentences"]
for k, s in enumerate(sents):
    st = s["start"]
    en = (sents[k + 1]["start"] - 0.05) if k + 1 < len(sents) else min(tm["narration_end_s"], VD)
    cues.append((st, max(min(en, s["end"] + 0.4), st + 0.6), s["text"]))
(HERE / f"{NAME}.srt").write_text("".join(f"{i}\n{ts(s)} --> {ts(e)}\n{x}\n\n" for i, (s, e, x) in enumerate(cues, 1)))
(HERE / f"{NAME}.vtt").write_text("WEBVTT\n\n" + "".join(f"{ts(s, True)} --> {ts(e, True)}\n{x}\n\n" for s, e, x in cues))
d = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(final)]).stdout)
print(f"{final.name}: {d:.3f} s, video {VD:.3f} s, {len(cues)} caption cues; preview {prev.stat().st_size / 1e6:.1f} MB")
