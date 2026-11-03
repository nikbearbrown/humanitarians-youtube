#!/usr/bin/env python3
"""Cue sheet: the time each reveal stage of each beat starts, from the Whisper word clock (mp3/timings.json, short/mp3/timings.json).
A stage appears LEAD seconds before the first word of its trigger phrase, and never closer than MINGAP to the stage before.
Run: /opt/homebrew/bin/python3.12 cues.py  -> CUES.json, and a table of the longest static stretch per beat."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
LEAD, MINGAP = 0.25, 0.8
LONG = {"B00": ["this week", "public repository"], "B00b": ["twelve", "in another file", "same run"], "B01": ["earlier i built", "this time", "step six is"],
        "B02": ["first is a program", "second is a person", "constitution"], "B03": ["plain file", "records seen", "stop conditions", "it is built"],
        "B04": ["names its reader", "then fifteen sections", "recommendation"], "B05": ["in the log", "in the report", "twelve requests read", "eleven stress", "neither count"],
        "B06": ["in the log", "weights add up", "the report carries", "word for word"], "B07": ["the log holds", "three questions", "on the clean run", "on the faulty", "computed from"],
        "B08": ["in the log", "triggered true", "and the report", "said nothing"], "B09": ["each of the four", "the report says", "planted", "thirty checks", "pull request"],
        "B10": ["what keeps", "the report is generated", "run again", "you can clone"], "B11": ["who reads", "what do they do", "and what has", "write that down"],
        "B12": ["the recipe is", "that built", "the correction"], "B13": ["signing off"]}
SHORT = {"S-1": ["different", "hi", "for humanitarians", "this week", "a public", "a person can read"], "S0": ["somebody", "to know", "but who"], "S1": ["one is a program", "the next script", "the other is a person", "who has to decide", "they need different"],
         "S2": ["the machine's page", "records seen"], "S3": ["names its reader", "in its first section", "same fact"], "S4": ["they agree", "and the counts"],
         "S5": ["approve", "block live", "from the"], "S6": ["the log said", "the report said", "now it says"], "S7": ["who reads", "what they do", "what must"],
         "S8": ["two customers", "writing a", "a program"], "S9": ["signing off"]}
def norm(w): return re.sub(r"[^a-z0-9]", "", w.lower())
sys.path.insert(0, str(HERE))
from make_audio import spoken
def tokens(words):
    out = []
    for w, s, e in words:
        for t in spoken(w):
            n = norm(t)
            if n: out.append((n, s))
    return out
def find(toks, phrase, after):
    p = [norm(x) for x in phrase.split()]
    for i in range(len(toks) - len(p) + 1):
        if toks[i][1] >= after and [t[0] for t in toks[i:i + len(p)]] == p: return toks[i][1]
    return None
def build(fmt, table, path):
    T = json.loads(Path(path).read_text()); out = {}
    for bid, phrases in table.items():
        t = T[bid]; toks = tokens([tuple(w) for w in t["words"]]); st = [0.0]; prev = 0.0
        for ph in phrases:
            at = find(toks, ph, prev)
            if at is None: raise SystemExit(f"{fmt} {bid}: phrase not found after {prev:.2f}s: {ph!r}")
            when = max(at - LEAD, (st[-1] + MINGAP) if len(st) > 1 else 0.05); st.append(round(when, 3)); prev = at
        out[bid] = {"stages": st, "duration": t["duration_s"], "narration_end": t["narration_end_s"]}
    return out
if __name__ == "__main__":
    C = {"long": build("long", LONG, HERE / "mp3" / "timings.json"), "short": build("short", SHORT, HERE / "short" / "mp3" / "timings.json")}
    (HERE / "CUES.json").write_text(json.dumps(C, indent=1))
    C["short"]["S9"]["stages"].append(round(C["short"]["S9"]["duration"] - 0.9, 3))   # the loop stage: the Short ends on its own first frame
    for fmt in C:
        print(fmt)
        for b, v in C[fmt].items():
            ts = v["stages"] + [v["duration"]]; gap = max(b2 - a for a, b2 in zip(ts, ts[1:]))
            print(f"  {b:5} stages {v['stages']}  longest static {gap:.1f} s")
