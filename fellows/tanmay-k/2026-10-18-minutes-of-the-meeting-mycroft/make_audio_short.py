#!/usr/bin/env python3
"""Short narration: Kokoro am_onyx, one continuous track. Audio is the clock.
Each script line is synthesised whole (not sentence by sentence), 0.35 s between lines, 0.15 s lead, 0.8 s tail
(under 1 s: a Short cannot afford dead air). Stage-1 loudness -16 LUFS, then Whisper word times.
Run: /opt/homebrew/bin/python3.12 short/make_audio_short.py"""
import json, re, subprocess, sys, wave
from pathlib import Path
import numpy as np
HERE = Path(__file__).parent; ROOT = HERE.parent    # ROOT is the work-video folder: its make_audio.py is the audio toolkit
sys.path.insert(0, str(ROOT))
import make_audio as ma                      # reuse spoken()/norm() and the Kokoro paths
SR, GAP, LINEGAP, LEAD, TAIL = 24000, 0.22, 0.35, 0.15, 0.8
(HERE / "mp3").mkdir(exist_ok=True)
src = (HERE / "SHORT-SCRIPT.md").read_text()
HEAD = re.compile(r"^### (S\d+) · ([^·]+?) · ~(\d+) s \(tone: ([^)]*)\)", re.M); ms = list(HEAD.finditer(src)); lines = []
for i, m in enumerate(ms):
    blk = src[m.end(): ms[i + 1].start() if i + 1 < len(ms) else len(src)]
    lines.append((m.group(1), " ".join(l[2:].strip() for l in blk.splitlines() if l.startswith("> "))))
from kokoro_onnx import Kokoro
from kokoro_onnx.tokenizer import Tokenizer
kok = Kokoro(str(ma.MODELS / "kokoro-v1.0.onnx"), str(ma.MODELS / "voices-v1.0.bin")); tok = Tokenizer()
chunks, cur, sent_t = [np.zeros(int(LEAD * SR))], LEAD, []
for lid, text in lines:
    # whole-line synthesis: Kokoro paces a full paragraph naturally (about 3.5 words a second); one sentence at a time came out about 30%
    # slower, and 3-word sentences ("Add a half.") were mangled. Sentence times come from the Whisper word clock below.
    ph = ma.phon(tok, text)
    a, sr = kok.create(ph, voice="am_onyx", speed=1.0, lang="en-us", is_phonemes=True); assert sr == SR
    a = np.asarray(a, dtype=np.float64)
    chunks += [a, np.zeros(int(LINEGAP * SR))]; cur += len(a) / SR + LINEGAP
narr_end = cur - LINEGAP
chunks[-1] = np.zeros(int(TAIL * SR)); total = narr_end + TAIL
raw = np.concatenate(chunks)
def write_wav(p, x, sr):
    with wave.open(str(p), "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((np.clip(x, -1, 1) * 32767).astype("<i2").tobytes())
write_wav(HERE / "mp3" / "narration.raw.wav", raw, SR)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(HERE / "mp3" / "narration.raw.wav"), "-af", "loudnorm=I=-16:TP=-2:LRA=11", "-ar", "48000", "-ac", "1", str(HERE / "mp3" / "narration.wav")], check=True)
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(HERE / "mp3" / "narration.wav")], capture_output=True, text=True).stdout)
from faster_whisper import WhisperModel
segs, _ = WhisperModel("small.en", device="cpu", compute_type="int8").transcribe(str(HERE / "mp3" / "narration.raw.wav"), word_timestamps=True, language="en")
words = [(w.word.strip(), round(w.start, 3), round(w.end, 3)) for s in segs for w in s.words]
text_all = " ".join(t for _, t in lines)
import difflib
ref = [t for t in (ma.norm(w) for w in text_all.split()) if t]; heard = ma.heard_words(words)
ratio = difflib.SequenceMatcher(None, ref, heard).ratio()
spans = ma.sentence_spans(text_all, words)
sent_t, k = [], 0
for lid, text in lines:
    for _ in re.split(r"(?<=[.?!])\s+", text.strip()):
        sent_t.append({"line": lid, **spans[k]}); k += 1
json.dump({"lines": [{"id": i, "text": t} for i, t in lines], "text": text_all, "sentences": sent_t, "words": words,
           "narration_end_s": round(narr_end, 3), "duration_s": round(dur, 3)}, open(HERE / "mp3" / "timings_short.json", "w"), indent=1)
print(f"{len(text_all.split())} words, narration {narr_end:.2f} s, track {dur:.2f} s; Whisper match {ratio:.3f}")
diff = [w for w in difflib.unified_diff(ref, heard, lineterm="", n=0) if w[:1] in "+-" and w[:3] not in ("+++", "---")]
print("differences:", diff[:20])
