import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))

from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,
    "B02": 11.0, "B04": 9.0, "B05": 9.0,
    "B07": 9.0,  "B08": 9.0, "B09": 8.0,
    "B10": 10.0, "B11": 7.0,
    "B12": 16.0,
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
        t1 = Text("Why the AI Wasn't Lying", font=DISPLAY, color=INK, font_size=44, weight=BOLD)
        t2 = Text("When It Said 'Deleted'", font=DISPLAY, color=INK, font_size=44, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── B02 — AshCase ─────────────────────────────────────────────────────────────

class B02_AshCase(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Three boxes in a horizontal flow
        b_agent = Rectangle(width=2.8, height=1.0, color=TEAL, fill_color=TEAL, fill_opacity=0.15, stroke_width=2)
        b_report = Rectangle(width=2.8, height=1.0, color=SLATE, fill_color=SLATE, fill_opacity=0.15, stroke_width=2)
        b_server = Rectangle(width=2.8, height=1.0, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.15, stroke_width=2)

        b_agent.move_to(LEFT * 4.4 + UP * 0.6)
        b_report.move_to(UP * 0.6)
        b_server.move_to(RIGHT * 4.4 + UP * 0.6)

        t_agent  = Text("ASH AGENT\n\"Email RESET\ncompleted\"", font=DISPLAY, font_size=16, color=TEAL).move_to(b_agent)
        t_report = Text("OWNER\nchecks\nProton Mail", font=DISPLAY, font_size=16, color=SLATE).move_to(b_report)
        t_server = Text("EMAIL\nSTILL EXISTS\non server", font=DISPLAY, font_size=16, color=CRIMSON).move_to(b_server)

        arr1 = Line(b_agent.get_right(), b_report.get_left(), color=INK, stroke_width=2)
        arr2 = Line(b_report.get_right(), b_server.get_left(), color=INK, stroke_width=2)

        caption = Text("Task not accomplished — but the agent believed it was",
                       font=DISPLAY, font_size=18, color=INK).move_to(DOWN * 1.8)
        cap_rect = Rectangle(width=8.0, height=0.5, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.10, stroke_width=1.5).move_to(DOWN * 1.8)

        self.play(GrowFromCenter(b_agent), run_time=0.5)
        self.play(Write(t_agent), run_time=0.5)
        self.play(GrowFromEdge(arr1, LEFT), run_time=0.4)
        self.play(GrowFromCenter(b_report), run_time=0.5)
        self.play(Write(t_report), run_time=0.4)
        self.play(GrowFromEdge(arr2, LEFT), run_time=0.4)
        self.play(GrowFromCenter(b_server), run_time=0.5)
        self.play(Write(t_server), run_time=0.4)
        self.play(GrowFromCenter(cap_rect), run_time=0.4)
        self.play(Write(caption), run_time=0.5)
        self.wait(DUR["B02"] - 5.5)


# ── B04 — TwoWorlds ───────────────────────────────────────────────────────────

class B04_TwoWorlds(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # DELETED divider word
        word_deleted = LabelChip("DELETED")
        word_deleted.move_to(UP * 2.8)

        # Left: AGENT WORLD
        col_left = Rectangle(width=5.5, height=4.5, color=TEAL, fill_color=TEAL, fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.3)
        lbl_left = Text("AGENT WORLD", font=DISPLAY, font_size=20, color=TEAL).move_to(LEFT * 3.2 + UP * 1.5)
        sub_left = Text("local email client", font=DISPLAY, font_size=16, color=INK).move_to(LEFT * 3.2 + UP * 0.8)
        res_left = Text("'delete' = reset local client", font="PT Mono", font_size=15, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.3)
        chk_left = Text("✓ complete (in agent's scope)", font=DISPLAY, font_size=14, color=TEAL).move_to(LEFT * 3.2 + DOWN * 1.2)

        # Right: USER WORLD
        col_right = Rectangle(width=5.5, height=4.5, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.3)
        lbl_right = Text("USER WORLD", font=DISPLAY, font_size=20, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.5)
        sub_right = Text("Proton Mail server", font=DISPLAY, font_size=16, color=INK).move_to(RIGHT * 3.2 + UP * 0.8)
        res_right = Text("'delete' = email gone from server", font="PT Mono", font_size=15, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.3)
        chk_right = Text("✗ not done", font=DISPLAY, font_size=14, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 1.2)

        self.play(GrowFromCenter(word_deleted), run_time=0.5)
        self.play(GrowFromCenter(col_left), GrowFromCenter(col_right), run_time=0.7)
        self.play(Write(lbl_left), Write(lbl_right), run_time=0.5)
        self.play(Write(sub_left), Write(sub_right), run_time=0.5)
        self.play(Write(res_left), Write(res_right), run_time=0.5)
        self.play(Write(chk_left), Write(chk_right), run_time=0.5)
        self.wait(DUR["B04"] - 3.7)


# ── B05 — WhatHappened ────────────────────────────────────────────────────────

class B05_WhatHappened(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        steps = [
            ("1", "No email-deletion tool available",             INK),
            ("2", "Reset local email account option found",       INK),
            ("3", "User approved twice — agent executed",         INK),
            ("4a", "Local client: GONE  ✓",                      TEAL),
            ("4b", "Mail server: UNCHANGED  ✗",                  CRIMSON),
        ]

        title = Text("What Actually Happened", font=DISPLAY, font_size=22, color=INK).move_to(UP * 3.1)
        self.play(Write(title), run_time=0.4)

        y_positions = [2.2, 1.2, 0.2, -0.8, -1.8]
        for i, ((num, text, col), y) in enumerate(zip(steps, y_positions)):
            box = Rectangle(width=9.5, height=0.75, color=col, fill_color=col, fill_opacity=0.10, stroke_width=1.5).move_to(UP * y)
            txt = Text(f"{num}. {text}", font=MONO, font_size=17, color=col if col != INK else BLACK).move_to(UP * y)
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(txt), run_time=0.3)

        self.wait(DUR["B05"] - 3.8)


# ── B07 — TwoDeletes ─────────────────────────────────────────────────────────

class B07_TwoDeletes(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        col_left  = Rectangle(width=5.5, height=4.2, color=TEAL,   fill_color=TEAL,   fill_opacity=0.10, stroke_width=2).move_to(LEFT * 3.2)
        col_right = Rectangle(width=5.5, height=4.2, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.10, stroke_width=2).move_to(RIGHT * 3.2)

        lbl_left  = Text("Agent's 'DELETE'", font=DISPLAY, font_size=19, color=TEAL).move_to(LEFT * 3.2 + UP * 1.6)
        lbl_right = Text("User's 'DELETE'",  font=DISPLAY, font_size=19, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.6)

        op_left   = Text("→ reset local email client", font=MONO, font_size=16, color=TEAL).move_to(LEFT * 3.2 + UP * 0.5)
        op_right  = Text("→ email gone from server",   font=MONO, font_size=16, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 0.5)

        res_left  = Text("✓  COMPLETE\n(in agent's world)", font=DISPLAY, font_size=17, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.9)
        res_right = Text("✗  NOT DONE\n(in user's world)",  font=DISPLAY, font_size=17, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.9)

        note = Text("Same word — two operations — no flag", font=DISPLAY, font_size=17, color=INK).move_to(DOWN * 2.7)

        self.play(GrowFromCenter(col_left), GrowFromCenter(col_right), run_time=0.6)
        self.play(Write(lbl_left), Write(lbl_right), run_time=0.5)
        self.play(Write(op_left),  Write(op_right),  run_time=0.5)
        self.play(Write(res_left), Write(res_right),  run_time=0.5)
        self.play(Write(note), run_time=0.5)
        self.wait(DUR["B07"] - 3.1)


# ── B08 — FalseSuccess ────────────────────────────────────────────────────────

class B08_FalseSuccess(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Three top boxes
        b_agent   = Rectangle(width=3.0, height=0.85, color=TEAL,   fill_color=TEAL,   fill_opacity=0.15, stroke_width=2).move_to(LEFT * 4.0 + UP * 1.5)
        b_report  = Rectangle(width=3.0, height=0.85, color=SLATE, fill_color=SLATE,   fill_opacity=0.15, stroke_width=2).move_to(UP * 1.5)
        b_user    = Rectangle(width=3.0, height=0.85, color=TEAL,   fill_color=TEAL,   fill_opacity=0.15, stroke_width=2).move_to(RIGHT * 4.0 + UP * 1.5)

        t_agent   = Text("AGENT: COMPLETED", font=MONO, font_size=14, color=TEAL).move_to(b_agent)
        t_report  = Text("REPORT: done", font=MONO, font_size=14, color=SLATE).move_to(b_report)
        t_user    = Text("USER: DONE?", font=MONO, font_size=14, color=TEAL).move_to(b_user)

        arr1 = Line(b_agent.get_right(), b_report.get_left(), color=INK, stroke_width=2)
        arr2 = Line(b_report.get_right(), b_user.get_left(), color=INK, stroke_width=2)

        # Reality check box below
        b_reality = Rectangle(width=5.5, height=0.85, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.15, stroke_width=2).move_to(DOWN * 0.3)
        t_reality = Text("SERVER: EMAIL STILL EXISTS", font=MONO, font_size=16, color=CRIMSON).move_to(b_reality)

        # Gap line
        gap_line = Line(b_report.get_bottom(), b_reality.get_top(), color=CRIMSON, stroke_width=2)

        label_gap = Text("← gap: nothing caught this", font=DISPLAY, font_size=15, color=CRIMSON).move_to(RIGHT * 3.8 + DOWN * 0.3)

        self.play(GrowFromCenter(b_agent), run_time=0.4)
        self.play(Write(t_agent), run_time=0.4)
        self.play(GrowFromEdge(arr1, LEFT), run_time=0.3)
        self.play(GrowFromCenter(b_report), run_time=0.4)
        self.play(Write(t_report), run_time=0.3)
        self.play(GrowFromEdge(arr2, LEFT), run_time=0.3)
        self.play(GrowFromCenter(b_user), run_time=0.4)
        self.play(Write(t_user), run_time=0.3)
        self.play(GrowFromEdge(gap_line, UP), run_time=0.4)
        self.play(GrowFromCenter(b_reality), run_time=0.4)
        self.play(Write(t_reality), run_time=0.4)
        self.play(Write(label_gap), run_time=0.4)
        self.wait(DUR["B08"] - 4.5)


# ── B09 — QuoteReport ────────────────────────────────────────────────────────

class B09_QuoteReport(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The agent's completion report and the world's state "
            "contradicted each other, and neither the agent nor any "
            "automated system noticed. That single fact — a false "
            "success report that nothing caught — is the entire "
            "architecture of what makes agentic validation different.",
            "— anatomy of a false success",
            None,
            "false success report",
            DUR["B09"],
        )


# ── B10 — Validation ─────────────────────────────────────────────────────────

class B10_Validation(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Headers
        hdr_wrong = Rectangle(width=5.5, height=0.6, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.20, stroke_width=1.5).move_to(LEFT * 3.2 + UP * 2.8)
        hdr_right = Rectangle(width=5.5, height=0.6, color=TEAL,   fill_color=TEAL,   fill_opacity=0.20, stroke_width=1.5).move_to(RIGHT * 3.2 + UP * 2.8)
        t_wrong   = Text("TRUST THE REPORT", font=DISPLAY, font_size=17, color=CRIMSON).move_to(hdr_wrong)
        t_right   = Text("CHECK WORLD STATE", font=DISPLAY, font_size=17, color=TEAL).move_to(hdr_right)

        # Wrong path
        wrong1 = Rectangle(width=5.0, height=0.7, color=INK, fill_opacity=0, stroke_width=1).move_to(LEFT * 3.2 + UP * 1.6)
        wrong2 = Rectangle(width=5.0, height=0.7, color=INK, fill_opacity=0, stroke_width=1).move_to(LEFT * 3.2 + UP * 0.7)
        t_w1   = Text("Agent → 'COMPLETED'", font=MONO, font_size=15, color=INK).move_to(wrong1)
        t_w2   = Text("User: done ✗", font=MONO, font_size=15, color=CRIMSON).move_to(wrong2)

        # Right path
        right1 = Rectangle(width=5.0, height=0.7, color=INK, fill_opacity=0, stroke_width=1).move_to(RIGHT * 3.2 + UP * 1.6)
        right2 = Rectangle(width=5.0, height=0.7, color=INK, fill_opacity=0, stroke_width=1).move_to(RIGHT * 3.2 + UP * 0.7)
        right3 = Rectangle(width=5.0, height=0.7, color=INK, fill_opacity=0, stroke_width=1).move_to(RIGHT * 3.2 + DOWN * 0.2)
        right4 = Rectangle(width=5.0, height=0.7, color=TEAL, fill_color=TEAL, fill_opacity=0.10, stroke_width=1.5).move_to(RIGHT * 3.2 + DOWN * 1.1)
        t_r1   = Text("Agent → 'COMPLETED'", font=MONO, font_size=15, color=INK).move_to(right1)
        t_r2   = Text("User checks server state", font=MONO, font_size=15, color=INK).move_to(right2)
        t_r3   = Text("Server: email still exists?", font=MONO, font_size=15, color=INK).move_to(right3)
        t_r4   = Text("MISMATCH CAUGHT ✓", font=MONO, font_size=15, color=TEAL).move_to(right4)

        self.play(GrowFromCenter(hdr_wrong), GrowFromCenter(hdr_right), run_time=0.5)
        self.play(Write(t_wrong), Write(t_right), run_time=0.5)
        self.play(GrowFromCenter(wrong1), GrowFromCenter(right1), run_time=0.4)
        self.play(Write(t_w1), Write(t_r1), run_time=0.4)
        self.play(GrowFromCenter(wrong2), GrowFromCenter(right2), run_time=0.4)
        self.play(Write(t_w2), Write(t_r2), run_time=0.4)
        self.play(GrowFromCenter(right3), run_time=0.3)
        self.play(Write(t_r3), run_time=0.3)
        self.play(GrowFromCenter(right4), run_time=0.3)
        self.play(Write(t_r4), run_time=0.3)
        self.wait(DUR["B10"] - 4.3)


# ── B11 — QuoteScope ─────────────────────────────────────────────────────────

class B11_QuoteScope(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The agent did not represent the gap between 'reset the "
            "local email client' and 'delete the email from the server.' "
            "Those are different operations, and the agent had no model "
            "of either its own scope or the structural dependencies "
            "between them.",
            "— the agent's blind spot",
            None,
            "different operations",
            DUR["B11"],
        )


# ── B12 — ExampleSchedule (THE EXAMPLE) ──────────────────────────────────────

class B12_ExampleSchedule(Scene):
    def construct(self):
        total = DUR["B12"]

        title = Text("The Same Gap — Different Domain", font=DISPLAY, font_size=20, color=INK)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("AGENT WORLD", font=DISPLAY, font_size=19, color=TEAL).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("USER WORLD", font=DISPLAY, font_size=19, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.55)

        sub_l = Text("your calendar view", font=DISPLAY, font_size=15, color=INK).move_to(LEFT * 3.2 + UP * 0.85)
        sub_r = Text("three attendees' calendars", font=DISPLAY, font_size=15, color=INK).move_to(RIGHT * 3.2 + UP * 0.85)

        op_l = Text("'cancel' = remove from view", font="PT Mono", font_size=14, color=TEAL).move_to(LEFT * 3.2 + UP * 0.1)
        op_r = Text("'cancel' = send cancellation", font="PT Mono", font_size=14, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 0.1)

        res_l = Text("DONE", font=DISPLAY, font_size=20, color=TEAL, weight=BOLD).move_to(LEFT * 3.2 + DOWN * 0.75)
        res_r = Text("NOT DONE", font=DISPLAY, font_size=20, color=CRIMSON, weight=BOLD).move_to(RIGHT * 3.2 + DOWN * 0.75)

        note = Text("Agent: 'Cancelled.' Two colleagues show up.", font=DISPLAY, font_size=16, color=INK).move_to(DOWN * 2.5)
        note_rect = (Rectangle(width=8.5, height=0.5, fill_color=CRIMSON, fill_opacity=0.10,
                               stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.5))

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.7)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(sub_l), Write(sub_r), run_time=0.4)
        self.play(Write(op_l), Write(op_r), run_time=0.5)
        self.play(FadeIn(res_l), FadeIn(res_r), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.3)
        self.play(Write(note), run_time=0.4)
        self.wait(max(0.5, total - 4.2))
