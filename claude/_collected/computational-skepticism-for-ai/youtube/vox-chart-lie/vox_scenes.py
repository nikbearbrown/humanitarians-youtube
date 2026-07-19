import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))

from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,  "B02": 11.0, "B04": 10.0, "B05": 9.0,
    "B07": 9.0,  "B08": 8.0,  "B09": 10.0,
    "B10": 8.0,  "B11": 8.0,  "B12": 18.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ── B01 — Title ──────────────────────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Watch Me Lie With a Chart", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        t2 = Text("Without Changing a Single Number", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── Shared chart constants ────────────────────────────────────────────────────
_YB      = -2.4   # y-coordinate of bar baseline
_BW      = 1.0    # bar width
_CHF     = 4.0    # chart height for full (0-100%) scale → pixels per 100%


def _bar(x_center, pct, scale_h, y_bot, color, opacity=0.75):
    h = scale_h * pct / 100.0
    r = Rectangle(width=_BW, height=max(h, 0.05),
                  color=color, fill_color=color, fill_opacity=opacity, stroke_width=0)
    r.move_to([x_center, y_bot + h / 2, 0])
    return r


def _axis(x_left, x_right, y_bot, chart_h, color=INK):
    x_ax = Line([x_left - 0.3, y_bot, 0], [x_right + 0.3, y_bot, 0], color=color, stroke_width=2)
    y_ax = Line([x_left - 0.3, y_bot, 0], [x_left - 0.3, y_bot + chart_h + 0.3, 0], color=color, stroke_width=2)
    return x_ax, y_ax


# ── B02 — HonestChart ─────────────────────────────────────────────────────────

class B02_HonestChart(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("The Honest Chart", font=DISPLAY, font_size=22, color=TEAL).move_to(UP * 3.2)

        # Full scale chart (0-100%)
        x_A, x_B = -1.4, 1.4
        x_ax, y_ax = _axis(x_A - 0.7, x_B + 0.7, _YB, _CHF)

        bar_A = _bar(x_A, 55, _CHF, _YB, SLATE)
        bar_B = _bar(x_B, 48, _CHF, _YB, SLATE)

        lbl_A = Text("Group A\n55%", font=MONO, font_size=16, color=INK).move_to([x_A, _YB - 0.55, 0])
        lbl_B = Text("Group B\n48%", font=MONO, font_size=16, color=INK).move_to([x_B, _YB - 0.55, 0])

        # y-axis label at 0%
        y0_lbl  = Text("0%",   font=MONO, font_size=13, color=INK).move_to([x_A - 1.0, _YB,         0])
        y50_lbl = Text("50%",  font=MONO, font_size=13, color=INK).move_to([x_A - 1.0, _YB + 2.0,  0])
        y100_lbl = Text("100%", font=MONO, font_size=13, color=INK).move_to([x_A - 1.0, _YB + _CHF, 0])

        # Error bars ±5 pct
        err_h = _CHF * 0.05
        eb_A_top  = Line([x_A - 0.25, _YB + _CHF * 0.55 + err_h, 0], [x_A + 0.25, _YB + _CHF * 0.55 + err_h, 0], color=INK, stroke_width=2)
        eb_A_bot  = Line([x_A - 0.25, _YB + _CHF * 0.55 - err_h, 0], [x_A + 0.25, _YB + _CHF * 0.55 - err_h, 0], color=INK, stroke_width=2)
        eb_A_mid  = Line([x_A, _YB + _CHF * 0.55 - err_h, 0], [x_A, _YB + _CHF * 0.55 + err_h, 0], color=INK, stroke_width=2)
        eb_B_top  = Line([x_B - 0.25, _YB + _CHF * 0.48 + err_h, 0], [x_B + 0.25, _YB + _CHF * 0.48 + err_h, 0], color=INK, stroke_width=2)
        eb_B_bot  = Line([x_B - 0.25, _YB + _CHF * 0.48 - err_h, 0], [x_B + 0.25, _YB + _CHF * 0.48 - err_h, 0], color=INK, stroke_width=2)
        eb_B_mid  = Line([x_B, _YB + _CHF * 0.48 - err_h, 0], [x_B, _YB + _CHF * 0.48 + err_h, 0], color=INK, stroke_width=2)

        caption = Text("Zero baseline · equal colors · error bars shown", font=DISPLAY, font_size=16, color=TEAL).move_to(DOWN * 3.2)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromEdge(x_ax, LEFT), GrowFromEdge(y_ax, DOWN), run_time=0.5)
        self.play(Write(y0_lbl), Write(y50_lbl), Write(y100_lbl), run_time=0.4)
        self.play(GrowFromEdge(bar_A, DOWN), GrowFromEdge(bar_B, DOWN), run_time=0.7)
        self.play(Write(lbl_A), Write(lbl_B), run_time=0.4)
        self.play(
            GrowFromCenter(eb_A_top), GrowFromCenter(eb_A_bot), GrowFromCenter(eb_A_mid),
            GrowFromCenter(eb_B_top), GrowFromCenter(eb_B_bot), GrowFromCenter(eb_B_mid),
            run_time=0.5,
        )
        self.play(Write(caption), run_time=0.4)
        self.wait(DUR["B02"] - 4.3)


# ── B04 — Move1 (truncated axis) ──────────────────────────────────────────────

class B04_Move1(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Left: honest (full 0-100%)
        # Right: truncated (44-60%)
        _CL, _CR = -3.6, 3.6
        _xOff = 0.8   # bar offset from chart center
        _ch   = 3.2   # chart display height

        lbl_hon   = Text("HONEST\n(y: 0–100%)", font=DISPLAY, font_size=16, color=TEAL).move_to([_CL, 2.8, 0])
        lbl_trunc = Text("TRUNCATED\n(y: 44–60%)", font=DISPLAY, font_size=16, color=CRIMSON).move_to([_CR, 2.8, 0])

        # Honest bars (0-100%)
        h_A_h = _ch * 0.55
        h_B_h = _ch * 0.48
        bar_A_h = Rectangle(width=0.9, height=h_A_h, color=SLATE, fill_color=SLATE, fill_opacity=0.75, stroke_width=0)
        bar_B_h = Rectangle(width=0.9, height=h_B_h, color=SLATE, fill_color=SLATE, fill_opacity=0.75, stroke_width=0)
        bar_A_h.move_to([_CL - _xOff, _YB + h_A_h / 2, 0])
        bar_B_h.move_to([_CL + _xOff, _YB + h_B_h / 2, 0])

        ax_hon_x = Line([_CL - 1.2, _YB, 0], [_CL + 1.2, _YB, 0], color=INK, stroke_width=1.5)
        ax_hon_y = Line([_CL - 1.2, _YB, 0], [_CL - 1.2, _YB + _ch + 0.2, 0], color=INK, stroke_width=1.5)
        y0h = Text("0%",   font=MONO, font_size=11, color=INK).move_to([_CL - 1.9, _YB,         0])
        y100h = Text("100%", font=MONO, font_size=11, color=INK).move_to([_CL - 1.9, _YB + _ch, 0])

        # Truncated bars (44-60%)
        h_A_t = _ch * (0.55 - 0.44) / 0.16   # 11/16 = 0.6875
        h_B_t = _ch * (0.48 - 0.44) / 0.16   # 4/16 = 0.25
        bar_A_t = Rectangle(width=0.9, height=h_A_t, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.75, stroke_width=0)
        bar_B_t = Rectangle(width=0.9, height=h_B_t, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.75, stroke_width=0)
        bar_A_t.move_to([_CR - _xOff, _YB + h_A_t / 2, 0])
        bar_B_t.move_to([_CR + _xOff, _YB + h_B_t / 2, 0])

        ax_tr_x = Line([_CR - 1.2, _YB, 0], [_CR + 1.2, _YB, 0], color=INK, stroke_width=1.5)
        ax_tr_y = Line([_CR - 1.2, _YB, 0], [_CR - 1.2, _YB + _ch + 0.2, 0], color=INK, stroke_width=1.5)
        y44 = Text("44%", font=MONO, font_size=11, color=INK).move_to([_CR - 1.9, _YB,         0])
        y60 = Text("60%", font=MONO, font_size=11, color=INK).move_to([_CR - 1.9, _YB + _ch, 0])

        note = Text("Same data. The gap now looks like a wall.", font=DISPLAY, font_size=16, color=GOLD).move_to(DOWN * 3.2)

        self.play(Write(lbl_hon), Write(lbl_trunc), run_time=0.5)
        self.play(
            GrowFromEdge(ax_hon_x, LEFT), GrowFromEdge(ax_hon_y, DOWN),
            GrowFromEdge(ax_tr_x, LEFT), GrowFromEdge(ax_tr_y, DOWN),
            run_time=0.5,
        )
        self.play(Write(y0h), Write(y100h), Write(y44), Write(y60), run_time=0.4)
        self.play(
            GrowFromEdge(bar_A_h, DOWN), GrowFromEdge(bar_B_h, DOWN),
            GrowFromEdge(bar_A_t, DOWN), GrowFromEdge(bar_B_t, DOWN),
            run_time=0.7,
        )
        self.play(Write(note), run_time=0.5)
        self.wait(DUR["B04"] - 4.0)


# ── B05 — Move2 (color asymmetry) ────────────────────────────────────────────

class B05_Move2(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        _CL, _CR = -3.6, 3.6
        _xOff = 0.8
        _ch   = 3.2

        lbl_left  = Text("EQUAL COLORS\n(neutral)", font=DISPLAY, font_size=16, color=TEAL).move_to([_CL, 2.8, 0])
        lbl_right = Text("COLOR ASYMMETRY\n(attentional tilt)", font=DISPLAY, font_size=16, color=CRIMSON).move_to([_CR, 2.8, 0])

        h_A = _ch * 0.55
        h_B = _ch * 0.48

        # Left: both SLATE
        bar_AL = Rectangle(width=0.9, height=h_A, color=SLATE, fill_color=SLATE, fill_opacity=0.75, stroke_width=0)
        bar_BL = Rectangle(width=0.9, height=h_B, color=SLATE, fill_color=SLATE, fill_opacity=0.75, stroke_width=0)
        bar_AL.move_to([_CL - _xOff, _YB + h_A / 2, 0])
        bar_BL.move_to([_CL + _xOff, _YB + h_B / 2, 0])

        ax_L_x = Line([_CL - 1.2, _YB, 0], [_CL + 1.2, _YB, 0], color=INK, stroke_width=1.5)
        ax_L_y = Line([_CL - 1.2, _YB, 0], [_CL - 1.2, _YB + _ch + 0.2, 0], color=INK, stroke_width=1.5)

        # Right: A = TEAL (salient), B = SLATE (faded)
        bar_AR = Rectangle(width=0.9, height=h_A, color=TEAL, fill_color=TEAL, fill_opacity=0.85, stroke_width=0)
        bar_BR = Rectangle(width=0.9, height=h_B, color=SLATE, fill_color=SLATE, fill_opacity=0.3, stroke_width=0)
        bar_AR.move_to([_CR - _xOff, _YB + h_A / 2, 0])
        bar_BR.move_to([_CR + _xOff, _YB + h_B / 2, 0])

        ax_R_x = Line([_CR - 1.2, _YB, 0], [_CR + 1.2, _YB, 0], color=INK, stroke_width=1.5)
        ax_R_y = Line([_CR - 1.2, _YB, 0], [_CR - 1.2, _YB + _ch + 0.2, 0], color=INK, stroke_width=1.5)

        note = Text("Same data. The eye goes where the color says to go.", font=DISPLAY, font_size=16, color=GOLD).move_to(DOWN * 3.2)

        self.play(Write(lbl_left), Write(lbl_right), run_time=0.5)
        self.play(
            GrowFromEdge(ax_L_x, LEFT), GrowFromEdge(ax_L_y, DOWN),
            GrowFromEdge(ax_R_x, LEFT), GrowFromEdge(ax_R_y, DOWN),
            run_time=0.5,
        )
        self.play(
            GrowFromEdge(bar_AL, DOWN), GrowFromEdge(bar_BL, DOWN),
            GrowFromEdge(bar_AR, DOWN), GrowFromEdge(bar_BR, DOWN),
            run_time=0.7,
        )
        self.play(Write(note), run_time=0.5)
        self.wait(DUR["B05"] - 3.5)


# ── B07 — Move3 (error bars) ──────────────────────────────────────────────────

class B07_Move3(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        _CL, _CR = -3.6, 3.6
        _xOff = 0.8
        _ch   = 3.2
        err_h = _ch * 0.05

        lbl_left  = Text("WITH ERROR BARS\n(±5%)", font=DISPLAY, font_size=16, color=TEAL).move_to([_CL, 2.8, 0])
        lbl_right = Text("ERROR BARS HIDDEN\n(false precision)", font=DISPLAY, font_size=16, color=CRIMSON).move_to([_CR, 2.8, 0])

        h_A = _ch * 0.55
        h_B = _ch * 0.48

        def _bars_and_axes(x_c, bar_col, eb_col=INK):
            ba = Rectangle(width=0.9, height=h_A, color=bar_col, fill_color=bar_col, fill_opacity=0.75, stroke_width=0)
            bb = Rectangle(width=0.9, height=h_B, color=bar_col, fill_color=bar_col, fill_opacity=0.75, stroke_width=0)
            ba.move_to([x_c - _xOff, _YB + h_A / 2, 0])
            bb.move_to([x_c + _xOff, _YB + h_B / 2, 0])
            x_ax = Line([x_c - 1.2, _YB, 0], [x_c + 1.2, _YB, 0], color=INK, stroke_width=1.5)
            y_ax = Line([x_c - 1.2, _YB, 0], [x_c - 1.2, _YB + _ch + 0.2, 0], color=INK, stroke_width=1.5)
            y_A = _YB + h_A
            y_B = _YB + h_B
            eb_A = VGroup(
                Line([x_c - _xOff - 0.2, y_A + err_h, 0], [x_c - _xOff + 0.2, y_A + err_h, 0], color=eb_col, stroke_width=2),
                Line([x_c - _xOff - 0.2, y_A - err_h, 0], [x_c - _xOff + 0.2, y_A - err_h, 0], color=eb_col, stroke_width=2),
                Line([x_c - _xOff, y_A - err_h, 0], [x_c - _xOff, y_A + err_h, 0], color=eb_col, stroke_width=2),
            )
            eb_B = VGroup(
                Line([x_c + _xOff - 0.2, y_B + err_h, 0], [x_c + _xOff + 0.2, y_B + err_h, 0], color=eb_col, stroke_width=2),
                Line([x_c + _xOff - 0.2, y_B - err_h, 0], [x_c + _xOff + 0.2, y_B - err_h, 0], color=eb_col, stroke_width=2),
                Line([x_c + _xOff, y_B - err_h, 0], [x_c + _xOff, y_B + err_h, 0], color=eb_col, stroke_width=2),
            )
            return ba, bb, x_ax, y_ax, eb_A, eb_B

        ba_L, bb_L, ax_Lx, ax_Ly, eb_AL, eb_BL = _bars_and_axes(_CL, SLATE)
        ba_R, bb_R, ax_Rx, ax_Ry, eb_AR, eb_BR = _bars_and_axes(_CR, SLATE)

        note = Text("Confidence intervals overlap: may be no real difference.", font=DISPLAY, font_size=15, color=GOLD).move_to(DOWN * 3.2)

        self.play(Write(lbl_left), Write(lbl_right), run_time=0.5)
        self.play(
            GrowFromEdge(ax_Lx, LEFT), GrowFromEdge(ax_Ly, DOWN),
            GrowFromEdge(ax_Rx, LEFT), GrowFromEdge(ax_Ry, DOWN),
            run_time=0.5,
        )
        self.play(
            GrowFromEdge(ba_L, DOWN), GrowFromEdge(bb_L, DOWN),
            GrowFromEdge(ba_R, DOWN), GrowFromEdge(bb_R, DOWN),
            run_time=0.7,
        )
        self.play(GrowFromCenter(eb_AL), GrowFromCenter(eb_BL), run_time=0.5)
        # Right chart has no error bars (deliberately absent — that's the point)
        self.play(Write(note), run_time=0.5)
        self.wait(DUR["B07"] - 3.7)


# ── B08 — QuoteArgument ───────────────────────────────────────────────────────

class B08_QuoteArgument(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Visualization is not transparent communication of facts. "
            "It is an argument, made through structural choices, about "
            "what the facts mean and how the reader should weight them. "
            "Engineers undercredit this — and produce many of the most "
            "misleading dashboards in deployment without intending to mislead.",
            "Computational Skepticism for AI, Chapter 10",
            None,
            "structural choices",
            DUR["B08"],
        )


# ── B09 — AllThree ────────────────────────────────────────────────────────────

class B09_AllThree(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        _CL, _CR = -3.6, 3.6
        _xOff = 0.8
        _ch   = 3.2

        lbl_left  = Text("HONEST CHART", font=DISPLAY, font_size=18, color=TEAL).move_to([_CL, 2.8, 0])
        lbl_right = Text("AFTER ALL THREE MOVES", font=DISPLAY, font_size=18, color=CRIMSON).move_to([_CR, 2.8, 0])

        h_A_h = _ch * 0.55
        h_B_h = _ch * 0.48
        h_A_t = _ch * (0.55 - 0.44) / 0.16
        h_B_t = _ch * (0.48 - 0.44) / 0.16

        # Honest bars
        ba_h = Rectangle(width=0.9, height=h_A_h, color=SLATE, fill_color=SLATE, fill_opacity=0.75, stroke_width=0)
        bb_h = Rectangle(width=0.9, height=h_B_h, color=SLATE, fill_color=SLATE, fill_opacity=0.75, stroke_width=0)
        ba_h.move_to([_CL - _xOff, _YB + h_A_h / 2, 0])
        bb_h.move_to([_CL + _xOff, _YB + h_B_h / 2, 0])
        ax_Hx = Line([_CL - 1.2, _YB, 0], [_CL + 1.2, _YB, 0], color=INK, stroke_width=1.5)
        ax_Hy = Line([_CL - 1.2, _YB, 0], [_CL - 1.2, _YB + _ch + 0.2, 0], color=INK, stroke_width=1.5)
        y0h  = Text("0%",   font=MONO, font_size=11, color=INK).move_to([_CL - 1.9, _YB, 0])
        y100h = Text("100%", font=MONO, font_size=11, color=INK).move_to([_CL - 1.9, _YB + _ch, 0])

        # Misleading bars (truncated + color asymmetry)
        ba_m = Rectangle(width=0.9, height=h_A_t, color=TEAL, fill_color=TEAL, fill_opacity=0.85, stroke_width=0)
        bb_m = Rectangle(width=0.9, height=h_B_t, color=SLATE, fill_color=SLATE, fill_opacity=0.30, stroke_width=0)
        ba_m.move_to([_CR - _xOff, _YB + h_A_t / 2, 0])
        bb_m.move_to([_CR + _xOff, _YB + h_B_t / 2, 0])
        ax_Mx = Line([_CR - 1.2, _YB, 0], [_CR + 1.2, _YB, 0], color=INK, stroke_width=1.5)
        ax_My = Line([_CR - 1.2, _YB, 0], [_CR - 1.2, _YB + _ch + 0.2, 0], color=INK, stroke_width=1.5)
        y44m  = Text("44%", font=MONO, font_size=11, color=INK).move_to([_CR - 1.9, _YB, 0])
        y60m  = Text("60%", font=MONO, font_size=11, color=INK).move_to([_CR - 1.9, _YB + _ch, 0])

        note = Text("Same CSV. Same numbers. Two different arguments.", font=DISPLAY, font_size=16, color=GOLD).move_to(DOWN * 3.2)

        self.play(Write(lbl_left), Write(lbl_right), run_time=0.5)
        self.play(
            GrowFromEdge(ax_Hx, LEFT), GrowFromEdge(ax_Hy, DOWN),
            GrowFromEdge(ax_Mx, LEFT), GrowFromEdge(ax_My, DOWN),
            run_time=0.5,
        )
        self.play(Write(y0h), Write(y100h), Write(y44m), Write(y60m), run_time=0.4)
        self.play(
            GrowFromEdge(ba_h, DOWN), GrowFromEdge(bb_h, DOWN),
            GrowFromEdge(ba_m, DOWN), GrowFromEdge(bb_m, DOWN),
            run_time=0.7,
        )
        self.play(Write(note), run_time=0.5)
        self.wait(DUR["B09"] - 4.1)


# ── B10 — QuoteChoice ────────────────────────────────────────────────────────

class B10_QuoteChoice(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Every one of these moves has an honest use — which is "
            "exactly why they are dangerous. The chart looks the same "
            "whether the choice was honest or not. The choice is the "
            "difference — not anything visible in the pixels.",
            "Computational Skepticism for AI, Chapter 10",
            None,
            "The choice is the difference",
            DUR["B10"],
        )


# ── B11 — Catalog ─────────────────────────────────────────────────────────────

class B11_Catalog(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Three Moves — Three Arguments", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)

        catalog = [
            ("TRUNCATED AXIS",         "amplifies a real effect — makes small differences look large", CRIMSON),
            ("COLOR ASYMMETRY",        "directs attention without the reader's awareness",              CRIMSON),
            ("SELECTIVE UNCERTAINTY",  "shows confidence intervals only where they support the argument", CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, desc, col) in enumerate(catalog):
            y = 1.5 - i * 1.5
            box = Rectangle(width=10.5, height=1.1, color=col, fill_color=col, fill_opacity=0.10, stroke_width=1.8).move_to(UP * y)
            lbl = Text(f"{name}", font=DISPLAY, font_size=18, color=col).move_to([0.0, y + 0.2, 0])
            desc_txt = Text(desc, font=MONO, font_size=14, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(desc_txt), run_time=0.35)

        note = Text("None is illegal. All are arguments made through structure.", font=DISPLAY, font_size=16, color=GOLD).move_to(DOWN * 2.7)
        self.play(Write(note), run_time=0.5)
        self.wait(DUR["B11"] - 4.3)


# ── B12 — ExampleRetention ────────────────────────────────────────────────────

class B12_ExampleRetention(Scene):
    def construct(self):
        total = DUR["B12"]
        title = Text("Same Numbers — Two Stories", font=DISPLAY, font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        # Left panel: honest chart (zero baseline) — modest change
        col_l = Rectangle(width=5.0, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        lbl_l = Text("HONEST (zero baseline)", font=DISPLAY, font_size=14, color=TEAL).move_to(LEFT * 3.2 + UP * 1.6)

        # Draw three tiny bars at 81%, 84%, 87% on a 0-100 scale
        bar_h_full = 2.5  # total chart height in scene units for 100%
        bar_w = 0.5
        months = [81, 84, 87]
        x_starts = [-4.05, -3.35, -2.65]
        bars_l = []
        for x, pct in zip(x_starts, months):
            h = bar_h_full * pct / 100
            b = Rectangle(width=bar_w, height=h, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.6, stroke_width=0)
            b.move_to([x, -1.75 + h / 2, 0])
            bars_l.append(b)

        res_l = Text("6-point gain", font=DISPLAY, font_size=14, color=TEAL).move_to(LEFT * 3.2 + DOWN * 1.5)

        # Right panel: truncated axis (starts at 79) — dramatic
        col_r = Rectangle(width=5.0, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)
        lbl_r = Text("TRUNCATED (axis: 79-88%)", font=DISPLAY, font_size=14, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.6)

        # Same data on a 79-88 scale makes bars look enormous
        bar_h_trunc = 2.5  # full chart height for just the 79-88 range (9 units)
        bars_r = []
        for x, pct in zip([2.15, 2.85, 3.55], months):
            h = bar_h_trunc * (pct - 79) / 9
            b = Rectangle(width=bar_w, height=max(h, 0.05), color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.6, stroke_width=0)
            b.move_to([x, -1.75 + h / 2, 0])
            bars_r.append(b)

        res_r = Text("DRAMATIC RECOVERY", font=DISPLAY, font_size=14, color=CRIMSON, weight=BOLD).move_to(RIGHT * 3.2 + DOWN * 1.5)

        note = Text("Same CSV. Different axis. Different conclusion.", font=DISPLAY, font_size=15, color=INK).move_to(DOWN * 2.6)
        note_rect = Rectangle(width=8.5, height=0.52, fill_color=GOLD, fill_opacity=0.12,
                              stroke_width=1.5, color=GOLD).move_to(DOWN * 2.6)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.6)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.4)
        for b in bars_l:
            self.play(GrowFromEdge(b, DOWN), run_time=0.3)
        for b in bars_r:
            self.play(GrowFromEdge(b, DOWN), run_time=0.3)
        self.play(Write(res_l), Write(res_r), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.3)
        self.play(Write(note), run_time=0.4)
        self.wait(max(0.5, total - 5.5))
