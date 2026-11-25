# -*- coding: utf-8 -*-
"""
Manim scenes for the 9:16 Short of "One Week of Fellows" (2160x3840) -- Boopesh M.
  B10_PerDay     -- 30 merged pull requests, per day; Thursday's 12
  B20_Numbers    -- 37 names -> 27 people; 84 new work folders; 72 frictional logs
  B30_MyPart     -- last week's two videos; Drive submitted, GitHub PR pending
  B40_Takeaway   -- small weekly evidence adds up: README, fact check, frictional log, source
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
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-01-one-week-of-fellows/code")
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
PR = RES["merged_prs"]
PPL = RES["contributors"]
FD = RES["folders"]


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


# ======================================================================== B10 =
class B10_PerDay(Scene):
    def construct(self):
        clock = Clock(self, "B10")
        hd = header("git log · Oct 25–31", "Pull requests\nmerged")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        big = t(str(PR["total"]), 96, INK, SERIF, weight="BOLD")
        gh = png("github-01.png", 0.45)
        top = Group(gh, big).arrange(RIGHT, buff=0.2).move_to([CX, 1.35, 0])
        sub = t("in seven days", 22, MUTED).next_to(top, DOWN, buff=0.08)

        days = list(PR["per_day"].items())
        names = ["S", "M", "T", "W", "T", "F", "S"]
        base, h_top = -1.8, 0.35
        unit = (h_top - base) / max(v for _, v in days)
        step = 0.5
        x0 = CX - 3 * step
        bars, vals, labs, ghosts = VGroup(), VGroup(), VGroup(), VGroup()
        for i, (d, v) in enumerate(days):
            x = x0 + i * step
            busy = d == PR["busiest_day"]
            h = max(v * unit, 0.02)
            bars.add(Rectangle(width=0.36, height=h, fill_color=ACCENT if busy else TEAL, fill_opacity=1,
                               stroke_width=0).move_to([x, base + h / 2, 0]))
            vals.add(t(str(v), 22 if busy else 18, ACCENT if busy else INK, MONO, weight="BOLD")
                     .move_to([x, base + h + 0.18, 0]))
            labs.add(t(names[i], 18, INK, weight="BOLD").move_to([x, base - 0.2, 0]))
            ghosts.add(Rectangle(width=0.36, height=h_top - base, stroke_color=GHOST, stroke_width=1.5)
                       .move_to([x, (h_top + base) / 2, 0]))
        axis = Line([x0 - 0.3, base, 0], [x0 + 6 * step + 0.3, base, 0], color=INK, stroke_width=3)
        thu = t("Thursday, Oct 29: 12", 22, ACCENT, weight="BOLD").move_to([CX, -2.35, 0])

        clock.play_at(0.3, FadeIn(ghosts), Create(axis), FadeIn(labs), run_time=0.5)
        clock.play_at(cue("B10", "Thirty", 0.6), FadeIn(top, scale=0.9), FadeIn(sub), run_time=0.6)
        clock.play_at(clock.t + 0.1, LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.12),
                      FadeIn(vals, lag_ratio=0.12), run_time=1.2)
        clock.play_at(cue("B10", "Thursday", 3.2), FadeIn(thu, shift=UP * 0.1),
                      Indicate(bars[4], color=ACCENT, scale_factor=1.08), run_time=0.6)
        clock.finish()


# ======================================================================== B20 =
class B20_Numbers(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("counted from git history", "Who shipped\nwhat")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        def stat(big, col, small, h=1.1):
            c = card(SAFE_W, h)
            g = VGroup(t(big, 52, col, SERIF, weight="BOLD"), t(small, 18, INK, line_spacing=0.9))
            g.arrange(RIGHT, buff=0.25)
            fit(g, SAFE_W - 0.3).move_to(c)
            return VGroup(c, g)

        s1 = stat(f"{PPL['distinct_author_names_raw']}→{PPL['distinct_people_after_obvious_dedupe']}", TEAL,
                  "author names →\npeople, once\nduplicates merged")
        s2 = stat(str(FD["new_work_folders"]), INK, f"new work folders\nfrom {FD['fellows_with_new_folders']} fellows")
        s3 = stat(str(FD["frictional_logs_added"]), ACCENT, "frictional logs:\nwhat resisted")
        col = VGroup(s1, s2, s3).arrange(DOWN, buff=0.25).move_to([CX, -0.3, 0])

        clock.play_at(0.3, FadeIn(VGroup(*[ghost_of(s[0]) for s in col])), run_time=0.4)
        clock.play_at(cue("B20", "Thirty-seven", 0.7), FadeIn(s1, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B20", "eighty-four", 5.5), FadeIn(s2, shift=UP * 0.1), run_time=0.6)
        clock.play_at(cue("B20", "seventy-two", 8.0), FadeIn(s3, shift=UP * 0.1), run_time=0.6)
        clock.finish()


# ======================================================================== B30 =
class B30_MyPart(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("Boopesh M. · last week", "My part")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        D = RES["boopesh"]["last_week_deliveries"]

        def mmss(x):
            return f"{int(x // 60)}:{int(x % 60):02d}"

        def vid(title, kind, lk, vk):
            c = card(SAFE_W, 1.6)
            tri = Triangle(fill_color=ON_DARK, fill_opacity=1, stroke_width=0).rotate(-PI / 2).scale(0.13)
            play = VGroup(RoundedRectangle(width=0.62, height=0.44, corner_radius=0.1, fill_color=DARK,
                                           fill_opacity=1, stroke_width=0), tri)
            tri.move_to(play[0]).shift(RIGHT * 0.02)
            head = VGroup(play, t(title, 27, INK, SANS, weight="BOLD")).arrange(RIGHT, buff=0.2)
            k = t(kind + " · 4K", 21, ACCENT, MONO, weight="BOLD")
            m1 = t(f"{mmss(D[lk]['duration_s'])} + Short {mmss(D[vk]['duration_s'])}", 22, INK, MONO)
            g = VGroup(head, k, m1).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
            fit(g, SAFE_W - 0.4).move_to(c)
            return VGroup(c, g)

        a = vid("Brutalist, Shared", "PROGRESS VIDEO", "landscape/BrutalistShared_BoopeshM.mp4",
                "vertical/BrutalistShared_BoopeshM.mp4")
        b = vid("Deep Hedging", "STEM EXPLAINER", "landscape/DeepHedging_BoopeshM.mp4",
                "vertical/DeepHedging_BoopeshM.mp4")
        pair = VGroup(a, b).arrange(DOWN, buff=0.25)
        pair.move_to([CX, 1.95 - pair.height / 2, 0])

        drive = svg("google-drive-01.svg", height=0.26)
        g1 = VGroup(drive, t("✓ on Drive", 21, GOOD, weight="BOLD")).arrange(RIGHT, buff=0.12)
        b1 = card(1.8, 0.5).move_to(g1)
        gh = png("github-01.png", 0.26)
        s2 = t("PR pending", 21, ACCENT, weight="BOLD")
        b2 = DashedVMobject(RoundedRectangle(width=1.8, height=0.5, corner_radius=0.08, stroke_color=ACCENT,
                                             stroke_width=3), num_dashes=24)
        stack = VGroup(b1, b2).arrange(RIGHT, buff=0.1).next_to(pair, DOWN, buff=0.25).set_x(CX)
        g1.move_to(b1)
        Group(gh, s2).arrange(RIGHT, buff=0.15).move_to(b2)

        clock.play_at(0.3, FadeIn(ghost_of(a[0])), FadeIn(ghost_of(b[0])),
                      FadeIn(ghost_of(b1)), FadeIn(b2.copy().set_stroke(GHOST)), run_time=0.4)
        clock.play_at(cue("B30", "Brutalist", 1.5), FadeIn(a, shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B30", "Deep Hedging", 2.8), FadeIn(b, shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B30", "on Drive", 5.0), FadeIn(b1), FadeIn(g1), run_time=0.5)
        clock.play_at(cue("B30", "still pending", 6.5), Create(b2), FadeIn(gh), FadeIn(s2), run_time=0.6)
        clock.finish()


# ======================================================================== B40 =
class B40_Takeaway(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        self.camera.background_color = DARK
        stmt = fit(t("Small weekly\nevidence\nadds up.", 52, ON_DARK, SERIF, weight="BOLD", line_spacing=0.9))
        stmt.move_to([CX, 2.2, 0])
        rows = VGroup()
        for name, what in (("README.md", "the result"), ("FACTCHECK.md", "every claim, sourced"),
                           ("FRICTIONAL.md", "what resisted"), ("source/", "rebuilds the video")):
            r = RoundedRectangle(width=SAFE_W, height=0.62, corner_radius=0.08, stroke_color=HOT_DARK, stroke_width=3)
            g = VGroup(t(name, 20, ON_DARK, MONO, weight="BOLD"), t(what, 16, "#D8D0C0")).arrange(DOWN, buff=0.06)
            rows.add(VGroup(r, g.move_to(r)))
        rows.arrange(DOWN, buff=0.14).move_to([CX, -0.85, 0])
        clock.play_at(0.2, FadeIn(rows.copy().set_color(DIM_DARK)), run_time=0.4)
        clock.play_at(cue("B40", "small weekly", 0.8), FadeIn(stmt, shift=UP * 0.1), run_time=0.6)
        for i, ph in enumerate(("A README", "a fact check", "a frictional log", "the source")):
            clock.play_at(max(cue("B40", ph, 2.5 + 0.8 * i), clock.t), FadeIn(rows[i], shift=UP * 0.08), run_time=0.4)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = fit(t("One Week\nof Fellows", 48, INK, SERIF, line_spacing=0.9))
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
