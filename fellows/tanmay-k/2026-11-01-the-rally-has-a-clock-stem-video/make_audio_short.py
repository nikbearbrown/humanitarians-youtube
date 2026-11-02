#!/usr/bin/env python3
"""Short narration: Kokoro am_onyx, each line synthesised WHOLE, 0.3 s lead, 0.8 s pauses (never 1 s), 0.6 s tail; stage-1 loudness -16 LUFS.
Whisper small.en then times every word and checks the heard text against the signed narration.  Writes mp3/short.wav, mp3/timings_short.json.
Run: /opt/homebrew/bin/python3.12 make_audio_short.py"""
import difflib, json, re, subprocess, sys, wave
from pathlib import Path
import numpy as np
HERE = Path(__file__).parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent))
from short_text import S
from cues import spoken, norm            # numerals + ordinals normaliser from the long film's cue script
MODELS = Path("/Users/tanny/Humanitarians_AI/brutalist.art/runtime/models/kokoro"); SR = 24000
LEAD, GAP, TAIL = 0.30, 0.80, 0.60

def write_wav(p, x):
    with wave.open(str(p), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(x, -1, 1) * 32767).astype("<i2").tobytes())

def main():
    from kokoro_onnx import Kokoro
    from kokoro_onnx.tokenizer import Tokenizer
    kok = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin")); tok = Tokenizer()
    parts = [np.zeros(int(LEAD * SR))]; t = LEAD; lines = []
    for i, (sid, title, text, _v, _s) in enumerate(S):
        a, sr = kok.create(tok.phonemize(text, "en-us"), voice="am_onyx", speed=1.0, lang="en-us", is_phonemes=True); assert sr == SR
        a = np.asarray(a, dtype=np.float64); d = len(a) / SR
        lines.append({"id": sid, "text": text, "start": round(t, 3), "end": round(t + d, 3)}); parts.append(a); t += d
        gap = GAP if i < len(S) - 1 else TAIL
        parts.append(np.zeros(int(gap * SR))); t += gap
    raw = HERE / "mp3" / "short.raw.wav"; write_wav(raw, np.concatenate(parts))
    out = HERE / "mp3" / "short.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-af", "loudnorm=I=-16:TP=-2:LRA=11", "-ar", "48000", "-ac", "1", str(out)], check=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)], capture_output=True, text=True).stdout)
    words = sum(len(l["text"].split()) for l in lines)
    print(f"{words} words, {dur:.2f} s, {words/dur:.2f} words per second overall")
    for l in lines: print(f"  {l['id']} {l['start']:6.2f}-{l['end']:6.2f}  ({l['end']-l['start']:.1f} s)")
    from faster_whisper import WhisperModel
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    segs, _ = model.transcribe(str(raw), word_timestamps=True, language="en")
    wl = [(w.word.strip(), round(w.start, 3), round(w.end, 3)) for s_ in segs for w in s_.words]
    heard = []
    for w, s0, e0 in wl:
        heard += [n for n in (norm(x) for x in spoken(w)) if n]
    ref = [norm(w) for l in lines for w in l["text"].split() if norm(w)]
    sm = difflib.SequenceMatcher(None, ref, heard, autojunk=False)
    print(f"WHISPER match {sm.ratio():.3f}", [x for x in difflib.unified_diff(ref, heard, lineterm="", n=0) if x[:1] in "+-" and x[:3] not in ("+++", "---")][:14])
    (HERE / "mp3" / "timings_short.json").write_text(json.dumps({"duration_s": round(dur, 3), "lines": lines, "words": wl}, indent=1))

if __name__ == "__main__": main()
