#!/usr/bin/env python3
"""Short (9:16, 2160x3840): ONE continuous scene drawn as a function of time. Nothing cuts; state carries across every line; the last 1.8 s
dissolve back to frame 1 so it loops. Every caption, chip and shot is anchored to a word time on the Whisper clock (mp3/timings_short.json).

Fades are exact: every element is drawn as mix(background, colour, alpha) (Pillow ignores fill alpha on text, so alpha is applied to the colour
itself against its known background). Text swaps are complementary (old = 1 - e, new = e, one eased progress).

Layout in logical px at 1080x1920 (x2 -> 2160x3840). Safe area: y 230 to 1440 (12% to 75% of the height), x 60 to 900 (nothing in the right rail).
All text is at least 34 logical px (68 px at 2160 wide).

  python3.12 build_short.py frames 0 5 12.5     -> _qc/f_<t>.png (1080x1920)
  python3.12 build_short.py times               -> the anchor times
  python3.12 build_short.py render              -> _frames/*.jpg -> _video/short-silent.mp4
"""
import json, shutil, subprocess, sys
from multiprocessing import Pool
from pathlib import Path
from PIL import Image, ImageDraw
HERE = Path(__file__).parent; sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent))
from build_slates import F, PAGE, CARD, BORDER, INK, INK_SOFT, GHOST, SPARK, SEND
import sim_model as sm
from cues import spoken, norm

def mix(a, b, t):
    a = tuple(int(a[i:i + 2], 16) for i in (1, 3, 5)); b = tuple(int(b[i:i + 2], 16) for i in (1, 3, 5)); t = max(0.0, min(1.0, t))
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))

S = 2; PW, PH = 1080, 1920; FPS = 30
TIM = json.loads((HERE / "mp3" / "timings_short.json").read_text()); DUR = TIM["duration_s"]
LINE = {l["id"]: l for l in TIM["lines"]}; L = lambda k: LINE[k]["start"]
old = sm.OLD; must = (old.H - old.h) / 2; can6 = 2.0 * old.T(5); MID = old.H / 2; SHORT_Y = MID - can6
TRACK = "#EDEBE1"

def ease(p): p = max(0.0, min(1.0, p)); return p * p * (3 - 2 * p)
def prog(t, t0, f=0.35): return ease((t - t0) / f)

# ------------------------------------------------------------------------------------------------ word anchors (Whisper clock)
TOK = []
for w, s0, e0 in TIM["words"]:
    for x in spoken(w):
        n = norm(x)
        if n: TOK.append((n, s0))
def wt(tok, after=0.0, nth=1):
    c = 0
    for n, s0 in TOK:
        if s0 >= after - 0.05 and n == tok:
            c += 1
            if c == nth: return s0
    raise KeyError((tok, after, nth))

CW = []                                                     # "Shot one" ... "Shot six"
a = L("S03")
for nm in ["one", "two", "three", "four", "five", "six"]:
    a = wt(nm, a) + 0.01; CW.append(a - 0.01)
T_ESSAY, T_BUILT, T_WANTED, T_TANMAY = wt("essay", L("S02")), wt("built", L("S02")), wt("wanted", L("S02")), wt("tanmay", L("S02"))
T_DEFENDED = wt("defended", L("S03")); T_LACKS, T_FASTER = wt("lacks", L("S04")), wt("faster", L("S04"))
T_FIRST, T_SECOND, T_LONGER = wt("first", L("S05")), wt("second", L("S05")), wt("longer", L("S05"))
T_SIXTH, T_EIGHT = wt("sixth", L("S06")), wt("eight", L("S06")); T_ARITH, T_SEARCH = wt("arithmetic", L("S06")), wt("search", L("S06"))
T_NOBODY, T_RAN = wt("nobody", L("S06")), wt("ran", L("S06")); T_BUT, T_SHOWS = wt("but", L("S07")), wt("shows", L("S07"))
T_SPIN, T_MACHINE = wt("spin", L("S07")), wt("machine", L("S07"))

# ------------------------------------------------------------------------------------------------ the shot timeline
def plays():
    P = []; t = 0.0; i = 0
    while t < L("S03") - 0.9:                                  # S01-S02: ambient rally, counter 1
        P.append({"t0": t, "d": 1.4, "k": 1, "amb": True, "y": MID + (110 if i % 2 else -110)}); t += 1.8; i += 1
    for k in range(1, 7): P.append({"t0": CW[k - 1] - 0.62, "d": 0.82, "k": k, "count_at": CW[k - 1] - 0.05, "ph": "S03"})
    t = L("S04"); k = 1                                        # S04: crossings getting shorter, the counter walks
    while k <= 5 and t < L("S05") - 0.6:
        d = 1.55 / 1.05 ** (k - 1); P.append({"t0": t, "d": d, "k": k, "count_at": t, "ph": "S04"}); t += d + 0.25; k += 1
    t = L("S05"); first = True                                 # S05: shot one repeating, counter back to 1
    while t < L("S06") - 0.2:
        P.append({"t0": t, "d": 1.3, "k": 1, "count_at": t if first else None, "ph": "S05"}); first = False; t += 2.1
    for k in range(1, 7):                                      # S06: shots 1..6, the bar sinks, shot six lands on the word "sixth"
        c = T_SIXTH - 0.15 - (6 - k) * 0.62; P.append({"t0": c, "d": 0.56, "k": k, "count_at": c, "ph": "S06", "sink": True})
    t = L("S08") + 0.1; i = 0                                  # S08: the rally resumes (the scene settles back to frame 1); counter back to 1
    while t < DUR - 0.2:
        P.append({"t0": t, "d": 1.4, "k": 1, "amb": True, "y": MID + (110 if i % 2 else -110), "count_at": t if i == 0 else None}); t += 1.8; i += 1
    return P
PLAYS = plays()
P6_S03 = [p for p in PLAYS if p.get("ph") == "S03" and p["k"] == 6][0]
_p6 = [p for p in PLAYS if p.get("ph") == "S06" and p["k"] == 6][0]; S6_END = _p6["t0"] + _p6["d"]
FROZEN = [(P6_S03["t0"] + P6_S03["d"], L("S04")), (S6_END, L("S08") - 0.1)]
S6 = [p for p in PLAYS if p.get("ph") == "S06"]

def cur_play(t):
    for p in PLAYS:
        if p["t0"] <= t < p["t0"] + p["d"]: return p
    return None
def counter_value(t):
    v = 1
    for p in PLAYS:
        if p.get("count_at") is not None and t >= p["count_at"]: v = p["k"]
    return v
def can_value(t):
    if t < S6[0]["t0"]: return 2.0 * old.T(0)
    vals = [(p["t0"], 2.0 * old.T(p["k"] - 1)) for p in S6]
    for i in range(len(vals) - 1):
        if vals[i][0] <= t < vals[i + 1][0]:
            u = ease((t - vals[i][0]) / (vals[i + 1][0] - vals[i][0])); return vals[i][1] + (vals[i + 1][1] - vals[i][1]) * u
    return vals[-1][1]
def rest_defender(t):
    for a, b in FROZEN:
        if a <= t < b: return SHORT_Y
        if b <= t < b + 0.3: return SHORT_Y + (MID - SHORT_Y) * ease((t - b) / 0.3)
    prev = [p for p in PLAYS if p["t0"] + p["d"] <= t]
    if prev:
        lp = prev[-1]; since = t - (lp["t0"] + lp["d"]); end_def = lp["y"] if lp.get("amb") else old.h / 2
        return end_def + (MID - end_def) * ease(since / 0.3)
    return MID

# ------------------------------------------------------------------------------------------------ copy on screen (muted-readable)
HEAD = [(0.0, "THE BET"), (L("S02") - 0.15, "PONG: TWO PADDLES, ONE BALL"), (L("S03") - 0.15, "SHOT SIX"), (L("S04") - 0.15, "THE DEFENDER SEES IT COMING"),
        (L("S05") - 0.15, "TWO BARS"), (L("S06") - 0.15, "THE CLOCK"), (L("S07") - 0.15, "A MODEL, NOT A MACHINE"), (L("S08") - 0.15, "THE RALLY HAS A CLOCK")]
CAP = [(0.0, "a perfect defender loses on the sixth shot"), (L("S02") - 0.15, "Pong: two paddles and one ball"), (T_ESSAY - 0.2, "an essay says: no perfect defense"),
       (T_WANTED - 0.2, "when is that true?"), (T_BUILT - 0.2, "so I built the smallest Pong I could"), (T_TANMAY - 0.25, "Tanmay Kulkarni, in for Humanitarians AI"),
       (L("S03") - 0.15, "watch the rally"), (T_DEFENDED - 0.4, "all five defended"), (CW[5] - 0.1, "shot six: the ball goes past"),
       (L("S04") - 0.15, "the defender sees where the ball is going"), (T_LACKS - 0.2, "what it lacks is time"), (T_FASTER - 0.3, "the ball is 5% faster on every shot"),
       (L("S05") - 0.15, "two bars explain it"), (T_FIRST - 0.2, "first: how far the paddle can travel while the ball crosses"),
       (T_SECOND - 0.2, "second: how far the worst shot makes it go, about half the field"), (T_LONGER - 0.3, "first longer: a perfect defense exists"),
       (L("S06") - 0.15, "the crossing keeps shrinking, so the first bar sinks"), (T_SIXTH - 0.3, "shot six: it drops below the line"),
       (T_EIGHT - 0.25, "8.4 pixels short"), (T_NOBODY - 0.2, "nobody made a mistake"), (T_RAN - 0.3, "the rally ran out of time"),
       (L("S07") - 0.15, "only a model: no spin, no real machine"), (T_SHOWS - 0.3, "no perfect defense is true here only because the ball speeds up"),
       (L("S08") - 0.15, "The Rally Has a Clock: When Is “No Perfect Defense” True in Pong?")]
SRC = [(0.0, ""), (T_ESSAY - 0.2, "From an essay in the Humanitarians AI repo"), (T_BUILT - 0.2, "Our simulation: 858 x 525, paddle 60, +5%/shot"),
       (L("S07") - 0.15, "Our simulation of a simplified Pong")]
CHIPS = [(T_ARITH - 0.15, "ARITHMETIC: shot six"), (T_SEARCH - 0.15, "SEARCH: shot six")]
BAR1, BAR2 = T_FIRST - 0.2, T_SECOND - 0.2
TIMER = (T_LACKS - 0.2, L("S05") - 0.2); NOSPEED = (T_SHOWS - 0.2, L("S08") - 0.3)
LOOP0 = DUR - 2.0

def txt(d, x, y, s, kind, size, col, a, bg=PAGE, anchor="la"):
    if a <= 0.004: return
    d.text((x * S, y * S), s, font=F(kind, size), fill=mix(bg, col, min(1.0, a)), anchor=anchor)
def wrap_lines(s, kind, size, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t2 = (cur + " " + w).strip()
        if F(kind, size).getlength(t2) / S <= maxw: cur = t2
        else: lines.append(cur); cur = w
    lines.append(cur); return lines
def swap(d, t, items, x, y, kind, size, col, maxw, lh=1.18, bg=PAGE, fit=False):
    """complementary text swap: current text at e, previous at 1 - e."""
    idx = max([i for i, (t0, _) in enumerate(items) if t0 <= t + 1e-9] or [0])
    t0, cur = items[idx]; e = prog(t, t0) if idx > 0 else 1.0
    def draw(s, a):
        sz = size
        while fit and F(kind, sz).getlength(s) / S > maxw and sz > 34: sz -= 1
        for i, l in enumerate(wrap_lines(s, kind, sz, maxw)): txt(d, x, y + i * sz * lh, l, kind, sz, col, a, bg)
    if idx > 0 and e < 1.0 and items[idx - 1][1]: draw(items[idx - 1][1], 1 - e)
    if cur: draw(cur, e)

FX0, FY0, FSC = 60, 330, 840 / 858.0
def fp(x, y): return (FX0 + x * FSC, FY0 + y * FSC)
def lerp(a, b, u): return a + (b - a) * u

def scene_body(t):
    im = Image.new("RGB", (PW * S, PH * S), PAGE); d = ImageDraw.Draw(im)
    swap(d, t, HEAD, 60, 238, "serif", 54, INK, 840, fit=True)
    d.rectangle((FX0 * S, FY0 * S, (FX0 + 840) * S, (FY0 + old.H * FSC) * S), fill=CARD, outline=BORDER, width=2 * S)
    pl = cur_play(t); ball = None; trail = None; dy = MID
    if pl:
        u = (t - pl["t0"]) / pl["d"]; amb = pl.get("amb"); short = (not amb) and pl["k"] == 6
        tgt = pl["y"] if amb else 0.0
        end_def = tgt if amb else (old.h / 2 if not short else SHORT_Y)
        ball = (lerp(old.W - 14, 14 if not short else -60, u), lerp(MID, tgt, u)); trail = (tgt, short)
        dy = lerp(MID, end_def, ease(min(1.0, u * 1.25)))
    else:
        dy = rest_defender(t)
    def paddle(side, yc):
        x0 = 0 if side == "L" else old.W - 14; (xa, ya), (xb, yb) = fp(x0, yc - old.h / 2), fp(x0 + 14, yc + old.h / 2)
        d.rectangle((xa * S, ya * S, xb * S, yb * S), fill=INK)
    paddle("R", MID); paddle("L", dy)
    if ball:
        x, y = fp(*ball); tg, sh = trail; a_, b_ = fp(old.W - 14, MID), fp(14 if not sh else -60, tg)
        for i in range(0, 28, 2):
            u0, u1 = i / 28, (i + 1) / 28
            d.line([(a_[0] + (b_[0] - a_[0]) * u0) * S, (a_[1] + (b_[1] - a_[1]) * u0) * S, (a_[0] + (b_[0] - a_[0]) * u1) * S, (a_[1] + (b_[1] - a_[1]) * u1) * S], fill=mix(CARD, SPARK, 0.35), width=3 * S)
        if x > FX0 - 2: d.ellipse(((x - 11) * S, (y - 11) * S, (x + 11) * S, (y + 11) * S), fill=SPARK)
    for g0, g1 in FROZEN:                                       # the 8.4 px gap while the defender stands short of shot six
        e = prog(t, g0, 0.4) * (1 - prog(t, g1, 0.3))
        if e > 0.01:
            gx = fp(26, 0)[0]
            d.line([(gx * S, (fp(0, 0)[1] + 2) * S), (gx * S, fp(0, 8.4)[1] * S)], fill=mix(CARD, SEND, e), width=4 * S)
            d.ellipse(((fp(8, 0)[0] - 11) * S, (fp(0, 0)[1] - 11) * S, (fp(8, 0)[0] + 11) * S, (fp(0, 0)[1] + 11) * S), fill=mix(CARD, SPARK, e))
            txt(d, gx + 16, fp(0, 0)[1] + 20, "8.4 px short", "sans", 34, SPARK, e, bg=CARD)
    swap(d, t, CAP, 60, 860, "serif", 40, INK, 840, lh=1.14)
    swap(d, t, SRC, 60, 1376, "sans", 34, INK_SOFT, 840, lh=1.1, fit=True)
    # counter: numeral swap at the counting moment
    k = counter_value(t); ch = sorted((p["count_at"], p["k"]) for p in PLAYS if p.get("count_at") is not None and p["count_at"] <= t)
    last = ch[-1][0] if ch else None; kprev = ch[-2][1] if len(ch) > 1 else 1
    e = prog(t, last, 0.14) if last is not None else 1.0
    txt(d, 60, 1000, "SHOT", "sans", 36, INK_SOFT, 1.0)
    if e < 1.0 and kprev != k: txt(d, 60, 1020, str(kprev), "serif", 104, INK, 1 - e)
    txt(d, 60, 1020, str(k), "serif", 104, SEND if k == 6 else INK, e if kprev != k else 1.0)
    for i in range(6):
        cx = 330 + i * 76; fill = TRACK
        if L("S03") - 0.1 <= t < L("S08") + 0.1 and k > i: fill = INK if i < 5 else SPARK
        d.ellipse(((cx - 20) * S, (1070 - 20) * S, (cx + 20) * S, (1070 + 20) * S), fill=fill)
    # the two bars
    bt = prog(t, BAR1, 0.5) * (1 - prog(t, L("S08") - 0.15, 0.4))
    if bt > 0:
        can = can_value(t); bx0, bw, mx = 60, 780, 300.0; a1, a2 = prog(t, BAR1, 0.4) * (1 - prog(t, L("S08") - 0.15, 0.4)), prog(t, BAR2, 0.4) * (1 - prog(t, L("S08") - 0.15, 0.4))
        txt(d, bx0, 1176, "CAN TRAVEL", "sans", 36, INK_SOFT, a1)
        d.rounded_rectangle((bx0 * S, 1216 * S, (bx0 + bw) * S, 1248 * S), radius=4 * S, fill=mix(PAGE, TRACK, a1))
        d.rounded_rectangle((bx0 * S, 1216 * S, (bx0 + bw * min(can, mx) / mx) * S, 1248 * S), radius=4 * S, fill=mix(PAGE, (INK if can >= must else SPARK), a1))
        txt(d, bx0 + bw, 1176, f"{can:.0f} px", "sans", 36, INK, a1, anchor="ra")
        if a2 > 0.01:
            txt(d, bx0, 1268, "MUST TRAVEL", "sans", 36, INK_SOFT, a2)
            d.rounded_rectangle((bx0 * S, 1308 * S, (bx0 + bw) * S, 1340 * S), radius=4 * S, fill=mix(PAGE, TRACK, a2))
            d.rounded_rectangle((bx0 * S, 1308 * S, (bx0 + bw * must / mx) * S, 1340 * S), radius=4 * S, fill=mix(PAGE, GHOST, a2))
            txt(d, bx0 + bw, 1268, f"{must:.1f} px", "sans", 36, INK, a2, anchor="ra")
            lx = bx0 + bw * must / mx
            for yy in range(1196, 1346, 14): d.line([(lx * S, yy * S), (lx * S, (yy + 8) * S)], fill=mix(PAGE, SEND, a2), width=3 * S)
    tb = prog(t, TIMER[0], 0.4) * (1 - prog(t, TIMER[1], 0.4))                 # S04: the crossing time shrinking
    if tb > 0.01:
        dd = 1.55 / 1.05 ** (counter_value(t) - 1)
        txt(d, 60, 1176, "ONE CROSSING", "sans", 36, INK_SOFT, tb)
        d.rounded_rectangle((60 * S, 1216 * S, 840 * S, 1248 * S), radius=4 * S, fill=mix(PAGE, TRACK, tb))
        d.rounded_rectangle((60 * S, 1216 * S, (60 + 780 * dd / 1.55) * S, 1248 * S), radius=4 * S, fill=mix(PAGE, SPARK, tb))
        txt(d, 840, 1176, f"{dd/1.55*100:.0f}%", "sans", 36, INK, tb, anchor="ra")
    for i, (t0, s) in enumerate(CHIPS):                                         # arithmetic / search land on shot six (inside the empty field)
        a = prog(t, t0, 0.35) * (1 - prog(t, L("S07") - 0.15, 0.35))
        if a > 0.01:
            y0 = 640 + i * 74
            d.rounded_rectangle((420 * S, y0 * S, 840 * S, (y0 + 60) * S), radius=10 * S, outline=mix(CARD, SEND, a), width=3 * S, fill=CARD)
            txt(d, 440, y0 + 10, s, "sans", 36, SEND, a, bg=CARD)
    for i, (t0, lab) in enumerate([(T_SPIN - 0.15, "NO SPIN"), (T_MACHINE - 0.15, "NO REAL MACHINE")]):      # S07: the model's limits, as they are spoken
        a = prog(t, t0, 0.35) * (1 - prog(t, L("S08") - 0.3, 0.35))
        if a > 0.01:
            y0 = 640 + i * 74
            d.rounded_rectangle((420 * S, y0 * S, 840 * S, (y0 + 60) * S), radius=10 * S, outline=mix(CARD, INK_SOFT, a), width=3 * S, fill=CARD)
            txt(d, 440, y0 + 10, lab, "sans", 36, INK_SOFT, a, bg=CARD)
    ns = prog(t, NOSPEED[0], 0.5) * (1 - prog(t, NOSPEED[1], 0.4))              # S07: shot after shot, no break: the dots land one by one
    if ns > 0.01:
        d.rectangle((0, 1160 * S, PW * S, 1350 * S), fill=PAGE)
        txt(d, 60, 1176, "NO SPEED-UP: PADDLES 2.0 AND 3.0", "sans", 36, INK_SOFT, ns)
        t_dot = NOSPEED[0] + 0.5; step = 0.34
        for i in range(9):
            cx = 76 + i * 76; a_ = prog(t, t_dot + i * step, 0.2) * (1 - prog(t, NOSPEED[1], 0.4))
            d.ellipse(((cx - 20) * S, (1250 - 20) * S, (cx + 20) * S, (1250 + 20) * S), fill=mix(PAGE, TRACK, ns))
            if a_ > 0.01: d.ellipse(((cx - 20) * S, (1250 - 20) * S, (cx + 20) * S, (1250 + 20) * S), fill=mix(PAGE, INK, a_))
        for j, r in enumerate((13, 9, 6)):
            cx = 76 + 9 * 76 + j * 40; a_ = prog(t, t_dot + (9 + j) * step, 0.2) * (1 - prog(t, NOSPEED[1], 0.4))
            if a_ > 0.01: d.ellipse(((cx - r) * S, (1250 - r) * S, (cx + r) * S, (1250 + r) * S), fill=mix(PAGE, INK, a_ * (1 - 0.25 * j)))
        txt(d, 60, 1290, "200 shots, no break", "sans", 36, SEND, prog(t, t_dot + 12 * step, 0.3) * (1 - prog(t, NOSPEED[1], 0.4)))
    return im

_f0 = None
def scene(t):
    """the continuous scene; the last 2 s dissolve back to frame 1 so the Short loops"""
    global _f0
    im = scene_body(min(t, LOOP0 - 0.01))
    if t >= LOOP0:
        if _f0 is None: _f0 = scene_body(0.0)
        return Image.blend(im, _f0, prog(t, LOOP0, 1.8))
    return im

def _job(i):
    p = HERE / "_frames" / f"f{i:05d}.jpg"; scene(i / FPS).save(p, quality=95, subsampling=0); return i

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "render"
    if cmd == "frames":
        (HERE / "_qc").mkdir(exist_ok=True)
        for a in sys.argv[2:]: scene(float(a)).resize((1080, 1920)).save(HERE / "_qc" / f"f_{float(a):05.1f}.png")
        print("ok")
    elif cmd == "times":
        for n, v in sorted(globals().items()):
            if n.startswith("T_") or n in ("BAR1", "BAR2", "S6_END"): print(n, round(v, 2))
        print("CW", [round(x, 2) for x in CW], "dur", DUR)
    else:
        fr = HERE / "_frames"; shutil.rmtree(fr, ignore_errors=True); fr.mkdir(); n = int(round(DUR * FPS))
        with Pool(5) as p:
            for i in p.imap_unordered(_job, range(n), chunksize=8):
                if i % 300 == 0: print("frame", i, flush=True)
        (HERE / "_video").mkdir(exist_ok=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(fr / "f%05d.jpg"), "-c:v", "libx264", "-preset", "medium", "-crf", "13",
                        "-pix_fmt", "yuv420p", str(HERE / "_video" / "short-silent.mp4")], check=True)
        print("done", n, "frames")
