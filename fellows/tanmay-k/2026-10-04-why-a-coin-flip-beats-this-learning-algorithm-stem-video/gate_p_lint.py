#!/usr/bin/env python3
"""Gate P mechanical pass (copied from Week 24; NAMES and UNITS replaced for Week 25) — the read-aloud failures catchable on the page.

**This is NOT Gate P.** Gate P is a human reading every line out loud against an animated
slate and signing off (source README, step 4; PROOF: "Claude cannot judge whether the
finished film works for an audience"). This script clears the subset a machine can see, so
the human read is spent on judgement — rhythm, emphasis, whether the retraction lands —
rather than on spotting a homophone.

Flags, in rough order of how badly they hurt:

    HOMOPHONE     a word that collides with a different word when heard. "nought" -> "not"
                  is fatal in a beat about a p-value threshold.
    MARKUP        markdown that survived into narration. Kokoro will voice or swallow it.
    SYMBOL        unicode that a TTS engine will read literally or drop silently.
    UNIT-DROP     a bare "thirty-eight point seven" with no percent/months within a few
                  words. THIS FILM'S SIGNATURE HAZARD: the same digits mean two different
                  quantities, and in the ear the unit is the only thing telling them apart.
    DIGIT-CHAIN   long runs of number-words. Fine on a page, mush in the ear.
    BREATH        a sentence too long to say in one pass.
    ECHO          the same sentence-opener twice running, or leaned on across the film.
    ACRONYM       a letter-string TTS may spell, mispronounce, or run together.
    NAME          a proper noun or drug name a TTS engine routinely mangles. Monoclonal
                  antibody names are the worst offenders in this film — "-umab" is not a
                  string English orthography prepares a voice engine for.
    LONE-LETTER   a bare single letter that may be voiced as a word or a digit.

Usage:  python3 gate_p_lint.py [--strict]   # --strict exits 1 on any flag
"""

import argparse
import collections
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BEATS = HERE / "beat_sheet.json"

MAX_SENTENCE_WORDS = 28
MAX_DIGIT_CHAIN = 6
UNIT_WINDOW = 4          # words after a decimal in which its unit must appear

NUMBER_WORDS = {
    "zero", "oh", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
    "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
    "eighty", "ninety", "hundred", "thousand", "million", "point", "minus", "and",
}
CHAIN_GLUE = {"and", "point", "minus", "oh"}

HOMOPHONES = {
    "weigh": "heard as 'way'.",
    "weight": "heard as 'wait' (Whisper heard 'let's wait the coin', W25). Use 'bias'.",
    "weighting": "heard as 'waiting' (W25). Use 'setting' / 'bias'.",
    "weighted": "heard as 'waited' unless 'coin' follows at once (W25).",
    "too": "heard as 'two' beside a number ('the book's number too', W25).",
    "mint": "fine alone, but check it isn't heard as 'meant'.",
    "nought": "heard as 'not'. Fatal in a p-value sentence. Use 'zero'.",
    "aught": "heard as 'ought'. Use 'zero'.",
    "sine": "heard as 'sign'.",
    "discrete": "heard as 'discreet'.",
    "principle": "heard as 'principal'.",
}

# Units that can follow a spoken decimal in this film. A decimal with none of these nearby
# is ambiguous by construction — see C23 in FACTCHECK.md.
UNITS = {"percent", "steps", "step", "points", "times", "round", "rounds", "right"}

# Em/en dashes are deliberate pause marks in this register and Kokoro handles them.
SYMBOLS = re.compile(r"[σπħλ°²³⁺⁻₀→×≈≤≥∞±]")
MARKUP = re.compile(r"\*+|`+|_[A-Za-z]|\[[^\]]*\]|\|\||#{1,6}\s")
ACRONYM = re.compile(r"\b(?:[A-Z]{2,}(?:-[A-Z0-9]+)?|[A-Z]{1,3}[0-9]+[A-Za-z]*)\b")
ACRONYM_OK = {"AI", "REINFORCE"}   # REINFORCE: algorithm name, phonemized as a word   # spoken deliberately and unambiguously
LONE_LETTER = re.compile(r"(?<![A-Za-z0-9'’-])([A-HJ-SU-Za-hj-su-z])(?![A-Za-z0-9'’-])")
LONE_LETTER_OK = {"a", "A", "I"}

# Proper nouns and drug names in this film that must be confirmed by ear. Not defects — a
# checklist, because Kokoro has no reason to know how any of these are said.
NAMES = {
    # Week 25 — corridor film. Checklist for the ear, not defects.
    "sutton": "SUT-n",
    "barto": "BAR-toe",
    "sarsa": "SAR-suh (Kokoro: sˈɑːɹsə, checked)",
    "reinforce": "ree-in-FORCE, the algorithm's name, said like the word",
    "kulkarni": "kul-KAR-nee",
    "irrational": "ih-RASH-uh-nul (the maths sense)",
}


def sentences(text):
    return [s.strip() for s in re.findall(r"[^.?!]+[.?!]+|[^.?!]+$", text) if s.strip()]


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z\-']*", text)


def digit_chains(text):
    """Runs of number-words WITHIN a sentence. A full stop is a breath; a chain that
    'crosses' one is not a chain the ear has to hold."""
    return [c for s in sentences(text) for c in _chains_in(s)]


def _chains_in(text):
    out, run = [], []
    for w in words(text):
        head = w.split("-")[0].lower()
        parts = [p.lower() for p in w.split("-")]
        if all(p in NUMBER_WORDS for p in parts) or head in NUMBER_WORDS:
            run.extend(parts)
        else:
            if len(run) > MAX_DIGIT_CHAIN and not all(r in CHAIN_GLUE for r in run):
                out.append(run)
            run = []
    if len(run) > MAX_DIGIT_CHAIN:
        out.append(run)
    return out


def unit_drops(text):
    """A spoken decimal whose unit does not arrive within UNIT_WINDOW words."""
    toks = words(text)
    low = [t.lower() for t in toks]
    hits = []
    # "a point for", "the whole point", "half a percentage point", "point at the chart" —
    # none of these are decimals. Only flag "point" sitting between number-words.
    noun_before = {"a", "the", "whole", "percentage", "one", "this", "that", "his", "her"}
    verb_after = {"at", "for", "of", "in", "to", "out", "towards", "toward"}
    # Genuinely dimensionless quantities. A correlation or a p-value has no unit to drop,
    # so demanding one would train the reader to ignore this check.
    unitless_ctx = {"correlation", "p-value", "pvalue", "squared", "r", "coefficient",
                    "probability"}
    for i, t in enumerate(low):
        if t != "point":
            continue
        prev = low[i - 1] if i else ""
        nxt = low[i + 1] if i + 1 < len(low) else ""
        if prev in noun_before and prev not in NUMBER_WORDS - {"one"}:
            continue
        if nxt in verb_after:
            continue
        window = set(low[max(0, i - 6): i + UNIT_WINDOW + 2])
        if window & unitless_ctx:
            continue
        tail = low[i + 1: i + 1 + UNIT_WINDOW + 1]
        if not any(u in tail for u in UNITS):
            start = max(0, i - 3)
            hits.append(" ".join(toks[start: i + UNIT_WINDOW + 1]))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 1 on any flag")
    args = ap.parse_args()

    beats = json.loads(BEATS.read_text())["beats"]
    flags = []
    openers = collections.Counter()
    prev_opener = None

    def flag(kind, bid, detail):
        flags.append((kind, bid, detail))

    for b in beats:
        bid, text = b["beat_id"], b["narration_text"]

        for w in words(text):
            if w.lower() in HOMOPHONES:
                flag("HOMOPHONE", bid, f"'{w}' — {HOMOPHONES[w.lower()]}")

        for m in MARKUP.finditer(text):
            ctx = text[max(0, m.start() - 25): m.end() + 25]
            flag("MARKUP", bid, f"{m.group(0)!r} in ...{ctx}...")

        for m in SYMBOLS.finditer(text):
            ctx = text[max(0, m.start() - 25): m.end() + 25]
            flag("SYMBOL", bid, f"{m.group(0)!r} in ...{ctx}...")

        for chain in digit_chains(text):
            flag("DIGIT-CHAIN", bid, f"{len(chain)} number-words: {' '.join(chain)}")

        for hit in unit_drops(text):
            flag("UNIT-DROP", bid, f"no unit within {UNIT_WINDOW} words: ...{hit}...")

        for s in sentences(text):
            n = len(s.split())
            if n > MAX_SENTENCE_WORDS:
                flag("BREATH", bid, f"{n} words: {s[:90]}...")
            first = (words(s) or ["?"])[0].lower()
            openers[first] += 1
            if first == prev_opener and first not in {"it", "the"}:
                flag("ECHO", bid, f"two sentences running open with '{first}'")
            prev_opener = first

        for m in ACRONYM.finditer(text):
            if m.group(0) not in ACRONYM_OK:
                flag("ACRONYM", bid, f"'{m.group(0)}' — confirm TTS pronunciation")

        seen_names = set()
        for w in words(text):
            key = w.lower().strip("-'")
            if key in NAMES and key not in seen_names:
                seen_names.add(key)
                flag("NAME", bid, f"'{w}' -> {NAMES[key]}")

        for m in LONE_LETTER.finditer(text):
            if m.group(1) not in LONE_LETTER_OK:
                ctx = text[max(0, m.start() - 20): m.end() + 20]
                flag("LONE-LETTER", bid, f"'{m.group(1)}' in ...{ctx}...")

    # Cross-film opener frequency is context, not a defect: "the"/"and" leading English
    # prose is normal. Reported below the flags, not counted as one.
    total_sentences = sum(openers.values())

    by_kind = collections.Counter(k for k, _, _ in flags)
    order = ["HOMOPHONE", "MARKUP", "SYMBOL", "UNIT-DROP", "DIGIT-CHAIN",
             "BREATH", "ECHO", "ACRONYM", "NAME", "LONE-LETTER"]
    for kind in order:
        rows = [(b, d) for k, b, d in flags if k == kind]
        if not rows:
            continue
        print(f"\n{kind}  ({len(rows)})")
        for bid, detail in rows:
            print(f"  {bid:5s} {detail}")

    top = [f"{o} {n} ({n / total_sentences:.0%})" for o, n in openers.most_common(4)]
    print(f"\nsentence openers (context, not flags): {', '.join(top)}"
          f" of {total_sentences} sentences")

    total_words = sum(len(b["narration_text"].split()) for b in beats)
    print(f"\n{len(beats)} beats · {total_words} narration words · {len(flags)} flags "
          f"({', '.join(f'{k}:{v}' for k, v in by_kind.most_common()) or 'none'})")
    print("\nThis is the mechanical pass only. Gate P is the human read-aloud.")
    return 1 if (args.strict and flags) else 0


if __name__ == "__main__":
    sys.exit(main())
