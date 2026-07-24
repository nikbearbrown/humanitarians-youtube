import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# vox-invisible-plan — Why Approving a Plan Is Not the Same as Approving the Work
# AGENTIC AI · ~148s · 9 beats
# Color law: TEAL = visible plan/checkpoint/correction-free; CRIMSON = invisible plan/surprise/undone work

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B02_FolderDamage(Scene):
    """Folder tree with 3 items: one moves to archive (CRIMSON), one renamed (CRIMSON), one displaced (CRIMSON)."""

    def construct(self):
        # Root folder label
        root_lbl = Text("project-folder/", font=DISPLAY, color=INK, font_size=24, weight="BOLD")
        root_box = Rectangle(width=3.5, height=0.7)
        root_box.set_fill(SLATE, 0.15).set_stroke(SLATE, 2)
        root_lbl.move_to(root_box)
        root = VGroup(root_box, root_lbl)
        root.move_to(UP * 2.8 + LEFT * 3.5)

        # Three files (start neutral)
        file_names = ["client-brief.docx", "Q1-active.xlsx", "draft-final.txt"]
        files = VGroup()
        for i, name in enumerate(file_names):
            box = Rectangle(width=3.2, height=0.65)
            box.set_fill(SLATE, 0.1).set_stroke(SLATE, 1.5)
            lbl = Text(name, font=SERIF, color=INK, font_size=18)
            lbl.move_to(box)
            f = VGroup(box, lbl)
            f.move_to(UP * (1.5 - i * 1.1) + LEFT * 3.5)
            files.add(f)

        # Connector lines from root to files
        connectors = VGroup(*[
            Line(root.get_bottom(), files[i].get_top(), stroke_width=1.5, color=SLATE)
            for i in range(3)
        ])

        # Archive folder (right side)
        archive_box = Rectangle(width=3.0, height=0.7)
        archive_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        archive_lbl = Text("archive/", font=DISPLAY, color=INK, font_size=22, weight="BOLD")
        archive_lbl.move_to(archive_box)
        archive = VGroup(archive_box, archive_lbl)
        archive.move_to(UP * 0.5 + RIGHT * 3.5)

        self.play(FadeIn(root, shift=DOWN * 0.2), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c) for c in connectors],
                               lag_ratio=0.15, run_time=0.5))
        self.play(LaggedStart(*[FadeIn(f, shift=RIGHT * 0.1) for f in files],
                               lag_ratio=0.2, run_time=0.8))

        self.play(FadeIn(archive, shift=LEFT * 0.2), run_time=0.5)

        # Move Q1-active.xlsx (file[1]) to archive — show as CRIMSON
        self.play(files[1].animate.set_stroke(CRIMSON, 2), run_time=0.3)
        self.play(files[1].animate.move_to(UP * 0.5 + RIGHT * 3.5 + DOWN * 0.9), run_time=0.7)

        # Rename draft-final.txt — label changes to CRIMSON
        renamed_lbl = Text("draft-final-v2-COPY.txt", font=SERIF, color=CRIMSON, font_size=16)
        renamed_lbl.move_to(files[2].get_center())
        self.play(Transform(files[2][1], renamed_lbl), run_time=0.5)
        self.play(files[2][0].animate.set_stroke(CRIMSON, 2), run_time=0.3)

        # Move client-brief.docx to a "new-subfolder" — show as CRIMSON
        sub_box = Rectangle(width=3.0, height=0.7)
        sub_box.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 1.5)
        sub_lbl = Text("new-subfolder/", font=SERIF, color=CRIMSON, font_size=18)
        sub_lbl.move_to(sub_box)
        sub = VGroup(sub_box, sub_lbl)
        sub.move_to(DOWN * 1.8 + RIGHT * 3.5)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)
        self.play(files[0].animate.set_stroke(CRIMSON, 2), run_time=0.3)
        self.play(files[0].animate.move_to(DOWN * 1.8 + RIGHT * 3.5 + DOWN * 0.9), run_time=0.7)

        damage_lbl = SerifLabel("nothing gone — everything wrong", accent=CRIMSON, size=20)
        damage_lbl.move_to(DOWN * 3.0)
        self.play(FadeIn(damage_lbl, shift=UP * 0.1), run_time=0.5)

        self.wait(4.5)


class B04_TwoTimelines(Scene):
    """Two parallel timelines: invisible plan (CRIMSON, actions fire immediately) vs visible plan (TEAL, checkpoint before execution)."""

    def construct(self):
        # Column headers
        invis_hdr = Text("INVISIBLE PLAN", font=DISPLAY, color=CRIMSON, font_size=22, weight="BOLD")
        invis_hdr.move_to(LEFT * 3.5 + UP * 3.0)

        vis_hdr = Text("VISIBLE PLAN", font=DISPLAY, color=TEAL, font_size=22, weight="BOLD")
        vis_hdr.move_to(RIGHT * 3.0 + UP * 3.0)

        # Divider
        divider = Line(UP * 3.5, DOWN * 3.0, stroke_width=1.5, color=SLATE)

        # Left timeline: Instruction -> action -> action -> action (all CRIMSON, fast)
        left_nodes = ["Instruction", "Move files", "Archive items", "Rename docs"]
        left_colors = [SLATE, CRIMSON, CRIMSON, CRIMSON]
        left_group = VGroup()
        for i, (name, col) in enumerate(zip(left_nodes, left_colors)):
            box = Rectangle(width=2.8, height=0.6)
            box.set_fill(col, 0.15).set_stroke(col, 2)
            lbl = Text(name, font=SERIF, color=INK, font_size=17)
            lbl.move_to(box)
            node = VGroup(box, lbl)
            node.move_to(LEFT * 3.5 + UP * (2.0 - i * 1.2))
            left_group.add(node)

        left_arrows = VGroup(*[
            Arrow(left_group[i].get_bottom(), left_group[i + 1].get_top(),
                  buff=0.05, stroke_width=2, color=CRIMSON,
                  max_tip_length_to_length_ratio=0.3)
            for i in range(3)
        ])

        # Right timeline: Instruction -> PLAN CHECKPOINT (TEAL) -> action -> action
        right_labels = ["Instruction", "PLAN REVIEW", "Move files", "Archive items"]
        right_colors = [SLATE, TEAL, TEAL, TEAL]
        right_group = VGroup()
        for i, (name, col) in enumerate(zip(right_labels, right_colors)):
            box = Rectangle(width=2.8, height=0.6)
            box.set_fill(col, 0.15 if col != TEAL else 0.25).set_stroke(col, 2)
            lbl = Text(name, font=SERIF, color=INK, font_size=17)
            lbl.move_to(box)
            node = VGroup(box, lbl)
            node.move_to(RIGHT * 3.0 + UP * (2.0 - i * 1.2))
            right_group.add(node)

        right_arrows = VGroup(*[
            Arrow(right_group[i].get_bottom(), right_group[i + 1].get_top(),
                  buff=0.05, stroke_width=2, color=TEAL,
                  max_tip_length_to_length_ratio=0.3)
            for i in range(3)
        ])

        # Correction chip on right side (next to PLAN REVIEW)
        corr_chip = LabelChip("correct here — free", accent=TEAL, size=16)
        corr_chip.next_to(right_group[1], RIGHT, buff=0.2)

        self.play(FadeIn(invis_hdr, shift=DOWN * 0.1),
                  FadeIn(vis_hdr, shift=DOWN * 0.1),
                  Create(divider), run_time=0.5)

        # Build left (invisible) side
        self.play(FadeIn(left_group[0], shift=DOWN * 0.1), run_time=0.3)
        for i in range(3):
            self.play(Create(left_arrows[i]), run_time=0.3)
            self.play(FadeIn(left_group[i + 1], scale=0.9), run_time=0.3)

        # Build right (visible) side
        self.play(FadeIn(right_group[0], shift=DOWN * 0.1), run_time=0.3)
        self.play(Create(right_arrows[0]), run_time=0.3)
        self.play(FadeIn(right_group[1], scale=1.05), run_time=0.4)
        self.play(FadeIn(corr_chip, shift=LEFT * 0.1), run_time=0.4)
        for i in range(1, 3):
            self.play(Create(right_arrows[i]), run_time=0.3)
            self.play(FadeIn(right_group[i + 1], scale=0.9), run_time=0.3)

        self.wait(5.0)


class B06_PlanElements(Scene):
    """Six plan elements accumulate one by one as labeled rows."""

    def construct(self):
        hdr = Text("A REVIEWABLE PLAN", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        hdr.to_edge(UP, buff=0.7)
        self.play(FadeIn(hdr, shift=DOWN * 0.1), run_time=0.4)

        elements = [
            ("Goal", "what is the task?"),
            ("Inputs", "which files / systems?"),
            ("Steps", "in what order?"),
            ("Exclusions", "what will it not touch?"),
            ("Stop Condition", "when to pause and ask?"),
            ("Evidence", "what shows it is done?"),
        ]

        for i, (label, desc) in enumerate(elements):
            label_txt = Text(label, font=DISPLAY, color=TEAL, font_size=19, weight="BOLD")
            desc_txt = Text(desc, font=SERIF, color=INK, font_size=17)
            row = VGroup(label_txt, desc_txt)
            row.arrange(RIGHT, buff=0.4)
            bg = Rectangle(width=row.width + 0.4, height=0.55)
            bg.set_fill(TEAL, 0.12).set_stroke(TEAL, 1.5)
            bg.move_to(row)
            chip = VGroup(bg, label_txt, desc_txt)
            chip.move_to(UP * (2.0 - i * 0.78))
            self.play(FadeIn(chip, shift=RIGHT * 0.2), run_time=0.3)

        self.wait(6.0)


class B07_AishaExample(Scene):
    """Two-row compare: invisible plan (90-day rule, January file archived, CRIMSON) vs visible plan (rule shown, corrected to 365, TEAL)."""

    def construct(self):
        hdr = Text("Aisha's Q1 folder cleanup", font=DISPLAY, color=INK, font_size=26)
        hdr.to_edge(UP, buff=0.8)

        # Row labels
        invis_lbl = Text("INVISIBLE PLAN", font=DISPLAY, color=CRIMSON, font_size=18, weight="BOLD")
        invis_lbl.move_to(LEFT * 5.5 + UP * 1.2)

        vis_lbl = Text("VISIBLE PLAN", font=DISPLAY, color=TEAL, font_size=18, weight="BOLD")
        vis_lbl.move_to(LEFT * 5.5 + DOWN * 1.0)

        # Divider between rows
        row_div = Line(LEFT * 6.5, RIGHT * 6.5, stroke_width=1, color=SLATE)

        # Invisible plan row: rule box + arrow + outcome
        rule_box = Rectangle(width=2.8, height=0.8)
        rule_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        rule_txt = Text("active = 90 days", font=SERIF, color=INK, font_size=16)
        rule_txt.move_to(rule_box)
        rule_widget = VGroup(rule_box, rule_txt)
        rule_widget.move_to(UP * 1.2 + LEFT * 1.5)

        invisible_note = LabelChip("silent assumption", accent=CRIMSON, size=14)
        invisible_note.next_to(rule_widget, UP, buff=0.1)

        arrow_invis = Arrow(rule_widget.get_right(), rule_widget.get_right() + RIGHT * 2.5,
                            buff=0.1, stroke_width=2, color=CRIMSON,
                            max_tip_length_to_length_ratio=0.25)

        outcome_box = Rectangle(width=2.8, height=0.8)
        outcome_box.set_fill(CRIMSON, 0.2).set_stroke(CRIMSON, 2)
        outcome_txt = Text("Jan file archived", font=SERIF, color=INK, font_size=16)
        outcome_txt.move_to(outcome_box)
        outcome_widget = VGroup(outcome_box, outcome_txt)
        outcome_widget.next_to(arrow_invis, RIGHT, buff=0.1)

        undo_lbl = LabelChip("40 min recovery", accent=CRIMSON, size=14)
        undo_lbl.next_to(outcome_widget, DOWN, buff=0.1)

        # Visible plan row: rule shown + human edits to 365 + safe outcome
        rule_vis_box = Rectangle(width=2.8, height=0.8)
        rule_vis_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        rule_vis_txt = Text("active = 90 days?", font=SERIF, color=INK, font_size=16)
        rule_vis_txt.move_to(rule_vis_box)
        rule_vis_widget = VGroup(rule_vis_box, rule_vis_txt)
        rule_vis_widget.move_to(DOWN * 1.0 + LEFT * 1.5)

        correct_chip = LabelChip("corrected to 365", accent=TEAL, size=14)
        correct_chip.next_to(rule_vis_widget, UP, buff=0.1)

        arrow_vis = Arrow(rule_vis_widget.get_right(), rule_vis_widget.get_right() + RIGHT * 2.5,
                          buff=0.1, stroke_width=2, color=TEAL,
                          max_tip_length_to_length_ratio=0.25)

        safe_box = Rectangle(width=2.8, height=0.8)
        safe_box.set_fill(TEAL, 0.2).set_stroke(TEAL, 2)
        safe_txt = Text("Jan file kept", font=SERIF, color=INK, font_size=16)
        safe_txt.move_to(safe_box)
        safe_widget = VGroup(safe_box, safe_txt)
        safe_widget.next_to(arrow_vis, RIGHT, buff=0.1)

        ok_lbl = LabelChip("0 min recovery", accent=TEAL, size=14)
        ok_lbl.next_to(safe_widget, DOWN, buff=0.1)

        self.play(FadeIn(hdr, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(invis_lbl, shift=RIGHT * 0.1),
                  FadeIn(vis_lbl, shift=RIGHT * 0.1),
                  Create(row_div), run_time=0.5)

        # Build invisible row
        self.play(FadeIn(rule_widget, shift=RIGHT * 0.2), run_time=0.4)
        self.play(FadeIn(invisible_note, shift=DOWN * 0.1), run_time=0.3)
        self.play(Create(arrow_invis), run_time=0.4)
        self.play(FadeIn(outcome_widget, scale=0.9), run_time=0.4)
        self.play(FadeIn(undo_lbl, shift=UP * 0.1), run_time=0.3)

        # Build visible row
        self.play(FadeIn(rule_vis_widget, shift=RIGHT * 0.2), run_time=0.4)
        self.play(FadeIn(correct_chip, shift=DOWN * 0.1), run_time=0.3)
        self.play(Create(arrow_vis), run_time=0.4)
        self.play(FadeIn(safe_widget, scale=0.9), run_time=0.4)
        self.play(FadeIn(ok_lbl, shift=UP * 0.1), run_time=0.3)

        self.wait(5.0)


class B08_RequestPlan(Scene):
    """Three-step checklist building: request plan -> read scope/stop -> correct before execution."""

    def construct(self):
        hdr = Text("BEFORE THE AGENT ACTS", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        hdr.to_edge(UP, buff=0.8)

        steps = [
            ("1", "Request the plan", TEAL),
            ("2", "Read: scope boundary + stop condition", TEAL),
            ("3", "Correct before execution begins", TEAL),
        ]

        step_nodes = VGroup()
        for num, text, color in steps:
            num_circle = Circle(radius=0.28, color=color)
            num_circle.set_fill(color, 0.3).set_stroke(color, 2)
            num_txt = Text(num, font=DISPLAY, color=INK, font_size=20, weight="BOLD")
            num_txt.move_to(num_circle)
            num_widget = VGroup(num_circle, num_txt)

            step_txt = Text(text, font=SERIF, color=INK, font_size=22)
            row = VGroup(num_widget, step_txt)
            row.arrange(RIGHT, buff=0.35)
            step_nodes.add(row)

        step_nodes.arrange(DOWN, buff=0.7, aligned_edge=LEFT)
        step_nodes.move_to(ORIGIN + DOWN * 0.3)

        # Arrows between steps
        arrows = VGroup(*[
            Arrow(step_nodes[i].get_bottom() + DOWN * 0.05,
                  step_nodes[i + 1].get_top() + UP * 0.05,
                  buff=0.05, stroke_width=2, color=TEAL,
                  max_tip_length_to_length_ratio=0.25)
            for i in range(2)
        ])

        self.play(FadeIn(hdr, shift=DOWN * 0.2), run_time=0.4)
        for i, node in enumerate(step_nodes):
            self.play(FadeIn(node, shift=RIGHT * 0.2), run_time=0.5)
            if i < 2:
                self.play(Create(arrows[i]), run_time=0.3)

        self.wait(5.5)
