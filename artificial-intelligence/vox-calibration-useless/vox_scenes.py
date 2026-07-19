import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))

from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,  "B02": 11.0, "B04": 9.0, "B05": 9.0,
    "B07": 9.0,  "B08": 8.0,  "B09": 9.0,
    "B10": 7.0,  "B11": 8.0,  "B12": 18.0,
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
        t1 = Text("Why a Perfectly Calibrated Model", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        t2 = Text("Can Be Perfectly Useless", font=DISPLAY, color=GOLD, font_size=36, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── B02 — BaseRateModel ───────────────────────────────────────────────────────

class B02_BaseRateModel(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Left: perfect calibration score badge
        cal_box = Rectangle(width=4.5, height=2.8, color=TEAL, fill_color=TEAL,
                            fill_opacity=0.12, stroke_width=2).move_to(LEFT * 3.5 + UP * 0.5)
        cal_lbl = Text("CALIBRATION", font=DISPLAY, font_size=15, color=TEAL).move_to(LEFT * 3.5 + UP * 1.5)
        cal_val = Text("ECE = 0.00", font=MONO, font_size=22, color=TEAL).move_to(LEFT * 3.5 + UP * 0.5)
        cal_sub = Text("PERFECT", font=DISPLAY, font_size=14, color=TEAL).move_to(LEFT * 3.5 + DOWN * 0.4)

        # Right: every patient gets same output
        pred_box = Rectangle(width=4.5, height=2.8, color=CRIMSON, fill_color=CRIMSON,
                             fill_opacity=0.12, stroke_width=2).move_to(RIGHT * 3.5 + UP * 0.5)
        pred_lbl = Text("OUTPUT FOR EVERY\nPATIENT", font=DISPLAY, font_size=14, color=CRIMSON).move_to(RIGHT * 3.5 + UP * 1.5)
        pred_val = Text("30%", font=MONO, font_size=32, color=CRIMSON).move_to(RIGHT * 3.5 + UP * 0.5)
        pred_sub = Text("(the base rate)", font=MONO, font_size=14, color=INK).move_to(RIGHT * 3.5 + DOWN * 0.4)

        verdict = Text("Perfectly calibrated. Completely useless for any individual decision.",
                       font=DISPLAY, font_size=14, color=GOLD).move_to(DOWN * 2.3)

        self.play(GrowFromCenter(cal_box), GrowFromCenter(pred_box), run_time=0.5)
        self.play(Write(cal_lbl), Write(pred_lbl), run_time=0.4)
        self.play(Write(cal_val), Write(pred_val), run_time=0.4)
        self.play(Write(cal_sub), Write(pred_sub), run_time=0.4)
        self.play(Write(verdict), run_time=0.5)
        self.wait(DUR["B02"] - 3.2)


# ── B04 — CalibrationMeasure ──────────────────────────────────────────────────

class B04_CalibrationMeasure(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What Calibration Actually Measures", font=DISPLAY, font_size=20, color=TEAL).move_to(UP * 3.1)

        rows = [
            ("Model says: 30% positive",     "30% of those patients ARE positive", TEAL),
            ("Model says: 30% (always)",      "still 30% across all predictions",   TEAL),
            ("ECE = 0",                       "stated confidence matches frequency", TEAL),
            ("Does not measure:",             "whether you say different things\nfor different patients", GOLD),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (label, desc, col) in enumerate(rows):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.5).move_to(UP * y)
            t1  = Text(label, font=DISPLAY, font_size=15, color=col).move_to([0.0, y + 0.22, 0])
            t2  = Text(desc,  font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(t1), run_time=0.3)
            self.play(Write(t2), run_time=0.3)

        self.wait(DUR["B04"] - 4.5)


# ── B05 — TwoAxes ─────────────────────────────────────────────────────────────

class B05_TwoAxes(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        hdr_cal  = Rectangle(width=5.5, height=0.6, color=TEAL,   fill_color=TEAL,
                             fill_opacity=0.20, stroke_width=1.5).move_to(LEFT * 3.2 + UP * 2.8)
        hdr_disc = Rectangle(width=5.5, height=0.6, color=GOLD,   fill_color=GOLD,
                             fill_opacity=0.20, stroke_width=1.5).move_to(RIGHT * 3.2 + UP * 2.8)
        t_cal    = Text("CALIBRATION", font=DISPLAY, font_size=17, color=TEAL).move_to(hdr_cal)
        t_disc   = Text("DISCRIMINATION", font=DISPLAY, font_size=17, color=GOLD).move_to(hdr_disc)

        body_cal  = Rectangle(width=5.5, height=3.8, color=TEAL, fill_opacity=0,
                              stroke_width=1.5).move_to(LEFT * 3.2 + DOWN * 0.6)
        body_disc = Rectangle(width=5.5, height=3.8, color=GOLD, fill_opacity=0,
                              stroke_width=1.5).move_to(RIGHT * 3.2 + DOWN * 0.6)

        c1 = Text("Confidence matches\nfrequency\n(honesty)", font=MONO, font_size=14, color=INK).move_to(LEFT * 3.2 + UP * 0.5)
        c2 = Text("→ ECE, reliability\ndiagram", font=DISPLAY, font_size=13, color=TEAL).move_to(LEFT * 3.2 + DOWN * 1.5)

        f1 = Text("Different outputs\nfor different patients\n(usefulness)", font=MONO, font_size=14, color=INK).move_to(RIGHT * 3.2 + UP * 0.5)
        f2 = Text("→ SEPARATE AXIS\nCALIBRATION BLIND\nTO THIS", font=DISPLAY, font_size=13, color=GOLD).move_to(RIGHT * 3.2 + DOWN * 1.5)

        self.play(GrowFromCenter(hdr_cal), GrowFromCenter(hdr_disc), run_time=0.5)
        self.play(Write(t_cal), Write(t_disc), run_time=0.5)
        self.play(GrowFromCenter(body_cal), GrowFromCenter(body_disc), run_time=0.5)
        self.play(Write(c1), Write(f1), run_time=0.5)
        self.play(Write(c2), Write(f2), run_time=0.5)
        self.wait(DUR["B05"] - 3.5)


# ── B07 — ReliabilityDiagram ──────────────────────────────────────────────────

class B07_ReliabilityDiagram(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Reliability Diagram", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)

        # Left: useful discriminating model — dots spread on diagonal
        ax1 = Rectangle(width=3.5, height=3.5, color=SLATE, fill_opacity=0,
                        stroke_width=1.5).move_to(LEFT * 3.3 + UP * 0.3)
        ax1_lbl = Text("DISCRIMINATING\nMODEL", font=DISPLAY, font_size=13, color=TEAL).move_to(LEFT * 3.3 + DOWN * 1.8)
        diag1 = Line(LEFT * 5.05 + DOWN * 1.45, LEFT * 1.55 + UP * 2.05,
                     color=TEAL, stroke_width=1, stroke_opacity=0.4)
        dots_spread = [
            Dot(radius=0.11, color=TEAL).move_to([(-3.3 + (i - 2) * 0.6), (0.3 + (i - 2) * 0.6), 0])
            for i in range(5)
        ]

        # Right: base-rate model — all dots pile on one point
        ax2 = Rectangle(width=3.5, height=3.5, color=SLATE, fill_opacity=0,
                        stroke_width=1.5).move_to(RIGHT * 3.3 + UP * 0.3)
        ax2_lbl = Text("BASE-RATE\nMODEL", font=DISPLAY, font_size=13, color=CRIMSON).move_to(RIGHT * 3.3 + DOWN * 1.8)
        diag2 = Line(RIGHT * 1.55 + DOWN * 1.45, RIGHT * 5.05 + UP * 2.05,
                     color=TEAL, stroke_width=1, stroke_opacity=0.4)
        dots_piled = [
            Dot(radius=0.11 + i * 0.02, color=CRIMSON).move_to([3.3, 0.3, 0])
            for i in range(4)
        ]

        ece_teal   = Text("ECE ≠ 0  (useful)", font=MONO, font_size=13, color=TEAL).move_to(LEFT  * 3.3 + UP * 2.35)
        ece_crimson = Text("ECE = 0  (useless)", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.3 + UP * 2.35)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(ax1), GrowFromCenter(ax2), run_time=0.5)
        self.play(Create(diag1), Create(diag2), run_time=0.4)
        self.play(Write(ece_teal), Write(ece_crimson), run_time=0.4)
        for d in dots_spread:
            self.play(GrowFromCenter(d), run_time=0.2)
        for d in dots_piled:
            self.play(GrowFromCenter(d), run_time=0.15)
        self.play(Write(ax1_lbl), Write(ax2_lbl), run_time=0.4)
        self.wait(DUR["B07"] - 4.8)


# ── B08 — QuoteUseless ────────────────────────────────────────────────────────

class B08_QuoteUseless(Scene):
    def construct(self):
        _quote_scene(
            self,
            "A model with perfect calibration but no resolution — "
            "predicting the base rate for every instance — "
            "has a calibration error of zero and is completely useless for triage.",
            "Computational Skepticism for AI, Chapter 11",
            None,
            "completely useless",
            DUR["B08"],
        )


# ── B09 — BothRequired ────────────────────────────────────────────────────────

class B09_BothRequired(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("You Need Both", font=DISPLAY, font_size=22, color=TEAL).move_to(UP * 3.1)

        rows = [
            ("CALIBRATED + DISCRIMINATING",  "Reliable probabilities that\ndiffer across patients",    TEAL),
            ("CALIBRATED, NOT DISCRIMINATING", "Honest but useless — base-rate\noutput for everyone",   CRIMSON),
            ("DISCRIMINATING, NOT CALIBRATED", "Ranks patients correctly but\nprobabilities mislead",   GOLD),
            ("ONE AGGREGATE SCORE",           "Collapses both — hides\nwhich failure you have",         CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, desc, col) in enumerate(rows):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.5).move_to(UP * y)
            t1  = Text(name, font=DISPLAY, font_size=14, color=col).move_to([0.0, y + 0.22, 0])
            t2  = Text(desc, font=MONO,    font_size=12, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(t1), run_time=0.3)
            self.play(Write(t2), run_time=0.3)

        self.wait(DUR["B09"] - 4.5)


# ── B10 — QuoteHonest ─────────────────────────────────────────────────────────

class B10_QuoteHonest(Scene):
    def construct(self):
        _quote_scene(
            self,
            "A model well-calibrated but predicting close to the base rate "
            "for every instance is honest about uncertainty "
            "but useless for triage.",
            "Computational Skepticism for AI, Chapter 11",
            None,
            "honest about uncertainty",
            DUR["B10"],
        )


# ── B11 — CheckBoth ───────────────────────────────────────────────────────────

class B11_CheckBoth(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What to Report", font=DISPLAY, font_size=22, color=TEAL).move_to(UP * 3.1)

        checks = [
            ("Plot the reliability diagram",     "Do predictions spread across the range or pile on the base rate?", TEAL),
            ("Report calibration AND resolution", "One number collapses both — check each separately",               TEAL),
            ("Good aggregate score",              "is NOT evidence the model is useful for individual decisions",     GOLD),
            ("Check subgroups separately",        "aggregate hides local miscalibration in small populations",        CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, action, col) in enumerate(checks):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to(UP * y)
            lbl = Text(name,   font=DISPLAY, font_size=14, color=col).move_to([0.0, y + 0.2,  0])
            act = Text(action, font=MONO,    font_size=12, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(act), run_time=0.3)

        self.wait(DUR["B11"] - 4.5)


# ── B12 — ExampleFraud ────────────────────────────────────────────────────────

class B12_ExampleFraud(Scene):
    def construct(self):
        total = DUR["B12"]
        title = Text("Same Gap — Different Domain", font=DISPLAY, font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("CALIBRATION SCORE", font=DISPLAY, font_size=17, color=TEAL).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("DISCRIMINATION", font=DISPLAY, font_size=17, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.55)

        val_l = Text("ECE = 0.00", font="PT Mono", font_size=22, color=TEAL).move_to(LEFT * 3.2 + UP * 0.65)
        val_r = Text("No signal", font="PT Mono", font_size=22, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 0.65)

        sub_l = Text("PERFECT", font=DISPLAY, font_size=15, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.05)
        sub_r = Text("$5 coffee = $10k wire\n= 2.1%", font="PT Mono", font_size=14, color=INK).move_to(RIGHT * 3.2 + DOWN * 0.1)

        res_l = Text("HONEST", font=DISPLAY, font_size=20, color=TEAL, weight=BOLD).move_to(LEFT * 3.2 + DOWN * 1.1)
        res_r = Text("USELESS", font=DISPLAY, font_size=20, color=CRIMSON, weight=BOLD).move_to(RIGHT * 3.2 + DOWN * 1.1)

        note = Text("Fraud team cannot flag anything — the model has no signal.", font=DISPLAY, font_size=15, color=INK).move_to(DOWN * 2.55)
        note_rect = Rectangle(width=9.5, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.7)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(val_l), Write(val_r), run_time=0.4)
        self.play(Write(sub_l), Write(sub_r), run_time=0.4)
        self.play(FadeIn(res_l), FadeIn(res_r), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.3)
        self.play(Write(note), run_time=0.4)
        self.wait(max(0.5, total - 4.5))
