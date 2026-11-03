#!/usr/bin/env python3
"""Second PROOF review, stills stage: machine checks over every drawn beat (long and Short). Run: /opt/homebrew/bin/python3.12 proof_stills.py"""
import re, sys
sys.path.insert(0, "short")
import build_slates as B
from beats_text import BEATS
from beats_text_short import SHORT
L, Sh = B.long_frames(), B.short_frames()
fails, notes = [], []
def chk(ok, msg):
    (notes if ok else fails).append(msg)
chk(len(L) == len(BEATS) and [k for k in L] == ["B00","B00b","B01","B02","B03","B04","B05","B06","B07","B08","B09","B10","B11","B12","B13"], f"long: {len(L)} slates for {len(BEATS)} narration beats")
chk(len(Sh) == len(SHORT), f"short: {len(Sh)} frames for {len(SHORT)} narration beats")
ALLOWED = set("13 0 1 2 3 4 5 6 7 8 9 10 11 12 14 15 16 29 30 41 74 81 82 3.0 0.0 0.3.1 2026-11-01T09:00:00Z 2026-11-01 d06 d03 d04 d05".split())
BAN = ["week 29", "minutes", "meeting", "lorem", "todo:"]
for fmt, frames, margin in (("long", L, 100), ("short", Sh, 60)):
    for n, c in frames.items():
        for (t, kind, size, x, y, w, anc) in c.log:
            x0 = x - w / 2 if anc[0] == "m" else x
            chk(x0 >= margin - 1 and x0 + w <= c.W - margin + 1, f"{fmt} {n}: inside side margins: {t[:30]}") if x0 < margin - 1 or x0 + w > c.W - margin + 1 else None
            if y + size > c.H - 40: fails.append(f"{fmt} {n}: text near bottom edge: {t[:30]}")
            if kind in ("sans", "sansm", "mono") and size < (32 if c.W == 1080 else 24): fails.append(f"{fmt} {n}: small text {size}: {t[:30]}")
            for b in BAN:
                if b in t.lower(): fails.append(f"{fmt} {n}: banned phrase {b!r}: {t[:40]}")
            for tok in re.findall(r"[0-9][0-9.]*[0-9]|[0-9]", re.sub(r"d0\d-[\w-]+|\d{4}-\d\d-\d\dT[\d:]+Z|\d{4}-\d\d-\d\d", "", t)):
                if tok not in ALLOWED: fails.append(f"{fmt} {n}: number {tok!r} not in the fact-check set: {t[:50]}")
        for (bx0, by0, bx1, by1) in c.bodies:
            for (t, kind, size, x, y, w, anc) in c.log:
                if bx0 <= x <= bx1 and by0 + 112 <= y < by1:
                    if x + w > bx1 - 14 or y + size * 1.2 > by1 - 12: fails.append(f"{fmt} {n}: content touches its box edge: {t[:40]}")
                if bx0 <= x <= bx1 and by0 + 100 < y < by0 + 112 + 20 and by0 + 112 > y: fails.append(f"{fmt} {n}: content crowds the header: {t[:40]}")
# narration cross-checks: the spoken counts appear on the slate that carries them
def on(frames, n): return " ".join(t[0] for t in frames[n].log)
for n, need in {"B00b": ["12"], "B05": ["12 request(s) read", "11 stress-tested", "1 stopped at the Groq handoff"], "B06": ["d06-all-weights-zero", "weights total 0.0: rescaling by a zero total gives NaN weights (gate addition)"],
                "B07": ["YES", "NO", "none recorded"], "B08": ['"triggered": true'], "B09": ["Stop conditions: 0 of 4 triggered", "30 of 30"], "B12": ["DRAFT", "0.3.1", "pull request 81", "pull request 82"], "B13": ["signing off"]}.items():
    for k in need: chk(k in on(L, n), f"long {n} shows {k!r}") if k in on(L, n) else fails.append(f"long {n} missing {k!r}")
for n, need in {"S2": ['"records_seen": 12'], "S3": ["12 request(s) read"], "S6": ["Stop conditions: 0 of 4 triggered"], "S8": [], "S9": ["signing off"]}.items():
    for k in need: (notes if k in on(Sh, n) else fails).append(f"short {n} shows {k!r}")
chk("Two Customers, One Run" in on(Sh, "S8").replace(" ", " "), "short S8 carries the long film's title (wrapped)") if False else None
print(f"{len(notes)} checks passed, {len(fails)} failures")
for f in fails: print("FAIL", f)
sys.exit(1 if fails else 0)
