#!/usr/bin/env python3
"""make_captions.py: SRT + VTT for the long film from the measured audio (mp3/timings.json, the Whisper word clock).

    /opt/homebrew/bin/python3.12 make_captions.py            # writes color-never-hears-the-music.srt / .vtt
    /opt/homebrew/bin/python3.12 make_captions.py --check short/color-never-hears-the-music-short.srt   # validate any SRT

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

ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def norm(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())


def spoken(tok):
    """digits -> words, the way Whisper writes numerals back (decimals as 'point', % as 'percent')."""
    t = tok.rstrip("%.,?!").replace(",", "")
    if not re.fullmatch(r"\d+(\.\d+)?", t):
        return [tok]
    whole, _, dec = t.partition(".")
    n = int(whole)
    out = [ONES[n]] if n < 20 else ([TENS[n // 10]] + ([ONES[n % 10]] if n % 10 else []) if n < 100 else [str(n)])
    if n >= 1000:
        out = ["two", "thousand"] + ([] if n % 1000 == 0 else spoken(str(n % 1000)))
    if dec:
        out += ["point"] + [ONES[int(c)] for c in dec]
    return out + (["percent"] if tok.endswith("%") else [])


# phrase -> written form (whole-word, case-insensitive, longest first)
DISPLAY = [
    ("point eight nine to point nine nine", ".89 to .99"),
    ("point nine seven", ".97"), ("point nine six", ".96"), ("point nine nine", ".99"), ("point eight nine", ".89"),
    ("point eight eight", ".88"), ("point nine nine", ".99"),
    ("about ninety seven people", "about 97 people"), ("ninety seven", "97"),
    ("twenty thirteen", "2013"), ("twenty eleven", "2011"),
    ("eighteen pieces", "18 pieces"), ("fifty seconds", "50 seconds"),
    ("a set of thirty seven", "a set of 37"), ("thirty seven", "37"),
    ("sixty four-year-olds", "60 four-year-olds"), ("nine minutes", "9 minutes"),
    ("about six months", "about 6 months"), ("by about eighteen", "by about 18"),
    ("seven to twelve seconds", "7 to 12 seconds"), ("one to three", "1 to 3"),
]


def display(text):
    out = text
    for a, b in sorted(DISPLAY, key=lambda p: -len(p[0])):
        def rep(m, b=b):
            return (b[0].upper() + b[1:]) if m.group(0)[0].isupper() and b[0].isalpha() else b
        out = re.sub(r"\b" + re.escape(a) + r"\b", rep, out, flags=re.I)
    return out


def tok_times(text, words):
    """start/end per narration token (text.split()), via alignment with Whisper's words; unmatched tokens interpolate."""
    toks = text.split()
    ref = [norm(t) for t in toks]
    heard = []
    for w, s0, e0 in words:
        parts = [n for n in (norm(x) for x in spoken(w)) if n]
        for j, n in enumerate(parts):
            span = (e0 - s0) / max(len(parts), 1)
            heard.append((n, s0 + span * j, s0 + span * (j + 1)))
    sm = difflib.SequenceMatcher(None, [r for r in ref if r], [h[0] for h in heard], autojunk=False)
    idx = [i for i, r in enumerate(ref) if r]
    st = [None] * len(toks)
    en = [None] * len(toks)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            st[idx[a + k]], en[idx[a + k]] = heard[b + k][1], heard[b + k][2]
    # interpolate gaps
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
            score = abs(len(a) - len(b)) - (10 if re.search(r'[:;,]$', a) else 0)
            if best is None or score < best[0]:
                best = (score, [a, b])
    return best[1] if best else None


def cues_for_beat(bid, t, offset):
    text = t["text"]
    toks, st, en = tok_times(text, t["words"])
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


def build():
    tim = json.loads((HERE / "mp3" / "timings.json").read_text())
    cues, off = [], 0.0
    for bid, t in tim.items():
        cues += merge_short(cues_for_beat(bid, t, off))
        off += t["duration_s"]
    # never overlap the next cue
    for i in range(len(cues) - 1):
        if cues[i]["end"] > cues[i + 1]["start"] - 0.02:
            cues[i]["end"] = max(cues[i]["start"] + 0.4, cues[i + 1]["start"] - 0.02)
    bad = 0
    srt, vtt = [], ["WEBVTT", ""]
    for n, c in enumerate(cues, 1):
        lines = wrap(c["text"])
        if lines is None:
            bad += 1
            lines = [c["text"]]
        body = "\n".join(lines)
        srt.append(f"{n}\n{ts(c['start'])} --> {ts(c['end'])}\n{body}\n")
        vtt.append(f"{ts(c['start'], True)} --> {ts(c['end'], True)}\n{body}\n")
    (HERE / "color-never-hears-the-music.srt").write_text("\n".join(srt))
    (HERE / "color-never-hears-the-music.vtt").write_text("\n".join(vtt))
    print(f"{len(cues)} cues, {off:.1f} s master, {bad} cues that do not wrap")
    return cues


def build_short():
    d = HERE / "short"
    t = json.loads((d / "mp3" / "timings_short.json").read_text())
    cues = merge_short(cues_for_beat("S", {"text": t["text"], "words": t["words"]}, 0.0))
    for i in range(len(cues) - 1):
        if cues[i]["end"] > cues[i + 1]["start"] - 0.02:
            cues[i]["end"] = max(cues[i]["start"] + 0.4, cues[i + 1]["start"] - 0.02)
    srt, vtt, bad = [], ["WEBVTT", ""], 0
    for n, c in enumerate(cues, 1):
        lines = wrap(c["text"])
        if lines is None:
            bad += 1
            lines = [c["text"]]
        body = "\n".join(lines)
        srt.append(f"{n}\n{ts(c['start'])} --> {ts(c['end'])}\n{body}\n")
        vtt.append(f"{ts(c['start'], True)} --> {ts(c['end'], True)}\n{body}\n")
    (d / "color-never-hears-the-music-short.srt").write_text("\n".join(srt))
    (d / "color-never-hears-the-music-short.vtt").write_text("\n".join(vtt))
    print(f"{len(cues)} cues, {t['duration_s']:.1f} s Short, {bad} cues that do not wrap")


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
    if "--short" in sys.argv:
        build_short()
        check(HERE / "short" / "color-never-hears-the-music-short.srt")
    elif "--check" in sys.argv:
        check(sys.argv[sys.argv.index("--check") + 1])
    else:
        build()
        check(HERE / "color-never-hears-the-music.srt")
