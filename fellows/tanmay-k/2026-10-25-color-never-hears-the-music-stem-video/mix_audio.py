#!/usr/bin/env python3
"""Mix the two tunes under / after the narration, for both formats. Audio is the clock; nothing here changes timing.

LONG  (mp3/beat-Bxx.wav -> mp3/beat-Bxx.mix.wav): the tunes are heard in the HOLD that follows the narration, so the
      viewer hears them at full level with no voice over them:
        B01  quick tune 8 s, then slow tune 8 s, then 3 s of silence for the pick   (hold 19 s)
        B12  quick tune 4 s, then slow tune 4 s                                      (hold 8 s)
      every other beat is narration only.
SHORT (short/mp3/narration.wav -> short/mp3/short.mix.wav): the tunes run UNDER the voice as a bed (about 17 dB below
      the voice) so the sky has something to follow:
        S01 quick, then slow (half and half)   S02 quick   S03 quick until the 'Slow, minor' sentence, then slow
        S04 slow   S05 quick for Bach's sentence, slow for Brahms's   S06 quick   S07 slow   S08 quick (opening state)
Stage-1 loudness on the result (-16 LUFS, -2 dBTP); the master pass later takes it to -14.

Run: /opt/homebrew/bin/python3.12 mix_audio.py [--long] [--short]
"""
import json
import subprocess
import sys
import wave
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
SR = 48000


def load(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(out, dtype="<f4").astype(np.float64)


def save(path, x):
    x = np.clip(x, -1, 1)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype("<i2").tobytes())


def loud(src, dst):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-af", "loudnorm=I=-16:TP=-2:LRA=11",
                    "-ar", str(SR), "-ac", "1", str(dst)], check=True)


def rms(x):
    return float(np.sqrt(np.mean(x ** 2)) + 1e-12)


def seg(tune, seconds, fade=0.08):
    n = int(seconds * SR)
    x = tune[:n].copy()
    f = int(fade * SR)
    x[:f] *= np.linspace(0, 1, f)
    x[-f:] *= np.linspace(1, 0, f)
    return x


def put(buf, x, start_s):
    i = int(start_s * SR)
    j = min(len(buf), i + len(x))
    if 0 <= i < len(buf):
        buf[i:j] += x[: j - i]


def tunes(level_rms):
    q = load(HERE / "tunes" / "tune_quick_major.wav")
    s = load(HERE / "tunes" / "tune_slow_minor.wav")
    return q * (level_rms / rms(q)), s * (level_rms / rms(s))


def long_mix():
    tim = json.loads((HERE / "mp3" / "timings.json").read_text())
    for bid, t in tim.items():
        v = load(HERE / "mp3" / f"beat-{bid}.wav")
        buf = v.copy()
        tail_start = t["narration_end_s"] + 0.45        # the hold begins where the normal tail ends
        q, s = tunes(rms(v[v != 0]) * 0.9)              # clips sit at about the voice's level, alone
        if bid == "B01":
            put(buf, seg(q, 8.0), tail_start)
            put(buf, seg(s, 8.0), tail_start + 8.0)
        elif bid == "B12":
            put(buf, seg(q, 4.0), tail_start)
            put(buf, seg(s, 4.0), tail_start + 4.0)
        out = HERE / "mp3" / f"beat-{bid}.mix.raw.wav"
        save(out, buf)
        loud(out, HERE / "mp3" / f"beat-{bid}.mix.wav")
        out.unlink()
        print(bid, round(len(buf) / SR, 2), "s", "(tunes)" if bid in ("B01", "B12") else "")


def short_mix():
    d = HERE / "short" / "mp3"
    tim = json.loads((d / "timings_short.json").read_text())
    v = load(d / "narration.wav")
    buf = v.copy()
    q, s = tunes(rms(v[np.abs(v) > 1e-4]) * 10 ** (-17 / 20))
    sents = tim["sentences"]
    by = {}
    for x in sents:
        by.setdefault(x["line"], []).append(x)

    def span(line):
        return by[line][0]["start"], by[line][-1]["end"]

    plan = []   # (tune, start, end)
    a, b = span("S01"); m = (a + b) / 2
    plan += [("q", a - 0.1, m), ("s", m, b + 0.2)]
    a, b = span("S02"); plan += [("q", a - 0.2, b + 0.2)]
    a, b = span("S03")
    sl = [x for x in by["S03"] if x["text"].lower().startswith("slow")]
    cut = sl[0]["start"] if sl else (a + b) / 2
    plan += [("q", a - 0.2, cut), ("s", cut, b + 0.2)]
    a, b = span("S04"); plan += [("s", a - 0.2, b + 0.2)]
    a, b = span("S05")
    br = [x for x in by["S05"] if x["text"].lower().startswith("brahms")]
    cut = br[0]["start"] if br else (a + b) / 2
    plan += [("q", a - 0.2, cut), ("s", cut, b + 0.2)]
    a, b = span("S06"); plan += [("q", a - 0.2, b + 0.2)]
    a, b = span("S07"); plan += [("s", a - 0.2, b + 0.2)]
    a, b = span("S08"); plan += [("q", a - 0.2, len(v) / SR)]
    pos = {"q": 0.0, "s": 0.0}
    bed = np.zeros_like(buf)
    for k, st, en in plan:
        st = max(0.0, st)
        dur = en - st
        src = q if k == "q" else s
        o = int(pos[k] * SR)
        x = np.tile(src, 3)[o: o + int(dur * SR)]
        pos[k] += dur
        n = len(x)
        f = min(int(0.3 * SR), n // 2)
        x = x.copy()
        x[:f] *= np.linspace(0, 1, f)
        x[-f:] *= np.linspace(1, 0, f)
        put(bed, x, st)
    bed[-int(0.8 * SR):] *= np.linspace(1, 0, int(0.8 * SR))     # tune ends with the track
    buf = buf + bed
    out = d / "short.mix.raw.wav"
    save(out, buf)
    loud(out, d / "short.mix.wav")
    out.unlink()
    print("short", round(len(buf) / SR, 2), "s;", len(plan), "tune segments")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or "--long" in args:
        long_mix()
    if not args or "--short" in args:
        short_mix()
