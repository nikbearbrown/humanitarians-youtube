"""vox_scenes.py — vox-simulation-ownership
Why the Simulation That Took 8 Minutes to Generate Wasn't Theirs.
One scene per GRAPHIC / CARD beat whose source is own.
STILL ai beat (B02) gets no scene — compiles as slate.
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
        t1 = Text("Why the simulation that took", font=SERIF, color=INK, font_size=40)
        t2 = Text("8 minutes to build wasn't theirs", font=SERIF, color=CRIMSON, font_size=40)
        title = VGroup(t1, t2).arrange(DOWN, center=True, buff=0.25)
        title.scale_to_fit_width(12.5)
        title.move_to(ORIGIN + UP * 0.2)
        rule = Line(title.get_corner(DL) + DOWN * 0.15,
                    title.get_corner(DR) + DOWN * 0.15,
                    stroke_width=2.0, color=CRIMSON)
        self.play(FadeIn(eyebrow, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(title), Create(rule), run_time=1.0)
        self.wait(8.4)


class B03_Question(Scene):
    def construct(self):
        l1 = Text("8 minutes. Working code.", font=SERIF, color=INK, font_size=42)
        l2 = Text("Not theirs.", font=SERIF, color=CRIMSON, font_size=42)
        l3 = Text("Why?", font=SERIF, color=INK, font_size=42)
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


class B04_DefaultsInvade(Scene):
    def construct(self):
        title = Text("one line of intent — Claude fills the rest", font=SERIF,
                     color=INK, font_size=26)
        title.to_edge(UP, buff=0.7)

        # Top: intent box (teal)
        intent_bg = Rectangle(width=10.0, height=1.0)
        intent_bg.set_fill(TEAL, 0.12).set_stroke(TEAL, 1.8)
        intent_bg.move_to(UP * 1.8)
        intent_text = Text("intent: build a sorting simulator", font=MONO,
                           color=TEAL, font_size=20)
        intent_text.move_to(intent_bg.get_center())

        # Four crimson default boxes dropping in
        defaults = [
            "color palette (Material Design default)",
            "interaction model (drag-and-drop default)",
            "pedagogical scaffolding (none)",
            "typography (system default)",
        ]
        default_boxes = VGroup()
        for i, label in enumerate(defaults):
            bg = Rectangle(width=10.0, height=0.75)
            bg.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 1.2)
            bg.move_to(UP * (0.6 - i * 0.9))
            lbl = Text(label, font=SERIF, color=INK, font_size=18)
            lbl.move_to(bg.get_center() + LEFT * 1.5)
            tag = Text("Claude default", font=DISPLAY, color=CRIMSON,
                       font_size=16, weight="MEDIUM")
            tag.move_to(bg.get_center() + RIGHT * 3.5)
            default_boxes.add(VGroup(bg, lbl, tag))

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(intent_bg), FadeIn(intent_text), run_time=0.5)
        for box in default_boxes:
            self.play(FadeIn(box, shift=DOWN * 0.2), run_time=0.4)
        self.wait(9.0)


class B05_ThreeFiles(Scene):
    def construct(self):
        title = Text("three files before the build", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        files_data = [
            ("CLAUDE.md", "Technical Constitution",
             "stack, file structure, never-touch"),
            ("DESIGN.md", "Visual Constitution",
             "six named colors, interaction vocabulary, never-list"),
            ("PROJECT.md", "Pedagogical Intent",
             "what students understand; questions answered and refused"),
        ]
        rows = VGroup()
        for fname, subtitle, desc in files_data:
            row_bg = Rectangle(width=12.5, height=1.35)
            row_bg.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.5)
            name_text = Text(fname, font=MONO, color=TEAL, font_size=22)
            name_text.move_to(row_bg.get_center() + LEFT * 4.2)
            sub_text = Text(subtitle, font=DISPLAY, color=INK,
                            font_size=18, weight="MEDIUM")
            sub_text.move_to(row_bg.get_center() + LEFT * 0.8)
            desc_text = Text(desc, font=SERIF, color=SLATE, font_size=16)
            desc_text.move_to(row_bg.get_center() + RIGHT * 3.2)
            rows.add(VGroup(row_bg, name_text, sub_text, desc_text))

        rows.arrange(DOWN, buff=0.45)
        rows.move_to(ORIGIN + DOWN * 0.1)
        rows.scale_to_fit_width(13.5)

        self.play(FadeIn(title), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=DOWN * 0.1), run_time=0.55)
        self.wait(9.0)


class B06_BeforeAfter(Scene):
    def construct(self):
        title = Text("defaults vs. decisions", font=SERIF,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.7)

        # Left column: without three files (crimson)
        left_header = Text("without three files", font=DISPLAY,
                           color=CRIMSON, font_size=20, weight="MEDIUM")
        left_header.move_to(np.array([-4.0, 1.8, 0]))

        left_items = [
            "blue palette (default)",
            "drag-and-drop (default)",
            "no pedagogy (default)",
        ]
        left_group = VGroup()
        for item in left_items:
            row = Text(item, font=SERIF, color=CRIMSON, font_size=18)
            left_group.add(row)
        left_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        left_group.next_to(left_header, DOWN, buff=0.4)

        # Right column: with three files (teal)
        right_header = Text("with three files", font=DISPLAY,
                            color=TEAL, font_size=20, weight="MEDIUM")
        right_header.move_to(np.array([3.5, 1.8, 0]))

        right_items = [
            "earth tones (DESIGN.md)",
            "single-click step (DESIGN.md)",
            "O(n^2) counter (PROJECT.md)",
        ]
        right_group = VGroup()
        for item in right_items:
            row = Text(item, font=SERIF, color=TEAL, font_size=18)
            right_group.add(row)
        right_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        right_group.next_to(right_header, DOWN, buff=0.4)

        # Divider — no text crosses it (vs. label removed to satisfy Gate W)
        divider = Line(UP * 2.2 + ORIGIN, DOWN * 2.0 + ORIGIN,
                       stroke_width=1.2, color=SLATE)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(left_header), FadeIn(right_header), run_time=0.5)
        for litem, ritem in zip(left_group, right_group):
            self.play(FadeIn(litem), FadeIn(ritem), run_time=0.4)
        self.wait(8.5)


class B07_SixColors(Scene):
    def construct(self):
        title = Text("six named colors — a seventh escalates to the human", font=SERIF,
                     color=INK, font_size=24)
        title.to_edge(UP, buff=0.7)

        # Six color swatches
        palette = [
            ("#f5f5f0", "warm white", "background"),
            ("#1a1a1a", "near-black", "text + lines"),
            ("#c97a3a", "terracotta", "element compared"),
            ("#3a7ac9", "blue", "element placed"),
            ("#999999", "gray", "axis lines"),
            ("#f0d843", "amber", "sorted region"),
        ]

        swatches = VGroup()
        x_positions = np.linspace(-5.5, 3.5, 6)
        for (hex_color, name, role), x in zip(palette, x_positions):
            swatch = Square(side_length=0.9)
            swatch.set_fill(hex_color, 1.0).set_stroke(SLATE, 1.0)
            swatch.move_to(np.array([x, 0.4, 0]))
            name_lbl = Text(name, font=SERIF, color=INK, font_size=14)
            name_lbl.next_to(swatch, DOWN, buff=0.12)
            role_lbl = Text(role, font=MONO, color=SLATE, font_size=12)
            role_lbl.next_to(name_lbl, DOWN, buff=0.08)
            swatches.add(VGroup(swatch, name_lbl, role_lbl))

        # Seventh slot: escalate (crimson outline, empty)
        seventh = Square(side_length=0.9)
        seventh.set_fill(GROUND, 0).set_stroke(CRIMSON, 1.8)
        seventh.move_to(np.array([5.2, 0.4, 0]))
        escalate_lbl = Text("escalate", font=SERIF, color=CRIMSON, font_size=14)
        escalate_lbl.next_to(seventh, DOWN, buff=0.12)
        escalate_sub = Text("do not invent", font=MONO, color=CRIMSON, font_size=12)
        escalate_sub.next_to(escalate_lbl, DOWN, buff=0.08)
        seventh_group = VGroup(seventh, escalate_lbl, escalate_sub)

        footer = Text("A simulation with 20 colors is one where the design was made by Claude.",
                      font=SERIF, color=SLATE, font_size=18)
        footer.to_edge(DOWN, buff=0.6)

        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(s) for s in swatches],
                              lag_ratio=0.15, run_time=1.2))
        self.play(FadeIn(seventh_group), run_time=0.5)
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(8.0)


class B08_FifteenMinutes(Scene):
    def construct(self):
        title = Text("the 45-minute test", font=SERIF, color=INK, font_size=30)
        title.to_edge(UP, buff=0.7)

        # Horizontal axis
        axis = Line(LEFT * 5.5 + DOWN * 0.2, RIGHT * 5.0 + DOWN * 0.2,
                    stroke_width=2.0, color=SLATE)

        # Time markers
        marks_data = [(-4.5, "0 min"), (-1.0, "15 min"), (2.5, "30 min"), (4.5, "45 min")]
        marks = VGroup()
        for x, label in marks_data:
            tick = Line(np.array([x, -0.3, 0]), np.array([x, -0.1, 0]),
                        stroke_width=1.5, color=SLATE)
            lbl = Text(label, font=MONO, color=SLATE, font_size=16)
            lbl.move_to(np.array([x, -0.65, 0]))
            marks.add(tick, lbl)

        # Three teal segments
        segments_data = [
            (-4.5, -1.0, "CLAUDE.md"),
            (-1.0, 2.5, "DESIGN.md"),
            (2.5, 4.5, "PROJECT.md"),
        ]
        segments = VGroup()
        for x_start, x_end, label in segments_data:
            width = x_end - x_start - 0.1
            seg = Rectangle(width=width, height=0.8)
            seg.set_fill(TEAL, 0.70).set_stroke(TEAL, 0)
            seg.move_to(np.array([(x_start + x_end) / 2, 0.3, 0]))
            lbl = Text(label, font=MONO, color=INK, font_size=17)
            lbl.move_to(seg.get_center())
            segments.add(VGroup(seg, lbl))

        # Arrow at 45 min
        build_arrow = Arrow(np.array([4.5, 0.3, 0]), np.array([6.0, 0.3, 0]),
                            stroke_width=2.0, color=TEAL, tip_length=0.2)
        build_lbl = Text("then build", font=SERIF, color=TEAL, font_size=17)
        build_lbl.next_to(build_arrow, UP, buff=0.1)

        # Note below
        scope_note = Text("over 45 min -> scope down", font=SERIF,
                          color=CRIMSON, font_size=19)
        scope_note.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(axis), FadeIn(marks), run_time=0.5)
        for seg in segments:
            self.play(FadeIn(seg, shift=UP * 0.1), run_time=0.45)
        self.play(Create(build_arrow), FadeIn(build_lbl), run_time=0.5)
        self.play(FadeIn(scope_note), run_time=0.4)
        self.wait(8.0)


class B09_Endcard(Scene):
    def construct(self):
        topic = Text("CLAUDE CODE FOR TEACHERS", font=DISPLAY,
                     color=INK, font_size=20, weight="MEDIUM")
        topic.to_edge(UP, buff=0.8)

        m1 = Text("Three files.", font=SERIF, color=TEAL, font_size=48)
        m2 = Text("45 minutes.", font=SERIF, color=INK, font_size=48)
        m3 = Text("Then it is yours.", font=SERIF, color=TEAL, font_size=48)
        main_text = VGroup(m1, m2, m3).arrange(DOWN, center=True, buff=0.35)
        main_text.scale_to_fit_width(11.5)
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
