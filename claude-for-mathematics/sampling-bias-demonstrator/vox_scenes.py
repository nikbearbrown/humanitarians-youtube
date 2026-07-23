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


class B04_SamplingBias(Scene):
    def construct(self):
        def tick_label(txt, pos, fontsize=18, color=SLATE):
            bg = Rectangle(
                width=max(len(txt)*0.12, 0.4)+0.15, height=0.34,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            t = Text(txt, font_size=fontsize, color=color).move_to(pos)
            return VGroup(bg, t)

        # Title
        title = Text(
            "SAMPLING BIAS — THE 1936 LITERARY DIGEST DISASTER",
            font_size=22, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # Divider
        divider = Line((0.0,-2.5,0),(0.0,2.2,0), color=SLATE, stroke_width=1, stroke_opacity=0.5)

        # Panel headers
        left_header_bg = Rectangle(width=4.2, height=0.38, fill_color=CREAM, fill_opacity=1,
                                    stroke_width=0, stroke_opacity=0).move_to((-2.3,2.5,0))
        left_header = Text("RANDOM SAMPLE (n=2,400)", font_size=18, color=PASS_CLR, weight=BOLD
                           ).move_to((-2.3,2.5,0))
        left_hdr = VGroup(left_header_bg, left_header)

        right_header_bg = Rectangle(width=4.0, height=0.38, fill_color=CREAM, fill_opacity=1,
                                     stroke_width=0, stroke_opacity=0).move_to((2.3,2.5,0))
        right_header = Text("BIASED SAMPLE (n=2,400)", font_size=18, color=CRIMSON, weight=BOLD
                            ).move_to((2.3,2.5,0))
        right_hdr = VGroup(right_header_bg, right_header)

        # Dot grid helpers — 6×6 = 36 dots per panel
        # Left panel: ~22 Democrat (PASS_CLR), 14 Republican (CRIMSON)
        # Right panel: ~13 Democrat, 23 Republican

        def make_dots(dem_count, rep_count, x_start, x_end):
            """Make a 6×6 dot grid from x_start to x_end, y from -1.5 to 1.3"""
            dem_dots = VGroup()
            rep_dots = VGroup()
            cols = 6
            rows = 6
            xs = [x_start + (x_end - x_start) * (c/(cols-1)) for c in range(cols)]
            ys = [-1.5 + 2.8 * (r/(rows-1)) for r in range(rows)]
            positions = [(x, y) for y in ys for x in xs]
            for i, (px, py) in enumerate(positions):
                color = PASS_CLR if i < dem_count else CRIMSON
                d = Dot(point=(px, py, 0), radius=0.18, color=color, fill_opacity=0.9)
                if i < dem_count:
                    dem_dots.add(d)
                else:
                    rep_dots.add(d)
            return dem_dots, rep_dots

        left_dem_dots, left_rep_dots = make_dots(22, 14, -4.3, -0.3)
        right_dem_dots, right_rep_dots = make_dots(13, 23,  0.3,  4.3)

        # Result bars (y=-2.1 to -2.5, thin horizontal bars)
        # Left: D=60% (PASS_CLR), R=40% (CRIMSON)
        # Right: R=65% (CRIMSON), D=35% (PASS_CLR)
        bar_h = 0.28
        bar_y = -2.15

        # Left panel bars (total width ~4.0 from x=-4.3 to -0.3)
        left_bar_w = 4.0
        left_d_w = left_bar_w * 0.60
        left_r_w = left_bar_w * 0.40
        left_d_bar = Rectangle(width=left_d_w, height=bar_h,
                               fill_color=PASS_CLR, fill_opacity=0.85,
                               stroke_width=0, stroke_opacity=0
                               ).move_to((-4.3 + left_d_w/2, bar_y, 0))
        left_r_bar = Rectangle(width=left_r_w, height=bar_h,
                               fill_color=CRIMSON, fill_opacity=0.85,
                               stroke_width=0, stroke_opacity=0
                               ).move_to((-4.3 + left_d_w + left_r_w/2, bar_y, 0))
        left_result_bar = VGroup(left_d_bar, left_r_bar)

        # Right panel bars (total width ~4.0 from x=0.3 to 4.3)
        right_bar_w = 4.0
        right_r_w = right_bar_w * 0.65
        right_d_w = right_bar_w * 0.35
        right_r_bar = Rectangle(width=right_r_w, height=bar_h,
                                fill_color=CRIMSON, fill_opacity=0.85,
                                stroke_width=0, stroke_opacity=0
                                ).move_to((0.3 + right_r_w/2, bar_y, 0))
        right_d_bar = Rectangle(width=right_d_w, height=bar_h,
                                fill_color=PASS_CLR, fill_opacity=0.85,
                                stroke_width=0, stroke_opacity=0
                                ).move_to((0.3 + right_r_w + right_d_w/2, bar_y, 0))
        right_result_bar = VGroup(right_r_bar, right_d_bar)

        # Predicted labels above result bars
        left_predicted  = tick_label("DEMOCRAT wins (60%)",  (-2.3,-1.75,0), fontsize=18, color=PASS_CLR)
        right_predicted = tick_label("REPUBLICAN wins (65%)", (2.3,-1.75,0), fontsize=18, color=CRIMSON)

        # Truth annotation
        truth_bg = Rectangle(width=9.5, height=0.38, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to((0,-2.8,0))
        truth_txt = Text("Truth: 60% Democrat — Literary Digest missed by 37 points",
                         font_size=20, color=CRIMSON).move_to((0,-2.8,0))
        truth_annotation = VGroup(truth_bg, truth_txt)

        # --- Sequence (7 play() calls) ---
        self.play(Write(title))
        self.play(FadeIn(divider), Write(left_hdr), Write(right_hdr))
        self.play(*[FadeIn(d) for d in left_dem_dots])
        self.play(*[FadeIn(d) for d in left_rep_dots])
        self.play(
            *[FadeIn(d) for d in right_dem_dots],
            *[FadeIn(d) for d in right_rep_dots]
        )
        self.play(
            FadeIn(left_result_bar), FadeIn(right_result_bar),
            Write(left_predicted), Write(right_predicted)
        )
        self.play(Write(truth_annotation))
        self.wait(1)
