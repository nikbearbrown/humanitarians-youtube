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


class B04_AuditCards(Scene):
    def construct(self):
        # 5 rows x 4 cols: DOMAIN | VERDICT | MECHANISM | EDGE
        # x from -5 to 5, col centers at approx -3.9, -1.9, 0.5, 3.4
        COL_CENTERS = [-3.7, -1.7, 0.7, 3.5]
        COL_WIDTHS  = [2.0, 1.4, 2.8, 2.8]
        ROW_YS = [1.6, 0.7, -0.2, -1.1, -2.0]
        ROW_H = 0.75

        ROWS = [
            # (domain, verdict, mechanism, edge, verdict_color, row_bg)
            ("Medical",    "YES",           "anomaly",  "requires clinical context", PASS_CLR, CREAM),
            ("Legal",      "INDETERMINATE", "pattern",  "citation verification needed", GOLD, "#F8F5F0"),
            ("Financial",  "NO",            "anomaly",  "R^2 implausibly high", CRIMSON, CREAM),
            ("Logistics",  "YES",           "pattern",  "assumes route data current", PASS_CLR, "#F8F5F0"),
            ("Engineering","YES",           "anomaly",  "load calc not checked", PASS_CLR, CREAM),
        ]

        title = Text("PLAUSIBILITY AUDIT — FIVE DOMAINS", color=INK, font_size=34, weight=BOLD).move_to([0, 3.2, 0])

        # Header row
        header_rects = VGroup()
        header_texts = VGroup()
        header_labels = ["DOMAIN", "VERDICT", "MECHANISM", "EDGE"]
        for i, (lbl, cx, cw) in enumerate(zip(header_labels, COL_CENTERS, COL_WIDTHS)):
            r = Rectangle(width=cw, height=0.55, fill_color=INK, fill_opacity=1,
                         stroke_width=0, stroke_opacity=0).move_to([cx, 2.5, 0])
            t = Text(lbl, color=CREAM, font_size=20, weight=BOLD).move_to([cx, 2.5, 0])
            header_rects.add(r)
            header_texts.add(t)
        header_row = VGroup(header_rects, header_texts)

        # Data rows
        row_groups = []
        for ri, (domain, verdict, mech, edge, vcol, row_bg_col) in enumerate(ROWS):
            ry = ROW_YS[ri]
            row_cells = VGroup()
            # background rects for each cell
            cell_data = [domain, verdict, mech, edge]
            cell_colors = [INK, vcol, INK, INK]
            for ci, (cell_txt, cx, cw, ctxt_col) in enumerate(zip(cell_data, COL_CENTERS, COL_WIDTHS, cell_colors)):
                bg = Rectangle(width=cw, height=ROW_H, fill_color=row_bg_col, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([cx, ry, 0])
                t = Text(cell_txt, color=ctxt_col, font_size=18).move_to([cx, ry, 0])
                row_cells.add(bg, t)
            row_groups.append(row_cells)

        verdict_text = Text(
            "Mechanism names what fired; expert supplies what it fires against",
            color=INK, font_size=22
        ).move_to([0, -2.9, 0])

        # 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(header_row))
        self.play(FadeIn(row_groups[0]))   # Medical
        self.play(FadeIn(row_groups[1]))   # Legal
        self.play(FadeIn(row_groups[2]))   # Financial — flagged
        self.play(FadeIn(row_groups[3]), FadeIn(row_groups[4]))
        self.play(Write(verdict_text))
