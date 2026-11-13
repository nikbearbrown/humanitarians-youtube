#!/usr/bin/env python3
"""Measured cue clock: when each narration word starts, from Whisper word timestamps.

The pause-anchored clock (cue_align.py) ran up to 1.2 s late in B07, where a long sentence has no
pause to anchor to. This writes mp3/word_times.json: for every beat, the start time of each word of
the signed narration (null where Whisper's words don't align). build_beat_sheet.py reads it first and
falls back to cue_align only for a cue whose word didn't align.
Run after make_audio.py:  /opt/homebrew/bin/python3.12 align_words.py [--dir short]
"""
import difflib
import json
import re
import sys
from pathlib import Path

from faster_whisper import WhisperModel

HERE = Path(__file__).parent
if "--dir" in sys.argv:   # --dir short → the Short
    HERE = HERE / sys.argv[sys.argv.index("--dir") + 1]
norm = lambda w: re.sub(r"[^a-z0-9']", "", w.lower())  # noqa: E731

model = WhisperModel("small.en", device="cpu", compute_type="int8")
out = {}
for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]:
    segs, _ = model.transcribe(str(HERE / "mp3" / f"beat-{b['beat_id']}.wav"), language="en",
                               word_timestamps=True, beam_size=5, condition_on_previous_text=False)
    heard = [(norm(w.word), round(w.start, 2), round(w.end, 2)) for s in segs for w in s.words]
    signed = [norm(x) for x in b["narration_text"].split()]
    times, ends = [None] * len(signed), [None] * len(signed)
    sm = difflib.SequenceMatcher(None, signed, [h[0] for h in heard], autojunk=False)
    for i, j, n in sm.get_matching_blocks():
        for k in range(n):
            times[i + k], ends[i + k] = heard[j + k][1], heard[j + k][2]
    out[b["beat_id"]] = times
    # the same alignment in the form cue_align.whisper_words reads (captions): signed words, start, end
    (HERE / "_qc" / "whisper").mkdir(parents=True, exist_ok=True)
    (HERE / "_qc" / "whisper" / f"{b['beat_id']}.json").write_text(json.dumps(
        {"words": b["narration_text"].split(), "start": times, "end": ends}))
    print(b["beat_id"], f"{sum(t is not None for t in times)}/{len(times)} words aligned")
(HERE / "mp3" / "word_times.json").write_text(json.dumps(out))
