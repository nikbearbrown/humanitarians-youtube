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
        t1 = Text("Why a Plan That Reads Perfectly", font=SERIF, color=INK, font_size=34, weight=BOLD)
        t2 = Text("Can Still Delete Your Files", font=SERIF, color=INK, font_size=34, weight=BOLD)
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
            "A plan that is fluent, logically ordered, and cleanly numbered should be safe. "
            "Steps four and five are irreversible and unsequenced from any backup. "
            "Why doesn't the format tell you?",
            "— the question this film answers",
            None,
            "Why?",
            DUR["B03"],
        )


class B04_SixSteps(Scene):
    def construct(self):
        total = DUR["B04"]
        steps = [
            "1. Inventory",
            "2. Identify duplicates",
            "3. Naming convention",
            "4. Apply convention",
            "5. Remove duplicates",
            "6. Manifest",
        ]
        step_texts = VGroup(*[
            Text(s, font=MONO, color=TEAL, font_size=26)
            for s in steps
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.28).move_to(ORIGIN)
        header = Text("THE PLAN", font=DISPLAY, color=SLATE, font_size=20)
        header.next_to(step_texts, UP, buff=0.4)
        self.play(FadeIn(header, shift=DOWN * 0.1), run_time=0.4)
        for st in step_texts:
            self.play(FadeIn(st, shift=RIGHT * 0.1), run_time=0.25)
        self.wait(max(0.3, total - 0.4 - len(steps) * 0.25 - 0.2))


class B05_StepsRevealed(Scene):
    def construct(self):
        total = DUR["B05"]
        steps = [
            ("1. Inventory", TEAL, ""),
            ("2. Identify duplicates", TEAL, ""),
            ("3. Naming convention", TEAL, ""),
            ("4. Apply convention", CRIMSON, "NO BACKUP"),
            ("5. Remove duplicates", CRIMSON, "NO DRY RUN"),
            ("6. Manifest", TEAL, ""),
        ]
        step_texts = VGroup()
        for label, color, _ in steps:
            step_texts.add(Text(label, font=MONO, color=color, font_size=26))
        step_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.28).move_to(LEFT * 1.2)

        header = Text("THE PLAN", font=DISPLAY, color=SLATE, font_size=20)
        header.next_to(step_texts, UP, buff=0.4)

        danger_labels = VGroup()
        for i, (_, color, tag) in enumerate(steps):
            if tag:
                chip = Text(tag, font=MONO, color=CRIMSON, font_size=18)
                chip.next_to(step_texts[i], RIGHT, buff=0.35)
                danger_labels.add(chip)

        self.play(FadeIn(header), FadeIn(step_texts), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(danger_labels, shift=LEFT * 0.1), run_time=0.7)
        self.wait(max(0.3, total - 1.7))


class B06_SectionMechanism(Scene):
    def construct(self):
        total = DUR["B06"]
        heading = Text("THE MECHANISM", font=DISPLAY, color=INK, font_size=48, weight=BOLD)
        sub = Text("coherence is not safety", font=SERIF, color=SLATE, font_size=28, slant=ITALIC)
        block = VGroup(heading, sub).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(heading, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 0.9))


class B07_FormVsSafety(Scene):
    def construct(self):
        total = DUR["B07"]

        # FORM column (TEAL)
        form_header = Text("FORM", font=DISPLAY, color=TEAL, font_size=30, weight=BOLD)
        form_items = VGroup(
            Text("fluent prose", font=SERIF, color=TEAL, font_size=22),
            Text("numbered steps", font=SERIF, color=TEAL, font_size=22),
            Text("logical order", font=SERIF, color=TEAL, font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        form_col = VGroup(form_header, form_items).arrange(DOWN, buff=0.3)
        form_border = Rectangle(width=3.2, height=2.8, color=TEAL, fill_opacity=0.06)
        form_border.set_stroke(color=TEAL, width=2, opacity=1)
        form_grp = VGroup(form_border, form_col)
        form_border.move_to(LEFT * 3.0)
        form_col.move_to(LEFT * 3.0)

        # SAFETY column (CRIMSON)
        safe_header = Text("SAFETY", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        safe_items = VGroup(
            Text("backup?", font=SERIF, color=CRIMSON, font_size=22),
            Text("dry run?", font=SERIF, color=CRIMSON, font_size=22),
            Text("review?", font=SERIF, color=CRIMSON, font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        safe_col = VGroup(safe_header, safe_items).arrange(DOWN, buff=0.3)
        safe_border = Rectangle(width=3.2, height=2.8, color=CRIMSON, fill_opacity=0.06)
        safe_border.set_stroke(color=CRIMSON, width=2, opacity=1)
        safe_grp = VGroup(safe_border, safe_col)
        safe_border.move_to(RIGHT * 3.0)
        safe_col.move_to(RIGHT * 3.0)

        # "≠" in the middle
        neq = Text("≠", font=SERIF, color=SLATE, font_size=48)
        neq.move_to(ORIGIN)

        self.play(FadeIn(form_border), FadeIn(form_col), run_time=0.6)
        self.play(FadeIn(safe_border), FadeIn(safe_col), run_time=0.6)
        self.play(FadeIn(neq, scale=1.2), run_time=0.5)
        self.wait(max(0.3, total - 1.7))


class B08_KeyClaim(Scene):
    def construct(self):
        _quote_scene(
            self,
            '"Remove duplicates" can be grammatically perfect '
            "and organizationally catastrophic. The format cannot tell you.",
            "— the mechanism",
            None,
            "cannot",
            DUR["B08"],
        )


class B09_MissingStep(Scene):
    def construct(self):
        total = DUR["B09"]
        steps_before = [
            "1. Inventory",
            "2. Identify duplicates",
            "3. Naming convention",
        ]
        steps_after = [
            "4. Apply convention",
            "5. Remove duplicates",
            "6. Manifest",
        ]

        before_texts = VGroup(*[
            Text(s, font=MONO, color=TEAL, font_size=24)
            for s in steps_before
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        after_texts = VGroup(*[
            Text(s, font=MONO, color=TEAL, font_size=24)
            for s in steps_after
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        gap_box = Rectangle(width=3.6, height=0.55, color=CRIMSON, fill_opacity=0.12)
        gap_box.set_stroke(color=CRIMSON, width=2, opacity=1)
        gap_label = Text("← BACKUP + DRY RUN missing", font=MONO, color=CRIMSON, font_size=18)
        gap_label.next_to(gap_box, RIGHT, buff=0.25)
        gap_grp = VGroup(gap_box, gap_label)

        all_col = VGroup(before_texts, gap_grp, after_texts).arrange(DOWN, buff=0.22)
        all_col.move_to(LEFT * 0.8)

        header = Text("THE PLAN", font=DISPLAY, color=SLATE, font_size=18)
        header.next_to(all_col, UP, buff=0.35)

        self.play(FadeIn(header), FadeIn(before_texts), FadeIn(after_texts), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(gap_box, scale=1.05), run_time=0.5)
        self.play(FadeIn(gap_label, shift=LEFT * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 2.0))


class B11_Example(Scene):
    def construct(self):
        total = DUR["B11"]

        step5 = Text("5. Remove duplicates and outdated drafts", font=MONO, color=TEAL, font_size=22)
        step5.move_to(UP * 2.2)

        arrow = Arrow(step5.get_bottom() + DOWN * 0.05,
                      step5.get_bottom() + DOWN * 0.7,
                      buff=0, color=SLATE, stroke_width=2)

        deleted_header = Text("deleted:", font=DISPLAY, color=CRIMSON, font_size=20)
        file1 = Text("report-final.docx", font=MONO, color=SLATE, font_size=20)
        file2 = Text("notes-draft-2.txt", font=MONO, color=SLATE, font_size=20)
        file3 = Text("grant-application-v1.docx", font=MONO, color=CRIMSON, font_size=22, weight=BOLD)
        file3_note = Text("← earlier version, not a duplicate", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
        file3_row = VGroup(file3, file3_note).arrange(RIGHT, buff=0.2)

        file_list = VGroup(deleted_header, file1, file2, file3_row).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        file_list.move_to(DOWN * 0.4)

        illus = Text("illustrative", font=MONO, color=SLATE, font_size=16, slant=ITALIC)
        illus.to_corner(DR, buff=0.35)

        self.play(FadeIn(step5, shift=DOWN * 0.1), run_time=0.5)
        self.play(Create(arrow), run_time=0.4)
        self.play(FadeIn(deleted_header), FadeIn(file1), FadeIn(file2), run_time=0.5)
        self.play(FadeIn(file3_row, shift=UP * 0.05), run_time=0.6)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.3, total - 2.3))


class B12_StepFive(Scene):
    def construct(self):
        total = DUR["B12"]
        steps = [
            ("1. Inventory", TEAL),
            ("2. Identify duplicates", TEAL),
            ("3. Naming convention", TEAL),
            ("4. Apply convention", TEAL),
            ("5. Remove duplicates", CRIMSON),
            ("6. Manifest", TEAL),
        ]
        step_texts = VGroup(*[
            Text(label, font=MONO, color=color, font_size=26)
            for label, color in steps
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.28).move_to(LEFT * 1.0)

        cannot_label = Text("cannot be undone", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        cannot_label.next_to(step_texts[4], RIGHT, buff=0.35)

        header = Text("THE PLAN", font=DISPLAY, color=SLATE, font_size=20)
        header.next_to(step_texts, UP, buff=0.4)

        self.play(FadeIn(header), FadeIn(step_texts), run_time=0.7)
        self.wait(0.4)
        self.play(FadeIn(cannot_label, shift=LEFT * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 1.7))


class B13_Quote(Scene):
    def construct(self):
        _quote_scene(
            self,
            "A coherent plan is not a safe plan. The format does not know the difference.",
            "— the example",
            None,
            "safe",
            DUR["B13"],
        )


class B14_Endcard(Scene):
    def construct(self):
        total = DUR["B14"]
        copy = Text("A coherent plan is not a safe plan.", font=SERIF, color=INK, font_size=34, weight=BOLD)
        sub = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        u = Line(copy.get_corner(DL) + DOWN * 0.14, copy.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        block = VGroup(copy, u).move_to(UP * 0.15)
        sub.next_to(block, DOWN, buff=0.5)
        self.play(FadeIn(copy, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.4))
