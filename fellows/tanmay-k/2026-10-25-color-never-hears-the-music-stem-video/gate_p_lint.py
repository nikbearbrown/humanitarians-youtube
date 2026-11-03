#!/usr/bin/env python3
"""Gate P mechanical pass for Week 28 (adapted from Week 26's gate_p_lint.py).

**This is NOT Gate P.** Gate P is a human reading every line aloud and signing off. This script
clears the subset a machine can see on the page, so the human read is spent on judgement (rhythm,
emphasis, whether the limit lands) rather than on spotting a homophone.

Reads the two read-aloud sheets (long film and Short), which are generated from the scripts.
Flags: HOMOPHONE, MARKUP, SYMBOL, DIGIT-CHAIN, BREATH, SHORT-SENTENCE (Kokoro merges/mangles
sentences under five words), ECHO, ACRONYM, LONE-LETTER, NAME (an ear checklist, not defects).
With --phonemes (needs homebrew python3.12 + kokoro_onnx) it also prints what Kokoro's own
tokenizer will say for each NAME phrase. No audio is generated.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHEETS = {"long": HERE / "READ-ALOUD.md", "short": HERE / "short" / "READ-ALOUD-SHORT.md"}

MAX_SENTENCE_WORDS = 28
MAX_DIGIT_CHAIN = 6
NUMBER_WORDS = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
                "hundred", "thousand", "point"}
HOMOPHONES = {
    "weak": "heard as 'week'. Fine beside 'strong' ('strong or weak'); check by ear.",
    "weight": "heard as 'wait'.",
    "too": "heard as 'two' beside a number.",
    "sine": "heard as 'sign'.",
    "principle": "heard as 'principal'.",
    "grey": "fine; US 'gray' is the repo's usual spelling in on-screen text. Voice is identical.",
    "minor": "heard as 'miner' only if a mining context; none here.",
}
SYMBOLS = re.compile(r"[σπħλ°²³⁺⁻₀→×≈≤≥∞±]")
MARKUP = re.compile(r"\*+|`+|_[A-Za-z]|\[[^\]]*\]|\|\||#{1,6}\s")
ACRONYM = re.compile(r"\b(?:[A-Z]{2,}(?:-[A-Z0-9]+)?|[A-Z]{1,3}[0-9]+[A-Za-z]*)\b")
ACRONYM_OK = {"AI"}
LONE_LETTER = re.compile(r"(?<![A-Za-z0-9'’-])([A-HJ-SU-Za-hj-su-z])(?![A-Za-z0-9'’-])")
NAMES = {
    "tanmay kulkarni": "TUN-may kul-KAR-nee (signed string `kul-KAR-nee`, as Week 26/27)",
    "humanitarians ai": "hyoo-MAN-ih-TAIR-ee-unz A-I",
    "stephen palmer": "STEE-ven PAH-mer",
    "berkeley": "BURK-lee",
    "guadalajara": "gwah-dah-lah-HAH-rah",
    "bach": "BAHKH (Kokoro often says BAHK)",
    "mozart": "MOHT-sart",
    "brahms": "BRAHMZ",
    "adagio": "ah-DAH-jee-oh",
    "angeline lillard": "AN-juh-leen LIL-ard",
    "jennifer peterson": "plain",
    "f major": "eff MAY-jer",
    "c minor": "see MY-ner",
    "saturated": "SACH-uh-ray-ted",
    "ninety seven": "plain; check not heard as 'ninety-heaven'",
}


def lines_of(path):
    out = []
    txt = path.read_text()
    for m in re.finditer(r"\*\*([BS]\d\d) · ([^*]*?)\*\*[^\n]*\n\n(.*?)\n", txt):
        out.append((m.group(1), m.group(3)))
    return out


def main():
    phon = "--phonemes" in sys.argv
    flags = 0
    seen_names = {}
    for fmt, path in SHEETS.items():
        beats = lines_of(path)
        print(f"\n=== {fmt.upper()}: {len(beats)} lines, {sum(len(t.split()) for _, t in beats)} words ===")
        openers = {}
        for bid, text in beats:
            def flag(kind, msg):
                nonlocal_flags.append((fmt, bid, kind, msg))
            nonlocal_flags = []
            sents = [s for s in re.split(r"(?<=[.?!])\s+", text) if s]
            for s in sents:
                w = s.split()
                if len(w) < 5:
                    flag("SHORT-SENTENCE", f"{len(w)} words: {s!r}")
                if len(w) > MAX_SENTENCE_WORDS:
                    flag("BREATH", f"{len(w)} words: {s[:60]}…")
            lw = re.findall(r"[A-Za-z']+", text.lower())
            for h, why in HOMOPHONES.items():
                if h in lw:
                    flag("HOMOPHONE", f"{h}: {why}")
            if SYMBOLS.search(text):
                flag("SYMBOL", "unicode symbol in narration")
            if MARKUP.search(text):
                flag("MARKUP", "markdown in narration")
            for a in ACRONYM.findall(text):
                if a not in ACRONYM_OK:
                    flag("ACRONYM", a)
            for m in LONE_LETTER.finditer(text):
                if m.group(1) in ("a", "A"):
                    continue
                flag("LONE-LETTER", f"{m.group(1)!r} in …{text[max(0, m.start()-12):m.end()+10]}…")
            run = best = 0
            for w in lw:
                run = run + 1 if w in NUMBER_WORDS else 0
                best = max(best, run)
            if best > MAX_DIGIT_CHAIN:
                flag("DIGIT-CHAIN", f"{best} number words in a row")
            low = text.lower()
            for n, how in NAMES.items():
                if n in low:
                    seen_names.setdefault(n, (how, []))[1].append(f"{fmt}:{bid}")
            first = " ".join(sents[0].split()[:3]).lower() if sents else ""
            openers.setdefault(first, []).append(bid)
            for _fmt, b, k, m in nonlocal_flags:
                print(f"  {b} {k:15s} {m}")
                flags += 1
        for o, ids in openers.items():
            if len(ids) > 2:
                print(f"  ECHO            opener '{o}' x{len(ids)}: {ids}")
    print("\n=== NAMES: checklist for the ear (not defects) ===")
    for n, (how, where) in sorted(seen_names.items()):
        print(f"  {n:20s} {how}   [{', '.join(where)}]")
    print(f"\n{flags} mechanical flags (SHORT-SENTENCE/HOMOPHONE/LONE-LETTER need a human decision).")
    if phon:
        from kokoro_onnx.tokenizer import Tokenizer
        tok = Tokenizer()
        print("\n=== Kokoro phonemes (en-us), no audio ===")
        for n in sorted(seen_names):
            print(f"  {n:20s} {tok.phonemize(n, lang='en-us')}")
        for extra in ["Berkeley", "Guadalajara", "Adagio", "Brahms", "Mozart", "Bach", "Palmer",
                      "Lillard", "ninety seven", "saturated", "yellower", "Bach's fast dance in F major",
                      "Adagio in C minor", "point nine seven", "thirty seven"]:
            print(f"  {extra:30s} {tok.phonemize(extra, lang='en-us')}")


if __name__ == "__main__":
    main()
