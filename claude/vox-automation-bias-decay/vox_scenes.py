import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B03_VigDecay(Scene):
    """Vigilance gauge decays over green success streak, CRIMSON failure at minimum."""

    def construct(self):
        dur = DUR.get("B03", 16.0)

        # Label: Review Effort at top-left
        gauge_lbl = Text("Review Effort", font=DISPLAY, font_size=20, color=TEAL)
        gauge_lbl.move_to([-5.0, 2.8, 0.0])
        self.play(FadeIn(gauge_lbl), run_time=0.3)

        # Gauge bar: background
        gauge_bg = Rectangle(width=7.5, height=0.6)
        gauge_bg.set_fill(SLATE, 0.2)
        gauge_bg.set_stroke(SLATE, 1.5)
        gauge_bg.move_to([0.5, 2.0, 0.0])
        self.play(FadeIn(gauge_bg), run_time=0.3)

        # Gauge fill — starts TEAL (high)
        gauge_fill = Rectangle(width=7.0, height=0.5)
        gauge_fill.set_fill(TEAL, 0.6)
        gauge_fill.set_stroke(TEAL, 0)
        gauge_fill.move_to([0.3, 2.0, 0.0])
        self.play(FadeIn(gauge_fill), run_time=0.4)

        high_lbl = Text("HIGH", font=SANS, font_size=14, color=TEAL)
        high_lbl.move_to([4.5, 2.0, 0.0])
        self.play(FadeIn(high_lbl), run_time=0.3)

        # Timeline of checkmarks below gauge
        check_xs = [-4.5, -3.0, -1.5, 0.0, 1.5, 3.0, 4.5]
        check_lbl = Text("✓", font=SANS, font_size=22, color=TEAL)

        for i, cx in enumerate(check_xs):
            ck = Text("✓", font=SANS, font_size=22, color=TEAL)
            ck.move_to([cx, 0.5, 0.0])
            self.play(FadeIn(ck), run_time=0.2)

        # Gauge decays — transform to shorter/CRIMSON
        # Replace with narrow CRIMSON fill
        gauge_fill2 = Rectangle(width=1.2, height=0.5)
        gauge_fill2.set_fill(CRIMSON, 0.6)
        gauge_fill2.set_stroke(CRIMSON, 0)
        gauge_fill2.move_to([-2.9, 2.0, 0.0])

        self.play(
            FadeOut(gauge_fill),
            FadeOut(high_lbl),
            run_time=0.4
        )
        self.play(FadeIn(gauge_fill2), run_time=0.4)

        low_lbl = Text("LOW", font=SANS, font_size=14, color=CRIMSON)
        low_lbl.move_to([-2.9, 2.0, 0.0])
        self.play(FadeIn(low_lbl), run_time=0.3)

        # Separator
        sep = Line([-5.5, -0.3, 0.0], [5.5, -0.3, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(sep), run_time=0.3)

        # CRIMSON failure marker
        fail_box = Rectangle(width=2.2, height=0.85)
        fail_box.set_fill(CRIMSON, 0.22)
        fail_box.set_stroke(CRIMSON, 2.5)
        fail_box.move_to([0.0, -1.0, 0.0])

        fail_lbl = Text("FAILURE", font=DISPLAY, font_size=22, color=CRIMSON)
        fail_lbl.move_to([0.0, -1.0, 0.0])

        arrow_down = Line([0.0, -0.15, 0.0], [0.0, -0.6, 0.0], stroke_width=2.5, color=CRIMSON)
        self.play(Create(arrow_down), run_time=0.2)
        self.play(FadeIn(fail_box), run_time=0.3)
        self.play(FadeIn(fail_lbl), run_time=0.3)

        note_lbl = Text("at minimum vigilance", font=SANS, font_size=14, color=CRIMSON)
        note_lbl.move_to([0.0, -1.9, 0.0])
        self.play(FadeIn(note_lbl), run_time=0.3)

        self.wait(max(0.1, dur - 5.5))


class B05_PriyaStreak(Scene):
    """11 green checkmarks, refactor 12 in CRIMSON, 8s approval, production failure."""

    def construct(self):
        dur = DUR.get("B05", 15.0)

        # Title
        title = Text("Priya — 11 correct refactors", font=DISPLAY, font_size=20, color=TEAL)
        title.move_to([0.0, 2.8, 0.0])
        self.play(FadeIn(title), run_time=0.3)

        # 11 checkmark boxes in a 6+5 grid
        check_positions = []
        # Row 1: 6 checks
        for i in range(6):
            check_positions.append([-4.5 + i * 1.6, 1.6, 0.0])
        # Row 2: 5 checks
        for i in range(5):
            check_positions.append([-3.7 + i * 1.6, 0.5, 0.0])

        for pos in check_positions:
            ck_box = Rectangle(width=1.2, height=0.8)
            ck_box.set_fill(TEAL, 0.2)
            ck_box.set_stroke(TEAL, 1.8)
            ck_box.move_to(pos)
            ck_lbl = Text("✓", font=SANS, font_size=20, color=TEAL)
            ck_lbl.move_to(pos)
            self.play(FadeIn(ck_box), FadeIn(ck_lbl), run_time=0.08)

        # Separator
        sep = Line([-5.5, -0.3, 0.0], [5.5, -0.3, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(sep), run_time=0.3)

        # Refactor 12 — CRIMSON
        r12_box = Rectangle(width=3.0, height=0.85)
        r12_box.set_fill(CRIMSON, 0.2)
        r12_box.set_stroke(CRIMSON, 2.5)
        r12_box.move_to([-2.5, -1.1, 0.0])
        r12_lbl = Text("Refactor 12:\nnull-check removed", font=SANS, font_size=14, color=CRIMSON)
        r12_lbl.move_to([-2.5, -1.1, 0.0])
        self.play(FadeIn(r12_box), run_time=0.4)
        self.play(FadeIn(r12_lbl), run_time=0.3)

        # Approval box
        appr_box = Rectangle(width=2.6, height=0.7)
        appr_box.set_fill(CRIMSON, 0.15)
        appr_box.set_stroke(CRIMSON, 1.8)
        appr_box.move_to([2.0, -1.1, 0.0])
        appr_lbl = Text("Approved\n8 seconds", font=SANS, font_size=14, color=CRIMSON)
        appr_lbl.move_to([2.0, -1.1, 0.0])

        arr12 = Line([-.9, -1.1, 0.0], [0.7, -1.1, 0.0], stroke_width=2.5, color=CRIMSON)
        self.play(Create(arr12), run_time=0.3)
        self.play(FadeIn(appr_box), run_time=0.3)
        self.play(FadeIn(appr_lbl), run_time=0.3)

        # Production failure
        prod_line = Line([0.0, -1.8, 0.0], [0.0, -2.2, 0.0], stroke_width=2, color=CRIMSON)
        self.play(Create(prod_line), run_time=0.2)

        prod_box = Rectangle(width=3.5, height=0.65)
        prod_box.set_fill(CRIMSON, 0.18)
        prod_box.set_stroke(CRIMSON, 2)
        prod_box.move_to([0.0, -2.6, 0.0])
        prod_lbl = Text("Null pointer in production — 4 days later", font=SANS, font_size=13, color=CRIMSON)
        prod_lbl.move_to([0.0, -2.6, 0.0])
        self.play(FadeIn(prod_box), run_time=0.3)
        self.play(FadeIn(prod_lbl), run_time=0.3)

        self.wait(max(0.1, dur - 4.5))


class B06_FixedReview(Scene):
    """Two columns: variable review (CRIMSON, shrinks) vs fixed review (TEAL, constant)."""

    def construct(self):
        dur = DUR.get("B06", 14.0)

        # Divider
        div = Line([0.0, 3.0, 0.0], [0.0, -3.0, 0.0], stroke_width=1.5, color=SLATE)
        self.play(Create(div), run_time=0.3)

        # Left header (CRIMSON)
        lhdr = Text("Variable Review", font=DISPLAY, font_size=20, color=CRIMSON)
        lhdr.move_to([-3.0, 2.7, 0.0])
        self.play(FadeIn(lhdr), run_time=0.3)

        # Right header (TEAL)
        rhdr = Text("Fixed Review", font=DISPLAY, font_size=20, color=TEAL)
        rhdr.move_to([3.0, 2.7, 0.0])
        self.play(FadeIn(rhdr), run_time=0.3)

        # Left: review bars shrinking
        bar_data = [(1.8, 3.5), (1.2, 2.6), (0.6, 1.7), (0.2, 0.8)]  # (width, y)
        for w, y in bar_data:
            bar = Rectangle(width=max(w, 0.2), height=0.5)
            bar.set_fill(CRIMSON, 0.2)
            bar.set_stroke(CRIMSON, 1.8)
            bar.move_to([-4.5 + w/2, y - 1.0, 0.0])
            self.play(FadeIn(bar), run_time=0.25)

        l_streak = Text("streak grows →\nreview shrinks", font=SANS, font_size=13, color=CRIMSON)
        l_streak.move_to([-3.0, -1.5, 0.0])
        self.play(FadeIn(l_streak), run_time=0.3)

        # Separator
        bot_sep = Line([-5.5, -2.0, 0.0], [5.5, -2.0, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(bot_sep), run_time=0.3)

        # Right: review bars constant
        const_ys = [2.5, 1.7, 0.9, 0.1]
        for y in const_ys:
            bar = Rectangle(width=3.5, height=0.5)
            bar.set_fill(TEAL, 0.18)
            bar.set_stroke(TEAL, 1.8)
            bar.move_to([3.0, y - 1.0, 0.0])
            self.play(FadeIn(bar), run_time=0.22)

        r_streak = Text("streak grows →\nreview stays constant", font=SANS, font_size=13, color=TEAL)
        r_streak.move_to([3.0, -1.5, 0.0])
        self.play(FadeIn(r_streak), run_time=0.3)

        self.wait(max(0.1, dur - 5.0))
