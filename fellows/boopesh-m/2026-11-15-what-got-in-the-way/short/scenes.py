# -*- coding: utf-8 -*-
"""
Manim scenes for the 9:16 Short of "What Got in the Way" (2160x3840) -- Boopesh M.
  B10_Themes     -- the top themes of the 31 frictional logs with obstacles (rough keyword sort)
  B20_Looked     -- what fixed them: 17 of 31 logs found a problem by looking
  B30_MyPart     -- last week's two videos; delivered for review; my obstacle: access, PR pending
  B90_Outro      -- @HumanitariansAI outro + fellow credit
Native portrait layouts (frame 4.5 x 8 units). Numbers read from ../code/results.json.
"""
import json
from pathlib import Path

from manim import *

config.frame_width = 4.5
config.frame_height = 8.0

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
CODE = HERE.parent / "code"
if not (CODE / "results.json").exists():   # isolated copies (static pre-flight) fall back to the reel's data
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-15-what-got-in-the-way/code")
    ASSETS = CODE.parent / "short" / "assets"

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
GHOST = "#A39A88"
TEAL = "#1F4E5F"
GOOD = "#3F6E4E"
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"
DIM_DARK = "#5E544C"
HOT_DARK = "#E08A6A"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

CX = -0.15
SAFE_W = 3.7

RES = json.loads((CODE / "results.json").read_text())
TW = RES["this_week"]
FD = TW["folders"]
CMP = RES["comparison"]
FR = RES["friction"]


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


def png(name, height):
    m = ImageMobject(str(ASSETS / name))
    m.scale_to_fit_height(height)
    return m


def card(w, h, fill=PANEL):
    return RoundedRectangle(width=w, height=h, corner_radius=0.08, fill_color=fill,
                            fill_opacity=1, stroke_width=0)


def ghost_of(m):
    return m.copy().set_fill(opacity=0).set_stroke(GHOST, 2)


def header(kicker, title):
    k = t(kicker.upper(), 13, MUTED, MONO)
    h = fit(t(title, 34, INK, SERIF, weight="BOLD", line_spacing=0.9))
    g = VGroup(k, h).arrange(DOWN, buff=0.12)
    g.move_to([CX, 3.1 - g.height / 2, 0])
    return g

SOFT_DARK = "#D8D0C0"


# ======================================================================== B10 =
class B10_Themes(Scene):
    def construct(self):
        clock = Clock(self, "B10")
        hd = header("Nov 8–14 · my rough sort", "What got in the way")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        n_obs = FR["logs_describing_obstacles"]
        big = t(f"{n_obs}", 70, TEAL, SERIF, weight="BOLD")
        sub = t("logs describe\nobstacles", 24, INK, line_spacing=0.9)
        top = VGroup(big, sub).arrange(RIGHT, buff=0.3)
        c0 = card(SAFE_W, 1.1)
        top.move_to(c0)
        g0 = VGroup(c0, top).move_to([CX, 1.75, 0])

        S = FR["theme_logs"]
        keys = list(S)[:4]
        phrases = ["layout and picture", "Then facts", "length and time", "tools and setup"]
        BW = SAFE_W - 0.75
        rows = VGroup()
        for i, k in enumerate(keys):
            lab = t(k, 24, INK, weight="BOLD")
            bar = Rectangle(width=BW * S[k] / n_obs, height=0.32, fill_color=ACCENT if i == 0 else TEAL,
                            fill_opacity=1, stroke_width=0)
            val = t(str(S[k]), 26, ACCENT if i == 0 else INK, MONO, weight="BOLD").next_to(bar, RIGHT, buff=0.12)
            g = VGroup(lab, VGroup(bar, val)).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            rows.add(g)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        rows.move_to([CX, -0.7, 0])
        rows.align_to([CX - SAFE_W / 2 + 0.12, 0, 0], LEFT)
        ghosts = VGroup(*[Rectangle(width=BW, height=0.32, stroke_color=GHOST, stroke_width=1.5)
                          .move_to(r[1][0], aligned_edge=LEFT) for r in rows])

        clock.play_at(0.3, FadeIn(ghost_of(c0)), FadeIn(ghosts), run_time=0.4)
        clock.play_at(cue("B10", "Thirty-one", 0.5), FadeIn(g0, scale=0.95), run_time=0.6)
        for i, ph in enumerate(phrases):
            r = rows[i]
            clock.play_at(max(cue("B10", ph, 4.0 + 1.8 * i), clock.t), FadeIn(r[0]), GrowFromEdge(r[1][0], LEFT),
                          FadeIn(r[1][1]), run_time=0.5)
        clock.finish()


# ======================================================================== B20 =
class B20_Looked(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        self.camera.background_color = DARK
        stmt = fit(t("Someone\nlooked.", 60, ON_DARK, SERIF, weight="BOLD", line_spacing=0.9))
        stmt.move_to([CX, 2.35, 0])
        n_look, n_obs = FR["found_by_looking_logs"], FR["logs_describing_obstacles"]
        count = VGroup(t(f"{n_look} of {n_obs}", 56, HOT_DARK, SERIF, weight="BOLD"),
                       t("logs found a problem\nby looking", 24, ON_DARK, line_spacing=0.9)).arrange(DOWN, buff=0.12)
        count.move_to([CX, 0.75, 0])
        rows = VGroup()
        for verb, what in (("watch", "the cut"), ("view", "the frames"), ("re-read", "the words")):
            r = RoundedRectangle(width=SAFE_W, height=0.78, corner_radius=0.08, stroke_color=HOT_DARK, stroke_width=3)
            g = VGroup(t(verb, 30, ON_DARK, SERIF, weight="BOLD"), t(what, 25, SOFT_DARK)).arrange(RIGHT, buff=0.25)
            rows.add(VGroup(r, g.move_to(r)))
        rows.arrange(DOWN, buff=0.16).move_to([CX, -1.35, 0])
        dim = VGroup(*[r[0].copy().set_stroke(DIM_DARK) for r in rows])
        clock.play_at(0.2, FadeIn(dim), FadeIn(count.copy().set_color(DIM_DARK)), run_time=0.4)
        clock.play_at(cue("B20", "Most often", 1.2), FadeIn(stmt, shift=UP * 0.1), run_time=0.5)
        clock.play_at(max(cue("B20", "In seventeen", 2.5), clock.t), FadeIn(count, shift=UP * 0.1), run_time=0.5)
        for i, ph in enumerate(("watching the cut", "viewing the frames", "re-reading the words")):
            clock.play_at(max(cue("B20", ph, 5.0 + 1.0 * i), clock.t), FadeIn(rows[i], shift=UP * 0.08), run_time=0.4)
        clock.finish()


# ======================================================================== B30 =
class B30_MyPart(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("Boopesh M. · last week", "My part")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        D = RES["boopesh"]["last_week_deliveries"]

        def vid(title, kind, lk, vk):
            c = card(SAFE_W, 1.45)
            head = t(title, 30, INK, SANS, weight="BOLD")
            k = t(kind + " · 4K", 24, ACCENT, MONO, weight="BOLD")
            m1 = t(f"{D[lk]['mm_ss']} + Short {D[vk]['mm_ss']}", 24, INK, MONO)
            g = VGroup(head, k, m1).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
            fit(g, SAFE_W - 0.2).move_to(c)
            return VGroup(c, g)

        a = vid("What the Fellows Taught", "PROGRESS", "landscape/WhatTheFellowsTaught_BoopeshM.mp4",
                "vertical/WhatTheFellowsTaught_BoopeshM.mp4")
        b = vid("The Backtest Mirage", "AI IN FINANCE", "landscape/BacktestMirage_BoopeshM.mp4",
                "vertical/BacktestMirage_BoopeshM.mp4")
        pair = VGroup(a, b).arrange(DOWN, buff=0.25)
        pair.move_to([CX, 1.95 - pair.height / 2, 0])

        g1 = t("✓ delivered\nfor review", 27, GOOD, weight="BOLD", line_spacing=0.85)
        b1 = card(1.8, 0.9).move_to(g1)
        gh = png("github-01.png", 0.26)
        s2 = t("PR\npending", 27, ACCENT, weight="BOLD", line_spacing=0.85)
        b2 = DashedVMobject(RoundedRectangle(width=1.8, height=0.9, corner_radius=0.08, stroke_color=ACCENT,
                                             stroke_width=3), num_dashes=24)
        VGroup(b1, b2).arrange(RIGHT, buff=0.1).next_to(pair, DOWN, buff=0.25).set_x(CX)
        g1.move_to(b1)
        Group(gh, s2).arrange(RIGHT, buff=0.15).move_to(b2)
        why = t("MY OBSTACLE: ACCESS", 26, INK, MONO, weight="BOLD").next_to(VGroup(b1, b2), DOWN, buff=0.22).set_x(CX)

        clock.play_at(0.3, FadeIn(ghost_of(a[0])), FadeIn(ghost_of(b[0])),
                      FadeIn(ghost_of(b1)), FadeIn(b2.copy().set_stroke(GHOST)), run_time=0.4)
        clock.play_at(cue("B30", "What the Fellows", 1.2), FadeIn(a, shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B30", "The Backtest", 2.6), FadeIn(b, shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B30", "delivered for review", 4.8), FadeIn(b1), FadeIn(g1), run_time=0.5)
        clock.play_at(max(cue("B30", "My own obstacle", 6.3), clock.t), FadeIn(why), run_time=0.4)
        clock.play_at(max(cue("B30", "still pending", 8.0), clock.t), Create(b2), FadeIn(gh), FadeIn(s2), run_time=0.6)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = fit(t("What Got\nin the Way", 46, INK, SERIF, line_spacing=0.9))
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
                        t("Data: frictional logs,", 18, MUTED), t("humanitarians-youtube", 18, MUTED)).arrange(DOWN, buff=0.17)
        credit.next_to(rule, DOWN, buff=0.3).set_x(CX)
        dim = VGroup(rule, credit).copy().set_opacity(0.18)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(min(cue("B90", "With Boopesh", 1.5), 1.8), FadeOut(dim), Create(rule), FadeIn(credit), run_time=0.6)
        clock.finish()
