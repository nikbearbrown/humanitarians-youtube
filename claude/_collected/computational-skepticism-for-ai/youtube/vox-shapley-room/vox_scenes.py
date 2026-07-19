import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))

from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,
    "B02": 10.0, "B04": 9.0, "B05": 10.0,
    "B07": 9.0,  "B08": 10.0, "B09": 8.0,
    "B10": 10.0, "B11": 7.0, "B12": 13.0,
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
        t1 = Text("Why Fair Credit-Splitting", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        t2 = Text("Has Exactly One Answer", font=DISPLAY, color=CRIMSON, font_size=36, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── B02 — TeamEffort ──────────────────────────────────────────────────────────

class B02_TeamEffort(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Three feature chips
        chips = VGroup(
            LabelChip("INCOME",    color=TEAL),
            LabelChip("DEBT RATIO", color=CRIMSON),
            LabelChip("ZIP CODE",  color=SLATE),
        ).arrange(RIGHT, buff=0.6).move_to(UP * 0.5)

        # Question-mark credit chips below each
        q_chips = VGroup(*[
            LabelChip("?", color=GOLD)
            for _ in range(3)
        ])
        for i, qc in enumerate(q_chips):
            qc.move_to(chips[i].get_center() + DOWN * 1.1)

        # Bracket above: 55% → 72%
        bracket_rect = Rectangle(
            width=7.2, height=0.55,
            color=GOLD, fill_color=GOLD, fill_opacity=0.12,
            stroke_width=2,
        ).move_to(chips.get_top() + UP * 0.65)

        bracket_txt = Text(
            "55% → 72%  (+17 pts to distribute)",
            font=MONO, font_size=22, color=GOLD,
        ).move_to(bracket_rect)

        self.play(GrowFromCenter(bracket_rect), run_time=0.7)
        self.play(Write(bracket_txt), run_time=0.7)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in chips], lag_ratio=0.3), run_time=1.0)
        self.play(LaggedStart(*[GrowFromCenter(q) for q in q_chips], lag_ratio=0.3), run_time=0.9)
        self.wait(DUR["B02"] - 3.3)


# ── B04 — OrderDepend ─────────────────────────────────────────────────────────

class B04_OrderDepend(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Two column rectangles
        col_left  = Rectangle(width=5.2, height=3.0, color=INK, stroke_width=2).move_to(LEFT * 3.2)
        col_right = Rectangle(width=5.2, height=3.0, color=INK, stroke_width=2).move_to(RIGHT * 3.2)

        lbl_left  = Text("Order 1 — Income First",  font=DISPLAY, font_size=22, color=TEAL).move_to(col_left.get_top()   + DOWN * 0.4)
        lbl_right = Text("Order 2 — Income Last",   font=DISPLAY, font_size=22, color=CRIMSON).move_to(col_right.get_top() + DOWN * 0.4)

        seq_left  = Text("Income → Debt → Zip", font=MONO, font_size=18, color=INK).move_to(col_left.get_center()  + UP * 0.4)
        seq_right = Text("Debt → Zip → Income", font=MONO, font_size=18, color=INK).move_to(col_right.get_center() + UP * 0.4)

        val_left  = Text("Income adds  +0.08", font=MONO, font_size=20, color=TEAL).move_to(col_left.get_center()  + DOWN * 0.5)
        val_right = Text("Income adds  +0.06", font=MONO, font_size=20, color=CRIMSON).move_to(col_right.get_center() + DOWN * 0.5)

        note = Text("Same feature, different coalition → different credit", font=DISPLAY, font_size=18, color=GOLD).move_to(DOWN * 2.3)

        self.play(GrowFromCenter(col_left), GrowFromCenter(col_right), run_time=0.8)
        self.play(Write(lbl_left), Write(lbl_right), run_time=0.6)
        self.play(Write(seq_left), Write(seq_right), run_time=0.6)
        self.play(Write(val_left), Write(val_right), run_time=0.6)
        self.play(Write(note), run_time=0.6)
        self.wait(DUR["B04"] - 3.2)


# ── B05 — AllOrderings ────────────────────────────────────────────────────────

class B05_AllOrderings(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        rows = [
            ("Income → Debt → Zip",   "+0.08"),
            ("Income → Zip → Debt",   "+0.08"),
            ("Debt → Income → Zip",   "+0.07"),
            ("Zip → Income → Debt",   "+0.09"),
            ("Debt → Zip → Income",   "+0.06"),
            ("Zip → Debt → Income",   "+0.06"),
        ]

        # Header rectangle
        hdr_rect = Rectangle(width=8.5, height=0.5, color=SLATE, fill_color=SLATE, fill_opacity=0.2, stroke_width=1.5)
        hdr_rect.move_to(UP * 2.8)
        hdr_txt  = Text("Ordering              Income credit", font=MONO, font_size=18, color=INK).move_to(hdr_rect)

        self.play(GrowFromCenter(hdr_rect), run_time=0.4)
        self.play(Write(hdr_txt), run_time=0.4)

        row_grp = []
        for i, (ordering, credit) in enumerate(rows):
            y = 2.2 - i * 0.55
            r = Rectangle(width=8.5, height=0.48, color=INK, fill_opacity=0, stroke_width=0.8).move_to(UP * y)
            t = Text(f"{ordering:<28}{credit}", font=MONO, font_size=17, color=INK).move_to(UP * y)
            self.play(GrowFromCenter(r), Write(t), run_time=0.22)
            row_grp.append(VGroup(r, t))

        # Average = SHAPLEY VALUE
        avg_rect = Rectangle(width=8.5, height=0.55, color=GOLD, fill_color=GOLD, fill_opacity=0.15, stroke_width=2)
        avg_rect.move_to(DOWN * 1.3)
        avg_txt  = Text("AVERAGE  =  0.073   (Income Shapley value)", font=MONO, font_size=18, color=GOLD).move_to(avg_rect)

        self.play(GrowFromCenter(avg_rect), run_time=0.5)
        self.play(Write(avg_txt), run_time=0.5)
        self.wait(DUR["B05"] - 4.5)


# ── B07 — RoomConcept ─────────────────────────────────────────────────────────

class B07_RoomConcept(Scene):
    def construct(self):
        DISPLAY = "Montserrat"

        # Room outline
        room = Rectangle(width=2.0, height=4.2, color=INK, stroke_width=2.5).move_to(LEFT * 1.0)

        # Bar segments stacked from bottom, anchored at bottom of room
        _base_y = room.get_bottom()[1]
        _room_h = 4.2

        h1 = _room_h * 0.50  # INCOME: 50% of room
        h2 = _room_h * 0.32  # DEBT:   32%
        h3 = _room_h * 0.18  # ZIP:    18%

        bar1 = Rectangle(width=1.8, height=h1, color=TEAL,   fill_color=TEAL,   fill_opacity=0.7, stroke_width=0)
        bar2 = Rectangle(width=1.8, height=h2, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.7, stroke_width=0)
        bar3 = Rectangle(width=1.8, height=h3, color=SLATE,  fill_color=SLATE,  fill_opacity=0.7, stroke_width=0)

        bar1.align_to(room, DOWN).shift(UP * 0.1)
        bar2.next_to(bar1, UP, buff=0)
        bar3.next_to(bar2, UP, buff=0)

        lbl1 = Text("INCOME",     font=DISPLAY, font_size=16, color=WHITE).move_to(bar1)
        lbl2 = Text("DEBT RATIO", font=DISPLAY, font_size=14, color=WHITE).move_to(bar2)
        lbl3 = Text("ZIP CODE",   font=DISPLAY, font_size=13, color=WHITE).move_to(bar3)

        # Door label
        door_lbl = Text("THE ROOM", font=DISPLAY, font_size=20, color=INK).next_to(room, UP, buff=0.3)

        # Right side: labels for each contribution
        c1 = Text("+0.08",  font="PT Mono", font_size=22, color=TEAL).move_to(RIGHT * 2.8 + UP * (_base_y + h1/2 - room.get_center()[1]))
        c2 = Text("+0.06",  font="PT Mono", font_size=22, color=CRIMSON).move_to(RIGHT * 2.8 + UP * (_base_y + h1 + h2/2 - room.get_center()[1]))
        c3 = Text("+0.03",  font="PT Mono", font_size=22, color=SLATE).move_to(RIGHT * 2.8 + UP * (_base_y + h1 + h2 + h3/2 - room.get_center()[1]))

        self.play(GrowFromCenter(room), Write(door_lbl), run_time=0.6)
        self.play(GrowFromEdge(bar1, DOWN), run_time=0.6)
        self.play(Write(lbl1), Write(c1), run_time=0.4)
        self.play(GrowFromEdge(bar2, DOWN), run_time=0.5)
        self.play(Write(lbl2), Write(c2), run_time=0.4)
        self.play(GrowFromEdge(bar3, DOWN), run_time=0.5)
        self.play(Write(lbl3), Write(c3), run_time=0.4)
        self.wait(DUR["B07"] - 3.9)


# ── B08 — AccumAverage ────────────────────────────────────────────────────────

class B08_AccumAverage(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Shapley Values — Loan Applicant", font=DISPLAY, font_size=24, color=INK).move_to(UP * 2.8)

        # Three value chips
        chip_inc  = LabelChip("INCOME  = 0.073", color=TEAL)
        chip_debt = LabelChip("DEBT    = 0.062", color=CRIMSON)
        chip_zip  = LabelChip("ZIP     = 0.035", color=SLATE)

        chip_inc.move_to(UP * 1.4)
        chip_debt.move_to(UP * 0.4)
        chip_zip.move_to(DOWN * 0.6)

        # Sum line
        sum_rect = Rectangle(width=6.5, height=0.55, color=GOLD, fill_color=GOLD, fill_opacity=0.15, stroke_width=2)
        sum_rect.move_to(DOWN * 1.7)
        sum_txt  = Text("0.073 + 0.062 + 0.035  =  0.17  ✓", font=MONO, font_size=20, color=GOLD).move_to(sum_rect)

        note = Text("Efficiency: credits sum exactly to the prediction deviation",
                    font=DISPLAY, font_size=16, color=INK).move_to(DOWN * 2.6)

        self.play(Write(title), run_time=0.5)
        self.play(GrowFromCenter(chip_inc),  run_time=0.4)
        self.play(GrowFromCenter(chip_debt), run_time=0.4)
        self.play(GrowFromCenter(chip_zip),  run_time=0.4)
        self.play(GrowFromCenter(sum_rect),  run_time=0.4)
        self.play(Write(sum_txt), run_time=0.5)
        self.play(Write(note), run_time=0.5)
        self.wait(DUR["B08"] - 3.5)


# ── B09 — QuoteRoom ───────────────────────────────────────────────────────────

class B09_QuoteRoom(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Think of the features entering a room in a random order. "
            "Every ordering is equally likely. When a feature enters, "
            "it finds some coalition already there. The Shapley value "
            "is the average change in the prediction across all those "
            "random arrivals.",
            "Computational Skepticism for AI, Chapter 5",
            None,
            "random arrivals",
            DUR["B09"],
        )


# ── B10 — Uniqueness ─────────────────────────────────────────────────────────

class B10_Uniqueness(Scene):
    def construct(self):
        DISPLAY = "Montserrat"

        title = Text("The Four Axioms — Unique Attribution", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.0)

        axioms = [
            ("EFFICIENCY",  "Credits sum to the full prediction deviation",   TEAL),
            ("SYMMETRY",    "Identical features get identical credit",         TEAL),
            ("DUMMY",       "Unused features get zero attribution",            TEAL),
            ("ADDITIVITY",  "Credits compose cleanly across models",           TEAL),
        ]

        boxes = []
        for i, (name, desc, col) in enumerate(axioms):
            y = 1.8 - i * 1.2
            box = Rectangle(width=10.0, height=0.9, color=col, fill_color=col, fill_opacity=0.10, stroke_width=1.8)
            box.move_to(UP * y)
            lbl = Text(f"{name:<14} {desc}", font=DISPLAY, font_size=18, color=INK).move_to(box)
            boxes.append(VGroup(box, lbl))

        result = Text("→ Shapley values are the UNIQUE attribution satisfying all four",
                      font=DISPLAY, font_size=17, color=GOLD).move_to(DOWN * 2.7)

        self.play(Write(title), run_time=0.5)
        for bg in boxes:
            self.play(GrowFromCenter(bg[0]), run_time=0.35)
            self.play(Write(bg[1]), run_time=0.35)
        self.play(Write(result), run_time=0.6)
        self.wait(DUR["B10"] - 3.8)


# ── B11 — QuoteLimits ────────────────────────────────────────────────────────

class B11_QuoteLimits(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The attribution to zip code is a real number describing "
            "the model's behavior, and it tells you nothing about the world.",
            "Computational Skepticism for AI, Chapter 5",
            None,
            "nothing about the world",
            DUR["B11"],
        )


# ── B12 — ExampleShapley ──────────────────────────────────────────────────────

class B12_ExampleShapley(Scene):
    def construct(self):
        total = DUR["B12"]
        title = Text("Recommendation Model — credit attribution", font=DISPLAY, font_size=19, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("Shapley (all 6 orderings)", font=DISPLAY, font_size=15, color=TEAL).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("Naive (one ordering)", font=DISPLAY, font_size=15, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.55)

        val_l1 = Text("Reading time: +0.14", font=MONO, font_size=13, color=TEAL).move_to(LEFT * 3.2 + UP * 0.65)
        val_l2 = Text("Scroll depth: +0.06", font=MONO, font_size=13, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.05)
        val_l3 = Text("Clicks: +0.03", font=MONO, font_size=13, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.75)
        val_l4 = Text("Sum: 0.23 ✓", font=MONO, font_size=14, color=GOLD).move_to(LEFT * 3.2 + DOWN * 1.35)

        val_r1 = Text("Reading time first: +0.17", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 0.65)
        val_r2 = Text("Reading time last: +0.09", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.05)
        val_r3 = Text("Changes with ordering ✗", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.75)

        note_rect = Rectangle(width=9.5, height=0.52, fill_color=TEAL, fill_opacity=0.10,
                              stroke_width=1.5, color=TEAL).move_to(DOWN * 2.55)
        note_txt = Text("Shapley: the unique attribution satisfying efficiency + symmetry + dummy + additivity (illustrative)",
                        font=MONO, font_size=10, color=TEAL).move_to(DOWN * 2.55)

        self.play(Write(title), run_time=0.5)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.6)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(val_l1), Write(val_r1), run_time=0.4)
        self.play(Write(val_l2), Write(val_r2), run_time=0.4)
        self.play(Write(val_l3), Write(val_r3), run_time=0.4)
        self.play(Write(val_l4), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.4)
        self.play(Write(note_txt), run_time=0.4)
        self.wait(max(0.5, total - 4.5))
