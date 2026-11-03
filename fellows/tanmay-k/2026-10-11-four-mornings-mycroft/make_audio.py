#!/usr/bin/env python3
"""Narration audio for every beat of *Four Mornings*, with the Mycroft pronunciation override, then checks.

Adapted from the topic video's make_audio.py. Kokoro says "Mycroft" as MICK-roft (mˈɪkɹɔft); the
override signed in SCRIPT.md makes it MY-croft (mˈaɪkɹɔft). Each beat's text is phonemized with
Kokoro's own tokenizer, the wrong phonemes are swapped, and Kokoro speaks the phonemes
(is_phonemes=True). Every swap is asserted, so an override that silently didn't apply fails the run.
The narration text and captions keep the real spelling.

Writes mp3/beat-<ID>.wav + .mp3 and mp3/timings.json; then runs:
  1. stage-1 loudness: every beat to -16 LUFS / -2 dBTP (the master goes to -14 at compile, normalise.py)
  2. gap sweep (PLAYBOOK §1d): silences > 0.55 s inside narration beats
  3. Whisper (small.en) on every narration beat: word match vs the signed text, worst first
Run:  /opt/homebrew/bin/python3.12 make_audio.py
"""
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
MODELS = HERE.parent.parent / "brutalist.art" / "runtime" / "models" / "kokoro"
SR = 24000


def write_wav(p, x):
    import wave
    p.parent.mkdir(exist_ok=True)
    pcm = (np.clip(x, -1, 1) * 32767).astype("<i2")
    with wave.open(str(p), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())


# --dir short  → the Short (short/beat_sheet.json, short/mp3/); default is the long film
if "--dir" in sys.argv:
    HERE = HERE / sys.argv[sys.argv.index("--dir") + 1]

# Kokoro's own (wrong) phonemes → the override signed in SCRIPT.md (TTS spelling)
OVERRIDES = {
    "Mycroft": ("mˈɪkɹɔft", "mˈaɪkɹɔft"),
}
STAGE1_I, STAGE1_TP = -16.0, -2.0


NUMBER_WORDS = set("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
                   "fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy "
                   "eighty ninety hundred thousand point percent and".split())


def words(s):
    """Lower-case words, with any run of number words or digits collapsed to one '#', so 'three
    hundred and three' and '303' compare equal (Whisper writes numbers as digits)."""
    toks = re.findall(r"[a-z']+|\d[\d.,%]*", s.lower().replace("-", " "))
    out = []
    for t in toks:
        num = t[0].isdigit() or (t in NUMBER_WORDS and t != "and")
        if t == "and" and out and out[-1] == "#":
            continue                      # "hundred and three" stays one number
        if num:
            if not out or out[-1] != "#":
                out.append("#")
        else:
            out.append(t)
    return out


def main():
    if "--check-only" in sys.argv:
        return whisper_check(json.loads((HERE / "beat_sheet.json").read_text()))
    from kokoro_onnx import Kokoro
    from kokoro_onnx.tokenizer import Tokenizer
    sheet = json.loads((HERE / "beat_sheet.json").read_text())
    voice = sheet["metadata"]["voice_kokoro"]
    kok = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
    tok = Tokenizer()
    timings, applied = {}, []
    only = sys.argv[sys.argv.index("--only") + 1].split(",") if "--only" in sys.argv else None
    old = json.loads((HERE / "mp3" / "timings.json").read_text()) if only else {}
    for b in sheet["beats"]:
        bid = b["beat_id"]
        wav = HERE / "mp3" / f"beat-{bid}.wav"
        if only and bid not in only:      # --only S01: regenerate just these; keep the others' measured audio
            timings[bid] = old[bid]
            continue
        if b["act"] != "DEMO":
            ph = tok.phonemize(b["narration_text"], "en-us")
            for word, (wrong, right) in OVERRIDES.items():
                if word in b["narration_text"]:
                    n = ph.count(wrong)
                    assert n >= 1, f"{bid}: override for {word} found no '{wrong}' in {ph!r}"
                    ph = ph.replace(wrong, right)
                    applied.append((bid, word, n))
            audio, sr = kok.create(ph, voice=voice, speed=1.0, lang="en-us", is_phonemes=True)
            assert sr == SR
            write_wav(wav, np.asarray(audio, dtype=np.float64))
        # stage-1 loudness, every beat (DEMO included), into the .mp3 the compiler reads
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-af",
                        f"loudnorm=I={STAGE1_I}:TP={STAGE1_TP}:LRA=11", "-ar", str(SR),
                        "-codec:a", "libmp3lame", "-q:a", "2", str(wav.with_suffix(".mp3"))], check=True)
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                    "csv=p=0", str(wav.with_suffix(".mp3"))], capture_output=True, text=True).stdout)
        timings[bid] = round(dur, 3)
    (HERE / "mp3" / "timings.json").write_text(json.dumps(timings, indent=1))
    print(f"{len(timings)} beats · {sum(timings.values()):.1f} s total · overrides applied: "
          + ", ".join(f"{w}@{b}" for b, w, _ in applied))

    # gap sweep: narration beats only (DEMO pauses are deliberate)
    print("\nGAPS > 0.55 s inside narration beats:")
    for b in sheet["beats"]:
        if b["act"] == "DEMO":
            continue
        r = subprocess.run(["ffmpeg", "-i", str(HERE / "mp3" / f"beat-{b['beat_id']}.mp3"), "-af",
                            "silencedetect=n=-40dB:d=0.55", "-f", "null", "-"], capture_output=True, text=True)
        starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
        ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
        inner = [(s, e) for s, e in zip(starts, ends) if s > 0.05 and e < timings[b["beat_id"]] - 0.05]
        if inner:
            print(f"  {b['beat_id']}: " + ", ".join(f"{s:.2f}–{e:.2f}s" for s, e in inner))

    whisper_check(sheet)


def whisper_check(sheet):
    from faster_whisper import WhisperModel
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    rows = []
    for b in sheet["beats"]:
        if b["act"] == "DEMO":
            continue
        segs, _ = model.transcribe(str(HERE / "mp3" / f"beat-{b['beat_id']}.wav"), language="en",
                                   beam_size=5, condition_on_previous_text=False)
        heard = " ".join(s.text.strip() for s in segs)
        t, h = words(b["narration_text"]), words(heard)
        sm = difflib.SequenceMatcher(None, t, h)
        diffs = [(" ".join(t[i1:i2]), " ".join(h[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
        rows.append({"beat": b["beat_id"], "match": round(sm.ratio(), 3), "heard": heard, "diffs": diffs})
    rows.sort(key=lambda r: r["match"])
    (HERE / "mp3" / "whisper_check.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print("\nWHISPER (small.en), worst first:")
    for r in rows:
        print(f"  {r['beat']}  {r['match']:.3f}  " + " | ".join(f"'{a}'→'{b}'" for a, b in r["diffs"][:6]))


if __name__ == "__main__":
    main()
