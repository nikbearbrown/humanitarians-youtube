"""scenes.py — portrait (9:16) Manim scenes for hai-interview-end-to-end/short.
Full-length short (no beats cut): all 10 Manim beats re-laid-out for portrait —
B02, B06, B07, B08, B13, B18, B20, B21, B22, B23. Not shrunk copies of the
landscape scenes: the portrait frame is narrow in x (frame_width=4.5, Gate B safe
±1.95) and unchanged in y (frame_height=8.0, safe ±3.4), so every layout is
restacked vertically. The week strips become vertical blocks (height ∝ time) and
the hours chart turns horizontal, so both fill a tall frame.

DATA + TIMING come from the landscape ../scenes.py (imported, not copied): the
same stage/matrix/SQL/hours data, the same measured audio durations, the same
narration-cue placement. Scene classes must be declared as plain Scene subclasses
named B0X_Name — run.sh finds them by regex.
"""
from manim import *
from pathlib import Path
import importlib.util

# `manim -r 2160,3840` does NOT reset the coordinate frame to portrait — without
# these two lines every scene below renders in the 16:9 default space.
config.frame_width = 4.5
config.frame_height = 8.0

# Import the landscape module for data/timing. run.sh's Gate A/W pre-flights run an
# ISOLATED COPY of this file in a temp dir, so fall back to the reel's real location.
_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/data-analyst-interview-prep-week2-3-4/2026-08-10-data-analyst-interview-prep-end-to-end-part1")
_parent = Path(__file__).resolve().parent.parent / "scenes.py"
if not _parent.is_file() or not (_parent.parent / "beat_sheet.json").is_file():
    _parent = _REEL / "scenes.py"
_spec = importlib.util.spec_from_file_location("landscape_scenes", _parent)
L = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L)

H, SERIF, SANS, MONO = L.H, L.SERIF, L.SANS, L.MONO
STAGES, STAGE_CUES, SCORED = L.STAGES, L.STAGE_CUES, L.SCORED
SAFE_X = 1.95


def handle(scene):
    """Visible author handle, lower-right inside the portrait safe area."""
    h = Text("Supriya", font=SANS, color=H["INK"], font_size=18, weight="BOLD").set_opacity(0.75)
    h.move_to([SAFE_X - 0.05, -3.22, 0], aligned_edge=RIGHT)
    scene.add(h)
    return h


class Clock(L.Clock):
    """The landscape clock (same cues, same DUR) with the portrait handle."""

    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.DUR = L.dur(bid)
        scene.camera.background_color = H["CREAM"]
        handle(scene)


def fit(m, w):
    """Shrink (never grow) a mobject to width w."""
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def title(text, size=30, y=3.05):
    t = Text(text, font=SERIF, font_size=size, color=H["INK"], weight="BOLD")
    return fit(t, 3.8).move_to([0, y, 0])


def chip(label, color=H["SLATE"], text_color="#FFFFFF", width=1.85, height=0.62, font_size=18):
    box = RoundedRectangle(corner_radius=0.1, width=width, height=height, color=color,
                           fill_color=color, fill_opacity=1)
    txt = Text(label, font=SANS, font_size=font_size, color=text_color, weight="BOLD")
    fit(txt, width * 0.86).move_to(box)
    return VGroup(box, txt)


# ── Act I ─────────────────────────────────────────────────────────────────────

class B02_SixStageChips(Scene):
    def construct(self):
        c = Clock(self, "B02")
        head = title("The Loop, In Order")
        cells = VGroup()
        for i, s in enumerate(STAGES):
            box = RoundedRectangle(corner_radius=0.14, width=1.8, height=1.55, color=H["SLATE"],
                                   fill_color=H["SLATE"], fill_opacity=0.18, stroke_width=3)
            num = Text(str(i + 1), font=SANS, font_size=30, color=H["SLATE"], weight="BOLD")
            words = s.split(" ", 1) if s != "Hiring-Manager Chat" else ["Hiring-Manager", "Chat"]
            name = VGroup(*[Text(w, font=SANS, font_size=17, color=H["SLATE"], weight="BOLD")
                            for w in words]).arrange(DOWN, buff=0.06)
            fit(name, 1.6)
            VGroup(num, name).arrange(DOWN, buff=0.16).move_to(box)
            cells.add(VGroup(box, num, name))
        cells.arrange_in_grid(rows=3, cols=2, buff=(0.22, 0.28)).move_to([0, -0.25, 0])
        ring = RoundedRectangle(corner_radius=0.18, width=1.98, height=1.73, stroke_color=H["GOLD"],
                                stroke_width=7, fill_opacity=0).move_to(cells[0])
        c.run(FadeIn(head), FadeIn(cells), rt=0.6)
        for k, (cell, word) in enumerate(zip(cells, STAGE_CUES)):
            c.until(word)
            box, num, name = cell
            box.set_stroke(H["TEAL"])
            anims = [box.animate.set_fill(H["TEAL"], opacity=1),
                     num.animate.set_color("#FFFFFF"), name.animate.set_color("#FFFFFF")]
            anims.append(FadeIn(ring) if k == 0 else ring.animate.move_to(cell))
            c.run(*anims, rt=0.35)
            ring.move_to(cell)   # direct mutation: the ring's real resting place
        c.pad()


# ── Act II — the matrix, two lines per row ────────────────────────────────────

ROW_Y = [2.25, 1.32, 0.39, -0.54, -1.47, -2.4]
TEXT_X = -1.72


def matrix_row(i, lit):
    col_l = H["INK"] if lit else H["DIM"]
    col_r = H["TEAL"] if lit else H["DIM"]
    left = Text(STAGES[i], font=SERIF, font_size=24, color=col_l, weight="BOLD")
    right = Text(SCORED[i] if lit else "·  ·  ·", font=SANS, font_size=17, color=col_r)
    fit(left, 3.6)
    fit(right, 3.6)
    left.move_to([TEXT_X, ROW_Y[i] + 0.17, 0], aligned_edge=LEFT)
    right.move_to([TEXT_X, ROW_Y[i] - 0.2, 0], aligned_edge=LEFT)
    return VGroup(left, right)


def matrix_beat(scene, bid, lit_before, new_rows, cues):
    c = Clock(scene, bid)
    scene.add(title("What's Really Scored", size=28))
    scene.add(Line([-1.9, 2.75, 0], [1.9, 2.75, 0], color=H["INK"], stroke_width=2).set_opacity(0.5))
    marker = Rectangle(width=0.07, height=0.72, stroke_width=0, fill_color=H["TEAL"], fill_opacity=1)
    marker.move_to([-1.88, ROW_Y[max(lit_before - 1, 0)], 0])
    scene.add(marker)
    rows = {i: matrix_row(i, i < lit_before) for i in range(6)}
    for r in rows.values():
        scene.add(r)
    for i, word in zip(new_rows, cues):
        c.until(word)
        lit = matrix_row(i, True)
        c.run(FadeOut(rows[i]), FadeIn(lit, shift=RIGHT * 0.1),
              marker.animate.move_to([-1.88, ROW_Y[i], 0]), rt=0.6)
        marker.move_to([-1.88, ROW_Y[i], 0])   # direct mutation: real resting place
        rows[i] = lit
    c.pad()


class B06_MatrixRows12(Scene):
    def construct(self):
        matrix_beat(self, "B06", 0, [0, 1], ["recruiter", "hiring"])


class B07_MatrixRows34(Scene):
    def construct(self):
        matrix_beat(self, "B07", 2, [2, 3], ["technical", "statistics"])


class B08_MatrixRows56(Scene):
    def construct(self):
        matrix_beat(self, "B08", 4, [4, 5], ["case", "behavioral"])


# ── Act III ───────────────────────────────────────────────────────────────────

# Same query as landscape, minus the long comment line (shown as a tag above the panel
# so the code stays legible in a 4.5-unit-wide frame).
SQL_LINES = L.SQL_LINES[1:]
BUG_LINE = L.BUG_LINE - 1


class B13_LineByLineCheck(Scene):
    def construct(self):
        c = Clock(self, "B13")
        head = title("Read It Line by Line", size=28)
        tag = Text("AI-generated · “top 5 cities by revenue”", font=SANS, font_size=16, color="#6B6357")
        fit(tag, 3.8).next_to(head, DOWN, buff=0.35)
        code = VGroup(*[Text(l, font=MONO, font_size=22, color=H["SLATE"]) for l in SQL_LINES])
        code.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        fit(code, 3.4)
        panel = RoundedRectangle(corner_radius=0.14, width=3.85, height=code.height + 0.9,
                                 color=H["SLATE"], fill_color="#FFFFFF", fill_opacity=1, stroke_width=3)
        code.move_to(panel)
        block = VGroup(panel, code).next_to(tag, DOWN, buff=0.25)
        c.run(FadeIn(head), FadeIn(tag), FadeIn(block), rt=0.6)

        bar = Rectangle(width=panel.width - 0.2, height=0.5, stroke_width=0,
                        fill_color=H["GOLD"], fill_opacity=0.3)
        bar.move_to([0, code[0].get_center()[1], 0])
        c.until("read")
        c.run(FadeIn(bar), rt=0.3)
        for line in code[1:BUG_LINE + 1]:
            c.run(bar.animate.move_to([0, line.get_center()[1], 0]), rt=0.4)
        c.until("wrong")
        c.run(bar.animate.set_fill(H["CRIMSON"], opacity=0.3), rt=0.3)
        flag = VGroup(
            Text("ORDER BY is ascending:", font=SANS, font_size=22, color=H["CRIMSON"], weight="BOLD"),
            Text("this returns the BOTTOM 5", font=SANS, font_size=22, color=H["CRIMSON"], weight="BOLD"),
        ).arrange(DOWN, buff=0.12)
        fit(flag, 3.8).next_to(panel, DOWN, buff=0.4)
        c.run(FadeIn(flag, shift=UP * 0.15), rt=0.4)
        c.pad()


# ── Act IV — Maya's plan ──────────────────────────────────────────────────────

class B18_MayaProfile(Scene):
    def construct(self):
        c = Clock(self, "B18")
        head = title("Meet Maya")
        bio = VGroup(*[chip(l) for l in ["Econ degree", "2 stats courses", "1 DB course", "Bootcamp"]])
        bio.arrange_in_grid(rows=2, cols=2, buff=(0.16, 0.16)).next_to(head, DOWN, buff=0.3)
        clock_chip = chip("Interviews in 3 weeks", color=H["CRIMSON"], width=3.88, height=0.62, font_size=20)
        clock_chip.next_to(bio, DOWN, buff=0.18)
        c.run(FadeIn(head), rt=0.4)
        c.until("economics")
        c.run(LaggedStart(*[FadeIn(b, shift=UP * 0.15) for b in bio], lag_ratio=0.25), rt=1.0)
        c.until("interviews")
        c.run(FadeIn(clock_chip, scale=0.9), rt=0.4)

        def column(heading, items, color):
            h = Text(heading, font=SANS, font_size=22, color=color, weight="BOLD")
            rows = VGroup(*[Text(t, font=SERIF, font_size=24, color=H["INK"]) for t in items])
            rows.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
            g = VGroup(h, rows).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
            fit(g, 3.4)
            box = RoundedRectangle(corner_radius=0.12, width=3.88, height=g.height + 0.36,
                                   stroke_color=color, stroke_width=4, fill_opacity=0)
            g.move_to(box).align_to(box, LEFT).shift(RIGHT * 0.22)
            return VGroup(box, g)

        can = column("CAN", ["write a SELECT … JOIN", "build a pivot table"], H["TEAL"])
        never = column("NEVER DONE", ["a take-home case", "a behavioral story that landed"], H["CRIMSON"])
        VGroup(can, never).arrange(DOWN, buff=0.2).next_to(clock_chip, DOWN, buff=0.25)
        c.until("she can")
        c.run(FadeIn(can, shift=UP * 0.15), rt=0.5)
        c.until("never")
        c.run(FadeIn(never, shift=UP * 0.15), rt=0.5)
        c.pad()


def week_tabs(active):
    tabs = VGroup()
    for i, n in enumerate(L.WEEK_NAMES):
        on = i == active
        box = RoundedRectangle(corner_radius=0.1, width=1.22, height=0.55, stroke_width=3,
                               color=H["TEAL"] if on else H["DIM"],
                               fill_color=H["TEAL"] if on else H["CREAM"], fill_opacity=1)
        t = Text(n, font=SANS, font_size=18, weight="BOLD", color="#FFFFFF" if on else H["DIM"])
        tabs.add(VGroup(box, fit(t, 1.05).move_to(box)))
    return tabs.arrange(RIGHT, buff=0.12).move_to([0, 3.05, 0])


def week_blocks(blocks, top, width=3.88, total_h=4.6, x=0.0):
    """Vertical stack: block height ∝ share of the week's time."""
    stack = VGroup()
    for label, sub, ratio, color in blocks:
        hgt = max(total_h * ratio, 0.62)
        r = RoundedRectangle(corner_radius=0.12, width=width, height=hgt - 0.1, color=color,
                             fill_color=color, fill_opacity=0.92)
        lines = [Text(label, font=SANS, font_size=26, color="#FFFFFF", weight="BOLD")]
        if sub:
            lines.append(Text(sub, font=SERIF, font_size=20, color="#FFFFFF"))
        t = VGroup(*lines).arrange(DOWN, buff=0.1)
        fit(t, width - 0.4)
        if t.height > hgt - 0.25:
            t.scale_to_fit_height(hgt - 0.25)
        stack.add(VGroup(r, t.move_to(r)))
    stack.arrange(DOWN, buff=0.0).next_to(top, DOWN, buff=0.35)
    stack.set_x(x)
    return stack


def week_beat(scene, bid, active, heading, blocks, cues, **kw):
    c = Clock(scene, bid)
    tabs = week_tabs(active)
    head = Text(heading, font=SERIF, font_size=26, color=H["INK"], weight="BOLD", slant="ITALIC")
    fit(head, 3.8).next_to(tabs, DOWN, buff=0.3)
    stack = week_blocks(blocks, head, **kw)
    c.run(FadeIn(tabs), FadeIn(head), rt=0.4)
    for b, word in zip(stack, cues):
        c.until(word)
        c.run(FadeIn(b, shift=UP * 0.15), rt=0.4)
    return c, stack


class B20_Week1Block(Scene):
    def construct(self):
        # Ch.1: the 90 minutes a day is SQL's; statistics is "plus" (see ../scenes.py).
        c, _ = week_beat(self, "B20", 0, "the technical floor", [
            ("SQL", "90 min a day", 0.64, H["TEAL"]),
            ("+ Statistics", "half-remembered", 0.36, H["SLATE"]),
        ], ["sql", "plus"])
        c.pad()


class B21_Week2Block(Scene):
    def construct(self):
        c, _ = week_beat(self, "B21", 1, "what she's never done", [
            ("Sheets · pandas", "upkeep", 0.2, H["DIM"]),
            ("Case round", "+ one full take-home", 0.8, H["TEAL"]),
        ], ["week", "case"])
        c.pad()


class B22_Week3Block(Scene):
    def construct(self):
        c, stack = week_beat(self, "B22", 2, "integrate and rehearse", [
            ("Behavioral", "stories", 0.26, H["SLATE"]),
            ("Mock loop ×2", "full loop, self-scored", 0.46, H["TEAL"]),
            ("Re-drill", "her 2 weakest", 0.28, H["CRIMSON"]),
        ], ["behavioral", "mock", "re-drilling"], width=3.4, x=-0.24)
        arrow = CurvedArrow(stack[2].get_right() + RIGHT * 0.06, stack[1].get_right() + RIGHT * 0.06,
                            color=H["CRIMSON"], stroke_width=6, angle=TAU / 4)
        c.run(Create(arrow), rt=0.5)
        c.pad()


class B23_LopsidedHours(Scene):
    def construct(self):
        c = Clock(self, "B23")
        head = VGroup(Text("Prep hours by stage", font=SERIF, font_size=28, color=H["INK"], weight="BOLD"),
                      Text("illustrative, not a book figure", font=SERIF, font_size=20, color=H["INK"],
                           slant="ITALIC")).arrange(DOWN, buff=0.12)
        fit(head, 3.8).move_to([0, 2.95, 0])
        top, step, x0, max_len = 1.25, 0.8, -0.45, 2.3
        hmax = max(h for _, h in L.HOURS)
        bars, labels = VGroup(), VGroup()
        for i, (name, h) in enumerate(L.HOURS):
            y = top - i * step
            col = H["TEAL"] if h >= 4 else H["SLATE"]
            ln = max_len * h / hmax
            r = Rectangle(width=ln, height=0.52, stroke_width=0, fill_color=col, fill_opacity=1)
            r.move_to([x0 + ln / 2, y, 0])
            bars.add(r)
            lab = Text(name, font=SANS, font_size=18, color=H["INK"], weight="BOLD")
            labels.add(fit(lab, 1.25).move_to([x0 - 0.12, y, 0], aligned_edge=RIGHT))
        axis = Line([x0, top + 0.34, 0], [x0, top - 5 * step - 0.34, 0], color=H["INK"], stroke_width=3)
        c.run(FadeIn(head), Create(axis), FadeIn(labels), rt=0.5)
        c.run(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.15), rt=1.4)
        pill = chip("lopsided on purpose", color=H["GOLD"], text_color=H["INK"], width=3.4,
                    height=0.6, font_size=22).move_to([0, 2.12, 0])
        c.until("weakest")
        c.run(FadeIn(pill, scale=0.9), rt=0.4)
        c.pad()
