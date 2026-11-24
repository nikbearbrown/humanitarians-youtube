# -*- coding: utf-8 -*-
"""
Manim scenes for the 9:16 Short of "What the Fellows Taught" (2160x3840) -- Boopesh M.
  B10_Subjects   -- 50 of 74 new folders teach a topic; the top three subjects
  B20_Compare    -- last week vs this week: new folders 84 -> 74, frictional logs 72 -> 95
  B30_MyPart     -- last week's two videos; delivered for review, GitHub PR pending
  B40_Takeaway   -- teach one idea: one idea, one example, where it breaks
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
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-08-what-the-fellows-taught/code")
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
class B10_Subjects(Scene):
    def construct(self):
        clock = Clock(self, "B10")
        hd = header("new folders · Nov 1–7", "What they\ntaught")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        n_stem, total = FD["kinds"]["STEM / explainer video"], FD["new_work_folders"]
        big = t(f"{n_stem} of {total}", 70, TEAL, SERIF, weight="BOLD")
        sub = t("new work folders\nteach a topic", 22, INK, line_spacing=0.9)
        top = VGroup(big, sub).arrange(DOWN, buff=0.1)
        c0 = card(SAFE_W, 1.75)
        top.move_to(c0)
        g0 = VGroup(c0, top).move_to([CX, 1.05, 0])

        S = FD["stem_subjects"]
        keys = list(S)[:3]
        mx = S[keys[0]]
        BW = SAFE_W - 0.75
        rows = VGroup()
        for i, k in enumerate(keys):
            lab = t(k, 22, INK, weight="BOLD")
            bar = Rectangle(width=BW * S[k] / mx, height=0.34, fill_color=ACCENT if i == 1 else TEAL, fill_opacity=1,
                            stroke_width=0)
            val = t(str(S[k]), 24, ACCENT if i == 1 else INK, MONO, weight="BOLD").next_to(bar, RIGHT, buff=0.12)
            line = VGroup(bar, val)
            g = VGroup(lab, line).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            rows.add(g)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        rows.move_to([CX, -1.35, 0])
        rows.align_to([CX - SAFE_W / 2 + 0.12, 0, 0], LEFT)
        ghosts = VGroup(*[Rectangle(width=BW, height=0.34, stroke_color=GHOST, stroke_width=1.5)
                          .move_to(r[1][0], aligned_edge=LEFT) for r in rows])

        clock.play_at(0.3, FadeIn(ghost_of(c0)), FadeIn(ghosts), run_time=0.4)
        clock.play_at(cue("B10", "fifty of them", 2.0), FadeIn(g0, scale=0.95), run_time=0.6)
        clock.play_at(cue("B10", "The top subjects", 4.5), FadeIn(VGroup(*[r[0] for r in rows]), lag_ratio=0.2),
                      LaggedStart(*[GrowFromEdge(r[1][0], LEFT) for r in rows], lag_ratio=0.3),
                      FadeIn(VGroup(*[r[1][1] for r in rows])), run_time=1.4)
        clock.finish()


# ======================================================================== B20 =
class B20_Compare(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("same script · Oct 25–31 vs Nov 1–7", "Last week\nvs this week")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        def pair(key, lab, up):
            a, b = CMP[key]["last_week"], CMP[key]["this_week"]
            c = card(SAFE_W, 2.15)
            title = t(lab, 30, INK, weight="BOLD")
            BW = SAFE_W - 1.55
            mx = max(a, b)
            ra = Rectangle(width=BW * a / mx, height=0.36, fill_color=LINE, fill_opacity=1, stroke_width=0)
            rb = Rectangle(width=BW * b / mx, height=0.36, fill_color=ACCENT if up else TEAL, fill_opacity=1,
                           stroke_width=0)
            la = VGroup(t("last", 24, MUTED), ra, t(str(a), 26, MUTED, MONO, weight="BOLD")).arrange(RIGHT, buff=0.12)
            lb = VGroup(t("this", 24, INK, weight="BOLD"), rb,
                        t(str(b), 28, ACCENT if up else TEAL, MONO, weight="BOLD")).arrange(RIGHT, buff=0.12)
            rb.align_to(ra, LEFT)
            lb[2].next_to(rb, RIGHT, buff=0.12)
            g = VGroup(title, la, lb).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
            rb.align_to(ra, LEFT)
            lb[2].next_to(rb, RIGHT, buff=0.12)
            g.move_to(c)
            return VGroup(c, g)

        p1 = pair("new_work_folders", "new work folders", False)
        p2 = pair("frictional_logs_added", "frictional logs", True)
        col = VGroup(p1, p2).arrange(DOWN, buff=0.3).move_to([CX, -0.45, 0])
        clock.play_at(0.3, FadeIn(ghost_of(p1[0])), FadeIn(ghost_of(p2[0])), run_time=0.4)
        clock.play_at(cue("B20", "fewer new folders", 1.5), FadeIn(p1[0]), FadeIn(p1[1][0]), FadeIn(p1[1][1]),
                      run_time=0.5)
        clock.play_at(cue("B20", "seventy-four instead", 2.8), GrowFromEdge(p1[1][2][1], LEFT), FadeIn(p1[1][2][0]),
                      FadeIn(p1[1][2][2]), run_time=0.5)
        clock.play_at(cue("B20", "but more", 5.0), FadeIn(p2[0]), FadeIn(p2[1][0]), FadeIn(p2[1][1]), run_time=0.5)
        clock.play_at(cue("B20", "ninety-five", 6.0), GrowFromEdge(p2[1][2][1], LEFT), FadeIn(p2[1][2][0]),
                      FadeIn(p2[1][2][2], scale=1.2), run_time=0.6)
        clock.finish()


# ======================================================================== B30 =
class B30_MyPart(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("Boopesh M. · last week", "My part")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        D = RES["boopesh"]["last_week_deliveries"]

        def vid(title, kind, lk, vk):
            c = card(SAFE_W, 1.6)
            head = t(title, 25, INK, SANS, weight="BOLD")
            k = t(kind + " · 4K", 24, ACCENT, MONO, weight="BOLD")
            m1 = t(f"{D[lk]['mm_ss']} + Short {D[vk]['mm_ss']}", 24, INK, MONO)
            g = VGroup(head, k, m1).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
            fit(g, SAFE_W - 0.3).move_to(c)
            return VGroup(c, g)

        a = vid("One Week of Fellows", "PROGRESS VIDEO", "landscape/OneWeekOfFellows_BoopeshM.mp4",
                "vertical/OneWeekOfFellows_BoopeshM.mp4")
        b = vid("The 99.9% Accuracy Trap", "STEM EXPLAINER", "landscape/FraudAccuracyTrap_BoopeshM.mp4",
                "vertical/FraudAccuracyTrap_BoopeshM.mp4")
        pair = VGroup(a, b).arrange(DOWN, buff=0.25)
        pair.move_to([CX, 1.95 - pair.height / 2, 0])

        g1 = t("✓ delivered\nfor review", 23, GOOD, weight="BOLD", line_spacing=0.85)
        b1 = card(1.8, 0.85).move_to(g1)
        gh = png("github-01.png", 0.26)
        s2 = t("PR\npending", 23, ACCENT, weight="BOLD", line_spacing=0.85)
        b2 = DashedVMobject(RoundedRectangle(width=1.8, height=0.85, corner_radius=0.08, stroke_color=ACCENT,
                                             stroke_width=3), num_dashes=24)
        VGroup(b1, b2).arrange(RIGHT, buff=0.1).next_to(pair, DOWN, buff=0.25).set_x(CX)
        g1.move_to(b1)
        Group(gh, s2).arrange(RIGHT, buff=0.15).move_to(b2)

        clock.play_at(0.3, FadeIn(ghost_of(a[0])), FadeIn(ghost_of(b[0])),
                      FadeIn(ghost_of(b1)), FadeIn(b2.copy().set_stroke(GHOST)), run_time=0.4)
        clock.play_at(cue("B30", "One Week", 1.5), FadeIn(a, shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B30", "The Accuracy Trap", 2.8), FadeIn(b, shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B30", "delivered for review", 5.0), FadeIn(b1), FadeIn(g1), run_time=0.5)
        clock.play_at(cue("B30", "still pending", 6.5), Create(b2), FadeIn(gh), FadeIn(s2), run_time=0.6)
        clock.finish()


# ======================================================================== B40 =
class B40_Takeaway(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        self.camera.background_color = DARK
        stmt = fit(t("Teach\none idea.", 60, ON_DARK, SERIF, weight="BOLD", line_spacing=0.9))
        stmt.move_to([CX, 2.2, 0])
        rows = VGroup()
        for i, (name, what) in enumerate((("one idea", "from your week"), ("one example", "worked through"),
                                          ("one limit", "where it breaks"))):
            r = RoundedRectangle(width=SAFE_W, height=0.9, corner_radius=0.08, stroke_color=HOT_DARK, stroke_width=3)
            g = VGroup(t(str(i + 1), 26, HOT_DARK, MONO, weight="BOLD"),
                       VGroup(t(name, 28, ON_DARK, SERIF, weight="BOLD"), t(what, 23, SOFT_DARK))
                       .arrange(DOWN, aligned_edge=LEFT, buff=0.05)).arrange(RIGHT, buff=0.3)
            rows.add(VGroup(r, g.move_to(r)))
        rows.arrange(DOWN, buff=0.18).move_to([CX, -0.75, 0])
        dim = VGroup(*[r[0].copy().set_stroke(DIM_DARK) for r in rows])
        clock.play_at(0.2, FadeIn(dim), run_time=0.4)
        clock.play_at(cue("B40", "teach one idea", 0.8), FadeIn(stmt, shift=UP * 0.1), FadeIn(rows[0]), run_time=0.6)
        clock.play_at(max(cue("B40", "One worked", 2.5), clock.t), FadeIn(rows[1], shift=UP * 0.08), run_time=0.4)
        clock.play_at(max(cue("B40", "where it breaks", 3.5), clock.t), FadeIn(rows[2], shift=UP * 0.08), run_time=0.4)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = fit(t("What the\nFellows Taught", 46, INK, SERIF, line_spacing=0.9))
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
                        t("Data: git history,", 18, MUTED), t("humanitarians-youtube", 18, MUTED)).arrange(DOWN, buff=0.17)
        credit.next_to(rule, DOWN, buff=0.3).set_x(CX)
        dim = VGroup(rule, credit).copy().set_opacity(0.18)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(min(cue("B90", "With Boopesh", 1.5), 1.8), FadeOut(dim), Create(rule), FadeIn(credit), run_time=0.6)
        clock.finish()
