#!/usr/bin/env python3
"""make_captions.py: SRT + VTT for the long film from the measured audio (mp3/timings.json, the Whisper word clock).

    /opt/homebrew/bin/python3.12 make_captions.py            # writes the-rally-has-a-clock.srt / .vtt
    /opt/homebrew/bin/python3.12 make_captions.py --check short/the-rally-has-a-clock-short.srt   # validate any SRT

TIMING. Each narration token is aligned to the Whisper words of its beat (difflib on normalised tokens, digits spoken
as words), so a cue starts on the word that opens it. Beat starts on the master are the cumulative beat durations
(the master is the plain concatenation of the beats), so there is no drift.

TEXT. Captions show the WRITTEN form of figures the voice says in words ("ninety seven" -> "97", "twenty thirteen" ->
"2013", "point nine seven" -> ".97"). DISPLAY maps phrases whole, after the cue is chosen, so a mapped phrase is never
split across two cues. Cues break only at sentence ends, then at a clause mark (, : ;), then at a real pause.

RULES (carried from Week 26): <= 2 lines of <= 42 characters; a cue never spans a pause longer than 0.35 s; a cue
shorter than 1.2 s merges into its predecessor when they are adjacent; no captions in the tune clips and answer holds.
"""
import difflib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAX_CHARS, MAX_LINES, MIN_DUR, MAX_DUR, PAUSE_BREAK = 42, 2, 1.2, 6.0, 0.35

def norm(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())


import sys as _sys
_sys.path.insert(0, str(HERE)); _sys.path.insert(0, str(HERE / "short"))
from make_audio import spoken


def _heard(words):
    out = []
    for w, s0, e0 in words:
        toks = [n for n in (norm(x) for x in spoken(w)) if n]
        for j, n in enumerate(toks):
            out.append((n, s0 + (e0 - s0) * j / max(len(toks), 1), s0 + (e0 - s0) * (j + 1) / max(len(toks), 1)))
    return out


def _align(text, words):
    """signed tokens -> (start, end) on the Whisper clock (difflib on normalised tokens; digits spoken as words)."""
    ref = [norm(w) for w in text.split()]; keep = [i for i, r in enumerate(ref) if r]
    rr = [ref[i] for i in keep]; heard = _heard(words)
    sm = difflib.SequenceMatcher(None, rr, [h[0] for h in heard], autojunk=False); st = {}
    for a_, b_, n in sm.get_matching_blocks():
        for k in range(n): st[keep[a_ + k]] = (heard[b_ + k][1], heard[b_ + k][2])
    return st


# phrase -> written form (whole-word, case-insensitive, longest first)
DISPLAY = [
    ("pull request eighty two", "pull request 82"), ("pull request eighty one", "pull request 81"), ("eighty two", "82"), ("eighty one", "81"),
    ("twelve requests read", "12 requests read"), ("twelve accepted", "12 accepted"), ("eleven stress tested", "11 stress-tested"),
    ("zero of four triggered", "0 of 4 triggered"), ("thirty checks", "30 checks"), ("sixteen fields", "16 fields"), ("fifteen sections", "15 sections"),
    ("records seen is twelve", "records seen is 12"), ("records seen: twelve", "records seen: 12"), ("ten deliberate faults", "10 deliberate faults"),
    ("steps one, three and five", "steps 1, 3 and 5"), ("steps four and six", "steps 4 and 6"), ("three pieces", "3 pieces"),
    ("yes, no, yes", "YES, NO, YES"), ("no, yes, yes", "NO, YES, YES"), ("seven gate decisions", "7 gate decisions"),
    ("Twelve.", "12."), ("twelve", "12"),
]


def display(text):
    out = text
    for a, b in sorted(DISPLAY, key=lambda p: -len(p[0])):
        def rep(m, b=b):
            return (b[0].upper() + b[1:]) if m.group(0)[0].isupper() and b[0].isalpha() else b
        out = re.sub(r"\b" + re.escape(a) + r"\b", rep, out, flags=re.I)
    return out


def tok_times(text, words):
    """start/end per narration token (text.split()), aligned to Whisper's words with numerals and ordinals normalised; gaps interpolate."""
    toks = text.split(); st_map = _align(text, words); st = [None] * len(toks); en = [None] * len(toks)
    for i, (a_, b_) in st_map.items(): st[i], en[i] = a_, b_
    last = 0.0
    for i in range(len(toks)):
        if st[i] is None:
            nxt = next((st[j] for j in range(i + 1, len(toks)) if st[j] is not None), last + 0.3)
            st[i], en[i] = last, min(nxt, last + 0.3)
        last = en[i]
    return toks, st, en


def wrap(text):
    """<= MAX_LINES lines of <= MAX_CHARS, balanced; None if impossible."""
    if len(text) <= MAX_CHARS:
        return [text]
    words = text.split()
    best = None
    for k in range(1, len(words)):
        a, b = " ".join(words[:k]), " ".join(words[k:])
        if len(a) <= MAX_CHARS and len(b) <= MAX_CHARS:
            score = abs(len(a) - len(b)) - (10 if re.search(r'[:;,.]$', a) else 0) + (25 if a.split()[-1].lower() in ('shot', 'a', 'the', 'of', 'and', 'to', 'in', 'is', 'than', 'does', 'one at') else 0)
            if best is None or score < best[0]:
                best = (score, [a, b])
    return best[1] if best else None


def cues_for_beat(bid, t, offset):
    text = t["text"]
    toks, st, en = tok_times(text, t["words"])
    if False:
        h1 = t["inner_hold_at_s"] + t["inner_hold_s"]
        i0 = next(i for i in range(len(toks) - 3) if toks[i] == "Point" and toks[i + 3].startswith("five"))
        for k in range(4): st[i0 + k] = h1 + 0.18 * k; en[i0 + k] = h1 + 0.18 * (k + 1)
    # sentence ranges (token indices)
    sents, cur = [], []
    for i, tk in enumerate(toks):
        cur.append(i)
        if re.search(r"[.?!]$", tk):
            sents.append(cur)
            cur = []
    if cur:
        sents.append(cur)
    chunks = []
    for s in sents:
        pieces = [s]
        # split a sentence that does not fit in 2 lines, or spans a long pause, at clause marks first, then at pauses
        def too_long(p):
            return wrap(display(" ".join(toks[i] for i in p))) is None

        def has_pause(p):
            return any(st[p[k + 1]] - en[p[k]] > PAUSE_BREAK for k in range(len(p) - 1))
        changed = True
        while changed:
            changed = False
            nxt = []
            for p in pieces:
                if len(p) > 1 and (too_long(p) or has_pause(p)):
                    inq, quoted = False, []
                    for i in p:                       # token i is inside a quoted title: never split there
                        if toks[i].startswith('"'):
                            inq = True
                        quoted.append(inq)
                        if re.search(r'"[.,?!]?$', toks[i]) and (toks[i].count('"') % 2 == 1 or not toks[i].startswith('"')):
                            inq = False
                    roomy = [k for k in range(len(p) - 1) if k + 1 >= 3 and len(p) - (k + 1) >= 3 and not quoted[k]]
                    cand = [k for k in roomy if re.search(r"[,:;]$", toks[p[k]])]
                    if not cand:
                        cand = [k for k in roomy if st[p[k + 1]] - en[p[k]] > PAUSE_BREAK]
                    if not cand and too_long(p):
                        cand = list(range(2, len(p) - 2)) or [len(p) // 2]
                    if cand:
                        mid = len(p) / 2
                        k = min(cand, key=lambda k: abs(k + 1 - mid))
                        nxt += [p[: k + 1], p[k + 1:]]
                        changed = True
                        continue
                nxt.append(p)
            pieces = nxt
        chunks += pieces
    cues = []
    for p in chunks:
        a, b = st[p[0]] + offset, en[p[-1]] + offset + 0.12
        cues.append({"beat": bid, "start": a, "end": b, "text": display(" ".join(toks[i] for i in p))})
    return cues


def merge_short(cues):
    out = []
    for c in cues:
        if out and (c["end"] - c["start"]) < MIN_DUR and c["beat"] == out[-1]["beat"] and c["start"] - out[-1]["end"] < 0.8 \
                and len(wrap(out[-1]["text"] + " " + c["text"]) or []) > 0 and (c["end"] - out[-1]["start"]) <= MAX_DUR:
            out[-1]["end"] = c["end"]
            out[-1]["text"] += " " + c["text"]
        else:
            out.append(dict(c))
    return out


def ts(x, vtt=False):
    h, r = divmod(x, 3600)
    m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d}{'.' if vtt else ','}{int(round((s % 1) * 1000)):03d}".replace("1000", "999")


def _write(cues, stem):
    for i in range(len(cues) - 1):
        if cues[i]["end"] > cues[i + 1]["start"] - 0.02:
            cues[i]["end"] = max(cues[i]["start"] + 0.4, cues[i + 1]["start"] - 0.02)
    srt, vtt, bad = [], ["WEBVTT", ""], 0
    for n, c in enumerate(cues, 1):
        lines = wrap(c["text"])
        if lines is None: bad += 1; lines = [c["text"]]
        body = "\n".join(lines)
        srt.append(f"{n}\n{ts(c['start'])} --> {ts(c['end'])}\n{body}\n"); vtt.append(f"{ts(c['start'], True)} --> {ts(c['end'], True)}\n{body}\n")
    stem.with_suffix(".srt").write_text("\n".join(srt)); stem.with_suffix(".vtt").write_text("\n".join(vtt))
    return bad


def build(fmt):
    d = HERE / ("short" if fmt == "short" else ""); tim = json.loads((d / "mp3" / "timings.json").read_text())
    if fmt == "short":
        from beats_text_short import SHORT as L
    else:
        from beats_text import BEATS as L
    signed = {n.split()[0]: t for n, t in L}; cues, off = [], 0.0
    for bid in [n.split()[0] for n, _ in L]:
        t = dict(tim[bid]); t["text"] = signed[bid]
        cues += merge_short(cues_for_beat(bid, t, off)); off += round(t["duration_s"] * 30) / 30
    stem = d / ("two-customers-one-run-mycroft-short" if fmt == "short" else "two-customers-one-run-mycroft")
    bad = _write(cues, stem); print(f"{fmt}: {len(cues)} cues, {off:.1f} s, {bad} cues that do not wrap"); return stem.with_suffix(".srt")


def parse_srt(path):
    txt = Path(path).read_text().strip().split("\n\n")
    out = []
    for blk in txt:
        ln = blk.split("\n")
        m = re.match(r"(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+)", ln[1])
        g = list(map(int, m.groups()))
        out.append((g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000, g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000, ln[2:]))
    return out


def check(path):
    cues = parse_srt(path)
    probs = []
    for i, (a, b, lines) in enumerate(cues, 1):
        if len(lines) > MAX_LINES:
            probs.append((i, "more than 2 lines"))
        if any(len(x) > MAX_CHARS for x in lines):
            probs.append((i, f"line over {MAX_CHARS}: {max(lines, key=len)!r}"))
        if b - a > MAX_DUR:
            probs.append((i, f"longer than {MAX_DUR}s ({b - a:.1f})"))
        if i < len(cues) and b > cues[i][0]:
            probs.append((i, "overlaps the next cue"))
    print(f"{path}: {len(cues)} cues; last ends {cues[-1][1]:.2f} s; shortest {min(b - a for a, b, _ in cues):.2f} s; "
          f"longest {max(b - a for a, b, _ in cues):.2f} s")
    for p in probs:
        print("  PROBLEM", p)
    if not probs:
        print("  no rule problems")
    return probs


if __name__ == "__main__":
    if "--check" in sys.argv:
        check(sys.argv[sys.argv.index("--check") + 1])
    else:
        for f in ("long", "short"): check(build(f))
