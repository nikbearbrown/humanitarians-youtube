"""vox_scenes.py — Recency Beats Size: Why the Seed-Round Lab Outranks the
$220M Incumbent (vox-recency-size, slate cut, 16:9).

One Scene per GRAPHIC/CARD/COMPOSITE beat whose source is 'own'.
B02 is the only STILL (ai media slot) and has no scene here.
Durations read from beat_sheet.json (actuals after audio lock; estimates as fallback).

Color law:
  TEAL = recently-funded / small / high-signal / target zone
  CRIMSON = large / stale-raise / low-signal / wrong-ranking
  GOLD = fill highlight only, never text (used once: B07 target quadrant)

Exclusions: no SEC Form D filing mechanics, no seven-step pipeline, no
domain-inference percentage, no geography filter detail beyond one sentence.

Gate B: every zero-width stroke is also zero-opacity.
"""

import sys
import json
import pathlib

# Resolve the shared graphics library wherever this reel lives.
# parents[3] from this file goes up to books/; then into vox/aspects/.../manim.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403

_bs = str(pathlib.Path(__file__).resolve().parent / "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 11)}


# ── helpers ──────────────────────────────────────────────────────────────────

def _card(w, h, color=SLATE, alpha=0.10, stroke_color=None, stroke_w=2.0):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, alpha)
    sc = stroke_color if stroke_color else color
    r.set_stroke(sc, stroke_w)
    return r


def _bar(height, width=0.9, color=TEAL):
    b = Rectangle(width=width, height=height)
    b.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return b


# ── scenes ───────────────────────────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("Recency Beats Size", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        t2 = Text("Why the Seed-Round Lab Outranks the Incumbent", font=DISPLAY,
                  color=CRIMSON, font_size=20, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        # underline bar gives real shape motion (Create)
        q1 = Text("A larger raise should mean a stronger hiring signal.",
                  font=SERIF, color=INK, font_size=28)
        q2 = Text("Here is the case where the", font=SERIF, color=INK, font_size=28)
        q3 = Text("six-million-dollar company is the better target.",
                  font=SERIF, color=TEAL, font_size=28, weight=BOLD)
        q4 = Text("Why?", font=DISPLAY, color=CRIMSON, font_size=34, weight=BOLD)
        block = VGroup(q1, q2, q3, q4).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(q3.get_corner(DL) + DOWN * 0.12, q3.get_corner(DR) + DOWN * 0.12,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.8)
        self.play(FadeIn(q2), FadeIn(q3), run_time=0.7)
        self.play(Create(u), run_time=0.5)
        self.play(FadeIn(q4, scale=0.85), run_time=0.7)
        self.wait(max(0.3, total - 2.7))


class B04_NaiveRanking(Scene):
    """Two bars: MegaCloud (CRIMSON, tall) vs Helix Bio (TEAL, short).
    Sort by dollar amount — the naive ranking."""
    def construct(self):
        total = DUR["B04"]

        # bars
        mega_h, helix_h = 3.0, 0.9
        mega_bar = _bar(mega_h, 1.4, CRIMSON).move_to(LEFT * 1.8 + DOWN * (2.0 - mega_h / 2))
        helix_bar = _bar(helix_h, 1.4, TEAL).move_to(RIGHT * 1.8 + DOWN * (2.0 - helix_h / 2))

        baseline = Line(LEFT * 3.5 + DOWN * 2.0, RIGHT * 3.5 + DOWN * 2.0,
                        color=INK, stroke_width=2)

        mega_label = LabelChip("$220M", accent=CRIMSON, size=22)
        mega_label.next_to(mega_bar, UP, buff=0.18)
        helix_label = LabelChip("$6M", accent=TEAL, size=22)
        helix_label.next_to(helix_bar, UP, buff=0.18)

        mega_name = SerifLabel("MegaCloud", CRIMSON, size=22)
        mega_name.next_to(mega_bar, DOWN, buff=0.22)
        helix_name = SerifLabel("Helix Bio", TEAL, size=22)
        helix_name.next_to(helix_bar, DOWN, buff=0.22)

        rank_1 = Text("1", font=MONO, color=CRIMSON, font_size=36, weight=BOLD)
        rank_1.next_to(mega_bar, LEFT, buff=0.28)
        rank_2 = Text("2", font=MONO, color=TEAL, font_size=36, weight=BOLD)
        rank_2.next_to(helix_bar, LEFT, buff=0.28)

        header = SerifLabel("ranked by dollar amount", INK, size=24)
        header.to_edge(UP, buff=0.7)

        self.play(FadeIn(header), Create(baseline), run_time=0.7)
        self.play(GrowFromEdge(mega_bar, DOWN), FadeIn(mega_label), FadeIn(mega_name),
                  run_time=0.9)
        self.play(GrowFromEdge(helix_bar, DOWN), FadeIn(helix_label), FadeIn(helix_name),
                  run_time=0.9)
        self.play(FadeIn(rank_1), FadeIn(rank_2), run_time=0.6)
        self.wait(max(0.3, total - 3.1))


class B05_RecencyLeading(Scene):
    """Timeline: months since raise. TEAL zone = 0-12 months (signal).
    Transition zone 12-18 months. CRIMSON = past 18 months (history)."""
    def construct(self):
        total = DUR["B05"]

        # axis
        ax_start = LEFT * 5.5 + DOWN * 0.5
        ax_end = RIGHT * 5.5 + DOWN * 0.5
        axis = Line(ax_start, ax_end, color=INK, stroke_width=2)

        # zones: 0-12 months (TEAL), 12-18 (fade), 18-24+ (CRIMSON)
        # map 0-24 months to -5.5 to 5.5 (11 units wide, so 1 month = 11/24)
        scale = 11.0 / 24.0  # x per month
        x0 = -5.5

        teal_zone = Rectangle(width=12 * scale, height=0.9)
        teal_zone.set_fill(TEAL, 0.20).set_stroke(width=0, opacity=0)
        teal_zone.move_to(RIGHT * (x0 + 6 * scale) + DOWN * 0.5)

        mid_zone = Rectangle(width=6 * scale, height=0.9)
        mid_zone.set_fill(INK, 0.06).set_stroke(width=0, opacity=0)
        mid_zone.move_to(RIGHT * (x0 + 15 * scale) + DOWN * 0.5)

        crimson_zone = Rectangle(width=6 * scale, height=0.9)
        crimson_zone.set_fill(CRIMSON, 0.20).set_stroke(width=0, opacity=0)
        crimson_zone.move_to(RIGHT * (x0 + 21 * scale) + DOWN * 0.5)

        # tick marks & labels
        for mo, label_txt in [(0, "0"), (6, "6 mo"), (12, "12 mo"), (18, "18 mo"), (24, "24 mo")]:
            xp = x0 + mo * scale
            tick = Line(RIGHT * xp + DOWN * 0.95, RIGHT * xp + DOWN * 1.05,
                        color=INK, stroke_width=1.5)
            self.add(tick)
            lbl = Text(label_txt, font=MONO, color=INK, font_size=14)
            lbl.move_to(RIGHT * xp + DOWN * 1.3)
            self.add(lbl)

        axis_label = SerifLabel("months since raise", INK, size=20)
        axis_label.next_to(axis, DOWN, buff=0.85)

        # company dots
        helix_x = x0 + (7 / 4) * scale  # 7 weeks ~ 1.75 months
        mega_x = x0 + 14 * scale

        helix_dot = Dot(radius=0.16, color=TEAL)
        helix_dot.move_to(RIGHT * helix_x + DOWN * 0.5)
        helix_lbl = LabelChip("Helix Bio", accent=TEAL, size=20)
        helix_lbl.next_to(helix_dot, UP, buff=0.28)

        mega_dot = Dot(radius=0.16, color=CRIMSON)
        mega_dot.move_to(RIGHT * mega_x + DOWN * 0.5)
        mega_lbl = LabelChip("MegaCloud", accent=CRIMSON, size=20)
        mega_lbl.next_to(mega_dot, UP, buff=0.28)

        zone_label_teal = SerifLabel("signal zone", TEAL, size=20)
        zone_label_teal.move_to(RIGHT * (x0 + 6 * scale) + UP * 0.35)
        zone_label_crimson = SerifLabel("history", CRIMSON, size=20)
        zone_label_crimson.move_to(RIGHT * (x0 + 21 * scale) + UP * 0.35)

        self.play(FadeIn(teal_zone), FadeIn(mid_zone), FadeIn(crimson_zone),
                  Create(axis), FadeIn(axis_label), run_time=0.9)
        self.play(FadeIn(zone_label_teal), FadeIn(zone_label_crimson), run_time=0.6)
        self.play(FadeIn(helix_dot), FadeIn(helix_lbl), run_time=0.7)
        self.play(FadeIn(mega_dot), FadeIn(mega_lbl), run_time=0.7)
        self.wait(max(0.3, total - 2.9))


class B06_SizeInversion(Scene):
    """Two company cards: 14-person startup (TEAL) vs 3000-person corp (CRIMSON).
    Access dynamic labeled below each."""
    def construct(self):
        total = DUR["B06"]

        # left card: small company
        left_card = _card(4.0, 4.2, TEAL, 0.10, TEAL, 2.5)
        left_card.move_to(LEFT * 3.2 + DOWN * 0.1)

        left_num = Text("14", font=DISPLAY, color=TEAL, font_size=64, weight=BOLD)
        left_num.move_to(left_card.get_center() + UP * 0.4)
        left_unit = Text("people", font=SERIF, color=INK, font_size=22)
        left_unit.next_to(left_num, DOWN, buff=0.1)
        left_chip = LabelChip("Helix Bio", accent=TEAL, size=22)
        left_chip.next_to(left_card, UP, buff=0.2)

        left_access = SerifLabel("founder reads your email", TEAL, size=22)
        left_access.next_to(left_card, DOWN, buff=0.25)

        # right card: large company
        right_card = _card(4.0, 4.2, CRIMSON, 0.10, CRIMSON, 2.5)
        right_card.move_to(RIGHT * 3.2 + DOWN * 0.1)

        right_num = Text("3,000", font=DISPLAY, color=CRIMSON, font_size=48, weight=BOLD)
        right_num.move_to(right_card.get_center() + UP * 0.4)
        right_unit = Text("people", font=SERIF, color=INK, font_size=22)
        right_unit.next_to(right_num, DOWN, buff=0.1)
        right_chip = LabelChip("MegaCloud", accent=CRIMSON, size=22)
        right_chip.next_to(right_card, UP, buff=0.2)

        right_access = SerifLabel("applicant 847 in the queue", CRIMSON, size=22)
        right_access.next_to(right_card, DOWN, buff=0.25)

        self.play(FadeIn(left_card), FadeIn(left_chip), run_time=0.6)
        self.play(FadeIn(left_num), FadeIn(left_unit), run_time=0.5)
        self.play(FadeIn(left_access, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(right_card), FadeIn(right_chip), run_time=0.6)
        self.play(FadeIn(right_num), FadeIn(right_unit), run_time=0.5)
        self.play(FadeIn(right_access, shift=UP * 0.15), run_time=0.5)
        self.wait(max(0.3, total - 3.2))


class B07_QuadrantMap(Scene):
    """2x2 quadrant. Recency (horizontal: old left, recent right).
    Size (vertical: large up, small down). Target zone: bottom-right (GOLD fill).
    Helix Bio dot in target zone, MegaCloud in top-left."""
    def construct(self):
        total = DUR["B07"]

        # axes
        h_axis = Line(LEFT * 5.5 + DOWN * 0.1, RIGHT * 5.5 + DOWN * 0.1,
                      color=INK, stroke_width=2)
        v_axis = Line(DOWN * 3.5 + LEFT * 0.0, UP * 3.5 + LEFT * 0.0,
                      color=INK, stroke_width=2)

        # axis labels
        h_label_left = SerifLabel("older raise", INK, size=20)
        h_label_left.move_to(LEFT * 4.5 + DOWN * 0.65)
        h_label_right = SerifLabel("recent raise", TEAL, size=20)
        h_label_right.move_to(RIGHT * 4.0 + DOWN * 0.65)

        v_label_top = SerifLabel("large company", CRIMSON, size=20)
        v_label_top.move_to(RIGHT * 1.8 + UP * 3.1)
        v_label_bottom = SerifLabel("small company", TEAL, size=20)
        v_label_bottom.move_to(RIGHT * 1.8 + DOWN * 2.8)

        # four quadrant fills
        q_tl = Rectangle(width=5.5, height=3.4)
        q_tl.set_fill(CRIMSON, 0.07).set_stroke(width=0, opacity=0)
        q_tl.move_to(LEFT * 2.75 + UP * 1.7)

        q_tr = Rectangle(width=5.5, height=3.4)
        q_tr.set_fill(SLATE, 0.06).set_stroke(width=0, opacity=0)
        q_tr.move_to(RIGHT * 2.75 + UP * 1.7)

        q_bl = Rectangle(width=5.5, height=3.2)
        q_bl.set_fill(SLATE, 0.06).set_stroke(width=0, opacity=0)
        q_bl.move_to(LEFT * 2.75 + DOWN * 1.7)

        q_br = Rectangle(width=5.5, height=3.2)
        q_br.set_fill(GOLD, 0.28).set_stroke(width=0, opacity=0)
        q_br.move_to(RIGHT * 2.75 + DOWN * 1.7)

        target_label = LabelChip("TARGET ZONE", accent=TEAL, size=22)
        target_label.move_to(RIGHT * 3.2 + DOWN * 2.5)

        # company dots
        helix_dot = Dot(radius=0.18, color=TEAL)
        helix_dot.move_to(RIGHT * 3.5 + DOWN * 2.0)
        helix_lbl = LabelChip("Helix Bio", accent=TEAL, size=20)
        helix_lbl.next_to(helix_dot, RIGHT, buff=0.2)

        mega_dot = Dot(radius=0.18, color=CRIMSON)
        mega_dot.move_to(LEFT * 2.0 + UP * 2.0)
        mega_lbl = LabelChip("MegaCloud", accent=CRIMSON, size=20)
        mega_lbl.next_to(mega_dot, RIGHT, buff=0.2)

        self.play(FadeIn(q_tl), FadeIn(q_tr), FadeIn(q_bl), FadeIn(q_br),
                  Create(h_axis), Create(v_axis), run_time=1.0)
        self.play(FadeIn(h_label_left), FadeIn(h_label_right),
                  FadeIn(v_label_top), FadeIn(v_label_bottom), run_time=0.7)
        self.play(FadeIn(target_label, scale=0.9), run_time=0.6)
        self.play(FadeIn(helix_dot), FadeIn(helix_lbl), run_time=0.6)
        self.play(FadeIn(mega_dot), FadeIn(mega_lbl), run_time=0.6)
        self.wait(max(0.3, total - 3.5))


class B08_RecencyDecay(Scene):
    """Decay curve: hiring energy vs months since raise.
    Teal high zone (0-12 mo) -> transition -> Crimson low (18+ mo).
    Uses explicit coordinates to avoid ax.i2gp() compatibility issues."""
    def construct(self):
        total = DUR["B08"]

        # coordinate system
        ax = Axes(
            x_range=[0, 24, 6],
            y_range=[0, 1, 0.5],
            x_length=10,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2},
            tips=False,
        )
        ax.move_to(DOWN * 0.2)

        x_lbl = SerifLabel("months since raise", INK, size=20)
        x_lbl.next_to(ax, DOWN, buff=0.45)
        y_lbl = SerifLabel("hiring energy", INK, size=20)
        y_lbl.rotate(PI / 2).next_to(ax, LEFT, buff=0.45)

        def _f(x):
            return max(0.05, 0.95 * (0.87 ** x))

        # decay curve
        curve = ax.plot(_f, x_range=[0, 24], color=TEAL, stroke_width=3)

        # shade zones using rectangles mapped to axes coords
        teal_area = ax.get_area(ax.plot(_f, x_range=[0, 12]), x_range=[0, 12],
                                color=TEAL, opacity=0.18)
        crimson_area = ax.get_area(ax.plot(_f, x_range=[18, 24]), x_range=[18, 24],
                                   color=CRIMSON, opacity=0.25)

        # vertical dashed markers — use explicit c2p coords
        x12_bot = ax.c2p(12, 0)
        x12_top = ax.c2p(12, _f(12))
        m12 = DashedLine(x12_bot, x12_top, color=INK, stroke_width=1.5)

        x18_bot = ax.c2p(18, 0)
        x18_top = ax.c2p(18, _f(18))
        m18 = DashedLine(x18_bot, x18_top, color=CRIMSON, stroke_width=1.5)

        lbl_12 = LabelChip("12 mo", accent=INK, size=18)
        lbl_12.move_to(ax.c2p(12, -0.25))
        lbl_18 = LabelChip("18 mo", accent=CRIMSON, size=18)
        lbl_18.move_to(ax.c2p(18, -0.25))

        # company dots at explicit positions on the curve
        helix_pos = ax.c2p(1.75, _f(1.75))
        helix_dot = Dot(radius=0.13, color=TEAL)
        helix_dot.move_to(helix_pos)
        helix_lbl = LabelChip("Helix Bio", accent=TEAL, size=18)
        helix_lbl.next_to(helix_dot, UP, buff=0.22)

        mega_pos = ax.c2p(14, _f(14))
        mega_dot = Dot(radius=0.13, color=CRIMSON)
        mega_dot.move_to(mega_pos)
        mega_lbl = LabelChip("MegaCloud", accent=CRIMSON, size=18)
        mega_lbl.next_to(mega_dot, UP, buff=0.22)

        self.play(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.8)
        self.play(Create(curve), FadeIn(teal_area), FadeIn(crimson_area), run_time=1.0)
        self.play(Create(m12), Create(m18), FadeIn(lbl_12), FadeIn(lbl_18), run_time=0.7)
        self.play(FadeIn(helix_dot), FadeIn(helix_lbl),
                  FadeIn(mega_dot), FadeIn(mega_lbl), run_time=0.7)
        self.wait(max(0.3, total - 3.2))


class B09_ThreeLeads(Scene):
    """Three leads table. Two rankings shown side by side:
    Dollar-amount order (reversed, CRIMSON) vs Recency-x-size order (correct, TEAL)."""
    def construct(self):
        total = DUR["B09"]

        # ── LEFT TABLE: wrong ranking (dollar amount) ──
        left_header = LabelChip("dollar amount rank", accent=CRIMSON, size=20)
        left_header.move_to(LEFT * 3.4 + UP * 3.0)

        wrong_rows = [
            ("1", "MegaCloud", "$220M · 14 mo · 3,000 ppl", CRIMSON),
            ("2", "DataCorp", "$90M · 11 mo · 600 ppl", SLATE),
            ("3", "Helix Bio", "$6M · 7 wks · 14 ppl", TEAL),
        ]

        wrong_vgroup = []
        for i, (rank, co, detail, color) in enumerate(wrong_rows):
            y = 1.8 - i * 1.4
            row_bg = _card(5.8, 1.1, color, 0.08, color, 1.5)
            row_bg.move_to(LEFT * 3.4 + UP * y)
            rank_t = Text(rank, font=MONO, color=color, font_size=28, weight=BOLD)
            rank_t.move_to(LEFT * 5.8 + UP * y)
            co_t = Text(co, font=DISPLAY, color=color, font_size=18, weight=BOLD)
            co_t.move_to(LEFT * 4.2 + UP * (y + 0.18))
            det_t = Text(detail, font=SERIF, color=INK, font_size=14)
            det_t.move_to(LEFT * 4.2 + UP * (y - 0.22))
            wrong_vgroup.extend([row_bg, rank_t, co_t, det_t])

        # ── RIGHT TABLE: correct ranking (recency x size) ──
        right_header = LabelChip("recency x size rank", accent=TEAL, size=20)
        right_header.move_to(RIGHT * 3.4 + UP * 3.0)

        correct_rows = [
            ("1", "Helix Bio", "$6M · 7 wks · 14 ppl", TEAL),
            ("2", "DataCorp", "$90M · 11 mo · 600 ppl", SLATE),
            ("3", "MegaCloud", "$220M · 14 mo · 3,000 ppl", CRIMSON),
        ]

        correct_vgroup = []
        for i, (rank, co, detail, color) in enumerate(correct_rows):
            y = 1.8 - i * 1.4
            row_bg = _card(5.8, 1.1, color, 0.08, color, 1.5)
            row_bg.move_to(RIGHT * 3.4 + UP * y)
            rank_t = Text(rank, font=MONO, color=color, font_size=28, weight=BOLD)
            rank_t.move_to(RIGHT * 0.9 + UP * y)
            co_t = Text(co, font=DISPLAY, color=color, font_size=18, weight=BOLD)
            co_t.move_to(RIGHT * 2.7 + UP * (y + 0.18))
            det_t = Text(detail, font=SERIF, color=INK, font_size=14)
            det_t.move_to(RIGHT * 2.7 + UP * (y - 0.22))
            correct_vgroup.extend([row_bg, rank_t, co_t, det_t])

        divider = Line(UP * 3.2 + ORIGIN, DOWN * 2.8 + ORIGIN,
                       color=INK, stroke_width=1.5)

        note = SerifLabel("illustrative", INK, size=16)
        note.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(left_header), FadeIn(right_header), Create(divider), run_time=0.7)
        self.play(*[FadeIn(m, shift=RIGHT * 0.3) for m in wrong_vgroup], run_time=1.2)
        self.play(*[FadeIn(m, shift=LEFT * 0.3) for m in correct_vgroup], run_time=1.2)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(max(0.3, total - 3.6))


class B10_Endcard(Scene):
    def construct(self):
        total = DUR["B10"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        a1 = Text("Raise size: lagging descriptor.", font=SERIF, color=INK,
                  font_size=28, weight=BOLD)
        a2 = Text("Recency: leading indicator.", font=SERIF, color=TEAL,
                  font_size=28, weight=BOLD)
        a3 = Text("Sort by recency, weighted by size.", font=DISPLAY, color=INK,
                  font_size=22)
        block = VGroup(a1, a2, a3).arrange(DOWN, buff=0.22).move_to(ORIGIN + UP * 0.1)
        u = Line(a3.get_corner(DL) + DOWN * 0.12, a3.get_corner(DR) + DOWN * 0.12,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.5)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(a1), run_time=0.6)
        self.play(FadeIn(a2), run_time=0.6)
        self.play(FadeIn(a3), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 2.5))
