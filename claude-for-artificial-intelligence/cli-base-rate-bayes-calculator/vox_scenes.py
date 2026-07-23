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


class B04_BayesHeatmap(Scene):
    def construct(self):
        # Pre-computed PPV grid (specificity=0.82 fixed)
        # rows: prevalence [0.005, 0.01, 0.02, 0.05, 0.10]
        # cols: sensitivity [0.70,  0.80, 0.85, 0.90, 0.99]
        PPV_GRID = [
            [0.019, 0.022, 0.023, 0.024, 0.027],  # prev=0.005
            [0.037, 0.043, 0.045, 0.048, 0.052],  # prev=0.01
            [0.073, 0.083, 0.087, 0.092, 0.101],  # prev=0.02
            [0.163, 0.183, 0.190, 0.200, 0.215],  # prev=0.05
            [0.277, 0.306, 0.318, 0.331, 0.354],  # prev=0.10
        ]
        PREV_LABELS = ["0.5%", "1%", "2%", "5%", "10%"]
        SENS_LABELS = ["70%", "80%", "85%", "90%", "99%"]

        CELL_W = 1.8
        CELL_H = 0.78
        GRID_LEFT = -4.5  # left edge of grid (x of column 0 center = GRID_LEFT + CELL_W*0 + CELL_W/2)
        GRID_TOP  =  2.0  # top edge; row 0 center y = GRID_TOP - CELL_H/2

        def cell_center(row, col):
            x = GRID_LEFT + col * CELL_W + CELL_W / 2
            y = GRID_TOP - row * CELL_H - CELL_H / 2
            return [x, y, 0]

        def ppv_color(v):
            if v < 0.10:
                return CRIMSON
            elif v < 0.30:
                return GOLD
            else:
                return PASS_CLR

        def text_color_on(bg):
            return CREAM if bg == CRIMSON else INK

        # ── Title ──────────────────────────────────────────────────────────────
        title = Text("BAYES PPV: BASE RATE x SENSITIVITY",
                     color=INK, weight=BOLD, font_size=30).move_to([0, 3.2, 0])

        # ── Column headers (sensitivity) ───────────────────────────────────────
        col_header_y = GRID_TOP + CELL_H * 0.22
        col_headers = VGroup(*[
            Text(SENS_LABELS[j], color=INK, font_size=18).move_to(
                [GRID_LEFT + j * CELL_W + CELL_W / 2, col_header_y, 0]
            )
            for j in range(5)
        ])

        # Column axis label
        col_axis_bg = Rectangle(width=2.4, height=0.30, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0).move_to([0, col_header_y + 0.35, 0])
        col_axis_lbl = Text("Sensitivity →", color=SLATE, font_size=18
                            ).move_to([0, col_header_y + 0.35, 0])
        col_headers_group = VGroup(col_headers, col_axis_bg, col_axis_lbl)

        # ── Row headers (prevalence) ───────────────────────────────────────────
        row_headers = VGroup(*[
            Text(PREV_LABELS[i], color=INK, font_size=18).move_to(
                [-5.2, GRID_TOP - i * CELL_H - CELL_H / 2, 0]
            )
            for i in range(5)
        ])

        # Row axis label (vertical)
        row_axis_bg = Rectangle(width=2.0, height=0.28, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0
                                ).move_to([-5.65, GRID_TOP - 2 * CELL_H, 0]).rotate(PI / 2)
        row_axis_lbl = Text("Prevalence ↑", color=SLATE, font_size=18
                            ).move_to([-5.65, GRID_TOP - 2 * CELL_H, 0]).rotate(PI / 2)
        row_headers_group = VGroup(row_headers, row_axis_bg, row_axis_lbl)

        # ── Build cells grouped by color ───────────────────────────────────────
        crimson_cells = VGroup()
        gold_cells    = VGroup()
        green_cells   = VGroup()
        all_value_texts = VGroup()

        # Also track sepsis cell (row=2, col=2 ≈ prev=0.02, sens=0.85)
        sepsis_highlight = None

        for i in range(5):
            for j in range(5):
                ppv = PPV_GRID[i][j]
                clr = ppv_color(ppv)
                ctr = cell_center(i, j)
                cell = Rectangle(
                    width=CELL_W - 0.04, height=CELL_H - 0.04,
                    fill_color=clr, fill_opacity=0.85,
                    stroke_width=0.5, stroke_color=INK, stroke_opacity=0.4
                ).move_to(ctr)
                txt = Text(f"{ppv:.2f}", font_size=19,
                           color=text_color_on(clr)).move_to(ctr)
                all_value_texts.add(txt)
                if clr == CRIMSON:
                    crimson_cells.add(cell)
                elif clr == GOLD:
                    gold_cells.add(cell)
                else:
                    green_cells.add(cell)

                # Sepsis highlight: row=2 (prev=0.02), col=2 (sens=0.85)
                if i == 2 and j == 2:
                    sepsis_highlight = Rectangle(
                        width=CELL_W - 0.04, height=CELL_H - 0.04,
                        fill_opacity=0,
                        stroke_width=3, stroke_color=INK
                    ).move_to(ctr)

        # Sepsis label
        sep_ctr = cell_center(2, 2)
        sep_bg = Rectangle(width=1.8, height=0.30, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0
                           ).move_to([sep_ctr[0] + 1.5, sep_ctr[1] - 0.5, 0])
        sepsis_label = Text("Sepsis model", color=INK, font_size=18
                            ).move_to([sep_ctr[0] + 1.5, sep_ctr[1] - 0.5, 0])
        sepsis_group = VGroup(sepsis_highlight, sep_bg, sepsis_label)

        # ── Bottom label ───────────────────────────────────────────────────────
        bottom_bg = Rectangle(width=6.8, height=0.30, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([0, -2.8, 0])
        bottom_lbl = Text("Specificity = 0.82 (sepsis model, Wong et al. 2021)",
                          color=SLATE, font_size=18).move_to([0, -2.8, 0])

        # ── Verdict ────────────────────────────────────────────────────────────
        verdict_bg = Rectangle(width=6.8, height=0.38, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to([0, -3.2, 0])
        verdict_text = Text("High sensitivity cannot overcome a low base rate",
                            color=CRIMSON, font_size=24).move_to([0, -3.2, 0])

        # ── 6 play() calls ─────────────────────────────────────────────────────
        self.play(Write(title))
        self.play(FadeIn(col_headers_group), FadeIn(row_headers_group))
        self.play(*[FadeIn(c) for c in crimson_cells])
        self.play(*[FadeIn(c) for c in gold_cells])
        self.play(*[FadeIn(c) for c in green_cells],
                  *[Write(v) for v in all_value_texts])
        self.play(FadeIn(sepsis_group),
                  FadeIn(bottom_bg), Write(bottom_lbl),
                  FadeIn(verdict_bg), Write(verdict_text))
        self.wait(1)
