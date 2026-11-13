"""How well auto-captions find each word, and when it was said: measured on speech with known timings.

    python captions.py            # writes evidence/run.log, evidence/results.json, evidence/scene.json, WAVs

The recogniser is faster-whisper, model "base" (the one our pipeline's align.py uses for word timings), run
offline on the CPU with word_timestamps=True.

Ground truth: 24 sentences of everyday English are built word by word from our narrator's voice (Kokoro,
af_bella): each word is synthesised on its own, its leading and trailing silence trimmed, and the words are
joined with short gaps. So the true start of every word is known to the sample. (Word-by-word speech is a little
choppier than a real read; the test is of timing, and is stated as built this way.)

  1. clean    — word error rate (WER) and the start-time error of every correctly heard word.
  2. noise    — the same 24 sentences with pink noise added at 20, 10, 5, 0 and -5 dB SNR.
WER = (substitutions + deletions + insertions) / reference words, after lower-casing and removing punctuation.
"""
import json
import os
import re
import sys
import wave
from pathlib import Path

import numpy as np

TOOLKIT = Path("D:/Rohan/Claude/HAI/RohanClaudeHAIbrutalist.art")
sys.path.insert(0, str(TOOLKIT / "runtime" / "scripts"))
os.environ.setdefault("HF_HUB_OFFLINE", "1")
from generate_audio_kokoro import load_engine  # noqa: E402

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
VOICE = "af_bella"
SENTENCES = [
    "The train to Boston leaves from platform nine at noon",
    "Please bring a jacket because the evening gets cold",
    "She played the piano while her brother sang along",
    "We need two eggs a cup of milk and some flour",
    "The meeting moved to Thursday afternoon in the small room",
    "Turn left at the bakery and walk past the park",
    "His new song has a slow verse and a loud chorus",
    "The library closes early on Sundays during the summer",
    "Our team finished the project two days before the deadline",
    "A light rain fell over the quiet harbor all morning",
    "Put the blue folder on the shelf next to the printer",
    "The coach asked every player to run three more laps",
    "My grandmother keeps her old letters in a wooden box",
    "The museum opens a new exhibit about ocean life today",
    "Remember to water the plants while I am away",
    "The bus was late so we walked home through the snow",
    "He fixed the broken chair with glue and a few nails",
    "Fresh bread from the market smells better than anything",
    "The children built a tall tower out of colored blocks",
    "Send me the photos from the concert when you can",
    "The pilot said we would land twenty minutes early",
    "A small black cat slept on the warm window seat",
    "Our neighbors painted their fence a bright shade of green",
    "The teacher wrote the answer slowly on the board",
]
SNRS = [None, 20, 10, 5, 0, -5]
SR = 24000


ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def num_words(n):
    return [ONES[n]] if n < 20 else [TENS[n // 10]] + ([ONES[n % 10]] if n % 10 else [])


def norm(s):
    """lower-case, drop punctuation, and spell out numbers 0-99 (so "9" and "nine" are the same word)."""
    out = []
    for tok in re.sub(r"[^a-z0-9' ]+", " ", s.lower()).split():
        out += num_words(int(tok)) if tok.isdigit() and int(tok) < 100 else [tok]
    return out


def to16k(x):
    """faster-whisper reads a NumPy array as 16 kHz audio; our voice is 24 kHz."""
    from scipy.signal import resample_poly
    return resample_poly(x, 2, 3).astype(np.float32)


def build(k, cache):
    """Sentence audio + true word starts (s). Words are synthesised once and reused."""
    rng = np.random.default_rng(7)
    out = []
    for sent in SENTENCES:
        parts, starts, t = [], [], 0.25
        parts.append(np.zeros(int(0.25 * SR), np.float32))
        for w in sent.split():
            if w not in cache:
                y, sr = k.create(w, voice=VOICE, speed=1.0, lang="en-us")
                y = np.asarray(y, np.float32)
                assert sr == SR
                env = np.abs(y) > 0.02 * np.abs(y).max()
                i0, i1 = np.argmax(env), len(env) - np.argmax(env[::-1])
                cache[w] = y[max(0, i0 - int(0.005 * SR)): i1 + int(0.01 * SR)]
            starts.append(t + 0.005)
            parts.append(cache[w]); t += len(cache[w]) / SR
            gap = rng.uniform(0.04, 0.12)
            parts.append(np.zeros(int(gap * SR), np.float32)); t += gap
        parts.append(np.zeros(int(0.4 * SR), np.float32))
        out.append((sent, np.concatenate(parts), starts))
    return out


def pink(n, rng):
    X = np.fft.rfft(rng.standard_normal(n)); f = np.fft.rfftfreq(n, 1 / SR)
    X[1:] /= np.sqrt(f[1:]); X[0] = 0
    return np.fft.irfft(X, n)


def align(ref, hyp):
    """Levenshtein alignment; returns (subs, dels, ins, pairs of (ref_index, hyp_index) that match exactly)."""
    n, m = len(ref), len(hyp)
    D = np.zeros((n + 1, m + 1), int); D[:, 0] = range(n + 1); D[0, :] = range(m + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i, j] = min(D[i - 1, j] + 1, D[i, j - 1] + 1, D[i - 1, j - 1] + (ref[i - 1] != hyp[j - 1]))
    i, j, s, d, ins, pairs = n, m, 0, 0, 0, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i, j] == D[i - 1, j - 1] + (ref[i - 1] != hyp[j - 1]):
            if ref[i - 1] == hyp[j - 1]:
                pairs.append((i - 1, j - 1))
            else:
                s += 1
            i, j = i - 1, j - 1
        elif i > 0 and D[i, j] == D[i - 1, j] + 1:
            d += 1; i -= 1
        else:
            ins += 1; j -= 1
    return s, d, ins, pairs[::-1]


def run(asr, items, snr, rng):
    tot_ref = errs = 0
    timing = []
    detail = []
    for sent, y, starts in items:
        x = y.copy()
        if snr is not None:
            nz = pink(len(y), rng)
            ps = np.mean(y[np.abs(y) > 0] ** 2); pn = np.mean(nz ** 2)
            x = y + nz * np.sqrt(ps / (pn * 10 ** (snr / 10)))
        x = (x / (np.abs(x).max() + 1e-9) * 0.9).astype(np.float32)
        if snr == 0 and sent == SENTENCES[0]:      # the listening clip: exactly the audio the run transcribed
            pcm = (np.clip(x, -1, 1) * 32767).astype("<i2")
            with wave.open(str(EV / "sentence_1_0db.wav"), "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
        segs, _ = asr.transcribe(to16k(x), language="en", word_timestamps=True, beam_size=5)
        words = [(w.word, w.start) for sg in segs for w in (sg.words or [])]
        hyp, hstart = [], []
        for w, st in words:
            for tok in norm(w):
                hyp.append(tok); hstart.append(st)
        ref = norm(sent)
        s, d, ins, pairs = align(ref, hyp)
        tot_ref += len(ref); errs += s + d + ins
        for ri, hi in pairs:
            timing.append(hstart[hi] - starts[ri])
        detail.append(dict(ref=sent, hyp=" ".join(hyp), s=s, d=d, i=ins))
    t = np.abs(np.array(timing)) * 1000
    return dict(snr=snr, wer=round(100 * errs / tot_ref, 1), words=tot_ref, matched=len(timing),
                med_ms=round(float(np.median(t)), 0), p90_ms=round(float(np.percentile(t, 90)), 0),
                signed_med_ms=round(float(np.median(np.array(timing) * 1000)), 0), detail=detail)


def main():
    EV.mkdir(exist_ok=True)
    log = []
    P = lambda *a: (log.append(" ".join(str(x) for x in a)), print(*a))
    k = load_engine()
    from faster_whisper import WhisperModel
    asr = WhisperModel("base", device="cpu", compute_type="int8")
    items = build(k, {})
    total_s = sum(len(y) for _, y, _ in items) / SR
    P(f"TEST SET: {len(items)} sentences, {sum(len(s.split()) for s in SENTENCES)} words, {total_s:.0f} s of speech "
      f"(Kokoro {VOICE}, word by word, true starts known); recogniser faster-whisper base, word_timestamps=True")
    rng = np.random.default_rng(11)
    res = []
    for snr in SNRS:
        r = run(asr, items, snr, rng)
        res.append(r)
        P(f"  {'clean' if snr is None else f'{snr:+d} dB SNR':12s} WER {r['wer']:5.1f}%   start error: median {r['med_ms']:.0f} ms, "
          f"90% within {r['p90_ms']:.0f} ms ({r['matched']} words matched), signed median {r['signed_med_ms']:+.0f} ms")
    P("")
    P("Misheard (clean): " + "; ".join(f"'{d['ref']}' -> '{d['hyp']}'" for d in res[0]["detail"] if d["s"] + d["d"] + d["i"]))
    P("Misheard (0 dB, first 3): " + "; ".join([f"'{d['ref']}' -> '{d['hyp']}'" for d in res[4]["detail"] if d["s"] + d["d"] + d["i"]][:3]))

    # the scene's worked example: sentence 1 clean, its waveform envelope, true starts and Whisper's
    sent, y, starts = items[0]
    segs, _ = asr.transcribe(to16k(y / np.abs(y).max() * 0.9), language="en", word_timestamps=True)
    ws = [dict(w=w.word.strip(), start=round(w.start, 3), end=round(w.end, 3)) for sg in segs for w in (sg.words or [])]
    blk = len(y) // 600
    env = np.abs(y[: blk * 600]).reshape(600, blk).max(1)
    pcm = (np.clip(y / np.abs(y).max() * 0.9, -1, 1) * 32767).astype("<i2")
    with wave.open(str(EV / "sentence_1.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    (EV / "run.log").write_text("\n".join(log) + "\n", encoding="utf-8")
    (EV / "results.json").write_text(json.dumps(dict(sentences=SENTENCES, results=res), indent=1), encoding="utf-8")
    (EV / "scene.json").write_text(json.dumps(dict(example=dict(sentence=sent, seconds=round(len(y) / SR, 3),
        env=[round(float(v), 3) for v in env / env.max()], true=[round(s, 3) for s in starts], whisper=ws),
        curve=[{k2: r[k2] for k2 in ("snr", "wer", "med_ms", "p90_ms")} for r in res]), separators=(",", ":")), encoding="utf-8")


if __name__ == "__main__":
    main()
