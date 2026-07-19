import sys, pathlib, os, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {}
try:
    _data = json.load(open(os.path.join(os.path.dirname(__file__), "beat_sheet.json")))
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0)
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Why an Agent Obeys the Web Page", font=SERIF, color=INK, font_size=40, weight=BOLD)
        t2 = Text("Instead of You", font=SERIF, color=INK, font_size=40, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.15).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(block, shift=UP * 0.1), Create(u), run_time=1.1)
        self.wait(max(0.5, total - 1.6))


class B03_TheQuestion(Scene):
    def construct(self):
        _quote_scene(
            self,
            "You told the agent exactly one thing — summarize this page. "
            "The page told it something else, and it complied. "
            "Why can't it tell your instruction from the page's?",
            "— the question this film answers",
            None,
            "Why?",
            DUR["B03"],
        )


class B04_OneChannel(Scene):
    def construct(self):
        total = DUR["B04"]
        brief_lbl = LabelChip("YOUR TASK BRIEF", accent=TEAL, size=20)
        agent_box = RoundedRectangle(width=2.0, height=0.9, corner_radius=0.12,
                                     color=SLATE, fill_opacity=0)
        agent_box.set_stroke(color=SLATE, width=2, opacity=1)
        agent_txt = Text("AGENT", font=DISPLAY, color=SLATE, font_size=22)
        agent_grp = VGroup(agent_box, agent_txt)
        funnel = RoundedRectangle(width=1.4, height=0.7, corner_radius=0.1,
                                  color=TEAL, fill_opacity=0)
        funnel.set_stroke(color=TEAL, width=2, opacity=1)
        funnel_txt = Text("channel", font=SERIF, color=TEAL, font_size=18, slant=ITALIC)
        funnel_grp = VGroup(funnel, funnel_txt)
        row = VGroup(brief_lbl, funnel_grp, agent_grp).arrange(RIGHT, buff=0.7).move_to(ORIGIN)
        arrow1 = Arrow(brief_lbl.get_right(), funnel_grp.get_left(), buff=0.1,
                       color=TEAL, stroke_width=2)
        arrow2 = Arrow(funnel_grp.get_right(), agent_grp.get_left(), buff=0.1,
                       color=TEAL, stroke_width=2)
        self.play(FadeIn(brief_lbl, shift=RIGHT * 0.1), run_time=0.4)
        self.play(GrowArrow(arrow1), FadeIn(funnel_grp, shift=RIGHT * 0.1), run_time=0.5)
        self.play(GrowArrow(arrow2), FadeIn(agent_grp, shift=RIGHT * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.4))


class B05_TwoSources(Scene):
    def construct(self):
        total = DUR["B05"]
        brief_lbl = LabelChip("YOUR TASK BRIEF", accent=TEAL, size=20)
        page_lbl = LabelChip("PAGE CONTENT", accent=CRIMSON, size=20)
        sources = VGroup(brief_lbl, page_lbl).arrange(DOWN, buff=0.4)
        sources.move_to(LEFT * 3.5)
        funnel = RoundedRectangle(width=1.4, height=1.3, corner_radius=0.1,
                                  color=SLATE, fill_opacity=0)
        funnel.set_stroke(color=SLATE, width=2, opacity=1)
        funnel_txt = Text("channel", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        funnel_grp = VGroup(funnel, funnel_txt).move_to(ORIGIN)
        agent_box = RoundedRectangle(width=2.0, height=0.9, corner_radius=0.12,
                                     color=SLATE, fill_opacity=0)
        agent_box.set_stroke(color=SLATE, width=2, opacity=1)
        agent_txt = Text("AGENT", font=DISPLAY, color=SLATE, font_size=22)
        agent_grp = VGroup(agent_box, agent_txt).move_to(RIGHT * 3.5)
        arrow_t = Arrow(brief_lbl.get_right(), funnel_grp.get_left() + UP * 0.25,
                        buff=0.1, color=TEAL, stroke_width=2)
        arrow_c = Arrow(page_lbl.get_right(), funnel_grp.get_left() + DOWN * 0.25,
                        buff=0.1, color=CRIMSON, stroke_width=2)
        arrow_out = Arrow(funnel_grp.get_right(), agent_grp.get_left(),
                          buff=0.1, color=SLATE, stroke_width=2)
        self.play(FadeIn(brief_lbl, shift=RIGHT * 0.1), run_time=0.4)
        self.play(FadeIn(page_lbl, shift=RIGHT * 0.1), run_time=0.4)
        self.play(GrowArrow(arrow_t), GrowArrow(arrow_c), FadeIn(funnel_grp), run_time=0.6)
        self.play(GrowArrow(arrow_out), FadeIn(agent_grp, shift=RIGHT * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.9))


class B06_SectionMechanism(Scene):
    def construct(self):
        total = DUR["B06"]
        heading = Text("THE MECHANISM", font=DISPLAY, color=INK, font_size=48, weight=BOLD)
        sub = Text("one channel, no wall", font=SERIF, color=SLATE, font_size=28, slant=ITALIC)
        block = VGroup(heading, sub).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(heading, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 0.9))


class B07_NoWall(Scene):
    def construct(self):
        total = DUR["B07"]
        teal_rect = Rectangle(width=2.6, height=1.0, color=TEAL, fill_opacity=0.12)
        teal_rect.set_stroke(color=TEAL, width=2, opacity=1)
        teal_txt = Text("your instruction", font=SERIF, color=TEAL, font_size=22)
        teal_grp = VGroup(teal_rect, teal_txt).arrange(DOWN, buff=0.05)
        teal_grp.move_to(LEFT * 1.45 + UP * 0.3)
        crim_rect = Rectangle(width=2.6, height=1.0, color=CRIMSON, fill_opacity=0.12)
        crim_rect.set_stroke(color=CRIMSON, width=2, opacity=1)
        crim_txt = Text("page content", font=SERIF, color=CRIMSON, font_size=22)
        crim_grp = VGroup(crim_rect, crim_txt).arrange(DOWN, buff=0.05)
        crim_grp.move_to(RIGHT * 1.45 + UP * 0.3)
        pipe_border = Rectangle(width=5.8, height=1.6, color=SLATE, fill_opacity=0)
        pipe_border.set_stroke(color=SLATE, width=1.5, opacity=0.5)
        pipe_border.move_to(UP * 0.3)
        pipe_lbl = Text("one channel", font=DISPLAY, color=SLATE, font_size=18)
        pipe_lbl.set_opacity(0.6)
        pipe_lbl.next_to(pipe_border, UP, buff=0.18)
        no_wall = Text("NO WALL", font=DISPLAY, color=CRIMSON, font_size=24, weight=BOLD)
        no_wall.next_to(pipe_border, DOWN, buff=0.38)
        self.play(FadeIn(pipe_border), FadeIn(pipe_lbl), run_time=0.5)
        self.play(FadeIn(teal_grp, shift=RIGHT * 0.1), run_time=0.5)
        self.play(FadeIn(crim_grp, shift=LEFT * 0.1), run_time=0.5)
        self.play(FadeIn(no_wall, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.0))


class B08_KeyClaim(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Text in a document is treated as a command if it is phrased like one.",
            "— the mechanism",
            None,
            "command",
            DUR["B08"],
        )


class B09_HiddenLine(Scene):
    def construct(self):
        total = DUR["B09"]
        task_lbl = LabelChip("YOUR TASK BRIEF", accent=TEAL, size=19)
        task_txt = Text("summarize these pages", font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        task_grp = VGroup(task_lbl, task_txt).arrange(RIGHT, buff=0.3)
        hidden_lbl = LabelChip("PAGE 2 HIDDEN", accent=CRIMSON, size=19)
        hidden_txt = Text("ignore previous instructions...", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)
        hidden_grp = VGroup(hidden_lbl, hidden_txt).arrange(RIGHT, buff=0.3)
        stack = VGroup(task_grp, hidden_grp).arrange(DOWN, buff=0.45).move_to(LEFT * 1.0)
        agent_box = RoundedRectangle(width=1.8, height=0.85, corner_radius=0.1,
                                     color=SLATE, fill_opacity=0)
        agent_box.set_stroke(color=SLATE, width=2, opacity=1)
        agent_txt = Text("AGENT", font=DISPLAY, color=SLATE, font_size=21)
        agent_grp = VGroup(agent_box, agent_txt).move_to(RIGHT * 3.5)
        arrow_t = Arrow(task_grp.get_right(), agent_grp.get_left() + UP * 0.2,
                        buff=0.1, color=TEAL, stroke_width=2)
        arrow_c = Arrow(hidden_grp.get_right(), agent_grp.get_left() + DOWN * 0.2,
                        buff=0.1, color=CRIMSON, stroke_width=2)
        self.play(FadeIn(task_grp, shift=RIGHT * 0.1), run_time=0.5)
        self.play(FadeIn(hidden_grp, shift=RIGHT * 0.1), run_time=0.5)
        self.play(GrowArrow(arrow_t), GrowArrow(arrow_c), FadeIn(agent_grp), run_time=0.7)
        self.wait(max(0.5, total - 1.7))


class B11_ThreePages(Scene):
    def construct(self):
        total = DUR["B11"]
        pages = []
        page_defs = [
            ("PAGE 1", TEAL, "vendor content", 1.0),
            ("PAGE 2", CRIMSON, "hidden instruction", 1.0),
            ("PAGE 3", TEAL, "vendor content", 1.0),
        ]
        for title, col, sub_txt, op in page_defs:
            rect = RoundedRectangle(width=2.2, height=2.6, corner_radius=0.12,
                                    color=col, fill_opacity=0)
            rect.set_stroke(color=col, width=2, opacity=op)
            lbl = Text(title, font=DISPLAY, color=col, font_size=20)
            lbl.set_opacity(op)
            sub = Text(sub_txt, font=SERIF, color=col, font_size=17, slant=ITALIC)
            sub.set_opacity(op * 0.7)
            g = VGroup(rect, VGroup(lbl, sub).arrange(DOWN, buff=0.2))
            pages.append(g)
        page_grp = VGroup(*pages).arrange(RIGHT, buff=0.45).move_to(UP * 0.1)
        illus = LabelChip("illustrative", accent=SLATE, size=17)
        illus.set_opacity(0.55)
        illus.move_to(DOWN * 2.3)
        self.play(FadeIn(pages[0], shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(pages[1], shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(pages[2], shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.5, total - 1.5))


class B12_Hijack(Scene):
    def construct(self):
        total = DUR["B12"]
        page2_rect = RoundedRectangle(width=2.6, height=3.0, corner_radius=0.12,
                                      color=CRIMSON, fill_opacity=0.08)
        page2_rect.set_stroke(color=CRIMSON, width=2.5, opacity=1)
        page2_lbl = Text("PAGE 2", font=DISPLAY, color=CRIMSON, font_size=22)
        hidden_line = Text("ignore previous instructions...",
                           font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        page2_grp = VGroup(page2_rect, VGroup(page2_lbl, hidden_line).arrange(DOWN, buff=0.25))
        page2_grp.move_to(LEFT * 2.8)
        channel_rect = RoundedRectangle(width=1.4, height=0.75, corner_radius=0.1,
                                        color=SLATE, fill_opacity=0)
        channel_rect.set_stroke(color=SLATE, width=1.5, opacity=0.6)
        channel_txt = Text("channel", font=SERIF, color=SLATE, font_size=17, slant=ITALIC)
        channel_txt.set_opacity(0.6)
        channel_grp = VGroup(channel_rect, channel_txt).move_to(ORIGIN)
        agent_box = RoundedRectangle(width=1.8, height=0.85, corner_radius=0.1,
                                     color=SLATE, fill_opacity=0)
        agent_box.set_stroke(color=SLATE, width=2, opacity=1)
        agent_txt = Text("AGENT", font=DISPLAY, color=SLATE, font_size=21)
        agent_grp = VGroup(agent_box, agent_txt).move_to(RIGHT * 2.8)
        hijack_lbl = Text("HIJACKED", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        hijack_lbl.next_to(agent_grp, DOWN, buff=0.3)
        arrow = Arrow(page2_grp.get_right(), channel_grp.get_left(), buff=0.1,
                      color=CRIMSON, stroke_width=2.5)
        arrow2 = Arrow(channel_grp.get_right(), agent_grp.get_left(), buff=0.1,
                       color=CRIMSON, stroke_width=2.5)
        illus = LabelChip("illustrative", accent=SLATE, size=17)
        illus.set_opacity(0.55)
        illus.move_to(DOWN * 2.5)
        self.play(FadeIn(page2_grp, shift=UP * 0.1), run_time=0.6)
        self.play(GrowArrow(arrow), FadeIn(channel_grp), run_time=0.5)
        self.play(GrowArrow(arrow2), FadeIn(agent_grp), run_time=0.5)
        self.play(FadeIn(hijack_lbl, shift=UP * 0.1), FadeIn(illus), run_time=0.5)
        self.wait(max(0.5, total - 2.1))


class B13_Quote(Scene):
    def construct(self):
        _quote_scene(
            self,
            "There is no built-in wall separating data to summarize from commands to obey.",
            "— the example",
            None,
            "wall",
            DUR["B13"],
        )


class B14_Endcard(Scene):
    def construct(self):
        total = DUR["B14"]
        copy = Text("Your instructions and the content share one channel.",
                    font=SERIF, color=INK, font_size=34, weight=BOLD)
        sub = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        u = Line(copy.get_corner(DL) + DOWN * 0.14, copy.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        block = VGroup(copy, u).move_to(UP * 0.15)
        sub.next_to(block, DOWN, buff=0.5)
        self.play(FadeIn(copy, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.4))
