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

# Bar data: SHAP values and corresponding y-plot coordinates
# y: SHAP 0->0.5 maps to y_plot = -2.5 + (shap/0.5)*5.0
# Bar center y = -2.5 + height/2
# Bar top y = -2.5 + height
_BARS = [
    # (x, shap, color, class_label)
    (-3.5, 0.45, CRIMSON,  "SPURIOUS"),
    (-1.0, 0.38, PASS_CLR, "CAUSAL"),
    ( 1.5, 0.12, SLATE,    None),
    ( 4.0, 0.08, SLATE,    None),
]


def _bar_height(shap):
    return (shap / 0.5) * 5.0


class B04_SHAPAudit(Scene):
    def construct(self):
        # Title
        title = Text("CONFOUNDING AUDIT — SHAP VALUES",
                     color=INK, weight=BOLD, font_size=34).move_to([0, 3.2, 0])

        # Axes
        y_axis = Line([-5.0, -2.5, 0], [-5.0,  2.5, 0], color=INK, stroke_width=2)
        x_axis = Line([-5.0, -2.5, 0], [ 5.0, -2.5, 0], color=INK, stroke_width=2)

        # Helper: text with CREAM bg
        def lbl_with_bg(text_str, x, y, font_size=20, color=INK):
            t = Text(text_str, color=color, font_size=font_size)
            t.move_to([x, y, 0])
            bg = Rectangle(
                width=t.width + 0.12, height=t.height + 0.08,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(t.get_center())
            return VGroup(bg, t)

        # y-tick labels
        y_tick_labels = VGroup(
            lbl_with_bg("0.0",  -5.5, -2.5),
            lbl_with_bg("0.25", -5.5,  0.0),
            lbl_with_bg("0.5",  -5.5,  2.5),
        )

        # x-tick labels (feature names, short)
        x_tick_labels = VGroup(
            lbl_with_bg("spurious",   -3.5, -2.9, font_size=18),
            lbl_with_bg("true_signal",-1.0, -2.9, font_size=18),
            lbl_with_bg("noise_1",     1.5, -2.9, font_size=18),
            lbl_with_bg("noise_2",     4.0, -2.9, font_size=18),
        )

        # Build bars
        bars = []
        shap_labels = []
        class_labels = []
        for bx, shap, color, cls in _BARS:
            h = _bar_height(shap)
            cy = -2.5 + h / 2.0
            bar = Rectangle(
                width=2.0, height=h,
                fill_color=color, fill_opacity=0.9,
                stroke_width=0, stroke_opacity=0
            ).move_to([bx, cy, 0])
            bars.append(bar)

            # SHAP value label above bar with CREAM bg
            top_y = -2.5 + h
            shap_lbl = lbl_with_bg(f"{shap:.2f}", bx, top_y + 0.25, font_size=22)
            shap_labels.append(shap_lbl)

            # Class label on bar (if not None)
            if cls is not None:
                cl_txt = Text(cls, color=INK, weight=BOLD, font_size=22)
                cl_txt.move_to([bx, cy, 0])
                class_labels.append(cl_txt)

        spurious_bar = bars[0]
        true_bar     = bars[1]
        noise_bars   = VGroup(bars[2], bars[3])

        spurious_shap_label = shap_labels[0]
        true_shap_label     = shap_labels[1]

        spurious_class_label = class_labels[0]  # "SPURIOUS" on CRIMSON bar
        true_class_label     = class_labels[1]  # "CAUSAL"   on green bar

        # Annotation at bottom
        annotation = Text("High SHAP != Causal feature",
                          color=CRIMSON, weight=BOLD, font_size=28).move_to([0, -3.2, 0])

        # 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(y_axis), FadeIn(x_axis), FadeIn(y_tick_labels))
        self.play(GrowFromEdge(spurious_bar, DOWN))
        self.play(Write(spurious_shap_label), Write(spurious_class_label))
        self.play(GrowFromEdge(true_bar, DOWN))
        self.play(Write(true_shap_label), Write(true_class_label),
                  FadeIn(noise_bars), FadeIn(x_tick_labels))
        self.play(Write(annotation))
        self.wait(1)
