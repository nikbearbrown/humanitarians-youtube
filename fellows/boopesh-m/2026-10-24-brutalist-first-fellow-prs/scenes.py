# -*- coding: utf-8 -*-
"""
Manim scenes for "Brutalist, Shared" (16:9, 3840x2160) -- Boopesh M., week of Oct 18-24 2026.
  B20_Timeline    -- the week from git history; the three merges stack at Oct 23
  B30_Thumbnails  -- PR #1: real 4K thumbnails from runtime/thumbnails/out/claude-skills/@3x
  B40_Setup       -- PR #3: setup checks tick in a terminal panel
  B50_Speaker     -- PR #4: Teams recording -> speaker-series filmstrip, word-level mutes
  B60_Blender     -- three Blender skills, three jobs
  B70_Takeaway    -- dark statement card: branch -> pull request -> everyone
  B90_Outro       -- @HumanitariansAI outro + fellow credit
Claude palette (cream ground, warm ink, one terracotta accent). Every scene reads its own
beat's measured narration length from beat_sheet.json and lands on it exactly; cues are
placed at the share of the narration where the phrase is spoken.
"""
import json
from pathlib import Path

from manim import *

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"

BG = "#FAF9F5"       # cream
INK = "#2B2A26"      # warm ink
ACCENT = "#A64B2A"   # terracotta, darkened to pass WCAG 4.5:1 on cream (5.4:1) and panel (4.8:1)
MUTED = "#6F6A5E"    # secondary text (>= 4.5:1 on cream)
PANEL = "#EEEADF"    # soft card
LINE = "#D9D3C4"     # hairline
GOOD = "#3F6E4E"     # green tick
DARK = "#2B2A26"     # statement-card ground
ON_DARK = "#F5F1E8"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"


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


def logo(name, height):
    m = SVGMobject(str(ASSETS / name))
    m.scale_to_fit_height(height)
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


def framed(img_name, width):
    im = ImageMobject(str(ASSETS / img_name))
    im.scale_to_fit_width(width)
    border = Rectangle(width=im.width, height=im.height, stroke_color=LINE, stroke_width=3)
    border.move_to(im)
    return Group(im, border)


# ======================================================================== B20 =
SAFE_W = 12.6   # usable width inside the 14.22-unit frame


def fit(m, w=SAFE_W):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


class B20_Timeline(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header("brutalist.art · git log 4115560a..a99b5323", "One week in the commit history")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        days = list(range(18, 25))
        x0, x1, y = -5.4, 5.4, -1.0
        xs = {d: x0 + (x1 - x0) * i / (len(days) - 1) for i, d in enumerate(days)}
        axis = Line([x0 - 0.4, y, 0], [x1 + 0.4, y, 0], color=INK, stroke_width=4)
        ticks = VGroup()
        for d in days:
            ticks.add(Line([xs[d], y - 0.1, 0], [xs[d], y + 0.1, 0], color=INK, stroke_width=4))
            ticks.add(t(f"Oct {d}", 22, MUTED, MONO).move_to([xs[d], y - 0.42, 0]))
        clock.play_at(0.6, Create(axis), FadeIn(ticks, lag_ratio=0.08), run_time=1.0)

        def event(d, lines, center, logo_name):
            dot = Dot([xs[d], y, 0], radius=0.12, color=ACCENT)
            rows = VGroup(*[t(s, 24, INK) for s in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
            rows = VGroup(logo(logo_name, 0.5), rows).arrange(RIGHT, buff=0.25)
            box = card(rows.width + 0.5, rows.height + 0.4).move_to(center)
            rows.move_to(box)
            above = center[1] > y
            edge = box.get_bottom() if above else box.get_top()
            start = dot.get_center() if above else [xs[d], y - 0.7, 0]   # below the date label
            stem = Line(start, [xs[d], edge[1], 0], color=LINE, stroke_width=3)
            return dot, VGroup(stem, box, rows)

        d18, e18 = event(18, ["Oct 18", "building-walkthrough", "blender-build"], [-4.0, 0.55, 0], "blender-01.svg")
        clock.play_at(cue("B20", "October eighteenth", 2.0), GrowFromCenter(d18), FadeIn(e18, shift=UP * 0.2), run_time=0.8)
        d21, e21 = event(21, ["Oct 21", "blender-modelbuild", "blender-build, image-based"], [0, -2.75, 0], "blender-01.svg")
        clock.play_at(cue("B20", "October twenty-first", 5.0), GrowFromCenter(d21), FadeIn(e21, shift=DOWN * 0.2), run_time=0.8)

        dot23 = Dot([xs[23], y, 0], radius=0.14, color=ACCENT)
        merges = [("20:12:21", "PR #4", "SEIS speaker series"),
                  ("20:12:24", "PR #3", "setup fixes"),
                  ("20:12:28", "PR #1", "thumbnails")]
        rows = VGroup()
        for ts, pr, what in merges:
            rows.add(VGroup(t(ts, 22, MUTED, MONO), t(pr, 22, ACCENT, MONO, weight="BOLD"), t(what, 24, INK))
                     .arrange(RIGHT, buff=0.25))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        head = t("Oct 23 · merged", 24, INK, weight="BOLD")
        lab = t("all three within 7 seconds", 24, ACCENT, weight="BOLD")
        body = VGroup(head, rows, lab).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        gh = ImageMobject(str(ASSETS / "github-01.png"))
        gh.scale_to_fit_height(0.6)
        stack = Group(gh, body).arrange(RIGHT, buff=0.3)
        box = card(stack.width + 0.5, stack.height + 0.45)
        box.move_to([2.55, 0.5, 0])
        lab.set_opacity(0)
        stack.move_to(box)
        stem = Line(dot23.get_center(), [xs[23], box.get_bottom()[1], 0], color=LINE, stroke_width=3)
        t23 = cue("B20", "twenty-third", 7.5)
        clock.play_at(t23, GrowFromCenter(dot23), Create(stem), FadeIn(box), FadeIn(gh), FadeIn(head), run_time=0.6)
        for i, r in enumerate(rows):
            clock.play_at(t23 + 0.6 + i * 0.45, FadeIn(r, shift=LEFT * 0.2), run_time=0.4)

        clock.play_at(cue("B20", "within ten seconds", 10.0), lab.animate.set_opacity(1),
                     Indicate(VGroup(*[r[0] for r in rows]), color=ACCENT, scale_factor=1.05), run_time=0.7)
        clock.finish()


# ======================================================================== B30 =
class B30_Thumbnails(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("pull request #1 · @gaurav-bakale", "A thumbnail generator")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        names = ["yt-code-review-top.png", "yt-superpowers-top.png", "yt-deep-research-top.png",
                 "yt-skill-creator-top.png", "yt-mcp-server-dev-top.png", "yt-frontend-design-top.png"]
        tiles = Group(*[framed(n, 3.55) for n in names]).arrange_in_grid(rows=2, cols=3, buff=0.3)
        tiles.move_to([0, -1.05, 0])
        start = cue("B30", "HTML templates", 2.5)
        for i, tile in enumerate(tiles):
            clock.play_at(start + i * 0.45, FadeIn(tile, scale=0.92), run_time=0.45)

        chips = VGroup()
        for s in ("HTML → YouTube-size PNG", "toolkit's own colours", "no faces"):
            lab = t(s, 22, INK)
            chips.add(VGroup(card(lab.width + 0.4, lab.height + 0.28, fill=PANEL), lab))
        for c in chips:
            c[1].move_to(c[0])
        chips.arrange(RIGHT, buff=0.25)
        chips.next_to(tiles, UP, buff=0.22)
        clock.play_at(cue("B30", "toolkit's own colours", 6.0), FadeIn(chips, lag_ratio=0.25), run_time=0.9)

        tl = cue("B30", "locked to one template", 9.0)
        a, b = framed(names[0], 5.7), framed(names[1], 5.7)
        pair = Group(a, b).arrange(RIGHT, buff=0.45).move_to([0, -0.55, 0])
        clock.play_at(tl, FadeOut(tiles), FadeOut(chips), FadeIn(pair, shift=UP * 0.2), run_time=0.8)
        same = t("one locked template", 26, MUTED).next_to(pair, UP, buff=0.25)
        clock.play_at(tl + 0.9, FadeIn(same), run_time=0.5)

        def mark(img, fx0, fy0, fx1, fy1):  # region given as fractions of the image
            w, h = img.width, img.height
            c = img.get_corner(UL)
            r = RoundedRectangle(width=(fx1 - fx0) * w, height=(fy1 - fy0) * h, corner_radius=0.06,
                                 stroke_color=ACCENT, stroke_width=6)
            return r.move_to(c + RIGHT * (fx0 + fx1) / 2 * w + DOWN * (fy0 + fy1) / 2 * h)

        cmd = VGroup(mark(a, 0.29, 0.74, 0.71, 0.93), mark(b, 0.29, 0.74, 0.71, 0.93))
        lab1 = t("only the command changes", 28, ACCENT, weight="BOLD")
        labs = VGroup(lab1).next_to(pair, DOWN, buff=0.3)
        clock.play_at(cue("B30", "changes only its command", 11.5), Create(cmd), FadeIn(lab1), run_time=0.7)

        src = t("real output · runtime/thumbnails/out/claude-skills/@3x · 3840×2160", 18, MUTED, MONO)
        src.next_to(labs, DOWN, buff=0.18)
        clock.play_at(cue("B30", "Everything on screen", 15.5), FadeIn(src), run_time=0.6)
        clock.finish()


# ======================================================================== B40 =
class B40_Setup(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        hd = header("pull request #3 · @meenuviji · 11 commits", "A fresh install that actually works")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        panel = RoundedRectangle(width=9.6, height=4.6, corner_radius=0.18, fill_color=DARK,
                                 fill_opacity=1, stroke_width=0).move_to([1.0, -1.05, 0])
        dots = VGroup(*[Dot(radius=0.07, color=c) for c in ("#E26D5C", "#E2B35C", "#7DB37A")]).arrange(RIGHT, buff=0.14)
        dots.move_to(panel.get_corner(UL) + RIGHT * 0.5 + DOWN * 0.3)
        left = panel.get_left()[0] + 0.55
        prompt = t("$ ./setup --install", 26, ON_DARK, MONO)
        prompt.move_to([left + prompt.width / 2, panel.get_top()[1] - 0.85, 0])
        py = logo("python-01.svg", 1.3).move_to([-5.4, -1.05, 0])
        clock.play_at(0.7, FadeIn(panel), FadeIn(dots), run_time=0.6)
        clock.play_at(1.3, AddTextLetterByLetter(prompt), run_time=0.9)

        checks = [("Python", "python3 ≥ 3.10 required"),
                  ("caption decoding", "faster-whisper decodes a real clip"),
                  ("caps a library", "av < 19: no transcription crash"),
                  ("loudness", "fellows: report loudness = narration")]
        prev = prompt
        for i, (phrase, line) in enumerate(checks):
            tick = t("✓", 28, "#8CCB8A", MONO, weight="BOLD")
            row = VGroup(tick, t(line, 26, ON_DARK, MONO)).arrange(RIGHT, buff=0.25)
            row.next_to(prev, DOWN, buff=0.36)
            row.shift(RIGHT * (left - row.get_left()[0]))
            prev = row
            at = cue("B40", phrase, 4.0 + i * 3)
            anims = [FadeIn(row, shift=RIGHT * 0.2)]
            if i == 0:
                anims.append(FadeIn(py, scale=0.8))
            clock.play_at(at, *anims, run_time=0.5)
            clock.play_at(at + 0.5, Indicate(tick, color="#B8F0B5", scale_factor=1.4), run_time=0.5)
        clock.finish()


# ======================================================================== B50 =
class B50_Speaker(Scene):
    def construct(self):
        clock = Clock(self, "B50")
        hd = header("pull request #4 · Aditi", "SEIS speaker series")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        segs = [("SEIS\nlogo", 1.35, ACCENT, "logo reveal"), ("Speaker\nSeries N", 1.65, INK, "speaker card"),
                ("the talk + Q&A, uncut", 5.2, "#4A5560", "then the talk"),
                ("SEIS\nlogo", 1.35, ACCENT, "Q and A, uncut")]
        x = -3.85
        strip = VGroup()
        for label, w, col, _ in segs:
            r = Rectangle(width=w, height=1.4, fill_color=col, fill_opacity=1, stroke_color=BG, stroke_width=6)
            r.move_to([x + w / 2, -0.6, 0])
            lab = t(label, 22, ON_DARK, weight="BOLD", line_spacing=0.9).move_to(r)
            strip.add(VGroup(r, lab))
            x += w
        n_sp = 20
        sprockets = VGroup(*[Square(0.12, fill_color=INK, fill_opacity=1, stroke_width=0)
                             .move_to([-3.7 + k * ((x - 0.15) - (-3.7)) / (n_sp - 1), edge, 0])
                             for edge in (0.25, -1.45) for k in range(n_sp)])
        ghost = VGroup(*[p[0].copy().set_fill(opacity=0).set_stroke("#A39A88", 5) for p in strip])
        clock.play_at(0.6, FadeIn(ghost), FadeIn(sprockets.copy().set_color("#A39A88")), run_time=0.6)
        teams = logo("microsoft-teams-01.svg", 1.0).move_to([-5.2, -0.6, 0])
        tl = t("1–4 hour Teams\nrecording", 20, MUTED, line_spacing=0.9).next_to(teams, DOWN, buff=0.2)
        clock.play_at(cue("B50", "Teams recording", 4.0), FadeIn(teams, scale=0.8), FadeIn(tl), run_time=0.6)
        arrow = Arrow([-4.5, -0.6, 0], [-3.95, -0.6, 0], color=ACCENT, stroke_width=8, buff=0)
        clock.play_at(cue("B50", "into a finished film", 6.5), GrowArrow(arrow), run_time=0.5)

        for i, (piece, seg) in enumerate(zip(strip, segs)):
            at = cue("B50", seg[3], 7.0 + i)
            anims = [FadeIn(piece, shift=LEFT * 0.3)]
            if i == 0:
                anims.append(FadeIn(sprockets, lag_ratio=0.02))
            clock.play_at(max(at, clock.t), *anims, run_time=0.55)

        talk = strip[2][0]
        base_y = talk.get_bottom()[1] - 1.05
        import math
        wave = VGroup()
        n = 64
        for k in range(n):
            hgt = 0.12 + 0.5 * abs(math.sin(k * 0.73) * math.cos(k * 0.21))
            xk = talk.get_left()[0] + 0.1 + k * (talk.width - 0.2) / (n - 1)
            wave.add(Line([xk, base_y - hgt / 2, 0], [xk, base_y + hgt / 2, 0], color=MUTED, stroke_width=5))
        clock.play_at(clock.t, FadeIn(wave, lag_ratio=0.01), run_time=0.6)
        mutes = [11, 29, 48]
        marks = VGroup(*[SurroundingRectangle(wave[k], color=ACCENT, buff=0.06, stroke_width=5) for k in mutes])
        ml = t("word-level mutes", 24, ACCENT, weight="BOLD").next_to(wave, DOWN, buff=0.28)
        clock.play_at(cue("B50", "word-level mutes", 12.0), *[wave[k].animate.set_color(LINE) for k in mutes],
                     Create(marks), FadeIn(ml), run_time=0.7)
        clock.finish()


# ======================================================================== B60 =
class B60_Blender(Scene):
    def construct(self):
        clock = Clock(self, "B60")
        bl = logo("blender-01.svg", 0.8)
        hd = header("three new skills · Oct 18–21", "Brutalist goes 3D")
        bl.next_to(hd[1], RIGHT, buff=0.35)
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), FadeIn(bl, scale=0.8), run_time=0.8)

        specs = [("building-walkthrough", "measure the camera route,\nthen render", "Building walkthrough"),
                 ("blender-build", "learn to build it from\nthe finished images", "Blender build teaches"),
                 ("blender-modelbuild", "film from real build evidence:\nAI script vs hand steps", "Blender model build")]
        CW, CH = 3.9, 4.2
        cards = VGroup()
        for name, job, _ in specs:
            c = card(CW, CH)
            nm = fit(t(name, 24, INK, MONO, weight="BOLD"), CW - 0.4)
            jb = fit(t(job, 22, MUTED, line_spacing=1.0), CW - 0.4)
            cards.add(VGroup(c, nm, jb))
        cards.arrange(RIGHT, buff=0.3).move_to([0, -1.0, 0])

        icons = []
        c0 = cards[0][0]
        pts = [c0.get_center() + v for v in (LEFT * 1.3 + DOWN * 0.1, LEFT * 0.5 + UP * 0.45,
                                              RIGHT * 0.3 + DOWN * 0.2, RIGHT * 1.2 + UP * 0.35)]
        route = VMobject(color=ACCENT, stroke_width=6).set_points_smoothly(pts)
        cam = VGroup(Rectangle(width=0.4, height=0.28, fill_color=INK, fill_opacity=1, stroke_width=0),
                     Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.12).rotate(-PI / 2))
        cam[1].next_to(cam[0], RIGHT, buff=0)
        cam.move_to(route.get_start())
        ruler = VGroup(*[Line(UP * 0.08, DOWN * 0.08, color=MUTED, stroke_width=3).move_to(route.point_from_proportion(p))
                         for p in (0.2, 0.4, 0.6, 0.8)])
        icons.append(VGroup(route, ruler, cam))
        c1 = cards[1][0]
        frames = VGroup(*[Rectangle(width=0.9, height=0.66, stroke_color=INK, stroke_width=4) for _ in range(3)])
        frames.arrange(RIGHT, buff=0.14)
        for f, sc in zip(frames, (0.75, 0.95, 0.6)):
            f.add(Square(0.5, stroke_color=ACCENT, stroke_width=5).rotate(PI / 4).scale(sc).move_to(f))
        icons.append(frames)
        lft = card(1.45, 0.66, fill="#DCD4C2")
        rgt = card(1.45, 0.66, fill="#F6DCCF")
        pair = VGroup(VGroup(lft, t("AI script", 18, INK, MONO)), VGroup(rgt, t("by hand", 18, INK, MONO)))
        for g in pair:
            g[1].move_to(g[0])
        pair.arrange(RIGHT, buff=0.2)
        icons.append(pair)

        for (c, nm, jb), ic in zip(cards, icons):
            nm.move_to(c.get_top() + DOWN * 0.5)
            ic.move_to(c.get_center() + UP * 0.2)
            jb.move_to(c.get_bottom() + UP * 0.8)

        for i, ((_, _, phrase), (c, nm, jb), ic) in enumerate(zip(specs, cards, icons)):
            at = cue("B60", phrase, 2.0 + 5 * i)
            clock.play_at(at, FadeIn(c, shift=UP * 0.2), FadeIn(nm), run_time=0.5)
            if i == 0:
                clock.play_at(clock.t, FadeIn(VGroup(route, ruler)), FadeIn(cam), run_time=0.4)
                clock.play_at(clock.t, MoveAlongPath(cam, route), FadeIn(jb), run_time=1.6)
            else:
                clock.play_at(clock.t, FadeIn(ic, lag_ratio=0.3), FadeIn(jb), run_time=0.8)
        clock.finish()


# ======================================================================== B70 =
class B70_Takeaway(Scene):
    def construct(self):
        clock = Clock(self, "B70")
        self.camera.background_color = DARK
        line1 = t("You don't have to be the maintainer", 68, ON_DARK, SERIF, weight="BOLD")
        line2 = t("to improve the tool you use.", 68, ON_DARK, SERIF, weight="BOLD")
        stmt = fit(VGroup(line1, line2).arrange(DOWN, buff=0.28)).move_to(UP * 1.7)

        nodes = ["your branch", "pull request", "everyone's toolkit"]
        boxes = VGroup()
        for s in nodes:
            lab = t(s, 34, ON_DARK, MONO)
            r = RoundedRectangle(width=lab.width + 0.9, height=1.25, corner_radius=0.14,
                                 stroke_color="#E08A6A", stroke_width=5)
            boxes.add(VGroup(r, lab.move_to(r)))
        boxes.arrange(RIGHT, buff=0.9).move_to(DOWN * 1.9)
        fit(boxes)
        arrows = VGroup(*[Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), color="#E08A6A",
                                stroke_width=6, buff=0.12) for i in range(2)])
        dim = VGroup(boxes, arrows).copy().set_color("#5E544C")   # the path, before anyone walks it
        clock.play_at(0.2, FadeIn(dim), run_time=0.6)
        clock.play_at(cue("B70", "You don't have to", 1.5), FadeIn(line1, shift=UP * 0.15), run_time=0.7)
        clock.play_at(clock.t + 0.6, FadeIn(line2, shift=UP * 0.15), run_time=0.7)
        at = cue("B70", "a fellow's own branch", 6.0)
        clock.play_at(at, FadeIn(boxes[0]), run_time=0.5)
        clock.play_at(cue("B70", "through a pull request", at + 1.5), GrowArrow(arrows[0]), FadeIn(boxes[1]), run_time=0.6)
        clock.play_at(clock.t + 0.3, GrowArrow(arrows[1]), FadeIn(boxes[2]), run_time=0.6)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = t("Brutalist, Shared", 92, INK, SERIF)
        pill_lab = t("SUBSCRIBE", 32, ON_DARK, SANS, weight="BOLD")
        pill = RoundedRectangle(width=pill_lab.width + 0.8, height=0.74, corner_radius=0.37,
                                fill_color=DARK, fill_opacity=1, stroke_width=0)
        pill_lab.move_to(pill)
        hai = logo("hai-logo.svg", 0.52).set_color(INK)
        handle = t("@HumanitariansAI", 38, INK, SANS, weight="BOLD")
        row = VGroup(VGroup(pill, pill_lab), hai, handle).arrange(RIGHT, buff=0.3)
        main = VGroup(title, row).arrange(DOWN, buff=0.55).move_to(UP * 1.45)
        clock.play_at(0.2, FadeIn(title, shift=UP * 0.15), run_time=0.8)
        clock.play_at(clock.t + 0.1, FadeIn(row, shift=UP * 0.1), run_time=0.6)

        rule = Line(LEFT * 3.4, RIGHT * 3.4, color=LINE, stroke_width=3).next_to(main, DOWN, buff=0.7)
        c1 = t("Boopesh M.", 46, INK, SERIF, weight="BOLD")
        c2 = t("Humanitarians AI Fellow · Brutalist team", 32, MUTED)
        c3 = t("Narration: AI voice (Kokoro am_onyx) reading Boopesh's script", 26, MUTED)
        credit = VGroup(c1, c2, c3).arrange(DOWN, buff=0.22).next_to(rule, DOWN, buff=0.5)
        clock.play_at(cue("B90", "with Boopesh", 1.5), Create(rule), FadeIn(credit, shift=UP * 0.1), run_time=0.7)
        clock.finish()
