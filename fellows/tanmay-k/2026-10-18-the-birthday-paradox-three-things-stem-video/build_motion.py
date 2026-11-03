#!/usr/bin/env python3
"""Motion for the 18 beats: reveal stages (build_slates.py, cv.k) timed to the narration, crossfaded.

plan   -> cue times per beat from the Whisper word clock (mp3/timings.json)   [--plan]
render -> every reveal state at 3840x2160 into _motion/                          [--render]
encode -> one 4K 30 fps video per beat into _beats/ (duration = padded audio)    [--encode]
compile-> master mp4 + captions + loudness                                       [--compile]
"""
import difflib, importlib.util, json, math, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
HERE = Path(__file__).parent
FPS, FADE, LEAD_IN = 30, 0.25, 0.10
CUES = {
 "B01": [(1, "twenty three people"), (2, "bet me"), (3, "two of them"), (4, "about half")],
 "B02": [(1, "how many people"), (2, "how uneven"), (3, "how many days"), (4, "hold a guess")],
 "B03": [(1, "the trick"), (2, "twenty three people make"), (3, "two hundred and fifty three pairs"), (4, "each pair")],
 "B04": [(1, "i run four hundred thousand"), (2, "fifty point seven percent"), (3, "with ten"), (4, "with thirty"), (5, "with fifty"), (6, "by fifty seven")],
 "B05": [(1, "it says some pair"), (2, "for somebody to share"), (3, "same crowd")],
 "B06": [(1, "i used federal counts"), (2, "the busiest day"), (3, "february twenty ninth")],
 "B07": [(1, "fifty point eight percent"), (2, "uneven days can only")],
 "B08": [(1, "about ninety six"), (2, "so the real calendar")],
 "B09": [(1, "squeeze it"), (2, "twenty three people all born"), (3, "ninety five point four percent"), (4, "same group size")],
 "B10": [(1, "a full year"), (2, "half a year"), (3, "ninety days"), (4, "sixty days"), (5, "born in the same month"), (6, "and with a window")],
 "B11": [(1, "across a whole year"), (2, "ninety day window"), (3, "sixty days"), (4, "a thirty day window"), (5, "a fortnight"), (6, "a week")],
 "B12": [(1, "does the uneven calendar"), (2, "of the three things"), (3, "the head count"), (4, "the evenness of the days"), (5, "and the number of days")],
 "B13": [(1, "twenty three for"), (2, "they follow a rule"), (3, "take the square root"), (4, "a year gives"), (5, "it is right for every"), (6, "never more than one")],
 "B14": [(1, "but a school year"), (2, "cutoff date"), (3, "about fifty point eight"), (4, "the squeeze only")],
 "B15": [(1, "birth months"), (2, "the square root of twelve"), (3, "times one point two"), (4, "so five people"), (5, "four people give"), (6, "five give")],
 "B16": [(1, "how many people"), (2, "use the rule"), (3, "a tempting"), (4, "pause")],
 "B17": [(1, "the root of fifty"), (2, "times one point two"), (3, "nine people give"), (4, "eight give"), (5, "not twenty five"), (6, "the slots set")],
 "B18": [(1, "ask how many"), (2, "tanmay kulkarni")],
}
COUNTDOWN = [(4 + n, n) for n in range(1, 8)]   # B16: stage 5..11 at narration_end + n s

def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
ma = load("make_audio")

def ref_tokens(text): return [t for t in (ma.norm(w) for w in text.split()) if t]

def heard_tokens(words):
    out = []
    for w, s, e in words:
        toks = [t for t in (ma.norm(x) for x in ma.spoken(w)) if t]
        for j, t in enumerate(toks): out.append((t, s + (e - s) * j / max(len(toks), 1)))
    return out

def times_for(entry):
    ref = ref_tokens(entry["text"]); heard = heard_tokens(entry["words"])
    sm = difflib.SequenceMatcher(None, ref, [h[0] for h in heard], autojunk=False)
    t = [None] * len(ref)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): t[a + k] = heard[b + k][1]
    last = None
    known = [(i, v) for i, v in enumerate(t) if v is not None]
    for i in range(len(t)):
        if t[i] is None:
            lo = max([(j, v) for j, v in known if j < i], default=None); hi = min([(j, v) for j, v in known if j > i], default=None)
            t[i] = lo[1] + (hi[1] - lo[1]) * (i - lo[0]) / (hi[0] - lo[0]) if lo and hi else (lo or hi or (0, 0.0))[1]
    return ref, t

def plan():
    timings = json.loads((HERE / "mp3" / "timings.json").read_text()); out = {}
    for bid, cues in CUES.items():
        e = timings[bid]; ref, t = times_for(e); pos = 0; cue_t = [(0, 0.0)]
        for stage, phrase in cues:
            toks = [ma.norm(w) for w in phrase.split()]
            idx = next((i for i in range(pos, len(ref) - len(toks) + 1) if ref[i:i + len(toks)] == toks), None)
            assert idx is not None, f"{bid}: phrase not found in order: {phrase!r}"
            pos = idx + 1
            at = max(0.0, t[idx])
            if at < cue_t[-1][1] + 0.6: at = cue_t[-1][1] + 0.6      # min spacing so fades never overlap
            cue_t.append((stage, round(at, 3)))
        if bid == "B16":
            cue_t = [(st, (round(e["narration_end_s"] - 0.2, 3) if st == 4 else t)) for st, t in cue_t]   # countdown bar appears as narration ends
            for stage, n in COUNTDOWN: cue_t.append((stage, round(e["narration_end_s"] + n * 1.0, 3)))
        out[bid] = {"duration_s": e["duration_s"], "cues": cue_t}
    (HERE / "_motion" / "plan.json").write_text(json.dumps(out, indent=1))
    return out

def render():
    bs = load("build_slates"); plan_ = json.loads((HERE / "_motion" / "plan.json").read_text())
    for bid, p in plan_.items():
        for stage, _ in p["cues"]:
            bs.BEATS[bid](stage).save(f"../_motion/{bid}_s{stage}.png")   # OUT is _stills; ../ -> _motion
        print("rendered", bid, len(p["cues"]), "states", flush=True)

def frames(sec): return round(sec * FPS) / FPS

def encode_one(bid, p):
    dur = math.ceil(p["duration_s"] * FPS) / FPS
    cues = p["cues"]; offs = [0.0] + [max(0.0, t - LEAD_IN) for _, t in cues[1:]]
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for i, (stage, _) in enumerate(cues):
        d = (offs[i + 1] + FADE - offs[i]) if i + 1 < len(cues) else (dur - offs[i])
        cmd += ["-loop", "1", "-framerate", str(FPS), "-t", f"{d + 0.05:.3f}", "-i", str(HERE / "_motion" / f"{bid}_s{stage}.png")]
    fc = ";".join(f"[{i}:v]format=yuv420p,setsar=1[v{i}]" for i in range(len(cues)))
    prev = "v0"
    for i in range(1, len(cues)):
        fc += f";[{prev}][v{i}]xfade=transition=fade:duration={FADE}:offset={offs[i]:.3f}[x{i}]"; prev = f"x{i}"
    cmd += ["-filter_complex", fc, "-map", f"[{prev}]", "-t", f"{dur:.3f}", "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast",
            "-crf", "17", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(HERE / "_beats" / f"{bid}.mp4")]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: sys.exit(f"{bid}: ffmpeg failed\n{r.stderr[-1500:]}")
    return bid, dur

def encode(only=None):
    plan_ = json.loads((HERE / "_motion" / "plan.json").read_text())
    jobs = {b: p for b, p in plan_.items() if not only or b in only}
    with ThreadPoolExecutor(2) as ex:
        for bid, dur in ex.map(lambda kv: encode_one(*kv), jobs.items()): print("encoded", bid, f"{dur:.2f}s", flush=True)

if __name__ == "__main__":
    a = sys.argv[1:]
    if "--plan" in a:
        p = plan()
        for b, v in p.items(): print(b, f"{v['duration_s']:.1f}s", [(s, round(t, 2)) for s, t in v["cues"]])
    if "--render" in a: render()
    if "--encode" in a: encode([x for x in a if x.startswith("B")] or None)
