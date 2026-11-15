"""Manim scenes for what-is-ppo ("What PPO Is, In Plain Words").

One file, two native layouts: the scenes lay out side by side at 3840x2160 and stacked at
2160x3840 (vertical/scenes.py is a byte-identical copy). Every number and curve comes from
env.py (lakshdhamija/rl-autoscaler @ 8b126bd) and stable-baselines3 2.9.2; see evidence/facts_stdout.txt.
Each scene lasts exactly its beat's measured narration (beat_sheet.json is the clock).
Palette: humanitarians (brands/hai.md). Type: EB Garamond + Montserrat, Menlo for code.
Type floor: 26 pt (41 px at 2160, 73 px at 3840). Portrait text stays above y = -2.85
(GATE T keeps the bottom 14% of a 9:16 frame free of text).
"""
import json
from pathlib import Path

import numpy as np
from manim import *

# manim -r 2160,3840 keeps the 16:9 frame width; a portrait layout needs a 4.5 x 8 frame.
PORTRAIT = config.pixel_height > config.pixel_width
if PORTRAIT:
    config.frame_height = 8.0
    config.frame_width = 8.0 * config.pixel_width / config.pixel_height
SX, SY = (1.94, 3.39) if PORTRAIT else (6.28, 3.39)   # title-safe half extents (audit: 1.95 / 6.3 x 3.4)
TEXT_FLOOR = -2.85 if PORTRAIT else -SY             # lowest y any text may reach

CREAM, INK, TEAL, CRIMSON = "#F3EBDD", "#2F2A26", "#1F4E5F", "#E4572E"
SLATE, GOLD, GREY, TERRA = "#29335C", "#F3A712", "#A39A8E", "#D97757"
TEAL_LINE = "#3B8EA5"   # lighter teal, so the yesterday-rule line separates from the navy requests line
if PORTRAIT:
    # At 2160x3840 the anti-aliased edges of #29335C marks read as small ink "text runs" to GATE T,
    # so portrait uses a bluer navy (6.4:1 on cream) whose edges never approach the ink colours.
    SLATE = "#3A4F9A"
SERIF, SANS, MONO = "EB Garamond", "Montserrat", "Menlo"
HERE = Path(__file__).resolve().parent



def beat_seconds(bid, default):
    """The beat's measured narration length (the clock). Falls back when run outside the reel."""
    try:
        for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]:
            if b["beat_id"] == bid:
                return float(b.get("render_duration_s") or b.get("actual_duration_s") or default)
    except Exception:
        pass
    return default


def T(s, size=30, color=INK, font=SANS, weight="NORMAL", **kw):
    """Text built at 48 pt and scaled (avoids Pango's small-size glyph gaps)."""
    return Text(s, font=font, font_size=48, color=color, weight=weight, **kw).scale(max(size, 26) / 48)


def stack(*lines, size=30, color=INK, font=SANS, weight="NORMAL", buff=0.1, aligned=LEFT):
    return VGroup(*[T(s, size, color, font, weight) for s in lines]).arrange(DOWN, buff=buff, aligned_edge=aligned)


def place(m, x=None, y=None, left=None, top=None, right=None, bottom=None):
    """Position by an edge or the center, in frame units."""
    if left is not None:
        m.shift((left - m.get_left()[0]) * RIGHT)
    if right is not None:
        m.shift((right - m.get_right()[0]) * RIGHT)
    if x is not None:
        m.shift((x - m.get_center()[0]) * RIGHT)
    if top is not None:
        m.shift((top - m.get_top()[1]) * UP)
    if bottom is not None:
        m.shift((bottom - m.get_bottom()[1]) * UP)
    if y is not None:
        m.shift((y - m.get_center()[1]) * UP)
    return m


def column(items, top, bottom, left=None, min_gap=0.12):
    """Stack items top to bottom, spreading the spare height evenly (fills the canvas)."""
    gap = max(min_gap, (top - bottom - sum(i.height for i in items)) / max(len(items) - 1, 1))
    y = top
    for i in items:
        place(i, top=y)
        if left is not None:
            place(i, left=left)
        y = i.get_bottom()[1] - gap
    return items


def hai_mark(height, color=INK, opacity=1.0):
    """The Humanitarians AI mark (logos/humanitarians/humanitarians-logo-1.svg), as polygons."""
    polys = [[(0, 0), (74, 0), (74, 148), (178, 148), (206, 218), (74, 218), (74, 368), (0, 368)],
             [(81, 1), (153, 1), (302, 367), (228, 367)],
             [(237, 0), (311, 0), (311, 368), (237, 368)]]
    g = VGroup(*[Polygon(*[np.array([x, -y, 0.0]) for x, y in p], stroke_width=0,
                         fill_color=color, fill_opacity=opacity) for p in polys])
    return g.scale_to_fit_height(height)


def logo(name, height):
    return ImageMobject(str(HERE / "assets" / f"{name}-01.png")).scale_to_fit_height(height)


def headline(landscape, *portrait):
    """Serif headline, top-left, with a gold highlighter rule beneath."""
    lines = portrait if PORTRAIT else (landscape,)
    h = stack(*lines, size=40 if PORTRAIT else 46, font=SERIF, buff=0.04)
    place(h, left=-SX, top=SY)
    rule = Rectangle(width=h.width, height=0.07, stroke_width=0, fill_color=GOLD, fill_opacity=1)
    place(rule, left=-SX, top=h.get_bottom()[1] - 0.1)
    return VGroup(h, rule)


class Beat:
    """Timing helpers. run.sh only discovers scene classes that subclass Scene directly, so these
    methods are attached to Scene below instead of being inherited from a subclass."""
    BID, DEFAULT = "B00", 10.0

    def begin(self):
        self.camera.background_color = CREAM
        self.D = beat_seconds(self.BID, self.DEFAULT)
        self.el = 0.0
        self.add(place(hai_mark(0.42, INK, 0.3), right=SX, bottom=-SY))

    def P(self, *anims, rt=1.0):
        self.play(*anims, run_time=rt)
        self.el += rt

    def at(self, frac):
        """Hold until this fraction of the narration."""
        t = frac * self.D
        if t - self.el > 0.02:
            self.wait(t - self.el)
            self.el = t

    def end(self):
        self.at(1.0)


for _name in ("begin", "P", "at", "end"):
    setattr(Scene, _name, getattr(Beat, _name))


class Box:
    """Maps data coordinates into a rectangle of the frame."""

    def __init__(self, x0, y0, x1, y1, xr, yr):
        self.x0, self.y0, self.x1, self.y1, self.xr, self.yr = x0, y0, x1, y1, xr, yr

    def p(self, x, y):
        fx = (x - self.xr[0]) / (self.xr[1] - self.xr[0])
        fy = (y - self.yr[0]) / (self.yr[1] - self.yr[0])
        return np.array([self.x0 + fx * (self.x1 - self.x0), self.y0 + fy * (self.y1 - self.y0), 0.0])

    def line(self, xs, ys, color, width=5, step=False):
        pts = []
        for i, (x, y) in enumerate(zip(xs, ys)):
            if step and i:
                pts.append(self.p(x, ys[i - 1]))
            pts.append(self.p(x, y))
        if step:
            pts.append(self.p(xs[-1] + 1, ys[-1]))
        return VMobject(stroke_color=color, stroke_width=width).set_points_as_corners(pts)

    def column(self, x, y0, y1, width, color, opacity):
        a, b = self.p(x - width / 2, y0), self.p(x + width / 2, y1)
        r = Rectangle(width=abs(b[0] - a[0]), height=max(abs(b[1] - a[1]), 1e-3), stroke_width=0,
                      fill_color=color, fill_opacity=opacity)
        return r.move_to((a + b) / 2)


def axes(box, yticks, xticks, xlabel=None, size=28):
    """Baseline, y gridlines and tick labels, all kept clear of the plot area."""
    g = VGroup(Line(box.p(box.xr[0], box.yr[0]), box.p(box.xr[1], box.yr[0]), stroke_color=INK, stroke_width=3))
    for v, s in yticks:
        if v not in (box.yr[0], 0):
            g.add(DashedLine(box.p(box.xr[0], v), box.p(box.xr[1], v), stroke_color=GREY, stroke_width=1.5,
                             dash_length=0.06))
        g.add(place(T(s, size, SLATE), right=box.x0 - 0.12, y=box.p(0, v)[1]))
    for v, s in xticks:
        g.add(place(T(s, size, SLATE), x=box.p(v, 0)[0], top=box.y0 - 0.12))
    if xlabel:
        xl = place(T(xlabel, size, SLATE), x=(box.x0 + box.x1) / 2, top=box.y0 - 0.55)
        if xl.get_right()[0] > SX:
            place(xl, right=SX)
        if xl.get_left()[0] < -SX:
            place(xl, left=-SX)
        g.add(xl)
    return g


def swatch(color, label, kind="line", size=28):
    if kind == "line" and PORTRAIT:   # a short bar: a thin swatch line reads as a small text run in 9:16
        mark = Rectangle(width=0.34, height=0.24, stroke_width=0, fill_color=color, fill_opacity=1)
    elif kind == "line":
        mark = Line(LEFT * 0.25, RIGHT * 0.25, stroke_color=color, stroke_width=7)
    elif kind == "outline":
        mark = Square(0.3, stroke_color=color, stroke_width=5, fill_opacity=0)
    else:
        mark = Square(0.3, stroke_width=0, fill_color=color, fill_opacity=0.45 if kind == "fill" else 1)
    return VGroup(mark, T(label, size)).arrange(RIGHT, buff=0.16)


def k(v):
    return f"{int(round(v)):,}"





# Facts used on screen (evidence/facts_stdout.txt): 25 observation numbers, 11 actions (-5..+5 servers),
# n_steps 2048, clip_range 0.2, n_epochs 10. Example probabilities and advantages are illustrations.
N_STEPS, CLIP, N_EPOCHS = 2048, 0.2, 10
EXAMPLE_ODDS = [0.02, 0.03, 0.04, 0.06, 0.10, 0.18, 0.22, 0.16, 0.10, 0.05, 0.04]   # illustration, sums to 1


def card(lines, w, h, stroke=INK, fill=None, size=30, weight="NORMAL"):
    box = RoundedRectangle(width=w, height=h, corner_radius=0.15, stroke_color=stroke, stroke_width=4,
                           fill_color=fill or CREAM, fill_opacity=1)
    txt = stack(*lines, size=size, weight=weight, buff=0.06, aligned=ORIGIN).move_to(box)
    return VGroup(box, txt)


def math(tex, size=1.0, color=INK):
    return MathTex(tex, color=color).scale(size)


# --------------------------------------------------------------------------------------------
# B02: the running example. What the agent sees (25 numbers) and the 11 actions it can take (env.py).
# --------------------------------------------------------------------------------------------
class B02_Agent(Scene):
    BID, DEFAULT = "B02", 15.0

    def construct(self):
        self.begin()
        hl = headline("Every minute: 25 numbers in, 1 action out", "25 numbers in,", "1 action out")
        groups = [(10, SLATE, "requests, last 10 minutes"), (10, GREY, "yesterday's requests, next 10"),
                  (1, TEAL, "servers running"), (1, TEAL, "servers booting"), (1, CRIMSON, "queue"),
                  (2, GOLD, "time of day")]
        if PORTRAIT:
            groups = [(10, SLATE, "past 10 min"), (10, GREY, "yesterday 10"), (1, TEAL, "running"),
                      (1, TEAL, "booting"), (1, CRIMSON, "queue"), (2, GOLD, "time of day")]
        cell = 0.11 if PORTRAIT else 0.34
        rows = VGroup()
        for n, col, lab in groups:
            cells = VGroup(*[Square(cell, stroke_width=2, stroke_color=CREAM, fill_color=col, fill_opacity=1)
                             for _ in range(n)]).arrange(RIGHT, buff=0.03)
            rows.add(VGroup(cells, T(lab, 26 if PORTRAIT else 28)))
        width = max(r[0].width for r in rows)
        for r in rows:
            r[0].align_to(ORIGIN, LEFT)
            r[1].next_to(r[0], RIGHT, buff=0.25 + width - r[0].width)
        rows.arrange(DOWN, buff=0.12 if PORTRAIT else 0.16, aligned_edge=LEFT)
        title = T("what the agent sees", 28, SLATE)
        chips = VGroup(*[card([f"{d:+d}" if d else "0"], 0.58 if PORTRAIT else 0.95, 0.42 if PORTRAIT else 0.62,
                              stroke=GREY, size=26 if PORTRAIT else 30) for d in range(-5, 6)]).arrange(RIGHT, buff=0.06 if PORTRAIT else 0.18)
        atitle = T("what it can do: change servers by", 28, SLATE) if not PORTRAIT else stack(
            "what it can do:", "change servers by", size=26, color=SLATE, buff=0.04)
        src = T("src/rl_autoscaler/env.py" if not PORTRAIT else "from env.py", 26, SLATE)
        if PORTRAIT:
            chips = VGroup(VGroup(*chips[:6]).copy().arrange(RIGHT, buff=0.06), VGroup(*chips[6:]).copy().arrange(RIGHT, buff=0.06))
            chips.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            title = VGroup()
            column([rows, atitle, chips, src], hl.get_bottom()[1] - 0.25, TEXT_FLOOR, left=-SX, min_gap=0.15)
            flat = VGroup(*chips[0], *chips[1])
        else:
            column([title, rows], hl.get_bottom()[1] - 0.3, -0.2, left=-SX, min_gap=0.2)
            place(atitle, left=-SX, top=rows.get_bottom()[1] - 0.45)
            place(chips, left=-SX, top=atitle.get_bottom()[1] - 0.2)
            place(src, left=-SX, bottom=-SY)
            flat = chips
        pick = flat[7]   # +2: an example choice, not a trained policy's
        self.P(FadeIn(hl), FadeIn(title), rt=0.6)
        self.P(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.15) for r in rows], lag_ratio=0.35), rt=0.45 * self.D)
        self.at(0.6)
        self.P(FadeIn(atitle), LaggedStart(*[FadeIn(c) for c in flat], lag_ratio=0.08), FadeIn(src), rt=1.6)
        self.P(pick[0].animate.set_fill(TEAL, 1).set_stroke(TEAL), pick[1].animate.set_color(CREAM), rt=0.5)
        self.end()


# --------------------------------------------------------------------------------------------
# B03: reward and the trial-and-error loop. The reward line is quoted from env.py.
# --------------------------------------------------------------------------------------------
class B03_Reward(Scene):
    BID, DEFAULT = "B03", 13.0

    def construct(self):
        self.begin()
        hl = headline("A score every minute: the reward", "Every minute,", "a reward")
        if PORTRAIT:
            agent = card(["agent"], 3.8, 0.8, stroke=TEAL, size=32, weight="BOLD")
            env = card(["environment:", "simulated cluster"], 3.8, 1.05, stroke=SLATE, size=28)
            VGroup(agent, env).arrange(DOWN, buff=1.25)
            place(VGroup(agent, env), x=0, top=hl.get_bottom()[1] - 0.25)
            a1 = Arrow(agent.get_corner(DL) + RIGHT * 0.2, env.get_corner(UL) + RIGHT * 0.2, buff=0.06, stroke_color=INK,
                       stroke_width=5, tip_length=0.15)
            a2 = Arrow(env.get_corner(UR) + LEFT * 0.2, agent.get_corner(DR) + LEFT * 0.2, buff=0.06, stroke_color=INK,
                       stroke_width=5, tip_length=0.15)
            mid = (agent.get_bottom()[1] + env.get_top()[1]) / 2
            # staggered: "action" under the agent, "25 numbers + reward" above the environment
            l1 = place(T("action", 26), left=a1.get_right()[0] + 0.15, top=agent.get_bottom()[1] - 0.1)
            l2 = place(stack("25 numbers", "+ reward", size=26, buff=0.02, aligned=RIGHT), right=a2.get_left()[0] - 0.15,
                       bottom=env.get_top()[1] + 0.1)
            code = stack("reward = -(cost", "  + late_penalty", "  * late)", size=26, font=MONO, buff=0.05)
            gloss = stack("cost: servers billed", "late: requests late", size=26, color=SLATE, buff=0.04)
            column([code, gloss], env.get_bottom()[1] - 0.25, TEXT_FLOOR, left=-SX, min_gap=0.12)
        else:
            agent = card(["agent"], 3.1, 1.6, stroke=TEAL, size=44, weight="BOLD")
            env = card(["environment:", "a simulated cluster"], 4.4, 1.6, stroke=SLATE, size=32)
            VGroup(agent, env).arrange(RIGHT, buff=4.6)
            place(VGroup(agent, env), x=0, top=hl.get_bottom()[1] - 0.8)
            a1 = Arrow(agent.get_right() + UP * 0.4, env.get_left() + UP * 0.4, buff=0.1, stroke_color=INK, stroke_width=6)
            a2 = Arrow(env.get_left() + DOWN * 0.4, agent.get_right() + DOWN * 0.4, buff=0.1, stroke_color=INK, stroke_width=6)
            l1 = place(T("action", 30), x=a1.get_center()[0], bottom=a1.get_top()[1] + 0.14)
            l2 = place(T("25 numbers + reward", 28), x=a2.get_center()[0], top=a2.get_bottom()[1] - 0.14)
            src = T("src/rl_autoscaler/env.py", 26, SLATE)
            line = T("reward = -(cost + c.late_penalty * late)", 34, INK, MONO)
            gloss = stack("cost: servers billed this minute", "late: requests not served in the minute they arrive",
                          size=28, color=SLATE, buff=0.08)
            g = VGroup(src, line, gloss).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            place(g, left=-SX, bottom=-SY + 0.05)
            code = VGroup(src, line)
        dot = Dot(radius=0.11, color=GOLD)
        path = VMobject().set_points_as_corners([a1.get_start(), a1.get_end(), a2.get_start(), a2.get_end(), a1.get_start()])
        self.P(FadeIn(hl), FadeIn(agent), FadeIn(env), rt=0.6)
        self.P(GrowArrow(a1), FadeIn(l1), rt=0.6)
        self.P(GrowArrow(a2), FadeIn(l2), rt=0.6)
        self.at(0.3)
        self.P(FadeIn(code, shift=UP * 0.1), rt=0.8)
        self.P(FadeIn(gloss), rt=0.6)
        self.at(0.62)
        self.add(dot)
        self.P(MoveAlongPath(dot, path), rt=1.6)
        self.P(MoveAlongPath(dot, path), rt=1.6)
        self.P(FadeOut(dot), rt=0.3)
        self.end()


# --------------------------------------------------------------------------------------------
# B04: the policy is a small neural network: 25 numbers in, a probability for each of 11 actions out.
# The odds shown are an illustration, not a trained policy.
# --------------------------------------------------------------------------------------------
class B04_Policy(Scene):
    BID, DEFAULT = "B04", 13.0

    def construct(self):
        self.begin()
        hl = headline("The policy: numbers in, odds out", "The policy:", "numbers to odds")
        if PORTRAIT:
            x0, y0, x1, y1 = -SX + 0.15, 0.55, SX - 0.15, hl.get_bottom()[1] - 0.6
        else:
            x0, y0, x1, y1 = -SX + 0.7, -1.75, -0.4, hl.get_bottom()[1] - 0.95
        sizes = [25, 8, 8, 11]
        cols = []
        for i, n in enumerate(sizes):
            x = x0 + (x1 - x0) * i / (len(sizes) - 1)
            pad = 0 if n == 25 else (y1 - y0) * 0.08
            cols.append([np.array([x, y, 0.0]) for y in np.linspace(y1 - pad, y0 + pad, n)])
        edges = VGroup(*[Line(a, b, stroke_color=GREY, stroke_width=1, stroke_opacity=0.6)
                         for c0, c1 in zip(cols, cols[1:]) for a in c0 for b in c1])
        nodes = VGroup(*[Dot(p, radius=0.045 if PORTRAIT else 0.06, color=[SLATE, INK, INK, TEAL][i])
                         for i, c in enumerate(cols) for p in c])
        labs = VGroup(T("25 numbers", 26, SLATE), T("hidden layers", 26, SLATE), T("11 actions", 26, SLATE))
        place(labs[0], left=x0 - 0.1, bottom=y1 + 0.12)   # input label above the input column
        place(labs[1], x=(cols[1][0][0] + cols[2][0][0]) / 2, top=y0 - 0.15)
        place(labs[2], right=min(x1 + 0.2, SX), top=labs[1].get_bottom()[1] - 0.08)
        if PORTRAIT:
            bx0, by0, bx1, by1 = -SX + 0.1, TEXT_FLOOR + 0.9, SX - 0.05, labs.get_bottom()[1] - 0.65
        else:
            bx0, by0, bx1, by1 = 0.55, -1.75, SX - 0.05, hl.get_bottom()[1] - 0.55
        box = Box(bx0, by0, bx1, by1, (-0.5, 10.5), (0, 0.30))
        bars = VGroup(*[box.column(i, 0, p, 0.62, TEAL if i == 7 else SLATE, 1) for i, p in enumerate(EXAMPLE_ODDS)])
        ticks = VGroup(*[place(T(lab, 26, TEAL if i == 7 else SLATE, weight="BOLD" if i == 7 else "NORMAL"),
                               x=box.p(i, 0)[0], top=by0 - 0.1) for i, lab in ((0, "-5"), (5, "0"), (7, "+2"), (10, "+5"))])
        base = Line(box.p(-0.5, 0), box.p(10.5, 0), stroke_color=INK, stroke_width=3)
        btitle = T("probability of each action" if not PORTRAIT else "odds per action", 28 if not PORTRAIT else 26, SLATE)
        place(btitle, left=bx0, bottom=by1 + 0.12)
        note = (stack("example odds, for illustration", "they add up to 1", size=26, color=SLATE, buff=0.04) if not PORTRAIT
                else T("illustration only", 26, SLATE))
        place(note, left=bx0, top=ticks.get_bottom()[1] - 0.12)
        picked = stack("picked: +2 servers", size=30, weight="BOLD", color=TEAL) if not PORTRAIT else VGroup()
        place(picked, right=bx1, top=by1 - 0.05)
        self.P(FadeIn(hl), Create(edges), FadeIn(nodes), FadeIn(labs), rt=1.6)
        flow = VGroup(*[e.copy().set_stroke(GOLD, 2.5, 1) for e in edges[::7]])
        self.P(LaggedStart(*[ShowPassingFlash(f, time_width=0.6) for f in flow], lag_ratio=0.01), rt=1.5)
        self.at(0.32)   # bars and note settle before Gate V's mid-beat sample
        self.P(FadeIn(btitle), Create(base), FadeIn(ticks), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.08), rt=1.6)
        self.P(FadeIn(note), rt=0.5)
        self.at(0.8)
        self.P(Indicate(bars[7], color=TEAL, scale_factor=1.08), FadeIn(picked), rt=0.8)
        self.end()


# --------------------------------------------------------------------------------------------
# B05: the training loop. Collect (n_steps = 2048 by default), advantage (against the critic), update.
# The bars are an illustration.
# --------------------------------------------------------------------------------------------
class B05_Loop(Scene):
    BID, DEFAULT = "B05", 16.0

    def construct(self):
        self.begin()
        hl = headline("Training repeats three steps", "The training loop")
        specs = [("1  Collect", f"{N_STEPS:,} steps", "with the policy" if not PORTRAIT else "by default"),
                 ("2  Advantage", "result minus", "the critic's guess"),
                 ("3  Update", "make good actions", "more likely")]
        w, h = (3.88, 1.25) if PORTRAIT else (3.9, 1.6)
        cards = VGroup()
        for t, a, b in specs:
            box = RoundedRectangle(width=w, height=h, corner_radius=0.15, stroke_color=GREY, stroke_width=4,
                                   fill_color=CREAM, fill_opacity=1)
            txt = VGroup(T(t, 28 if not PORTRAIT else 26, weight="BOLD"), T(a, 26), T(b, 26)).arrange(DOWN, buff=0.06 if not PORTRAIT else 0.03)
            cards.add(VGroup(box, txt.move_to(box)))
        if PORTRAIT:
            cards.arrange(DOWN, buff=0.18)
            place(cards, x=0, top=hl.get_bottom()[1] - 0.25)
            arrows = VGroup(*[Arrow(a.get_bottom(), b.get_top(), buff=0.04, stroke_color=INK, stroke_width=5, tip_length=0.14)
                              for a, b in zip(cards, cards[1:])])
            back = VGroup()
            top = cards.get_bottom()[1] - 0.3
        else:
            cards.arrange(RIGHT, buff=0.43)
            place(cards, x=0, top=hl.get_bottom()[1] - 0.4)
            arrows = VGroup(*[Arrow(a.get_right(), b.get_left(), buff=0.04, stroke_color=INK, stroke_width=6, tip_length=0.16)
                              for a, b in zip(cards, cards[1:])])
            back = CurvedArrow(cards[2].get_bottom() + DOWN * 0.08, cards[0].get_bottom() + DOWN * 0.08, angle=-TAU / 9,
                               stroke_color=GREY, stroke_width=4, tip_length=0.18)
            top = back.get_bottom()[1] - 0.35
        # step 2: the result against the critic's guess; the gap is the advantage (illustration)
        res = Rectangle(width=0.5, height=1.2, stroke_width=0, fill_color=TEAL, fill_opacity=1)
        guess = Rectangle(width=0.5, height=0.75, stroke_width=0, fill_color=GREY, fill_opacity=1)
        pair = VGroup(res, guess).arrange(RIGHT, buff=0.7, aligned_edge=DOWN)
        brace = BraceBetweenPoints(guess.get_corner(UR) + RIGHT * 0.12, guess.get_corner(UR) + RIGHT * 0.12 + UP * 0.45,
                                   direction=RIGHT, color=GOLD)
        two = VGroup(pair, brace)
        two_l = VGroup(T("result", 26, SLATE), T("guess", 26, SLATE), T("advantage", 26, INK, weight="BOLD"))
        # step 3: that action's probability before and after the update (illustration)
        p_old = Rectangle(width=0.5, height=0.6, stroke_width=0, fill_color=SLATE, fill_opacity=1)
        p_new = Rectangle(width=0.5, height=0.95, stroke_width=0, fill_color=TEAL, fill_opacity=1)
        three = VGroup(p_old, p_new).arrange(RIGHT, buff=0.9, aligned_edge=DOWN)
        three_l = VGroup(T("before", 26, SLATE), T("after", 26, SLATE))
        note = stack(f"{N_STEPS:,} steps: the Stable-Baselines3 default (n_steps)", "bars: illustration", size=26, color=SLATE,
                     buff=0.04)   # two lines, so the footnote stays clear of the corner mark
        crit = T("critic: a second network that guesses the reward to come", 26, SLATE)
        if PORTRAIT:
            minis = [VGroup(), VGroup(), VGroup()]
            note = VGroup()
            crit = stack("critic: a second", "network's guess", size=26, color=SLATE, buff=0.03)
            place(crit, left=-SX, top=top)
        else:
            place(two, x=cards[1].get_center()[0] - 0.3, top=top)
            place(two_l[0], x=res.get_center()[0], top=pair.get_bottom()[1] - 0.1)
            place(two_l[1], x=guess.get_center()[0], top=pair.get_bottom()[1] - 0.1)
            place(two_l[2], left=brace.get_right()[0] + 0.1, y=brace.get_center()[1])
            place(three, x=cards[2].get_center()[0], top=top + 0.25 - 0.25)
            three.align_to(pair, DOWN)
            place(three_l[0], x=p_old.get_center()[0], top=three.get_bottom()[1] - 0.1)
            place(three_l[1], x=p_new.get_center()[0], top=three.get_bottom()[1] - 0.1)
            place(note, left=-SX, bottom=-SY)
            place(crit, left=-SX, bottom=note.get_top()[1] + 0.12)
            minis = [VGroup(), VGroup(two, two_l), VGroup(three, three_l)]
        self.P(FadeIn(hl), FadeIn(cards), FadeIn(arrows), FadeIn(back), rt=0.7)
        extras = [[FadeIn(note)], [FadeIn(crit)], []]
        for k, frac in enumerate((0.05, 0.36, 0.8)):
            self.at(frac)
            self.P(cards[k][0].animate.set_stroke(TEAL, 7), *[FadeIn(m) for m in minis[k]], *extras[k], rt=0.8)
        self.end()


# --------------------------------------------------------------------------------------------
# B06: proximal = close by. The new/old probability ratio, and the band 0.8 to 1.2 (clip_range 0.2).
# The example probabilities (0.20 -> 0.30) are an illustration.
# --------------------------------------------------------------------------------------------
class B06_Proximal(Scene):
    BID, DEFAULT = "B06", 15.0

    def construct(self):
        self.begin()
        hl = headline("Proximal: stay close to the old policy", "Proximal: stay", "close by")
        old = T("old probability  0.20", 30 if not PORTRAIT else 28)
        new = T("new probability  0.30", 30 if not PORTRAIT else 28)
        ratio = math(r"r=\frac{0.30}{0.20}=1.5", 1.1 if not PORTRAIT else 0.8)
        ex = T("one example action, for illustration" if not PORTRAIT else "made-up example", 26, SLATE)
        lo, hi = 1 - CLIP, 1 + CLIP
        if PORTRAIT:
            old = T("old 0.20, new 0.30", 28)
            new = VGroup()
            left = VGroup(ex, old, ratio).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            place(left, left=-SX, top=hl.get_bottom()[1] - 0.22)
            lx0, lx1, ly = -SX + 0.2, SX - 0.2, ratio.get_bottom()[1] - 0.78
        else:
            left = VGroup(ex, old, new).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            place(left, left=-SX, top=hl.get_bottom()[1] - 0.35)
            place(ratio, left=2.0, y=VGroup(old, new).get_center()[1])
            lx0, lx1, ly = -SX + 0.4, SX - 0.4, -0.85
        nl = Box(lx0, ly, lx1, ly + 1, (0.4, 1.6), (0, 1))
        axis = Line(nl.p(0.4, 0), nl.p(1.6, 0), stroke_color=INK, stroke_width=4)
        band = Rectangle(width=nl.p(hi, 0)[0] - nl.p(lo, 0)[0], height=0.36, stroke_width=0, fill_color=GOLD, fill_opacity=0.4)
        band.move_to([(nl.p(lo, 0)[0] + nl.p(hi, 0)[0]) / 2, ly, 0])
        ticks = VGroup()
        for v in (0.5, lo, 1.0, hi, 1.5):
            ticks.add(Line(nl.p(v, 0) + DOWN * 0.1, nl.p(v, 0) + UP * 0.1, stroke_color=INK, stroke_width=3))
            ticks.add(place(T(f"{v:.1f}", 28 if not PORTRAIT else 26, SLATE), x=nl.p(v, 0)[0], top=ly - 0.28))
        raw = Triangle(fill_color=SLATE, fill_opacity=1, stroke_width=0).scale(0.14).rotate(PI).move_to(nl.p(1.0, 0) + UP * 0.42)
        rawlab = T("the ratio", 26, SLATE)
        if PORTRAIT:
            rawlab.add_updater(lambda m: place(m, y=raw.get_center()[1], right=raw.get_left()[0] - 0.12))   # pointer moves 1.0 to 1.5 only
        else:
            rawlab.add_updater(lambda m: place(place(m, x=raw.get_center()[0], bottom=raw.get_top()[1] + 0.1),
                                               right=min(m.get_right()[0], SX)))
        kept = Dot(nl.p(1.0, 0), radius=0.13, color=TEAL)
        keptlab = T("what PPO counts", 26, TEAL, weight="BOLD")
        keptlab.add_updater(lambda m: place(place(m, x=kept.get_center()[0], top=ly - (0.72 if not PORTRAIT else 0.62)),
                                            right=min(m.get_right()[0], SX)))
        bandlab = T(f"allowed band: {lo:.1f} to {hi:.1f}  (clip range {CLIP})", 28 if not PORTRAIT else 26)
        if PORTRAIT:
            bandlab = VGroup()   # the shaded band and its 0.8 / 1.2 ticks carry this in 9:16
        place(bandlab, left=-SX, top=ly - 1.2 if not PORTRAIT else ly - 1.12)
        moral = (stack("PPO limits how far a single update", "can move the policy.", size=32, weight="BOLD", buff=0.05)
                 if not PORTRAIT else
                 stack("PPO limits how far", "a single update can", "move the policy.", size=26, weight="BOLD", buff=0.04))
        if PORTRAIT:
            place(moral, left=-SX, top=ly - 1.05)
        else:
            place(moral, left=-SX, bottom=-SY)
        self.P(FadeIn(hl), FadeIn(ex), FadeIn(old), rt=0.6)
        self.at(0.18)
        self.P(FadeIn(new), rt=0.5)
        self.P(Write(ratio), rt=1.0)
        self.at(0.42)
        self.P(Create(axis), FadeIn(ticks), FadeIn(band), FadeIn(bandlab), FadeIn(raw), FadeIn(rawlab),
               FadeIn(kept), FadeIn(keptlab), rt=1.0)
        self.at(0.62)
        self.P(raw.animate.move_to(nl.p(1.5, 0) + UP * 0.42), kept.animate.move_to(nl.p(hi, 0)), rt=1.5)
        rawlab.clear_updaters()
        keptlab.clear_updaters()
        self.at(0.82)
        self.P(FadeIn(moral, shift=UP * 0.1), rt=0.6)
        self.end()


# --------------------------------------------------------------------------------------------
# B07: the clipped objective (Schulman et al. 2017, eq. 7), typeset; it matches PPO.train in
# stable-baselines3 2.9.2 (min of ratio*A and clamp(ratio, 1-0.2, 1+0.2)*A, averaged over the batch).
# --------------------------------------------------------------------------------------------
class B07_Rule(Scene):
    BID, DEFAULT = "B07", 14.0

    def construct(self):
        self.begin()
        hl = headline("The rule, as math", "The rule, as math")
        if PORTRAIT:
            # two left-aligned lines at 0.78: 'min' glyphs clear GATE T's 72 px floor at 3840, clip line fits the width
            l1 = MathTex(r"L=\mathbb{E}\Big[\min\big(", r"r\,A", r",", color=INK).scale(0.78)
            l2 = MathTex(r"\operatorname{clip}(r,\,1-\epsilon,\,1+\epsilon)\,A", r"\big)\Big]", color=INK).scale(0.78)
            obj = VGroup(l1, l2).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            terms = (l1[1], l2[0])
        else:
            obj = MathTex(r"L=\mathbb{E}\Big[\min\big(", r"r\,A", r",\;", r"\operatorname{clip}(r,\,1-\epsilon,\,1+\epsilon)\,A",
                          r"\big)\Big]", color=INK).scale(1.25)
            terms = (obj[1], obj[3])
        rdef = MathTex(r"r=\frac{\pi_{\text{new}}(a\mid s)}{\pi_{\text{old}}(a\mid s)}", color=INK).scale(1.08 if PORTRAIT else 1.2)   # subscript "new" clears GATE T's 72 px floor at 3840
        entries = [(r"r", "new over old probability"), (r"A", "advantage (from the critic)"),
                   (r"\epsilon", f"{CLIP}: r is clipped to {1 - CLIP:.1f} to {1 + CLIP:.1f}"), (r"\mathbb{E}", "average over the batch")]
        if PORTRAIT:   # r is defined by the fraction just above it
            entries = [(r"A", "advantage"), (r"\epsilon", f"clip range {CLIP}"), (r"\mathbb{E}", "batch average")]
        gloss = VGroup()
        for sym, words in entries:
            s = MathTex(sym, color=INK).scale(0.9 if not PORTRAIT else 0.75)
            gloss.add(VGroup(s, T(words, 28 if not PORTRAIT else 26)))
        for row in gloss:
            row[1].next_to(row[0], RIGHT, buff=0.3)
            row[1].shift(RIGHT * (0.45 - row[0].width))
        gloss.arrange(DOWN, buff=0.14 if not PORTRAIT else 0.08, aligned_edge=LEFT)
        passes = T(f"each batch is reused for {N_EPOCHS} passes (n_epochs = {N_EPOCHS})", 28) if not PORTRAIT else \
            T(f"{N_EPOCHS} passes per batch", 26)
        src = Group(logo("openai", 0.42), T("Schulman et al. 2017, arXiv:1707.06347", 26, SLATE)).arrange(RIGHT, buff=0.15)
        if PORTRAIT:
            src = Group(logo("openai", 0.36), stack("Schulman et al.", "2017", size=26, color=SLATE, buff=0.03)).arrange(RIGHT, buff=0.15)
        if PORTRAIT:
            column([obj, rdef, gloss, passes, src], hl.get_bottom()[1] - 0.14, TEXT_FLOOR, left=-SX, min_gap=0.08)
        else:
            place(obj, left=-SX, top=hl.get_bottom()[1] - 0.45)
            place(rdef, left=-SX, top=obj.get_bottom()[1] - 0.5)
            place(gloss, left=rdef.get_right()[0] + 0.9, top=obj.get_bottom()[1] - 0.45)
            place(passes, left=-SX, top=gloss.get_bottom()[1] - 0.45)
            place(src, left=-SX, bottom=-SY)
        hi1 = SurroundingRectangle(terms[0], buff=0.08, stroke_color=TEAL, stroke_width=5)
        hi2 = SurroundingRectangle(terms[1], buff=0.08, stroke_color=TEAL, stroke_width=5)
        self.P(FadeIn(hl), Write(obj), rt=1.6)
        self.at(0.2)
        self.P(Write(rdef), FadeIn(gloss[0]), rt=1.0)
        self.at(0.36)
        self.P(*[FadeIn(g) for g in gloss[1:]], rt=0.8)
        self.at(0.52)
        self.P(Create(hi1), rt=0.5)
        self.at(0.66)
        self.P(ReplacementTransform(hi1, hi2), rt=0.6)
        self.at(0.8)
        self.P(FadeIn(passes), FadeIn(src), FadeOut(hi2), rt=0.7)
        self.end()


# --------------------------------------------------------------------------------------------
# B10: title restate. The full HAI mark, the title with a terracotta period, the handle, the repo.
# --------------------------------------------------------------------------------------------
class B10_Outro(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        D = beat_seconds("B10", 4.0)
        mark = hai_mark(1.1 if PORTRAIT else 1.7)
        lines = ("What PPO Is,", "In Plain", "Words.") if PORTRAIT else ("What PPO Is,", "In Plain Words.")
        title = VGroup(*[T(s, 52 if PORTRAIT else 100, INK, SERIF, t2c={".": TERRA}) for s in lines]).arrange(DOWN, buff=0.05)
        title.scale_to_fit_width(min(title.width, 2 * SX - 0.1))
        handle = T("@HumanitariansAI", 28 if PORTRAIT else 42, weight="BOLD")
        repo = (stack("github.com/", "lakshdhamija/", "rl-autoscaler", size=26, color=SLATE, buff=0.05, aligned=ORIGIN)
                if PORTRAIT else T("github.com/lakshdhamija/rl-autoscaler", 36, SLATE))
        g = VGroup(mark, title, handle, repo).arrange(DOWN, buff=0.28 if PORTRAIT else 0.4).move_to(ORIGIN)
        if PORTRAIT:
            place(g, top=SY - 0.2)
        rule = Line(LEFT, RIGHT, stroke_color=GOLD, stroke_width=8).set_width(min(title.width, 2 * SX))
        rule.move_to([0, (title.get_bottom()[1] + handle.get_top()[1]) / 2, 0])
        self.play(FadeIn(mark, shift=UP * 0.1), FadeIn(title), run_time=0.6)
        self.play(Create(rule), FadeIn(handle), FadeIn(repo), run_time=0.4)
        self.wait(max(D - 1.0, 0.1))
