#!/usr/bin/env python3
"""Which delivery survives the simulated cathedral, and in what room? Measured with Whisper.

History (kept, PLAYBOOK §11):
- run 1: room_voice.py at full tail. Slowed speech scored WORSE (0.2) than normal (0.5).
- run 2: an earlier version of this grid scaled the tail by hand and accidentally left its first
  0.12 s at full level. It measured a different room from the film's (0.25 tail: normal 0.45 /
  slowed 0.90); room_voice.py at the "same" setting then gave 0.1 / 0.2.
- run 3: shared path (make_ir.build_ir + room_voice.render), no early field: nothing clearly
  survives (best 0.30 -> 0.55 at tail 0.06).
- run 4 (this file): adds an explicit early diffuse field (make_ir.EARLY_FIELD_GAIN) and sweeps it.
  The grid imports the film's own generator and signal path, so it measures what the film plays.

Deliveries: normal (speed 1.0) · slowed (0.78, the signed D02) · pauses (phrases at 1.0 + gaps).
Run:  /opt/homebrew/bin/python3.12 experiment/demo_grid.py
"""
import difflib
import json
import re
import sys
import tempfile
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
from make_ir import build_ir            # noqa: E402
from room_voice import render, MODELS, SR, write_wav   # noqa: E402

SENTENCE = "Every room you play in is asking you a question."
PHRASES = ["Every room", "you play in", "is asking you", "a question."]
TAIL_GAINS = [0.25, 0.15]
EARLY_GAINS = [0.0, 0.5, 1.0]   # 0.0 = the run-3 room (sparse taps only)


def words(s):
    return re.findall(r"[a-z']+", s.lower())


def score(model, y, target):
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "t.wav"
        write_wav(f, y)
        scores, heard_all = [], []
        for beam in (1, 5):          # two decodes, so one lucky decode can't decide it
            segs, _ = model.transcribe(str(f), language="en", beam_size=beam,
                                       condition_on_previous_text=False)
            heard = " ".join(s.text.strip() for s in segs)
            sm = difflib.SequenceMatcher(None, target, words(heard))
            scores.append(sum(m.size for m in sm.get_matching_blocks()) / len(target))
            heard_all.append(heard)
    return round(float(np.mean(scores)), 2), heard_all


def main():
    from kokoro_onnx import Kokoro
    from faster_whisper import WhisperModel
    kok = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
    voice = json.loads((HERE / "beat_sheet.json").read_text())["metadata"]["voice_kokoro"]
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    say = lambda t, sp: np.asarray(kok.create(t, voice=voice, speed=sp, lang="en-us")[0], dtype=np.float64)
    takes = {"normal": say(SENTENCE, 1.0), "slowed 0.78": say(SENTENCE, 0.78)}
    chunks = [say(p, 1.0) for p in PHRASES]
    sil = np.zeros(int(0.6 * SR))
    takes["pauses 0.6s"] = np.concatenate(sum(([c, sil] for c in chunks), [])[:-1])
    target = words(SENTENCE)
    rows = []
    for g in TAIL_GAINS:
        for eg in EARLY_GAINS:
            ir = build_ir(g, eg)
            for name, dry in takes.items():
                m, heard = score(model, render(dry, ir), target)
                rows.append({"tail_gain": g, "early_gain": eg, "delivery": name, "word_match": m,
                             "heard": heard})
                print(f"tail {g:<5} early {eg:<4} {name:12} {m:.2f}  {heard}")
    (HERE / "experiment" / "demo_grid.json").write_text(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
