#!/usr/bin/env python3
"""DEMO beats: Kokoro at each beat's own speed, then the beat's impulse response (audio_fx).

generate_audio_kokoro.py takes one global --speed, so DEMO beats are made here instead; the toolkit
is not modified. For every DEMO beat in beat_sheet.json this writes:

  mp3/beat-<ID>.wav / .mp3      the audio the film uses (dry voice convolved with the IR, or dry)
  envelopes/<ID>.json           30 fps RMS envelopes (dB) of the DRY voice and of the ROOM output,
                                which RoomVoice draws. Real audio, no invented shapes
  envelopes/whisper.json        what Whisper hears in each, scored against the sentence. That's the
                                objective check that the cold open's "Most of that got lost" is true

Run:  /opt/homebrew/bin/python3.12 room_voice.py   (needs kokoro_onnx, numpy, scipy, faster_whisper)
"""
import json
import re
import subprocess
import wave
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

HERE = Path(__file__).parent
MODELS = HERE.parent.parent / "brutalist.art" / "runtime" / "models" / "kokoro"
SR = 24000
FPS = 30


def read_wav(p):
    with wave.open(str(p)) as w:
        assert w.getframerate() == SR, f"{p}: {w.getframerate()} Hz, expected {SR}"
        x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float64) / 32768
    return x


def write_wav(p, x):
    p.parent.mkdir(exist_ok=True)
    pcm = (np.clip(x, -1, 1) * 32767).astype("<i2")
    with wave.open(str(p), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())


def envelope(x):
    hop = SR // FPS
    frames = [x[i:i + hop] for i in range(0, len(x), hop)]
    return [round(float(20 * np.log10(np.sqrt(np.mean(f ** 2)) + 1e-6)), 1) for f in frames if len(f)]


def render(dry, ir):
    """Dry voice → the room. Shared with experiment/demo_grid.py, so the grid measures this path."""
    if ir is not None:
        wet = fftconvolve(dry, ir)
        # keep the tail until it falls 50 dB below the peak, so the echo isn't cut off
        env = np.abs(wet)
        last = np.nonzero(env > env.max() * 10 ** (-50 / 20))[0][-1]
        y = wet[:last + 1]
    else:
        y = np.concatenate([dry, np.zeros(int(0.4 * SR))])
    # same RMS for every DEMO beat, so the wet/dry comparison isn't a loudness comparison
    y = y / (np.sqrt(np.mean(y ** 2)) + 1e-12) * 0.08
    return y / max(1.0, np.max(np.abs(y)) / 0.89)          # ≤ -1 dBFS


def words(s):
    return re.findall(r"[a-z']+", s.lower())


def main():
    from kokoro_onnx import Kokoro
    sheet = json.loads((HERE / "beat_sheet.json").read_text())
    kok = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
    voice = sheet["metadata"]["voice_kokoro"]
    demos = [b for b in sheet["beats"] if b["act"] == "DEMO"]
    out = {}
    for b in demos:
        fx = b["audio_fx"]
        if fx.get("phrases"):
            # pauses delivery (experiment/demo_final.json): phrases joined by silence
            sil = np.zeros(int(fx["pause_s"] * SR))
            parts = [np.asarray(kok.create(p, voice=voice, speed=fx["speed"], lang="en-us")[0], dtype=np.float64)
                     for p in fx["phrases"]]
            dry = np.concatenate(sum(([p, sil] for p in parts), [])[:-1])
        else:
            dry, sr = kok.create(b["narration_text"], voice=voice, speed=fx["speed"], lang="en-us")
            assert sr == SR
            dry = np.asarray(dry, dtype=np.float64)
        y = render(dry, read_wav(HERE / fx["ir"]) if fx.get("ir") else None)
        wav = HERE / "mp3" / f"beat-{b['beat_id']}.wav"
        write_wav(wav, y)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav), "-codec:a", "libmp3lame",
                        "-q:a", "2", str(wav.with_suffix(".mp3"))], check=True)
        drypad = np.concatenate([dry / (np.max(np.abs(dry)) + 1e-12), np.zeros(max(0, len(y) - len(dry)))])
        (HERE / "envelopes").mkdir(exist_ok=True)
        (HERE / "envelopes" / f"{b['beat_id']}.json").write_text(json.dumps(
            {"fps": FPS, "seconds": round(len(y) / SR, 2), "dry_seconds": round(len(dry) / SR, 2),
             "dry": envelope(drypad), "room": envelope(y / (np.max(np.abs(y)) + 1e-12))}))
        out[b["beat_id"]] = {"seconds": round(len(y) / SR, 2), "dry_seconds": round(len(dry) / SR, 2),
                             "speed": fx["speed"], "ir": fx.get("ir")}
        print(b["beat_id"], out[b["beat_id"]])

    from faster_whisper import WhisperModel
    import difflib
    model = WhisperModel("small.en", device="cpu", compute_type="int8")   # as demo_final.py
    for bid, rec in out.items():
        segs, _ = model.transcribe(str(HERE / "mp3" / f"beat-{bid}.wav"), language="en", beam_size=5,
                                   condition_on_previous_text=False)
        heard = " ".join(s.text.strip() for s in segs)
        target = words(demos[0]["narration_text"])
        sm = difflib.SequenceMatcher(None, target, words(heard))
        rec["whisper_heard"] = heard
        rec["word_match"] = round(sum(m.size for m in sm.get_matching_blocks()) / len(target), 2)
        print(bid, rec["word_match"], repr(heard))
    (HERE / "envelopes" / "whisper.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
