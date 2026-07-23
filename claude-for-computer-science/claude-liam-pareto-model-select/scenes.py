"""scenes.py — Manim for claude-liam-pareto-model-select. Source: embedded-ai Ch. 11"""
from manim import *
import numpy as np

BG    = ManimColor("#FAF9F5")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


def _xy(flash_mb, acc_pct):
    """Manual coordinate mapping: flash [1.0,2.5] -> x [-3.0,3.5], acc [85,96] -> y [-2.0,2.0]"""
    x = -3.0 + (flash_mb - 1.0) / 1.5 * 6.5
    y = -2.0 + (acc_pct - 85) / 11.0 * 4.0
    return [x, y, 0]


class B01_ScatterPlot(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Model Candidates: Accuracy vs Flash", font_size=26, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Axes labels
        x_lbl = Text("Flash (MB) ->", font_size=14, color=SOFT)
        x_lbl.move_to([0.0, -2.5, 0])
        y_lbl = Text("Accuracy (%)", font_size=14, color=SOFT).rotate(PI/2)
        y_lbl.move_to([-4.2, 0.0, 0])
        ax_x = Line(start=[-3.2, -2.0, 0], end=[3.8, -2.0, 0], color=INK, stroke_width=1.5)
        ax_y = Line(start=[-3.0, -2.2, 0], end=[-3.0, 2.2, 0], color=INK, stroke_width=1.5)
        self.play(Create(ax_x), Create(ax_y), FadeIn(x_lbl), FadeIn(y_lbl))

        # Candidate models: (flash_mb, accuracy, label)
        candidates = [
            (1.5, 88.0, "C1", SOFT),
            (1.8, 91.0, "C2", SOFT),
            (2.0, 92.5, "C3", SOFT),
            (1.6, 89.5, "C4", SOFT),
            (2.04, 94.0, "BEST", ACC),  # leaderboard winner — infeasible
            (1.9, 90.5, "C6", SOFT),
        ]

        for flash, acc, name, color in candidates:
            pos = _xy(flash, acc)
            dot = Dot(point=pos, radius=0.14, color=color, fill_opacity=0.9)
            lbl = Text(name, font_size=13, color=color)
            lbl.move_to([pos[0] + 0.25, pos[1] + 0.25, 0])
            self.play(FadeIn(dot), FadeIn(lbl), run_time=0.25)

        # Flash ceiling line at 2.0 MB
        ceil_x = _xy(2.0, 85)[0]
        ceiling = DashedLine(
            start=[ceil_x, -2.2, 0],
            end=[ceil_x, 2.2, 0],
            color=ACC, dash_length=0.2, stroke_width=2
        )
        ceiling_lbl = Text("2 MB ceiling", font_size=13, color=ACC)
        ceiling_lbl.move_to([ceil_x + 0.7, 2.0, 0])
        self.play(Create(ceiling))
        self.play(FadeIn(ceiling_lbl))

        note = Text("BEST: 94% accuracy — 40 KB over limit. Can't ship.", font_size=14, color=ACC)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(1.2)


class B02_ConstraintLines(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Constraints Strike Out Infeasible Candidates", font_size=24, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        ax_x = Line(start=[-3.2, -2.0, 0], end=[3.8, -2.0, 0], color=INK, stroke_width=1.5)
        ax_y = Line(start=[-3.0, -2.2, 0], end=[-3.0, 2.2, 0], color=INK, stroke_width=1.5)
        self.play(Create(ax_x), Create(ax_y))

        candidates = [
            (1.5, 88.0, SOFT, True),
            (1.8, 91.0, SOFT, True),
            (2.0, 92.5, SOFT, True),
            (1.6, 89.5, SOFT, True),
            (2.04, 94.0, ACC, False),
            (1.9, 90.5, SOFT, True),
        ]

        dots = []
        for flash, acc, color, feasible in candidates:
            pos = _xy(flash, acc)
            dot = Dot(point=pos, radius=0.13, color=color if feasible else ACC, fill_opacity=0.8)
            dots.append((dot, flash, acc, feasible))
            self.play(FadeIn(dot), run_time=0.2)

        # Flash ceiling
        ceil_x = _xy(2.0, 85)[0]
        ceiling = DashedLine(
            start=[ceil_x, -2.2, 0],
            end=[ceil_x, 2.2, 0],
            color=ACC, dash_length=0.2, stroke_width=2
        )
        self.play(Create(ceiling))

        # Shade infeasible zone
        infeasible_zone = Rectangle(
            width=1.5, height=4.4, fill_color=ACC, fill_opacity=0.12, stroke_width=0
        )
        infeasible_zone.move_to([ceil_x + 0.75, 0.0, 0])
        self.play(FadeIn(infeasible_zone))

        # Cross out infeasible dot
        infeasible_pos = _xy(2.04, 94.0)
        cross = Cross(Square(side_length=0.3).move_to(infeasible_pos), color=ACC, stroke_width=2.5)
        self.play(Create(cross))

        note = Text("Only candidates left of the ceiling can ship.", font_size=14, color=SOFT)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(1.2)


class B03_ParetoFrontier(Scene):
    def construct(self):
        self.camera.background_color = BG
        source = Text("Source: Embedded AI — Bear Brown", font_size=11, color=GHOST).to_corner(DR, buff=0.5)
        self.add(source)

        title = Text("Pareto Frontier Among Feasible Candidates", font_size=24, color=INK, weight="BOLD")
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        ax_x = Line(start=[-3.2, -2.0, 0], end=[3.8, -2.0, 0], color=INK, stroke_width=1.5)
        ax_y = Line(start=[-3.0, -2.2, 0], end=[-3.0, 2.2, 0], color=INK, stroke_width=1.5)
        self.play(Create(ax_x), Create(ax_y))

        # Feasible candidates: (flash, acc, on_frontier)
        feasible = [
            (1.5, 88.0, False),
            (1.8, 91.0, True),   # shipped model
            (2.0, 92.5, True),
            (1.6, 89.5, False),  # dominated by C2
            (1.9, 90.5, False),  # dominated by C3
        ]

        for flash, acc, on_front in feasible:
            color = ACC if (on_front and flash == 1.8) else (SOFT if on_front else GHOST)
            pos = _xy(flash, acc)
            dot = Dot(point=pos, radius=0.13, color=color, fill_opacity=0.85)
            self.play(FadeIn(dot), run_time=0.2)

        # Grey out dominated
        for flash, acc, on_front in feasible:
            if not on_front:
                pos = _xy(flash, acc)
                sq = Square(side_length=0.28)
                sq.move_to(pos)
                strike = Cross(sq, color=GHOST, stroke_width=1.5)
                self.play(Create(strike), run_time=0.3)

        # Pareto frontier trace (staircase)
        p18 = _xy(1.8, 91.0)
        p18_92 = _xy(1.8, 92.5)
        p20 = _xy(2.0, 92.5)
        frontier = VMobject()
        frontier.set_points_as_corners([p18, p18_92, p20])
        frontier.set_stroke(color=SOFT, width=2.5)
        self.play(Create(frontier), run_time=0.8)

        # Highlight shipped model
        shipped_pos = _xy(1.8, 91.0)
        circle = Circle(radius=0.22, color=ACC, stroke_width=2.5)
        circle.move_to(shipped_pos)
        shipped_lbl = Text("Shipped: 91%, 1.8 MB\n(200 KB margin)", font_size=14, color=ACC)
        shipped_lbl.move_to([shipped_pos[0] + 1.8, shipped_pos[1] - 0.5, 0])
        self.play(Create(circle))
        self.play(FadeIn(shipped_lbl))

        note = Text("Worse benchmark. Ships reliably.", font_size=15, color=SOFT)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(1.2)
