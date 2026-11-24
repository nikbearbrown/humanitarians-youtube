# -*- coding: utf-8 -*-
"""
Manim scenes for the 9:16 Short of "The 99.9% Accuracy Trap" (2160x3840) -- Boopesh M.
  B10_Rare        -- 580 dots, 1 red: fraud is about 1 in 580 card transactions (real dataset counts)
  B20_LazyVsReal  -- "always legit" vs gradient boosting: 99.8% vs 99.9% accurate, 0 vs 127 of 148 caught
  B30_Takeaway    -- check recall, precision, and cost; honest limit
  B90_Outro       -- @HumanitariansAI outro + fellow credit
Native portrait layouts (frame 4.5 x 8 units). Numbers read from ../code/results.json (synthetic data).
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
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-01-fraud-accuracy-trap/code")
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
GREY = "#8C8578"
FRAUD = "#B3261E"
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"
ON_DARK_MUTED = "#D8D0C0"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

CX = -0.15
SAFE_W = 3.7

RES = json.loads((CODE / "results.json").read_text())
SET = RES["setup"]
LAZY, BOOST = RES["always_legit"], RES["boosted"]
NF = SET["test_frauds"]
REAL = SET["real_dataset_reference"]
ONE_IN = int(round(REAL["one_in"], -1))


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


def pct(x, nd=1):
    return f"{100 * x:.{nd}f}%"


def header(kicker, title):
    k = fit(t(kicker.upper(), 13, MUTED, MONO))
    h = fit(t(title, 34, INK, SERIF, weight="BOLD", line_spacing=0.9))
    g = VGroup(k, h).arrange(DOWN, buff=0.12)
    g.move_to([CX, 3.1 - g.height / 2, 0])
    return g


# ======================================================================== B10 =
class B10_Rare(Scene):
    def construct(self):
        clock = Clock(self, "B10")
        hd = header("real card data · ULB + Worldline", "How rare is\ncard fraud?")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        cols, rows, sp = 20, 29, 0.138
        dots = VGroup(*[Circle(radius=0.047, stroke_width=0, fill_color=GREY, fill_opacity=1)
                        for _ in range(rows * cols)]).arrange_in_grid(rows=rows, cols=cols, buff=sp - 0.094)
        top = hd.get_bottom()[1] - 0.3
        dots.move_to([CX, top - dots.height / 2, 0])
        red = dots[17 * cols + 13]
        ghosts = dots.copy().set_fill(opacity=0).set_stroke(GHOST, 1)
        ring = Circle(radius=0.17, color=FRAUD, stroke_width=4).move_to(red)

        big = t(f"1 in {ONE_IN}", 46, FRAUD, SERIF, weight="BOLD")
        sub = fit(t(f"{REAL['frauds']:,} frauds in {REAL['rows']:,} transactions", 18, MUTED))
        stat = VGroup(big, sub).arrange(DOWN, buff=0.08).next_to(dots, DOWN, buff=0.25).set_x(CX)

        dim_stat = stat.copy().set_opacity(0.18)
        clock.play_at(0.3, FadeIn(ghosts), FadeIn(dim_stat), run_time=0.5)
        clock.play_at(0.8, LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.003), run_time=1.4)
        clock.play_at(cue("B10", "about one", 2.5), red.animate.set_fill(FRAUD).scale(1.4), Create(ring),
                      FadeIn(big, scale=0.9), run_time=0.7)
        clock.play_at(cue("B10", "Four hundred", 5.0), FadeOut(dim_stat), FadeIn(sub), run_time=0.5)
        clock.finish()


# ======================================================================== B20 =
def model_card(name, r, y, color):
    c = card(SAFE_W, 2.15).move_to([CX, y, 0])
    nm = t(name, 30, INK, weight="BOLD")
    acc = VGroup(t(pct(r["accuracy"]), 40, INK, SERIF, weight="BOLD"), t("accurate", 22, MUTED)).arrange(
        RIGHT, buff=0.12, aligned_edge=DOWN)
    w = SAFE_W - 0.5
    track = Rectangle(width=w, height=0.3, fill_color=BG, fill_opacity=1, stroke_color=GHOST, stroke_width=2)
    fw = max(w * r["caught"] / NF, 0.001)
    bar = Rectangle(width=fw, height=0.3, fill_color=color, fill_opacity=1, stroke_width=0)
    caught = t(f"caught {r['caught']} of {NF} frauds", 20, FRAUD if r["caught"] == 0 else TEAL, weight="BOLD")
    body = VGroup(nm, acc, track, caught).arrange(DOWN, buff=0.16).move_to(c)
    bar.move_to(track.get_left() + RIGHT * fw / 2)
    return c, nm, acc, track, bar, caught


class B20_LazyVsReal(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header(f"synthetic test · {NF} frauds", "Same accuracy?")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        a = model_card("always says “legit”", LAZY, 1.2, GREY)
        b = model_card("gradient boosting", BOOST, -1.35, TEAL)
        note = fit(t("synthetic data, real fraud rate", 20, MUTED)).next_to(a[0], DOWN, buff=0.07).set_x(CX)

        clock.play_at(0.3, FadeIn(ghost_of(a[0])), FadeIn(ghost_of(b[0])), run_time=0.4)
        clock.play_at(cue("B20", "lazy model", 0.8), FadeIn(a[0]), FadeIn(a[1]), FadeIn(a[3]), FadeIn(note),
                      run_time=0.5)
        clock.play_at(cue("B20", "ninety-nine point eight", 2.5), FadeIn(a[2], scale=0.9), run_time=0.5)
        clock.play_at(cue("B20", "catches zero", 4.5), FadeIn(a[5]), run_time=0.5)
        clock.play_at(cue("B20", "A small boosted", 6.5), FadeIn(b[0]), FadeIn(b[1]), FadeIn(b[3]), run_time=0.5)
        clock.play_at(cue("B20", "ninety-nine point nine", 9.5), FadeIn(b[2], scale=0.9), run_time=0.5)
        clock.play_at(cue("B20", "but it catches", 12.0), GrowFromEdge(b[4], LEFT), FadeIn(b[5]), run_time=0.8)
        clock.finish()


# ======================================================================== B30 =
class B30_Takeaway(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("takeaway", "When it's rare,\ndon't trust accuracy")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        box = card(SAFE_W, 3.6, fill=DARK).move_to([CX, -0.2, 0])
        head = t("check these instead", 18, ON_DARK_MUTED)
        rows = VGroup()
        for a, b in (("recall", "how much fraud you catch"), ("precision", "how many alarms are real"),
                     ("cost", "what each mistake costs")):
            rows.add(VGroup(t(a, 32, ON_DARK, SERIF, weight="BOLD"), t(b, 17, ON_DARK_MUTED)).arrange(DOWN, buff=0.04))
        body = VGroup(head, *rows).arrange(DOWN, buff=0.22).move_to(box)
        lim = VGroup(t("synthetic data · real systems", 16, MUTED),
                     t("use far more signals", 16, MUTED)).arrange(DOWN, buff=0.05).next_to(box, DOWN, buff=0.2)
        lim.set_x(CX)

        clock.play_at(0.3, FadeIn(ghost_of(box, "#5E544C")), FadeIn(lim), run_time=0.4)
        clock.play_at(cue("B30", "For rare", 2.5), FadeIn(box), FadeIn(head), run_time=0.5)
        for i, p in enumerate(["recall", "precision", "what each"]):
            clock.play_at(max(clock.t, cue("B30", p, 3.5 + i)), FadeIn(rows[i], shift=UP * 0.08), run_time=0.4)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = fit(VGroup(t("The 99.9%", 46, INK, SERIF), t("Accuracy Trap", 46, INK, SERIF)).arrange(DOWN, buff=0.12))
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
                        t("Data: synthetic, real fraud rate", 16, MUTED),
                        t("(ULB + Worldline card dataset)", 16, MUTED)).arrange(DOWN, buff=0.17)
        credit.next_to(rule, DOWN, buff=0.3).set_x(CX)
        dim = VGroup(rule, credit).copy().set_opacity(0.18)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(max(clock.t, min(cue("B90", "With Boopesh", 1.5), 1.8)), FadeOut(dim), Create(rule),
                      FadeIn(credit), run_time=0.6)
        clock.finish()
