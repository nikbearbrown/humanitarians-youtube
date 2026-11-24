"""Whisper-check the narration: transcribe each beat mp3 and compare with narration_text."""
import json, re, os, difflib
from faster_whisper import WhisperModel
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "beat_sheet.json")))
model = WhisperModel("base.en", device="cpu", compute_type="int8")
NUM = {"0":"zero","1":"one","2":"two","3":"three","4":"four","10":"ten","16":"sixteen","64":"sixty four","512":"five hundred and twelve","2048":"two thousand and forty eight"}
def norm(t):
    t = t.lower().replace("-", " ").replace("’", "'")
    t = re.sub(r"[^a-z0-9' ]", " ", t)
    return t.split()
out = []
for b in d["beats"]:
    segs, _ = model.transcribe(os.path.join(HERE, b["audio_file"]), language="en", beam_size=5, word_timestamps=False)
    heard = " ".join(s.text.strip() for s in segs)
    want = b["narration_text"]
    a, h = norm(want), norm(heard)
    sm = difflib.SequenceMatcher(None, a, h)
    diffs = [(" ".join(a[i1:i2]), " ".join(h[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
    out.append((b["beat_id"], round(sm.ratio(), 3), heard, diffs))
    print(f"\n[{b['beat_id']}] match={sm.ratio():.3f}\n  heard: {heard}")
    for w, hh in diffs: print(f"  script: {w!r:45} heard: {hh!r}")
json.dump(out, open(os.path.join(HERE, "transcribe_report.json"), "w"), indent=1)
