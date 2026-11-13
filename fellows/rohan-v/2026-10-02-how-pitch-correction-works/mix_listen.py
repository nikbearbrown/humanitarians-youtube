"""Appends the listening clips to B04's and B05's narration, so the viewer hears the evidence.

B04: narration, then the melody AS SUNG (evidence/sung.wav), then CORRECTED (corrected_instant.wav).
B05: narration, then INSTANT (corrected_instant.wav), then SLOW (corrected_natural.wav).

Each clip is the unedited output of pitch_demo.py, resampled to the narration's rate and set to the
narration's RMS level (same loudness, nothing else changed). The mixed file becomes the beat's
audio_file; actual_duration_s is re-measured from it, and the clip windows are written into the beat's
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

PLAN = {
    "B04": [("AS SUNG", "sung.wav"), ("CORRECTED", "corrected_instant.wav")],
    "B05": [("INSTANT", "corrected_instant.wav"), ("SLOW", "corrected_natural.wav")],
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
        for i, (label, wav) in enumerate(PLAN[bid], start=1):
            c = EV / wav
            gain = n_db - rms_db(c)
            inputs += ["-i", str(c)]
            pad = TAIL if i == len(PLAN[bid]) else GAP
            filters.append(f"[{i}:a]aresample=24000,aformat=channel_layouts=mono,volume={gain:.2f}dB,"
                           f"apad=pad_dur={pad}[c{i}]")
            cd = dur(c)
            windows.append({"label": label, "file": wav, "start_s": round(t, 3), "end_s": round(t + cd, 3),
                            "gain_db": round(gain, 2)})
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
