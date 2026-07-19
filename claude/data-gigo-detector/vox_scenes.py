import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
VERIFIED_CLR  = "#2A7A2A"
VERIFIABLE_CLR = "#8A6A00"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_GIGOChecklist(Scene):
    def construct(self):
        # state 1: title
        title_bg = Rectangle(width=10.0, height=0.65, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        title_bg.move_to([0, 3.2, 0])
        title = Text("GIGO Risk Assessment", font_size=36, color=INK)
        title.move_to([0, 3.2, 0])
        self.play(FadeIn(VGroup(title_bg, title)))
        self.wait(0.3)

        # assumptions: (label, status-text, color)
        assumptions = [
            ("No duplicate rows in dataset",    "VERIFIED",      VERIFIED_CLR),
            ("Sample is representative",        "UNVERIFIABLE",  CRIMSON),
            ("No temporal drift in features",   "VERIFIABLE",    VERIFIABLE_CLR),
            ("Normal distribution assumed",     "UNVERIFIABLE",  CRIMSON),
            ("No measurement error",            "UNVERIFIABLE",  CRIMSON),
            ("Variables are independent",       "VERIFIABLE",    VERIFIABLE_CLR),
        ]

        y_top = 2.1
        gap   = 0.72
        x_lbl = -1.0   # label center
        x_sta =  4.2   # status center

        # state 2: items 1–2
        grp_a = VGroup()
        for j in range(2):
            y = y_top - j * gap
            lbl_bg = Rectangle(width=7.5, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            lbl_bg.move_to([x_lbl, y, 0])
            lbl = Text(assumptions[j][0], font_size=17, color=INK)
            lbl.move_to([x_lbl, y, 0])
            sta_bg = Rectangle(width=2.6, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                                stroke_color=assumptions[j][2], stroke_width=1.5)
            sta_bg.move_to([x_sta, y, 0])
            sta = Text(assumptions[j][1], font_size=14, color=assumptions[j][2])
            sta.move_to([x_sta, y, 0])
            grp_a.add(lbl_bg, lbl, sta_bg, sta)
        self.play(FadeIn(grp_a), run_time=0.7)
        self.wait(0.25)

        # state 3: items 3–4
        grp_b = VGroup()
        for j in range(2, 4):
            y = y_top - j * gap
            lbl_bg = Rectangle(width=7.5, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            lbl_bg.move_to([x_lbl, y, 0])
            lbl = Text(assumptions[j][0], font_size=17, color=INK)
            lbl.move_to([x_lbl, y, 0])
            sta_bg = Rectangle(width=2.6, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                                stroke_color=assumptions[j][2], stroke_width=1.5)
            sta_bg.move_to([x_sta, y, 0])
            sta = Text(assumptions[j][1], font_size=14, color=assumptions[j][2])
            sta.move_to([x_sta, y, 0])
            grp_b.add(lbl_bg, lbl, sta_bg, sta)
        self.play(FadeIn(grp_b), run_time=0.7)
        self.wait(0.25)

        # state 4: items 5–6
        grp_c = VGroup()
        for j in range(4, 6):
            y = y_top - j * gap
            lbl_bg = Rectangle(width=7.5, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                                stroke_width=0, stroke_opacity=0)
            lbl_bg.move_to([x_lbl, y, 0])
            lbl = Text(assumptions[j][0], font_size=17, color=INK)
            lbl.move_to([x_lbl, y, 0])
            sta_bg = Rectangle(width=2.6, height=0.52, fill_color=CREAM, fill_opacity=1.0,
                                stroke_color=assumptions[j][2], stroke_width=1.5)
            sta_bg.move_to([x_sta, y, 0])
            sta = Text(assumptions[j][1], font_size=14, color=assumptions[j][2])
            sta.move_to([x_sta, y, 0])
            grp_c.add(lbl_bg, lbl, sta_bg, sta)
        self.play(FadeIn(grp_c), run_time=0.7)
        self.wait(0.25)

        # state 5: separator
        y_sep = y_top - 6 * gap - 0.15
        sep = Line([-5.5, y_sep, 0], [5.5, y_sep, 0], stroke_color=INK, stroke_width=1.0)
        self.play(FadeIn(sep), run_time=0.4)
        self.wait(0.1)

        # state 6: GIGO risk score
        y_bar = y_sep - 0.42
        bar_bg = Rectangle(width=5.5, height=0.42, fill_color=SLATE, fill_opacity=0.15,
                            stroke_width=0, stroke_opacity=0)
        bar_bg.move_to([0, y_bar, 0])
        fill_w = 5.5 * 0.50
        fill = Rectangle(width=fill_w, height=0.42, fill_color=CRIMSON, fill_opacity=0.85,
                          stroke_width=0, stroke_opacity=0)
        fill.move_to([-5.5/2 + fill_w/2, y_bar, 0])
        y_lbl = y_bar - 0.48
        lbl_bg2 = Rectangle(width=9.0, height=0.44, fill_color=CREAM, fill_opacity=1.0,
                              stroke_width=0, stroke_opacity=0)
        lbl_bg2.move_to([0, y_lbl, 0])
        lbl2 = Text("GIGO RISK: 3 of 6 assumptions unverifiable  (50%)",
                    font_size=17, color=CRIMSON)
        lbl2.move_to([0, y_lbl, 0])
        self.play(FadeIn(VGroup(bar_bg, fill, lbl_bg2, lbl2)), run_time=0.8)
        self.wait(1.0)
