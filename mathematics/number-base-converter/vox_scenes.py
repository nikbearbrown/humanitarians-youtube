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


class B04_BaseConverter(Scene):
    def construct(self):
        SEG_COLORS = [CRIMSON, PASS_CLR, "#0055AA", "#E06400", SLATE, "#7B0099"]

        def tick_label(txt, pos, fontsize=18, color=SLATE):
            bg = Rectangle(
                width=max(len(txt)*0.13, 0.4)+0.15, height=0.34,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            t = Text(txt, font_size=fontsize, color=color).move_to(pos)
            return VGroup(bg, t)

        # Title
        title = Text(
            "NUMBER BASE CONVERTER — 738 in BASE 10, 2, 16",
            font_size=24, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # Axes
        x_axis_line = Line((-5.5,-2.5,0),(5.5,-2.5,0), color=INK, stroke_width=1.5)

        # y-tick labels at x=-5.4
        y_lbl_0   = tick_label("0",   (-5.4,-2.5,0))
        y_lbl_369 = tick_label("369", (-5.4,-2.5+2.25,0))   # 369/738*4.5=2.25 → y=-0.25
        y_lbl_738 = tick_label("738", (-5.4, 2.0,0))
        y_tick_labels = VGroup(y_lbl_0, y_lbl_369, y_lbl_738)

        # Column positions and headers
        COL_X = [-3.5, 0.0, 3.5]
        COL_W = 2.5
        BOTTOM_Y = -2.5
        MAX_H = 4.5  # total bar height for value=738

        hdr_10 = tick_label("BASE 10", (COL_X[0], 2.4, 0), fontsize=22, color=INK)
        hdr_2  = tick_label("BASE 2",  (COL_X[1], 2.4, 0), fontsize=22, color=INK)
        hdr_16 = tick_label("BASE 16", (COL_X[2], 2.4, 0), fontsize=22, color=INK)
        col_headers = VGroup(hdr_10, hdr_2, hdr_16)

        def make_stack(contributions, cx, seg_colors):
            """contributions: list of (label, value) from bottom up"""
            segs = VGroup()
            labels = VGroup()
            y_bot = BOTTOM_Y
            for idx, (lbl_txt, val) in enumerate(contributions):
                h = (val / 738.0) * MAX_H
                h = max(h, 0.02)
                cy = y_bot + h/2
                color = seg_colors[idx % len(seg_colors)]
                seg = Rectangle(
                    width=COL_W, height=h,
                    fill_color=color, fill_opacity=1,
                    stroke_width=0, stroke_opacity=0
                ).move_to((cx, cy, 0))
                segs.add(seg)
                if h > 0.28 and lbl_txt:
                    seg_lbl_bg = Rectangle(width=len(lbl_txt)*0.095+0.1, height=0.24,
                                           fill_color=CREAM, fill_opacity=0.7,
                                           stroke_width=0, stroke_opacity=0).move_to((cx, cy, 0))
                    seg_lbl = Text(lbl_txt, font_size=13, color=INK).move_to((cx, cy, 0))
                    labels.add(VGroup(seg_lbl_bg, seg_lbl))
                elif lbl_txt:
                    # tiny bar: label above
                    lbl_above = tick_label(lbl_txt, (cx, y_bot+h+0.18, 0), fontsize=11, color=INK)
                    labels.add(lbl_above)
                y_bot += h
            return segs, labels

        # BASE 10: segments (value, label) bottom up
        b10_data = [
            ("8×1",   8),
            ("3×10",  30),
            ("7×100", 700),
        ]
        b10_segs, b10_lbls = make_stack(b10_data, COL_X[0], SEG_COLORS)

        # BASE 2: 738 = 1011100010
        # contributions of set bits (from LSB to MSB):
        b2_data = [
            ("2",   2),
            ("32",  32),
            ("64",  64),
            ("128", 128),
            ("512", 512),
        ]
        b2_segs, b2_lbls = make_stack(b2_data, COL_X[1], SEG_COLORS)

        # BASE 16: 738 = 2×256 + 14×16 + 2×1
        b16_data = [
            ("2×1",    2),
            ("E×16",  224),
            ("2×256", 512),
        ]
        b16_segs, b16_lbls = make_stack(b16_data, COL_X[2], SEG_COLORS)

        all_segment_labels = VGroup(b10_lbls, b2_lbls, b16_lbls)

        # "= 738" labels below each column
        tot_10 = tick_label("= 738", (COL_X[0],-2.9,0), fontsize=18)
        tot_2  = tick_label("= 738", (COL_X[1],-2.9,0), fontsize=18)
        tot_16 = tick_label("= 738", (COL_X[2],-2.9,0), fontsize=18)
        total_labels = VGroup(tot_10, tot_2, tot_16)

        # Verdict
        verdict_bg = Rectangle(width=8.5, height=0.38, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0).move_to((0,-3.15,0))
        verdict_txt = Text("Same number — three representations",
                           font_size=24, color=CRIMSON, weight=BOLD).move_to((0,-3.15,0))
        verdict_text = VGroup(verdict_bg, verdict_txt)

        # --- Sequence (7 play() calls) ---
        self.play(Write(title))
        self.play(
            FadeIn(x_axis_line),
            FadeIn(y_tick_labels),
            FadeIn(col_headers)
        )
        self.play(*[GrowFromEdge(seg, DOWN) for seg in b10_segs])
        self.play(*[GrowFromEdge(seg, DOWN) for seg in b2_segs])
        self.play(*[GrowFromEdge(seg, DOWN) for seg in b16_segs])
        self.play(*[Write(lbl) for lbl in all_segment_labels])
        self.play(Write(total_labels), Write(verdict_text))
        self.wait(1)
