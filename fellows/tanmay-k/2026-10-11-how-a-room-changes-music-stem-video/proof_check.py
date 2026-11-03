#!/usr/bin/env python3
"""PROOF production gate, the statically checkable half, over beat_sheet.json.

1. SOURCE   every beat citing an A-row (external fact) has a non-empty on-screen source line
2. QUOTE    every phrase the narration presents as someone's words is printed on screen, same beat
3. NUMBER   every figure the narration states is printed on screen, same beat (spoken -> digits)
4. TIMING   a reveal prop (statAt, answersAt, drySideAt) lands no later than its spoken claim
5. LENGTH   on-screen lines over 90 characters (9:16 legibility risk, eyes-only follow-up)

Run after build_beat_sheet.py. Exit code 1 on any SOURCE/QUOTE/NUMBER/TIMING failure.
Rendered frames are still owed: this checks intent, not pixels (BEATS.md, governing observation).
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
SHEET = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "beat_sheet.json"   # short/beat_sheet.json for the Short
sheet = json.loads(SHEET.read_text())

# Phrases the narration attributes to a person or paper, keyed by beat
QUOTES = {
    "B05": ["would just turn into mush in a Gothic cathedral"],
    "B06": ["didn't sound all that great"],
    "B11": ["very individual"],
    "B16": ["adapting yourself to your environment whether you're aware of it or not"],
}
# Spoken figure -> the digits that must be on screen in the same beat
NUMBERS = {
    "B07": [("seventeen fifty-two", "1752")],
    "B09": [("seventy-four percent", "74")],
    "B11": [("nine percent", "8.73"), ("Twelve musicians", "Twelve"), ("fourteen", "fourteen")],
    "B12": [("Cleveland", "Cleveland")],
    "B13": [],
    "B14": [("two thousand three", "2003")],
    "B15": [("nineteen twenty-five", "1925"), ("seventy-eight", "78"), ("three minutes", "three minutes")],
    "B16": [("three hundred and three", "303"), ("nineteen eighty-six", "1986"),
            ("two thousand fifteen", "2015"), ("twenty seconds", "20"), ("about five", "5")],
    "B17": [],
}
# the Short (its own beat ids)
QUOTES.update({"S02": ["music is made to fit the place it will be heard"]})
NUMBERS.update({
    "S04": [("two thousand fifteen", "2015"), ("seven European", "seven"), ("seventeen fifty-two", "1752")],
    "S05": [("seventy-four percent", "74")],
    "S11": [("twelve more musicians", "twelve more musicians")],
})
TIMED = ("statAt", "answersAt", "drySideAt", "captionAt", "activeAt")


def strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            if k not in ("ir", "envelopeFrom"):
                yield from strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from strings(v)


def norm(s):
    return s.replace("’", "'").replace("“", "").replace("”", "").lower()


fails, warns, rows = [], [], []
for b in sheet["beats"]:
    bid, text = b["beat_id"], b["narration_text"]
    props = b["shot"].get("remotion", {}).get("props", {})
    screen = norm(" | ".join(strings(props)))
    refs = [r.split()[-1] for r in (b.get("factcheck_ref") or [])]
    src = props.get("source") or props.get("sparkLine") or ""
    status = []
    if any(r.startswith("A") for r in refs):
        if src.strip():
            status.append("source ✓")
        else:
            fails.append(f"{bid} SOURCE: cites {refs} but no on-screen source")
    for q in QUOTES.get(bid, []):
        if norm(q) in screen:
            status.append("quote ✓")
        else:
            fails.append(f"{bid} QUOTE: '{q}' spoken as a quote, not on screen")
    for spoken, digits in NUMBERS.get(bid, []):
        assert spoken.lower() in text.lower(), f"{bid}: NUMBERS table drifted from narration ({spoken})"
        if norm(digits) in screen:
            status.append(f"{digits} ✓")
        else:
            fails.append(f"{bid} NUMBER: '{spoken}' spoken, '{digits}' not on screen")
    est = b["estimated_duration_s"]
    for k in TIMED:
        v = props.get(k)
        if isinstance(v, (int, float)) and v > est:
            fails.append(f"{bid} TIMING: {k}={v}s is past the beat's estimated end ({est}s)")
    for s in strings(props):
        if len(s) > 90 and s != props.get("source") and s != props.get("sparkLine"):
            warns.append(f"{bid} LENGTH {len(s)} chars: {s[:70]}…")
    rows.append((bid, b["act"], ", ".join(status) or "no external claim"))

for bid, act, st in rows:
    print(f"  {bid:4} {act:24} {st}")
print(f"\nFAIL ({len(fails)})")
for f in fails:
    print("  " + f)
print(f"WARN ({len(warns)})")
for w in warns:
    print("  " + w)
sys.exit(1 if fails else 0)
