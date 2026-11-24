# -*- coding: utf-8 -*-
"""
Manim scenes for the 9:16 Short of "Hedging When Trading Isn't Free" (2160x3840) -- Boopesh M.
  B10_Cost     -- the daily Black-Scholes hedge pays $1.11 in fees, ~40% of the option price
  B20_Move     -- Deep Hedging: a network picks the position; fees inside the objective
  B30_Result   -- turnover and fee bars, BS delta vs deep hedge (40,000 test paths)
  B40_Limits   -- gamma = 0 sanity check + the honest limit
  B90_Outro    -- @HumanitariansAI outro + fellow credit
Native portrait layouts (frame 4.5 x 8 units). Numbers read from ../code/results.json.
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
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-10-24-deep-hedging/code")

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
GHOST = "#A39A88"
TEAL = "#1F4E5F"
GREY = "#8C8578"
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

CX = -0.15
SAFE_W = 3.7

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


def ghost_of(m):
    return m.copy().set_fill(opacity=0).set_stroke(GHOST, 2)


def money(x):
    return f"${x:.2f}" if x >= 0 else f"−${-x:.2f}"


def header(kicker, title):
    k = t(kicker.upper(), 13, MUTED, MONO)
    h = fit(t(title, 34, INK, SERIF, weight="BOLD", line_spacing=0.9))
    g = VGroup(k, h).arrange(DOWN, buff=0.12)
    g.move_to([CX, 3.1 - g.height / 2, 0])
    return g


def bar_pair(name, vb, vd, fmt, y, width=2.5):
    m = max(vb, vd)
    nm = t(name, 22, INK, weight="BOLD")
    rows = VGroup()
    for v, c, lab in ((vb, GREY, "BS delta"), (vd, TEAL, "deep hedge")):
        w = width * v / m
        r = Rectangle(width=w, height=0.36, fill_color=c, fill_opacity=1, stroke_width=0)
        val = t(fmt(v), 22, INK, MONO)
        tag = t(lab, 16, MUTED)
        rows.add(VGroup(tag, VGroup(r, val).arrange(RIGHT, buff=0.1)).arrange(DOWN, aligned_edge=LEFT, buff=0.06))
    g = VGroup(nm, *rows).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
    g.move_to([CX, y, 0])
    g.shift(RIGHT * ((CX - SAFE_W / 2 + 0.1) - g.get_left()[0]))
    return g


# ======================================================================== B10 =
class B10_Cost(Scene):
    def construct(self):
        clock = Clock(self, "B10")
        hd = header("the textbook hedge · 0.5% fee", "Every trade pays a fee")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        per_day = ARR["gamma_0.005_turnover_bs_per_day"]
        L, R, B, T = CX - 1.8, CX + 1.8, 0.0, 1.5
        bars = VGroup()
        for i, v in enumerate(per_day):
            h = max(0.02, (T - B) * min(v, 0.6) / 0.6)
            w = (R - L) / 30
            bars.add(Rectangle(width=w * 0.75, height=h, fill_color=GREY, fill_opacity=1, stroke_width=0)
                     .move_to([L + w * (i + 0.5), B + h / 2, 0]))
        base = Line([L, B, 0], [R, B, 0], color=INK, stroke_width=3)
        cap = t("shares traded each day, days 1 to 30", 16, MUTED).next_to(base, DOWN, buff=0.12)
        daily = t("adjusts every single day", 20, INK).move_to([CX + 0.35, 0.75, 0])

        big = t(money(G["bs_delta"]["mean_cost"]), 64, ACCENT, SERIF, weight="BOLD")
        sub = t("paid in fees per option", 22, INK)
        pct = G["bs_delta"]["mean_cost"] / RES["setup"]["premium_bs"] * 100
        sub2 = t(f"≈ {pct:.0f}% of its {money(RES['setup']['premium_bs'])} price", 22, MUTED)
        stat = VGroup(big, sub, sub2).arrange(DOWN, buff=0.14)
        box = card(SAFE_W, stat.height + 0.5).move_to([CX, -1.55, 0])
        stat.move_to(box)

        clock.play_at(0.3, FadeIn(ghost_of(box)), FadeIn(bars.copy().set_fill(opacity=0).set_stroke(GHOST, 1)),
                      run_time=0.5)
        clock.play_at(0.8, Create(base), FadeIn(cap), run_time=0.4)
        clock.play_at(cue("B10", "adjusts every day", 1.5),
                      LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.05), FadeIn(daily), run_time=1.4)
        clock.play_at(cue("B10", "costs a dollar", 4.0), FadeIn(box), FadeIn(big, scale=0.9), FadeIn(sub), run_time=0.6)
        clock.play_at(cue("B10", "About forty", 6.5), FadeIn(sub2), run_time=0.5)
        clock.finish()


# ======================================================================== B20 =
class B20_Move(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("Deep Hedging · 2019", "Learn the hedge,\nfees included")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        ins = card(SAFE_W, 0.6)
        ins_l = t("time left · price · position", 20, INK).move_to(ins)
        cols = []
        for n in (3, 5, 5, 1):
            c = VGroup(*[Circle(0.09, color=TEAL, stroke_width=2, fill_color=TEAL, fill_opacity=0.25)
                         for _ in range(n)]).arrange(RIGHT, buff=0.14)
            cols.append(c)
        net = VGroup(*cols).arrange(DOWN, buff=0.22)
        edges = VGroup(*[Line(u.get_center(), v.get_center(), color=LINE, stroke_width=1.2)
                         for a, b in zip(cols[:-1], cols[1:]) for u in a for v in b])
        out = card(SAFE_W, 0.6)
        out_l = t("new position δ, every day", 20, TEAL, weight="BOLD").move_to(out)
        flow = VGroup(VGroup(ins, ins_l), VGroup(edges, net), VGroup(out, out_l)).arrange(DOWN, buff=0.3)
        edges.move_to(net)
        flow.move_to([CX, 0.15, 0])
        flow.shift(DOWN * max(0, flow.get_top()[1] - (hd.get_bottom()[1] - 0.2)))
        a1 = Arrow(ins.get_bottom(), net.get_top(), buff=0.06, color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.4)
        a2 = Arrow(net.get_bottom(), out.get_top(), buff=0.06, color=INK, stroke_width=3, max_tip_length_to_length_ratio=0.4)

        ent_box = card(SAFE_W, 1.15).next_to(flow, DOWN, buff=0.15).set_x(CX)
        ent = svg("eq_ent_ink.svg", width=2.7)
        ent_n = t("score of final P&L, after fees", 16, ACCENT, weight="BOLD")
        VGroup(ent, ent_n).arrange(DOWN, buff=0.12).move_to(ent_box)

        clock.play_at(0.3, FadeIn(ghost_of(ins)), FadeIn(ghost_of(out)), FadeIn(ghost_of(ent_box)), run_time=0.4)
        clock.play_at(cue("B20", "neural network", 1.2), FadeIn(VGroup(ins, ins_l)), GrowArrow(a1),
                      FadeIn(VGroup(edges, net)), run_time=0.7)
        clock.play_at(cue("B20", "choose the position", 2.5), GrowArrow(a2), FadeIn(VGroup(out, out_l)), run_time=0.6)
        clock.play_at(cue("B20", "fees inside", 4.2), FadeIn(ent_box), FadeIn(ent, shift=UP * 0.1), FadeIn(ent_n),
                      run_time=0.7)
        clock.finish()


# ======================================================================== B30 =
class B30_Result(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("my replication · 40,000 test paths", "It trades less")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        g1 = bar_pair("shares traded", G["turnover_bs"], G["turnover_deep"], lambda v: f"{v:.2f}", 1.05)
        g2 = bar_pair("fees paid", G["bs_delta"]["mean_cost"], G["deep_hedge"]["mean_cost"], money, -0.95)
        u = VGroup(t("risk score (higher is better)", 18, MUTED),
                   t(f"{G['bs_delta']['entropic_utility']:.2f} → {G['deep_hedge']['entropic_utility']:.2f}".replace("-", "−"),
                     26, ACCENT, MONO, weight="BOLD")).arrange(DOWN, buff=0.1).move_to([CX, -2.45, 0])

        clock.play_at(0.3, FadeIn(VGroup(g1, g2, u).copy().set_opacity(0.15)), run_time=0.5)
        clock.play_at(cue("B30", "trades one point", 2.0), FadeIn(g1, shift=RIGHT * 0.1), run_time=0.6)
        clock.play_at(cue("B30", "pays sixty", 5.0), FadeIn(g2, shift=RIGHT * 0.1), run_time=0.6)
        clock.play_at(clock.t + 0.4, FadeIn(u), run_time=0.5)
        clock.finish()


# ======================================================================== B40 =
class B40_Limits(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        hd = header("sanity check + the catch", "Does it\nfool itself?")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        top = card(SAFE_W, 1.75).move_to([CX, 0.85, 0])
        tl = VGroup(t("fee = 0: close to Black–Scholes", 20, INK, weight="BOLD"),
                    t(f"avg position gap {G0['mean_abs_gap_to_bs_delta']:.3f} shares", 18, MUTED),
                    t(f"utility {G0['deep_hedge']['entropic_utility']:.3f} vs BS {G0['bs_delta']['entropic_utility']:.3f}"
                      .replace("-", "−"), 18, MUTED)).arrange(DOWN, buff=0.14)
        fit(tl, SAFE_W - 0.3).move_to(top)
        bot = card(SAFE_W, 2.1, fill=DARK).move_to([CX, -1.35, 0])
        bl = VGroup(t("toy world:", 20, "#D8D0C0"), t("Black–Scholes prices", 22, ON_DARK, weight="BOLD"),
                    t("only as good as", 22, ON_DARK, weight="BOLD"), t("its simulator", 22, ON_DARK, weight="BOLD"))
        bl.arrange(DOWN, buff=0.12).move_to(bot)

        clock.play_at(0.3, FadeIn(ghost_of(top)), FadeIn(ghost_of(bot)), run_time=0.4)
        clock.play_at(cue("B40", "zero fees", 0.8), FadeIn(top), FadeIn(tl), run_time=0.6)
        clock.play_at(cue("B40", "The catch", 3.5), FadeIn(bot), FadeIn(bl[:2]), run_time=0.6)
        clock.play_at(cue("B40", "only as good", 5.5), FadeIn(bl[2:]), run_time=0.5)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = fit(t("Hedging When\nTrading Isn't Free", 44, INK, SERIF, line_spacing=0.9))
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
                        t("Paper: Buehler, Gonon,", 18, MUTED), t("Teichmann & Wood, 2019", 18, MUTED)).arrange(DOWN, buff=0.17)
        credit.next_to(rule, DOWN, buff=0.3).set_x(CX)
        dim = VGroup(rule, credit).copy().set_opacity(0.18)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(min(cue("B90", "With Boopesh", 1.5), 1.8), FadeOut(dim), Create(rule), FadeIn(credit), run_time=0.6)
        clock.finish()
