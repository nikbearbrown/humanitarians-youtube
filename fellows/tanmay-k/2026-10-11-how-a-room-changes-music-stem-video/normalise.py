#!/usr/bin/env python3
"""Two-pass EBU R128 to -14 LUFS / -2.0 dBTP, video stream-copied.

BEATS.md defect 13 and the Week 21 delivery note: the compiler does not normalise and
nothing downstream checks, so a technically perfect master ships ~10 dB quiet. Measured
before and after here, never assumed.

Video is copied, not re-encoded: the picture stays byte-identical and no beat is re-rendered.
"""
import json, re, subprocess, sys
from pathlib import Path

TARGET_I, TARGET_TP, TARGET_LRA = -14.0, -2.0, 11.0   # TP -2.0: W24 at -1.5 landed 0.1 dB over


def measure(p):
    r = subprocess.run(["ffmpeg", "-i", str(p), "-af",
                        f"loudnorm=I={TARGET_I}:TP={TARGET_TP}:LRA={TARGET_LRA}:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"\{[^{}]*input_i[^{}]*\}", r.stderr, re.S)
    if not m:
        sys.exit(f"loudnorm measurement failed for {p}")
    return json.loads(m.group(0))


def main():
    for src in sys.argv[1:]:
        src = Path(src)
        d = measure(src)
        out = src.with_name(src.stem + "-norm.mp4")
        subprocess.run(["ffmpeg", "-y", "-i", str(src), "-c:v", "copy", "-af",
                        f"loudnorm=I={TARGET_I}:TP={TARGET_TP}:LRA={TARGET_LRA}:"
                        f"measured_I={d['input_i']}:measured_TP={d['input_tp']}:"
                        f"measured_LRA={d['input_lra']}:measured_thresh={d['input_thresh']}:"
                        f"offset={d['target_offset']}:linear=true",
                        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(out)],
                       capture_output=True, text=True)
        out.replace(src)
        after = measure(src)
        print(f"{src.name:<34} {float(d['input_i']):+7.1f} -> {float(after['input_i']):+7.1f} LUFS"
              f"   TP {float(after['input_tp']):+5.1f} dBFS")


if __name__ == "__main__":
    main()
