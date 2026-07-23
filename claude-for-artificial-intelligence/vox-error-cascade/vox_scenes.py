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
        t1 = Text("You Validated Each Agent at 1%.", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        t2 = Text("The System Fails at 30%.", font=DISPLAY, color=CRIMSON, font_size=32, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── B02 — CascadeOpen ─────────────────────────────────────────────────────────

class B02_CascadeOpen(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Three agent boxes across the screen
        agents = []
        for i, label in enumerate(["AGENT A", "AGENT B", "AGENT C"]):
            x = (i - 1) * 3.8
            box = Rectangle(width=2.8, height=1.4, color=TEAL, fill_color=TEAL,
                            fill_opacity=0.12, stroke_width=2).move_to([x, 1.2, 0])
            lbl = Text(label, font=DISPLAY, font_size=16, color=TEAL).move_to([x, 1.5, 0])
            pct = Text("1% error", font=MONO, font_size=13, color=TEAL).move_to([x, 0.9, 0])
            agents.append((box, lbl, pct, x))

        # Arrows between agents
        arr1 = Line([-2.3, 1.2, 0], [-1.8, 1.2, 0], color=TEAL, stroke_width=2.5)
        arr2 = Line([1.5, 1.2, 0], [2.0, 1.2, 0], color=TEAL, stroke_width=2.5)

        # Error accumulation dots
        dot_a = Dot(radius=0.12, color=CRIMSON).move_to([-3.8, 1.2, 0])
        dot_b = Dot(radius=0.17, color=CRIMSON).move_to([0, 1.2, 0])
        dot_c = Dot(radius=0.24, color=CRIMSON).move_to([3.8, 1.2, 0])

        # Output failure
        out_box = Rectangle(width=3.2, height=1.0, color=CRIMSON, fill_color=CRIMSON,
                            fill_opacity=0.18, stroke_width=2).move_to([0, -0.8, 0])
        out_lbl = Text("PIPELINE OUTPUT: 30% FAILURE", font=DISPLAY, font_size=15, color=CRIMSON).move_to([0, -0.8, 0])

        caption = Text("No individual agent was broken.", font=DISPLAY, font_size=16, color=GOLD).move_to(DOWN * 2.3)

        # Animate
        for box, lbl, pct, x in agents:
            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(Write(lbl), Write(pct), run_time=0.3)
        self.play(GrowFromEdge(arr1, LEFT), GrowFromEdge(arr2, LEFT), run_time=0.4)
        self.play(GrowFromCenter(dot_a), run_time=0.3)
        self.play(GrowFromCenter(dot_b), run_time=0.3)
        self.play(GrowFromCenter(dot_c), run_time=0.3)
        self.play(GrowFromCenter(out_box), run_time=0.4)
        self.play(Write(out_lbl), run_time=0.3)
        self.play(Write(caption), run_time=0.4)
        self.wait(DUR["B02"] - 4.1)


# ── B04 — IsolationVsPipeline ─────────────────────────────────────────────────

class B04_IsolationVsPipeline(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        hdr_iso  = Rectangle(width=5.5, height=0.6, color=TEAL,   fill_color=TEAL,   fill_opacity=0.20, stroke_width=1.5).move_to(LEFT * 3.2 + UP * 2.8)
        hdr_pipe = Rectangle(width=5.5, height=0.6, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.20, stroke_width=1.5).move_to(RIGHT * 3.2 + UP * 2.8)
        t_iso    = Text("ISOLATION TESTING", font=DISPLAY, font_size=16, color=TEAL).move_to(hdr_iso)
        t_pipe   = Text("PIPELINE REALITY", font=DISPLAY, font_size=16, color=CRIMSON).move_to(hdr_pipe)

        body_iso  = Rectangle(width=5.5, height=3.8, color=TEAL,   fill_opacity=0, stroke_width=1.5).move_to(LEFT * 3.2 + DOWN * 0.6)
        body_pipe = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_opacity=0, stroke_width=1.5).move_to(RIGHT * 3.2 + DOWN * 0.6)

        c1 = Text("Clean inputs\nKnown ground truth\nAgent tested alone", font=MONO, font_size=14, color=INK).move_to(LEFT * 3.2 + UP * 0.5)
        c2 = Text("→ PASSES", font=DISPLAY, font_size=15, color=TEAL).move_to(LEFT * 3.2 + DOWN * 1.5)

        f1 = Text("Prior agent's output\ntreated as fact\nError propagates forward", font=MONO, font_size=14, color=INK).move_to(RIGHT * 3.2 + UP * 0.5)
        f2 = Text("→ CASCADES", font=DISPLAY, font_size=15, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 1.5)

        self.play(GrowFromCenter(hdr_iso), GrowFromCenter(hdr_pipe), run_time=0.5)
        self.play(Write(t_iso), Write(t_pipe), run_time=0.5)
        self.play(GrowFromCenter(body_iso), GrowFromCenter(body_pipe), run_time=0.5)
        self.play(Write(c1), Write(f1), run_time=0.5)
        self.play(Write(c2), Write(f2), run_time=0.5)
        self.wait(DUR["B04"] - 3.5)


# ── B05 — Conditioning ────────────────────────────────────────────────────────

class B05_Conditioning(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Why Error Cascades", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)

        # Agent A row
        box_a = Rectangle(width=3.0, height=1.0, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.12, stroke_width=1.5).move_to(LEFT * 4.0 + UP * 1.3)
        lbl_a = Text("AGENT A", font=DISPLAY, font_size=15, color=TEAL).move_to(LEFT * 4.0 + UP * 1.3)

        err_a = Rectangle(width=2.4, height=0.6, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.25, stroke_width=1).move_to(LEFT * 4.0 + UP * 0.1)
        err_a_lbl = Text("1% wrong output →", font=MONO, font_size=12, color=CRIMSON).move_to(LEFT * 4.0 + UP * 0.1)

        # Agent B conditions on it
        arr_ab = Line([-2.4, 0.1, 0], [-0.3, -0.3, 0], color=CRIMSON, stroke_width=2.5)
        box_b  = Rectangle(width=3.0, height=1.0, color=SLATE, fill_color=SLATE,
                           fill_opacity=0.12, stroke_width=1.5).move_to([0.5, -0.8, 0])
        lbl_b  = Text("AGENT B\n(takes A as truth)", font=MONO, font_size=13, color=SLATE).move_to([0.5, -0.8, 0])

        # Agent C further compound
        arr_bc  = Line([2.1, -0.8, 0], [3.5, -1.8, 0], color=CRIMSON, stroke_width=2.5)
        box_c   = Rectangle(width=3.0, height=1.0, color=CRIMSON, fill_color=CRIMSON,
                            fill_opacity=0.18, stroke_width=1.5).move_to([4.2, -2.2, 0])
        lbl_c   = Text("SYSTEM: 30%\nERROR", font=DISPLAY, font_size=14, color=CRIMSON).move_to([4.2, -2.2, 0])

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(box_a), run_time=0.4)
        self.play(Write(lbl_a), run_time=0.3)
        self.play(GrowFromCenter(err_a), run_time=0.3)
        self.play(Write(err_a_lbl), run_time=0.3)
        self.play(GrowFromEdge(arr_ab, LEFT), run_time=0.4)
        self.play(GrowFromCenter(box_b), run_time=0.4)
        self.play(Write(lbl_b), run_time=0.3)
        self.play(GrowFromEdge(arr_bc, LEFT), run_time=0.4)
        self.play(GrowFromCenter(box_c), run_time=0.4)
        self.play(Write(lbl_c), run_time=0.3)
        self.wait(DUR["B05"] - 4.5)


# ── B07 — CascadeTrace ────────────────────────────────────────────────────────

class B07_CascadeTrace(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Each Hop: Multiplication, Not Addition", font=DISPLAY, font_size=20, color=GOLD).move_to(UP * 3.1)

        steps = [
            ("AGENT A output",   "1% chance of error → downstream receives it as fact",    TEAL),
            ("AGENT B conditions on A", "wrong input → B's output compounds the error",     CRIMSON),
            ("AGENT C compounds B", "error rate now dominated by cascade, not individuals", CRIMSON),
            ("SYSTEM failure rate",  "→ 30% — not 3% (1+1+1%)",                            GOLD),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (patch, result, col) in enumerate(steps):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.5).move_to(UP * y)
            t1  = Text(patch,  font=DISPLAY, font_size=15, color=col).move_to([0.0, y + 0.22, 0])
            t2  = Text(result, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(t1), run_time=0.3)
            self.play(Write(t2), run_time=0.3)

        self.wait(DUR["B07"] - 4.5)


# ── B08 — QuoteCascade ────────────────────────────────────────────────────────

class B08_QuoteCascade(Scene):
    def construct(self):
        _quote_scene(
            self,
            "You validated each agent at one percent; "
            "the compound system fails at thirty.",
            "Computational Skepticism for AI, Chapter 8",
            None,
            "compound system fails",
            DUR["B08"],
        )


# ── B09 — ValidationMove ──────────────────────────────────────────────────────

class B09_ValidationMove(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What to Validate Instead", font=DISPLAY, font_size=22, color=TEAL).move_to(UP * 3.1)

        moves = [
            ("INTERACTIONS",  "Which agent outputs flow into which inputs?\nAre those flows permitted?",    TEAL),
            ("MONITORING",    "What detects runaway error propagation?\nFlag output quality at each hop",   TEAL),
            ("HANDOFF GATES", "Gate downstream agents on upstream\noutput quality — not just completion",   TEAL),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, desc, col) in enumerate(moves):
            x = (i - 1) * 4.3
            box = Rectangle(width=3.8, height=2.5, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to([x, 0.5, 0])
            lbl = Text(name, font=DISPLAY, font_size=16, color=col).move_to([x, 1.4, 0])
            desc_txt = Text(desc, font=MONO, font_size=12, color=INK).move_to([x, 0.1, 0])
            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(desc_txt), run_time=0.3)

        note = Text("The interaction pattern is the failure — validate it.",
                    font=DISPLAY, font_size=15, color=GOLD).move_to(DOWN * 2.2)
        self.play(Write(note), run_time=0.5)
        self.wait(DUR["B09"] - 4.3)


# ── B10 — QuoteInteraction ────────────────────────────────────────────────────

class B10_QuoteInteraction(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Validate the interaction patterns, not just the individual agents "
            "— which interactions are permitted, what monitoring detects runaway loops.",
            "Computational Skepticism for AI, Chapter 8",
            None,
            "interaction patterns",
            DUR["B10"],
        )


# ── B11 — Sufficiency ─────────────────────────────────────────────────────────

class B11_Sufficiency(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Necessary. Not Sufficient.", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)

        rows = [
            ("Individual agent validation",  "Necessary — test each component",                      TEAL),
            ("Individual agent validation",  "NOT sufficient — interaction patterns are invisible",   CRIMSON),
            ("System-level validation",      "Tests the interactions, catches cascade dynamics",      TEAL),
            ("Missing either one",           "ships a failure with no single-agent analog",           GOLD),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, action, col) in enumerate(rows):
            y = 1.8 - i * 1.25
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to(UP * y)
            lbl = Text(name,   font=DISPLAY, font_size=15, color=col).move_to([0.0, y + 0.2,  0])
            act = Text(action, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(act), run_time=0.3)

        self.wait(DUR["B11"] - 4.5)


# ── B12 — ExampleCascade ─────────────────────────────────────────────────────

class B12_ExampleCascade(Scene):
    def construct(self):
        total = DUR["B12"]
        title = Text("Three Cleared Agents. Wrong Output.", font=DISPLAY, font_size=19, color=GOLD)
        title.move_to(UP * 3.1)

        agents = [
            ("AGENT 1", "Extract order #", "Reads O-7821 as O-7281", TEAL, CRIMSON),
            ("AGENT 2", "Fetch record",    "Fetches wrong customer",  CRIMSON, CRIMSON),
            ("AGENT 3", "Draft reply",     "Confident. Wrong order.", CRIMSON, CRIMSON),
        ]

        y_positions = [1.4, 0.0, -1.4]
        for i, ((name, task, outcome, col_name, col_out), y) in enumerate(zip(agents, y_positions)):
            box = Rectangle(width=10.5, height=1.05, color=col_out, fill_color=col_out,
                            fill_opacity=0.09, stroke_width=1.8).move_to(UP * y)
            lbl = Text(f"{name}: {task}", font=DISPLAY, font_size=15, color=col_name).move_to([-1.0, y + 0.22, 0])
            out = Text(outcome, font="PT Mono", font_size=13, color=INK).move_to([-1.0, y - 0.2, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(out), run_time=0.3)

        note = Text("Each agent: cleared. Pipeline: wrong customer's order, delivered confidently.",
                    font=DISPLAY, font_size=14, color=INK).move_to(DOWN * 2.55)
        note_rect = Rectangle(width=10.5, height=0.55, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)
        self.play(GrowFromCenter(note_rect), run_time=0.3)
        self.play(Write(note), run_time=0.5)
        self.wait(max(0.5, total - 4.0))
