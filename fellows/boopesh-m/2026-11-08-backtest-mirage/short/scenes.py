# -*- coding: utf-8 -*-
"""
Manim scenes for the 9:16 Short of "The Backtest Mirage" (2160x3840) -- Boopesh M.
  B10_Climb   -- best in-sample Sharpe of 1 / 100 / 10,000 rules tried on pure noise (200 noise markets)
  B20_Unlock  -- the 10,000-rule winner: climbs in-sample, stalls and slips on the 2 locked years
  B30_Fix     -- count your trials, hold out data, demand more as you test more; limits
  B90_Outro   -- @HumanitariansAI outro + fellow credit
Native portrait layouts (frame 4.5 x 8 units). Numbers read from ../code/results.json and ../code/curves.npz
(SYNTHETIC NOISE DATA, zero true edge).
"""
import json
from pathlib import Path

import numpy as np
from manim import *

config.frame_width = 4.5
config.frame_height = 8.0

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
CODE = HERE.parent / "code"
if not (CODE / "results.json").exists():   # isolated copies (static pre-flight) fall back to the reel's data
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-08-backtest-mirage/code")
if not (ASSETS / "hai-logo.svg").exists():
    ASSETS = CODE.parent / "short" / "assets"

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
GHOST = "#A39A88"
TEAL = "#1F4E5F"
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"
ON_DARK_MUTED = "#D8D0C0"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

CX = -0.15
SAFE_W = 3.7

RES = json.loads((CODE / "results.json").read_text())
CUR = np.load(CODE / "curves.npz")
SET = RES["setup"]
WIN = RES["main_world"]["winner"]
WORLDS = {w["n"]: w for w in RES["worlds"]}
YEAR = SET["days_per_year"]
DIS = SET["days_in_sample"]
YIS, YOOS = int(SET["years_in_sample"]), int(SET["years_out_of_sample"])
NW = SET["n_worlds"]


def _sheet():
    try:
        return {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}
    except Exception:
        return {}


BEATS = _sheet()


def beat_len(bid, default=8.0):
    b = BEATS.get(bid, {})
    return float(b.get("render_duration_s") or b.get("actual_duration_s") or default)


def cue(bid, phrase, default):
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

    def play_at(self, at, *anims, run_time=0.7, **kw):
        if at > self.t:
            self.scene.wait(at - self.t)
            self.t = at
        self.scene.play(*anims, run_time=run_time, **kw)
        self.t += run_time

    def finish(self):
        end = beat_len(self.bid)
        if end - self.t > 1 / 24:
            self.scene.wait(end - self.t)


TYPE_SCALE = 0.72
KERN = 4


def t(s, size=24, color=INK, font=SANS, weight="NORMAL", **kw):
    m = Text(s, font=font, font_size=size * TYPE_SCALE * KERN, color=color, weight=weight, **kw)
    return m.scale(1 / KERN)


def fit(m, w=SAFE_W):
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


def card(w, h, fill=PANEL):
    return RoundedRectangle(width=w, height=h, corner_radius=0.08, fill_color=fill,
                            fill_opacity=1, stroke_width=0)


def ghost_of(m, color=GHOST):
    return m.copy().set_fill(opacity=0).set_stroke(color, 2)


def sr(x, nd=2):
    return f"{x:.{nd}f}".replace("-", "−")


def comma(n):
    return f"{n:,}"


def header(kicker, title):
    k = fit(t(kicker.upper(), 13, MUTED, MONO))
    h = fit(t(title, 34, INK, SERIF, weight="BOLD", line_spacing=0.9))
    g = VGroup(k, h).arrange(DOWN, buff=0.12)
    g.move_to([CX, 3.1 - g.height / 2, 0])
    return g


# ======================================================================== B10 =
class B10_Climb(Scene):
    def construct(self):
        clock = Clock(self, "B10")
        hd = header("synthetic noise data · zero real edge", "Best Sharpe found\nby the search")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        ns = [1, 100, 10_000]
        x0, x1 = CX - 1.6, CX + 1.6
        yb, yt = -1.9, 1.5           # baseline (Sharpe 0) .. Sharpe 2.0
        sc = (yt - yb) / 2.0
        xs = np.linspace(x0 + 0.5, x1 - 0.5, len(ns))
        base = Line([x0, yb, 0], [x1, yb, 0], color=INK, stroke_width=4)
        good = DashedLine([x0, yb + sc, 0], [x1, yb + sc, 0], color=GHOST, stroke_width=3, dash_length=0.08)

        bars, labs, frames, xl = VGroup(), VGroup(), VGroup(), VGroup()
        for x, n in zip(xs, ns):
            v = WORLDS[n]["best_is_median"]
            h = max(abs(v) * sc, 0.03)
            bar = Rectangle(width=0.85, height=h, fill_color=TEAL, fill_opacity=1, stroke_width=0)
            bar.move_to([x, yb + (h / 2 if v >= 0 else -h / 2), 0])
            bars.add(bar)
            if v > 0.45:
                labs.add(t(sr(v), 30, ON_DARK, SERIF, weight="BOLD").move_to([x, yb + v * sc - 0.28, 0]))
            else:
                labs.add(t(sr(v), 30, TEAL, SERIF, weight="BOLD").move_to([x, yb + 0.32, 0]))
            frames.add(Rectangle(width=0.85, height=2.0 * sc, stroke_color=GHOST, stroke_width=2,
                                 fill_opacity=0).move_to([x, yb + sc, 0]))
            xl.add(VGroup(t(comma(n), 24, INK, weight="BOLD"),
                          t("rule" if n == 1 else "rules", 16, MUTED)).arrange(DOWN, buff=0.03).move_to([x, yb - 0.45, 0]))
        cap = VGroup(t(f"median of {NW} noise markets", 16, MUTED),
                     t("dashed line: Sharpe 1, usually called good", 16, MUTED)).arrange(DOWN, buff=0.05)
        fit(cap).next_to(xl, DOWN, buff=0.2).set_x(CX)

        clock.play_at(0.3, FadeIn(frames), Create(base), FadeIn(xl), run_time=0.5)
        clock.play_at(cue("B10", "where no real", 2.5), Create(good), FadeIn(cap), run_time=0.5)
        for i, p in enumerate(["Best of one", "Best of a hundred", "Best of ten thousand"]):
            d = DOWN if WORLDS[ns[i]]["best_is_median"] >= 0 else UP
            clock.play_at(max(clock.t, cue("B10", p, 5.0 + 2.5 * i)), GrowFromEdge(bars[i], d), FadeIn(labs[i]),
                          run_time=0.5)
        clock.finish()


# ======================================================================== B20 =
class B20_Unlock(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("best of 10,000 rules · synthetic noise", "Then: new data")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        pnl = CUR["winner_pnl"]
        cum = 100 * np.cumsum(pnl)
        days = np.arange(1, len(pnl) + 1) / YEAR
        lo, hi = min(0.0, float(cum.min())), float(cum.max())
        L, R, B, T = CX - 1.75, CX + 1.75, -0.35, 1.75

        def p(x, y):
            return np.array([L + x / (YIS + YOOS) * (R - L), B + (y - lo) / (hi - lo) * (T - B), 0.0])

        ax = VGroup(Line(p(0, lo) + DOWN * 0.05, p(YIS + YOOS, lo) + DOWN * 0.05, color=INK, stroke_width=3))
        idx = np.unique(np.linspace(0, DIS - 1, 300).astype(int))
        l_is = VMobject(color=TEAL, stroke_width=4).set_points_as_corners([p(days[i], cum[i]) for i in idx])
        idx2 = np.unique(np.linspace(DIS - 1, len(cum) - 1, 150).astype(int))
        l_oos = VMobject(color=ACCENT, stroke_width=4).set_points_as_corners([p(days[i], cum[i]) for i in idx2])
        div = DashedLine(p(YIS, lo), p(YIS, hi), color=INK, stroke_width=2, dash_length=0.06)
        lock_r = Rectangle(width=p(YIS + YOOS, 0)[0] - p(YIS, 0)[0], height=T - B + 0.1, fill_color=DARK,
                           fill_opacity=1, stroke_width=0).move_to([(p(YIS, 0)[0] + R) / 2, (B + T) / 2, 0])
        lock_t = t("locked", 16, ON_DARK, weight="BOLD").move_to(lock_r)
        tl = VGroup(t(f"{YIS} years", 16, TEAL, weight="BOLD").move_to(p(YIS / 2, lo) + DOWN * 0.3),
                    t(f"{YOOS} new", 16, ACCENT, weight="BOLD").move_to(p(YIS + YOOS / 2, lo) + DOWN * 0.3))

        def stat(title, value, color):
            c = card(1.75, 1.25)
            g = VGroup(t(title, 15, MUTED), t(value, 40, color, SERIF, weight="BOLD")).arrange(DOWN, buff=0.04)
            return VGroup(c, fit(g, 1.55).move_to(c))

        s1 = stat("Sharpe, searched", sr(WIN["is_sharpe"]), TEAL)
        s2 = stat("Sharpe, new data", sr(WIN["oos_sharpe"]), ACCENT)
        stats = VGroup(s1, s2).arrange(RIGHT, buff=0.2).move_to([CX, -1.55, 0])
        w = WORLDS[10_000]
        avg = VGroup(t(f"{NW} noise markets:", 16, MUTED),
                     t(f"winners average {sr(w['winner_oos_mean'])} on new data", 18, INK, weight="BOLD")).arrange(
            DOWN, buff=0.05)
        fit(avg).next_to(stats, DOWN, buff=0.25).set_x(CX)

        clock.play_at(0.3, FadeIn(ghost_of(VGroup(s1[0], s2[0]))), Create(ax), FadeIn(lock_r), FadeIn(lock_t),
                      FadeIn(tl), run_time=0.5)
        clock.play_at(0.8, Create(l_is), FadeIn(s1), run_time=1.2)
        clock.play_at(cue("B20", "two years it never", 2.5), FadeOut(lock_r), FadeOut(lock_t), Create(div),
                      run_time=0.5)
        clock.play_at(clock.t, Create(l_oos), run_time=1.2)
        clock.play_at(cue("B20", "Its Sharpe", 4.5), FadeIn(s2, scale=0.95), run_time=0.5)
        clock.play_at(cue("B20", "Across two hundred", 6.0), FadeIn(avg, shift=UP * 0.08), run_time=0.5)
        clock.finish()


# ======================================================================== B30 =
class B30_Fix(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("the fix", "Don't trust the\nluckiest backtest")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        box = card(SAFE_W, 3.7, fill=DARK).move_to([CX, -0.15, 0])
        rows = VGroup()
        for n, a, b in (("1", "count your trials", "and report them"), ("2", "hold out data", "never touch it early"),
                        ("3", "demand more", "as you test more")):
            rows.add(VGroup(t(n, 34, ON_DARK, SERIF, weight="BOLD"),
                            VGroup(t(a, 28, ON_DARK, SERIF, weight="BOLD"), t(b, 17, ON_DARK_MUTED)).arrange(
                                DOWN, aligned_edge=LEFT, buff=0.03)).arrange(RIGHT, buff=0.22, aligned_edge=UP))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        fit(rows, SAFE_W - 0.5).move_to(box)
        lim = VGroup(t("limits: synthetic noise,", 16, MUTED),
                     t("no trading costs", 16, MUTED)).arrange(DOWN, buff=0.05).next_to(box, DOWN, buff=0.2)
        lim.set_x(CX)

        clock.play_at(0.3, FadeIn(ghost_of(box, "#5E544C")), FadeIn(lim), run_time=0.4)
        clock.play_at(0.6, FadeIn(box), run_time=0.4)
        for i, p in enumerate(["count your", "hold out", "demand more"]):
            clock.play_at(max(clock.t, cue("B30", p, 1.0 + 1.5 * i)), FadeIn(rows[i], shift=UP * 0.08), run_time=0.4)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = fit(VGroup(t("The Backtest", 46, INK, SERIF), t("Mirage", 46, INK, SERIF)).arrange(DOWN, buff=0.12))
        pill_lab = t("SUBSCRIBE", 20, ON_DARK, SANS, weight="BOLD")
        pill = RoundedRectangle(width=pill_lab.width + 0.5, height=0.5, corner_radius=0.25,
                                fill_color=DARK, fill_opacity=1, stroke_width=0)
        pill_lab.move_to(pill)
        hai = svg("hai-logo.svg", height=0.42).set_color(INK)
        handle = t("@HumanitariansAI", 24, INK, SANS, weight="BOLD")
        row = VGroup(hai, handle).arrange(RIGHT, buff=0.2)
        main = VGroup(title, VGroup(pill, pill_lab), row).arrange(DOWN, buff=0.45).move_to([CX, 1.85, 0])
        clock.play_at(0.2, FadeIn(title, shift=UP * 0.1), FadeIn(ghost_of(VGroup(pill))), run_time=0.6)
        clock.play_at(clock.t, FadeIn(VGroup(pill, pill_lab)), FadeIn(row), run_time=0.5)
        rule = Line(LEFT * 1.4, RIGHT * 1.4, color=LINE, stroke_width=2).next_to(main, DOWN, buff=0.55).set_x(CX)
        credit = VGroup(t("Boopesh M.", 36, INK, SERIF, weight="BOLD"),
                        t("Humanitarians AI Fellow", 22, MUTED), t("Brutalist team", 22, MUTED),
                        fit(t("Narration: AI voice", 18, MUTED)), t("(Kokoro am_onyx)", 18, MUTED),
                        t("Data: synthetic noise", 16, MUTED),
                        t("Paper: Bailey et al., 2014", 16, MUTED)).arrange(DOWN, buff=0.17)
        credit.next_to(rule, DOWN, buff=0.3).set_x(CX)
        dim = VGroup(rule, credit).copy().set_opacity(0.18)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(max(clock.t, min(cue("B90", "With Boopesh", 1.5), 1.8)), FadeOut(dim), Create(rule),
                      FadeIn(credit), run_time=0.6)
        clock.finish()
