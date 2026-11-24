"""short/scenes.py -- native 9:16 Manim scenes for "How an AI Sells a Big Order" (Short).

Its own layout, never a crop of the 16:9: frame 4.5 x 8 units, content between y = 3.3 and
y = -2.5, centred near x = -0.15. Same house look and the same receipts: every number is
read at render time from ../code/results.json (numpy, seed-locked, run twice -> identical).
Timing from this folder's beat_sheet.json (measured narration once audio exists).
"""
from manim import *
from pathlib import Path
import json

config.frame_width = 4.5
config.frame_height = 8.0

_SHORT = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-22-ai-sells-a-big-order/short")
HERE = Path(__file__).resolve().parent
if not (HERE / "beat_sheet.json").is_file() or not (HERE.parent / "code" / "results.json").is_file():
    HERE = _SHORT                                         # Gate A/W run an isolated copy

RES = json.loads((HERE.parent / "code" / "results.json").read_text())
STRAT = RES["strategies"]
PAR = RES["params"]
BEATS = {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}

BG = "#FAF9F5"; INK = "#2B2A26"; MUTED = "#6F6A5E"; PANEL = "#EEEADF"
DARK = "#2B2A26"; ON_DARK = "#F5F1E8"; ACCENT = "#A64B2A"; TEAL = "#1F4E5F"
GHOST = "#A39A88"; GHOST_DARK = "#5E544C"; DARK_PANEL = "#3A3833"; MUTED_DARK = "#C9C1B1"
SERIF = "EB Garamond"; SANS = "Inter"; MONO = "JetBrains Mono"
LX, RX = -1.9, 1.7                                       # content band, x
CX = (LX + RX) / 2


def T(s, size=40, color=INK, font=SANS, weight="NORMAL"):
    """Create large, then scale down (portrait type stays crisp at 2160 x 3840)."""
    return Text(s, font=font, font_size=size * 0.72 * 4, color=color, weight=weight).scale(1 / 4)


def comma(n):
    return f"{int(round(n)):,}"


def dur(bid):
    b = BEATS[bid]
    return float(b.get("actual_duration_s") or b["estimated_duration_s"])


def cue(bid, phrase):
    text = BEATS[bid]["narration_text"]
    i = text.find(phrase)
    if i < 0:
        raise ValueError(f"{bid}: cue phrase not in narration: {phrase!r}")
    return dur(bid) * i / len(text)


class Clock:
    def __init__(self, scene, bid, bg=BG):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.DUR = dur(bid)
        scene.camera.background_color = bg

    def run(self, *anims, rt=0.8):
        self.s.play(*anims, run_time=rt)
        self.t += rt

    def until(self, phrase):
        at = cue(self.bid, phrase)
        if at > self.t + 0.04:
            self.s.wait(at - self.t)
            self.t = at

    def pad(self):
        self.s.wait(max(0.1, self.DUR - self.t))


def header(kicker, title, dark=False):
    k = T(kicker, 30, MUTED_DARK if dark else MUTED, MONO, "BOLD")
    h = T(title, 44, ON_DARK if dark else INK, SERIF)
    g = VGroup(k, h).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
    g.move_to([LX, 3.3, 0], aligned_edge=UL)
    return g


def card(w, h, color=PANEL):
    return RoundedRectangle(corner_radius=0.12, width=w, height=h, fill_color=color,
                            fill_opacity=1, stroke_width=0)


def bar(x_center, base_y, width, height, color=TEAL):
    r = Rectangle(width=width, height=max(height, 0.01), fill_color=color, fill_opacity=1,
                  stroke_width=0)
    r.move_to([x_center, base_y + max(height, 0.01) / 2, 0])
    return r


def tag():
    t = T("SYNTHETIC MARKET", 28, ACCENT, MONO, "BOLD")
    box = card(t.width + 0.3, t.height + 0.2)
    t.move_to(box.get_center())
    return VGroup(box, t)


# ── B20: all at once vs equal slices ──────────────────────────────────────────
class B20_Problem(Scene):
    def construct(self):
        c = Clock(self, "B20")
        X, S0, ETA = PAR["X"], PAR["S0"], PAR["eta"]
        head = header("THE PROBLEM", "Sell 10,000 shares")
        tg = tag().move_to([LX, 2.0, 0], aligned_edge=LEFT)

        # A: all at once
        a_box = card(RX - LX, 1.7).move_to([CX, 0.88, 0])
        big = bar(LX + 0.4, 0.13, 0.42, 1.5, ACCENT)
        a1 = T("all at once", 40, INK, SERIF).move_to([LX + 0.9, 1.45, 0], aligned_edge=LEFT)
        a2 = T(f"${S0:.2f} → ${S0 - ETA * X:.2f}", 30, INK).move_to([LX + 0.9, 0.82, 0],
                                                              aligned_edge=LEFT)
        a2.shift(UP * 0.1)
        a3 = T(f"cost {STRAT['dump']['mean_bps']:.0f} bps", 36, ACCENT, SANS, "BOLD").move_to(
            [LX + 0.9, 0.42, 0], aligned_edge=LEFT)

        # B: equal slices + price fan
        paths = RES["sample_days"]["price_paths"]
        worst = RES["sample_days"]["worst_twap_day"]
        b1 = T("equal slices", 40, INK, SERIF).move_to([LX, -0.25, 0], aligned_edge=LEFT)
        base = -2.45
        step = (RX - LX) / 10
        slices = VGroup(*[bar(LX + step * (k + 0.5), base, step * 0.6, 0.3) for k in range(10)])
        lo = min(min(p) for p in paths); hi = max(max(p) for p in paths)
        span = max(hi - S0, S0 - lo) + 0.05
        ym, yh = -1.6, 0.42

        def P(k, v):
            return [LX + step * k, ym + (v - S0) / span * yh, 0]

        fan = VGroup()
        for i, p in enumerate(paths):
            if i != worst:
                m = VMobject(stroke_color=TEAL, stroke_width=2, stroke_opacity=0.5)
                m.set_points_as_corners([P(k, v) for k, v in enumerate(p)])
                fan.add(m)
        bad = VMobject(stroke_color=ACCENT, stroke_width=5)
        bad.set_points_as_corners([P(k, v) for k, v in enumerate(paths[worst])])
        b2 = T("the price can drift", 30, ACCENT, SANS, "BOLD").move_to([LX, -0.7, 0], aligned_edge=LEFT)
        ghosts = VGroup(*[Rectangle(width=step * 0.6, height=0.3, stroke_color=GHOST, stroke_width=2)
                          .move_to([LX + step * (k + 0.5), base + 0.15, 0]) for k in range(10)])
        fan_frame = Rectangle(width=RX - LX, height=2 * yh + 0.1, stroke_color=GHOST, stroke_width=2)
        fan_frame.move_to([CX, ym, 0])

        self.add(head, tg, a_box, ghosts, fan_frame)
        c.until("at once")
        c.run(GrowFromEdge(big, DOWN), FadeIn(a1), rt=0.9)
        c.until("you push")
        c.run(FadeIn(a2), rt=0.6)
        c.until("that costs")
        c.run(FadeIn(a3, shift=UP * 0.1), rt=0.6)
        c.until("equal slices")
        c.run(FadeIn(b1), FadeOut(ghosts), LaggedStart(*[GrowFromEdge(s, DOWN) for s in slices], lag_ratio=0.1),
              rt=1.0)
        c.run(Create(fan, lag_ratio=0.01), rt=1.1)
        c.until("drift")
        c.run(Create(bad), FadeIn(b2), rt=0.8)
        c.pad()


# ── B30: what the agent learned ───────────────────────────────────────────────
class B30_Schedule(Scene):
    def construct(self):
        c = Clock(self, "B30")
        rl = STRAT["rl"]["schedule"]
        ac = RES["ac"]["n"]
        head = header("WHAT IT LEARNED", "Sell early, taper off")
        days = T(f"{PAR['episodes'] // 1_000_000}M practice runs", 32, ACCENT, SANS, "BOLD").move_to(
            [LX, 2.05, 0], aligned_edge=LEFT)
        fbox = card(RX - LX, 0.95).move_to([CX, 1.2, 0])
        formula = SVGMobject(str(HERE / "assets" / "ac-formula-ink.svg")).scale_to_fit_width(3.1)
        formula.move_to(fbox.get_center())

        base, top, ymax = -1.85, 0.45, 3000.0
        slot = (RX - LX) / 10

        def Y(v):
            return base + v / ymax * (top - base)

        axis = Line([LX, base, 0], [RX, base, 0], color=INK, stroke_width=3)
        ghosts = VGroup(*[Rectangle(width=slot * 0.62, height=Y(1000) - base, stroke_color=GHOST,
                                    stroke_width=2).move_to([LX + slot * (k + 0.5), (base + Y(1000)) / 2, 0])
                          for k in range(10)])
        bars = VGroup(*[bar(LX + slot * (k + 0.5), base, slot * 0.62, Y(v) - base) for k, v in enumerate(rl)])
        dots = VGroup(*[Dot([LX + slot * (k + 0.5), Y(v), 0], radius=0.065, color=ACCENT) for k, v in enumerate(ac)])
        link = VMobject(stroke_color=ACCENT, stroke_width=2.5).set_points_as_corners(
            [[LX + slot * (k + 0.5), Y(v), 0] for k, v in enumerate(ac)])
        lg1 = VGroup(Square(0.2, fill_color=TEAL, fill_opacity=1, stroke_width=0),
                     T("agent", 30, INK)).arrange(RIGHT, buff=0.12)
        lg2 = VGroup(Dot(radius=0.08, color=ACCENT), T("formula", 30, INK)).arrange(RIGHT, buff=0.12)
        lg = VGroup(lg1, lg2).arrange(RIGHT, buff=0.4).move_to([CX, -2.25, 0])

        self.add(head, axis, ghosts, fbox)
        c.until("practiced")
        c.run(FadeIn(days), FadeIn(formula), rt=0.6)
        c.until("sell")
        c.run(FadeOut(ghosts), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.15), FadeIn(lg1),
              rt=1.6)
        c.until("close to")
        c.run(LaggedStart(*[FadeIn(d, shift=DOWN * 0.2) for d in dots], lag_ratio=0.08), FadeIn(lg2), rt=1.0)
        c.run(Create(link), rt=0.6)
        c.pad()


# ── B40: held-out costs ───────────────────────────────────────────────────────
class B40_Costs(Scene):
    def construct(self):
        c = Clock(self, "B40")
        head = header(f"{comma(PAR['test_days'])} NEW DAYS", "Cost, in basis points")
        w = RX - LX

        def X_(b):
            return LX + b / 100 * w

        rows = [("All at once", "dump", 1.55), ("Equal slices", "twap", 0.05), ("The agent", "rl", -1.45)]
        items = []
        for label, key, y in rows:
            s = STRAT[key]
            lab = T(label, 40, INK, SERIF).move_to([LX, y + 0.5, 0], aligned_edge=LEFT)
            lane = Rectangle(width=w, height=0.46, fill_color=PANEL, fill_opacity=1, stroke_width=0).move_to([CX, y, 0])
            b = Rectangle(width=max(0.02, X_(s["mean_bps"]) - LX), height=0.46, fill_color=TEAL, fill_opacity=1,
                          stroke_width=0)
            b.move_to([LX + b.width / 2, y, 0])
            if key == "dump":
                val = T(f"{s['mean_bps']:.0f} every day", 32, ON_DARK, SANS, "BOLD").move_to([RX - 0.12, y, 0],
                                                                                         aligned_edge=RIGHT)
                extra = VGroup()
            else:
                val = T(f"{s['mean_bps']:.0f} avg", 30, INK, SANS, "BOLD").next_to(b, RIGHT, buff=0.1)
                col = ACCENT if key == "rl" else INK
                tick = Line([X_(s["p95_bps"]), y - 0.32, 0], [X_(s["p95_bps"]), y + 0.32, 0], color=col,
                            stroke_width=6)
                tl = T(f"bad day {s['p95_bps']:.0f}", 32, col, SANS, "BOLD").move_to([X_(s["p95_bps"]), y - 0.55, 0])
                extra = VGroup(tick, tl)
            items.append((lab, lane, b, val, extra))
        ax = Line([LX, -2.3, 0], [RX, -2.3, 0], color=INK, stroke_width=3)
        a0 = T("0", 28, MUTED).move_to([LX + 0.1, -2.52, 0])
        a1 = T("100 bps", 28, MUTED).move_to([RX - 0.3, -2.52, 0])

        self.add(head, ax, a0, a1)
        for it in items:
            self.add(it[1])
        c.run(*[FadeIn(it[0]) for it in items], rt=0.5)
        c.until("averaged")
        for lab, lane, b, val, extra in items:
            c.run(GrowFromEdge(b, LEFT), FadeIn(val), rt=0.55)
        c.until("bad days")
        c.run(*[FadeIn(it[4]) for it in items], rt=0.8)
        c.pad()


# ── B50: dark takeaway ────────────────────────────────────────────────────────
class B50_Takeaway(Scene):
    def construct(self):
        c = Clock(self, "B50", bg=DARK)
        head = header("TAKEAWAY", "Impact versus risk", dark=True)
        fx, fy = CX, 0.55
        fulcrum = Triangle(fill_color=GHOST_DARK, fill_opacity=1, stroke_width=0).scale(0.3).move_to([fx, fy - 0.2, 0])
        beam = Line([fx - 1.7, fy + 0.1, 0], [fx + 1.7, fy + 0.1, 0], color=ON_DARK, stroke_width=7)
        lp = card(1.45, 0.62, DARK_PANEL).move_to([fx - 1.2, fy + 0.6, 0])
        rp = card(1.45, 0.62, DARK_PANEL).move_to([fx + 1.2, fy + 0.6, 0])
        lt = T("impact", 36, ON_DARK, SERIF).move_to(lp.get_center())
        rt_ = T("risk", 36, ON_DARK, SERIF).move_to(rp.get_center())
        sg = VGroup(beam, lp, rp, lt, rt_)
        pivot = [fx, fy + 0.1, 0]
        cb = card(RX - LX, 2.25, DARK_PANEL).move_to([CX, -1.4, 0])
        cg = Rectangle(width=RX - LX, height=2.25, stroke_color=GHOST_DARK, stroke_width=2).move_to([CX, -1.4, 0])
        c1 = T("Synthetic market only", 40, ON_DARK, SERIF).move_to([LX + 0.2, -0.6, 0], aligned_edge=LEFT)
        c2 = T("Real ones add:", 30, MUTED_DARK).move_to([LX + 0.2, -1.05, 0], aligned_edge=LEFT)
        c3 = VGroup(*[T("+ " + w, 30, ON_DARK).move_to([LX + 0.3, y, 0], aligned_edge=LEFT)
                      for w, y in (("order books", -1.45), ("other traders", -1.85), ("price jumps", -2.25))])
        self.add(head, fulcrum, cg)
        c.run(FadeIn(sg), rt=0.4)
        c.until("impact versus risk")
        c.run(Rotate(sg, angle=-0.15, about_point=pivot), rt=0.7)
        c.run(Rotate(sg, angle=0.15, about_point=pivot), rt=0.7)
        c.until("synthetic market")
        c.run(FadeIn(cb), FadeOut(cg), FadeIn(c1), FadeIn(c2), FadeIn(c3), rt=0.7)
        c.pad()


# ── B90: outro ────────────────────────────────────────────────────────────────
class B90_Outro(Scene):
    def construct(self):
        c = Clock(self, "B90")
        title = VGroup(T("How an AI Sells", 56, INK, SERIF), T("a Big Order", 56, INK, SERIF)).arrange(
            DOWN, buff=0.08).move_to([CX, 2.75, 0])
        logo = ImageMobject(str(HERE / "assets" / "hai-logo-1-ink.png")).scale_to_fit_height(0.85)
        handle = T("@HumanitariansAI", 40, INK, SERIF)
        brand = Group(logo, handle).arrange(DOWN, buff=0.16).move_to([CX, 1.15, 0])
        pt = T("SUBSCRIBE", 40, ON_DARK, SANS, "BOLD")
        pill = RoundedRectangle(corner_radius=0.28, width=pt.width + 0.7, height=0.6, fill_color=ACCENT,
                                fill_opacity=1, stroke_width=0)
        pg = VGroup(pill, pt).move_to([CX, -0.05, 0])
        pt.move_to(pill.get_center())
        cr = VGroup(T("Boopesh M.", 32, INK), T("Humanitarians AI Fellow", 28, MUTED), T("Brutalist team", 28, MUTED),
                    T("Narration: AI voice", 28, MUTED), T("(Kokoro am_onyx)", 28, MUTED),
                    T("Data: synthetic market", 28, MUTED)).arrange(DOWN, buff=0.07).move_to([CX, -1.55, 0])
        self.add(title)
        c.run(FadeIn(logo, shift=UP * 0.15), FadeIn(handle), FadeIn(cr), rt=0.6)
        c.until("Subscribe")
        c.run(FadeIn(pg, scale=1.12), rt=0.4)
        c.pad()
