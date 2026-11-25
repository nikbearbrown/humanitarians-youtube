"""tts_demo.py — the real evidence for B04/B05 of "How a Computer Turns Text into a Voice".

Runs the same engine that narrates the video (Kokoro-82M via kokoro-onnx, espeak-ng
phonemizer) on a few tricky sentences, in Bella (af_bella) and one other built-in
voice, and records: the phonemes it chose, the sample rate, the size of a voice
style, the waveform (downsampled for drawing), and what a speech recognizer
(faster-whisper) hears back. Writes demo/tts_output.json and demo/*.wav.

Run inside the brutalist env:  python demo/tts_demo.py
"""
import json
from pathlib import Path

import numpy as np
import soundfile as sf
from faster_whisper import WhisperModel
from kokoro_onnx import Kokoro
from kokoro_onnx.tokenizer import Tokenizer

HERE = Path(__file__).resolve().parent
MODELS = HERE.parents[2] / "brutalist.art" / "runtime" / "models" / "kokoro"
VOICES = ["af_bella", "am_michael"]
SENTENCES = ["I read it yesterday.", "I will read it tomorrow.", "Dr. Lee lives on Oak Dr.", "It costs $5 in 2026."]

k = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
tk = Tokenizer()
asr = WhisperModel("base.en", device="cpu", compute_type="int8")
style = k.get_voice_style("af_bella")
out = {"engine": "kokoro-onnx 0.6.1, Kokoro-82M v1.0", "phonemizer": "espeak-ng (via kokoro_onnx.Tokenizer)",
       "style_shape": list(style.shape), "style_numbers_per_voice": int(style.shape[-1]),
       "bella_style_first8": [round(float(x), 3) for x in style[40, 0, :8]],
       "michael_style_first8": [round(float(x), 3) for x in k.get_voice_style("am_michael")[40, 0, :8]],
       "sentences": []}
for i, s in enumerate(SENTENCES):
    row = {"text": s, "phonemes": tk.phonemize(s, "en-us"), "voices": {}}
    for v in VOICES:
        audio, sr = k.create(s, voice=v, speed=0.95)
        wav = HERE / f"s{i}-{v}.wav"
        sf.write(wav, audio, sr)
        segs, _ = asr.transcribe(str(wav), word_timestamps=True, language="en")
        words = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)} for g in segs for w in g.words]
        env = np.abs(audio)
        n = 240
        env = [round(float(env[j * len(env) // n:(j + 1) * len(env) // n].max()), 3) for j in range(n)]
        row["voices"][v] = {"sample_rate": sr, "samples": len(audio), "seconds": round(len(audio) / sr, 3),
                            "heard": " ".join(w["w"] for w in words), "words": words, "envelope": env,
                            "raw_first12": [round(float(x), 4) for x in audio[int(0.3 * sr):int(0.3 * sr) + 12]]}
    out["sentences"].append(row)
    print(s, "|", row["phonemes"], "|", {v: row["voices"][v]["heard"] for v in VOICES})
(HERE / "tts_output.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print("sample rate", out["sentences"][0]["voices"]["af_bella"]["sample_rate"], "· style", out["style_shape"])
