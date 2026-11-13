#!/usr/bin/env python3
"""The Short: ONE continuous 9:16 scene, 2160x3840 at 30 fps, every event timed to the Whisper word clock.

A calendar of possible birthdays holds 23 dots. The narration takes days away; the calendar narrows around the same dots
and the odds counter climbs; the rule is typeset; the calendar widens again and the loop closes on the opening state.
There are no cuts: scene(t) is a pure function of time, so every frame follows from the one before.

  /opt/homebrew/bin/python3.12 short/build_short.py --cues      # event times from the audio
  /opt/homebrew/bin/python3.12 short/build_short.py --render    # frames -> short/_frames/
  /opt/homebrew/bin/python3.12 short/build_short.py --encode    # frames -> short/_video/short-silent.mp4
"""
import importlib.util, json, math, random, subprocess, sys
from multiprocessing import Pool
from pathlib import Path
from PIL import Image, ImageDraw

HERE = Path(__file__).parent; ROOT = HERE.parent
FPS = 30
W, H, S = 1080, 1920, 2                  # logical 1080x1920, rendered x2 = 2160x3840 (4K portrait)
SAFE_TOP, SAFE_BOTTOM, SAFE_L, SAFE_R = 230, 1440, 60, 900   # Shorts UI safe area (logical px)
MIN_SANS = 30                            # nothing smaller than 30 px logical on a label


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


bs = load(ROOT / "build_slates.py", "bs")          # palette, fonts, Math, exact probabilities
bm = load(ROOT / "build_motion.py", "bm")          # times_for(): narration tokens -> Whisper clock
ma = bm.ma
PAGE, CARD, BORDER, INK, INK_SOFT, SPARK, SEND = bs.PAGE, bs.CARD, bs.BORDER, bs.INK, bs.INK_SOFT, bs.SPARK, bs.SEND
SPARK_TEXT = bs.SPARK_TEXT
pm = bs.pm


def rgba(c, a=1.0):
    if isinstance(c, tuple): return c[:3] + (int(255 * a * (c[3] / 255 if len(c) > 3 else 1)),)
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (int(255 * max(0.0, min(1.0, a))),)


class PCanvas:
    """Portrait canvas: RGB base, drawn with real alpha blending; every primitive honours cv.alpha; logs the text it draws."""
    def __init__(self):
        self.im = Image.new("RGB", (W * S, H * S), rgba(PAGE)[:3]); self.d = ImageDraw.Draw(self.im, "RGBA"); self.alpha = 1.0; self.log = []   # RGB base + RGBA draw = real alpha blending (an RGBA base replaced pixels, so every fade was a pop)

    def tw(self, s, kind, size): return bs.F(kind, size).getlength(s) / S

    def text(self, x, y, s, kind="sans", size=30, fill=INK, anchor="ls"):
        if kind.startswith("sans"): assert size >= MIN_SANS, f"type below {MIN_SANS}px: {s!r} at {size}"
        if self.alpha <= 0.01: return
        if isinstance(fill, str) and fill == SPARK: fill = SPARK_TEXT if size < 48 else SEND
        self.log.append((s, size, round(self.alpha, 2), y))
        # Pillow ignores the alpha of a text fill, so draw the glyph coverage into a small mask, scale it by the alpha, and paste the colour through it
        font = sk.F(kind, size) if "sk" in globals() else bs.F(kind, size)
        l, t_, r, b = font.getbbox(s, anchor=anchor); pad = 3
        mask = Image.new("L", (r - l + 2 * pad, b - t_ + 2 * pad), 0)
        ImageDraw.Draw(mask).text((-l + pad, -t_ + pad), s, font=font, fill=255, anchor=anchor)
        a = max(0.0, min(1.0, self.alpha))
        if a < 0.999: mask = mask.point(lambda v: int(v * a))
        self.im.paste(rgba(fill, 1.0)[:3], (int(round(x * S + l - pad)), int(round(y * S + t_ - pad))), mask)

    def line(self, pts, fill=INK, width=2):
        if self.alpha > 0.01: self.d.line([(x * S, y * S) for x, y in pts], fill=rgba(fill, self.alpha), width=round(width * S), joint="curve")

    def rect(self, x0, y0, x1, y1, fill=None, outline=None, width=1, r=0):
        if self.alpha <= 0.01: return
        box = (x0 * S, y0 * S, x1 * S, y1 * S); f = rgba(fill, self.alpha) if fill else None; o = rgba(outline, self.alpha) if outline else None
        if r: self.d.rounded_rectangle(box, radius=r * S, fill=f, outline=o, width=round(width * S))
        else: self.d.rectangle(box, fill=f, outline=o, width=round(width * S))

    def dot(self, x, y, r, fill=INK, outline=None, width=1):
        if self.alpha <= 0.01: return
        self.d.ellipse(((x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S), fill=rgba(fill, self.alpha) if fill else None,
                       outline=rgba(outline, self.alpha) if outline else None, width=round(width * S))

    def wrap(self, x, y, s, kind, size, fill, maxw, lh=1.25, anchor="la"):
        words, lines, cur = s.split(), [], ""
        for w_ in words:
            t = (cur + " " + w_).strip()
            if self.tw(t, kind, size) <= maxw: cur = t
            else: lines.append(cur); cur = w_
        lines.append(cur)
        for i, l in enumerate(lines): self.text(x, y + i * size * lh, l, kind, size, fill, anchor)


def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease(x): x = clamp(x); return 0.5 - 0.5 * math.cos(math.pi * x)
def ramp(t, t0, t1): return clamp((t - t0) / max(t1 - t0, 1e-6))
def fade_in(t, t0, d=0.5): return ease(ramp(t, t0, t0 + d))
def fade_out(t, t0, d=0.5): return 1 - ease(ramp(t, t0, t0 + d))


# ---------------------------------------------------------------- cues from the Whisper clock
ORDER = [("im_tanmay", "im tanmay"), ("name", "tanmay kulkarni"), ("youd_lose", "youd lose"), ("about_half", "about half"),
         ("keep_group", "now keep the group"), ("take_away", "take away days"), ("sq_cal", "squeeze the calendar"), ("ninety_days", "ninety days"),
         ("ninety_five", "ninety five percent"), ("sq_month", "squeeze it to one month"), ("one_month", "one month"), ("almost", "almost certain"),
         ("decides", "so what decides it"), ("not_people", "not the people"), ("we_kept", "we kept them"), ("not_uneven", "not uneven birthdays"),
         ("tenth", "a tenth of a point"), ("its_days", "its how many days"), ("rule", "heres the rule"), ("sqrt", "take the square root"),
         ("mult", "multiply by one point two"), ("add", "add a half"), ("even_odds", "for even odds"), ("a_year", "a year needs"),
         ("p23", "twenty three people"), ("month_needs", "one month needs"), ("seven", "seven"), ("thats_why", "thats why"),
         ("its23", "its twenty three"), ("full_video", "the full video"), ("three_things", "three things you could change"),
         ("its_on", "its on humanitarians ai")]
FIRST_BIRTHDAY = ("share_birthday", "share a birthday")


def cues():
    tm = json.loads((HERE / "mp3" / "timings_short.json").read_text())
    ref, t = bm.times_for(tm); out = {}; pos = 0
    for key, phrase in [FIRST_BIRTHDAY] + ORDER:
        toks = [ma.norm(w) for w in phrase.split()]
        idx = next((i for i in range(pos, len(ref) - len(toks) + 1) if ref[i:i + len(toks)] == toks), None)
        assert idx is not None, f"cue not found in order: {phrase!r}"
        out[key] = round(float(t[idx]), 3); pos = idx + 1
    out["end_of_speech"] = round(max(w[2] for w in tm["words"]), 3); out["duration"] = tm["duration_s"]
    return out


# ---------------------------------------------------------------- the one scene
GX0, GY0, CELL, GAP, COLS, ROWS = 60, 420, 24, 3, 31, 12
ALL365 = bs.ALL365                                # (month, day) in calendar order, Feb 29 absent: 365 cells


def cell_center(idx):
    r, c = divmod(int(idx), COLS)
    # month rows have different lengths in the long film's grid; here the 365 days are laid out as a plain 31-wide sheet
    return GX0 + c * (CELL + GAP) + CELL / 2, GY0 + r * (CELL + GAP) + CELL / 2


# the group: the long film's seed-2701 random group of 23, reordered so its one shared pair lands last
_days, _ring = bs.draw_days(random.Random(2701), ALL365, 23, "one")
_idx = [ALL365.index(d) for d in _days]
_pair = [i for i, d in enumerate(_days) if d == _ring]
ORDER_DOTS = [i for i in range(23) if i not in _pair] + _pair
FRAC = [(_idx[i] + 0.5) / 365 for i in ORDER_DOTS]       # each dot's place in the year, kept as it narrows
RING_IDX = _idx[_pair[0]]


def dot_cells(Wk):
    return [min(int(f * Wk), int(Wk) - 1) for f in FRAC]


def dot_positions(Wk):
    cells = dot_cells(Wk); seen = {}; out = []
    for c in cells:
        k = seen.get(c, 0); seen[c] = k + 1
    count = dict(seen); seen2 = {}
    for c in cells:
        k = seen2.get(c, 0); seen2[c] = k + 1; n = count[c]; cx, cy = cell_center(c)
        if n == 1: ox, oy = 0, 0
        else:
            ang = 2 * math.pi * k / n + 0.5; rad = 5.0 if n <= 4 else 7.5; ox, oy = rad * math.cos(ang), rad * math.sin(ang)
        out.append((cx + ox, cy + oy))
    return out


POS = {Wk: dot_positions(Wk) for Wk in (365, 90, 30)}
HEADLINES = ["Two of these 23 share a day", "You'd lose about half the time", "Same 23 people. Fewer days.", "What decides it?",
             "The rule", "Try it", "That's why it's twenty three"]
SOURCES = ["Illustration: one random group of 23 (seed 2701). Not data.", "Our calculation: exact; 400,000 simulated groups agree.",
           "Our calculation: 23 people, days equally likely.", "Our calculation. US births: NCHS and SSA via FiveThirtyEight (CC BY 4.0).",
           "Checked against the exact answer for every day count from 2 to 2,000.", "Our calculation: 365 days give 23 people, 30 days give 7.", ""]


class Timeline:
    def __init__(self, c):
        self.c = c
        self.trans = [  # (t0, t1, W from, W to, key from, key to)
            (c["take_away"], c["ninety_days"] + 0.3, 365, 90, 365, 90),
            (c["sq_month"], c["one_month"] + 0.4, 90, 30, 90, 30),
            (c["even_odds"], c["a_year"] + 0.8, 30, 365, 30, 365),
            (c["month_needs"], c["seven"] + 0.4, 365, 30, 365, 30),
            (c["thats_why"] - 0.25, c["its23"] + 0.25, 30, 365, 30, 365)]
        self.head_t = [0, c["im_tanmay"], c["keep_group"], c["decides"], c["rule"], c["even_odds"], c["thats_why"]]
        self.dot_t0 = 0.30; self.dot_t1 = c["share_birthday"] + 0.45

    def state_W(self, t):
        Wv, key, p, last = 365.0, 365, 0.0, 365
        for t0, t1, a, b, ka, kb in self.trans:
            if t >= t1: Wv = float(b); last = b
            elif t > t0:
                p = ease(ramp(t, t0, t1)); Wv = a + (b - a) * p; return Wv, (ka, kb, p)
        return Wv, (last, last, 0.0)

    def dots(self, t):
        c = self.c; Wv, (ka, kb, p) = self.state_W(t); out = []
        for i in range(23):
            (xa, ya), (xb, yb) = POS[ka][i], POS[kb][i]; x, y = xa + (xb - xa) * p, ya + (yb - ya) * p
            a = 1.0
            if i < 21 + 2:                                        # landing in S01
                land = self.dot_t0 + (self.dot_t1 - self.dot_t0) * (i + 1) / 23
                a = ease(ramp(t, land - 0.35, land)); y -= (1 - a) * 46
            if i >= 7:                                             # 16 dots leave for "one month needs seven" and return at "that's why"
                a *= 1 - ease(ramp(t, c["month_needs"] + 0.25, c["seven"] + 0.3)) * (1 - ease(ramp(t, c["thats_why"] - 0.25, c["its23"] + 0.1)))
            out.append((x, y, a))
        return Wv, out


def scene(t, tl, c):
    cv = PCanvas()
    Wv, dots = tl.dots(t)
    # headline: cross-fades at each new line; the argument reads with the sound off
    for k, txt in enumerate(HEADLINES):
        a = fade_in(t, tl.head_t[k], 0.25) if k else 1.0
        if k + 1 < len(HEADLINES): a *= fade_out(t, tl.head_t[k + 1] - 0.18, 0.18)
        cv.alpha = a; cv.text(SAFE_L, 300, txt, "serif", 56, INK, "ls")
    cv.alpha = fade_in(t, c["name"], 0.5) * fade_out(t, c["rule"] - 0.3, 0.5) if True else 0
    cv.text(SAFE_L, 352, "Tanmay Kulkarni · Humanitarians AI", "sans", 32, INK_SOFT)
    # the calendar of possible birthdays: neutral at a full year, tinted inside the band when it narrows
    cv.alpha = 1.0; q = clamp((365 - Wv) / 25.0); lit = bs.mix(SPARK, PAGE, 0.78); dim = bs.mix(BORDER, PAGE, 0.62)
    for idx in range(365):
        w_in = clamp(Wv - idx)
        target = bs.mix(dim, lit, w_in)
        col = bs.mix(BORDER, target, q); r, cc = divmod(idx, COLS)
        cv.rect(GX0 + cc * (CELL + GAP), GY0 + r * (CELL + GAP), GX0 + cc * (CELL + GAP) + CELL, GY0 + r * (CELL + GAP) + CELL, fill=col, r=3)
    cv.alpha = 1.0
    cv.text(SAFE_L, 790, f"possible birthdays: {int(round(Wv))}", "sans", 34, INK_SOFT)
    # sources: inside the safe area, one per phase
    for k, txt in enumerate(SOURCES):
        if not txt: continue
        a = fade_in(t, tl.head_t[k], 0.25) if k else 1.0
        if k + 1 < len(SOURCES): a *= fade_out(t, tl.head_t[k + 1] - 0.18, 0.18)
        cv.alpha = a; cv.wrap(SAFE_L, 838, txt, "sans", 30, INK_SOFT, SAFE_R - SAFE_L, 1.3)
    # the ring on the shared pair (a full year only), pulsing once on "you'd lose"
    cv.alpha = 1.0
    ring_a = clamp((Wv - 300) / 65) * fade_in(t, tl.dot_t1 - 0.5, 0.4)
    if ring_a > 0:
        pulse = 1.0
        for tp in (c["name"] + 1.5, c["youd_lose"], c["its_on"] + 1.0):
            if tp <= t <= tp + 0.9: pulse = 1 + 0.55 * math.sin(math.pi * clamp((t - tp) / 0.9))
        cx, cy = cell_center(RING_IDX); cv.alpha = ring_a; cv.dot(cx, cy, 17 * pulse, fill=None, outline=SPARK, width=3)
    for (x, y, a) in dots:
        cv.alpha = a; cv.dot(x, y, 7.5, fill=INK)
    # the odds counter
    cnt_a = fade_in(t, c["about_half"], 0.6) * fade_out(t, c["rule"] - 0.2, 0.5) + fade_in(t, c["its23"] + 0.4, 0.6) * (1 if t >= c["its23"] + 0.4 else 0)
    if cnt_a > 0:
        p = pm(23, max(1, int(round(Wv)))); cv.alpha = clamp(cnt_a)
        if p >= 0.99995: cv.text(SAFE_L, 930, "above", "sans", 40, INK_SOFT); s_ = "99.99%"
        else: s_ = f"{p * 100:.2f}%" if p > 0.995 else f"{p * 100:.1f}%"
        pul = max(math.sin(math.pi * clamp((t - tp) / 0.8)) for tp in (c["ninety_five"], c["almost"]))
        cv.text(SAFE_L, 1160, s_, "serif", int(240 * (1 + 0.06 * pul)), bs.mix(SEND, "#7A3419", pul * 0.8), "ls")      # a visible swell on the number as it is said
        la = cnt_a * fade_out(t, c["decides"] - 0.3, 0.4) * (1 if t < c["thats_why"] else 0)
        cv.alpha = clamp(la); cv.wrap(SAFE_L, 1190, "of random groups of 23 have a shared birthday", "sans", 34, INK, SAFE_R - SAFE_L, 1.25)
    # S04: three rows, one per phrase; DAYS ringed as the one that moved it
    rows = [("PEOPLE", "23, kept", c["not_people"], c["we_kept"]), ("EVENNESS", "+0.1 point at most", c["not_uneven"], c["tenth"]),
            ("DAYS", "365 → 30", c["its_days"], c["its_days"] + 0.45)]
    row_vis = fade_out(t, c["rule"] - 0.2, 0.5)
    for i, (lab, val, t_lab, t_val) in enumerate(rows):
        y = 1275 + i * 56
        cv.alpha = fade_in(t, t_lab, 0.4) * row_vis; cv.text(SAFE_L, y, lab, "sansm", 32, INK_SOFT)
        cv.alpha = fade_in(t, t_val, 0.4) * row_vis; cv.text(330, y - 3, val, "serif", 40, INK)
    cv.alpha = fade_in(t, c["its_days"] + 0.1, 0.4) * row_vis
    cv.rect(SAFE_L - 16, 1275 + 112 - 8, 640, 1275 + 112 + 48, outline=SPARK, width=3, r=10)
    # S05-S06: the rule, typeset in the order it is spoken
    m = bs.Math(cv, 74); items = bs.rule_items(m); xs = [SAFE_L]
    for it in items: xs.append(xs[-1] + it[-1])
    # parts: 0 n,1 ≈,2 round,3 (,4 1.2,5 ×,6 √d,7 +,8 ½,9 )
    appear = {6: c["sqrt"], 4: c["mult"], 5: c["mult"], 7: c["add"], 8: c["add"], 0: c["add"] + 0.5, 1: c["add"] + 0.5, 2: c["add"] + 0.5, 3: c["add"] + 0.5, 9: c["add"] + 0.5}
    rule_vis = fade_out(t, c["thats_why"] + 0.45, 0.55)      # the "30 days give 7" line stays readable for 1.5 s+
    for i, it in enumerate(items):
        cv.alpha = fade_in(t, appear[i], 0.45) * rule_vis
        if cv.alpha > 0: m.draw(xs[i], 1160, [it], INK)
    leg = fade_in(t, c["add"] + 0.9, 0.5) * rule_vis
    cv.alpha = leg; cv.text(SAFE_L, 1235, "d = possible birthdays", "sans", 32, INK_SOFT); cv.text(SAFE_L, 1280, "n = people for even odds (a 50% chance)", "sans", 32, INK_SOFT)
    cv.alpha = fade_in(t, c["p23"] - 0.2, 0.45) * rule_vis; cv.text(SAFE_L, 1366, "365 days → 23 people", "serif", 52, INK, "ls")
    cv.alpha = fade_in(t, c["seven"] - 0.2, 0.45) * rule_vis; cv.text(SAFE_L, 1424, "30 days → 7 people", "serif", 52, SPARK, "ls")
    # S07: the closing text over the restored opening scene; the exact title is searchable
    cv.alpha = fade_in(t, c["full_video"], 0.5); cv.text(SAFE_L, 1285, "The full video. Search:", "sans", 34, INK_SOFT, "ls")
    cv.alpha = fade_in(t, c["three_things"] - 1.2, 0.5); cv.text(SAFE_L, 1340, "The Birthday Paradox:", "serifm", 46, INK, "ls")
    cv.alpha = fade_in(t, c["three_things"], 0.5); cv.text(SAFE_L, 1392, "Three Things You Could Change", "serifm", 46, INK, "ls")
    cv.alpha = fade_in(t, c["its_on"], 0.5); cv.text(SAFE_L, 1432, "Humanitarians AI", "sans", 34, INK_SOFT, "ls")
    cv.alpha = 1.0
    return cv


def frame_png(args):
    n, c = args; tl = Timeline(c); t = n / FPS
    cv = scene(t, tl, c); (HERE / "_frames").mkdir(exist_ok=True)
    cv.im.convert("RGB").save(HERE / "_frames" / f"f{n:05d}.png", compress_level=1)
    return n


if __name__ == "__main__":
    a = sys.argv[1:]; c = cues()
    if "--cues" in a:
        (HERE / "_video").mkdir(exist_ok=True); (HERE / "_video" / "cues.json").write_text(json.dumps(c, indent=1))
        for k, v in c.items(): print(f"{k:14s} {v:7.2f}")
    if "--render" in a:
        c = json.loads((HERE / "_video" / "cues.json").read_text()); n = math.ceil(c["duration"] * FPS)
        only = [int(x) for x in a if x.isdigit()]
        with Pool(6) as pool:
            for k, _ in enumerate(pool.imap_unordered(frame_png, [(i, c) for i in (only or range(n))], chunksize=8)):
                if k % 200 == 0: print("frames", k, "/", len(only or range(n)), flush=True)
    if "--encode" in a:
        c = json.loads((HERE / "_video" / "cues.json").read_text()); (HERE / "_video").mkdir(exist_ok=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(HERE / "_frames" / "f%05d.png"), "-c:v", "libx264",
                        "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(HERE / "_video" / "short-silent.mp4")], check=True)
        print("encoded")
