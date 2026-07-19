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


class B04_CompoundInterest(Scene):
    def construct(self):
        # Palette
        CLR_4 = PASS_CLR
        CLR_7 = "#E06400"
        CLR_10 = CRIMSON

        # Pre-computed monthly compound values P=1000
        PTS_4  = [(0,1000),(5,1221),(10,1491),(15,1819),(20,2220),(25,2711),(30,3310)]
        PTS_7  = [(0,1000),(5,1417),(10,2009),(15,2848),(20,4039),(25,5727),(30,8117)]
        PTS_10 = [(0,1000),(5,1645),(10,2707),(15,4454),(20,7328),(25,12056),(30,19837)]

        def to_xy(year, value):
            x = -5.0 + (year / 30.0) * 10.0
            y = -2.5 + (value / 20000.0) * 5.0
            return (x, y, 0)

        def make_curve(pts, color, sw=2.5):
            segs = VGroup()
            for i in range(len(pts) - 1):
                x1, y1, _ = to_xy(*pts[i])
                x2, y2, _ = to_xy(*pts[i+1])
                segs.add(Line((x1,y1,0),(x2,y2,0), color=color, stroke_width=sw))
            return segs

        # Title
        title = Text(
            "COMPOUND INTEREST — THE EXPONENTIAL CLIFF",
            font_size=28, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # Axes
        x_axis = Line((-5.0,-2.5,0),(5.0,-2.5,0), color=INK, stroke_width=1.5)
        y_axis = Line((-5.0,-2.5,0),(-5.0,2.5,0), color=INK, stroke_width=1.5)

        # Tick labels with CREAM background
        def tick_label(txt, pos, fontsize=18, color=SLATE):
            bg = Rectangle(
                width=len(txt)*0.12+0.15, height=0.32,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            t = Text(txt, font_size=fontsize, color=color).move_to(pos)
            return VGroup(bg, t)

        # x-tick labels at y=-2.9
        x_lbl_0  = tick_label("0",    (-5.0,-2.9,0))
        x_lbl_15 = tick_label("15yr", ( 0.0,-2.9,0))
        x_lbl_30 = tick_label("30yr", ( 5.0,-2.9,0))
        tick_labels = VGroup(x_lbl_0, x_lbl_15, x_lbl_30)

        # y-tick labels at x=-5.5
        y_lbl_0  = tick_label("$0",   (-5.55,-2.5,0))
        y_lbl_10 = tick_label("$10k", (-5.55, 0.0,0))
        y_lbl_20 = tick_label("$20k", (-5.55, 2.5,0))
        axis_labels = VGroup(y_lbl_0, y_lbl_10, y_lbl_20)

        # Curves
        curve_4  = make_curve(PTS_4,  CLR_4)
        curve_7  = make_curve(PTS_7,  CLR_7)
        curve_10 = make_curve(PTS_10, CLR_10)

        # Doubling markers — vertical DashedLines
        # 4%: doubles at t≈17.6yr → y at $2000
        x_d4 = -5.0 + (17.6/30)*10   # 0.87
        y_2k  = -2.5 + (2000/20000)*5  # -2.0
        x_end_4, y_end_4, _ = to_xy(30, 3310)

        # 7%: doubles at t≈10.3yr
        x_d7 = -5.0 + (10.3/30)*10   # -1.57

        # 10%: doubles at t≈7.2yr
        x_d10 = -5.0 + (7.2/30)*10   # -2.6

        dline_4  = DashedLine((x_d4, -2.5,0),(x_d4,  y_2k,0), color=CLR_4,  stroke_width=1.5, dash_length=0.08)
        dline_7  = DashedLine((x_d7, -2.5,0),(x_d7,  y_2k,0), color=CLR_7,  stroke_width=1.5, dash_length=0.08)
        dline_10 = DashedLine((x_d10,-2.5,0),(x_d10, y_2k,0), color=CLR_10, stroke_width=1.5, dash_length=0.08)
        doubling_lines = VGroup(dline_4, dline_7, dline_10)

        # Doubling labels (small text near each doubling line)
        dlbl_4  = tick_label("2x@18yr", (x_d4+0.6,  y_2k+0.25,0), fontsize=14, color=CLR_4)
        dlbl_7  = tick_label("2x@10yr", (x_d7+0.6,  y_2k+0.25,0), fontsize=14, color=CLR_7)
        dlbl_10 = tick_label("2x@7yr",  (x_d10+0.55,y_2k+0.25,0), fontsize=14, color=CLR_10)
        doubling_labels = VGroup(dlbl_4, dlbl_7, dlbl_10)

        # Curve end labels (right side)
        x_end, y_end_4,  _ = to_xy(30, 3310)
        _, y_end_7,  _     = to_xy(30, 8117)
        _, y_end_10, _     = to_xy(30, 19837)

        lbl_4  = tick_label("4%: $3,310",   (4.0, y_end_4 + 0.2, 0), fontsize=17, color=CLR_4)
        lbl_7  = tick_label("7%: $8,117",   (4.0, y_end_7 + 0.2, 0), fontsize=17, color=CLR_7)
        lbl_10 = tick_label("10%: $19,837", (4.0, y_end_10- 0.25,0), fontsize=17, color=CLR_10)
        curve_labels = VGroup(lbl_4, lbl_7, lbl_10)

        # Verdict
        verdict_bg = Rectangle(width=7.5, height=0.4, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0).move_to((0,-3.2,0))
        verdict_txt = Text("10% earns 6x more than 4% over 30 years",
                           font_size=24, color=CRIMSON, weight=BOLD).move_to((0,-3.2,0))
        verdict_text = VGroup(verdict_bg, verdict_txt)

        # --- Sequence (7 play() calls) ---
        self.play(Write(title))
        self.play(
            FadeIn(x_axis), FadeIn(y_axis),
            FadeIn(tick_labels), FadeIn(axis_labels)
        )
        self.play(Create(curve_4))
        self.play(Create(curve_7))
        self.play(Create(curve_10))
        self.play(FadeIn(doubling_lines), Write(doubling_labels))
        self.play(Write(curve_labels), Write(verdict_text))
        self.wait(1)
