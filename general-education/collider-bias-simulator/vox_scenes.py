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


# Pre-computed dot positions (deterministic, no random()) — 60 total
# Left panel: x in [-4.8, -0.7], y in [-2.5, 2.2]
# 50 SLATE dots (neither disease), 5 GOLD dots (disease A only), 5 CRIMSON dots (disease B only)
_LEFT_SLATE = [
    (-4.5, 2.0), (-4.2, 1.5), (-3.9, 2.1), (-3.6, 1.8), (-3.3, 2.0),
    (-4.4, 1.1), (-4.1, 0.8), (-3.8, 1.3), (-3.5, 1.0), (-3.2, 1.4),
    (-4.6, 0.2), (-4.3, -0.1), (-4.0, 0.4), (-3.7, 0.1), (-3.4, 0.5),
    (-4.5, -0.7), (-4.2, -1.0), (-3.9, -0.5), (-3.6, -0.8), (-3.3, -0.4),
    (-4.4, -1.6), (-4.1, -1.9), (-3.8, -1.4), (-3.5, -1.7), (-3.2, -1.3),
    (-4.7, -2.3), (-4.4, -2.4), (-4.1, -2.2), (-3.8, -2.4), (-3.5, -2.3),
    (-2.9, 2.0), (-2.6, 1.6), (-2.3, 2.1), (-2.0, 1.8), (-1.7, 2.0),
    (-2.8, 1.1), (-2.5, 0.7), (-2.2, 1.2), (-1.9, 0.9), (-1.6, 1.3),
    (-2.7, 0.1), (-2.4, -0.2), (-2.1, 0.3), (-1.8, 0.0), (-1.5, 0.4),
    (-2.6, -0.9), (-2.3, -1.2), (-2.0, -0.7), (-1.7, -1.0), (-1.4, -0.6),
]
_LEFT_GOLD = [
    (-4.0, -1.0), (-3.0, 0.5), (-2.0, -2.0), (-1.5, 1.5), (-4.5, 0.0),
]
_LEFT_CRIMSON = [
    (-3.5, -2.0), (-2.5, 1.0), (-1.8, -1.5), (-4.2, 1.8), (-2.8, -0.5),
]

# Right panel: hospital subset — GOLD and CRIMSON dots only, x shifted to [0.7, 5.3]
_RIGHT_GOLD = [
    (1.0, 1.2), (1.8, 0.5), (2.6, -0.3), (3.4, -1.0), (4.2, -1.7),
]
_RIGHT_CRIMSON = [
    (1.2, 0.8), (2.0, 0.1), (2.8, -0.6), (3.6, -1.3), (4.4, -2.0),
]
# Additional mixed dots for hospital panel (10 more)
_RIGHT_EXTRA_GOLD = [
    (1.5, 1.5), (2.3, 0.8), (3.1, 0.0), (3.9, -0.7), (4.7, -1.4),
]
_RIGHT_EXTRA_CRIMSON = [
    (1.7, 0.3), (2.5, -0.4), (3.3, -1.1), (4.1, -1.8), (4.9, -2.4),
]


class B04_BerksonClouds(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # Title
        title = Text("BERKSON'S PARADOX", color=INK, weight=BOLD, font_size=38)
        title.move_to([0, 3.2, 0])

        # Dividing line
        divider_line = Line(start=[0.0, -3.2, 0], end=[0.0, 3.0, 0],
                            color=SLATE, stroke_width=2)

        # Panel labels
        left_label = Text("FULL POPULATION", color=INK, weight=BOLD, font_size=30)
        left_label.move_to([-2.8, 2.8, 0])
        right_label = Text("HOSPITAL SUBSET", color=CRIMSON, weight=BOLD, font_size=30)
        right_label.move_to([2.8, 2.8, 0])

        # LEFT panel dots
        left_dots = VGroup()
        for (x, y) in _LEFT_SLATE:
            d = Dot(point=[x, y, 0], radius=0.06, color=SLATE)
            left_dots.add(d)
        for (x, y) in _LEFT_GOLD:
            d = Dot(point=[x, y, 0], radius=0.09, color=GOLD)
            left_dots.add(d)
        for (x, y) in _LEFT_CRIMSON:
            d = Dot(point=[x, y, 0], radius=0.09, color=CRIMSON)
            left_dots.add(d)
        full_pop_dots = left_dots

        # Left correlation label
        left_corr_bg = Rectangle(width=3.2, height=0.35, fill_color=CREAM,
                                  fill_opacity=1, stroke_width=0, stroke_opacity=0)
        left_corr_bg.move_to([-2.8, -2.9, 0])
        left_corr_txt = Text("correlation: rho = 0.02", color=SLATE, font_size=26)
        left_corr_txt.move_to([-2.8, -2.9, 0])
        left_corr_label = VGroup(left_corr_bg, left_corr_txt)

        # RIGHT panel dots
        right_dots = VGroup()
        for (x, y) in _RIGHT_GOLD + _RIGHT_EXTRA_GOLD:
            d = Dot(point=[x, y, 0], radius=0.09, color=GOLD)
            right_dots.add(d)
        for (x, y) in _RIGHT_CRIMSON + _RIGHT_EXTRA_CRIMSON:
            d = Dot(point=[x, y, 0], radius=0.09, color=CRIMSON)
            right_dots.add(d)
        hospital_dots = right_dots

        # Trend line (downward slope: top-left to bottom-right)
        trend_line = Line(start=[0.7, 1.5, 0], end=[5.3, -1.5, 0],
                          color=CRIMSON, stroke_width=3)

        # Right correlation label
        right_corr_bg = Rectangle(width=3.8, height=0.35, fill_color=CREAM,
                                   fill_opacity=1, stroke_width=0, stroke_opacity=0)
        right_corr_bg.move_to([2.8, -2.9, 0])
        right_corr_txt = Text("correlation: rho = -0.42", color=CRIMSON, weight=BOLD, font_size=26)
        right_corr_txt.move_to([2.8, -2.9, 0])
        right_corr_label = VGroup(right_corr_bg, right_corr_txt)

        # Sequence — 6 play() calls
        self.play(Write(title))
        self.play(Write(divider_line), Write(left_label), Write(right_label))
        self.play(FadeIn(full_pop_dots))
        self.play(Write(left_corr_label))
        self.play(FadeIn(hospital_dots), FadeIn(trend_line))
        self.play(Write(right_corr_label))
        self.wait(1)
