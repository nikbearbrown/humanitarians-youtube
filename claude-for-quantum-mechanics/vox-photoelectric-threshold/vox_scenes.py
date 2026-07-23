import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------------------
# B01 — Title card (CARD beat)
# ---------------------------------------------------------------------------
class B01_Title(Scene):
    def construct(self):
        duration = DUR.get("B01", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 1.8)
        headline = Text("Why Bright Red Light\nEjects No Electrons",
                        font=DISPLAY, font_size=42, color=INK,
                        line_spacing=1.2).move_to(DOWN * 0.2)
        self.add(bg)
        self.play(FadeIn(eyebrow), run_time=0.5)
        self.play(Create(headline), run_time=1.0)
        self.wait(duration - 1.5)


# ---------------------------------------------------------------------------
# B02 — Millikan's observation: ammeter at zero under red, electrons under violet
# ---------------------------------------------------------------------------
class B02_MillikanObservation(Scene):
    def construct(self):
        duration = DUR.get("B02", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Millikan, 1914: sodium surface", font=DISPLAY, font_size=24,
                     color=INK).move_to(UP * 3.2)

        # Left: red light, high intensity
        box_red = Rectangle(width=5.5, height=3.2).set_fill(CRIMSON, 0.07).set_stroke(CRIMSON, 2)
        box_red.move_to(LEFT * 3.5 + DOWN * 0.3)
        label_red = Text("RED  (high power)", font=DISPLAY, font_size=20,
                         color=CRIMSON).move_to(LEFT * 3.5 + UP * 1.5)
        result_red = Text("ammeter: 0", font="PT Mono", font_size=22,
                          color=CRIMSON).move_to(LEFT * 3.5 + DOWN * 0.5)
        note_red = Text("zero electrons", font=DISPLAY, font_size=18,
                        color=CRIMSON).move_to(LEFT * 3.5 + DOWN * 1.3)

        # Right: violet light, low intensity
        box_violet = Rectangle(width=5.5, height=3.2).set_fill(TEAL, 0.07).set_stroke(TEAL, 2)
        box_violet.move_to(RIGHT * 3.5 + DOWN * 0.3)
        label_violet = Text("VIOLET  (dim)", font=DISPLAY, font_size=20,
                            color=TEAL).move_to(RIGHT * 3.5 + UP * 1.5)
        result_violet = Text("electrons: ejected", font="PT Mono", font_size=22,
                             color=TEAL).move_to(RIGHT * 3.5 + DOWN * 0.5)
        note_violet = Text("immediately", font=DISPLAY, font_size=18,
                           color=TEAL).move_to(RIGHT * 3.5 + DOWN * 1.3)

        divider = Line(UP * 2.5, DOWN * 2.0, color=INK, stroke_width=1).set_opacity(0.3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(GrowFromCenter(box_red), GrowFromCenter(box_violet), run_time=0.8)
        self.play(FadeIn(label_red), FadeIn(label_violet), run_time=0.5)
        self.play(Write(result_red), Write(result_violet), run_time=0.9)
        self.play(FadeIn(note_red), FadeIn(note_violet), Create(divider), run_time=0.6)
        self.wait(duration - 3.5)


# ---------------------------------------------------------------------------
# B03 — THE QUESTION card (CARD beat)
# ---------------------------------------------------------------------------
class B03_TheQuestion(Scene):
    def construct(self):
        duration = DUR.get("B03", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE QUESTION", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 2.8)
        rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5).move_to(UP * 2.2)
        line1 = Text("A brighter wave delivers more energy per second.", font=SERIF, font_size=26, color=INK).move_to(UP * 1.4)
        line2 = Text("Classical theory: electrons should accumulate and escape.", font=SERIF, font_size=24, color=INK).move_to(UP * 0.5)
        line3 = Text("Here: zero electrons under intense red,", font=SERIF, font_size=24, color=INK).move_to(DOWN * 0.4)
        line4 = Text("electrons fly under dim violet. Why?", font=SERIF, font_size=24, color=INK).move_to(DOWN * 1.2)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.6)
        self.play(Write(line1), run_time=0.5)
        self.play(Write(line2), run_time=0.6)
        self.play(Write(line3), Write(line4), run_time=0.7)
        self.wait(duration - 2.4)


# ---------------------------------------------------------------------------
# B04 — Classical wave: energy accumulates (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B04_ClassicalWave(Scene):
    def construct(self):
        duration = DUR.get("B04", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Classical prediction: waves deliver energy continuously", font=DISPLAY,
                     font_size=22, color=CRIMSON).move_to(UP * 3.2)

        # A horizontal wave approaching a surface
        surface = Rectangle(width=0.3, height=5.0).set_fill(SLATE, 0.4).set_stroke(INK, 2)
        surface.move_to(RIGHT * 4.5)
        surface_label = Text("metal", font=DISPLAY, font_size=18, color=INK).move_to(RIGHT * 5.5 + DOWN * 0.3)

        # Wave approaching from left
        def wave_pts(x_offset=0, n=80):
            xs = np.linspace(-6.0 + x_offset, 4.2 + x_offset, n)
            ys = 0.5 * np.sin(xs * 2.2)
            return [np.array([x, y, 0]) for x, y in zip(xs, ys)]

        wave = VMobject().set_points_as_corners(wave_pts(0))
        wave.set_stroke(CRIMSON, 3).set_fill(opacity=0)

        # Energy bucket filling
        bucket_bg = Rectangle(width=1.5, height=2.0).set_fill(SLATE, 0.15).set_stroke(INK, 1.5)
        bucket_bg.move_to(RIGHT * 3.0 + DOWN * 1.5)
        bucket_label = Text("electron\nenergy", font=DISPLAY, font_size=16, color=INK,
                            line_spacing=1.1).move_to(RIGHT * 3.0 + DOWN * 1.5)

        fill_start = Rectangle(width=1.5, height=0.1).set_fill(CRIMSON, 0.8).set_stroke(width=0, opacity=0)
        fill_start.align_to(bucket_bg, DOWN).align_to(bucket_bg, LEFT)

        fill_end = Rectangle(width=1.5, height=2.0).set_fill(CRIMSON, 0.8).set_stroke(width=0, opacity=0)
        fill_end.align_to(bucket_bg, DOWN).align_to(bucket_bg, LEFT)

        prediction = Text("prediction: wait long enough -- electron escapes", font=DISPLAY,
                          font_size=20, color=CRIMSON).move_to(DOWN * 3.2)

        self.play(FadeIn(title), Create(surface), FadeIn(surface_label), run_time=0.7)
        self.play(Create(wave), run_time=0.9)
        self.play(Create(bucket_bg), run_time=0.4)
        self.play(GrowFromCenter(fill_start), run_time=0.3)
        self.play(Transform(fill_start, fill_end), run_time=2.0)
        self.play(FadeIn(prediction), run_time=0.5)
        self.wait(duration - 5.3)


# ---------------------------------------------------------------------------
# B05 — Experiments show frequency matters, not intensity (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B05_FrequencyMatters(Scene):
    def construct(self):
        duration = DUR.get("B05", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Experiment: frequency controls outcome", font=DISPLAY, font_size=24,
                     color=INK).move_to(UP * 3.2)

        # Frequency axis
        axis = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=2).move_to(DOWN * 0.5)
        ax_label = Text("frequency", font=DISPLAY, font_size=18, color=INK).move_to(RIGHT * 5.8 + DOWN * 0.5)

        # Threshold marker
        thresh = Line(UP * 2.0, DOWN * 0.5, color=GOLD, stroke_width=3).move_to(ORIGIN + DOWN * 0.0)
        thresh_label = Text("threshold", font=DISPLAY, font_size=18, color=INK).move_to(UP * 2.3)

        # Left: red photons - below threshold
        dot_red1 = Dot(radius=0.18, color=CRIMSON).move_to(LEFT * 3.5 + DOWN * 0.5)
        dot_red2 = Dot(radius=0.18, color=CRIMSON).move_to(LEFT * 2.5 + DOWN * 0.5)
        label_below = Text("red: below threshold", font=DISPLAY, font_size=18,
                           color=CRIMSON).move_to(LEFT * 3.0 + UP * 0.5)
        x_mark = Text("X  no electrons", font=DISPLAY, font_size=18,
                      color=CRIMSON).move_to(LEFT * 3.0 + DOWN * 1.5)

        # Right: violet photons - above threshold
        dot_violet = Dot(radius=0.18, color=TEAL).move_to(RIGHT * 2.5 + DOWN * 0.5)
        label_above = Text("violet: above threshold", font=DISPLAY, font_size=18,
                           color=TEAL).move_to(RIGHT * 2.8 + UP * 0.5)
        up_arrow = Arrow(RIGHT * 2.5 + DOWN * 0.3, RIGHT * 2.5 + UP * 1.5, color=TEAL,
                         buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.18)
        check_mark = Text("electron ejected", font=DISPLAY, font_size=18,
                          color=TEAL).move_to(RIGHT * 4.0 + UP * 1.3)

        self.play(FadeIn(title), Create(axis), FadeIn(ax_label), run_time=0.7)
        self.play(Create(thresh), FadeIn(thresh_label), run_time=0.6)
        self.play(GrowFromCenter(dot_red1), GrowFromCenter(dot_red2),
                  FadeIn(label_below), run_time=0.7)
        self.play(FadeIn(x_mark), run_time=0.5)
        self.play(GrowFromCenter(dot_violet), FadeIn(label_above), run_time=0.6)
        self.play(GrowArrow(up_arrow), FadeIn(check_mark), run_time=0.7)
        self.wait(duration - 4.2)


# ---------------------------------------------------------------------------
# B06 — THE MECHANISM section card (CARD beat)
# ---------------------------------------------------------------------------
class B06_MechanismCard(Scene):
    def construct(self):
        duration = DUR.get("B06", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.8)
        headline = Text("Light arrives in\nindivisible packets", font=DISPLAY, font_size=46,
                        color=INK, line_spacing=1.2).move_to(DOWN * 0.1)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(headline), run_time=0.9)
        self.wait(duration - 1.4)


# ---------------------------------------------------------------------------
# B07 — Photon packets: one photon, one electron (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B07_PhotonPackets(Scene):
    def construct(self):
        duration = DUR.get("B07", 13.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Einstein: light arrives as photons, each carrying h x nu", font=DISPLAY,
                     font_size=22, color=INK).move_to(UP * 3.2)

        # Surface on right
        surface = Rectangle(width=0.3, height=5.0).set_fill(SLATE, 0.4).set_stroke(INK, 2)
        surface.move_to(RIGHT * 3.5)

        # Photon as a dot traveling left-to-right
        photon = Dot(radius=0.28, color=TEAL).move_to(LEFT * 4.0)
        photon_label = Text("photon\nh x nu", font="PT Mono", font_size=20,
                            color=TEAL, line_spacing=1.1).move_to(LEFT * 4.0 + UP * 0.85)

        # Electron at surface
        electron = Dot(radius=0.28, color=INK).move_to(RIGHT * 3.5 + UP * 0.3)
        electron_label = Text("electron", font=DISPLAY, font_size=18,
                              color=INK).move_to(RIGHT * 4.5 + UP * 0.3)

        # Ejected electron arrow
        eject_arrow = Arrow(RIGHT * 3.5 + UP * 0.3, RIGHT * 3.5 + UP * 2.3, color=TEAL,
                            buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        eject_label = Text("ejected", font=DISPLAY, font_size=18,
                           color=TEAL).move_to(RIGHT * 4.8 + UP * 1.5)

        self.play(FadeIn(title), Create(surface), run_time=0.7)
        self.play(GrowFromCenter(photon), FadeIn(photon_label), run_time=0.6)
        self.play(GrowFromCenter(electron), FadeIn(electron_label), run_time=0.5)
        self.play(photon.animate.move_to(RIGHT * 3.2), run_time=1.5)
        photon.set_opacity(0)
        self.play(
            photon.animate.scale(0.1),
            electron.animate.shift(UP * 0.2),
            run_time=0.5
        )
        self.play(GrowArrow(eject_arrow), FadeIn(eject_label), run_time=0.8)
        self.wait(duration - 5.3)


# ---------------------------------------------------------------------------
# B08 — Intensity = photon rate, not per-photon energy (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B08_IntensityIsRate(Scene):
    def construct(self):
        duration = DUR.get("B08", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Intensity controls rate, not energy per photon", font=DISPLAY,
                     font_size=24, color=INK).move_to(UP * 3.2)

        # Threshold bar
        thresh_bar = Line(UP * 2.5, DOWN * 2.5, color=GOLD, stroke_width=3).move_to(ORIGIN)
        thresh_label = Text("threshold", font=DISPLAY, font_size=18,
                            color=INK).move_to(UP * 2.8)

        # Left: many low-energy photons (CRIMSON)
        dots_left = VGroup(*[
            Dot(radius=0.16, color=CRIMSON).move_to(LEFT * (3.0 + 0.5 * i) + UP * (0.8 - 0.4 * j))
            for i in range(4) for j in range(3)
        ])
        label_left = Text("many red photons\n(none can clear bar)", font=DISPLAY, font_size=16,
                          color=CRIMSON, line_spacing=1.1).move_to(LEFT * 3.5 + DOWN * 1.8)

        # Right: one high-energy photon (TEAL)
        dot_right = Dot(radius=0.28, color=TEAL).move_to(RIGHT * 2.5 + UP * 0.5)
        arrow_right = Arrow(RIGHT * 2.5 + UP * 0.5, RIGHT * 2.5 + UP * 2.5, color=TEAL,
                            buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.2)
        label_right = Text("one violet photon\n(clears bar -- success)", font=DISPLAY, font_size=16,
                           color=TEAL, line_spacing=1.1).move_to(RIGHT * 3.5 + DOWN * 1.8)

        self.play(FadeIn(title), Create(thresh_bar), FadeIn(thresh_label), run_time=0.7)
        self.play(GrowFromCenter(dots_left), FadeIn(label_left), run_time=1.0)
        self.play(GrowFromCenter(dot_right), FadeIn(label_right), run_time=0.7)
        self.play(GrowArrow(arrow_right), run_time=0.8)
        self.wait(duration - 3.5)


# ---------------------------------------------------------------------------
# B09 — Section card: one photon one electron (CARD beat)
# ---------------------------------------------------------------------------
class B09_OnePhotonCard(Scene):
    def construct(self):
        duration = DUR.get("B09", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE MECHANISM", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 1.8)
        headline = Text("One photon, one electron —\nor nothing", font=DISPLAY, font_size=44,
                        color=INK, line_spacing=1.2).move_to(DOWN * 0.1)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.1)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(headline), run_time=0.9)
        self.wait(duration - 1.4)


# ---------------------------------------------------------------------------
# B10 — Work function barrier (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B10_WorkFunction(Scene):
    def construct(self):
        duration = DUR.get("B10", 11.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Work function: the binding energy barrier", font=DISPLAY, font_size=24,
                     color=INK).move_to(UP * 3.2)

        # Energy axis
        axis_y = Line(DOWN * 2.5, UP * 2.5, color=INK, stroke_width=2).move_to(LEFT * 4.5)
        ax_label = Text("energy", font=DISPLAY, font_size=18, color=INK).move_to(LEFT * 4.5 + UP * 3.0)

        # Floor (bound state)
        floor_line = Line(LEFT * 4.0, RIGHT * 5.0, color=SLATE, stroke_width=2).move_to(DOWN * 1.5)
        floor_label = Text("electron bound state", font=DISPLAY, font_size=16,
                           color=SLATE).move_to(RIGHT * 2.5 + DOWN * 2.0)

        # Work function bar
        wf_bar = Rectangle(width=0.5, height=2.0).set_fill(GOLD, 0.4).set_stroke(GOLD, 2)
        wf_bar.move_to(LEFT * 1.5 + DOWN * 0.5)
        wf_label = Text("phi\n(work\nfunction)", font="PT Mono", font_size=16,
                        color=INK, line_spacing=1.1).move_to(LEFT * 0.3 + DOWN * 0.5)

        # Photon incoming, too small (CRIMSON)
        photon_small = Dot(radius=0.2, color=CRIMSON).move_to(LEFT * 3.5 + DOWN * 1.5)
        small_label = Text("red photon\nh x nu < phi", font="PT Mono", font_size=16,
                           color=CRIMSON, line_spacing=1.1).move_to(LEFT * 3.5 + UP * 0.0)
        bounce = Arrow(LEFT * 3.5 + DOWN * 1.5, LEFT * 5.0 + DOWN * 1.5, color=CRIMSON,
                       buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.2)

        # Photon incoming, large enough (TEAL)
        photon_big = Dot(radius=0.28, color=TEAL).move_to(RIGHT * 1.5 + DOWN * 1.5)
        big_label = Text("violet photon\nh x nu > phi", font="PT Mono", font_size=16,
                         color=TEAL, line_spacing=1.1).move_to(RIGHT * 2.8 + UP * 0.0)
        escape = Arrow(RIGHT * 1.5 + DOWN * 1.5, RIGHT * 1.5 + UP * 1.5, color=TEAL,
                       buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.2)

        self.play(FadeIn(title), Create(axis_y), FadeIn(ax_label), run_time=0.6)
        self.play(Create(floor_line), FadeIn(floor_label), run_time=0.5)
        self.play(GrowFromCenter(wf_bar), FadeIn(wf_label), run_time=0.7)
        self.play(GrowFromCenter(photon_small), FadeIn(small_label), run_time=0.6)
        self.play(GrowArrow(bounce), run_time=0.7)
        self.play(GrowFromCenter(photon_big), FadeIn(big_label), run_time=0.6)
        self.play(GrowArrow(escape), run_time=0.7)
        self.wait(duration - 5.1)


# ---------------------------------------------------------------------------
# B12 — No partial credit (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B12_NoPartialCredit(Scene):
    def construct(self):
        duration = DUR.get("B12", 9.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("No partial credit: no accumulation, no waiting", font=DISPLAY,
                     font_size=24, color=CRIMSON).move_to(UP * 3.2)

        # A series of photons all failing
        y_levels = [1.0, 0.3, -0.4, -1.1]
        photons = VGroup()
        x_marks = VGroup()
        for i, y in enumerate(y_levels):
            p = Dot(radius=0.2, color=CRIMSON).move_to(LEFT * (3.0 - i * 0.3) + UP * y)
            photons.add(p)
            x = Text("X", font=DISPLAY, font_size=22, color=CRIMSON).move_to(RIGHT * 0.5 + UP * y)
            x_marks.add(x)

        wall = Rectangle(width=0.3, height=5.5).set_fill(SLATE, 0.4).set_stroke(INK, 2)
        wall.move_to(RIGHT * 0.3)
        wall_label = Text("barrier", font=DISPLAY, font_size=18, color=INK).move_to(RIGHT * 1.3 + UP * 2.5)

        conclusion = Text("Each photon succeeds or fails independently.", font=DISPLAY,
                          font_size=22, color=CRIMSON).move_to(DOWN * 2.5)

        self.play(FadeIn(title), Create(wall), FadeIn(wall_label), run_time=0.7)
        self.play(GrowFromCenter(photons), run_time=0.9)
        self.play(FadeIn(x_marks), run_time=0.7)
        self.play(FadeIn(conclusion), run_time=0.6)
        self.wait(duration - 3.2)


# ---------------------------------------------------------------------------
# B13 — THE EXAMPLE card (CARD beat)
# ---------------------------------------------------------------------------
class B13_ExampleCard(Scene):
    def construct(self):
        duration = DUR.get("B13", 7.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("THE EXAMPLE", font=DISPLAY, font_size=22, color=SLATE).move_to(UP * 2.0)
        headline = Text("Sodium under red\nand violet light", font=DISPLAY, font_size=44,
                        color=INK, line_spacing=1.2).move_to(UP * 0.4)
        sub = Text("(illustrative)", font=SERIF, font_size=24,
                   color=SLATE).move_to(DOWN * 0.9)
        rule = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=1.5).move_to(UP * 1.2)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(headline), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(max(0.1, duration - 1.7))


# ---------------------------------------------------------------------------
# B14 — Sodium worked example (GRAPHIC beat)
# ---------------------------------------------------------------------------
class B14_SodiumExample(Scene):
    def construct(self):
        duration = DUR.get("B14", 20.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        self.add(bg)

        title = Text("Sodium: work function 2.36 eV", font=DISPLAY, font_size=24,
                     color=INK).move_to(UP * 3.2)

        # Energy axis
        axis = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=2).move_to(DOWN * 1.5)
        zero_label = Text("0", font="PT Mono", font_size=18, color=INK).move_to(LEFT * 5.8 + DOWN * 1.5)

        # Work function threshold bar
        wf_y = 0.3
        wf_line = DashedLine(LEFT * 5.5, RIGHT * 5.5, color=GOLD, stroke_width=2).move_to(UP * wf_y)
        wf_label = Text("threshold  2.36 eV", font="PT Mono", font_size=18,
                        color=INK).move_to(RIGHT * 3.0 + UP * (wf_y + 0.5))

        # Red photon bar (2.0 eV) — CRIMSON, below threshold
        bar_red = Rectangle(width=1.8, height=1.7).set_fill(CRIMSON, 0.7).set_stroke(width=0, opacity=0)
        bar_red.align_to(axis, DOWN).move_to(LEFT * 2.8 + DOWN * 0.65)
        label_red_e = Text("red\n2.0 eV", font="PT Mono", font_size=18,
                           color=CRIMSON, line_spacing=1.1).move_to(LEFT * 2.8 + DOWN * 2.5)
        label_red_r = Text("below bar:\nno electrons", font=DISPLAY, font_size=16,
                           color=CRIMSON, line_spacing=1.1).move_to(LEFT * 2.8 + UP * 1.5)

        # Violet photon bar (3.1 eV) — TEAL, above threshold
        bar_violet = Rectangle(width=1.8, height=2.4).set_fill(TEAL, 0.7).set_stroke(width=0, opacity=0)
        bar_violet.align_to(axis, DOWN).move_to(RIGHT * 1.8 + DOWN * 0.3)
        label_violet_e = Text("violet\n3.1 eV", font="PT Mono", font_size=18,
                              color=TEAL, line_spacing=1.1).move_to(RIGHT * 1.8 + DOWN * 2.5)
        kinetic_arrow = Arrow(UP * wf_y, UP * 2.8, color=TEAL, buff=0,
                              stroke_width=3, max_tip_length_to_length_ratio=0.18)
        kinetic_arrow.move_to(RIGHT * 1.8 + UP * (wf_y + 0.9))
        kinetic_label = Text("0.74 eV\nkinetic", font="PT Mono", font_size=18,
                             color=TEAL, line_spacing=1.1).move_to(RIGHT * 3.5 + UP * 2.2)

        self.play(FadeIn(title), Create(axis), FadeIn(zero_label), run_time=0.7)
        self.play(Create(wf_line), FadeIn(wf_label), run_time=0.6)
        self.play(GrowFromCenter(bar_red), FadeIn(label_red_e), run_time=0.8)
        self.play(FadeIn(label_red_r), run_time=0.5)
        self.play(GrowFromCenter(bar_violet), FadeIn(label_violet_e), run_time=0.8)
        self.play(GrowArrow(kinetic_arrow), FadeIn(kinetic_label), run_time=0.8)
        self.wait(duration - 5.0)


# ---------------------------------------------------------------------------
# B15 — RECAP endcard (CARD beat)
# ---------------------------------------------------------------------------
class B15_Recap(Scene):
    def construct(self):
        duration = DUR.get("B15", 10.0)
        bg = Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)
        eyebrow = Text("QUANTUM MECHANICS", font=DISPLAY, font_size=22,
                       color=TEAL).move_to(UP * 2.8)
        rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5).move_to(UP * 2.2)
        line1 = Text("Below threshold:", font=DISPLAY, font_size=32,
                     color=CRIMSON).move_to(UP * 1.3)
        line2 = Text("no electrons at any intensity.", font=SERIF, font_size=30,
                     color=CRIMSON).move_to(UP * 0.5)
        line3 = Text("Above threshold:", font=DISPLAY, font_size=32,
                     color=TEAL).move_to(DOWN * 0.5)
        line4 = Text("every photon ejects one electron at fixed energy.", font=SERIF, font_size=26,
                     color=TEAL).move_to(DOWN * 1.3)
        kicker = Text("Frequency decides. Intensity never does.", font=DISPLAY,
                      font_size=26, color=INK).move_to(DOWN * 2.5)
        self.add(bg)
        self.play(FadeIn(eyebrow), Create(rule), run_time=0.5)
        self.play(Write(line1), Write(line2), run_time=1.0)
        self.play(Write(line3), Write(line4), run_time=1.0)
        self.play(FadeIn(kicker), run_time=0.6)
        self.wait(duration - 3.1)
