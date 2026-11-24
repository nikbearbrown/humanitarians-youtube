import json, os
from faster_whisper import WhisperModel
HERE = os.path.dirname(os.path.abspath(__file__))
d = {b["beat_id"]: b for b in json.load(open(os.path.join(HERE, "beat_sheet.json")))["beats"]}
m = WhisperModel("small.en", device="cpu", compute_type="int8")
for bid in ("B02", "B11", "B12", "B15", "BOUT", "B00"):
    segs, _ = m.transcribe(os.path.join(HERE, d[bid]["audio_file"]), language="en", beam_size=5, word_timestamps=True)
    words = [(w.word.strip(), round(w.probability, 2)) for s in segs for w in s.words]
    print(f"\n[{bid}] script: {d[bid]['narration_text']}\n  heard : {' '.join(w for w,_ in words)}")
    print("  low-confidence words:", [(w, p) for w, p in words if p < 0.6])
