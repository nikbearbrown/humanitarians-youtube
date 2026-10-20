"""
Manim scenes for hai-interview-end-to-end (Chapter 1 map + 2026 shifts + worked plan) — v2.
One Scene per GRAPHIC-lane beat named in beat_sheet.json's graphic.manim field.
Humanitarians palette (matches runtime/remotion/src/tokens/humanitarians.ts).
Scene classes must be declared as plain Scene subclasses named B0X_Name — run.sh finds them by regex.
No LaTeX (Text/Pango only).

v2 (2026-10-15): re-timed to the v2 narration, re-laid-out to fill the frame, and
every scene carries the "Supriya" corner handle (PM requirement 4 / LOGO LAW) — see
`handle()`. The matrix (B06–B08) shows all six rows from frame 0 as dim placeholders
and lights each row on its spoken cue, so the table's shape is visible while it builds.

TIMING: DUR is read from beat_sheet.json — `actual_duration_s` once audio exists,
`estimated_duration_s` before. Narration cues are placed by the cue phrase's word
position in that beat's narration_text, scaled to DUR, so regenerated audio
re-times the scenes without hand edits. Never hand-trim an mp4.
"""

from manim import *
from pathlib import Path
import json

# run.sh's Gate A/W pre-flights execute an ISOLATED COPY of scenes.py in a temp dir,
# so fall back to the reel's real location for the beat sheet.
_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/data-analyst-interview-prep-week2-3-4/2026-08-10-data-analyst-interview-prep-end-to-end-part1")
HERE = Path(__file__).resolve().parent
if not (HERE / "beat_sheet.json").is_file():
    HERE = _REEL

H = {
    "CREAM": "#F3EBDD",
    "INK": "#2F2A26",
    "TEAL": "#1F4E5F",
    "CRIMSON": "#E4572E",
    "SLATE": "#29335C",
    "GOLD": "#F3A712",
    "DIM": "#B9B2A6",
}

SERIF = "EB Garamond"
SANS = "Montserrat"
MONO = "PT Mono"

# ── timing: from the beat sheet ───────────────────────────────────────────────

BEATS = {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}


def dur(bid):
    b = BEATS[bid]
    return float(b.get("actual_duration_s") or b["estimated_duration_s"])


def _norm(w):
    return w.strip(".,:;!?\"'").lower()


def cue(bid, phrase):
    """Seconds into the beat where `phrase` starts, by word position in the narration."""
    words = BEATS[bid]["narration_text"].split()
    target = phrase.split()
    for i in range(len(words) - len(target) + 1):
        if [_norm(w) for w in words[i:i + len(target)]] == [_norm(t) for t in target]:
            return dur(bid) * i / len(words)
    raise ValueError(f"{bid}: cue phrase not in narration: {phrase!r}")


def handle(scene):
    """Visible author handle, lower-right inside the safe area, on from frame 0."""
    h = Text("Supriya", font=SANS, color=H["INK"], font_size=26, weight="BOLD").set_opacity(0.75)
    h.to_corner(DR, buff=0.9)
    scene.add(h)
    return h


class Clock:
    """A beat's running clock. Scenes stay plain `(Scene)` subclasses and open with
    `c = Clock(self, "B0X")`. `until(phrase)` waits to that cue; `pad()` holds to
    the end of the beat's audio."""

    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.DUR = dur(bid)
        scene.camera.background_color = H["CREAM"]
        handle(scene)

    def run(self, *anims, rt=0.6):
        self.s.play(*anims, run_time=rt)
        self.t += rt

    def until(self, phrase):
        at = cue(self.bid, phrase)
        if at > self.t:
            self.s.wait(at - self.t)
            self.t = at

    def pad(self):
        self.s.wait(max(0.4, self.DUR - self.t - 0.2))


# ── shared visuals ────────────────────────────────────────────────────────────

def chip(label, color=H["SLATE"], text_color="#FFFFFF", width=3.4, height=0.9, font_size=26):
    box = RoundedRectangle(corner_radius=0.14, width=width, height=height, color=color,
                           fill_color=color, fill_opacity=1)
    txt = Text(label, font=SANS, font_size=font_size, color=text_color, weight="BOLD")
    txt.scale_to_fit_width(min(txt.width, width * 0.86))
    return VGroup(box, txt)


def title(text, size=44):
    return Text(text, font=SERIF, font_size=size, color=H["INK"], weight="BOLD").to_edge(UP, buff=0.7)


# ── Act I ─────────────────────────────────────────────────────────────────────

STAGES = ["Recruiter Screen", "Hiring-Manager Chat", "Technical Screen",
          "Statistics Round", "Case Round", "Behavioral Round"]
# last cue is "and" (one word early): "behavioral" is the final word, so cueing on it
# left the sixth cell lit for only ~0.5s before the cut.
STAGE_CUES = ["recruiter", "hiring-manager", "technical", "statistics", "case", "and"]


class B02_SixStageChips(Scene):
    def construct(self):
        c = Clock(self, "B02")
        head = title("The Loop, In Order")
        cells = VGroup()
        for i, s in enumerate(STAGES):
            box = RoundedRectangle(corner_radius=0.18, width=3.75, height=2.05, color=H["SLATE"],
                                   fill_color=H["SLATE"], fill_opacity=0.18, stroke_width=3)
            num = Text(str(i + 1), font=SANS, font_size=40, color=H["SLATE"], weight="BOLD")
            name = Text(s, font=SANS, font_size=30, color=H["SLATE"], weight="BOLD")
            name.scale_to_fit_width(min(name.width, 3.3))
            VGroup(num, name).arrange(DOWN, buff=0.22).move_to(box)
            cells.add(VGroup(box, num, name))
        cells.arrange_in_grid(rows=2, cols=3, buff=(0.4, 0.5)).next_to(head, DOWN, buff=0.5)
        # GOLD ring steps to each stage as it's named.
        ring = RoundedRectangle(corner_radius=0.24, width=4.0, height=2.3, stroke_color=H["GOLD"],
                                stroke_width=8, fill_opacity=0).move_to(cells[0])
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


# ── Act II — the matrix, built across three beats ─────────────────────────────

SCORED = [
    "Fit, communication, logistics",
    "Relevant experience, motivation",
    "Correct SQL/Python + explain your logic",
    "Sound reasoning, assumptions out loud",
    "Framing + a defensible recommendation",
    "Collaboration, ownership, ambiguity",
]
ROW_Y = [2.05, 1.17, 0.29, -0.59, -1.47, -2.35]
LEFT_X, RIGHT_X = -5.85, -1.05


def matrix_row(i, lit):
    """One row of the what's-tested-where table; lit=False → dim placeholder."""
    col_l = H["INK"] if lit else H["DIM"]
    col_r = H["TEAL"] if lit else H["DIM"]
    left = Text(STAGES[i], font=SERIF, font_size=38, color=col_l, weight="BOLD")
    left.scale_to_fit_width(min(left.width, 4.2))
    left.move_to([LEFT_X, ROW_Y[i], 0], aligned_edge=LEFT)
    right = Text(SCORED[i] if lit else "·  ·  ·", font=SANS, font_size=32, color=col_r)
    right.scale_to_fit_width(min(right.width, 7.05))
    right.move_to([RIGHT_X, ROW_Y[i], 0], aligned_edge=LEFT)
    return VGroup(left, right)


def matrix_frame():
    head = title("What's Really Scored", size=42)
    rule = Line([LEFT_X, 2.6, 0], [6.0, 2.6, 0], color=H["INK"], stroke_width=2).set_opacity(0.5)
    divider = Line([RIGHT_X - 0.35, 2.45, 0], [RIGHT_X - 0.35, -2.75, 0], color=H["INK"],
                   stroke_width=2).set_opacity(0.25)
    return VGroup(head, rule, divider)


def matrix_beat(scene, bid, lit_before, new_rows, cues):
    c = Clock(scene, bid)
    scene.add(matrix_frame())
    # TEAL row marker: slides to each row as it lights, so the eye tracks the build.
    marker = Rectangle(width=0.14, height=0.7, stroke_width=0, fill_color=H["TEAL"], fill_opacity=1)
    marker.move_to([LEFT_X - 0.35, ROW_Y[max(lit_before - 1, 0)], 0])
    scene.add(marker)
    rows = {i: matrix_row(i, i < lit_before) for i in range(6)}
    for r in rows.values():
        scene.add(r)
    for i, word in zip(new_rows, cues):
        c.until(word)
        lit = matrix_row(i, True)
        c.run(FadeOut(rows[i]), FadeIn(lit, shift=RIGHT * 0.15),
              marker.animate.move_to([LEFT_X - 0.35, ROW_Y[i], 0]), rt=0.6)
        marker.move_to([LEFT_X - 0.35, ROW_Y[i], 0])   # direct mutation: real resting place
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

# Generic illustration (Ch.1/Ch.7 theme), not a claim about any real tool's output:
# asked for the TOP 5 cities, the query sorts ascending — so LIMIT 5 returns the bottom 5.
SQL_LINES = [
    "-- top 5 cities by revenue (AI-generated)",
    "SELECT city, SUM(revenue) AS rev",
    "FROM orders",
    "WHERE status = 'paid'",
    "GROUP BY city",
    "ORDER BY rev",
    "LIMIT 5;",
]
BUG_LINE = 5


class B13_LineByLineCheck(Scene):
    def construct(self):
        c = Clock(self, "B13")
        head = title("Read It Line by Line", size=42)
        code = VGroup(*[Text(l, font=MONO, font_size=34,
                             color=H["SLATE"] if i else "#6B6357") for i, l in enumerate(SQL_LINES)])
        code.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        code.scale_to_fit_width(8.4)
        panel = RoundedRectangle(corner_radius=0.2, width=code.width + 1.2, height=code.height + 0.9,
                                 color=H["SLATE"], fill_color="#FFFFFF", fill_opacity=1, stroke_width=3)
        block = VGroup(panel, code)
        code.move_to(panel)
        block.next_to(head, DOWN, buff=0.45)
        c.run(FadeIn(head), FadeIn(block), rt=0.6)

        bar = Rectangle(width=panel.width - 0.3, height=0.62, stroke_width=0,
                        fill_color=H["GOLD"], fill_opacity=0.3)
        bar.move_to([panel.get_center()[0], code[1].get_center()[1], 0])
        c.until("read")
        c.run(FadeIn(bar), rt=0.3)
        for line in code[2:BUG_LINE + 1]:
            c.run(bar.animate.move_to([bar.get_center()[0], line.get_center()[1], 0]), rt=0.4)
        c.until("wrong")
        c.run(bar.animate.set_fill(H["CRIMSON"], opacity=0.3), rt=0.3)
        flag = Text("ORDER BY is ascending: this returns the BOTTOM 5", font=SANS, font_size=36,
                    color=H["CRIMSON"], weight="BOLD")
        flag.scale_to_fit_width(min(flag.width, 9.6))
        flag.next_to(panel, DOWN, buff=0.35)
        c.run(FadeIn(flag, shift=UP * 0.2), rt=0.4)
        c.pad()


# ── Act IV — Maya's plan ──────────────────────────────────────────────────────

class B18_MayaProfile(Scene):
    def construct(self):
        c = Clock(self, "B18")
        head = title("Meet Maya")
        bio = VGroup(*[chip(l, width=2.85, height=1.0, font_size=28)
                       for l in ["Econ degree", "2 stats courses", "1 DB course", "Bootcamp"]])
        bio.arrange(RIGHT, buff=0.28).next_to(head, DOWN, buff=0.5)
        clock_chip = chip("Interviews in 3 weeks", color=H["CRIMSON"], width=6.0, height=0.95, font_size=30)
        clock_chip.next_to(bio, DOWN, buff=0.35)
        c.run(FadeIn(head), rt=0.4)
        c.until("economics")
        c.run(LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in bio], lag_ratio=0.25), rt=1.0)
        c.until("interviews")
        c.run(FadeIn(clock_chip, scale=0.9), rt=0.4)

        def column(heading, items, color):
            h = Text(heading, font=SANS, font_size=34, color=color, weight="BOLD")
            rows = VGroup(*[Text(t, font=SERIF, font_size=36, color=H["INK"]) for t in items])
            rows.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
            g = VGroup(h, rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            box = SurroundingRectangle(g, color=color, buff=0.35, corner_radius=0.15, stroke_width=4)
            return VGroup(box, g)

        can = column("CAN", ["write a SELECT … JOIN", "build a pivot table"], H["TEAL"])
        never = column("NEVER DONE", ["a take-home case", "a behavioral story that landed"], H["CRIMSON"])
        cols = VGroup(can, never).arrange(RIGHT, buff=0.6, aligned_edge=UP)
        cols.scale_to_fit_width(min(cols.width, 12.4)).next_to(clock_chip, DOWN, buff=0.45)
        c.until("she can")
        c.run(FadeIn(can, shift=UP * 0.2), rt=0.5)
        c.until("never")
        c.run(FadeIn(never, shift=UP * 0.2), rt=0.5)
        c.pad()


WEEK_NAMES = ["Week 1", "Week 2", "Week 3"]


def week_tabs(active):
    tabs = VGroup()
    for i, n in enumerate(WEEK_NAMES):
        on = i == active
        box = RoundedRectangle(corner_radius=0.14, width=3.2, height=0.85, stroke_width=3,
                               color=H["TEAL"] if on else H["DIM"],
                               fill_color=H["TEAL"] if on else H["CREAM"], fill_opacity=1)
        t = Text(n, font=SANS, font_size=30, weight="BOLD", color="#FFFFFF" if on else H["DIM"]).move_to(box)
        tabs.add(VGroup(box, t))
    return tabs.arrange(RIGHT, buff=0.35).to_edge(UP, buff=0.7)


def week_bars(blocks, top):
    """blocks: (label, sublabel, width_ratio, color). Bars span the frame width."""
    total_w = 12.6
    bars = VGroup()
    x = -total_w / 2
    for label, sub, ratio, color in blocks:
        w = total_w * ratio
        r = RoundedRectangle(corner_radius=0.16, width=w - 0.2, height=3.5, color=color,
                             fill_color=color, fill_opacity=0.92)
        r.move_to([x + w / 2, 0, 0])
        lines = [Text(label, font=SANS, font_size=40, color="#FFFFFF", weight="BOLD")]
        if sub:
            lines.append(Text(sub, font=SERIF, font_size=32, color="#FFFFFF"))
        t = VGroup(*lines).arrange(DOWN, buff=0.2)
        t.scale_to_fit_width(min(t.width, w - 0.6))
        t.move_to(r.get_center())
        bars.add(VGroup(r, t))
        x += w
    bars.next_to(top, DOWN, buff=0.7)
    return bars


def week_beat(scene, bid, active, heading, blocks, cues):
    c = Clock(scene, bid)
    tabs = week_tabs(active)
    head = Text(heading, font=SERIF, font_size=40, color=H["INK"], weight="BOLD", slant="ITALIC")
    head.next_to(tabs, DOWN, buff=0.4)
    bars = week_bars(blocks, head)
    c.run(FadeIn(tabs), FadeIn(head), rt=0.4)
    for b, word in zip(bars, cues):
        c.until(word)
        c.run(FadeIn(b, shift=UP * 0.2), rt=0.4)
    return c, bars


class B20_Week1Block(Scene):
    def construct(self):
        # Ch.1: "SQL I and II, 90 minutes a day, PLUS the statistics round" — the
        # 90 minutes is SQL's (v1 wrongly gave statistics 90 min/day too).
        c, _ = week_beat(self, "B20", 0, "the technical floor", [
            ("SQL", "90 min a day", 0.64, H["TEAL"]),
            ("+ Statistics", "half-remembered", 0.36, H["SLATE"]),
        ], ["sql", "plus"])
        c.pad()


class B21_Week2Block(Scene):
    def construct(self):
        c, _ = week_beat(self, "B21", 1, "what she's never done", [
            ("Sheets", "upkeep", 0.14, H["DIM"]),
            ("pandas", "upkeep", 0.14, H["DIM"]),
            ("Case round", "+ one full take-home", 0.72, H["TEAL"]),
        ], ["week", "week", "case"])
        c.pad()


class B22_Week3Block(Scene):
    def construct(self):
        c, bars = week_beat(self, "B22", 2, "integrate and rehearse", [
            ("Behavioral", "stories", 0.26, H["SLATE"]),
            ("Mock loop ×2", "full loop, self-scored", 0.46, H["TEAL"]),
            ("Re-drill", "her 2 weakest", 0.28, H["CRIMSON"]),
        ], ["behavioral", "mock", "re-drilling"])
        arrow = CurvedArrow(bars[2].get_bottom() + DOWN * 0.15, bars[1].get_bottom() + DOWN * 0.15,
                            color=H["CRIMSON"], stroke_width=6, angle=-TAU / 8)
        c.run(Create(arrow), rt=0.5)
        c.pad()


# Illustrative heights (v1 labeled them the same way): weight × gap, not a book figure.
HOURS = [("Recruiter", 1.0), ("HM chat", 1.4), ("Technical", 3.2),
         ("Statistics", 2.6), ("Case", 4.4), ("Behavioral", 4.0)]


class B23_LopsidedHours(Scene):
    def construct(self):
        c = Clock(self, "B23")
        head = Text("Prep hours by stage — illustrative, not a book figure", font=SERIF,
                    font_size=34, color=H["INK"], slant="ITALIC").to_edge(UP, buff=0.7)
        base_y = -2.15
        bars, labels = VGroup(), VGroup()
        for i, (name, h) in enumerate(HOURS):
            x = -5.1 + i * 2.04
            col = H["TEAL"] if h >= 4 else H["SLATE"]
            r = Rectangle(width=1.5, height=h, stroke_width=0, fill_color=col, fill_opacity=1)
            r.move_to([x, base_y + h / 2, 0])
            bars.add(r)
            labels.add(Text(name, font=SANS, font_size=25, color=H["INK"], weight="BOLD")
                       .move_to([x, base_y - 0.45, 0]))
        axis = Line([-6.1, base_y, 0], [6.1, base_y, 0], color=H["INK"], stroke_width=3)
        c.run(FadeIn(head), Create(axis), FadeIn(labels), rt=0.5)
        c.run(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.15), rt=1.4)
        pill = chip("lopsided on purpose", color=H["GOLD"], text_color=H["INK"], width=5.4,
                    height=0.85, font_size=32)
        pill.move_to([-3.2, 1.6, 0])
        c.until("weakest")
        c.run(FadeIn(pill, scale=0.9), rt=0.4)
        c.pad()
