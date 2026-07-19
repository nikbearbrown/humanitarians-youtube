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
        t1 = Text("The Better the AI Works,", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        t2 = Text("the Worse You Watch It", font=DISPLAY, color=CRIMSON, font_size=36, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── B02 — VigilanceDrain ──────────────────────────────────────────────────────

class B02_VigilanceDrain(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("100 outputs. 100 stamps.", font=DISPLAY, font_size=20, color=GOLD).move_to(UP * 3.1)

        # Output boxes in a row — growing row of checkmarks
        checks = []
        for i in range(5):
            x = -4.0 + i * 2.0
            box = Rectangle(width=1.6, height=0.9, color=TEAL, fill_color=TEAL,
                            fill_opacity=0.15, stroke_width=1.5).move_to([x, 1.3, 0])
            ck  = Text("✓", font=DISPLAY, font_size=22, color=TEAL).move_to([x, 1.3, 0])
            checks.append((box, ck))

        # Vigilance meter bar (draining)
        meter_frame = Rectangle(width=6.0, height=0.7, color=GOLD, fill_opacity=0,
                                stroke_width=2).move_to([0, -0.2, 0])
        meter_lbl   = Text("VIGILANCE", font=DISPLAY, font_size=14, color=GOLD).move_to([-3.8, -0.2, 0])
        meter_full  = Rectangle(width=5.7, height=0.5, color=TEAL, fill_color=TEAL,
                                fill_opacity=0.6, stroke_width=0).move_to([-0.15, -0.2, 0])
        meter_low   = Rectangle(width=1.4, height=0.5, color=CRIMSON, fill_color=CRIMSON,
                                fill_opacity=0.7, stroke_width=0).move_to([-2.45, -0.2, 0])

        # The bad output
        bad_box = Rectangle(width=1.6, height=0.9, color=CRIMSON, fill_color=CRIMSON,
                            fill_opacity=0.20, stroke_width=2).move_to([2.0, 1.3, 0])
        bad_lbl = Text("✗", font=DISPLAY, font_size=22, color=CRIMSON).move_to([2.0, 1.3, 0])
        bad_stamp = Text("STAMPED\nANYWAY", font=DISPLAY, font_size=13, color=CRIMSON).move_to([2.0, -0.9, 0])
        bad_stamp_box = Rectangle(width=2.0, height=0.9, color=CRIMSON, fill_color=CRIMSON,
                                  fill_opacity=0.15, stroke_width=1.5).move_to([2.0, -0.9, 0])

        self.play(Write(title), run_time=0.4)
        for box, ck in checks:
            self.play(GrowFromCenter(box), run_time=0.25)
            self.play(Write(ck), run_time=0.2)
        self.play(GrowFromCenter(meter_frame), run_time=0.4)
        self.play(Write(meter_lbl), run_time=0.3)
        self.play(GrowFromCenter(meter_full), run_time=0.4)
        self.play(Transform(meter_full, meter_low), run_time=0.6)
        self.play(GrowFromCenter(bad_box), run_time=0.4)
        self.play(Write(bad_lbl), run_time=0.3)
        self.play(GrowFromCenter(bad_stamp_box), run_time=0.3)
        self.play(Write(bad_stamp), run_time=0.3)
        self.wait(DUR["B02"] - 5.6)


# ── B04 — OvertrusVsUndertrust ────────────────────────────────────────────────

class B04_OvertrusVsUndertrust(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        hdr_und = Rectangle(width=5.5, height=0.6, color=SLATE, fill_color=SLATE,
                            fill_opacity=0.20, stroke_width=1.5).move_to(LEFT * 3.2 + UP * 2.8)
        hdr_ovr = Rectangle(width=5.5, height=0.6, color=CRIMSON, fill_color=CRIMSON,
                            fill_opacity=0.20, stroke_width=1.5).move_to(RIGHT * 3.2 + UP * 2.8)
        t_und   = Text("UNDERTRUST", font=DISPLAY, font_size=17, color=SLATE).move_to(hdr_und)
        t_ovr   = Text("OVERTRUST", font=DISPLAY, font_size=17, color=CRIMSON).move_to(hdr_ovr)

        body_und = Rectangle(width=5.5, height=3.8, color=SLATE, fill_opacity=0,
                             stroke_width=1.5).move_to(LEFT * 3.2 + DOWN * 0.6)
        body_ovr = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_opacity=0,
                             stroke_width=1.5).move_to(RIGHT * 3.2 + DOWN * 0.6)

        c1 = Text("Systematically discounts\nAI output\nDeployment loses value", font=MONO, font_size=13, color=INK).move_to(LEFT * 3.2 + UP * 0.5)
        c2 = Text("→ VISIBLE IMMEDIATELY", font=DISPLAY, font_size=14, color=SLATE).move_to(LEFT * 3.2 + DOWN * 1.5)

        f1 = Text("Accepts output without\nchecking when it should\ncheck — silently", font=MONO, font_size=13, color=INK).move_to(RIGHT * 3.2 + UP * 0.5)
        f2 = Text("→ NO FLAG. ERROR\nDISCOVERED LATER.", font=DISPLAY, font_size=14, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 1.5)

        self.play(GrowFromCenter(hdr_und), GrowFromCenter(hdr_ovr), run_time=0.5)
        self.play(Write(t_und), Write(t_ovr), run_time=0.5)
        self.play(GrowFromCenter(body_und), GrowFromCenter(body_ovr), run_time=0.5)
        self.play(Write(c1), Write(f1), run_time=0.5)
        self.play(Write(c2), Write(f2), run_time=0.5)
        self.wait(DUR["B04"] - 3.5)


# ── B05 — VerifyCost ──────────────────────────────────────────────────────────

class B05_VerifyCost(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Economics, Not Character", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)

        steps = [
            ("AI has been right 100 times",      "verification costs attention each time",      TEAL),
            ("Rational response: check less",     "economics acting on attention — not a flaw",  GOLD),
            ("AI eventually makes an error",      "verification habit has already eroded",        CRIMSON),
            ("Error reaches user undetected",     "because the cost structure pushed that way",   CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, desc, col) in enumerate(steps):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.5).move_to(UP * y)
            t1  = Text(name, font=DISPLAY, font_size=15, color=col).move_to([0.0, y + 0.22, 0])
            t2  = Text(desc, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(t1), run_time=0.3)
            self.play(Write(t2), run_time=0.3)

        self.wait(DUR["B05"] - 4.5)


# ── B07 — SignalRate ──────────────────────────────────────────────────────────

class B07_SignalRate(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Low Signal Rate → Degraded Monitoring", font=DISPLAY, font_size=20, color=GOLD).move_to(UP * 3.1)

        # Signal rate meter
        rate_frame = Rectangle(width=8.0, height=0.9, color=GOLD, fill_opacity=0,
                               stroke_width=2).move_to([0, 1.2, 0])
        rate_lbl   = Text("SIGNAL RATE (how often AI fails)", font=DISPLAY, font_size=13, color=GOLD).move_to([0, 2.0, 0])
        rate_low   = Rectangle(width=0.7, height=0.7, color=CRIMSON, fill_color=CRIMSON,
                               fill_opacity=0.7, stroke_width=0).move_to([-3.65, 1.2, 0])

        # Monitoring quality drops
        mon_frame = Rectangle(width=8.0, height=0.9, color=TEAL, fill_opacity=0,
                              stroke_width=2).move_to([0, -0.3, 0])
        mon_lbl   = Text("MONITORING QUALITY", font=DISPLAY, font_size=13, color=TEAL).move_to([0, -1.1, 0])
        mon_high  = Rectangle(width=7.7, height=0.7, color=TEAL, fill_color=TEAL,
                              fill_opacity=0.6, stroke_width=0).move_to([0.15, -0.3, 0])
        mon_low2  = Rectangle(width=1.2, height=0.7, color=CRIMSON, fill_color=CRIMSON,
                              fill_opacity=0.6, stroke_width=0).move_to([-3.4, -0.3, 0])

        arrow = Line([0, 0.7, 0], [0, 0.1, 0], color=GOLD, stroke_width=2.5)
        arrow_lbl = Text("decay", font=MONO, font_size=13, color=GOLD).move_to([0.8, 0.4, 0])

        caption = Text("The rare error arrives when checking has eroded.",
                       font=DISPLAY, font_size=15, color=CRIMSON).move_to(DOWN * 2.4)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(rate_frame), run_time=0.4)
        self.play(Write(rate_lbl), run_time=0.3)
        self.play(GrowFromCenter(rate_low), run_time=0.4)
        self.play(GrowFromCenter(mon_frame), run_time=0.4)
        self.play(Write(mon_lbl), run_time=0.3)
        self.play(GrowFromCenter(mon_high), run_time=0.4)
        self.play(GrowFromEdge(arrow, UP), run_time=0.4)
        self.play(Write(arrow_lbl), run_time=0.3)
        self.play(Transform(mon_high, mon_low2), run_time=0.6)
        self.play(Write(caption), run_time=0.4)
        self.wait(DUR["B07"] - 5.0)


# ── B08 — QuoteOvertrust ──────────────────────────────────────────────────────

class B08_QuoteOvertrust(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Overtrust does not produce immediate flags. "
            "It produces uncaught errors that are discovered later, "
            "often by the affected user.",
            "Computational Skepticism for AI, Chapter 9",
            None,
            "discovered later",
            DUR["B08"],
        )


# ── B09 — CalibratedTrust ─────────────────────────────────────────────────────

class B09_CalibratedTrust(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Calibrated Trust", font=DISPLAY, font_size=22, color=TEAL).move_to(UP * 3.1)

        cols = [
            ("NOT THIS",   "Trust based on\nrecent performance\n(the AI has been right!)",  CRIMSON),
            ("THIS",       "Trust based on\nactual measured reliability\nfor this case type", TEAL),
            ("HOW",        "Verification workflows\nthat hold even when\nAI seems fine",      TEAL),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, desc, col) in enumerate(cols):
            x = (i - 1) * 4.3
            box = Rectangle(width=3.8, height=2.8, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to([x, 0.4, 0])
            lbl = Text(name, font=DISPLAY, font_size=18, color=col).move_to([x, 1.4, 0])
            desc_txt = Text(desc, font=MONO, font_size=13, color=INK).move_to([x, 0.0, 0])
            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(desc_txt), run_time=0.3)

        note = Text("The track record is not evidence checking is safe — it's when it's most dangerous.",
                    font=DISPLAY, font_size=13, color=GOLD).move_to(DOWN * 2.4)
        self.play(Write(note), run_time=0.5)
        self.wait(DUR["B09"] - 4.3)


# ── B10 — QuoteCalibrated ─────────────────────────────────────────────────────

class B10_QuoteCalibrated(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Calibrated trust requires knowing the AI's actual reliability "
            "for this kind of case, and acting on that knowledge consistently.",
            "Computational Skepticism for AI, Chapter 9",
            None,
            "acting on that knowledge",
            DUR["B10"],
        )


# ── B11 — WorkflowFix ─────────────────────────────────────────────────────────

class B11_WorkflowFix(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Workflow That Supports Discipline", font=DISPLAY, font_size=20, color=TEAL).move_to(UP * 3.1)

        rows = [
            ("Checklists that run even on streaks",  "verification is not optional when AI is performing",  TEAL),
            ("Verification steps that are required", "not left to the reviewer's sense of whether to check", TEAL),
            ("Good track record = more caution",     "not less — highest overtrust risk at peak performance", GOLD),
            ("Skipping when tempted",                "is precisely when the error has been waiting",          CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, action, col) in enumerate(rows):
            y = 1.7 - i * 1.25
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to(UP * y)
            lbl = Text(name,   font=DISPLAY, font_size=15, color=col).move_to([0.0, y + 0.2,  0])
            act = Text(action, font=MONO,    font_size=12, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(act), run_time=0.3)

        self.wait(DUR["B11"] - 4.5)


# ── B12 — ExampleVigilance ────────────────────────────────────────────────────

class B12_ExampleVigilance(Scene):
    def construct(self):
        total = DUR["B12"]
        title = Text("Circuit board QC — vigilance over time", font=DISPLAY, font_size=19, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("Month 1 — active checking", font=DISPLAY, font_size=15, color=TEAL).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("Month 5 — degraded monitoring", font=DISPLAY, font_size=14, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.55)

        val_l1 = Text("Review time: 25 sec / board", font=MONO, font_size=13, color=TEAL).move_to(LEFT * 3.2 + UP * 0.65)
        val_l2 = Text("Error catch rate: high", font=MONO, font_size=13, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.05)
        val_l3 = Text("Workflow: systematic", font=MONO, font_size=13, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.75)

        val_r1 = Text("Review time: 3 sec / board", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 0.65)
        val_r2 = Text("Batch 17: defects missed ✗", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.05)
        val_r3 = Text("340 units shipped ✗", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.75)

        note_rect = Rectangle(width=9.5, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)
        note_txt = Text("AI accuracy unchanged — supervision had decayed (illustrative)",
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
