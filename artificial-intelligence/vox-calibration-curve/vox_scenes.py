import sys, json, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,
    "B02": 8.5, "B04": 9.0, "B05": 8.5, "B07": 9.5,
    "B08": 10.0, "B09": 9.0, "B10": 9.5, "B11": 8.5, "B12": 9.0,
    "B13": 18.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _BS["beats"]
    })
except Exception:
    pass

# ── B01 — Title ───────────────────────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why an Accurate Model Can Still", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        t2 = Text("Lie Every Time It Says 99%", font=DISPLAY, color=CRIMSON, font_size=42, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# Shared reliability-diagram geometry for B07–B11
_OX, _OY = -3.5, -2.5   # bottom-left corner
_DW, _DH =  6.5,  4.5   # diagram width / height
_BINS = 5
_BW   = _DW / _BINS      # 1.3 per bin
# Bin x-centers (confidence midpoints 10, 30, 50, 70, 90 %)
_BXC  = [_OX + (i + 0.5) * _BW for i in range(_BINS)]
# Diagonal (calibrated) bar tops
_DIAG_Y = [_OY + c * _DH for c in [0.10, 0.30, 0.50, 0.70, 0.90]]
# Actual (overclaiming) bar tops
_ACT_Y  = [_OY + f * _DH for f in [0.10, 0.30, 0.48, 0.53, 0.66]]
# Bin colors: low = calibrated (teal), high = overclaiming (crimson)
_BCOL   = [TEAL, TEAL, TEAL, CRIMSON, CRIMSON]
_CLBLS  = ["0-20%", "20-40%", "40-60%", "60-80%", "80-100%"]


def _make_axes():
    xax = Line(np.array([_OX, _OY, 0]), np.array([_OX + _DW, _OY, 0]),
               color=SLATE, stroke_width=2.5)
    yax = Line(np.array([_OX, _OY, 0]), np.array([_OX, _OY + _DH, 0]),
               color=SLATE, stroke_width=2.5)
    return xax, yax


def _make_diagonal():
    return Line(np.array([_OX, _OY, 0]), np.array([_OX + _DW, _OY + _DH, 0]),
                color=TEAL, stroke_width=2.5)


def _freq_bar(i, heights, color):
    h = max(heights[i] - _OY, 0.05)
    bar = Rectangle(width=_BW * 0.68, height=h, color=color, fill_opacity=0.78)
    bar.set_stroke(width=0, opacity=0)
    bar.move_to(np.array([_BXC[i], _OY + h / 2, 0]))
    return bar


# ─── scenes ───────────────────────────────────────────────────────────────────

class B02_DashboardTrace(Scene):
    def construct(self):
        pct = Text("94%", font=DISPLAY, color=TEAL).scale(2.8).move_to(UP * 0.9)
        acc = Text("ACCURACY", font=DISPLAY, color=TEAL).scale(0.55).next_to(pct, DOWN, buff=0.15)
        bar = Rectangle(width=5.5, height=0.55, color=TEAL, fill_opacity=0.75)
        bar.set_stroke(width=0, opacity=0)
        bar.move_to(DOWN * 1.8)
        tag = Text("all metrics green", font=MONO, color=TEAL).scale(0.42).next_to(bar, DOWN, buff=0.2)
        self.play(GrowFromCenter(pct), run_time=0.9)
        self.play(FadeIn(acc))
        self.play(GrowFromEdge(bar, LEFT), run_time=1.8)
        self.play(FadeIn(tag))
        self.wait(max(0.3, DUR["B02"] - 5.2))


class B04_AccuracyVsConf(Scene):
    def construct(self):
        divider = Line(UP * 3.0, DOWN * 3.0, color=SLATE, stroke_width=2)
        left_chip  = LabelChip("ACCURACY",   accent=TEAL).move_to(LEFT * 3.0 + UP * 1.9)
        left_q     = Text("Did it get the label right?", font=SERIF, color=INK).scale(0.46).move_to(LEFT * 3.0 + UP * 0.85)
        left_a     = Text("YES  or  NO", font=MONO, color=TEAL).scale(0.52).move_to(LEFT * 3.0 + UP * 0.1)
        right_chip = LabelChip("CONFIDENCE", accent=CRIMSON).move_to(RIGHT * 3.0 + UP * 1.9)
        right_q    = Text("How certain was it?", font=SERIF, color=INK).scale(0.46).move_to(RIGHT * 3.0 + UP * 0.85)
        right_a    = Text("0%  to  100%", font=MONO, color=CRIMSON).scale(0.52).move_to(RIGHT * 3.0 + UP * 0.1)
        note = Text("Not the same question.", font=SERIF, color=INK).scale(0.5).move_to(DOWN * 2.4)
        self.play(Create(divider))
        self.play(FadeIn(left_chip), FadeIn(right_chip))
        self.play(FadeIn(left_q), FadeIn(right_q))
        self.play(FadeIn(left_a), FadeIn(right_a))
        self.play(FadeIn(note))
        self.wait(max(0.3, DUR["B04"] - 6.0))


class B05_NinetyNinePromise(Scene):
    def construct(self):
        conf = Text("99%", font=DISPLAY, color=CRIMSON).scale(3.0).move_to(UP * 1.3)
        conf_lbl = Text("model's stated confidence", font=MONO, color=INK).scale(0.42).next_to(conf, DOWN, buff=0.2)
        arrow_lbl = Text("means:", font=SERIF, color=SLATE).scale(0.48).move_to(DOWN * 0.45)
        promise = Text("99 of 100 similar cases should be positive", font=MONO, color=INK).scale(0.43).move_to(DOWN * 1.1)
        # dot grid: 10x10, dot 0 is crimson (the 1 miss), rest teal
        dots = VGroup()
        for r in range(10):
            for c in range(10):
                col = CRIMSON if (r == 9 and c == 9) else TEAL
                d = Dot(radius=0.125, color=col, fill_opacity=0.88)
                d.set_stroke(width=0, opacity=0)
                d.move_to(np.array([-2.25 + c * 0.5, -1.85 - r * 0.24, 0]))
                dots.add(d)
        self.play(GrowFromCenter(conf), run_time=0.9)
        self.play(FadeIn(conf_lbl))
        self.play(FadeIn(arrow_lbl), FadeIn(promise))
        self.play(Create(dots, lag_ratio=0.015), run_time=2.5)
        self.wait(max(0.3, DUR["B05"] - 6.2))


class B07_BlankDiagram(Scene):
    def construct(self):
        xax, yax = _make_axes()
        diag = _make_diagonal()
        # axis labels
        x_lbl = Text("stated confidence", font=MONO, color=SLATE).scale(0.38).move_to(
            np.array([_OX + _DW / 2, _OY - 0.45, 0]))
        y_lbl = Text("actual frequency", font=MONO, color=SLATE).scale(0.38).rotate(PI / 2).move_to(
            np.array([_OX - 0.55, _OY + _DH / 2, 0]))
        diag_lbl = SerifLabel("perfect calibration", accent=TEAL, size=24).move_to(
            np.array([1.5, 1.8, 0]))
        # tick marks at 0 and 100%
        t_lo_x = Text("0%",   font=MONO, color=SLATE).scale(0.32).move_to(np.array([_OX,       _OY - 0.28, 0]))
        t_hi_x = Text("100%", font=MONO, color=SLATE).scale(0.32).move_to(np.array([_OX + _DW, _OY - 0.28, 0]))
        t_lo_y = Text("0%",   font=MONO, color=SLATE).scale(0.32).move_to(np.array([_OX - 0.4, _OY,        0]))
        t_hi_y = Text("100%", font=MONO, color=SLATE).scale(0.32).move_to(np.array([_OX - 0.5, _OY + _DH, 0]))
        self.play(Create(xax), Create(yax))
        self.play(FadeIn(x_lbl), FadeIn(y_lbl))
        self.play(FadeIn(t_lo_x), FadeIn(t_hi_x), FadeIn(t_lo_y), FadeIn(t_hi_y))
        self.play(Create(diag), run_time=1.8)
        self.play(FadeIn(diag_lbl))
        self.wait(max(0.3, DUR["B07"] - 7.0))


class B08_PredictionsAccum(Scene):
    def construct(self):
        xax, yax = _make_axes()
        self.add(xax, yax)
        # uniform prediction count bars (same height = roughly equal predictions per bin)
        pred_h = 2.8  # height of each prediction-count bar
        bars = VGroup()
        lbls = VGroup()
        for i in range(_BINS):
            bar = Rectangle(width=_BW * 0.68, height=pred_h, color=SLATE, fill_opacity=0.35)
            bar.set_stroke(width=0, opacity=0)
            bar.move_to(np.array([_BXC[i], _OY + pred_h / 2, 0]))
            bars.add(bar)
            lbl = Text(_CLBLS[i], font=MONO, color=SLATE).scale(0.3).move_to(
                np.array([_BXC[i], _OY - 0.3, 0]))
            lbls.add(lbl)
        count_lbl = Text("predictions per bin", font=MONO, color=SLATE).scale(0.36).move_to(
            np.array([_OX + _DW / 2, _OY + pred_h + 0.35, 0]))
        self.play(FadeIn(lbls))
        for i in range(_BINS):
            self.play(GrowFromEdge(bars[i], DOWN), run_time=0.7)
        self.play(FadeIn(count_lbl))
        self.wait(max(0.3, DUR["B08"] - 6.5))


class B09_CalibContract(Scene):
    def construct(self):
        _quote_scene(
            self,
            "If the model says ‘seventy percent confident’ on a thousand cases, "
            "you want roughly seven hundred of those cases to turn out positive.",
            "Computational Skepticism for AI, Chapter 2",
            None,
            "seven hundred",
            DUR["B09"],
        )


class B10_OutcomesAccum(Scene):
    def construct(self):
        xax, yax = _make_axes()
        diag = _make_diagonal()
        self.add(xax, yax, diag)
        bars = VGroup()
        freq_lbls = VGroup()
        conf_lbls = VGroup()
        freq_pcts = ["10%", "30%", "48%", "53%", "66%"]
        for i in range(_BINS):
            bar = _freq_bar(i, _ACT_Y, _BCOL[i])
            bars.add(bar)
            # actual frequency label above bar
            f_lbl = Text(freq_pcts[i], font=MONO, color=_BCOL[i]).scale(0.33).move_to(
                np.array([_BXC[i], _ACT_Y[i] + 0.28, 0]))
            freq_lbls.add(f_lbl)
            # confidence bin label below axis
            c_lbl = Text(_CLBLS[i], font=MONO, color=SLATE).scale(0.28).move_to(
                np.array([_BXC[i], _OY - 0.3, 0]))
            conf_lbls.add(c_lbl)
        self.play(FadeIn(conf_lbls))
        for i in range(_BINS):
            self.play(GrowFromEdge(bars[i], DOWN), FadeIn(freq_lbls[i]), run_time=0.85)
        self.wait(max(0.3, DUR["B10"] - 6.5))


class B11_CalibCurve(Scene):
    def construct(self):
        xax, yax = _make_axes()
        diag = _make_diagonal()
        # actual-frequency bars (background context)
        bars = VGroup(*[_freq_bar(i, _ACT_Y, _BCOL[i]) for i in range(_BINS)])
        self.add(xax, yax, diag, bars)
        # dots at top of each actual bar
        dots = VGroup()
        for i in range(_BINS):
            d = Dot(radius=0.14, color=_BCOL[i], fill_opacity=1.0)
            d.set_stroke(width=0, opacity=0)
            d.move_to(np.array([_BXC[i], _ACT_Y[i], 0]))
            dots.add(d)
        # empirical curve: teal for first 3 points, crimson for last 3 (overlap at midpoint)
        def _seg(pts, color):
            vm = VMobject()
            vm.set_points_as_corners([np.array([x, y, 0]) for x, y in pts])
            vm.set_color(color)
            vm.set_stroke(width=3.5)
            vm.set_fill(opacity=0)
            return vm
        curve_teal = _seg(
            [(x, y) for x, y in zip(_BXC[:3], _ACT_Y[:3])], TEAL)
        curve_crim = _seg(
            [(x, y) for x, y in zip(_BXC[2:], _ACT_Y[2:])], CRIMSON)
        # label for the peel
        peel_lbl = SerifLabel("overclaims here", accent=CRIMSON, size=24).move_to(
            np.array([2.1, 0.9, 0]))
        self.play(Create(dots, lag_ratio=0.15))
        self.play(Create(curve_teal), run_time=1.2)
        self.play(Create(curve_crim), run_time=1.2)
        self.play(FadeIn(peel_lbl))
        self.wait(max(0.3, DUR["B11"] - 5.5))


class B12_QuoteFluent(Scene):
    def construct(self):
        _quote_scene(
            self,
            "A net will say ‘99%’ when it should say ‘85%,’ "
            "and it will say it fluently.",
            "Computational Skepticism for AI, Chapter 2",
            None,
            "fluently",
            DUR["B12"],
        )


# ── B13 — ExampleCalib (THE EXAMPLE) ─────────────────────────────────────────

class B13_ExampleCalib(Scene):
    def construct(self):
        total = DUR["B13"]

        title = Text("Count What Actually Happened", font=DISPLAY, font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.0, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.0 + DOWN * 0.1)
        col_r = Rectangle(width=5.0, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.0 + DOWN * 0.1)

        lbl_l = Text("MODEL SAID", font=DISPLAY, font_size=18, color=TEAL).move_to(LEFT * 3.0 + UP * 1.55)
        lbl_r = Text("REALITY", font=DISPLAY, font_size=18, color=CRIMSON).move_to(RIGHT * 3.0 + UP * 1.55)

        n_cases  = Text("400 patients", font="PT Mono", font_size=16, color=INK).move_to(LEFT * 3.0 + UP * 0.75)
        conf_out = Text("99% confident", font="PT Mono", font_size=20, color=TEAL, weight=BOLD).move_to(LEFT * 3.0 + UP * 0.0)
        label_l  = Text("each case: essentially certain", font=DISPLAY, font_size=14, color=INK).move_to(LEFT * 3.0 + DOWN * 0.75)

        actual_n = Text("310 of 400 had condition", font="PT Mono", font_size=16, color=INK).move_to(RIGHT * 3.0 + UP * 0.75)
        rate_out = Text("77% actual rate", font="PT Mono", font_size=20, color=CRIMSON, weight=BOLD).move_to(RIGHT * 3.0 + UP * 0.0)
        label_r  = Text("not 99 — less than 4 in 5", font=DISPLAY, font_size=14, color=CRIMSON).move_to(RIGHT * 3.0 + DOWN * 0.75)

        note = Text("Precise score. Wrong claim.", font=DISPLAY, font_size=17, color=INK).move_to(DOWN * 2.5)
        note_rect = Rectangle(width=7.0, height=0.5, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.5)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.6)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(n_cases), Write(actual_n), run_time=0.4)
        self.play(FadeIn(conf_out), FadeIn(rate_out), run_time=0.5)
        self.play(Write(label_l), Write(label_r), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.3)
        self.play(Write(note), run_time=0.4)
        self.wait(max(0.5, total - 4.5))
