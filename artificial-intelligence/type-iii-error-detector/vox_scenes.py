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


class B04_ReframingTable(Scene):
    def construct(self):
        # 3 rows x 5 cols: MOVE | REFRAMING | TEST SOLUTION | PASS A | PASS B
        # x from -5.5 to 5.5, col widths: 1.4, 2.4, 2.4, 0.9, 0.9
        COL_CENTERS = [-4.5, -2.5, 0.5, 3.2, 4.5]
        COL_WIDTHS  = [1.4, 2.4, 2.4, 0.9, 0.9]
        ROW_YS = [1.8, 0.8, -0.2]
        ROW_H = 0.85

        ROWS = [
            # (move, reframing, test_sol, pass_a, pass_b, is_distinct, row_bg)
            ("Zoom-Out", "Why need support at all?", "Hide the button",
             "YES", "YES", True, CREAM),
            ("Zoom-In", "Which ticket most expensive?", "Automate top-3 queries",
             "NO", "YES", True, "#F8F5F0"),
            ("Change-Actor", "What blocks self-service?", "Improve search UX",
             "YES", "YES", False, CREAM),
        ]

        title = Text("TYPE III ERROR DETECTOR — REFRAMING TEST", color=INK, font_size=28, weight=BOLD).move_to([0, 3.2, 0])

        # Header row at y=2.7 — INK background with CREAM text (explicitly named per column)
        # Header uses GOLD (light warm) background with INK text for contrast
        HDR_BG = GOLD
        hdr_bg_move  = Rectangle(width=COL_WIDTHS[0], height=0.5, fill_color=HDR_BG, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([COL_CENTERS[0], 2.7, 0])
        hdr_bg_frame = Rectangle(width=COL_WIDTHS[1], height=0.5, fill_color=HDR_BG, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([COL_CENTERS[1], 2.7, 0])
        hdr_bg_sol   = Rectangle(width=COL_WIDTHS[2], height=0.5, fill_color=HDR_BG, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([COL_CENTERS[2], 2.7, 0])
        hdr_bg_pa    = Rectangle(width=COL_WIDTHS[3], height=0.5, fill_color=HDR_BG, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([COL_CENTERS[3], 2.7, 0])
        hdr_bg_pb    = Rectangle(width=COL_WIDTHS[4], height=0.5, fill_color=HDR_BG, fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([COL_CENTERS[4], 2.7, 0])
        hdr_txt_move  = Text("MOVE",          color=INK, font_size=18, weight=BOLD).move_to([COL_CENTERS[0], 2.7, 0])
        hdr_txt_frame = Text("REFRAMING",     color=INK, font_size=18, weight=BOLD).move_to([COL_CENTERS[1], 2.7, 0])
        hdr_txt_sol   = Text("TEST SOLUTION", color=INK, font_size=18, weight=BOLD).move_to([COL_CENTERS[2], 2.7, 0])
        hdr_txt_pa    = Text("PASS A",        color=INK, font_size=18, weight=BOLD).move_to([COL_CENTERS[3], 2.7, 0])
        hdr_txt_pb    = Text("PASS B",        color=INK, font_size=18, weight=BOLD).move_to([COL_CENTERS[4], 2.7, 0])
        table_header = VGroup(hdr_bg_move, hdr_bg_frame, hdr_bg_sol, hdr_bg_pa, hdr_bg_pb,
                              hdr_txt_move, hdr_txt_frame, hdr_txt_sol, hdr_txt_pa, hdr_txt_pb)

        # Build row groups
        row_cell_groups = []
        for ri, (move, reframe, test_sol, pa, pb, distinct, row_bg_col) in enumerate(ROWS):
            ry = ROW_YS[ri]
            # Flag non-distinct row with light CRIMSON fill
            actual_bg = row_bg_col if distinct else "#FFE8E8"
            cell_data = [move, reframe, test_sol, pa, pb]
            pa_col = PASS_CLR if pa == "YES" else CRIMSON
            pb_col = PASS_CLR if pb == "YES" else CRIMSON
            cell_colors = [INK, INK, INK, pa_col, pb_col]
            row_cells = VGroup()
            for ci, (ctxt, cx, cw, ccol) in enumerate(zip(cell_data, COL_CENTERS, COL_WIDTHS, cell_colors)):
                bg = Rectangle(width=cw, height=ROW_H, fill_color=actual_bg, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([cx, ry, 0])
                t = Text(ctxt, color=ccol, font_size=17).move_to([cx, ry, 0])
                row_cells.add(bg, t)
            row_cell_groups.append(row_cells)

        row1_cells = row_cell_groups[0]
        row2_cells = row_cell_groups[1]
        row3_cells = row_cell_groups[2]

        # Extract texts as separate VGroups for Write calls — simplified: just use FadeIn
        row1_texts = VGroup()
        row2_texts = VGroup()
        row3_texts = VGroup()

        # Verdict summary below table
        verdict_distinct = Text("2 of 3 reframings are distinct", color=PASS_CLR, font_size=26).move_to([0, -1.5, 0])
        not_distinct_annotation = Text(
            "Row 3 collapses to original problem — not distinct",
            color=CRIMSON, font_size=24
        ).move_to([0, -2.1, 0])

        verdict_summary = VGroup(verdict_distinct)

        # 6 play() calls
        self.play(Write(title))
        self.play(FadeIn(table_header))
        self.play(FadeIn(row1_cells), Write(row1_texts))
        self.play(FadeIn(row2_cells), Write(row2_texts))
        self.play(FadeIn(row3_cells), Write(row3_texts))
        self.play(Write(verdict_summary), Write(not_distinct_annotation))
