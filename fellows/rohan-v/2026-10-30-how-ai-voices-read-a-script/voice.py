"""What our narrator actually does with a script: the text-to-phoneme step, tested.

    python voice.py            # writes evidence/run.log, evidence/results.json, evidence WAVs

Our narrator is Kokoro-82M through kokoro-onnx, whose G2P (grapheme-to-phoneme) step is espeak-ng. The toolkit
exposes that step as `generate_audio_kokoro.phonemize()`, the same function the narration uses. Three tests:

  1. heteronyms   — 8 English words spelled the same but said two ways (read/read, lead/lead, live/live,
                    record/record, close/close, wind/wind, tears/tears, present/present), each in a sentence that
                    fixes its meaning. Right = the sentence's IPA contains the expected pronunciation.
  2. normalising  — numbers, money, times, abbreviations: what words the G2P turns them into.
  3. respelling   — words our own narrator got wrong in earlier videos, and the respelling that fixed them.

Audio clips (Kokoro, af_bella) of the interesting cases are written to evidence/, and each is transcribed by
faster-whisper (the base model our alignment step uses, run offline) to check what the voice really said.
"""
import json
import os
import sys
import wave
from pathlib import Path

import numpy as np

TOOLKIT = Path("D:/Rohan/Claude/HAI/RohanClaudeHAIbrutalist.art")
sys.path.insert(0, str(TOOLKIT / "runtime" / "scripts"))
os.environ.setdefault("HF_HUB_OFFLINE", "1")
from generate_audio_kokoro import phonemize, load_engine  # noqa: E402

HERE = Path(__file__).resolve().parent
EV = HERE / "evidence"
VOICE = "af_bella"

HETERONYMS = [  # word, (sentence, meaning, expected IPA) x 2
    ("read", ("I read a book every night.", "now", "ɹˈiːd"), ("Last night I read a book.", "past", "ɹˈɛd")),
    ("lead", ("Lead the way.", "guide", "lˈiːd"), ("The pipe is made of lead.", "metal", "lˈɛd")),
    ("live", ("I live in Boston.", "reside", "lˈɪv"), ("We saw a live show.", "in person", "lˈaɪv")),
    ("record", ("Please record the song.", "verb", "ɹɪkˈɔːɹd"), ("She bought a record.", "noun", "ɹˈɛkɚd")),
    ("close", ("Close the door.", "shut", "klˈoʊz"), ("They are close friends.", "near", "klˈoʊs")),
    ("wind", ("Wind the clock.", "turn", "wˈaɪnd"), ("The wind is cold.", "air", "wˈɪnd")),
    ("tears", ("Tears ran down her face.", "crying", "tˈɪɹz"), ("He tears the paper.", "rips", "tˈɛɹz")),
    ("present", ("Present the award.", "verb", "pɹɪzˈɛnt"), ("It was a birthday present.", "gift", "pɹˈɛzənt")),
]
NORMALISE = [  # text, what a person would say
    ("Dr. Smith", "doctor smith"), ("Main St.", "main street"), ("1,024 bytes", "one thousand twenty-four bytes"),
    ("in 2026", "in twenty twenty-six"), ("at 10:30", "at ten thirty"), ("the 5th of May", "the fifth of may"),
    ("It costs $3.50.", "it costs three dollars fifty"),
]
EXAMPLES = ["book", "night", "phoneme", "Boston"]   # B02's letters-to-sounds examples
RESPELL = [  # word, our respelling, where it came from
    ("Rohan", "Row-Haan", "the presenter's own name, every video"),
    ("dhol", "dhole", "week-08 progress video"),
    ("sitar", "sitaar", "week-08 progress video"),
    ("tabla", "tubla", "week-08 progress video"),
]


def write_wav(path, y, sr):
    pcm = (np.clip(y / (np.abs(y).max() + 1e-9) * 0.9, -1, 1) * 32767).astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm.tobytes())


def main():
    EV.mkdir(exist_ok=True)
    log = []
    P = lambda *a: (log.append(" ".join(str(x) for x in a)), print(*a))
    het = []
    for word, a, b in HETERONYMS:
        row = dict(word=word, forms=[])
        for sent, meaning, exp in (a, b):
            ipa = phonemize(sent)
            row["forms"].append(dict(sentence=sent, meaning=meaning, expected=exp, ipa=ipa, right=exp in ipa))
        same = row["forms"][0]["ipa"].count(row["forms"][1]["expected"]) == 0 and not all(f["right"] for f in row["forms"])
        row["both_right"] = all(f["right"] for f in row["forms"])
        het.append(row)
    n_right = sum(f["right"] for r in het for f in r["forms"])
    both = sum(r["both_right"] for r in het)
    P(f"HETERONYMS: {n_right} of {2 * len(het)} sentences got the right pronunciation; both meanings right for {both} of {len(het)} words")
    for r in het:
        P(f"  {r['word']:8s} " + " | ".join(f"{f['meaning']}: {'right' if f['right'] else 'WRONG'} ({f['ipa']})" for f in r["forms"]))

    norm = []
    for text, said in NORMALISE:
        norm.append(dict(text=text, should=said, ipa=phonemize(text)))
    P("")
    P("NORMALISING (text -> phonemes):")
    for n in norm:
        P(f"  {n['text']:18s} -> {n['ipa']}")

    examples = [dict(word=w, ipa=phonemize(w)) for w in EXAMPLES]
    P("")
    P("EXAMPLES: " + "; ".join(f"{e['word']} -> {e['ipa']}" for e in examples))
    resp = []
    for w, fix, where in RESPELL:
        resp.append(dict(word=w, fix=fix, where=where, ipa=phonemize(w), ipa_fix=phonemize(fix)))
    P("")
    P("RESPELLING (our narrator's real mistakes):")
    for r in resp:
        P(f"  {r['word']:6s} {r['ipa']:12s} -> {r['fix']:9s} {r['ipa_fix']}   ({r['where']})")

    # audio, and what a speech recogniser hears in it
    k = load_engine()
    from faster_whisper import WhisperModel
    asr = WhisperModel("base", device="cpu", compute_type="int8")
    clips = [("read_past", "Last night I read a book."), ("price", "It costs $3.50."),
             ("name_default", "Hi, I am Rohan."), ("name_fixed", "Hi, I am Row-Haan.")]
    heard = {}
    P("")
    P("AUDIO CHECK (Kokoro af_bella -> faster-whisper base):")
    for key, text in clips:
        y, sr = k.create(text, voice=VOICE, speed=1.0, lang="en-us")
        write_wav(EV / f"{key}.wav", np.asarray(y, dtype=np.float32), sr)
        segs, _ = asr.transcribe(str(EV / f"{key}.wav"), language="en")
        t = " ".join(s.text.strip() for s in segs)
        heard[key] = dict(text=text, heard=t, seconds=round(len(y) / sr, 2))
        P(f"  {key:13s} '{text}' -> heard '{t}'")

    (EV / "run.log").write_text("\n".join(log) + "\n", encoding="utf-8")
    (EV / "results.json").write_text(json.dumps(dict(heteronyms=het, heteronym_right=n_right, heteronym_both=both,
                                                     normalise=norm, respell=resp, heard=heard, examples=examples), ensure_ascii=False,
                                                indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
