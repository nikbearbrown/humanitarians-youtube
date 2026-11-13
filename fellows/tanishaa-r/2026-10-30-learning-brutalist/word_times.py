"""word_times.py — measure when each word is actually spoken in Bella's audio.

Runs faster-whisper (local, free) with word timestamps on every mp3/beat-*.mp3
and writes mp3/words.json: {"B06": [{"w": "So", "s": 0.12, "e": 0.30}, ...]}.
build_sheet.py uses these real times for on-screen reveals instead of
estimating from word position (which drifts at every pause).

Run inside the brutalist env:  python word_times.py
"""
import json
from pathlib import Path

from faster_whisper import WhisperModel

HERE = Path(__file__).resolve().parent


def main():
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    out = {}
    for mp3 in sorted((HERE / "mp3").glob("beat-*.mp3")):
        bid = mp3.stem.split("-", 1)[1]
        segs, _ = model.transcribe(str(mp3), word_timestamps=True, language="en")
        out[bid] = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)}
                    for s in segs for w in s.words]
        print(bid, len(out[bid]), "words")
    (HERE / "mp3" / "words.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
