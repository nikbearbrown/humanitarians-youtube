#!/usr/bin/env python3
"""Narration audio for every beat of *Minutes of the Meeting* (Kokoro am_onyx), audio-first: durations are the master clock.

Beats come from beat_sheet.json (words = SCRIPT.md, Gate P signed). Kokoro says "Mycroft" as MICK-roft (mˈɪkɹɔft); the override
signed in SCRIPT.md makes it MY-croft (mˈaɪkɹɔft); every swap is asserted so an override that silently did not apply fails the run.
--phonemes prints Kokoro's phonemes for every sentence (front-load check) and writes PHONEMES-CHECK.md.

Each beat is synthesised sentence by sentence (Kokoro's token limit), joined with short gaps, padded
(0.15 s lead, 0.45 s tail; B16 gets its 8 s silent hold after the narration), then stage-1 loudness
(-16 LUFS, -2 dBTP). Whisper (small.en, cached) then times every word and checks the spoken text
against the signed narration, worst first. Writes mp3/beat-<ID>.wav, mp3/timings.json.
Run:  /opt/homebrew/bin/python3.12 make_audio.py
"""
import difflib, json, re, subprocess, sys, wave
from pathlib import Path
import numpy as np
HERE = Path(__file__).parent
MODELS = Path("brutalist.art/runtime/models/kokoro")  # the toolkit checkout; adjust to where it lives
VOICE, SR = "am_onyx", 24000
GAP, LEAD, TAIL = 0.22, 0.15, 0.45
OVERRIDES = {"Mycroft": ("mˈɪkɹɔft", "mˈaɪkɹɔft")}
FRAGMENTS = ["Invented.", "Four out of four.", "Who had a vote?", "I fixed it.", "Adjourned.", "Nobody has made a mistake."]

SHEET = json.loads((HERE / "beat_sheet.json").read_text())["beats"]
HOLDS = {b["beat_id"]: b["hold_after_narration_s"] for b in SHEET}
def beats(): return [(b["beat_id"], b["narration_text"]) for b in SHEET]

def write_wav(path, x, sr):
    x = np.clip(x, -1, 1); 
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((x * 32767).astype("<i2").tobytes())

TTS_SPELL = {"What-If": "What if"}   # Kokoro merges the hyphenated form into 'wudif'; the text and captions keep the real spelling

def phon(tok, s):
    spoken_s = s
    for k, v in TTS_SPELL.items(): spoken_s = spoken_s.replace(k, v)
    ph = tok.phonemize(spoken_s, "en-us")
    for word, (wrong, right) in OVERRIDES.items():
        if word in s:
            assert wrong in ph, f"override for {word}: no '{wrong}' in {ph!r}"
            ph = ph.replace(wrong, right)
    return ph

def main():
    if "--phonemes" in sys.argv:
        from kokoro_onnx.tokenizer import Tokenizer
        tok = Tokenizer(); rows = []
        for bid, text in beats():
            for s in re.split(r"(?<=[.?!])\s+", text.strip()):
                rows.append((bid, s, tok.phonemize(s, "en-us"), phon(tok, s)))
        out = ["# PHONEMES-CHECK: Kokoro on every sentence (checked by make_audio.py --phonemes)", "",
               "Kokoro's own phonemes beside what is spoken after the one signed override (Mycroft → MY-croft). Read for words that sound wrong; `Fragments` are the short sentences Whisper is asked to confirm.", "",
               "| Beat | Sentence | Phonemes spoken |", "|---|---|---|"]
        out += [f"| {b} | {s.replace('|', '/')} | `{p}`{' (override applied)' if p != raw else ''} |" for b, s, raw, p in rows]
        (HERE / "PHONEMES-CHECK.md").write_text("\n".join(out) + "\n"); print(len(rows), "sentences written to PHONEMES-CHECK.md"); return
    if "--check-only" not in sys.argv:
        from kokoro_onnx import Kokoro
        from kokoro_onnx.tokenizer import Tokenizer
        kok = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin")); tok = Tokenizer()
        (HERE / "mp3").mkdir(exist_ok=True)
        timings = {}
        for bid, text in beats():
            # whole-beat synthesis: Kokoro paces a full paragraph naturally (about 3.5 words a second); sentence-by-sentence
            # synthesis reads each sentence in isolation and comes out about 30% slower ("slow motion"). Sentence times
            # for the captions come from the Whisper word clock afterwards.
            audio, sr = kok.create(phon(tok, text), voice=VOICE, speed=1.0, lang="en-us", is_phonemes=True)
            assert sr == SR
            a = np.asarray(audio, dtype=np.float64)
            narr_end = LEAD + len(a) / SR
            tail = TAIL + HOLDS.get(bid, 0.0)
            chunks = [np.zeros(int(LEAD * SR)), a, np.zeros(int(tail * SR))]; total = narr_end + tail
            sent_t = []
            raw = np.concatenate(chunks)
            raw_path = HERE / "mp3" / f"beat-{bid}.raw.wav"; write_wav(raw_path, raw, SR)
            out = HERE / "mp3" / f"beat-{bid}.wav"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw_path), "-af",
                            "loudnorm=I=-16:TP=-2:LRA=11", "-ar", "48000", "-ac", "1", str(out)], check=True)
            dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)],
                                       capture_output=True, text=True).stdout)
            timings[bid] = {"text": text, "sentences": sent_t, "narration_end_s": round(narr_end, 3),
                            "hold_s": HOLDS.get(bid, 0.0), "duration_s": round(dur, 3)}
            print(f"{bid}: {dur:6.2f} s  ({len(text.split())} words)", flush=True)
        (HERE / "mp3" / "timings.json").write_text(json.dumps(timings, indent=1))
        print(f"total {sum(t['duration_s'] for t in timings.values()):.1f} s")
    whisper_check()

ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def below1000(n, and_=True):
    if n < 20: return [ONES[n]]
    if n < 100: return [TENS[n // 10]] + ([ONES[n % 10]] if n % 10 else [])
    r = [ONES[n // 100], "hundred"]
    if n % 100: r += (["and"] if and_ else []) + below1000(n % 100)
    return r
def say_int(n):
    if n >= 1000:
        r = below1000(n // 1000, False) + ["thousand"]
        if n % 1000: r += below1000(n % 1000, n % 1000 >= 100)
        return r
    return below1000(n)
def spoken(tok):
    """digits -> words, the way the narration writes them (decimals as 'point', % as 'percent')."""
    pct = tok.endswith("%"); t = tok.rstrip("%.,?!").replace(",", "")
    if not re.fullmatch(r"\d+(\.\d+)?", t): return [tok]
    whole, _, dec = t.partition("."); out = say_int(int(whole))
    if dec: out += ["point"] + [ONES[int(c)] for c in dec]
    return out + (["percent"] if pct else [])
def norm(w): return re.sub(r"[^a-z0-9]", "", w.lower())
def heard_words(words):
    out = []
    for w, *_ in words:
        for x in spoken(w): 
            n = norm(x)
            if n: out.append(n)
    return out
def sentence_spans(text, words):
    """Sentence start/end on the Whisper clock: align the signed tokens to the heard tokens, take the first and last token of each sentence."""
    sents = re.split(r"(?<=[.?!])\s+", text.strip())
    ref, owner = [], []
    for si, s in enumerate(sents):
        for w in s.split():
            n = norm(w)
            if n: ref.append(n); owner.append(si)
    heard = []
    for w, s0, e0 in words:
        toks = [n for n in (norm(x) for x in spoken(w)) if n]
        for j, n in enumerate(toks):
            heard.append((n, s0 + (e0 - s0) * j / max(len(toks), 1), s0 + (e0 - s0) * (j + 1) / max(len(toks), 1)))
    sm = difflib.SequenceMatcher(None, ref, [h[0] for h in heard], autojunk=False)
    st = [None] * len(ref); en = [None] * len(ref)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): st[a + k], en[a + k] = heard[b + k][1], heard[b + k][2]
    out = []
    for si, s in enumerate(sents):
        idx = [i for i, o in enumerate(owner) if o == si and st[i] is not None]
        if idx: out.append({"text": s, "start": round(st[idx[0]], 3), "end": round(en[idx[-1]], 3)})
        else: out.append({"text": s, "start": out[-1]["end"] if out else 0.0, "end": (out[-1]["end"] if out else 0.0) + 1.0})
    return out

def whisper_check():
    from faster_whisper import WhisperModel
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    timings = json.loads((HERE / "mp3" / "timings.json").read_text()); report = []
    for bid, t in timings.items():
        segs, _ = model.transcribe(str(HERE / "mp3" / f"beat-{bid}.raw.wav"), word_timestamps=True, language="en")
        words = [(w.word.strip(), round(w.start, 3), round(w.end, 3)) for s in segs for w in s.words]
        t["words"] = words
        t["sentences"] = sentence_spans(t["text"], words)
        heard = heard_words(words)
        ref = [norm(w) for w in t["text"].split() if norm(w)]
        ratio = difflib.SequenceMatcher(None, ref, heard).ratio()
        report.append((ratio, bid, [w for w in difflib.unified_diff(ref, heard, lineterm="", n=0) if w[:1] in "+-" and w[:3] not in ("+++", "---")][:10]))
    (HERE / "mp3" / "timings.json").write_text(json.dumps(timings, indent=1))
    print("\nWHISPER (small.en), worst first (word-sequence match vs the signed text):")
    for ratio, bid, d in sorted(report): print(f"  {bid}: {ratio:.3f}  {d}")
    print("\nFRAGMENTS (Whisper's transcript of each short sentence's own audio window):")
    for bid, t in timings.items():
        for s in t["sentences"]:
            if s["text"] in FRAGMENTS:
                got = " ".join(w[0] for w in t["words"] if s["start"] - 0.1 <= w[1] <= s["end"] + 0.1)
                ok = [norm(x) for x in s["text"].split()] == [n for n in (norm(x) for x in got.split()) if n]
                print(f"  {bid} {s['text']!r}: heard {got!r} {'OK' if ok else 'CHECK'}")

if __name__ == "__main__":
    main()
