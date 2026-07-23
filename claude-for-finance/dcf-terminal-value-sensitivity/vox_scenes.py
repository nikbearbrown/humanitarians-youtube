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


class B04_DCFSensitivity(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        AMBER="#E8A020"

        # Pre-computed EV values ($M)
        ev_data = [
            [2831, 3355, 4178, 5661],
            [2384, 2734, 3239, 4032],
            [2057, 2304, 2641, 3128],
            [1808, 1989, 2228, 2552],
        ]
        wacc_labels = ["7.0%", "8.0%", "9.0%", "10.0%"]
        g_labels = ["1.5%", "2.5%", "3.5%", "4.5%"]

        # Layout
        CELL_W = 2.4
        CELL_H = 0.78
        col_xs = [-3.6, -1.2, 1.2, 3.6]
        row_ys = [1.8, 1.0, 0.2, -0.6]

        def ev_color(ev):
            if ev >= 4500:
                return CRIMSON
            elif ev >= 3000:
                return AMBER
            elif ev >= 2200:
                return GOLD
            else:
                return CREAM

        def ev_text_color(ev):
            if ev >= 4500:
                return CREAM
            elif ev >= 3000:
                return INK
            else:
                return INK

        # Title and subtitle
        title = Text(
            "Terminal Value Is Driven by g, Not WACC",
            font="Georgia", font_size=22, color=ManimColor(INK), weight=BOLD
        ).move_to([0, 3.2, 0])
        subtitle = Text(
            "Enterprise Value ($M) -- Sensitivity Grid",
            font="Georgia", font_size=16, color=ManimColor(SLATE)
        ).move_to([0, 2.95, 0])

        # g header labels
        g_header_labels = VGroup()
        for ci, gl in enumerate(g_labels):
            lbl = Text(f"g={gl}", font="Georgia", font_size=15, color=ManimColor(SLATE))
            lbl.move_to([col_xs[ci], 2.6, 0])
            g_header_labels.add(lbl)

        # WACC side labels
        wacc_side_labels = VGroup()
        for ri, wl in enumerate(wacc_labels):
            bg = Rectangle(
                width=1.2, height=0.38,
                fill_color=ManimColor(CREAM), fill_opacity=1.0,
                stroke_width=0, stroke_opacity=0
            ).move_to([-5.3, row_ys[ri], 0])
            lbl = Text(f"WACC={wl}", font="Georgia", font_size=14, color=ManimColor(INK))
            lbl.move_to([-5.3, row_ys[ri], 0])
            wacc_side_labels.add(VGroup(bg, lbl))

        # Build cell rows
        all_rows = []
        for ri in range(4):
            row_group = VGroup()
            for ci in range(4):
                ev = ev_data[ri][ci]
                clr = ev_color(ev)
                tclr = ev_text_color(ev)
                cell = Rectangle(
                    width=CELL_W - 0.08, height=CELL_H - 0.08,
                    fill_color=ManimColor(clr), fill_opacity=1.0,
                    stroke_width=0, stroke_opacity=0
                ).move_to([col_xs[ci], row_ys[ri], 0])
                val_lbl = Text(
                    f"${ev:,}", font="Georgia", font_size=15, color=ManimColor(tclr)
                ).move_to([col_xs[ci], row_ys[ri], 0])
                row_group.add(VGroup(cell, val_lbl))
            all_rows.append(row_group)

        # Cursor: CRIMSON outline rectangle sweeping g=4.5% column (col index 3)
        cursor = Rectangle(
            width=CELL_W - 0.04, height=CELL_H * 4 + 0.3,
            fill_opacity=0,
            stroke_color=ManimColor(CRIMSON), stroke_width=3, stroke_opacity=1
        ).move_to([col_xs[3], (row_ys[0] + row_ys[3]) / 2, 0])

        # Annotation
        ann_bg = Rectangle(
            width=5.8, height=0.38,
            fill_color=ManimColor(CREAM), fill_opacity=1.0,
            stroke_width=0, stroke_opacity=0
        ).move_to([0, -1.6, 0])
        ann_text = Text(
            "g-axis range: $1808M-$5661M (3.1x);  WACC range per row: smaller",
            font="Georgia", font_size=14, color=ManimColor(INK)
        ).move_to([0, -1.6, 0])

        # Color legend
        legend_items = [
            (CREAM, "<$2,200M"),
            (GOLD, "$2,200-3,000M"),
            (AMBER, "$3,000-4,500M"),
            (CRIMSON, ">=$4,500M"),
        ]
        legend_group = VGroup()
        for li, (clr, label) in enumerate(legend_items):
            swatch = Rectangle(
                width=0.35, height=0.28,
                fill_color=ManimColor(clr), fill_opacity=1.0,
                stroke_width=0, stroke_opacity=0
            ).move_to([-4.5 + li * 2.5, -2.4, 0])
            lbl = Text(label, font="Georgia", font_size=11, color=ManimColor(INK))
            lbl.next_to(swatch, RIGHT, buff=0.08)
            legend_group.add(VGroup(swatch, lbl))

        # Animation
        self.play(Write(title), Write(subtitle))                          # 1
        self.play(FadeIn(g_header_labels), FadeIn(wacc_side_labels))      # 2
        self.play(FadeIn(all_rows[0]))                                    # 3
        self.play(FadeIn(all_rows[1]))                                    # 4
        self.play(FadeIn(all_rows[2]))                                    # 5
        self.play(FadeIn(all_rows[3]))                                    # 6
        self.play(FadeIn(cursor))                                         # 7
        self.play(FadeIn(ann_bg), FadeIn(ann_text), FadeIn(legend_group)) # 8
