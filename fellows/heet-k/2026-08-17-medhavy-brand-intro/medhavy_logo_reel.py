"""
medhavy_logo_reel.py  —  PNG-based Medhavy logo reel. 16:9, SILENT; assemble.py muxes
the voiceover. STRUCTURE: 16 segments, one per cleaned logo (medhavy-01..16). The
3-line voiceover ("Medhavy. / Intelligent Textbooks. / www.Medhavy.com", voice
1sgY6Voq1aexKOB1IJ2D) REPLAYS every segment (reuse_audio in the beat sheet) — the
logos are NOT stacked; each gets its own moment. Length = per-logo segment × 16.

Each logo is CONSTRUCTED by tile assembly (assets/png/tiles/<name>/) with a DIFFERENT
fly-in pattern per segment (scatter, sweep, spiral, explode, zoom, rotate, …). MEDHAVY
appears below in Montserrat Bold, all caps, ~0.28em tracking, then the tagline and URL.

Run:
    ai
    python ../../bears-doodles/scripts/generate_audio.py .   # silence + reuse, no new API calls
    manim -qh medhavy_logo_reel.py BearsDoodlesVideo
    python ../../bears-doodles/scripts/assemble.py . --mode manim
"""
import json
from pathlib import Path

import numpy as np
from manim import *

try:
    import manimpango
except Exception:
    manimpango = None

HERE = Path(__file__).resolve().parent
PNG = HERE / "assets" / "png"
TILES = PNG / "tiles"
FONTS = HERE / "assets" / "fonts"

INK    = "#15151c"
ACCENT = "#2A6FB0"
FONT   = "Montserrat"
HEROH  = 3.0
CENTER_UP = np.array([0.0, 0.65, 0.0])
WORD_Y = -2.45
SUB_Y  = -3.05
NSEG = 16

if manimpango is not None:
    for _f in ("Montserrat-Bold.ttf", "Montserrat-Medium.ttf", "Montserrat-Regular.ttf"):
        try:
            manimpango.register_font(str(FONTS / _f))
        except Exception:
            pass

_META = json.loads((TILES / "meta_all.json").read_text())
_tp = HERE / "mp3" / "timings.json"
_T = json.loads(_tp.read_text()) if _tp.exists() else {}
_FB_SIL = {"build": 2.2, "out": 0.6}
_FB_SAY = {"name": 1.02, "tag": 1.38, "url": 2.12}


def dur(bid):
    if bid in _T:
        return float(_T[bid])
    kind = bid.split("_")[-1]
    return float(_FB_SIL.get(kind, _FB_SAY.get(kind, 1.5)))


def load_png(name, height=HEROH, center=CENTER_UP):
    m = ImageMobject(str(PNG / f"{name}.png"))
    m.height = height
    m.move_to(center)
    return m


def tracked_text(text, fs, color, weight="BOLD", track=0.28):
    words, em = [], fs / 100.0
    for w in text.split(" "):
        letters = VGroup(*[Text(c, font=FONT, weight=weight, font_size=fs, color=color) for c in w])
        em = max((l.height for l in letters), default=fs / 100.0) / 0.7
        letters.arrange(RIGHT, buff=track * em)
        words.append(letters)
    return VGroup(*words).arrange(RIGHT, buff=track * em * 3.2)


def accent_nodes(ref, n=6, r=0.055, seed=3):
    rng = np.random.default_rng(seed)
    w, h = ref.width, ref.height
    c = ref.get_center()
    return VGroup(*[Dot([c[0] + rng.uniform(-0.4, 0.4) * w,
                         c[1] + rng.uniform(-0.4, 0.4) * h, 0], radius=r, color=ACCENT)
                    for _ in range(n)])


def _start_state(p, r, c, rows, cols, fc, rng):
    """Return (start_xy, scale0, rot0, order) for tile (r,c) under pattern p."""
    cx, cy = fc[0], fc[1]
    s0, rot, order = 1.0, 0.0, float(r * cols + c)
    cux, cuy = CENTER_UP[0], CENTER_UP[1]
    p %= 16
    if p == 0:      # scatter
        a = rng.uniform(0, TAU); rad = rng.uniform(2.2, 4.0)
        start = (cx + rad*np.cos(a), cy + rad*np.sin(a)); order = rng.random()
    elif p == 1:    start = (cx - 6, cy); order = float(c)
    elif p == 2:    start = (cx + 6, cy); order = float(cols - c)
    elif p == 3:    start = (cx, cy + 5); order = float(r)
    elif p == 4:    start = (cx, cy - 5); order = float(rows - r)
    elif p == 5:    start = (cx, cy); order = float(r * cols + c)              # fade grid
    elif p == 6:    start = (cx, cy); s0 = 0.12; order = rng.random()          # zoom each
    elif p == 7:                                                              # spiral
        start = (cux + (cx-cux)*1.6, cuy + (cy-cuy)*1.6)
        order = float(np.arctan2(cy-cuy, cx-cux) % TAU)
    elif p == 8:    start = (cux, cuy); s0 = 0.2; order = float(np.hypot(cx-cux, cy-cuy))   # explode
    elif p == 9:    start = (cx + (cx-cux)*2, cy + (cy-cuy)*2); order = float(-np.hypot(cx-cux, cy-cuy))  # implode
    elif p == 10:   start = (cx - 2, cy + 2); order = float(r + c)            # diagonal
    elif p == 11:   start = (cx, cy); rot = PI/4; order = rng.random()        # rotate each
    elif p == 12:   start = (cx, cy); order = float(((r + c) % 2) * 1000 + r*cols + c)  # checker
    elif p == 13:   start = (cx, cy - 1.6); order = rng.random()              # rise + fade
    elif p == 14:   start = (cx - 4, cy); order = float(c * 100 + r)          # columns sweep
    else:           start = (cx, cy + 4); order = float(r * 100 + c)          # rows sweep
    return start, s0, rot, order


class BearsDoodlesVideo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.rng = np.random.default_rng(7)
        for i in range(1, NSEG + 1):
            self._segment(i)

    def _segment(self, i):
        png = f"medhavy-{i:02d}"
        p = (i - 1)
        # ── build: tile assembly ─────────────────────────────────────────────
        hero, nodes = self._assemble(png, p, dur(f"s{i:02d}_build"))
        # ── name: MEDHAVY wordmark cascades in ───────────────────────────────
        t = dur(f"s{i:02d}_name")
        word = tracked_text("MEDHAVY", 44, INK, "BOLD").move_to([0, WORD_Y, 0])
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.12) for l in word[0]],
                              lag_ratio=0.06), run_time=max(0.5, t))
        # ── tag ──────────────────────────────────────────────────────────────
        t = dur(f"s{i:02d}_tag")
        tag = tracked_text("INTELLIGENT TEXTBOOKS", 22, ACCENT, "MEDIUM").move_to([0, SUB_Y, 0])
        self.play(FadeIn(tag, shift=UP * 0.1), Indicate(nodes, color=ACCENT, scale_factor=1.2),
                  run_time=max(0.5, t))
        # ── url ──────────────────────────────────────────────────────────────
        t = dur(f"s{i:02d}_url")
        url = Text("www.Medhavy.com", font=FONT, weight="MEDIUM", font_size=30, color=INK).move_to([0, SUB_Y, 0])
        self.play(FadeOut(tag, shift=DOWN * 0.1), run_time=t * 0.28)
        self.play(Write(url), run_time=t * 0.72)
        # ── out: clear for next ──────────────────────────────────────────────
        t = dur(f"s{i:02d}_out")
        self.play(FadeOut(hero), FadeOut(nodes), FadeOut(word), FadeOut(url), run_time=max(0.3, t))

    def _assemble(self, png, pattern, t):
        meta = _META[png]
        W, H = meta["w"], meta["h"]
        rows, cols = meta["rows"], meta["cols"]
        disp_w = HEROH * (W / H)
        sx = disp_w / W
        left = CENTER_UP[0] - disp_w / 2
        top = CENTER_UP[1] + HEROH / 2
        items = []
        for ti in meta["tiles"]:
            m = ImageMobject(str(TILES / png / f"{ti['r']}_{ti['c']}.png"))
            tw = (ti["x1"] - ti["x0"]) * sx
            if m.width > 1e-6:
                m.width = tw
            fc = np.array([left + ((ti["x0"] + ti["x1"]) / 2) * sx,
                           top - ((ti["y0"] + ti["y1"]) / 2) * sx, 0.0])
            (sxp, syp), s0, rot, order = _start_state(pattern, ti["r"], ti["c"], rows, cols, fc, self.rng)
            if s0 != 1.0:
                m.scale(s0)
            if rot != 0.0:
                m.rotate(rot)
            m.move_to([sxp, syp, 0]).set_opacity(0.0)
            items.append((order, m, fc, s0, rot))
        items.sort(key=lambda z: z[0])
        grp = Group(*[it[1] for it in items])
        anims = []
        for order, m, fc, s0, rot in items:
            a = m.animate.move_to(fc).set_opacity(1.0)
            if s0 != 1.0:
                a = a.scale(1.0 / s0)
            if rot != 0.0:
                a = a.rotate(-rot)
            anims.append(a)
        self.play(LaggedStart(*anims, lag_ratio=0.05), run_time=t * 0.82)
        # settle to a single clean image; pulse accent nodes
        hero = load_png(png, HEROH)
        nodes = accent_nodes(hero)
        self.add(hero)
        self.remove(grp)
        self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in nodes], lag_ratio=0.1),
                  run_time=t * 0.18)
        return hero, nodes
