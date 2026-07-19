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


class B04_LegitimacyCards(Scene):
    def construct(self):
        # 2 cols x 3 rows matrix: Finance Committee (left) vs Bedside (right)
        # Cols at x=-2.5 and x=2.5; Rows at y=1.3, 0.0, -1.3
        COL_XS = [-2.5, 2.5]
        ROW_YS = [1.3, 0.0, -1.3]
        CELL_W = 4.5
        CELL_H = 1.1

        ROW_LABELS = ["Pragmatic", "Moral", "Cognitive"]
        # (fill_color, fill_opacity, cell_text)
        CELLS = [
            # Pragmatic left, Pragmatic right
            (PASS_CLR, 0.3, "Serves finance interest V"),
            (PASS_CLR, 0.3, "Serves immediate query V"),
            # Moral left, Moral right
            (PASS_CLR, 0.3, "CFO accountable V"),
            (CRIMSON,  0.3, "Who is accountable? X"),
            # Cognitive left, Cognitive right
            (GOLD, 0.5, "Traceable reasoning ~"),
            (CRIMSON, 0.3, "Counterfeit: trusted for fluency X"),
        ]

        title = Text("LEGITIMACY AUDIT (Suchman 1995)", color=INK, font_size=32, weight=BOLD).move_to([0, 3.1, 0])

        # Divider at x=0
        divider = Line((0.0, -2.3, 0), (0.0, 2.5, 0), color=SLATE, stroke_width=1, stroke_opacity=0.4)

        # Column headers
        fin_bg = Rectangle(width=4.5, height=0.45, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0).move_to([-2.5, 2.3, 0])
        fin_hdr = Text("FINANCE COMMITTEE", color=INK, font_size=22, weight=BOLD).move_to([-2.5, 2.3, 0])
        bed_bg = Rectangle(width=2.5, height=0.45, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0).move_to([2.5, 2.3, 0])
        bed_hdr = Text("BEDSIDE", color=INK, font_size=22, weight=BOLD).move_to([2.5, 2.3, 0])
        col_headers = VGroup(fin_bg, fin_hdr, bed_bg, bed_hdr)

        # Row labels at x=-5.3
        row_labels = VGroup()
        for lbl_str, ry in zip(ROW_LABELS, ROW_YS):
            bg = Rectangle(width=1.5, height=0.4, fill_color=CREAM, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0).move_to([-5.3, ry, 0])
            txt = Text(lbl_str, color=SLATE, font_size=20).move_to([-5.3, ry, 0])
            row_labels.add(bg, txt)

        # Build the 6 cells (row-major: [prag_left, prag_right, moral_left, moral_right, cog_left, cog_right])
        cells_flat = []
        for ci, (fill_col, fill_op, cell_text) in enumerate(CELLS):
            row_i = ci // 2
            col_i = ci % 2
            cx = COL_XS[col_i]
            ry = ROW_YS[row_i]
            bg = Rectangle(width=CELL_W, height=CELL_H, fill_color=fill_col, fill_opacity=fill_op,
                          stroke_width=0, stroke_opacity=0).move_to([cx, ry, 0])
            txt = Text(cell_text, color=INK, font_size=18).move_to([cx, ry, 0])
            cells_flat.append(VGroup(bg, txt))

        pragmatic_left  = cells_flat[0]
        pragmatic_right = cells_flat[1]
        moral_left      = cells_flat[2]
        moral_right     = cells_flat[3]
        cognitive_left  = cells_flat[4]
        cognitive_right = cells_flat[5]

        pragmatic_texts = VGroup()
        moral_texts     = VGroup()
        cognitive_texts = VGroup()

        # Moral flag annotation — placed below the moral row, away from the divider line
        moral_flag_bg = Rectangle(width=2.2, height=0.38, fill_color=CREAM, fill_opacity=1,
                                 stroke_width=0, stroke_opacity=0).move_to([2.5, -0.6, 0])
        moral_flag = Text("accountability gap", color=CRIMSON, font_size=22).move_to([2.5, -0.6, 0])
        moral_flag_annotation = VGroup(moral_flag_bg, moral_flag)

        verdict_bg = Rectangle(width=6.5, height=0.38, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([0, -2.8, 0])
        verdict_text = Text(
            "Same output. Different context. Different moral legitimacy.",
            color=CRIMSON, font_size=24
        ).move_to([0, -2.8, 0])

        # 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(divider), FadeIn(col_headers), FadeIn(row_labels))
        self.play(FadeIn(pragmatic_left), FadeIn(pragmatic_right), Write(pragmatic_texts))
        self.play(FadeIn(moral_left), FadeIn(moral_right), Write(moral_texts))
        self.play(FadeIn(cognitive_left), FadeIn(cognitive_right), Write(cognitive_texts))
        self.play(Write(moral_flag_annotation))
        self.play(FadeIn(verdict_bg), Write(verdict_text))
