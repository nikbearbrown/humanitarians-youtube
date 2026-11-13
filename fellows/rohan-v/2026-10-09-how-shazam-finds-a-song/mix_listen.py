"""Appends the listening clips to B04's narration, so the viewer hears the evidence: the noisy phone-style
query (evidence/clip_cafe.wav), then the same five seconds of the original song (original_segment.wav).

Each clip is the unedited output of fingerprint.py, trimmed to its window, resampled to the narration's
rate and set to the narration's RMS level (same loudness, nothing else changed). The mixed file becomes the
beat's audio_file; actual_duration_s is re-measured from it, and the clip windows are written into the beat's
props as fractions of the beat (props.listen) so the scene can show which clip is playing.

Run after generate_audio_kokoro.py + align.py, and before sync_cues.py:  python mix_listen.py
"""
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
MP3 = HERE / "mp3"
PAUSE, GAP, TAIL = 0.6, 0.7, 0.8

PLAN = {  # beat -> (label, file, start in the file, seconds)
    "B04": [("NOISY CLIP", "clip_cafe.wav", 0.0, 5.0), ("ORIGINAL", "original_segment.wav", 0.0, 5.0)],
}


def run(args):
    return subprocess.run(args, capture_output=True, text=True, check=True)


def dur(path):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)])
    return float(r.stdout.strip())


def rms_db(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    return float(re.search(r"mean_volume:\s*([-\d.]+) dB", r.stderr).group(1))


def main():
    sheet_p = HERE / "beat_sheet.json"
    sheet = json.loads(sheet_p.read_text(encoding="utf-8"))
    for beat in sheet["beats"]:
        bid = beat["beat_id"]
        if bid not in PLAN:
            continue
        narr = MP3 / f"beat-{bid}.mp3"
        n_dur = dur(narr)
        n_db = rms_db(narr)
        parts, t, windows = [], n_dur + PAUSE, []
        inputs = ["-i", str(narr)]
        filters = [f"[0:a]aresample=24000,aformat=channel_layouts=mono,apad=pad_dur={PAUSE}[n]"]
        for i, (label, wav, start, length) in enumerate(PLAN[bid], start=1):
            c = EV / wav
            gain = n_db - rms_db(c)
            inputs += ["-i", str(c)]
            pad = TAIL if i == len(PLAN[bid]) else GAP
            filters.append(f"[{i}:a]atrim=start={start}:duration={length},asetpts=PTS-STARTPTS,aresample=24000,"
                           f"aformat=channel_layouts=mono,volume={gain:.2f}dB,afade=t=in:d=0.02,"
                           f"afade=t=out:st={length - 0.03}:d=0.03,apad=pad_dur={pad}[c{i}]")
            cd = min(length, dur(c) - start)
            windows.append({"label": label, "file": wav, "clip_from_s": start, "start_s": round(t, 3),
                            "end_s": round(t + cd, 3), "gain_db": round(gain, 2)})
            t += cd + pad
        chain = "[n]" + "".join(f"[c{i}]" for i in range(1, len(PLAN[bid]) + 1))
        filters.append(f"{chain}concat=n={len(PLAN[bid]) + 1}:v=0:a=1[out]")
        out = MP3 / f"beat-{bid}-listen.mp3"
        run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", ";".join(filters), "-map", "[out]",
             "-ar", "24000", "-ac", "1", "-b:a", "128k", str(out)])
        total = dur(out)
        beat["audio_file"] = f"mp3/{out.name}"
        beat["narration_audio_file"] = f"mp3/{narr.name}"
        beat["actual_duration_s"] = round(total, 2)
        props = beat["shot"]["remotion"]["props"]
        props["listen"] = [{"label": w["label"], "from": round(w["start_s"] / total, 4),
                            "to": round(w["end_s"] / total, 4)} for w in windows]
        beat["listen_clips"] = windows
        print(f"{bid}: narration {n_dur:.2f}s + clips -> {total:.2f}s  {[(w['label'], w['start_s'], w['end_s']) for w in windows]}")
    sheet_p.write_text(json.dumps(sheet, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
