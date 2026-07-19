"""vox_scenes.py — Why the Document You Asked AI to Read Might Be Giving It New Instructions
(vox-prompt-injection, slate cut, 16:9)

One Scene per GRAPHIC/CARD beat whose source is 'own'.
STILL beats B02 and B13 are ai-media slots — no scene here.

Color law: TEAL = trusted instructions / user-authorized commands;
           CRIMSON = injected instructions / adversarial commands.
Never swap mid-film.

Exclusions: NO formal prompt injection attack taxonomy, NO cryptographic or
sandboxing solutions, NO SQL injection comparison, NO extended VPI-Bench methodology.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 10.0, "B03": 10.0, "B04": 11.0, "B05": 12.0,
    "B06": 12.0, "B07": 11.0, "B08": 12.0, "B09": 13.0,
    "B10": 11.0, "B11": 12.0, "B12": 12.0, "B14": 12.0,
    "B15": 10.0, "B16": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- B01 — agent task gone wrong

class B01_AgentTask(Scene):
    def construct(self):
        total = DUR["B01"]

        user_chip = LabelChip("USER", accent=TEAL, size=26)
        user_chip.move_to(LEFT * 4.5)

        a1 = Arrow(LEFT * 3.3, LEFT * 1.6,
                   color=TEAL, stroke_width=3, buff=0.0)
        task_label = Text("read vendor quotes", font=SERIF, color=SLATE, font_size=18)
        task_label.next_to(a1, UP, buff=0.12)

        agent_chip = LabelChip("AGENT", accent=SLATE, size=26)
        agent_chip.move_to(ORIGIN)

        a2 = Arrow(RIGHT * 1.3, RIGHT * 2.9,
                   color=CRIMSON, stroke_width=3, buff=0.0)

        output_chip = LabelChip("WRONG VENDOR", accent=CRIMSON, size=26)
        output_chip.move_to(RIGHT * 4.5)

        wrong_label = SerifLabel("email draft in compose window", CRIMSON, size=22)
        wrong_label.next_to(output_chip, DOWN, buff=0.6)

        self.play(FadeIn(user_chip), run_time=0.5)
        self.play(Create(a1), FadeIn(task_label), run_time=0.5)
        self.play(FadeIn(agent_chip), run_time=0.5)
        self.play(Create(a2), run_time=0.4)
        self.play(FadeIn(output_chip), run_time=0.5)
        self.play(FadeIn(wrong_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.9))


# ---------------------------------------------------------------- B03 — THE QUESTION card

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = Text("THE QUESTION", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        q1 = Text("Why did the agent do something", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        q2 = Text("the user never asked?", font=SERIF,
                  color=INK, font_size=40, weight="BOLD")
        block = VGroup(q1, q2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(q2.get_corner(DL) + DOWN * 0.16, q2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.7)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B04 — naive model

class B04_NaiveModel(Scene):
    def construct(self):
        total = DUR["B04"]
        eye = Text("THE NAIVE EXPECTATION", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.7)

        user_chip = LabelChip("USER", accent=TEAL, size=24)
        user_chip.move_to(LEFT * 4.5 + UP * 0.5)

        cmd_arrow = Arrow(LEFT * 3.4 + UP * 0.5, LEFT * 1.5 + UP * 0.5,
                          color=TEAL, stroke_width=3, buff=0.0)
        cmd_label = Text("commands", font=SERIF, color=TEAL, font_size=18)
        cmd_label.next_to(cmd_arrow, UP, buff=0.1)

        doc_chip = LabelChip("DOCUMENT", accent=SLATE, size=24)
        doc_chip.move_to(LEFT * 4.5 + DOWN * 0.9)

        data_arrow = Arrow(LEFT * 3.4 + DOWN * 0.9, LEFT * 1.5 + DOWN * 0.9,
                           color=SLATE, stroke_width=3, buff=0.0)
        data_label = Text("data only", font=SERIF, color=SLATE, font_size=18)
        data_label.next_to(data_arrow, DOWN, buff=0.1)

        agent_chip = LabelChip("AGENT", accent=SLATE, size=24)
        agent_chip.move_to(ORIGIN + RIGHT * 0.5)

        naive_label = SerifLabel("the naive expectation: instructions and data are separate", SLATE, size=20)
        naive_label.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(user_chip), FadeIn(doc_chip), run_time=0.5)
        self.play(Create(cmd_arrow), FadeIn(cmd_label),
                  Create(data_arrow), FadeIn(data_label), run_time=0.8)
        self.play(FadeIn(agent_chip), run_time=0.5)
        self.play(FadeIn(naive_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.8))


# ---------------------------------------------------------------- B05 — context window identity

class B05_ContextWindow(Scene):
    def construct(self):
        total = DUR["B05"]
        eye = Text("THE CONTEXT WINDOW", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Context window box
        cw_box = Rectangle(width=9.0, height=2.2)
        cw_box.set_fill(SLATE, 0.10).set_stroke(SLATE, 1.8)
        cw_box.move_to(ORIGIN + UP * 0.5)
        cw_label = Text("CONTEXT WINDOW", font=DISPLAY, color=SLATE,
                        font_size=18, weight="MEDIUM")
        cw_label.next_to(cw_box, UP, buff=0.1)

        user_instr = LabelChip("USER INSTRUCTIONS", accent=TEAL, size=22)
        user_instr.move_to(LEFT * 2.5 + UP * 0.5)

        eq_sign = Text("=", font=DISPLAY, color=INK, font_size=32, weight="BOLD")
        eq_sign.move_to(ORIGIN + UP * 0.5)

        doc_content = LabelChip("DOCUMENT CONTENT", accent=SLATE, size=22)
        doc_content.move_to(RIGHT * 2.5 + UP * 0.5)

        agent_chip = LabelChip("AGENT reads both", accent=SLATE, size=24)
        agent_chip.move_to(DOWN * 1.2)

        same_label = SerifLabel("both are text — processed identically", CRIMSON, size=22)
        same_label.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(cw_box), FadeIn(cw_label), run_time=0.6)
        self.play(FadeIn(user_instr), run_time=0.5)
        self.play(FadeIn(eq_sign), run_time=0.3)
        self.play(FadeIn(doc_content), run_time=0.5)
        self.play(FadeIn(agent_chip), run_time=0.5)
        self.play(FadeIn(same_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.4))


# ---------------------------------------------------------------- B06 — injection mechanism

class B06_InjectionMechanism(Scene):
    def construct(self):
        total = DUR["B06"]
        eye = Text("THE INJECTION MECHANISM", font=DISPLAY, color=CRIMSON,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Document card with surface and hidden layer
        doc_box = Rectangle(width=3.2, height=2.4)
        doc_box.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.8)
        doc_box.move_to(LEFT * 3.5)

        doc_title = Text("DOCUMENT", font=DISPLAY, color=INK,
                         font_size=18, weight="MEDIUM")
        doc_title.next_to(doc_box, UP, buff=0.1)

        surface_chip = LabelChip("visible content", accent=TEAL, size=18)
        surface_chip.move_to(LEFT * 3.5 + UP * 0.4)

        hidden_chip = LabelChip("INJECTED COMMAND", accent=CRIMSON, size=18)
        hidden_chip.move_to(LEFT * 3.5 + DOWN * 0.5)

        # Arrow from injected command to agent output
        inj_arrow = Arrow(LEFT * 1.8 + DOWN * 0.5, RIGHT * 0.4 + DOWN * 0.5,
                          color=CRIMSON, stroke_width=4, buff=0.0)

        agent_chip = LabelChip("AGENT", accent=SLATE, size=26)
        agent_chip.move_to(RIGHT * 1.2)

        # User task crossed out
        user_task = LabelChip("user task", accent=TEAL, size=24)
        user_task.move_to(RIGHT * 1.2 + UP * 1.2)

        injected_action = LabelChip("INJECTED ACTION", accent=CRIMSON, size=24)
        injected_action.move_to(RIGHT * 4.2 + DOWN * 0.5)

        out_arrow = Arrow(RIGHT * 2.1, RIGHT * 3.0 + DOWN * 0.3,
                          color=CRIMSON, stroke_width=3, buff=0.0)

        strikeout = Line(user_task.get_left() + LEFT * 0.1,
                         user_task.get_right() + RIGHT * 0.1,
                         color=CRIMSON, stroke_width=3)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(doc_box), FadeIn(doc_title), FadeIn(surface_chip), run_time=0.6)
        self.play(FadeIn(hidden_chip, scale=0.9), run_time=0.5)
        self.play(FadeIn(agent_chip), FadeIn(user_task), run_time=0.5)
        self.play(Create(inj_arrow), run_time=0.5)
        self.play(Create(strikeout), run_time=0.4)
        self.play(Create(out_arrow), FadeIn(injected_action), run_time=0.6)
        self.wait(max(0.5, total - 3.6))


# ---------------------------------------------------------------- B07 — identity card

class B07_IdentityCard(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("The content of a document", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        t2 = Text("is indistinguishable from a command.", font=SERIF, color=CRIMSON,
                  font_size=40, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B08 — attack surface

class B08_AttackSurface(Scene):
    def construct(self):
        total = DUR["B08"]
        eye = Text("THE ATTACK SURFACE", font=DISPLAY, color=CRIMSON,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Three source chips in vertical column on left
        doc_src = LabelChip("DOCUMENT", accent=SLATE, size=22)
        doc_src.move_to(LEFT * 4.0 + UP * 1.2)

        web_src = LabelChip("WEB PAGE", accent=SLATE, size=22)
        web_src.move_to(LEFT * 4.0)

        email_src = LabelChip("EMAIL", accent=SLATE, size=22)
        email_src.move_to(LEFT * 4.0 + DOWN * 1.2)

        # Agent chip on right
        agent_chip = LabelChip("AGENT", accent=SLATE, size=26)
        agent_chip.move_to(RIGHT * 2.0)

        # Injection arrows (crimson) from each source
        a_doc = Arrow(LEFT * 2.7 + UP * 1.2, RIGHT * 0.8 + UP * 0.4,
                      color=CRIMSON, stroke_width=3, buff=0.0)
        a_web = Arrow(LEFT * 2.7, RIGHT * 0.8,
                      color=CRIMSON, stroke_width=3, buff=0.0)
        a_email = Arrow(LEFT * 2.7 + DOWN * 1.2, RIGHT * 0.8 + DOWN * 0.4,
                        color=CRIMSON, stroke_width=3, buff=0.0)

        same_mech = SerifLabel("same mechanism — all three", CRIMSON, size=22)
        same_mech.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(doc_src), run_time=0.4)
        self.play(FadeIn(web_src), run_time=0.4)
        self.play(FadeIn(email_src), run_time=0.4)
        self.play(FadeIn(agent_chip), run_time=0.4)
        self.play(Create(a_doc), Create(a_web), Create(a_email), run_time=0.8)
        self.play(FadeIn(same_mech, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.4))


# ---------------------------------------------------------------- B09 — Mia example

class B09_MiaExample(Scene):
    def construct(self):
        total = DUR["B09"]
        eye = Text("MIA'S VENDOR QUOTES", font=DISPLAY, color=SLATE,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        # Three document cards
        va_box = Rectangle(width=2.4, height=2.0)
        va_box.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.6)
        va_box.move_to(LEFT * 4.5)
        va_label = Text("VENDOR A", font=DISPLAY, color=INK, font_size=18, weight="MEDIUM")
        va_label.move_to(va_box)

        vb_box = Rectangle(width=2.4, height=2.0)
        vb_box.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 1.8)
        vb_box.move_to(ORIGIN)
        vb_label = Text("VENDOR B", font=DISPLAY, color=INK, font_size=18, weight="MEDIUM")
        vb_label.move_to(ORIGIN + UP * 0.5)

        # Hidden instruction in Vendor B
        hidden = LabelChip("INJECTED COMMAND", accent=CRIMSON, size=16)
        hidden.move_to(ORIGIN + DOWN * 0.45)

        vc_box = Rectangle(width=2.4, height=2.0)
        vc_box.set_fill(TEAL, 0.10).set_stroke(TEAL, 1.6)
        vc_box.move_to(RIGHT * 4.5)
        vc_label = Text("VENDOR C", font=DISPLAY, color=INK, font_size=18, weight="MEDIUM")
        vc_label.move_to(vc_box)

        # Output
        output_chip = LabelChip("RECOMMEND: VENDOR B", accent=CRIMSON, size=22)
        output_chip.to_edge(DOWN, buff=0.85)

        email_tag = SerifLabel("email draft in compose window", CRIMSON, size=20)
        email_tag.next_to(output_chip, DOWN, buff=0.2)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(va_box), FadeIn(va_label),
                  FadeIn(vc_box), FadeIn(vc_label), run_time=0.7)
        self.play(FadeIn(vb_box), FadeIn(vb_label), run_time=0.5)
        self.play(FadeIn(hidden, scale=0.9), run_time=0.5)
        self.play(FadeIn(output_chip, scale=1.1), run_time=0.6)
        self.play(FadeIn(email_tag, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.3))


# ---------------------------------------------------------------- B10 — fluency-correctness card

class B10_FluencyCard(Scene):
    def construct(self):
        total = DUR["B10"]
        t1 = Text("The output looked correct.", font=SERIF, color=INK,
                  font_size=44, weight="BOLD")
        t2 = Text("The task had been redirected.", font=SERIF, color=CRIMSON,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B11 — scope mitigation

class B11_ScopeMitigation(Scene):
    def construct(self):
        total = DUR["B11"]
        eye = Text("SCOPE IS THE MITIGATION", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Trusted zone box
        tz_box = Rectangle(width=4.8, height=3.0)
        tz_box.set_fill(TEAL, 0.08).set_stroke(TEAL, 2.2)
        tz_box.move_to(LEFT * 2.0)
        tz_label = Text("TRUSTED ZONE", font=DISPLAY, color=TEAL,
                        font_size=18, weight="MEDIUM")
        tz_label.next_to(tz_box, UP, buff=0.1)

        files_chip = LabelChip("YOUR FILES", accent=TEAL, size=22)
        files_chip.move_to(LEFT * 2.0 + UP * 0.5)
        conn_chip = LabelChip("CONNECTORS", accent=TEAL, size=22)
        conn_chip.move_to(LEFT * 2.0 + DOWN * 0.5)

        # External sources — stacked vertically, with BLOCKED badges
        ext_label = Text("EXTERNAL SOURCES", font=DISPLAY, color=SLATE,
                         font_size=18, weight="MEDIUM")
        ext_label.move_to(RIGHT * 4.2 + UP * 1.1)

        web_src = LabelChip("WEB", accent=SLATE, size=20)
        web_src.move_to(RIGHT * 4.2 + UP * 0.4)

        email_src = LabelChip("EMAIL", accent=SLATE, size=20)
        email_src.move_to(RIGHT * 4.2 + DOWN * 0.3)

        ext_src = LabelChip("EXTERNAL DOCS", accent=SLATE, size=20)
        ext_src.move_to(RIGHT * 4.2 + DOWN * 1.0)

        # BLOCKED badge to the right of the boundary — no line crossing
        blocked_chip = LabelChip("BLOCKED AT BOUNDARY", accent=CRIMSON, size=18)
        blocked_chip.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(tz_box), FadeIn(tz_label), run_time=0.5)
        self.play(FadeIn(files_chip), FadeIn(conn_chip), run_time=0.5)
        self.play(FadeIn(ext_label), FadeIn(web_src), FadeIn(email_src), FadeIn(ext_src), run_time=0.6)
        self.play(FadeIn(blocked_chip, scale=0.9), run_time=0.5)
        self.wait(max(0.5, total - 3.1))


# ---------------------------------------------------------------- B12 — review gate

class B12_ReviewGate(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("THE REVIEW GATE", font=DISPLAY, color=TEAL,
                   font_size=20, weight="MEDIUM")
        eye.to_edge(UP, buff=0.6)

        # Task flow
        read_chip = LabelChip("AGENT READS", accent=SLATE, size=22)
        read_chip.move_to(LEFT * 4.5)

        a1 = Arrow(LEFT * 3.0, LEFT * 1.8,
                   color=SLATE, stroke_width=3, buff=0.0)

        output_chip = LabelChip("AGENT OUTPUT", accent=SLATE, size=22)
        output_chip.move_to(LEFT * 0.5)

        a2 = Arrow(RIGHT * 0.8, RIGHT * 2.0,
                   color=TEAL, stroke_width=3, buff=0.0)

        gate_box = Rectangle(width=2.0, height=1.4)
        gate_box.set_fill(TEAL, 0.12).set_stroke(TEAL, 2.2)
        gate_box.move_to(RIGHT * 3.0)
        gate_text = Text("REVIEW\nGATE", font=DISPLAY, color=INK,
                         font_size=18, weight="MEDIUM")
        gate_text.move_to(gate_box)

        a3 = Arrow(RIGHT * 4.1, RIGHT * 5.3,
                   color=TEAL, stroke_width=3, buff=0.0)

        action_chip = LabelChip("ACTION", accent=TEAL, size=22)
        action_chip.move_to(RIGHT * 5.9 + UP * 0.0)

        human_label = SerifLabel("human inspects before action", TEAL, size=22)
        human_label.next_to(gate_box, DOWN, buff=0.55)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(read_chip), run_time=0.4)
        self.play(Create(a1), run_time=0.4)
        self.play(FadeIn(output_chip), run_time=0.4)
        self.play(Create(a2), run_time=0.4)
        self.play(FadeIn(gate_box), FadeIn(gate_text), run_time=0.5)
        self.play(Create(a3), FadeIn(action_chip), run_time=0.5)
        self.play(FadeIn(human_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.6))


# ---------------------------------------------------------------- B14 — the check (decision diamond)

class B14_TheCheck(Scene):
    def construct(self):
        total = DUR["B14"]
        eye = Text("THE CHECK BEFORE AGENTIC TASKS", font=DISPLAY, color=SLATE,
                   font_size=18, weight="MEDIUM")
        eye.to_edge(UP, buff=0.55)

        diamond = Square(side_length=2.2)
        diamond.rotate(45 * DEGREES)
        diamond.set_fill(GROUND, 1).set_stroke(INK, 2.5)
        diamond.move_to(ORIGIN + UP * 0.1)

        q_line1 = Text("Irreversible", font=SERIF, color=INK, font_size=20)
        q_line2 = Text("action?", font=SERIF, color=INK, font_size=20)
        q_block = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.1)
        q_block.move_to(diamond)

        yes_label = Text("YES", font=DISPLAY, color=CRIMSON,
                         font_size=22, weight="BOLD")
        yes_label.next_to(diamond, RIGHT, buff=0.5)

        gate_chip = LabelChip("ADD REVIEW GATE", accent=TEAL, size=22)
        gate_chip.next_to(yes_label, RIGHT, buff=0.5)

        no_label = Text("NO", font=DISPLAY, color=SLATE,
                        font_size=22, weight="BOLD")
        no_label.next_to(diamond, DOWN, buff=0.5)

        proceed_chip = LabelChip("PROCEED", accent=SLATE, size=22)
        proceed_chip.next_to(no_label, DOWN, buff=0.35)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(diamond), FadeIn(q_block), run_time=0.8)
        self.play(FadeIn(yes_label), FadeIn(gate_chip), run_time=0.6)
        self.play(FadeIn(no_label), FadeIn(proceed_chip), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


# ---------------------------------------------------------------- B15 — principle card

class B15_PrincipleCard(Scene):
    def construct(self):
        total = DUR["B15"]
        t1 = Text("Instructions and content", font=SERIF, color=INK,
                  font_size=40, weight="BOLD")
        t2 = Text("are the same type of thing.", font=SERIF, color=CRIMSON,
                  font_size=40, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B16 — endcard

class B16_End(Scene):
    def construct(self):
        total = DUR["B16"]

        kicker = Text("AGENTIC AI", font=DISPLAY, color=TEAL,
                      font_size=22, weight="MEDIUM")
        kicker.to_edge(UP, buff=0.7)

        t1 = Text("The document can command the agent.", font=SERIF, color=CRIMSON,
                  font_size=36, weight="BOLD")
        t2 = Text("Scope is the control.", font=SERIF, color=TEAL,
                  font_size=36, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN + DOWN * 0.2)

        u = Line(t1.get_corner(DL) + DOWN * 0.16, t1.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)

        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1), Create(u), run_time=0.7)
        self.play(FadeIn(t2, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 1.8))
