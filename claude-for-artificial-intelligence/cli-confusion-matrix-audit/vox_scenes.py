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


class B04_ConfusionMatrices(Scene):
    def construct(self):
        # Cell geometry
        CW = 2.2    # cell width
        CH = 1.2    # cell height

        # Left matrix: DummyClassifier — x center = -3.0
        # Right matrix: LogisticRegression — x center = +3.0
        # Row centers: row0 (Actual-) y=0.8; row1 (Actual+) y=-0.4
        # Col layout for each matrix:
        #   left matrix:  col0 x=-3.0-CW/2=-4.1; col1 x=-3.0+CW/2=-1.9
        #   right matrix: col0 x= 3.0-CW/2= 1.9; col1 x= 3.0+CW/2= 4.1

        DUMMY_CELLS = [
            # (col_x, row_y, fill_color, fill_opacity, label)
            (-4.1,  0.8, PASS_CLR, 0.4,  "TN\n9500"),   # TN
            (-1.9,  0.8, CRIMSON,  0.08, "FP\n0"),       # FP
            (-4.1, -0.4, CRIMSON,  0.5,  "FN\n500"),     # FN  ← missed all positives
            (-1.9, -0.4, PASS_CLR, 0.08, "TP\n0"),       # TP
        ]
        LR_CELLS = [
            (1.9,  0.8, PASS_CLR, 0.4,  "TN\n9200"),    # TN
            (4.1,  0.8, CRIMSON,  0.35, "FP\n300"),      # FP
            (1.9, -0.4, CRIMSON,  0.35, "FN\n150"),      # FN
            (4.1, -0.4, PASS_CLR, 0.55, "TP\n350"),      # TP
        ]

        def build_cells(data):
            cells = VGroup()
            values = VGroup()
            for (cx, cy, clr, op, lbl) in data:
                cell = Rectangle(
                    width=CW, height=CH,
                    fill_color=clr, fill_opacity=op,
                    stroke_width=0.5, stroke_color=INK, stroke_opacity=0.6,
                ).move_to([cx, cy, 0])
                cells.add(cell)
                t = Text(lbl, color=INK, font_size=19).move_to([cx, cy, 0])
                values.add(t)
            return cells, values

        dummy_cells, dummy_values = build_cells(DUMMY_CELLS)
        logreg_cells, logreg_values = build_cells(LR_CELLS)

        # ── Title ──────────────────────────────────────────────────────────────
        title = Text("CONFUSION MATRIX AUDIT — IMBALANCED DATA",
                     color=INK, weight=BOLD, font_size=26).move_to([0, 3.2, 0])

        # ── Matrix titles ──────────────────────────────────────────────────────
        dummy_title = Text("DUMMY CLASSIFIER", color=SLATE, font_size=20
                           ).move_to([-3.0, 1.65, 0])
        logreg_title = Text("LOGISTIC REG", color=INK, font_size=20
                            ).move_to([3.0, 1.65, 0])
        matrix_titles = VGroup(dummy_title, logreg_title)

        # ── Column labels (Pred- / Pred+) for each matrix ──────────────────────
        col_label_y = 2.1

        def col_lbl(txt, x):
            bg = Rectangle(width=1.0, height=0.28, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([x, col_label_y, 0])
            t = Text(txt, color=SLATE, font_size=17).move_to([x, col_label_y, 0])
            return VGroup(bg, t)

        col_labels = VGroup(
            col_lbl("Pred −", -4.1), col_lbl("Pred +", -1.9),
            col_lbl("Pred −",  1.9), col_lbl("Pred +",  4.1),
        )

        # ── Row labels (Actual- / Actual+) ────────────────────────────────────
        def row_lbl(txt, y):
            bg = Rectangle(width=1.2, height=0.28, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([-5.55, y, 0])
            t = Text(txt, color=SLATE, font_size=17).move_to([-5.55, y, 0])
            return VGroup(bg, t)

        row_labels = VGroup(
            row_lbl("Actual −",  0.8),
            row_lbl("Actual +", -0.4),
        )

        # ── Divider line ───────────────────────────────────────────────────────
        divider = Line([0.0, -2.0, 0], [0.0, 1.4, 0],
                       color=SLATE, stroke_width=0.5)

        # ── Accuracy / Recall labels ───────────────────────────────────────────
        def metric_label(txt, x, y, clr, bold=False):
            kw = {"weight": BOLD} if bold else {}
            bg = Rectangle(width=2.5, height=0.30, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([x, y, 0])
            t = Text(txt, color=clr, font_size=20, **kw).move_to([x, y, 0])
            return VGroup(bg, t)

        accuracy_labels = VGroup(
            metric_label("Accuracy: 95.0%", -3.0, -1.2, CRIMSON),
            metric_label("Accuracy: 95.5%",  3.0, -1.2, INK),
        )
        recall_labels = VGroup(
            metric_label("Recall:  0%",  -3.0, -1.75, CRIMSON, bold=True),
            metric_label("Recall: 70%",   3.0, -1.75, PASS_CLR, bold=True),
        )

        # ── Verdict ────────────────────────────────────────────────────────────
        verdict_bg = Rectangle(width=5.6, height=0.38, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to([0, -2.8, 0])
        verdict_text = Text("Same accuracy, opposite purpose",
                            color=CRIMSON, weight=BOLD, font_size=28
                            ).move_to([0, -2.8, 0])

        # ── 7 play() calls (distinct shape states each time) ──────────────────
        self.play(Write(title))
        self.play(FadeIn(col_labels), FadeIn(row_labels), FadeIn(matrix_titles))
        # Add dummy cells two at a time to ensure shape-state changes
        self.play(FadeIn(dummy_cells[0]), FadeIn(dummy_cells[1]),
                  *[Write(v) for v in dummy_values[:2]])
        self.play(FadeIn(dummy_cells[2]), FadeIn(dummy_cells[3]),
                  *[Write(v) for v in dummy_values[2:]])
        self.play(FadeIn(logreg_cells[0]), FadeIn(logreg_cells[1]),
                  *[Write(v) for v in logreg_values[:2]])
        self.play(FadeIn(logreg_cells[2]), FadeIn(logreg_cells[3]),
                  *[Write(v) for v in logreg_values[2:]])
        self.play(FadeIn(accuracy_labels), FadeIn(recall_labels),
                  FadeIn(divider),
                  FadeIn(verdict_bg), Write(verdict_text))
        self.wait(1)
