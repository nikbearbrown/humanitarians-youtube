# -*- coding: utf-8 -*-
"""
Manim scenes for "Hedging When Trading Isn't Free" (16:9, 3840x2160) -- Boopesh M.
Paper: Buehler, Gonon, Teichmann & Wood, "Deep Hedging", Quantitative Finance 19(8), 2019.
  B20_Basics     -- selling a call, holding delta shares; typeset Black-Scholes delta
  B30_Cost       -- the daily delta hedge's turnover and fees (from code/results.json)
  B40_Move       -- the paper's move: learned policy, cost-aware objective, entropic utility
  B50_Results    -- P&L histograms, BS delta vs deep hedge, 40,000 test paths, 0.5% costs
  B60_Learned    -- one path: positions BS vs deep; turnover / fees bars
  B70_Limits     -- gamma = 0 sanity check + honest limits
  B90_Outro      -- @HumanitariansAI outro + fellow credit
Every number and chart is read from code/results.json and code/arrays.npz, written by
code/deep_hedge.py. Each scene lands exactly on its beat's measured narration length.
"""
import json
from pathlib import Path

import numpy as np
from scipy.special import ndtr
from manim import *

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
CODE = HERE / "code"
if not (CODE / "results.json").exists():   # isolated copies (static pre-flight) fall back to the reel's data
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-10-24-deep-hedging/code")

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"   # terracotta, WCAG 4.5:1+ on cream and panel
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
GHOST = "#A39A88"
TEAL = "#1F4E5F"     # the deep hedge
GREY = "#8C8578"     # Black-Scholes delta (chart marks)
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

RES = json.loads((CODE / "results.json").read_text())
ARR = np.load(CODE / "arrays.npz")
G = RES["gamma_0.005"]
G0 = RES["gamma_0.0"]


def _sheet():
    try:
        return {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}
    except Exception:
        return {}


BEATS = _sheet()


def beat_len(bid, default=12.0):
    b = BEATS.get(bid, {})
    return float(b.get("render_duration_s") or b.get("actual_duration_s") or default)


def cue(bid, phrase, default):
    """Seconds into the beat when `phrase` is spoken (share of characters + lead silence)."""
    b = BEATS.get(bid)
    if not b:
        return default
    text = b["narration_text"]
    i = text.find(phrase)
    if i < 0:
        return default
    lead = float(b.get("lead_silence_s") or 0)
    return lead + (beat_len(bid) - lead) * i / len(text)


class Clock:
    """Schedules a scene's animations against narration cues and ends it on the beat length."""

    def __init__(self, scene, bid):
        self.scene, self.bid, self.t = scene, bid, 0.0
        scene.camera.background_color = BG

    def play_at(self, at, *anims, run_time=0.8, **kw):
        if at > self.t:
            self.scene.wait(at - self.t)
            self.t = at
        self.scene.play(*anims, run_time=run_time, **kw)
        self.t += run_time

    def finish(self):
        end = beat_len(self.bid)
        if end - self.t > 1 / 24:
            self.scene.wait(end - self.t)


def t(s, size=40, color=INK, font=SANS, weight="NORMAL", **kw):
    return Text(s, font=font, font_size=size, color=color, weight=weight, **kw)


def svg(name, height=None, width=None):
    m = SVGMobject(str(ASSETS / name))
    if height:
        m.scale_to_fit_height(height)
    if width:
        m.scale_to_fit_width(width)
    return m


def header(kicker, title):
    k = t(kicker.upper(), 22, MUTED, MONO)
    h = t(title, 58, INK, SERIF, weight="BOLD")
    g = VGroup(k, h).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    g.to_corner(UL, buff=0.85)
    return g


def card(w, h, fill=PANEL):
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color=fill,
                            fill_opacity=1, stroke_width=0)


def ghost_of(m):
    return m.copy().set_fill(opacity=0).set_stroke(GHOST, 3)


def money(x):
    return f"${x:.2f}" if x >= 0 else f"−${-x:.2f}"


def num(x, nd=2):
    return f"{x:.{nd}f}".replace("-", "−")


class Frame:
    """Maps data coordinates onto a rectangle of the scene."""

    def __init__(self, x0, x1, y0, y1, box):
        self.x0, self.x1, self.y0, self.y1 = x0, x1, y0, y1
        self.L, self.R, self.B, self.T = box

    def p(self, x, y):
        return np.array([self.L + (x - self.x0) / (self.x1 - self.x0) * (self.R - self.L),
                         self.B + (y - self.y0) / (self.y1 - self.y0) * (self.T - self.B), 0.0])

    def axes(self, color=INK):
        return VGroup(Line([self.L, self.B, 0], [self.R + 0.1, self.B, 0], color=color, stroke_width=3),
                      Line([self.L, self.B, 0], [self.L, self.T + 0.1, 0], color=color, stroke_width=3))


def hist_shape(fr, data, edges, color, opacity):
    counts, _ = np.histogram(data, bins=edges)
    dens = counts / counts.sum()
    pts = [fr.p(edges[0], 0)]
    for i, c in enumerate(dens):
        pts += [fr.p(edges[i], c), fr.p(edges[i + 1], c)]
    pts.append(fr.p(edges[-1], 0))
    poly = Polygon(*pts, color=color, stroke_width=3, fill_color=color, fill_opacity=opacity)
    return poly, dens.max()


def legend_row(color, label, size=24, fill=0.6):
    sw = Square(0.26, fill_color=color, fill_opacity=fill, stroke_color=color, stroke_width=3)
    return VGroup(sw, t(label, size, INK)).arrange(RIGHT, buff=0.18)


# ======================================================================== B20 =
class B20_Basics(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("hedging basics · Black–Scholes", "The textbook hedge")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        # left: the trade, as two cards with an arrow
        sell = card(4.3, 1.25)
        sell_l = VGroup(t("you SELL one call", 28, INK, weight="BOLD"),
                        t("strike $100 · 30 trading days", 22, MUTED)).arrange(DOWN, buff=0.12).move_to(sell)
        hold = card(4.3, 1.25)
        hold_l = VGroup(t("you HOLD Δ shares", 28, TEAL, weight="BOLD"),
                        t("stock starts at $100", 22, MUTED)).arrange(DOWN, buff=0.12).move_to(hold)
        g_sell, g_hold = VGroup(sell, sell_l), VGroup(hold, hold_l)
        col = VGroup(g_sell, g_hold).arrange(DOWN, buff=0.75).move_to([-3.75, -0.12, 0])
        arr = Arrow(sell.get_bottom(), hold.get_top(), buff=0.08, color=INK, stroke_width=5)
        risk = t("cancels the risk", 22, MUTED).next_to(arr, RIGHT, buff=0.2)

        # right: the formula panel
        pnl_box = card(6.0, 2.6).move_to([2.95, 0.22, 0])
        e1 = svg("eq_delta_ink.svg", height=0.85)
        e2 = VGroup(t("a number from 0 to 1", 28, INK),
                    t("higher price → hold more shares", 24, MUTED)).arrange(DOWN, buff=0.15)
        eqs = VGroup(e1, e2).arrange(DOWN, buff=0.45).move_to(pnl_box)
        r0 = t("Black–Scholes formula, interest rate 0", 18, MUTED).next_to(pnl_box, DOWN, buff=0.14)

        # bottom: delta as a function of price, computed from the formula
        fr = Frame(80, 120, 0, 1, (0.3, 5.85, -3.0, -1.75))
        ax = fr.axes()
        tau = 30 / 252
        xs = np.linspace(80, 120, 120)
        d = ndtr((np.log(xs / 100) + 0.5 * 0.04 * tau) / (0.2 * np.sqrt(tau)))
        curve = VMobject(color=TEAL, stroke_width=6).set_points_smoothly([fr.p(x, y) for x, y in zip(xs, d)])
        lab_x = VGroup(t("$80", 18, MUTED, MONO).move_to(fr.p(80, 0) + DOWN * 0.25),
                       t("$100", 18, MUTED, MONO).move_to(fr.p(100, 0) + DOWN * 0.25),
                       t("$120", 18, MUTED, MONO).move_to(fr.p(120, 0) + DOWN * 0.25))
        lab_y = VGroup(t("Δ = 1", 18, MUTED, MONO).next_to(fr.p(80, 1), LEFT, buff=0.12),
                       t("Δ = 0", 18, MUTED, MONO).next_to(fr.p(80, 0), LEFT, buff=0.12))
        ctitle = t("Δ vs. stock price", 20, MUTED).move_to(fr.p(112, 0.22))

        daily = card(4.3, 1.1, fill=DARK).move_to([-3.75, -2.6, 0])
        daily_l = VGroup(t("rebalance every day", 26, ON_DARK, weight="BOLD"),
                         t("assumes trading is free", 20, "#D8D0C0")).arrange(DOWN, buff=0.1).move_to(daily)

        ghosts = VGroup(ghost_of(sell), ghost_of(hold), ghost_of(pnl_box), ghost_of(daily),
                        ax.copy().set_color(GHOST))
        clock.play_at(0.4, FadeIn(ghosts), run_time=0.6)
        clock.play_at(cue("B20", "sell a call", 1.5), FadeIn(g_sell, shift=RIGHT * 0.2), run_time=0.6)
        clock.play_at(cue("B20", "hold delta", 4.0), GrowArrow(arr), FadeIn(g_hold, shift=RIGHT * 0.2),
                      FadeIn(risk), run_time=0.7)
        clock.play_at(cue("B20", "Black-Scholes gives", 7.0), FadeIn(pnl_box), FadeIn(e1, shift=UP * 0.1),
                      FadeIn(r0), run_time=0.6)
        clock.play_at(clock.t + 0.3, FadeIn(e2, shift=UP * 0.1), run_time=0.6)
        clock.play_at(clock.t + 0.2, Create(ax), FadeIn(lab_x), FadeIn(lab_y), FadeIn(ctitle), run_time=0.5)
        clock.play_at(clock.t, Create(curve), run_time=1.2)
        clock.play_at(cue("B20", "every trading day", 12.0), FadeIn(daily), FadeIn(daily_l), run_time=0.6)
        clock.finish()


# ======================================================================== B30 =
class B30_Cost(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("the catch · fee = 0.5% of each trade", "Every trade pays a fee")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        per_day = ARR["gamma_0.005_turnover_bs_per_day"]
        fr = Frame(0, 30, 0, 0.6, (-5.8, 0.15, -2.5, 1.35))
        ax = fr.axes()
        bars = VGroup()
        for i, v in enumerate(per_day):
            lo, hi = fr.p(i + 0.12, 0), fr.p(i + 0.88, min(v, 0.6))
            bars.add(Rectangle(width=hi[0] - lo[0], height=max(hi[1] - lo[1], 0.01), fill_color=GREY,
                               fill_opacity=1, stroke_width=0).move_to((lo + hi) / 2))
        ghost_bars = bars.copy().set_fill(opacity=0).set_stroke(GHOST, 2)
        xl = VGroup(t("day 1", 18, MUTED, MONO).move_to(fr.p(0.5, 0) + DOWN * 0.28),
                    t("day 30", 18, MUTED, MONO).move_to(fr.p(29.5, 0) + DOWN * 0.28))
        ctitle = t("shares traded per day (average of 40,000 paths)", 18, MUTED).move_to(fr.p(15, 0) + DOWN * 0.6)
        first = t(f"day 1: buy {per_day[0]:.2f} shares", 20, INK).next_to(bars[0], RIGHT, buff=0.15)
        first.align_to(bars[0], UP)
        later = t("then a little, every single day", 20, INK).move_to(fr.p(15.5, 0.17))

        stats = [(f"{G['turnover_bs']:.2f}", "shares traded per option", "trades about"),
                 (money(G["bs_delta"]["mean_cost"]), "paid in fees, on average", "in fees"),
                 (money(RES["setup"]["premium_bs"]), "the option's price", "only sold for")]
        cards = VGroup()
        for big, small, _ in stats:
            c = card(5.5, 1.1)
            lab = VGroup(t(big, 42, INK, SERIF, weight="BOLD"), t(small, 20, MUTED)).arrange(RIGHT, buff=0.3)
            lab.move_to(c)
            cards.add(VGroup(c, lab))
        cards.arrange(DOWN, buff=0.22).move_to([3.4, -0.6, 0])
        cards[1][1][0].set_color(ACCENT)
        share = t(f"fees eat {100 * G['bs_delta']['mean_cost'] / RES['setup']['premium_bs']:.0f}% of the premium",
                  24, ACCENT, weight="BOLD").next_to(cards, DOWN, buff=0.22)

        clock.play_at(0.4, FadeIn(ghost_bars), FadeIn(VGroup(*[ghost_of(c[0]) for c in cards])), run_time=0.6)
        clock.play_at(0.9, Create(ax), FadeIn(xl), FadeIn(ctitle), run_time=0.6)
        clock.play_at(cue("B30", "daily delta hedge", 2.5), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars],
                                                                         lag_ratio=0.05), run_time=1.6)
        clock.play_at(clock.t, FadeIn(first), FadeIn(later), run_time=0.5)
        for i, (_, _, phrase) in enumerate(stats):
            clock.play_at(cue("B30", phrase, 6.0 + 2.5 * i), FadeIn(cards[i], shift=LEFT * 0.2), run_time=0.6)
        clock.play_at(clock.t + 0.2, FadeIn(share, shift=UP * 0.1), run_time=0.6)
        clock.finish()


# ======================================================================== B40 =
class B40_Move(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        hd = header("Deep Hedging · Buehler, Gonon, Teichmann & Wood · 2019", "Learn the hedge, fees included")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        # flow: state -> network -> position
        ins = VGroup(*[t(s, 22, INK) for s in ("time left", "stock price", "current position")])
        ins.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        in_box = card(ins.width + 0.6, ins.height + 0.5)
        ins.move_to(in_box)
        g_in = VGroup(in_box, ins).move_to([-4.6, 0.55, 0])
        layers = [3, 5, 5, 1]
        net = VGroup()
        cols = []
        for li, n in enumerate(layers):
            colv = VGroup(*[Circle(0.13, color=TEAL, stroke_width=3, fill_color=TEAL, fill_opacity=0.25)
                            for _ in range(n)]).arrange(DOWN, buff=0.18)
            colv.move_to([-1.75 + li * 1.0, 0.55, 0])
            cols.append(colv)
        edges = VGroup()
        for a, b in zip(cols[:-1], cols[1:]):
            for u in a:
                for v in b:
                    edges.add(Line(u.get_center(), v.get_center(), color=LINE, stroke_width=1.5))
        net.add(edges, *cols)
        net_lab = t("small neural network (3-32-32-1)", 18, MUTED).next_to(net, DOWN, buff=0.18)
        out = card(2.9, 1.0)
        out_l = t("new position δ", 24, TEAL, weight="BOLD").move_to(out)
        g_out = VGroup(out, out_l).move_to([4.35, 0.55, 0])
        a1 = Arrow(g_in.get_right(), cols[0].get_left(), buff=0.12, color=INK, stroke_width=4)
        a2 = Arrow(cols[-1].get_right(), g_out.get_left(), buff=0.12, color=INK, stroke_width=4)
        loop_lab = t("again every day, for 30 days", 18, MUTED).next_to(g_out, DOWN, buff=0.2)

        obj_box = card(12.4, 1.3).move_to([0, -1.6, 0])
        obj = VGroup(t("score =", 34, INK), t("option money", 34, INK, weight="BOLD"), t("+", 34, INK),
                     t("hedge gains", 34, TEAL, weight="BOLD"), t("−", 34, INK),
                     t("fees", 34, ACCENT, weight="BOLD")).arrange(RIGHT, buff=0.25).move_to(obj_box)
        obj_note = VGroup()
        ent = svg("eq_ent_ink.svg", height=0.62)
        ent_note = t("big losses count much more (λ = 1)", 22, MUTED)
        lam = VGroup()
        VGroup(ent, ent_note).arrange(RIGHT, buff=0.4).move_to([0, -2.85, 0])

        ghosts = VGroup(ghost_of(in_box), ghost_of(out), ghost_of(obj_box),
                        VGroup(*cols).copy().set_fill(opacity=0).set_stroke(GHOST, 2))
        clock.play_at(0.4, FadeIn(ghosts), run_time=0.6)
        clock.play_at(cue("B40", "neural network", 2.5), FadeIn(g_in), GrowArrow(a1), FadeIn(net), FadeIn(net_lab),
                      run_time=0.8)
        clock.play_at(cue("B40", "choose the position", 4.0), GrowArrow(a2), FadeIn(g_out), run_time=0.6)
        clock.play_at(clock.t + 0.1, FadeIn(loop_lab), run_time=0.5)
        clock.play_at(cue("B40", "includes the fees", 8.0), FadeIn(obj_box), FadeIn(obj, shift=UP * 0.1),
                      FadeIn(obj_note), run_time=0.8)
        clock.play_at(cue("B40", "entropic utility", 12.0), FadeIn(ent, shift=UP * 0.1), FadeIn(ent_note), run_time=0.8)
        clock.finish()


# ======================================================================== B50 =
class B50_Results(Scene):
    def construct(self):
        clock = Clock(self, "B50")
        hd = header("my replication · 40,000 test paths · 0.5% fee", "Who keeps more money?")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        bs, dp = ARR["gamma_0.005_pnl_bs"], ARR["gamma_0.005_pnl_deep"]
        lo, hi = np.quantile(np.r_[bs, dp], [0.003, 0.997])
        lo, hi = np.floor(lo * 2) / 2, np.ceil(hi * 2) / 2
        edges = np.linspace(lo, hi, 56)
        mx = max(np.histogram(bs, edges)[0].max(), np.histogram(dp, edges)[0].max()) / len(bs) * 1.08
        fr = Frame(lo, hi, 0, mx, (-6.0, 0.9, -2.5, 1.4))
        ax = fr.axes()
        h_bs, _ = hist_shape(fr, bs, edges, GREY, 0.45)
        h_dp, _ = hist_shape(fr, dp, edges, TEAL, 0.45)
        ticks = VGroup()
        for v in np.arange(np.ceil(lo), np.floor(hi) + 0.01, 1.0):
            ticks.add(t((f"−${-v:.0f}" if v < 0 else f"${v:.0f}"), 18, MUTED, MONO).move_to(fr.p(v, 0) + DOWN * 0.27))
        xt = t("profit & loss per option sold", 20, MUTED).move_to(fr.p((lo + hi) / 2, 0) + DOWN * 0.62)
        zero = DashedLine(fr.p(0, 0), fr.p(0, mx), color=GHOST, stroke_width=2)
        leg = VGroup(legend_row(GREY, "Black–Scholes delta"), legend_row(TEAL, "deep hedge")).arrange(
            DOWN, aligned_edge=LEFT, buff=0.15).move_to(fr.p(lo, mx) + RIGHT * 1.95 + DOWN * 0.35)

        rows = [("", "BS delta", "deep"),
                ("average", money(G["bs_delta"]["mean"]), money(G["deep_hedge"]["mean"])),
                ("spread (std)", money(G["bs_delta"]["std"]), money(G["deep_hedge"]["std"])),
                ("worst 5% avg", money(G["bs_delta"]["cvar5"]), money(G["deep_hedge"]["cvar5"])),
                ("risk score", num(G['bs_delta']['entropic_utility']),
                 num(G['deep_hedge']['entropic_utility']))]
        table = VGroup()
        for i, (a, b, c) in enumerate(rows):
            w = "BOLD" if i == 0 or i == len(rows) - 1 else "NORMAL"
            cells = VGroup(t(a, 20, MUTED),
                           t(b, 22, INK, MONO, weight=w), t(c, 22, TEAL, MONO, weight=w))
            table.add(cells)
        xs = [2.05, 4.05, 5.4]
        tb_box = card(5.05, 4.2).move_to([3.7, -0.65, 0])
        for i, cells in enumerate(table):
            y = tb_box.get_top()[1] - 0.42 - i * 0.72
            cells[0].move_to([xs[0], y, 0])
            cells[0].shift(RIGHT * (1.45 - cells[0].get_left()[0]))
            cells[1].move_to([xs[1], y, 0])
            cells[2].move_to([xs[2], y, 0])
        hl = RoundedRectangle(width=4.85, height=0.56, corner_radius=0.08, stroke_color=ACCENT, stroke_width=4)
        hl.move_to([tb_box.get_center()[0], table[-1][1].get_center()[1], 0])
        note = t("higher is better", 18, ACCENT).next_to(hl, DOWN, buff=0.1)

        clock.play_at(0.4, FadeIn(ghost_of(tb_box)), FadeIn(ax.copy().set_color(GHOST)), run_time=0.5)
        clock.play_at(0.9, Create(ax), FadeIn(ticks), FadeIn(xt), FadeIn(zero), run_time=0.6)
        clock.play_at(cue("B50", "Black-Scholes delta", 2.0), FadeIn(h_bs), FadeIn(leg[0]), run_time=0.8)
        clock.play_at(cue("B50", "deep hedge", 4.0), FadeIn(h_dp), FadeIn(leg[1]), run_time=0.8)
        clock.play_at(clock.t + 0.2, FadeIn(tb_box), FadeIn(table[0]), run_time=0.4)
        phr = ["average", "spread", "worst five percent", "score it was trained"]
        for i, p in enumerate(phr):
            clock.play_at(max(clock.t, cue("B50", p, 6.0 + 2 * i)), FadeIn(table[i + 1], shift=LEFT * 0.15), run_time=0.45)
        clock.play_at(clock.t + 0.1, Create(hl), FadeIn(note), run_time=0.5)
        clock.finish()


# ======================================================================== B60 =
class B60_Learned(Scene):
    def construct(self):
        clock = Clock(self, "B60")
        hd = header("one test path · same prices for both hedges", "It trades less")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        S = ARR["gamma_0.005_path_S"]
        pb, pd = ARR["gamma_0.005_path_bs"], ARR["gamma_0.005_path_deep"]
        smin, smax = np.floor(S.min() - 1), np.ceil(S.max() + 1)
        frS = Frame(0, 30, smin, smax, (-5.8, 1.3, 0.35, 1.45))
        frP = Frame(0, 30, 0, 1, (-5.8, 1.3, -2.95, -0.2))
        price = VMobject(color=INK, stroke_width=4).set_points_as_corners([frS.p(i, s) for i, s in enumerate(S)])
        p_lab = t(f"stock price, ${S[0]:.0f} to ${S[-1]:.0f}", 20, MUTED)
        p_lab.move_to(frS.p(0, smax)).shift(RIGHT * (p_lab.width / 2) + UP * 0.12)

        def steps(pos, color, width):
            pts = []
            for i, v in enumerate(pos):
                pts += [frP.p(i, v), frP.p(i + 1, v)]
            return VMobject(color=color, stroke_width=width).set_points_as_corners(pts)

        axP = frP.axes()
        y_lab = VGroup(t("1", 18, MUTED, MONO).next_to(frP.p(0, 1), LEFT, buff=0.12),
                       t("0", 18, MUTED, MONO).next_to(frP.p(0, 0), LEFT, buff=0.12))
        y_name = t("shares held", 18, MUTED).next_to(frP.p(0, 1), RIGHT, buff=0.15)
        x_lab = t("trading day 1 to 30", 18, MUTED).move_to(frP.p(15, 0) + DOWN * 0.25)
        s_bs = steps(pb, GREY, 5)
        s_dp = steps(pd, TEAL, 6)
        bars_box = card(4.3, 4.6).move_to([4.15, -0.75, 0])
        top = bars_box.get_top()[1]
        leg = VGroup(legend_row(GREY, "BS delta", 22, 1),
                     legend_row(TEAL, "deep hedge", 22, 1)).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        leg.move_to([4.15, top - 0.5, 0]).align_to([2.4, 0, 0], LEFT)

        # right: turnover and fees, averaged over the 40,000 test paths
        title = t("average over 40,000 test paths", 18, MUTED).move_to([4.15, bars_box.get_bottom()[1] + 0.3, 0])
        groups = VGroup()
        specs = [("shares traded", G["turnover_bs"], G["turnover_deep"], lambda v: f"{v:.2f}"),
                 ("fees paid", G["bs_delta"]["mean_cost"], G["deep_hedge"]["mean_cost"], money)]
        for k, (name, vb, vd, fmt) in enumerate(specs):
            base_y = top - 2.3 - k * 1.55
            m = max(vb, vd)
            items = VGroup()
            for j, (v, c) in enumerate(((vb, GREY), (vd, TEAL))):
                w = 2.2 * v / m
                r = Rectangle(width=w, height=0.42, fill_color=c, fill_opacity=1, stroke_width=0)
                r.move_to([2.4 + w / 2, base_y + 0.45 - j * 0.5, 0])
                items.add(VGroup(r, t(fmt(v), 20, INK, MONO).next_to(r, RIGHT, buff=0.1)))
            nm = t(name, 20, INK).move_to([2.55, base_y + 0.95, 0])
            nm.shift(RIGHT * (2.4 - nm.get_left()[0]))
            groups.add(VGroup(nm, items))

        clock.play_at(0.3, FadeIn(ghost_of(bars_box)), FadeIn(axP.copy().set_color(GHOST)),
                      FadeIn(VGroup(s_bs, s_dp).copy().set_stroke(GHOST, 2, opacity=0.5)), run_time=0.6)
        clock.play_at(0.9, Create(price), FadeIn(p_lab), Create(axP), FadeIn(y_lab), FadeIn(y_name), FadeIn(x_lab),
                      FadeIn(bars_box), FadeIn(leg[0].copy().set_opacity(0.25)), run_time=1.0)
        clock.play_at(cue("B60", "Black-Scholes", 2.5), Create(s_bs), FadeIn(leg[0]), run_time=1.4)
        clock.play_at(cue("B60", "deep hedge", 5.0), Create(s_dp), FadeIn(leg[1]), run_time=1.4)
        clock.play_at(cue("B60", "Across all", 8.5), FadeIn(title), FadeIn(groups[0]), run_time=0.6)
        clock.play_at(cue("B60", "fees", clock.t + 1.0), FadeIn(groups[1]), run_time=0.6)
        clock.finish()


# ======================================================================== B70 =
class B70_Limits(Scene):
    def construct(self):
        clock = Clock(self, "B70")
        hd = header("sanity check + honest limits", "Does it fool itself?")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        L = card(5.9, 4.6).move_to([-3.1, -0.75, 0])
        R = card(5.9, 4.6).move_to([3.1, -0.75, 0])
        lt = t("Sanity check: fee set to 0", 26, INK, weight="BOLD").move_to(L.get_top() + DOWN * 0.45)
        rows = VGroup(
            VGroup(t("BS delta utility", 22, MUTED), t(num(G0['bs_delta']['entropic_utility'], 3), 24, INK, MONO)),
            VGroup(t("deep hedge utility", 22, MUTED), t(num(G0['deep_hedge']['entropic_utility'], 3), 24, TEAL, MONO)),
            VGroup(t("avg position gap", 22, MUTED), t(f"{G0['mean_abs_gap_to_bs_delta']:.3f} shares", 24, INK, MONO)),
        )
        for r in rows:
            r.arrange(RIGHT, buff=0.3)
        rows.arrange(DOWN, aligned_edge=RIGHT, buff=0.32).move_to(L.get_center() + DOWN * 0.05)
        verdict = t("close to Black–Scholes, slightly worse", 20, ACCENT, weight="BOLD").move_to(L.get_bottom() + UP * 0.55)

        rt = t("Limits", 26, INK, weight="BOLD").move_to(R.get_top() + DOWN * 0.45)
        lims = ["a toy world: Black–Scholes, one option",
                "the paper: S&P 500 + Heston model",
                "only as good as the simulator",
                "small network, one fee level"]
        items = VGroup()
        for s in lims:
            items.add(VGroup(Dot(radius=0.06, color=INK), t(s, 20, INK)).arrange(RIGHT, buff=0.2))
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.36).move_to(R.get_center() + DOWN * 0.15)
        items[2][1].set_color(ACCENT)

        clock.play_at(0.3, FadeIn(ghost_of(L)), FadeIn(ghost_of(R)), run_time=0.5)
        clock.play_at(cue("B70", "fee to zero", 1.2), FadeIn(L), FadeIn(lt), run_time=0.5)
        for i, p in enumerate(["Black-Scholes", "network", "positions differ"]):
            clock.play_at(max(clock.t, cue("B70", p, 2.0 + i)), FadeIn(rows[i], shift=LEFT * 0.15), run_time=0.45)
        clock.play_at(clock.t + 0.1, FadeIn(verdict), run_time=0.5)
        clock.play_at(cue("B70", "toy world", 8.0), FadeIn(R), FadeIn(rt), FadeIn(items[0]), run_time=0.6)
        clock.play_at(max(clock.t, cue("B70", "S and P", 10.0)), FadeIn(items[1]), run_time=0.45)
        clock.play_at(max(clock.t, cue("B70", "only as good", 12.0)), FadeIn(items[2]), run_time=0.45)
        clock.play_at(max(clock.t, cue("B70", "Small network", 14.0)), FadeIn(items[3]), run_time=0.45)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = t("Hedging When Trading Isn't Free", 80, INK, SERIF)
        title.scale_to_fit_width(11.6)
        pill_lab = t("SUBSCRIBE", 32, ON_DARK, SANS, weight="BOLD")
        pill = RoundedRectangle(width=pill_lab.width + 0.8, height=0.74, corner_radius=0.37,
                                fill_color=DARK, fill_opacity=1, stroke_width=0)
        pill_lab.move_to(pill)
        hai = svg("hai-logo.svg", height=0.52).set_color(INK)
        handle = t("@HumanitariansAI", 38, INK, SANS, weight="BOLD")
        row = VGroup(VGroup(pill, pill_lab), hai, handle).arrange(RIGHT, buff=0.3)
        main = VGroup(title, row).arrange(DOWN, buff=0.55).move_to(UP * 1.45)
        clock.play_at(0.2, FadeIn(title, shift=UP * 0.15), run_time=0.8)
        clock.play_at(clock.t + 0.1, FadeIn(row, shift=UP * 0.1), run_time=0.6)

        rule = Line(LEFT * 3.4, RIGHT * 3.4, color=LINE, stroke_width=3).next_to(main, DOWN, buff=0.6)
        c1 = t("Boopesh M.", 46, INK, SERIF, weight="BOLD")
        c2 = t("Humanitarians AI Fellow · Brutalist team", 32, MUTED)
        c3 = t("Paper: Buehler, Gonon, Teichmann & Wood, Deep Hedging, Quantitative Finance (2019)", 20, MUTED)
        c3.scale_to_fit_width(min(c3.width, 11.8))
        c4 = t("Narration: AI voice (Kokoro am_onyx) reading Boopesh's script", 24, MUTED)
        credit = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.2).next_to(rule, DOWN, buff=0.45)
        clock.play_at(cue("B90", "With Boopesh", 1.5), Create(rule), FadeIn(credit, shift=UP * 0.1), run_time=0.7)
        clock.finish()
