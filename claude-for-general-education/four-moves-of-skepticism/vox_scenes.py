import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR="#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_FourMoves(Scene):
    def construct(self):
        # ---- helper: labeled text with CREAM bg ----
        def bg_text(txt, pos, fontsize=22, color=INK, w=None, h=0.38):
            t = Text(txt, font_size=fontsize, color=color, weight=BOLD)
            t.move_to(pos)
            bw = w if w else max(t.width + 0.25, 0.5)
            bg = Rectangle(
                width=bw, height=h,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            return VGroup(bg, t)

        def plain_text(txt, pos, fontsize=22, color=INK):
            return Text(txt, font_size=fontsize, color=color).move_to(pos)

        # ---- Title ----
        title = Text(
            "The Skeptic's Four-Move Inspection Checklist",
            font_size=28, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # ---- Cell data ----
        CELL_W = 5.2
        CELL_H = 2.0
        COL_X = [-2.7, 2.7]
        ROW_Y = [1.3, -1.0]

        cells_data = [
            # (col, row, philosopher+year, move_name, definition, catches)
            (0, 0, "DESCARTES 1641",       "CARTESIAN DOUBT",
             "Inspect every source of confidence",   "Hallucinated citations"),
            (1, 0, "HUME 1739",             "HUMEAN INDUCTION",
             "Past success != future reliability",   "Distribution shift failures"),
            (0, 1, "POPPER 1934",           "POPPERIAN FALSIFIABILITY",
             "State what evidence would refute this", "Unfalsifiable AI predictions"),
            (1, 1, "PLATO ~380 BCE",        "PLATO'S CAVE",
             "Model sees proxies, not the world",    "Benchmark vs. real-world gap"),
        ]

        cell_groups = []
        for (ci, ri, phil_yr, move, defn, catches) in cells_data:
            cx = COL_X[ci]
            cy = ROW_Y[ri]

            # Background rectangle
            cell_rect = Rectangle(
                width=CELL_W, height=CELL_H,
                fill_color=GOLD, fill_opacity=1,
                stroke_color=INK, stroke_width=2
            ).move_to((cx, cy, 0))

            # Line 1: philosopher + year (CRIMSON, y+0.65)
            phil_t = Text(phil_yr, font_size=20, color=CRIMSON, weight=BOLD).move_to((cx, cy+0.65, 0))

            # Line 2: move name (INK bold, y+0.30)
            move_t = Text(move, font_size=24, color=INK, weight=BOLD).move_to((cx, cy+0.30, 0))

            # Thin horizontal rule at y+0.0
            rule = Line(
                (cx - CELL_W/2 + 0.3, cy+0.02, 0),
                (cx + CELL_W/2 - 0.3, cy+0.02, 0),
                color=SLATE, stroke_width=1, stroke_opacity=0.6
            )

            # Line 3: definition (SLATE, y-0.25)
            defn_t = Text(defn, font_size=19, color=SLATE).move_to((cx, cy-0.28, 0))

            # Line 4: catches box (CRIMSON text, CREAM bg rect with CRIMSON border)
            catches_str = "Catches: " + catches
            catches_bg = Rectangle(
                width=min(len(catches_str)*0.115 + 0.3, CELL_W - 0.4),
                height=0.34,
                fill_color=CREAM, fill_opacity=1,
                stroke_color=CRIMSON, stroke_width=1.5,
                stroke_opacity=1
            ).move_to((cx, cy-0.62, 0))
            catches_t = Text(catches_str, font_size=18, color=CRIMSON).move_to((cx, cy-0.62, 0))
            catches_box = VGroup(catches_bg, catches_t)

            grp = VGroup(cell_rect, phil_t, move_t, rule, defn_t, catches_box)
            cell_groups.append(grp)

        # ---- Highlight overlays (dashed CRIMSON outlines) ----
        highlights = []
        for (ci, ri, *_) in cells_data:
            cx = COL_X[ci]
            cy = ROW_Y[ri]
            hl = DashedVMobject(
                Rectangle(
                    width=CELL_W + 0.12, height=CELL_H + 0.12,
                    fill_opacity=0,
                    stroke_color=CRIMSON, stroke_width=3
                ).move_to((cx, cy, 0)),
                num_dashes=24, dashed_ratio=0.5
            )
            highlights.append(hl)

        # ---- Animate (6 play calls) ----
        self.play(Write(title))
        self.play(FadeIn(cell_groups[0]))
        self.play(FadeIn(cell_groups[1]))
        self.play(FadeIn(cell_groups[2]))
        self.play(FadeIn(cell_groups[3]))
        # Highlight sweep: show each outline in sequence
        self.play(
            FadeIn(highlights[0]),
            run_time=0.5
        )
        self.play(
            FadeIn(highlights[1]),
            run_time=0.5
        )
        self.play(
            FadeIn(highlights[2]),
            run_time=0.5
        )
        self.play(
            FadeIn(highlights[3]),
            run_time=0.5
        )
        self.wait(1)
