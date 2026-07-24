"""vox_scenes.py — vox-subagent-context
Why One Subagent Query Saved 48% of the Context Window.
One scene per GRAPHIC / CARD beat whose source is own.
STILL ai beat (B07) gets no scene — compiles as slate.
"""
import sys
import pathlib
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *  # noqa: F401,F403


class B01_Title(Scene):
    def construct(self):
        eyebrow = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                       color=INK, font_size=22, weight="MEDIUM")
        eyebrow.to_edge(UP, buff=0.7)
        t1 = Text("Why one subagent query", font=SERIF, color=INK, font_size=44)
        t2 = Text("saved 48% of the context window", font=SERIF, color=TEAL, font_size=44)
        title = VGroup(t1, t2).arrange(DOWN, center=True, buff=0.25)
        title.scale_to_fit_width(12.5)
        title.move_to(ORIGIN + UP * 0.2)
        rule = Line(title.get_corner(DL) + DOWN * 0.15,
                    title.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=TEAL)
        self.play(FadeIn(eyebrow, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(title), Create(rule), run_time=1.0)
        self.wait(7.4)


class B02_ContextFilling(Scene):
    def construct(self):
        title = Text("the context window fills as you read", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        # Vertical context bar
        bar_width = 2.2
        bar_total_height = 5.0
        bar_left = -4.5

        # Background outline
        outline = Rectangle(width=bar_width, height=bar_total_height)
        outline.set_fill(GROUND, 0).set_stroke(SLATE, 1.5)
        outline.move_to(np.array([bar_left, -0.3, 0]))

        # Build segment (30% = 1.5 units tall), from bottom
        build_h = bar_total_height * 0.30
        build_bar = Rectangle(width=bar_width, height=build_h)
        build_bar.set_fill(TEAL, 0.85).set_stroke(TEAL, 0)
        build_bar.move_to(outline.get_bottom() + UP * (build_h / 2))

        # Research segment (48% = 2.4 units), directly above build
        research_h = bar_total_height * 0.48
        research_bar = Rectangle(width=bar_width, height=research_h)
        research_bar.set_fill(CRIMSON, 0.80).set_stroke(CRIMSON, 0)
        research_bar.next_to(build_bar, UP, buff=0)

        # Labels on the bar
        build_label = Text("build  30%", font=MONO, color=INK, font_size=17)
        build_label.move_to(build_bar.get_center())

        research_label = Text("research  48%", font=MONO, color=INK, font_size=17)
        research_label.move_to(research_bar.get_center())

        # 22% remaining indicator
        remaining_label = Text("22% remains", font=SERIF, color=CRIMSON, font_size=20)
        remaining_label.next_to(outline, UP, buff=0.25)

        note = Text("barely enough for one feedback draft", font=SERIF, color=SLATE, font_size=18)
        note.next_to(remaining_label, DOWN, buff=0.2)

        # Right side: percentage readout
        pct_before = Text("30% used", font=DISPLAY, color=TEAL,
                          font_size=22, weight="MEDIUM")
        pct_before.move_to(np.array([2.5, 1.5, 0]))
        arrow_right = Text("after research:", font=SERIF, color=INK, font_size=20)
        arrow_right.next_to(pct_before, DOWN, buff=0.5)
        pct_after = Text("78% used", font=DISPLAY, color=CRIMSON,
                         font_size=28, weight="MEDIUM")
        pct_after.next_to(arrow_right, DOWN, buff=0.3)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(outline), run_time=0.4)
        self.play(FadeIn(build_bar), FadeIn(build_label),
                  FadeIn(pct_before), run_time=0.6)
        self.play(FadeIn(research_bar), FadeIn(research_label),
                  FadeIn(arrow_right), FadeIn(pct_after), run_time=0.8)
        self.play(FadeIn(remaining_label), FadeIn(note), run_time=0.5)
        self.wait(8.2)


class B03_Question(Scene):
    def construct(self):
        l1 = Text("10 minutes of research.", font=SERIF, color=INK, font_size=44)
        l2 = Text("48% of the window gone.", font=SERIF, color=CRIMSON, font_size=44)
        l3 = Text("Why?", font=SERIF, color=INK, font_size=44)
        question = VGroup(l1, l2, l3).arrange(DOWN, center=True, buff=0.3)
        question.scale_to_fit_width(11.0)
        question.move_to(ORIGIN)
        rule = Line(question.get_corner(DL) + DOWN * 0.2,
                    question.get_corner(DR) + DOWN * 0.2,
                    stroke_width=1.5, color=CRIMSON)
        self.play(FadeIn(l1), run_time=0.5)
        self.play(FadeIn(l2), run_time=0.5)
        self.play(FadeIn(l3), Create(rule), run_time=0.6)
        self.wait(7.4)


class B04_SharedWindow(Scene):
    def construct(self):
        title = Text("one window, no unread", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Context bar on the left
        bar_width = 1.8
        bar_total_height = 4.5
        bar_x = -4.2

        outline = Rectangle(width=bar_width, height=bar_total_height)
        outline.set_fill(GROUND, 0).set_stroke(SLATE, 1.5)
        outline.move_to(np.array([bar_x, -0.3, 0]))

        # Build (teal) at bottom - 30%
        build_h = bar_total_height * 0.30
        build_bar = Rectangle(width=bar_width, height=build_h)
        build_bar.set_fill(TEAL, 0.85).set_stroke(TEAL, 0)
        build_bar.move_to(outline.get_bottom() + UP * (build_h / 2))
        build_lbl = Text("build", font=MONO, color=INK, font_size=15)
        build_lbl.move_to(build_bar.get_center())

        # Files arriving one at a time (crimson segments)
        file_names = [
            "policy doc",
            "LMS export",
            "meeting notes",
            "syllabus section",
        ]
        file_heights = [bar_total_height * 0.11] * 4
        file_bars = []
        file_labels = []
        current_top = build_bar.get_top()
        for name, fh in zip(file_names, file_heights):
            fb = Rectangle(width=bar_width, height=fh)
            fb.set_fill(CRIMSON, 0.75).set_stroke(CRIMSON, 0)
            fb.move_to(current_top + UP * (fh / 2))
            fl = Text(name, font=MONO, color=INK, font_size=13)
            fl.move_to(fb.get_center())
            file_bars.append(fb)
            file_labels.append(fl)
            current_top = fb.get_top()

        # Right side annotation
        note_lines = [
            "Claude reads each file",
            "into the session.",
            "There is no unread.",
        ]
        note_group = VGroup(*[Text(l, font=SERIF, color=INK, font_size=20)
                               for l in note_lines])
        note_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        note_group.move_to(np.array([2.5, 0.5, 0]))

        # Convert VGroup slice to plain list for zip with None sentinel
        notes_tail = list(note_group)[1:] + [None]
        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(outline), FadeIn(build_bar), FadeIn(build_lbl), run_time=0.6)
        self.play(FadeIn(note_group[0]), run_time=0.4)
        for fb, fl, note in zip(file_bars, file_labels, notes_tail):
            self.play(FadeIn(fb), FadeIn(fl), run_time=0.4)
            if note is not None:
                self.play(FadeIn(note), run_time=0.3)
        self.wait(8.0)


class B05_SubagentIsolation(Scene):
    def construct(self):
        title = Text("the subagent runs in its own window", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        # Left box: subagent context (fills with crimson)
        left_outline = Rectangle(width=4.5, height=3.5)
        left_outline.set_fill(GROUND, 0).set_stroke(CRIMSON, 2.0)
        left_outline.move_to(np.array([-3.5, -0.3, 0]))
        left_title = Text("subagent context", font=DISPLAY,
                          color=CRIMSON, font_size=18, weight="MEDIUM")
        left_title.next_to(left_outline, UP, buff=0.15)

        # Files inside subagent box
        sub_files = VGroup(
            Text("policy doc", font=MONO, color=INK, font_size=16),
            Text("LMS export", font=MONO, color=INK, font_size=16),
            Text("meeting notes", font=MONO, color=INK, font_size=16),
            Text("3 policy revisions", font=MONO, color=INK, font_size=16),
        )
        sub_files.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        sub_files.move_to(left_outline.get_center())

        # Right box: main session (stays clean, teal)
        right_outline = Rectangle(width=4.0, height=3.5)
        right_outline.set_fill(GROUND, 0).set_stroke(TEAL, 2.0)
        right_outline.move_to(np.array([3.5, -0.3, 0]))
        right_title = Text("main session context", font=DISPLAY,
                           color=TEAL, font_size=18, weight="MEDIUM")
        right_title.next_to(right_outline, UP, buff=0.15)

        # Main session: only the build
        main_build = Text("grading build  30%", font=MONO, color=TEAL, font_size=18)
        main_build.move_to(right_outline.get_center() + DOWN * 0.5)

        # Summary arrow
        arrow = Arrow(left_outline.get_right(), right_outline.get_left(),
                      buff=0.1, stroke_width=2.5, color=INK,
                      tip_length=0.22)
        arrow_label = Text("summary (300 words)", font=SERIF, color=INK, font_size=17)
        arrow_label.next_to(arrow, UP, buff=0.15)

        # After arrow: summary block in main context
        summary_block = Rectangle(width=3.0, height=0.8)
        summary_block.set_fill(TEAL, 0.25).set_stroke(TEAL, 1.0)
        summary_block.next_to(main_build, UP, buff=0.3)
        summary_lbl = Text("summary  +2%", font=MONO, color=INK, font_size=16)
        summary_lbl.move_to(summary_block.get_center())

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(left_outline), FadeIn(left_title),
                  Create(right_outline), FadeIn(right_title), run_time=0.6)
        self.play(FadeIn(main_build), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(f, shift=DOWN * 0.1) for f in sub_files],
                              lag_ratio=0.2, run_time=0.8))
        self.play(Create(arrow), FadeIn(arrow_label), run_time=0.6)
        self.play(FadeIn(summary_block), FadeIn(summary_lbl), run_time=0.5)
        self.wait(8.0)


class B06_SideBySide(Scene):
    def construct(self):
        title = Text("same research, different cost", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        bar_w = 2.0
        bar_total = 4.5

        # --- WITHOUT subagent ---
        left_x = -3.0
        outline_l = Rectangle(width=bar_w, height=bar_total)
        outline_l.set_fill(GROUND, 0).set_stroke(SLATE, 1.5)
        outline_l.move_to(np.array([left_x, -0.3, 0]))

        build_h_l = bar_total * 0.30
        build_l = Rectangle(width=bar_w, height=build_h_l)
        build_l.set_fill(TEAL, 0.80).set_stroke(TEAL, 0)
        build_l.move_to(outline_l.get_bottom() + UP * (build_h_l / 2))
        build_lbl_l = Text("build 30%", font=MONO, color=INK, font_size=15)
        build_lbl_l.move_to(build_l.get_center())

        research_h_l = bar_total * 0.48
        research_l = Rectangle(width=bar_w, height=research_h_l)
        research_l.set_fill(CRIMSON, 0.78).set_stroke(CRIMSON, 0)
        research_l.next_to(build_l, UP, buff=0)
        research_lbl_l = Text("research 48%", font=MONO, color=INK, font_size=15)
        research_lbl_l.move_to(research_l.get_center())

        label_l = Text("without subagent", font=DISPLAY,
                       color=CRIMSON, font_size=18, weight="MEDIUM")
        label_l.next_to(outline_l, DOWN, buff=0.25)
        used_l = Text("78% used", font=DISPLAY, color=CRIMSON,
                      font_size=20, weight="MEDIUM")
        used_l.next_to(outline_l, UP, buff=0.2)
        remain_l = Text("22% remains", font=SERIF, color=CRIMSON, font_size=17)
        remain_l.next_to(used_l, DOWN, buff=0.1)

        # --- WITH subagent ---
        right_x = 3.0
        outline_r = Rectangle(width=bar_w, height=bar_total)
        outline_r.set_fill(GROUND, 0).set_stroke(SLATE, 1.5)
        outline_r.move_to(np.array([right_x, -0.3, 0]))

        build_h_r = bar_total * 0.30
        build_r = Rectangle(width=bar_w, height=build_h_r)
        build_r.set_fill(TEAL, 0.80).set_stroke(TEAL, 0)
        build_r.move_to(outline_r.get_bottom() + UP * (build_h_r / 2))
        build_lbl_r = Text("build 30%", font=MONO, color=INK, font_size=15)
        build_lbl_r.move_to(build_r.get_center())

        summary_h_r = bar_total * 0.02
        summary_r = Rectangle(width=bar_w, height=max(summary_h_r, 0.18))
        summary_r.set_fill(TEAL, 0.55).set_stroke(TEAL, 0)
        summary_r.next_to(build_r, UP, buff=0)
        summary_lbl_r = Text("+2% summary", font=MONO, color=INK, font_size=13)
        summary_lbl_r.move_to(summary_r.get_center())

        label_r = Text("with subagent", font=DISPLAY,
                       color=TEAL, font_size=18, weight="MEDIUM")
        label_r.next_to(outline_r, DOWN, buff=0.25)
        used_r = Text("32% used", font=DISPLAY, color=TEAL,
                      font_size=20, weight="MEDIUM")
        used_r.next_to(outline_r, UP, buff=0.2)
        remain_r = Text("68% remains", font=SERIF, color=TEAL, font_size=17)
        remain_r.next_to(used_r, DOWN, buff=0.1)

        self.play(FadeIn(title), run_time=0.5)
        # Left side
        self.play(Create(outline_l), FadeIn(label_l), run_time=0.4)
        self.play(FadeIn(build_l), FadeIn(build_lbl_l), run_time=0.4)
        self.play(FadeIn(research_l), FadeIn(research_lbl_l),
                  FadeIn(used_l), FadeIn(remain_l), run_time=0.6)
        # Right side
        self.play(Create(outline_r), FadeIn(label_r), run_time=0.4)
        self.play(FadeIn(build_r), FadeIn(build_lbl_r), run_time=0.4)
        self.play(FadeIn(summary_r), FadeIn(summary_lbl_r),
                  FadeIn(used_r), FadeIn(remain_r), run_time=0.6)
        self.wait(8.2)


class B08_HeuristicCard(Scene):
    def construct(self):
        title = Text("the heuristic", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        rows_data = [
            ("task reads many docs", "subagent"),
            ("task returns a summary", "subagent"),
        ]
        rows = VGroup()
        for condition, action in rows_data:
            row_bg = Rectangle(width=12.0, height=1.2)
            row_bg.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.5)
            cond_text = Text(condition, font=SERIF, color=INK, font_size=22)
            cond_text.move_to(row_bg.get_center() + LEFT * 2.8)
            arrow_text = Text("->", font=MONO, color=TEAL, font_size=22)
            arrow_text.move_to(row_bg.get_center() + RIGHT * 1.0)
            action_text = Text(action, font=DISPLAY, color=TEAL,
                               font_size=22, weight="MEDIUM")
            action_text.move_to(row_bg.get_center() + RIGHT * 3.2)
            rows.add(VGroup(row_bg, cond_text, arrow_text, action_text))

        rows.arrange(DOWN, buff=0.5)
        rows.move_to(ORIGIN + UP * 0.3)
        rows.scale_to_fit_width(13.5)

        footer = Text("the subagent is the design, not the workaround",
                      font=SERIF, color=SLATE, font_size=20)
        footer.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(footer), run_time=0.5)
        self.wait(7.5)


class B09_Endcard(Scene):
    def construct(self):
        topic = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                     color=INK, font_size=20, weight="MEDIUM")
        topic.to_edge(UP, buff=0.8)

        m1 = Text("Research fills context.", font=SERIF, color=CRIMSON, font_size=42)
        m2 = Text("The subagent takes the fill.", font=SERIF, color=INK, font_size=42)
        m3 = Text("The build stays clean.", font=SERIF, color=TEAL, font_size=42)
        main_text = VGroup(m1, m2, m3).arrange(DOWN, center=True, buff=0.35)
        main_text.scale_to_fit_width(12.0)
        main_text.move_to(ORIGIN + UP * 0.2)

        rule = Line(main_text.get_corner(DL) + DOWN * 0.15,
                    main_text.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=TEAL)

        handle = Text("@nikbearbrown", font=SERIF, color=CRIMSON, font_size=24)
        handle.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(main_text), Create(rule), run_time=1.0)
        self.play(FadeIn(handle), run_time=0.5)
        self.wait(8.0)
