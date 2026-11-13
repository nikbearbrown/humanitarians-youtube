#!/usr/bin/env python3
"""Final, pre-registered choice of the cathedral room and delivery (run 5). Written BEFORE running.

Findings so far (experiment/demo_grid.json, run 4): pauses beat normal pace in every room; stretching
words (speed 0.78) is no better than normal. That matches the research: in echoing halls the
cellist lengthens pauses (FACTCHECK A11, A15). So D02/D03 use PAUSES, and D04 (dry) keeps
stretching (the researchers' held-notes reading, A12).

DECISION RULE (fixed before this run):
  - Score with whisper small.en (closer to a human listener than base.en), two decodes, mean.
  - Candidates: rooms (tail 0.25, early 1.0) and (tail 0.2, early 1.0); deliveries pauses 0.6 s,
    pauses 0.9 s, and pauses 0.9 s at speed 0.9.
  - Pick the room and delivery where NORMAL <= 0.40 ("most of that got lost" is true) and the
    delivery is >= 0.80, preferring the largest gap. Ties go to the shorter delivery.
  - If no pair qualifies: keep the best-gap pair and REWRITE B02's "Most of that got lost" to match
    what the numbers support (re-opens Gate P for that line). Never tune past this run.
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "experiment"))
from make_ir import build_ir                       # noqa: E402
from room_voice import render, MODELS, SR          # noqa: E402
from demo_grid import score, words, SENTENCE, PHRASES   # noqa: E402

ROOMS = [(0.25, 1.0), (0.2, 1.0)]


def main():
    from kokoro_onnx import Kokoro
    from faster_whisper import WhisperModel
    kok = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
    voice = json.loads((HERE / "beat_sheet.json").read_text())["metadata"]["voice_kokoro"]
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    say = lambda t, sp: np.asarray(kok.create(t, voice=voice, speed=sp, lang="en-us")[0], dtype=np.float64)

    def paused(gap, sp):
        sil = np.zeros(int(gap * SR))
        return np.concatenate(sum(([say(p, sp), sil] for p in PHRASES), [])[:-1])

    takes = {"normal": say(SENTENCE, 1.0), "pauses 0.6s": paused(0.6, 1.0),
             "pauses 0.9s": paused(0.9, 1.0), "pauses 0.9s @0.9": paused(0.9, 0.9)}
    target = words(SENTENCE)
    rows = []
    for g, eg in ROOMS:
        ir = build_ir(g, eg)
        for name, dry in takes.items():
            m, heard = score(model, render(dry, ir), target)
            rows.append({"tail_gain": g, "early_gain": eg, "delivery": name, "word_match": m,
                         "seconds_dry": round(len(dry) / SR, 2), "heard": heard})
            print(f"tail {g:<5} early {eg:<4} {name:17} {m:.2f}  {heard}")
    picks = []
    for g, eg in ROOMS:
        r = [x for x in rows if x["tail_gain"] == g]
        normal = next(x for x in r if x["delivery"] == "normal")["word_match"]
        for x in r:
            if x["delivery"] != "normal":
                picks.append((normal <= 0.40 and x["word_match"] >= 0.80, x["word_match"] - normal,
                              -x["seconds_dry"], g, eg, x["delivery"], normal, x["word_match"]))
    picks.sort(reverse=True)
    best = picks[0]
    decision = {"qualifies": best[0], "tail_gain": best[3], "early_gain": best[4], "delivery": best[5],
                "normal_match": best[6], "delivery_match": best[7]}
    print("DECISION", decision)
    (HERE / "experiment" / "demo_final.json").write_text(json.dumps({"rows": rows, "decision": decision}, indent=1))


if __name__ == "__main__":
    main()
