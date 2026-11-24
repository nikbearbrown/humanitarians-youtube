"""scenes.py -- Manim scenes for "How an AI Sells a Big Order" (16:9, Boopesh M.).

House look: cream ground, serif headline top-left under a small mono kicker, PANEL cards,
teal data bars, the accent for the one number that matters, one dark takeaway beat (B70),
Manim outro with SUBSCRIBE pill + HAI mark (B90).

THE RECEIPT: every number and chart here is read at render time from code/results.json,
written by code/execution_rl.py (numpy, seed-locked, run twice -> identical). Nothing
is typed in by hand except the setup the code was given (10,000 shares, $50, 10 steps).

TIMING: a beat's length is its measured narration (actual_duration_s in beat_sheet.json;
estimated_duration_s until audio exists). Cues sit at a phrase's character position in
that beat's narration_text, scaled to the beat length, so regenerated audio re-times the
scenes without hand edits. Scene classes are plain `BXX_Name(Scene)` (run.sh greps them).
"""
from manim import *
from pathlib import Path
import json

_REEL = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-22-ai-sells-a-big-order")
HERE = Path(__file__).resolve().parent
if not (HERE / "code" / "results.json").is_file():      # Gate A/W run an isolated copy
    HERE = _REEL

RES = json.loads((HERE / "code" / "results.json").read_text())
STRAT = RES["strategies"]
PAR = RES["params"]
BEATS = {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}

BG = "#FAF9F5"; INK = "#2B2A26"; MUTED = "#6F6A5E"; PANEL = "#EEEADF"
DARK = "#2B2A26"; ON_DARK = "#F5F1E8"; ACCENT = "#A64B2A"; TEAL = "#1F4E5F"
GHOST = "#A39A88"; GHOST_DARK = "#5E544C"; DARK_PANEL = "#3A3833"; MUTED_DARK = "#C9C1B1"
SERIF = "EB Garamond"; SANS = "Inter"; MONO = "JetBrains Mono"


# ── type ──────────────────────────────────────────────────────────────────────
def T(s, size=30, color=INK, font=SANS, weight="NORMAL"):
    """Text built at 4x and scaled down (cleaner glyph outlines, same final size)."""
    return Text(s, font=font, font_size=size * 4, color=color, weight=weight).scale(0.25)


def comma(n):
    return f"{int(round(n)):,}"


# ── timing ────────────────────────────────────────────────────────────────────
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
    """`c = Clock(self, "B20")`; `c.until(phrase)` waits for a cue; `c.pad()` holds to the end."""

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


# ── shared pieces ─────────────────────────────────────────────────────────────
def header(kicker, title, dark=False):
    k = T(kicker, 24, MUTED_DARK if dark else MUTED, MONO, "BOLD")
    h = T(title, 54, ON_DARK if dark else INK, SERIF)
    g = VGroup(k, h).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    g.to_corner(UL, buff=0.85)
    return g


def synthetic_tag():
    t = T("SYNTHETIC MARKET", 22, ACCENT, MONO, "BOLD")
    box = RoundedRectangle(corner_radius=0.1, width=t.width + 0.4, height=t.height + 0.28,
                           fill_color=PANEL, fill_opacity=1, stroke_width=0)
    t.move_to(box.get_center())
    g = VGroup(box, t)
    g.to_corner(UR, buff=0.85)
    return g


def card(w, h, color=PANEL):
    return RoundedRectangle(corner_radius=0.16, width=w, height=h, fill_color=color,
                            fill_opacity=1, stroke_width=0)


def bar(x_center, base_y, width, height, color=TEAL):
    r = Rectangle(width=width, height=max(height, 0.01), fill_color=color, fill_opacity=1,
                  stroke_width=0)
    r.move_to([x_center, base_y + max(height, 0.01) / 2, 0])
    return r


# ── B20: one big sale walks the price down ────────────────────────────────────
class B20_Impact(Scene):
    def construct(self):
        c = Clock(self, "B20")
        X, S0, ETA = PAR["X"], PAR["S0"], PAR["eta"]
        p_dump = S0 - ETA * X
        cost = STRAT["dump"]["mean_usd"]
        bps = STRAT["dump"]["mean_bps"]
        head = header("THE PROBLEM · MARKET IMPACT", "One big sale pushes the price down")
        tag = synthetic_tag()

        # left: the ten-step schedule (ghost), one bar fills step 1
        x0, x1, base, top = -5.4, -0.6, -2.4, 1.15
        slot = (x1 - x0) / 10
        axis = Line([x0, base, 0], [x1, base, 0], color=INK, stroke_width=3)
        frame = Rectangle(width=x1 - x0, height=top - base, stroke_color=GHOST, stroke_width=2)
        frame.move_to([(x0 + x1) / 2, (base + top) / 2, 0])
        nums = VGroup(*[T(str(k + 1), 26, MUTED).move_to([x0 + slot * (k + 0.5), base - 0.28, 0])
                        for k in range(10)])
        xlab = T("time step", 26, MUTED).move_to([(x0 + x1) / 2, base - 0.66, 0])
        ylab = T("shares sold", 26, MUTED).rotate(PI / 2).move_to([x0 - 0.35, (base + top) / 2, 0])
        big = bar(x0 + slot * 0.5, base, slot * 0.72, top - base - 0.05, ACCENT)
        big_lab = T("10,000 shares", 30, INK, SANS, "BOLD")
        big_lab.next_to(big, RIGHT, buff=0.25).align_to(big, UP).shift(DOWN * 0.1)
        big_sub = T("all at once", 28, MUTED).next_to(big_lab, DOWN, buff=0.12, aligned_edge=LEFT)

        # right: price per share
        px = 0.7
        p_lab = T("price you get per share", 28, MUTED).move_to([px, 1.25, 0], aligned_edge=LEFT)
        p_old = T(f"${S0:.2f}", 72, INK, SERIF).move_to([px, 0.45, 0], aligned_edge=LEFT)
        p_new = T(f"${p_dump:.2f}", 72, ACCENT, SERIF).move_to([px, 0.45, 0], aligned_edge=LEFT)
        slide_y = -0.55
        s_line = Line([px + 0.1, slide_y, 0], [6.0, slide_y, 0], color=GHOST, stroke_width=6)
        s_hi = T(f"${S0:.2f}", 26, MUTED).move_to([5.55, slide_y - 0.35, 0])
        s_lo = T(f"${p_dump:.2f}", 26, MUTED).move_to([px + 0.35, slide_y - 0.35, 0])
        marker = Dot([6.0, slide_y, 0], radius=0.13, color=INK)
        trail = Line([6.0, slide_y, 0], [px + 0.1, slide_y, 0], color=ACCENT, stroke_width=8)

        cbox = card(5.6, 1.6).move_to([px + 2.8, -2.25, 0])
        c_lab = T("cost of the sale", 26, MUTED).move_to([px + 0.3, -1.75, 0], aligned_edge=LEFT)
        c_num = T(f"${comma(cost)} = {bps:.0f} bps", 44, ACCENT, SERIF).move_to(
            [px + 0.3, -2.3, 0], aligned_edge=LEFT)
        c_sub = T(f"1% of the ${comma(X * S0)} order", 26, MUTED).move_to(
            [px + 0.3, -2.78, 0], aligned_edge=LEFT)

        self.add(head, tag, frame, axis, nums, xlab, ylab, p_lab, s_line, s_hi, s_lo, cbox)
        c.run(FadeIn(p_old), FadeIn(marker), rt=0.6)
        c.until("ten thousand shares")
        c.run(GrowFromEdge(big, DOWN), rt=1.2)
        c.run(FadeIn(big_lab), FadeIn(big_sub), rt=0.6)
        c.until("walks the price down")
        c.run(Create(trail), marker.animate.move_to([px + 0.1, slide_y, 0]), rt=2.0)
        c.until("forty-nine fifty")
        c.run(ReplacementTransform(p_old, p_new), rt=0.8)
        c.until("five thousand dollars")
        c.run(FadeIn(c_lab), FadeIn(c_num, shift=UP * 0.15), FadeIn(c_sub), rt=0.8)
        c.until("market impact")
        c.run(Indicate(c_num, color=ACCENT, scale_factor=1.06), rt=0.8)
        c.pad()


# ── B30: equal slices, but the price wanders ──────────────────────────────────
class B30_Drift(Scene):
    def construct(self):
        c = Clock(self, "B30")
        sd = RES["sample_days"]
        paths = sd["price_paths"]
        worst = sd["worst_twap_day"]
        S0 = PAR["S0"]
        head = header("THE OTHER RISK · WAITING", "Slices let the price wander")
        tag = synthetic_tag()

        x0, x1 = -4.9, 6.0
        step = (x1 - x0) / 10
        lo = min(min(p) for p in paths); hi = max(max(p) for p in paths)
        span = max(hi - S0, S0 - lo) + 0.05
        ymid, yh = 0.2, 1.05                       # fan area: ymid +/- yh

        def P(k, price):
            return [x0 + step * k, ymid + (price - S0) / span * yh, 0]

        fan_frame = Rectangle(width=x1 - x0, height=2 * yh + 0.2, stroke_color=GHOST, stroke_width=2)
        fan_frame.move_to([(x0 + x1) / 2, ymid, 0])
        arrival = DashedLine(P(0, S0), P(10, S0), color=MUTED, stroke_width=2, dash_length=0.12)
        a_lab = T(f"${S0:.2f}", 26, MUTED).next_to(P(0, S0), LEFT, buff=0.15)
        f_lab = T("price on 40 simulated days", 26, MUTED).move_to(
            [x0 - 0.75, ymid + yh + 0.4, 0], aligned_edge=LEFT)
        lines = VGroup()
        for i, p in enumerate(paths):
            if i == worst:
                continue
            m = VMobject(stroke_color=TEAL, stroke_width=2.2, stroke_opacity=0.55)
            m.set_points_as_corners([P(k, v) for k, v in enumerate(p)])
            lines.add(m)
        bad = VMobject(stroke_color=ACCENT, stroke_width=6)
        bad.set_points_as_corners([P(k, v) for k, v in enumerate(paths[worst])])
        bad_lab = T(f"a bad day: {sd['twap_cost_bps'][worst]:.0f} bps", 28, ACCENT, SANS, "BOLD")
        bad_lab.move_to([x1, ymid + yh + 0.4, 0], aligned_edge=RIGHT)

        # equal slices below
        base, bh = -2.85, 1.1
        slices = VGroup(*[bar(x0 + step * (k + 0.5), base, step * 0.62, bh) for k in range(10)])
        ghosts = VGroup(*[Rectangle(width=step * 0.62, height=bh, stroke_color=GHOST, stroke_width=2)
                          .move_to([x0 + step * (k + 0.5), base + bh / 2, 0]) for k in range(10)])
        s_lab = T("1,000 shares each step", 26, MUTED).move_to([x0 - 0.75, base + bh + 0.33, 0],
                                                                aligned_edge=LEFT)
        nums = VGroup(*[T(str(k + 1), 24, MUTED).move_to([x0 + step * (k + 0.5), base - 0.28, 0])
                        for k in range(10)])
        chip_t = T(f"impact: {STRAT['dump']['mean_bps']:.0f} → {STRAT['twap']['mean_bps']:.0f} bps",
                   26, INK, MONO, "BOLD")
        chip = VGroup(card(chip_t.width + 0.5, chip_t.height + 0.32), chip_t)
        chip_t.move_to(chip[0].get_center())
        chip.move_to([6.0, base + bh + 0.36, 0], aligned_edge=RIGHT)

        self.add(head, tag, fan_frame, arrival, a_lab, ghosts, nums, s_lab)
        c.until("ten equal pieces")
        c.run(LaggedStart(*[GrowFromEdge(b, DOWN) for b in slices], lag_ratio=0.12), rt=1.6)
        c.until("about ten times")
        c.run(FadeIn(chip, shift=DOWN * 0.1), rt=0.6)
        c.until("keeps")
        c.run(FadeIn(f_lab), Create(lines, lag_ratio=0.02), rt=2.4)
        c.until("On a bad day")
        c.run(Create(bad), rt=1.4)
        c.run(FadeIn(bad_lab), rt=0.5)
        c.pad()


# ── B40: the agent and its table ──────────────────────────────────────────────
class B40_Agent(Scene):
    def construct(self):
        c = Clock(self, "B40")
        X = PAR["X"]
        sched = STRAT["rl"]["schedule"]
        inv = [X]
        for n in sched:
            inv.append(inv[-1] - n)
        head = header("THE AGENT · TABULAR Q-LEARNING", "It learns slice sizes from practice")
        tag = synthetic_tag()

        # table: 10 columns (time steps left), 8 rows (shares left)
        gx0, gy0, cw, rh = -5.0, -2.35, 0.56, 0.46
        cols, rows = 10, 8
        cells = VGroup()
        for i in range(cols):
            for j in range(rows):
                sq = Rectangle(width=cw - 0.06, height=rh - 0.06, fill_color=PANEL, fill_opacity=1,
                               stroke_width=0)
                sq.move_to([gx0 + cw * (i + 0.5), gy0 + rh * (j + 0.5), 0])
                cells.add(sq)
        gw, gh = cw * cols, rh * rows
        t_lab = T("time steps left: 10 down to 1", 26, MUTED).move_to([gx0 + gw / 2, gy0 - 0.35, 0])
        q_lab = T("shares left (10,000 at top)", 24, MUTED).move_to(
            [gx0, gy0 + gh + 0.3, 0], aligned_edge=LEFT)
        q_hi = VGroup()

        def cell_pt(k, shares):
            j = min(rows - 1, int(shares / X * rows - 1e-9)) if shares > 0 else 0
            return [gx0 + cw * (k + 0.5), gy0 + rh * (j + 0.5), 0]

        path_pts = [cell_pt(k, inv[k]) for k in range(cols)]
        cursor = Square(side_length=rh - 0.02, stroke_color=ACCENT, stroke_width=6).move_to(path_pts[0])
        trail = VMobject(stroke_color=ACCENT, stroke_width=4).set_points_as_corners(path_pts)
        dots = VGroup(*[Dot(p, radius=0.1, color=ACCENT) for p in path_pts])

        # right column
        rx = 0.9
        st_box = card(5.3, 1.35).move_to([rx + 2.65, 1.05, 0])
        st1 = T("sees: time left · shares left", 28, INK).move_to([rx + 0.3, 1.27, 0], aligned_edge=LEFT)
        st2 = T("state = one cell of the table", 26, MUTED).move_to([rx + 0.3, 0.8, 0], aligned_edge=LEFT)
        a_title = T("picks: fraction to sell now", 28, INK).move_to([rx + 0.3, 0.05, 0],
                                                                       aligned_edge=LEFT)
        sx0, sx1, sy = rx + 0.35, rx + 4.6, -0.7
        ticks = VGroup(*[Line([sx0 + (sx1 - sx0) * i / 20, sy - 0.1, 0], [sx0 + (sx1 - sx0) * i / 20, sy + 0.1, 0],
                              color=GHOST, stroke_width=3) for i in range(21)])
        rail = Line([sx0, sy, 0], [sx1, sy, 0], color=GHOST, stroke_width=3)
        tl = VGroup(*[T(s, 24, MUTED).move_to([sx0 + (sx1 - sx0) * f, sy - 0.38, 0])
                      for s, f in (("0%", 0), ("50%", 0.5), ("100%", 1))])
        first = sched[0] / X
        pick = Triangle(fill_color=ACCENT, fill_opacity=1, stroke_width=0).scale(0.13).rotate(PI)
        pick.move_to([sx0 + (sx1 - sx0) * first, sy + 0.3, 0])
        pick_lab = T(f"{first:.0%}", 26, ACCENT, SANS, "BOLD").next_to(pick, RIGHT, buff=0.12)
        sc_box = card(5.3, 1.2).move_to([rx + 2.65, -1.95, 0])
        sc1 = T("score = cash received", 28, INK).move_to([rx + 0.3, -1.74, 0], aligned_edge=LEFT)
        sc2 = T("− a small penalty on shares held", 24, MUTED).move_to([rx + 0.3, -2.17, 0],
                                                                            aligned_edge=LEFT)
        days = PAR["episodes"]
        n_lab = T(f"{comma(days)} practice runs", 28, ACCENT, SANS, "BOLD").move_to(
            [rx + 0.3, -3.0, 0], aligned_edge=LEFT)

        self.add(head, tag, cells, st_box, sc_box, rail, ticks, tl)
        c.until("time left and shares left")
        c.run(FadeIn(t_lab), FadeIn(q_lab), FadeIn(q_hi), FadeIn(st1), FadeIn(st2), rt=0.8)
        c.run(Create(cursor), rt=0.5)
        c.until("what fraction to sell now")
        c.run(FadeIn(a_title), FadeIn(pick, shift=DOWN * 0.2), FadeIn(pick_lab), rt=0.8)
        c.until("Its score")
        c.run(FadeIn(sc1), FadeIn(sc2), rt=0.8)
        c.until("It practiced")
        c.run(FadeIn(n_lab), cells.animate.set_fill(TEAL, opacity=0.35), rt=1.6)
        c.run(Create(trail), FadeIn(dots), cursor.animate.move_to(path_pts[-1]), rt=2.2)
        c.pad()


# ── B50: the learned schedule vs the closed form ──────────────────────────────
class B50_Schedule(Scene):
    def construct(self):
        c = Clock(self, "B50")
        rl = STRAT["rl"]["schedule"]
        ac = RES["ac"]["n"]
        head = header("WHAT IT LEARNED", "Sell more early, then taper off")
        tag = synthetic_tag()

        x0, x1, base, top = -5.2, 1.0, -2.45, 1.35
        ymax = 3000.0
        slot = (x1 - x0) / 10

        def Y(v):
            return base + v / ymax * (top - base)

        axis = Line([x0, base, 0], [x1, base, 0], color=INK, stroke_width=3)
        grid = VGroup(*[DashedLine([x0, Y(v), 0], [x1, Y(v), 0], color=GHOST, stroke_width=2,
                                   dash_length=0.1) for v in (1000, 2000, 3000)])
        ylabs = VGroup(*[T(comma(v), 24, MUTED).move_to([x0 - 0.12, Y(v), 0], aligned_edge=RIGHT)
                         for v in (1000, 2000, 3000)])
        nums = VGroup(*[T(str(k + 1), 24, MUTED).move_to([x0 + slot * (k + 0.5), base - 0.28, 0])
                        for k in range(10)])
        xl = T("time step · shares sold in each step", 26, MUTED).move_to([(x0 + x1) / 2, base - 0.64, 0])
        bars = VGroup(*[bar(x0 + slot * (k + 0.5), base, slot * 0.64, Y(v) - base) for k, v in enumerate(rl)])
        ghosts = VGroup(*[Rectangle(width=slot * 0.64, height=Y(1000) - base, stroke_color=GHOST,
                                    stroke_width=2).move_to([x0 + slot * (k + 0.5), (base + Y(1000)) / 2, 0])
                          for k in range(10)])
        dots = VGroup(*[Dot([x0 + slot * (k + 0.5), Y(v), 0], radius=0.1, color=ACCENT) for k, v in enumerate(ac)])
        link = VMobject(stroke_color=ACCENT, stroke_width=3).set_points_as_corners(
            [[x0 + slot * (k + 0.5), Y(v), 0] for k, v in enumerate(ac)])

        rx = 1.75
        lg1 = VGroup(Square(0.26, fill_color=TEAL, fill_opacity=1, stroke_width=0),
                     T("learned by Q-learning", 26, INK)).arrange(RIGHT, buff=0.2)
        lg2 = VGroup(Dot(radius=0.11, color=ACCENT), T("Almgren & Chriss", 26, INK)).arrange(RIGHT, buff=0.2)
        lg1.move_to([rx, 1.2, 0], aligned_edge=LEFT)
        lg2.move_to([rx, 0.65, 0], aligned_edge=LEFT)
        fbox = card(4.5, 1.4).move_to([rx + 2.25, -0.4, 0])
        formula = SVGMobject(str(HERE / "assets" / "ac-formula-ink.svg")).scale_to_fit_width(4.0)
        formula.move_to(fbox.get_center())
        f_src = VGroup(T("formula: shares still held", 24, MUTED),
                       T("dots: shares sold per step", 24, MUTED)).arrange(
            DOWN, aligned_edge=LEFT, buff=0.1).move_to([rx, -1.5, 0], aligned_edge=LEFT)
        gap = RES["rl_objective_gap_vs_ac_pct"]
        g1 = T("cost + risk, held-out days", 24, MUTED).move_to([rx, -2.2, 0], aligned_edge=LEFT)
        g2 = T(f"agent {STRAT['rl']['objective_bps']:.1f} · formula {STRAT['ac']['objective_bps']:.1f}",
               24, INK).move_to([rx, -2.58, 0], aligned_edge=LEFT)
        g3 = T(f"within {gap:.1f}%", 30, ACCENT, SANS, "BOLD").move_to([rx, -3.05, 0], aligned_edge=LEFT)

        self.add(head, tag, axis, grid, ylabs, nums, xl, ghosts, fbox)
        c.run(FadeIn(lg1), rt=0.5)
        c.until("sell more early")
        c.run(FadeOut(ghosts), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.15), rt=2.0)
        c.until("The dots")
        c.run(FadeIn(lg2), LaggedStart(*[FadeIn(d, shift=DOWN * 0.3) for d in dots], lag_ratio=0.1), rt=1.4)
        c.run(Create(link), FadeIn(formula), rt=0.9)
        c.run(FadeIn(f_src), rt=0.4)
        c.until("land close to it")
        c.run(FadeIn(g1), FadeIn(g2), FadeIn(g3), rt=0.8)
        c.pad()


# ── B60: held-out cost comparison ─────────────────────────────────────────────
class B60_Costs(Scene):
    def construct(self):
        c = Clock(self, "B60")
        head = header(f"HELD-OUT TEST · {comma(PAR['test_days'])} SIMULATED DAYS",
                      "Cost of selling 10,000 shares")
        tag = synthetic_tag()
        x0, x1 = -2.3, 6.0

        def X_(b):
            return x0 + b / 100 * (x1 - x0)

        rows = [("All at once", "dump", 0.75), ("Equal slices", "twap", -0.65), ("The agent", "rl", -2.05)]
        ax_y = -2.8
        axis = Line([x0, ax_y, 0], [x1, ax_y, 0], color=INK, stroke_width=3)
        tks = VGroup(*[Line([X_(v), ax_y, 0], [X_(v), ax_y - 0.12, 0], color=INK, stroke_width=3)
                       for v in (0, 25, 50, 75, 100)])
        tls = VGroup(*[T(str(v), 24, MUTED).move_to([X_(v), ax_y - 0.3, 0]) for v in (0, 25, 50, 75, 100)])
        unit = T("bps", 24, MUTED).move_to([x0 - 0.55, ax_y - 0.3, 0])
        cap = T("1 bp = 0.01% of the order · bad day = worst 1 in 20",
                24, MUTED).move_to([-6.25, 1.6, 0], aligned_edge=LEFT)
        groups = []
        for label, key, y in rows:
            s = STRAT[key]
            lab = T(label, 40, INK, SERIF).move_to([-6.25, y, 0], aligned_edge=LEFT)
            lane = Rectangle(width=x1 - x0, height=0.62, fill_color=PANEL, fill_opacity=1, stroke_width=0)
            lane.move_to([(x0 + x1) / 2, y, 0])
            b = Rectangle(width=max(0.02, X_(s["mean_bps"]) - x0), height=0.62, fill_color=TEAL,
                          fill_opacity=1, stroke_width=0)
            b.move_to([x0 + b.width / 2, y, 0])
            if key == "dump":
                val = T(f"{s['mean_bps']:.0f} every day", 30, ON_DARK, SANS, "BOLD")
                val.move_to([x1 - 0.2, y, 0], aligned_edge=RIGHT)
                extra = VGroup()
            else:
                val = T(f"{s['mean_bps']:.0f} avg", 28, INK, SANS, "BOLD").next_to(b, RIGHT, buff=0.15)
                col = ACCENT if key == "rl" else INK
                tick = Line([X_(s["p95_bps"]), y - 0.42, 0], [X_(s["p95_bps"]), y + 0.42, 0],
                            color=col, stroke_width=7)
                tl = T(f"bad day {s['p95_bps']:.0f}", 30 if key == "rl" else 28, col, SANS, "BOLD")
                tl.move_to([X_(s["p95_bps"]), y + 0.68, 0])
                extra = VGroup(tick, tl)
            groups.append((lab, lane, b, val, extra))

        self.add(head, tag, axis, tks, tls, unit, cap)
        for lab, lane, b, val, extra in groups:
            self.add(lane)
        c.run(*[FadeIn(g[0]) for g in groups], rt=0.6)
        for (lab, lane, b, val, extra), phrase in zip(groups, ("All at once", "Equal slices", "The agent")):
            c.until(phrase)
            c.run(GrowFromEdge(b, LEFT), rt=1.0)
            c.run(FadeIn(val), *[FadeIn(m) for m in extra], rt=0.6)
        c.pad()


# ── B70: dark takeaway ────────────────────────────────────────────────────────
class B70_Takeaway(Scene):
    def construct(self):
        c = Clock(self, "B70", bg=DARK)
        head = header("TAKEAWAY", "Impact versus risk", dark=True)

        fx, fy = -3.55, -1.9
        fulcrum = Triangle(fill_color=GHOST_DARK, fill_opacity=1, stroke_width=0).scale(0.45)
        fulcrum.move_to([fx, fy - 0.25, 0])
        beam = Line([fx - 2.5, fy + 0.2, 0], [fx + 2.5, fy + 0.2, 0], color=ON_DARK, stroke_width=8)
        lpan = card(1.9, 0.8, DARK_PANEL).move_to([fx - 2.0, fy + 0.85, 0])
        rpan = card(1.9, 0.8, DARK_PANEL).move_to([fx + 2.0, fy + 0.85, 0])
        lt = T("impact", 32, ON_DARK, SERIF).move_to(lpan.get_center())
        rt_ = T("risk", 32, ON_DARK, SERIF).move_to(rpan.get_center())
        scale_g = VGroup(beam, lpan, rpan, lt, rt_)
        pivot = [fx, fy + 0.2, 0]
        s1 = T("sell fast → pay impact", 30, ON_DARK).move_to([fx - 2.55, 1.15, 0], aligned_edge=LEFT)
        s2 = T("sell slowly → carry risk", 30, ON_DARK).move_to([fx - 2.55, 0.6, 0], aligned_edge=LEFT)
        s3 = T("the agent learned the balance", 30, MUTED_DARK).move_to([fx - 2.55, 0.05, 0],
                                                                         aligned_edge=LEFT)

        cx = 0.8
        cbox = card(5.4, 3.7, DARK_PANEL).move_to([cx + 2.7, -0.25, 0])
        c_title = T("This was a synthetic market", 34, ON_DARK, SERIF).move_to([cx + 0.35, 1.2, 0],
                                                                              aligned_edge=LEFT)
        c_sub = T("Real markets add:", 28, MUTED_DARK).move_to([cx + 0.35, 0.55, 0], aligned_edge=LEFT)
        items = VGroup(*[T("· " + s, 30, ON_DARK).move_to([cx + 0.45, y, 0], aligned_edge=LEFT)
                         for s, y in (("order books", -0.05), ("other traders who react", -0.65),
                                      ("sudden price jumps", -1.25))])
        ref = T("Read more: Nevmyvaka et al. 2006 · Almgren & Chriss 2000",
                24, MUTED_DARK).move_to([-6.25, -2.9, 0], aligned_edge=LEFT)

        cghost = Rectangle(width=5.4, height=3.7, stroke_color=GHOST_DARK,
                           stroke_width=2).move_to(cbox.get_center())
        self.add(head, fulcrum, cghost)
        c.run(FadeIn(scale_g), rt=0.6)
        c.until("a trade-off")
        c.run(Rotate(scale_g, angle=-0.16, about_point=pivot), FadeIn(s1), rt=1.0)
        c.run(Rotate(scale_g, angle=0.32, about_point=pivot), FadeIn(s2), rt=1.0)
        c.until("The agent learned")
        c.run(Rotate(scale_g, angle=-0.16, about_point=pivot), FadeIn(s3), rt=1.2)
        c.until("synthetic market")
        c.run(FadeIn(cbox), FadeOut(cghost), FadeIn(c_title), FadeIn(c_sub), rt=0.7)
        c.until("Real markets")
        c.run(LaggedStart(*[FadeIn(i, shift=RIGHT * 0.15) for i in items], lag_ratio=0.35), rt=1.6)
        c.until("For the research version")
        c.run(FadeIn(ref), rt=0.6)
        c.pad()


# ── B90: outro ────────────────────────────────────────────────────────────────
class B90_Outro(Scene):
    def construct(self):
        c = Clock(self, "B90")
        title = T("How an AI Sells a Big Order", 66, INK, SERIF).move_to([0, 2.45, 0])
        logo = ImageMobject(str(HERE / "assets" / "hai-logo-1-ink.png")).scale_to_fit_height(1.45)
        handle = T("@HumanitariansAI", 48, INK, SERIF)
        brand = Group(logo, handle).arrange(RIGHT, buff=0.45).move_to([0, 0.75, 0])
        pill_t = T("SUBSCRIBE", 32, ON_DARK, SANS, "BOLD")
        pill = RoundedRectangle(corner_radius=0.36, width=pill_t.width + 1.0, height=0.78,
                                fill_color=ACCENT, fill_opacity=1, stroke_width=0)
        pill_g = VGroup(pill, pill_t).move_to([0, -0.75, 0])
        pill_t.move_to(pill.get_center())
        cr = VGroup(
            T("Boopesh M. · Humanitarians AI Fellow · Brutalist team", 28, INK),
            T("Narration: AI voice (Kokoro am_onyx)", 26, MUTED),
            T("Data: synthetic market (code/execution_rl.py)", 26, MUTED),
        ).arrange(DOWN, buff=0.18).move_to([0, -2.45, 0])
        self.add(title)
        c.run(FadeIn(logo, shift=UP * 0.2), FadeIn(handle), rt=0.7)
        c.run(FadeIn(cr), rt=0.5)
        c.until("Subscribe")
        c.run(FadeIn(pill_g, scale=1.15), rt=0.5)
        c.run(pill_g.animate.scale(0.94), rt=0.2)
        c.run(pill_g.animate.scale(1 / 0.94), rt=0.2)
        c.pad()
