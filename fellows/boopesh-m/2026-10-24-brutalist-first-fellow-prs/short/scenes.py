# -*- coding: utf-8 -*-
"""
Manim scenes for the 9:16 Short of "Brutalist, Shared" (2160x3840) -- Boopesh M.
  B10_Merges    -- the first three pull requests ever, merged within 7 seconds
  B20_ThreePRs  -- one card per pull request (PR #1 card shows a real 4K thumbnail)
  B30_Blender   -- three Blender skills: Brutalist goes 3D
  B40_Takeaway  -- dark statement card: branch -> pull request -> everyone
  B90_Outro     -- @HumanitariansAI outro + fellow credit
Native portrait layouts (frame 4.5 x 8 units). Key content sits between y = -2.3 and 3.5 and
left of the Shorts action rail, clear of YouTube's bottom caption overlay.
Claude palette; each scene lands exactly on its beat's measured narration length.
"""
import json
from pathlib import Path

from manim import *

# Portrait frame in scene units: 4.5 wide x 8 tall (matches 2160x3840 pixels).
config.frame_width = 4.5
config.frame_height = 8.0

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"   # terracotta, WCAG 4.5:1+ on cream and panel
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

CX = -0.15        # content centre, nudged left of the Shorts action rail
SAFE_W = 3.7


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


TYPE_SCALE = 0.72   # sizes below are authored on a phone-legibility scale


KERN = 4            # set text large, then scale down: Pango kerns small Manim text unevenly


def t(s, size=24, color=INK, font=SANS, weight="NORMAL", **kw):
    m = Text(s, font=font, font_size=size * TYPE_SCALE * KERN, color=color, weight=weight, **kw)
    return m.scale(1 / KERN)


def fit(m, w=SAFE_W):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def logo(name, height):
    m = SVGMobject(str(ASSETS / name))
    m.scale_to_fit_height(height)
    return m


def png(name, height):
    m = ImageMobject(str(ASSETS / name))
    m.scale_to_fit_height(height)
    return m


def card(w, h, fill=PANEL):
    return RoundedRectangle(width=w, height=h, corner_radius=0.08, fill_color=fill,
                            fill_opacity=1, stroke_width=0)


def header(kicker, title):
    k = t(kicker.upper(), 13, MUTED, MONO)
    h = fit(t(title, 34, INK, SERIF, weight="BOLD", line_spacing=0.9))
    g = VGroup(k, h).arrange(DOWN, buff=0.12)
    g.move_to([CX, 3.1 - g.height / 2, 0])
    return g


# ======================================================================== B10 =
class B10_Merges(Scene):
    def construct(self):
        clock = Clock(self, "B10")
        hd = header("brutalist.art · Oct 23, 2026", "The first three\npull requests, ever")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        merges = [("PR #4", "SEIS speaker series", "20:12:21"),
                  ("PR #3", "setup fixes", "20:12:24"),
                  ("PR #1", "thumbnail generator", "20:12:28")]
        cards = VGroup()
        for pr, what, ts in merges:
            body = VGroup(t(pr, 24, ACCENT, MONO, weight="BOLD"), t(what, 26, INK)).arrange(RIGHT, buff=0.2)
            stamp = t(ts, 22, MUTED, MONO)
            inner = VGroup(fit(body, SAFE_W - 0.45), stamp).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
            c = card(SAFE_W, inner.height + 0.5)
            inner.move_to(c).align_to(c, LEFT).shift(RIGHT * 0.24)
            cards.add(VGroup(c, inner))
        cards.arrange(DOWN, buff=0.24)
        cards.move_to([CX, 1.45 - cards.height / 2, 0])
        ghost = VGroup(*[c[0].copy().set_fill(opacity=0).set_stroke("#A39A88", 3) for c in cards])
        clock.play_at(0.5, FadeIn(ghost), run_time=0.4)
        at = cue("B10", "merged the first three", 1.2)
        for i, c in enumerate(cards):
            clock.play_at(at + i * 0.45, FadeIn(c, shift=UP * 0.15), run_time=0.4)

        gh = png("github-01.png", 0.5)
        lab = t("all three within 7 seconds", 28, ACCENT, weight="BOLD")
        foot = Group(gh, lab).arrange(RIGHT, buff=0.18)
        fit(foot).next_to(cards, DOWN, buff=0.45)
        clock.play_at(cue("B10", "All three", 4.5), FadeIn(foot, shift=UP * 0.1),
                      Indicate(VGroup(*[c[1][1] for c in cards]), color=ACCENT, scale_factor=1.08), run_time=0.7)
        clock.finish()


# ======================================================================== B20 =
class B20_ThreePRs(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("what got merged", "Three pull requests")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.1), run_time=0.6)

        thumb = Group(png("yt-code-review-top.png", 0.9))
        thumb.add(Rectangle(width=thumb[0].width, height=thumb[0].height, stroke_color=LINE,
                            stroke_width=2).move_to(thumb[0]))
        rows = [
            (thumb, "PR #1", "thumbnail generator", "real 4K output", "thumbnail generator"),
            (logo("python-01.svg", 0.7), "PR #3", "setup fixes", "a fresh install just works", "Setup fixes"),
            (logo("microsoft-teams-01.svg", 0.7), "PR #4", "speaker series", "hour-long talk → finished film", "speaker-series engine"),
        ]
        groups = []
        y = 1.75
        for vis, pr, name, sub, phrase in rows:
            txt = VGroup(t(pr, 18, ACCENT, MONO, weight="BOLD"), t(name, 24, INK, weight="BOLD"),
                         t(sub, 18, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            if vis is thumb:
                block = Group(vis, txt).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
            else:
                block = Group(vis, txt).arrange(RIGHT, buff=0.25)
            c = card(SAFE_W, block.height + 0.34)
            c.move_to([CX, y - c.height / 2, 0])
            block.move_to(c).align_to(c, LEFT).shift(RIGHT * 0.22)
            y -= c.height + 0.16
            groups.append((Group(c, block), phrase))
        for g, phrase in groups:
            clock.play_at(max(cue("B20", phrase, clock.t), clock.t), FadeIn(g, shift=UP * 0.15), run_time=0.5)
        clock.finish()


# ======================================================================== B30 =
class B30_Blender(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        bl = logo("blender-01.svg", 1.9).move_to([CX, 2.2, 0])
        title = fit(t("Brutalist goes 3D", 50, INK, SERIF, weight="BOLD")).move_to([CX, 0.75, 0])
        chips = VGroup()
        for s_ in ("building-walkthrough", "blender-build", "blender-modelbuild"):
            lab = t(s_, 24, INK, MONO, weight="BOLD")
            chips.add(VGroup(card(SAFE_W - 0.3, lab.height + 0.42), lab))
        for c in chips:
            c[1].move_to(c[0])
        chips.arrange(DOWN, buff=0.2).move_to([CX, -1.0, 0])
        ghost = VGroup(*[c[0].copy().set_fill(opacity=0).set_stroke("#A39A88", 3) for c in chips])
        clock.play_at(0, FadeIn(bl, scale=0.7), FadeIn(ghost), run_time=0.6)
        clock.play_at(0.4, FadeIn(title, shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B30", "three new Blender skills", 1.0), FadeIn(chips, lag_ratio=0.35), run_time=1.0)
        clock.finish()


# ======================================================================== B40 =
class B40_Takeaway(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        self.camera.background_color = DARK
        stmt = fit(t("You don't need to be\nthe maintainer to\nimprove your tools.", 44, ON_DARK, SERIF,
                     weight="BOLD", line_spacing=0.95))
        stmt.move_to([CX, 2.2, 0])
        nodes = VGroup()
        for s_ in ("fix what's in your way", "open a pull request", "everyone's toolkit"):
            lab = t(s_, 24, ON_DARK, MONO)
            r = RoundedRectangle(width=SAFE_W - 0.2, height=0.72, corner_radius=0.09,
                                 stroke_color="#E08A6A", stroke_width=3)
            nodes.add(VGroup(r, fit(lab, SAFE_W - 0.5).move_to(r)))
        nodes.arrange(DOWN, buff=0.5).move_to([CX, -0.95, 0])
        arrows = VGroup(*[Arrow(nodes[i].get_bottom(), nodes[i + 1].get_top(), color="#E08A6A",
                                stroke_width=5, buff=0.06, max_tip_length_to_length_ratio=0.35) for i in range(2)])
        dim = VGroup(nodes, arrows).copy().set_color("#5E544C")
        clock.play_at(0, FadeIn(dim), run_time=0.5)
        clock.play_at(cue("B40", "you don't need", 0.8), FadeIn(stmt, shift=UP * 0.1), run_time=0.8)
        clock.play_at(cue("B40", "Fix what's in your way", 3.5), FadeIn(nodes[0], shift=DOWN * 0.1), run_time=0.5)
        clock.play_at(cue("B40", "open a pull request", 5.0), GrowArrow(arrows[0]), FadeIn(nodes[1]), run_time=0.5)
        clock.play_at(clock.t + 0.3, GrowArrow(arrows[1]), FadeIn(nodes[2]), run_time=0.5)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = fit(t("Brutalist, Shared", 56, INK, SERIF))
        pill_lab = t("SUBSCRIBE", 24, ON_DARK, SANS, weight="BOLD")
        pill = RoundedRectangle(width=pill_lab.width + 0.55, height=0.56, corner_radius=0.28,
                                fill_color=DARK, fill_opacity=1, stroke_width=0)
        pill_lab.move_to(pill)
        hai = logo("hai-logo.svg", 0.42).set_color(INK)
        handle = t("@HumanitariansAI", 28, INK, SANS, weight="BOLD")
        row = VGroup(hai, handle).arrange(RIGHT, buff=0.18)
        main = VGroup(title, VGroup(pill, pill_lab), row).arrange(DOWN, buff=0.42).move_to([CX, 1.9, 0])
        clock.play_at(0.2, FadeIn(title, shift=UP * 0.1), run_time=0.6)
        clock.play_at(clock.t, FadeIn(main[1:], shift=UP * 0.1), run_time=0.5)
        rule = Line(LEFT * 1.6, RIGHT * 1.6, color=LINE, stroke_width=3).next_to(main, DOWN, buff=0.55)
        credit = VGroup(t("Boopesh M.", 36, INK, SERIF, weight="BOLD"),
                        t("Humanitarians AI Fellow", 24, MUTED),
                        t("Brutalist team", 24, MUTED),
                        fit(t("AI narration (Kokoro am_onyx)", 20, MUTED))).arrange(DOWN, buff=0.16)
        credit.next_to(rule, DOWN, buff=0.4)
        clock.play_at(cue("B90", "With Boopesh", 1.5), Create(rule), FadeIn(credit, shift=UP * 0.1), run_time=0.6)
        clock.finish()
