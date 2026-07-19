import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))

from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,
    "B02": 11.0, "B04": 9.0, "B05": 9.0,
    "B07": 9.0,  "B08": 8.0, "B09": 9.0,
    "B10": 7.0,  "B11": 8.0, "B12": 12.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ── B01 — Title ───────────────────────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why the Average That Clears the Model", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Hides the Patient It Harms", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── B02 — AggregateHides ──────────────────────────────────────────────────────

class B02_AggregateHides(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Hospital AI — Passes Review", font=DISPLAY, font_size=20, color=TEAL).move_to(UP * 3.1)

        # Global ECE box
        global_box = Rectangle(width=4.5, height=2.0, color=TEAL, fill_color=TEAL,
                               fill_opacity=0.15, stroke_width=2).move_to(LEFT * 3.3 + UP * 0.8)
        global_lbl = Text("GLOBAL ECE", font=DISPLAY, font_size=15, color=TEAL).move_to(LEFT * 3.3 + UP * 1.4)
        global_val = Text("0.018   ✓", font=MONO, font_size=20, color=TEAL).move_to(LEFT * 3.3 + UP * 0.8)
        global_sub = Text("LOOKS FINE", font=DISPLAY, font_size=13, color=TEAL).move_to(LEFT * 3.3 + UP * 0.2)

        # Subgroup box — flagged
        sub_box = Rectangle(width=4.5, height=2.0, color=CRIMSON, fill_color=CRIMSON,
                            fill_opacity=0.15, stroke_width=2).move_to(RIGHT * 3.3 + UP * 0.8)
        sub_lbl = Text("ELDERLY SUBGROUP ECE", font=DISPLAY, font_size=13, color=CRIMSON).move_to(RIGHT * 3.3 + UP * 1.4)
        sub_val = Text("0.044   ✗", font=MONO, font_size=20, color=CRIMSON).move_to(RIGHT * 3.3 + UP * 0.8)
        sub_sub = Text("2.4× GLOBAL — FLAGGED", font=DISPLAY, font_size=12, color=CRIMSON).move_to(RIGHT * 3.3 + UP * 0.2)

        caption = Text("Both numbers correct. One was hiding the other.",
                       font=DISPLAY, font_size=15, color=GOLD).move_to(DOWN * 1.8)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(global_box), run_time=0.4)
        self.play(Write(global_lbl), Write(global_val), Write(global_sub), run_time=0.4)
        self.play(GrowFromCenter(sub_box), run_time=0.4)
        self.play(Write(sub_lbl), Write(sub_val), Write(sub_sub), run_time=0.4)
        self.play(Write(caption), run_time=0.4)
        self.wait(DUR["B02"] - 3.4)


# ── B04 — SizeWeight ──────────────────────────────────────────────────────────

class B04_SizeWeight(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Size-Weighted Average", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)

        # Large group bar
        big_box = Rectangle(width=7.0, height=1.2, color=TEAL, fill_color=TEAL,
                            fill_opacity=0.20, stroke_width=2).move_to([-1.0, 1.4, 0])
        big_lbl = Text("ADULT GROUP — 8,420 patients — ECE 0.019", font=MONO, font_size=13, color=TEAL).move_to([-1.0, 1.4, 0])

        # Small group bar
        sm_box = Rectangle(width=1.2, height=1.2, color=CRIMSON, fill_color=CRIMSON,
                           fill_opacity=0.25, stroke_width=2).move_to([3.7, 1.4, 0])
        sm_lbl = Text("ELDERLY\n95 cases\nECE 0.103", font=MONO, font_size=10, color=CRIMSON).move_to([3.7, 1.4, 0])

        # Arrow to aggregate
        arr = Line([0.5, 0.7, 0], [0.5, -0.1, 0], color=GOLD, stroke_width=2.5)

        agg_box = Rectangle(width=8.5, height=1.0, color=SLATE, fill_color=SLATE,
                            fill_opacity=0.15, stroke_width=2).move_to([0, -0.7, 0])
        agg_lbl = Text("AGGREGATE ECE = 0.018   (weighted by N)", font=MONO, font_size=14, color=SLATE).move_to([0, -0.7, 0])

        note = Text("Elderly miscalibration contributes <1% of the weight.",
                    font=DISPLAY, font_size=14, color=CRIMSON).move_to(DOWN * 1.8)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(big_box), run_time=0.4)
        self.play(Write(big_lbl), run_time=0.4)
        self.play(GrowFromCenter(sm_box), run_time=0.4)
        self.play(Write(sm_lbl), run_time=0.3)
        self.play(GrowFromEdge(arr, UP), run_time=0.4)
        self.play(GrowFromCenter(agg_box), run_time=0.4)
        self.play(Write(agg_lbl), run_time=0.4)
        self.play(Write(note), run_time=0.4)
        self.wait(DUR["B04"] - 4.1)


# ── B05 — CurvesMerge ─────────────────────────────────────────────────────────

class B05_CurvesMerge(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Reliability Diagram: Two Curves, One Aggregate", font=DISPLAY, font_size=18, color=GOLD).move_to(UP * 3.1)

        # Axis
        ax = Rectangle(width=5.5, height=5.5, color=SLATE, fill_opacity=0,
                       stroke_width=1.5).move_to([-0.5, 0.0, 0])
        diag = Line([-3.25, -2.75, 0], [2.25, 2.75, 0], color=SLATE, stroke_width=1, stroke_opacity=0.4)

        # Large group dots — on diagonal, TEAL
        teal_dots = [
            Dot(radius=0.13, color=TEAL).move_to([-2.0 + i * 1.0, -1.5 + i * 1.0, 0])
            for i in range(5)
        ]

        # Small group dots — off diagonal, CRIMSON
        crimson_dots = [
            Dot(radius=0.13, color=CRIMSON).move_to([-1.5 + i * 0.9, -0.5 + i * 0.3, 0])
            for i in range(3)
        ]

        # Aggregate dot — on diagonal, GOLD
        agg_dot = Dot(radius=0.18, color=GOLD).move_to([0.0, 0.0, 0])
        agg_lbl = Text("AGGREGATE\n(hides red)", font=MONO, font_size=11, color=GOLD).move_to([1.5, 0.0, 0])

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(ax), run_time=0.4)
        self.play(Create(diag), run_time=0.3)
        for d in teal_dots:
            self.play(GrowFromCenter(d), run_time=0.2)
        for d in crimson_dots:
            self.play(GrowFromCenter(d), run_time=0.2)
        self.play(GrowFromCenter(agg_dot), run_time=0.4)
        self.play(Write(agg_lbl), run_time=0.3)
        self.wait(DUR["B05"] - 4.2)


# ── B07 — SubgroupTable ───────────────────────────────────────────────────────

class B07_SubgroupTable(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Subgroup Breakdown", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)

        rows = [
            ("Adult, 18–64",   "N=8,420", "ECE 0.019", "OK",       TEAL),
            ("Elderly, 65+",   "N=2,850", "ECE 0.044", "FLAGGED",  CRIMSON),
            ("Rare-disease",   "N=95",    "ECE 0.103", "FLAGGED",  CRIMSON),
            ("GLOBAL",         "N=12,555","ECE 0.018", "PASSES",   SLATE),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, n, ece, flag, col) in enumerate(rows):
            y = 1.7 - i * 1.2
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.12, stroke_width=1.5).move_to(UP * y)
            t_name = Text(name, font=DISPLAY, font_size=14, color=col).move_to([-3.5, y, 0])
            t_n    = Text(n,    font=MONO,    font_size=13, color=INK).move_to([-0.5, y, 0])
            t_ece  = Text(ece,  font=MONO,    font_size=13, color=col).move_to([1.8,  y, 0])
            t_flag = Text(flag, font=DISPLAY, font_size=13, color=col).move_to([4.0,  y, 0])
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(t_name), Write(t_n), Write(t_ece), Write(t_flag), run_time=0.35)

        self.wait(DUR["B07"] - 4.0)


# ── B08 — QuoteAggregate ──────────────────────────────────────────────────────

class B08_QuoteAggregate(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The single most important limitation of aggregate calibration metrics "
            "is that they are aggregate. A system with low global calibration error "
            "can be catastrophically miscalibrated for a specific subgroup "
            "if that subgroup is small enough to be washed out in the overall average.",
            "Computational Skepticism for AI, Chapter 11",
            None,
            "washed out",
            DUR["B08"],
        )


# ── B09 — SubgroupCheck ───────────────────────────────────────────────────────

class B09_SubgroupCheck(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What to Compute Separately", font=DISPLAY, font_size=20, color=TEAL).move_to(UP * 3.1)

        checks = [
            ("DEMOGRAPHIC SUBGROUPS",  "Age, race, sex — every named group\nin the deployment population",  TEAL),
            ("SEVERITY STRATA",        "High-risk vs low-risk populations\noften have different error profiles",  TEAL),
            ("OOD POPULATIONS",        "Any group you suspect differs\nfrom training distribution",              TEAL),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, desc, col) in enumerate(checks):
            x = (i - 1) * 4.3
            box = Rectangle(width=3.8, height=2.6, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to([x, 0.4, 0])
            lbl = Text(name, font=DISPLAY, font_size=14, color=col).move_to([x, 1.3, 0])
            desc_txt = Text(desc, font=MONO, font_size=12, color=INK).move_to([x, 0.0, 0])
            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(desc_txt), run_time=0.3)

        note = Text("The aggregate is not the patient in front of you.",
                    font=DISPLAY, font_size=15, color=GOLD).move_to(DOWN * 2.2)
        self.play(Write(note), run_time=0.4)
        self.wait(DUR["B09"] - 4.2)


# ── B10 — QuotePatient ────────────────────────────────────────────────────────

class B10_QuotePatient(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The aggregate metric is evidence the model is calibrated on average. "
            "It is not evidence the model is calibrated "
            "for the patient in front of you.",
            "Computational Skepticism for AI, Chapter 11",
            None,
            "patient in front of you",
            DUR["B10"],
        )


# ── B11 — ReportBoth ──────────────────────────────────────────────────────────

class B11_ReportBoth(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What to Report", font=DISPLAY, font_size=22, color=TEAL).move_to(UP * 3.1)

        rows = [
            ("Global ECE",             "Report it — context for the deployment",                     TEAL),
            ("Max subgroup ECE",        "Flag if > 2× global — concealment signal",                  CRIMSON),
            ("Distribution of subgroup ECEs", "Not just the max — the full spread matters",          GOLD),
            ("Global ECE alone",       "is the cover story, not the finding",                        CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, action, col) in enumerate(rows):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to(UP * y)
            lbl = Text(name,   font=DISPLAY, font_size=15, color=col).move_to([0.0, y + 0.2,  0])
            act = Text(action, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(act), run_time=0.3)

        self.wait(DUR["B11"] - 4.5)


# ── B12 — ExampleSubgroup ─────────────────────────────────────────────────────

class B12_ExampleSubgroup(Scene):
    def construct(self):
        total = DUR["B12"]
        title = Text("Insurance pricing model — calibration audit", font=DISPLAY, font_size=19, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("Aggregate metric", font=DISPLAY, font_size=16, color=TEAL).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("Subgroup breakdown", font=DISPLAY, font_size=16, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.55)

        val_l1 = Text("Overall ECE: 0.03 ✓", font=MONO, font_size=14, color=TEAL).move_to(LEFT * 3.2 + UP * 0.65)
        val_l2 = Text("Threshold: 0.05", font=MONO, font_size=13, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.05)
        val_l3 = Text("Status: APPROVED", font=MONO, font_size=14, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.75)

        val_r1 = Text("General (92%): ECE 0.02 ✓", font=MONO, font_size=12, color=INK).move_to(RIGHT * 3.2 + UP * 0.65)
        val_r2 = Text("Elderly rural (8%): ECE 0.21 ✗", font=MONO, font_size=12, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.05)
        val_r3 = Text("Claims: +18% over-prediction ✗", font=MONO, font_size=12, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.75)

        note_rect = Rectangle(width=9.5, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)
        note_txt = Text("aggregate ECE 0.03 hides subgroup ECE 0.21 — 8% of applicants (illustrative)",
                        font=MONO, font_size=11, color=CRIMSON).move_to(DOWN * 2.55)

        self.play(Write(title), run_time=0.5)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.6)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(val_l1), Write(val_r1), run_time=0.4)
        self.play(Write(val_l2), Write(val_r2), run_time=0.4)
        self.play(Write(val_l3), Write(val_r3), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.4)
        self.play(Write(note_txt), run_time=0.4)
        self.wait(max(0.5, total - 4.2))
