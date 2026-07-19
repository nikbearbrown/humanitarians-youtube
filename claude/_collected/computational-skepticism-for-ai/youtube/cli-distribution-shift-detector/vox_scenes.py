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


class B04_PSIBars(Scene):
    def construct(self):
        # Pre-computed PSI values (hardcoded)
        PSI_NO_SHIFT   = 0.001
        PSI_MODERATE   = 0.08
        PSI_MAJOR      = 0.30
        PSI_MAX        = 0.35   # x-axis range

        BAR_H = 0.80
        BAR_Y = [1.5, 0.0, -1.5]   # y centers for 3 bars
        X_LEFT = -5.0               # bars start here
        X_SCALE = 8.0 / PSI_MAX    # pixels-per-PSI-unit: 8 units wide → PSI=0.35 at x=3.0

        def psi_to_x(psi):
            return X_LEFT + psi * X_SCALE

        def make_bar(psi, y_ctr, clr):
            w = psi * X_SCALE
            if w < 0.02:
                w = 0.02   # floor so zero-width bars are visible
            bar = Rectangle(
                width=w, height=BAR_H,
                fill_color=clr, fill_opacity=0.88,
                stroke_width=0, stroke_opacity=0,
            ).align_to([X_LEFT, 0, 0], LEFT).move_to([X_LEFT + w / 2, y_ctr, 0])
            return bar

        # ── Title ──────────────────────────────────────────────────────────────
        title = Text("POPULATION STABILITY INDEX — DISTRIBUTION SHIFT",
                     color=INK, weight=BOLD, font_size=26).move_to([0, 3.2, 0])

        # ── x-axis ─────────────────────────────────────────────────────────────
        x_axis = Line([X_LEFT, -2.5, 0], [3.5, -2.5, 0], color=INK, stroke_width=2)

        def x_tick_label(txt, x):
            bg = Rectangle(width=0.65, height=0.30, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([x, -2.85, 0])
            t = Text(txt, color=SLATE, font_size=17).move_to([x, -2.85, 0])
            return VGroup(bg, t)

        # x=−5.0 → PSI=0; x=−2.71 → PSI=0.10; x=−0.43 → PSI=0.20; x=3.0 → PSI=0.35
        x_tick_labels = VGroup(
            x_tick_label("0",    X_LEFT),
            x_tick_label("0.10", psi_to_x(0.10)),
            x_tick_label("0.20", psi_to_x(0.20)),
            x_tick_label("0.35", psi_to_x(PSI_MAX)),
        )

        # ── Row labels LEFT of bars ────────────────────────────────────────────
        GOLD_TEXT = "#956000"   # dark gold for readability on white

        def row_label(txt, y, clr):
            bg = Rectangle(width=1.4, height=0.34, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([-5.6, y, 0])
            t = Text(txt, color=clr, font_size=19).move_to([-5.6, y, 0])
            return VGroup(bg, t)

        row_labels = VGroup(
            row_label("No shift",  BAR_Y[0], PASS_CLR),
            row_label("Moderate",  BAR_Y[1], GOLD_TEXT),
            row_label("Major drift",BAR_Y[2], CRIMSON),
        )

        # ── Bars ───────────────────────────────────────────────────────────────
        no_shift_bar = make_bar(PSI_NO_SHIFT, BAR_Y[0], PASS_CLR)
        moderate_bar = make_bar(PSI_MODERATE, BAR_Y[1], GOLD)
        major_bar    = make_bar(PSI_MAJOR,    BAR_Y[2], CRIMSON)

        # ── PSI value labels RIGHT of each bar ────────────────────────────────
        def psi_label(txt, psi, y, clr, weight_bold=False):
            rx = psi_to_x(psi) + 0.25
            w = len(txt) * 0.14 + 0.2
            bg = Rectangle(width=w, height=0.32, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([rx + w / 2, y, 0])
            kw = {"weight": BOLD} if weight_bold else {}
            t = Text(txt, color=clr, font_size=20, **kw).move_to([rx + w / 2, y, 0])
            return VGroup(bg, t)

        no_shift_psi_label = psi_label("PSI=0.001", PSI_NO_SHIFT, BAR_Y[0], PASS_CLR)
        moderate_psi_label = psi_label("PSI=0.08",  PSI_MODERATE, BAR_Y[1], GOLD_TEXT)
        major_psi_label    = psi_label("PSI=0.30",  PSI_MAJOR,    BAR_Y[2] + 0.25, CRIMSON)

        # RETRAIN ALERT label below major PSI value
        alert_x = psi_to_x(PSI_MAJOR) + 1.6
        alert_bg = Rectangle(width=2.2, height=0.34, fill_color=CREAM, fill_opacity=1,
                             stroke_width=0, stroke_opacity=0
                             ).move_to([alert_x, BAR_Y[2] - 0.25, 0])
        retrain_alert = Text("RETRAIN ALERT", color=CRIMSON, weight=BOLD, font_size=20
                             ).move_to([alert_x, BAR_Y[2] - 0.25, 0])
        retrain_alert_label = VGroup(alert_bg, retrain_alert)

        # ── Threshold line at PSI=0.20 ─────────────────────────────────────────
        thresh_x = psi_to_x(0.20)
        threshold_line = DashedLine(
            [thresh_x, -2.2, 0], [thresh_x, 2.2, 0],
            color=CRIMSON, dash_length=0.18, stroke_width=2,
        )
        thresh_bg = Rectangle(width=2.6, height=0.30, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0
                              ).move_to([thresh_x + 1.5, 2.4, 0])
        threshold_label = Text("PSI=0.20 (major drift)", color=CRIMSON, font_size=20
                               ).move_to([thresh_x + 1.5, 2.4, 0])

        # ── Verdict ────────────────────────────────────────────────────────────
        verdict_bg = Rectangle(width=6.4, height=0.36, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to([0, -3.2, 0])
        verdict_text = Text("The model cannot detect its own distribution shift",
                            color=CRIMSON, font_size=24).move_to([0, -3.2, 0])

        # ── 7 play() calls ─────────────────────────────────────────────────────
        self.play(Write(title))
        self.play(FadeIn(x_axis), FadeIn(x_tick_labels), FadeIn(row_labels))
        self.play(GrowFromEdge(no_shift_bar, LEFT), FadeIn(no_shift_psi_label))
        self.play(GrowFromEdge(moderate_bar, LEFT), FadeIn(moderate_psi_label))
        self.play(GrowFromEdge(major_bar, LEFT))
        self.play(FadeIn(threshold_line), FadeIn(thresh_bg), Write(threshold_label))
        self.play(FadeIn(major_psi_label), FadeIn(retrain_alert_label),
                  FadeIn(verdict_bg), Write(verdict_text))
        self.wait(1)
