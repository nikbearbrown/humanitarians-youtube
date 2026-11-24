# -*- coding: utf-8 -*-
"""
Manim scenes for "The Backtest Mirage" (16:9, 3840x2160) -- Boopesh M.
  B20_Noise    -- 7 years of a pure-noise market: 5 years searched, 2 years locked
  B30_Search   -- 10,000 rules, histogram of in-sample Sharpe ratios, the winner at 1.69
  B40_Unlock   -- the winner's equity curve: climbs in-sample, turns down out-of-sample
  B50_Climb    -- best in-sample Sharpe vs number of rules tried (200 noise markets); winners' OOS ~ 0
  B60_Why      -- one formula (Sharpe noise ~ 1/sqrt(years)) + the paper (Bailey et al., 2014)
  B70_Fix      -- the fix (count, hold out, demand more) + the bar to beat; honest limits
  B90_Outro    -- @HumanitariansAI outro + fellow credit
Every number is read from code/results.json and code/curves.npz, written by code/backtest_mirage.py
(SYNTHETIC NOISE DATA, zero true edge). Each scene lands on its beat's measured length.
"""
import json
from pathlib import Path

import numpy as np
from manim import *

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
CODE = HERE / "code"
if not (CODE / "results.json").exists():   # isolated copies (static pre-flight) fall back to the reel's data
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-08-backtest-mirage/code")
if not (ASSETS / "hai-logo.svg").exists():
    ASSETS = CODE.parent / "assets"

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"   # terracotta, WCAG 4.5:1+ on cream and panel
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
GHOST = "#A39A88"
TEAL = "#1F4E5F"     # data
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"
ON_DARK_MUTED = "#D8D0C0"
DARK_GHOST = "#5E544C"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

RES = json.loads((CODE / "results.json").read_text())
CUR = np.load(CODE / "curves.npz")
SET = RES["setup"]
MW = RES["main_world"]
WIN = MW["winner"]
WORLDS = {w["n"]: w for w in RES["worlds"]}
YEAR = SET["days_per_year"]
DIS, DOOS = SET["days_in_sample"], SET["days_out_of_sample"]
YIS, YOOS = int(SET["years_in_sample"]), int(SET["years_out_of_sample"])
NR = SET["n_rules"]
NW = SET["n_worlds"]


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


KERN = 3   # build text large, then scale down: Pango drops spaces / mis-kerns small text


def t(s, size=40, color=INK, font=SANS, weight="NORMAL", **kw):
    return Text(s, font=font, font_size=size * KERN, color=color, weight=weight, **kw).scale(1 / KERN)


def fit(m, w):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


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


def ghost_of(m, color=GHOST):
    return m.copy().set_fill(opacity=0).set_stroke(color, 3)


def sr(x, nd=2):
    """Sharpe ratio with a real minus sign."""
    return f"{x:+.{nd}f}".replace("-", "−").replace("+", "") if x < 0 else f"{x:.{nd}f}"


def comma(n):
    return f"{n:,}"


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


def polyline(fr, xs, ys, color, width=4):
    return VMobject(color=color, stroke_width=width).set_points_as_corners(
        [fr.p(x, y) for x, y in zip(xs, ys)])


def padlock(color=ON_DARK, h=0.5):
    body = RoundedRectangle(width=h * 0.9, height=h * 0.62, corner_radius=0.05, fill_color=color,
                            fill_opacity=1, stroke_width=0)
    shackle = Arc(radius=h * 0.28, start_angle=0, angle=PI, color=color, stroke_width=6)
    shackle.next_to(body, UP, buff=-0.02)
    return VGroup(shackle, body)


def locked_panel(fr, x0, x1, label="locked"):
    a, b = fr.p(x0, fr.y0), fr.p(x1, fr.y1)
    r = Rectangle(width=b[0] - a[0], height=b[1] - a[1] + 0.1, fill_color=DARK, fill_opacity=1, stroke_width=0)
    r.move_to([(a[0] + b[0]) / 2, (a[1] + b[1] + 0.1) / 2, 0])
    lab = VGroup(padlock(), t(label, 24, ON_DARK, weight="BOLD")).arrange(DOWN, buff=0.18).move_to(r)
    return VGroup(r, lab)


def downsample(y, n=500):
    idx = np.unique(np.linspace(0, len(y) - 1, n).astype(int))
    return idx, y[idx]


# ======================================================================== B20 =
class B20_Noise(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("synthetic noise data · zero real edge by construction", "A market with nothing to find")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        r = CUR["market"]
        price = 100 * np.cumprod(1 + r)
        days = np.arange(1, len(r) + 1) / YEAR
        lo, hi = float(price.min()), float(price.max())
        pad = (hi - lo) * 0.12
        fr = Frame(0, YIS + YOOS, lo - pad, hi + pad, (-5.7, 5.9, -2.0, 0.65))
        ax = fr.axes()
        ticks = VGroup(*[t(f"{y}", 18, MUTED, MONO).move_to(fr.p(y, fr.y0) + DOWN * 0.25)
                         for y in range(0, YIS + YOOS + 1)])
        xt = t("years →", 18, MUTED).next_to(fr.p(YIS + YOOS, fr.y0), DOWN, buff=0.5).align_to(ax, RIGHT)
        yt = t("price (starts at 100)", 18, MUTED).rotate(PI / 2).next_to(fr.p(0, (fr.y0 + fr.y1) / 2), LEFT,
                                                                          buff=0.25)
        i_is = days <= YIS
        idx, ys = downsample(price[i_is], 600)
        line_is = polyline(fr, days[i_is][idx], ys, TEAL, 4)
        lock = locked_panel(fr, YIS, YIS + YOOS, f"{YOOS} years · locked")

        # brackets under the axis
        def bracket(x0, x1, text, color):
            a, b = fr.p(x0, fr.y0), fr.p(x1, fr.y0)
            y = a[1] - 0.95
            ln = VGroup(Line([a[0] + 0.05, y, 0], [b[0] - 0.05, y, 0], color=color, stroke_width=5),
                        Line([a[0] + 0.05, y, 0], [a[0] + 0.05, y + 0.15, 0], color=color, stroke_width=5),
                        Line([b[0] - 0.05, y, 0], [b[0] - 0.05, y + 0.15, 0], color=color, stroke_width=5))
            lab = t(text, 22, color, weight="BOLD").next_to(ln, DOWN, buff=0.14)
            return VGroup(ln, lab)

        br_is = bracket(0, YIS, f"in-sample: {YIS} years the search may look at", TEAL)
        br_oos = bracket(YIS, YIS + YOOS, "out-of-sample", ACCENT)
        tag = card(4.3, 0.95, fill=PANEL)
        tag_t = VGroup(t("daily returns = random noise", 21, INK, weight="BOLD"),
                       t("no rule can have a real edge", 19, MUTED)).arrange(DOWN, buff=0.08)
        tag_g = VGroup(tag, tag_t.move_to(tag)).move_to([fr.L + 2.35, 1.3, 0])

        clock.play_at(0.4, FadeIn(ax.copy().set_color(GHOST)), FadeIn(ghost_of(lock[0])), run_time=0.6)
        clock.play_at(cue("B20", "I generated", 2.5), Create(ax), FadeIn(ticks), FadeIn(xt), FadeIn(yt), run_time=0.6)
        clock.play_at(clock.t, Create(line_is), run_time=2.2)
        clock.play_at(cue("B20", "Synthetic noise", 8.0), FadeIn(tag_g, shift=DOWN * 0.1), run_time=0.6)
        clock.play_at(cue("B20", "The search may", 11.0), FadeIn(br_is, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B20", "The last two", 13.5), FadeIn(lock), FadeIn(br_oos, shift=UP * 0.1), run_time=0.7)
        clock.finish()


# ======================================================================== B30 =
class B30_Search(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header(f"the search · {comma(NR)} rules · {YIS} years of synthetic noise", "Ten thousand tries")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        # left: what a rule is
        lc = card(4.1, 4.6).move_to([-4.15, -0.55, 0])
        items = VGroup(
            VGroup(t(comma(NR), 54, INK, SERIF, weight="BOLD"), t("simple trading rules", 21, MUTED)).arrange(
                DOWN, aligned_edge=LEFT, buff=0.05),
            VGroup(t("each rule", 24, INK, weight="BOLD"), t("looks at the last 2–20 days,", 20, MUTED),
                   t("then goes long or short", 20, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.06),
            VGroup(t("its score", 24, INK, weight="BOLD"), t("Sharpe ratio =", 20, MUTED),
                   t("return per unit of risk", 20, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.06))
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        fit(items, 3.6).move_to(lc)

        # right: histogram of in-sample Sharpe ratios
        s = CUR["is_sharpe"]
        edges = np.arange(-2.0, 2.0001, 0.1)
        cnt, _ = np.histogram(s, bins=edges)
        ymax = cnt.max() * 1.12
        fr = Frame(-2.0, 2.0, 0, ymax, (-1.4, 5.9, -2.15, 1.1))
        ax = VGroup(Line(fr.p(-2.0, 0), fr.p(2.0, 0) + RIGHT * 0.1, color=INK, stroke_width=3))
        bars = VGroup()
        for c, e in zip(cnt, edges[:-1]):
            if c == 0:
                continue
            a, b = fr.p(e, 0), fr.p(e + 0.1, c)
            bars.add(Rectangle(width=(b[0] - a[0]) * 0.9, height=b[1] - a[1], fill_color=TEAL, fill_opacity=1,
                               stroke_width=0).move_to([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0]))
        ticks = VGroup(*[t(sr(v, 0) if v else "0", 18, MUTED, MONO).move_to(fr.p(v, 0) + DOWN * 0.25)
                         for v in (-2, -1, 0, 1, 2)])
        xt = t(f"in-sample Sharpe ratio ({YIS} years)", 20, MUTED).move_to(fr.p(0, 0) + DOWN * 0.62)
        good = DashedLine(fr.p(1, 0), fr.p(1, ymax * 0.97), color=INK, stroke_width=3, dash_length=0.1)
        good_l = t("above 1: usually called good", 19, INK).next_to(good, UP, buff=0.1)
        frame_ghost = Rectangle(width=fr.R - fr.L, height=fr.T - fr.B, stroke_color=GHOST, stroke_width=3,
                                fill_opacity=0).move_to([(fr.L + fr.R) / 2, (fr.B + fr.T) / 2, 0])
        wx = WIN["is_sharpe"]
        wdot = Dot(fr.p(wx, 0) + UP * 0.12, radius=0.12, color=ACCENT)
        warrow = Arrow(fr.p(wx, 0) + UP * 1.55, fr.p(wx, 0) + UP * 0.3, color=ACCENT, buff=0, stroke_width=6,
                       max_tip_length_to_length_ratio=0.25)
        wlab = VGroup(t(f"best of {comma(NR)}", 20, ACCENT, weight="BOLD"),
                      t(sr(wx), 40, ACCENT, SERIF, weight="BOLD")).arrange(DOWN, buff=0.04)
        wlab.next_to(warrow, UP, buff=0.08)
        most = t("most land near 0", 20, TEAL, weight="BOLD").move_to(fr.p(-1.25, cnt.max() * 0.75))
        verdict = t("…on pure noise", 26, ACCENT, weight="BOLD").move_to([4.6, -3.1, 0])

        clock.play_at(0.4, FadeIn(ghost_of(lc)), FadeIn(frame_ghost), run_time=0.6)
        clock.play_at(cue("B30", "It tries", 1.0), FadeIn(lc), FadeIn(items[0], shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B30", "Each looks", 4.0), FadeIn(items[1], shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B30", "Each gets", 7.0), FadeIn(items[2], shift=UP * 0.1), FadeOut(frame_ghost),
                      Create(ax), FadeIn(ticks), FadeIn(xt), run_time=0.6)
        clock.play_at(cue("B30", "Above one", 10.0), Create(good), FadeIn(good_l), run_time=0.6)
        clock.play_at(cue("B30", "Most rules", 12.0), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars],
                                                                    lag_ratio=0.03), FadeIn(most), run_time=1.4)
        clock.play_at(cue("B30", "But the best", 15.5), FadeIn(wdot, scale=0.5), GrowArrow(warrow), FadeIn(wlab),
                      run_time=0.7)
        clock.play_at(cue("B30", "On pure noise", 19.0), FadeIn(verdict, shift=UP * 0.1), run_time=0.5)
        clock.finish()


# ======================================================================== B40 =
class B40_Unlock(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        hd = header(f"the winner, rule #{WIN['rule']} · synthetic noise data", "Unlock the last two years")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        pnl = CUR["winner_pnl"]
        cum = 100 * np.cumsum(pnl)
        days = np.arange(1, len(pnl) + 1) / YEAR
        lo, hi = min(0.0, float(cum.min())), float(cum.max())
        pad = (hi - lo) * 0.1
        fr = Frame(0, YIS + YOOS, lo - pad, hi + pad, (-5.1, 2.2, -2.3, 1.2))
        ax = fr.axes()
        zero = DashedLine(fr.p(0, 0), fr.p(YIS + YOOS, 0), color=GHOST, stroke_width=2, dash_length=0.08)
        ticks = VGroup(*[t(f"{y}", 18, MUTED, MONO).move_to(fr.p(y, fr.y0) + DOWN * 0.25)
                         for y in range(0, YIS + YOOS + 1)])
        xt = t("years →", 18, MUTED).next_to(fr.p(YIS + YOOS, fr.y0), DOWN, buff=0.5).align_to(ax, RIGHT)
        yt = t("total return (sum of daily %)", 18, MUTED).next_to(fr.p(0, fr.y1), UP, buff=0.2).align_to(
            fr.p(0, 0), LEFT).shift(LEFT * 0.1)
        ylab = VGroup(*[t(f"{v:+.0f}%".replace("-", "−") if v else "0%", 18, MUTED, MONO).next_to(fr.p(0, v), LEFT,
                                                                                               buff=0.1)
                        for v in (0, 100)])
        i_is = np.arange(len(pnl)) < DIS
        idx, ys = downsample(cum[i_is], 500)
        l_is = polyline(fr, days[i_is][idx], ys, TEAL, 5)
        oos_x = np.concatenate([[days[DIS - 1]], days[~i_is]])
        oos_y = np.concatenate([[cum[DIS - 1]], cum[~i_is]])
        idx2, ys2 = downsample(oos_y, 250)
        l_oos = polyline(fr, oos_x[idx2], ys2, ACCENT, 5)
        lock = locked_panel(fr, YIS, YIS + YOOS, "locked")
        div = DashedLine(fr.p(YIS, fr.y0), fr.p(YIS, fr.y1), color=INK, stroke_width=2, dash_length=0.08)
        ylow = 0.2 * hi
        lab_is = t("searched", 22, TEAL, weight="BOLD").move_to(fr.p(YIS * 0.72, ylow))
        lab_oos = t("never seen", 22, ACCENT, weight="BOLD").move_to(fr.p(YIS + YOOS / 2, ylow))

        def stat(title, value, color, sub):
            c = card(3.7, 1.75)
            g = VGroup(t(title, 21, MUTED), t(value, 60, color, SERIF, weight="BOLD"), t(sub, 18, MUTED)).arrange(
                DOWN, buff=0.06)
            return VGroup(c, fit(g, 3.4).move_to(c))

        s_is = stat("in-sample Sharpe", sr(WIN["is_sharpe"]), TEAL, f"first {YIS} years")
        s_oos = stat("out-of-sample Sharpe", sr(WIN["oos_sharpe"]), ACCENT, f"last {YOOS} years")
        stats = VGroup(s_is, s_oos).arrange(DOWN, buff=0.3).move_to([4.45, -0.45, 0])
        verdict = t("the brilliant backtest was a mirage", 26, ACCENT, weight="BOLD")
        verdict.move_to([(fr.L + fr.R) / 2, -3.2, 0])

        clock.play_at(0.3, FadeIn(ax.copy().set_color(GHOST)), FadeIn(VGroup(*[ghost_of(s[0]) for s in stats])),
                      run_time=0.5)
        clock.play_at(0.8, Create(ax), FadeIn(ticks), FadeIn(xt), FadeIn(yt), FadeIn(ylab), FadeIn(zero),
                      FadeIn(lock), Create(l_is), FadeIn(lab_is), FadeIn(s_is), run_time=1.4)
        clock.play_at(cue("B40", "Now unlock", 0.5) + 1.6, FadeOut(lock), Create(div), FadeIn(lab_oos), run_time=0.7)
        clock.play_at(cue("B40", "stalls", 5.0), Create(l_oos), run_time=1.6)
        clock.play_at(cue("B40", "Out of sample", 7.5), FadeIn(s_oos, shift=LEFT * 0.15), run_time=0.6)
        clock.play_at(cue("B40", "The brilliant", 10.0), FadeIn(verdict, shift=UP * 0.1), run_time=0.6)
        clock.finish()


# ======================================================================== B50 =
class B50_Climb(Scene):
    def construct(self):
        clock = Clock(self, "B50")
        hd = header(f"same search, {NW} fresh noise markets", "The more you test, the better it looks")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        ns = RES["n_show"]
        fr = Frame(-0.5, len(ns) - 0.5, -0.45, 2.0, (-5.5, 2.4, -2.2, 1.25))
        base = Line(fr.p(-0.5, 0), fr.p(len(ns) - 0.5, 0), color=INK, stroke_width=3)
        yax = Line(fr.p(-0.5, -0.45), fr.p(-0.5, 2.0), color=INK, stroke_width=3)
        ylab = VGroup(*[t(f"{v:g}", 18, MUTED, MONO).next_to(fr.p(-0.5, v), LEFT, buff=0.1) for v in (0, 1, 2)])
        grid = VGroup(*[DashedLine(fr.p(-0.5, v), fr.p(len(ns) - 0.5, v), color=LINE, stroke_width=2,
                                   dash_length=0.08) for v in (1, 2)])
        yt = t("Sharpe ratio", 18, MUTED).rotate(PI / 2).next_to(ylab, LEFT, buff=0.15)
        bw = 0.95
        bars, vals, frames, xl = VGroup(), VGroup(), VGroup(), VGroup()
        for i, n in enumerate(ns):
            v = WORLDS[n]["best_is_median"]
            a, b = fr.p(i - bw / 2, 0), fr.p(i + bw / 2, v)
            h = abs(b[1] - a[1])
            bar = Rectangle(width=b[0] - a[0], height=max(h, 0.02), fill_color=TEAL, fill_opacity=1, stroke_width=0)
            bar.move_to([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0])
            bars.add(bar)
            if v > 0.45:
                lab = t(sr(v), 30, ON_DARK, SERIF, weight="BOLD").move_to(fr.p(i, v) + DOWN * 0.3)
            else:
                lab = t(sr(v), 30, TEAL, SERIF, weight="BOLD").move_to(fr.p(i, max(v, 0)) + UP * 0.3)
            vals.add(lab)
            top = fr.p(i + bw / 2, 2.0)
            frames.add(Rectangle(width=b[0] - a[0], height=top[1] - a[1], stroke_color=GHOST, stroke_width=2,
                                 fill_opacity=0).move_to([(a[0] + b[0]) / 2, (a[1] + top[1]) / 2, 0]))
            xl.add(t(comma(n), 22, INK, weight="BOLD").move_to(fr.p(i, -0.45) + DOWN * 0.28))
        xt = t("rules tried, keep the best", 20, MUTED).next_to(xl, DOWN, buff=0.15)
        oos_pts = [fr.p(i, WORLDS[n]["winner_oos_mean"]) for i, n in enumerate(ns)]
        oos_line = VMobject(color=ACCENT, stroke_width=5).set_points_as_corners(oos_pts)
        oos_dots = VGroup(*[Dot(p, radius=0.09, color=ACCENT) for p in oos_pts])

        # right column: legend + readout
        rc = card(3.4, 4.2).move_to([4.65, -0.45, 0])
        leg = VGroup(
            VGroup(Square(0.28, fill_color=TEAL, fill_opacity=1, stroke_width=0),
                   VGroup(t("best in-sample", 20, INK, weight="BOLD"),
                          t(f"median of {NW} markets", 17, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
                   ).arrange(RIGHT, buff=0.18, aligned_edge=UP),
            VGroup(Dot(radius=0.11, color=ACCENT),
                   VGroup(t("same winner,", 20, INK, weight="BOLD"), t("out-of-sample", 20, INK, weight="BOLD"),
                          t("average", 17, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
                   ).arrange(RIGHT, buff=0.18, aligned_edge=UP))
        leg.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        last = WORLDS[ns[-1]]
        read = VGroup(t(f"best of {comma(ns[-1])}:", 19, MUTED),
                      t(f"{sr(last['best_is_median'])} → {sr(last['winner_oos_mean'])}", 30, INK, SERIF,
                        weight="BOLD")).arrange(DOWN, aligned_edge=LEFT, buff=0.05)
        rbody = VGroup(leg, read).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        fit(rbody, 3.0).move_to(rc)

        clock.play_at(0.4, FadeIn(frames), FadeIn(ghost_of(rc)), run_time=0.6)
        clock.play_at(cue("B50", "I repeated", 2.0), Create(base), Create(yax), FadeIn(ylab), FadeIn(grid),
                      FadeIn(yt), FadeIn(xl), FadeIn(xt), FadeIn(rc), FadeIn(leg[0]), run_time=0.7)
        for i, p in enumerate(["Best of one", "Best of ten:", "Best of a hundred", None, "Best of ten thousand"]):
            if p is None:
                at = clock.t + 0.2
            else:
                at = max(clock.t, cue("B50", p, 6.0 + 2.5 * i))
            d = DOWN if WORLDS[ns[i]]["best_is_median"] >= 0 else UP
            clock.play_at(at, GrowFromEdge(bars[i], d), FadeIn(vals[i]), run_time=0.5)
        clock.play_at(cue("B50", "Out of sample", 17.0), Create(oos_line), FadeIn(oos_dots), FadeIn(leg[1]),
                      FadeIn(read), run_time=0.9)
        clock.play_at(cue("B50", "The more you test", 20.0),
                      Indicate(vals[-1], color=ACCENT, scale_factor=1.15), run_time=0.8)
        clock.finish()


# ======================================================================== B60 =
class B60_Why(Scene):
    def construct(self):
        clock = Clock(self, "B60")
        hd = header("why it happens · backtest overfitting", "The winner is the luckiest noise")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        se = SET["sharpe_se_theory"]
        # left: the formula + a bell curve of zero-edge Sharpe ratios
        f1 = svg("eq_noise_ink.svg", height=0.95)
        f2 = svg("eq_five_ink.svg", height=0.8)
        form = VGroup(f1, f2).arrange(RIGHT, buff=0.25)
        fit(form, 6.0).move_to([-3.2, 1.0, 0])
        fr = Frame(-2.0, 2.0, 0, 1.0, (-6.0, -0.4, -2.25, -0.1))
        xs = np.linspace(-2, 2, 301)
        ys = np.exp(-0.5 * (xs / se) ** 2)
        curve = polyline(fr, xs, ys, TEAL, 5)
        band_x = np.linspace(-se, se, 120)
        band = Polygon(*([fr.p(x, 0) for x in band_x[::-1]] + [fr.p(x, np.exp(-0.5 * (x / se) ** 2)) for x in band_x]),
                       fill_color=TEAL, fill_opacity=0.25, stroke_width=0)
        base = Line(fr.p(-2, 0), fr.p(2, 0), color=INK, stroke_width=3)
        ticks = VGroup(*[t(sr(v, 0) if v else "0", 18, MUTED, MONO).move_to(fr.p(v, 0) + DOWN * 0.25)
                         for v in (-2, -1, 0, 1, 2)])
        band_l = t(f"±{se:.2f}", 22, TEAL, weight="BOLD").move_to(fr.p(0, 0.45))
        cap = t("Sharpe of a rule with zero real edge, 5 years", 18, MUTED).move_to(fr.p(0, 0) + DOWN * 0.62)
        wx = WIN["is_sharpe"]
        wline = Line(fr.p(wx, 0), fr.p(wx, 0.62), color=ACCENT, stroke_width=6)
        wlab = VGroup(t(f"best of {comma(NR)}: {sr(wx)}", 20, ACCENT, weight="BOLD"),
                      t(f"= {wx / se:.1f} noise-widths up", 18, ACCENT)).arrange(DOWN, buff=0.05)
        wlab.next_to(wline, UP, buff=0.1).shift(LEFT * 0.35)
        meas = t(f"measured spread across all rules: {RES['worlds_is_sharpe_sd_mean']:.2f}", 18, MUTED)
        meas.next_to(form, DOWN, buff=0.2)

        # right: the paper
        pc = card(5.6, 4.6, fill=DARK).move_to([3.3, -0.9, 0])
        w45 = WORLDS[45]
        paper = VGroup(
            t("Bailey, Borwein, López de Prado & Zhu", 22, ON_DARK, weight="BOLD"),
            t("Pseudo-Mathematics and Financial Charlatanism", 18, ON_DARK_MUTED, slant="ITALIC"),
            t("Notices of the AMS 61(5), 2014", 18, ON_DARK_MUTED))
        paper.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        name = t("“backtest overfitting”", 30, ON_DARK, SERIF, weight="BOLD")
        warn = VGroup(t("their warning:", 19, ON_DARK_MUTED),
                      t(f"{YIS} years of data + about 45 tries", 22, ON_DARK, weight="BOLD"),
                      t("→ a Sharpe near 1, by luck", 22, ON_DARK, weight="BOLD")).arrange(DOWN, aligned_edge=LEFT,
                                                                                          buff=0.08)
        mine = VGroup(t(f"my run, best of 45: {sr(w45['best_is_median'])}", 20, ON_DARK, weight="BOLD"),
                      t(f"(median of {NW} noise markets)", 17, ON_DARK_MUTED)).arrange(DOWN, aligned_edge=LEFT,
                                                                                    buff=0.05)
        body = VGroup(paper, name, warn, mine).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        fit(body, 5.0)
        if body.height > 4.2:
            body.scale_to_fit_height(4.2)
        body.move_to(pc)

        clock.play_at(0.4, FadeIn(ghost_of(pc, DARK_GHOST)), FadeIn(base.copy().set_color(GHOST)), run_time=0.5)
        clock.play_at(cue("B60", "A Sharpe ratio", 0.8), FadeIn(form[0], shift=UP * 0.1), Create(base),
                      FadeIn(ticks), FadeIn(cap), run_time=0.6)
        clock.play_at(clock.t, Create(curve), run_time=1.0)
        clock.play_at(cue("B60", "point four five", 5.0), FadeIn(form[1]), FadeIn(band), FadeIn(band_l), FadeIn(meas),
                      run_time=0.6)
        clock.play_at(cue("B60", "Test many rules", 8.0), Create(wline), FadeIn(wlab), run_time=0.7)
        clock.play_at(cue("B60", "Bailey", 12.0), FadeIn(pc), FadeIn(paper), FadeIn(name), run_time=0.7)
        clock.play_at(cue("B60", "Their warning", 18.0), FadeIn(warn, shift=UP * 0.1), run_time=0.6)
        clock.play_at(clock.t + 1.5, FadeIn(mine, shift=UP * 0.1), run_time=0.5)
        clock.finish()


# ======================================================================== B70 =
class B70_Fix(Scene):
    def construct(self):
        clock = Clock(self, "B70")
        hd = header("the fix + honest limits", "Count, hold out, demand more")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        L = card(5.9, 4.3, fill=DARK).move_to([-3.25, -0.5, 0])
        steps = [("1", "count your trials", "and report how many"),
                 ("2", "hold out data", "never touch it until the end"),
                 ("3", "demand more", "as you test more")]
        rows = VGroup()
        for n, a, b in steps:
            num = t(n, 44, ACCENT if False else ON_DARK, SERIF, weight="BOLD")
            txt = VGroup(t(a, 30, ON_DARK, SERIF, weight="BOLD"), t(b, 20, ON_DARK_MUTED)).arrange(
                DOWN, aligned_edge=LEFT, buff=0.05)
            rows.add(VGroup(num, txt).arrange(RIGHT, buff=0.35, aligned_edge=UP))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        fit(rows, 5.2).move_to(L)

        # right: the bar to beat (95th percentile of the best in-sample Sharpe on pure noise)
        R = card(5.9, 4.3).move_to([3.25, -0.5, 0])
        rt = t("the bar to beat", 24, INK, weight="BOLD")
        rs = t(f"95% of noise searches stay below it", 18, MUTED)
        rhead = VGroup(rt, rs).arrange(DOWN, buff=0.06).move_to(R.get_top() + DOWN * 0.55)
        fr = Frame(-1.3, 1.5, 0, 2.2, (0.65, 5.85, -2.25, 0.55))
        base = Line(fr.p(-1.3, 0), fr.p(1.5, 0), color=INK, stroke_width=3)
        b1, b2 = WORLDS[1]["best_is_p95"], WORLDS[NR]["best_is_p95"]
        bars, labs, xl = VGroup(), VGroup(), VGroup()
        for i, (v, n) in enumerate(((b1, 1), (b2, NR))):
            a, b = fr.p(i - 0.3, 0), fr.p(i + 0.3, v)
            bars.add(Rectangle(width=b[0] - a[0], height=b[1] - a[1], fill_color=TEAL, fill_opacity=1,
                               stroke_width=0).move_to([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0]))
            labs.add(t(sr(v), 30, TEAL, SERIF, weight="BOLD").next_to(bars[-1], UP, buff=0.08))
            xl.add(t(f"{comma(n)} rule{'s' if n > 1 else ''} tried", 18, INK).move_to(fr.p(i, 0) + DOWN * 0.27))
        wv = WIN["is_sharpe"]
        wl = DashedLine(fr.p(-1.25, wv), fr.p(1.45, wv), color=ACCENT, stroke_width=4, dash_length=0.1)
        wlab = VGroup(t("our winner", 19, ACCENT, weight="BOLD"), t(sr(wv), 30, ACCENT, SERIF, weight="BOLD"),
                      t("rejected", 18, ACCENT)).arrange(DOWN, aligned_edge=LEFT, buff=0.03)
        wlab.next_to(fr.p(-1.25, wv), DOWN, buff=0.12).align_to(fr.p(-1.25, wv), LEFT)
        lim = VGroup(t("limits:", 20, MUTED, weight="BOLD"),
                     t("synthetic noise · no trading costs · real markets may hide small real edges", 20, MUTED)
                     ).arrange(RIGHT, buff=0.15).move_to([0, -3.15, 0])
        fit(lim, 12.4)

        clock.play_at(0.3, FadeIn(ghost_of(L, DARK_GHOST)), FadeIn(ghost_of(R)), run_time=0.5)
        clock.play_at(cue("B70", "So here's", 0.8), FadeIn(L), run_time=0.4)
        for i, p in enumerate(["Count your", "Hold out", "And demand"]):
            clock.play_at(max(clock.t, cue("B70", p, 2.0 + 2.5 * i)), FadeIn(rows[i], shift=RIGHT * 0.15),
                          run_time=0.45)
        clock.play_at(cue("B70", "In my noise", 9.0), FadeIn(R), FadeIn(rhead), Create(base), FadeIn(xl),
                      GrowFromEdge(bars[0], DOWN), FadeIn(labs[0]), run_time=0.7)
        clock.play_at(cue("B70", "With ten thousand", 13.0), GrowFromEdge(bars[1], DOWN), FadeIn(labs[1]), run_time=0.6)
        clock.play_at(cue("B70", "so our one", 15.5), Create(wl), FadeIn(wlab), run_time=0.6)
        clock.play_at(cue("B70", "Limits", 19.0), FadeIn(lim, shift=UP * 0.1), run_time=0.5)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = t("The Backtest Mirage", 80, INK, SERIF)
        title.scale_to_fit_width(min(title.width, 11.0))
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
        c3 = t("Data: synthetic noise made in code · Paper: Bailey, Borwein, López de Prado & Zhu, "
               "Notices of the AMS (2014)", 20, MUTED)
        c3.scale_to_fit_width(min(c3.width, 11.8))
        c4 = t("Narration: AI voice (Kokoro am_onyx) reading Boopesh's script", 24, MUTED)
        credit = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.2).next_to(rule, DOWN, buff=0.45)
        dim = VGroup(rule, credit).copy().set_opacity(0.18)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(max(clock.t, cue("B90", "With Boopesh", 1.5)), FadeOut(dim), Create(rule),
                      FadeIn(credit, shift=UP * 0.1), run_time=0.7)
        clock.finish()
