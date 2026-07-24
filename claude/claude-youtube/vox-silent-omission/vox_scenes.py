import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# vox-silent-omission — Why an Agent That Finishes First Can Be Worse Than One That Stops
# AGENTIC AI · ~150s · 12 beats
# Color law: TEAL = read/processed/reached; CRIMSON = unread/skipped/silent
# Note: TEAL here uses the palette TEAL token (maps to #1F6F5C in newsprint palette)


class B02_FolderTree(Scene):
    """Folder tree with read (TEAL) and unread (CRIMSON) nodes.
    The summary doc glows green 'COMPLETE' at the bottom."""

    def construct(self):
        # Root node
        root_label = Text("project/", font=DISPLAY, color=INK, font_size=28)
        root_box = SurroundingRectangle(root_label, buff=0.18, color=SLATE, fill_color=SLATE, fill_opacity=1)
        root_label.set_color(WHITE)
        root = VGroup(root_box, root_label).move_to(UP * 2.8)

        # Read files (TEAL)
        read_names = ["report_A.md", "report_B.md", "report_C.md", "brief_v1.md", "notes.md"]
        read_nodes = VGroup()
        for i, name in enumerate(read_names):
            lbl = Text(name, font=SERIF, color=INK, font_size=20)
            box = SurroundingRectangle(lbl, buff=0.12, color=TEAL, fill_color=TEAL, fill_opacity=0.25)
            node = VGroup(box, lbl)
            read_nodes.add(node)
        read_nodes.arrange(RIGHT, buff=0.3).move_to(UP * 0.8 + LEFT * 1.0)

        # Unread files in subfolder (CRIMSON)
        sub_label = Text("dissenting/", font=DISPLAY, color=INK, font_size=22)
        sub_box = SurroundingRectangle(sub_label, buff=0.15, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.2)
        sub_folder = VGroup(sub_box, sub_label).move_to(DOWN * 0.8 + RIGHT * 2.5)

        unread_names = ["dissent_1.md", "dissent_2.md", "dissent_3.md"]
        unread_nodes = VGroup()
        for name in unread_names:
            lbl = Text(name, font=SERIF, color=INK, font_size=18)
            box = SurroundingRectangle(lbl, buff=0.1, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.3)
            node = VGroup(box, lbl)
            unread_nodes.add(node)
        unread_nodes.arrange(RIGHT, buff=0.25).next_to(sub_folder, DOWN, buff=0.3)

        # Summary doc (green "COMPLETE")
        sum_lbl = Text("COMPLETE", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        sum_box = SurroundingRectangle(sum_lbl, buff=0.2, color=TEAL, fill_color=TEAL, fill_opacity=0.25)
        summary = VGroup(sum_box, sum_lbl).move_to(DOWN * 2.5 + LEFT * 2.5)

        # Lines connecting root to read nodes
        lines_to_read = VGroup(*[
            Line(root.get_bottom(), n.get_top(), stroke_width=1.5, color=SLATE)
            for n in read_nodes
        ])
        line_to_sub = Line(root.get_bottom(), sub_folder.get_top(), stroke_width=1.5, color=CRIMSON)
        line_to_summary = Line(root.get_bottom(), summary.get_top(), stroke_width=1.5, color=TEAL)

        # Build in sequence
        self.play(FadeIn(root, shift=DOWN * 0.3), run_time=0.7)
        self.play(Create(lines_to_read), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.2) for n in read_nodes],
                               lag_ratio=0.15, run_time=1.5))
        self.play(Create(line_to_sub), FadeIn(sub_folder, shift=UP * 0.2), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.15) for n in unread_nodes],
                               lag_ratio=0.2, run_time=1.2))
        self.play(Create(line_to_summary), FadeIn(summary, scale=0.9), run_time=0.8)
        # Pulse the COMPLETE to show it's "done"
        self.play(sum_box.animate.set_stroke(WHITE, 3), run_time=0.4)
        self.wait(5.0)


class B04_OperationChain(Scene):
    """Horizontal chain: READ -> SUMMARIZE -> NEXT, each filling TEAL with a check."""

    def construct(self):
        ops = ["READ", "SUMMARIZE", "NEXT"]
        boxes = VGroup()
        for op in ops:
            lbl = Text(op, font=DISPLAY, color=INK, font_size=28, weight="BOLD")
            box = RoundedRectangle(width=2.8, height=1.1, corner_radius=0.15)
            box.set_fill(SLATE, 0.15).set_stroke(SLATE, 2)
            lbl.move_to(box)
            boxes.add(VGroup(box, lbl))

        arrows = VGroup(*[
            Arrow(boxes[i].get_right(), boxes[i + 1].get_left(),
                  buff=0.05, stroke_width=2, color=SLATE,
                  max_tip_length_to_length_ratio=0.2)
            for i in range(len(boxes) - 1)
        ])
        chain = VGroup(boxes[0], arrows[0], boxes[1], arrows[1], boxes[2])
        chain.arrange(RIGHT, buff=0.2).move_to(UP * 0.5)

        # File label
        file_lbl = SerifLabel("file-01.pdf", accent=TEAL, size=24)
        file_lbl.next_to(chain, UP, buff=0.5)

        self.play(FadeIn(file_lbl, shift=DOWN * 0.2), run_time=0.5)
        self.play(FadeIn(boxes[0], shift=RIGHT * 0.2), run_time=0.4)
        self.play(Create(arrows[0]), run_time=0.3)
        self.play(FadeIn(boxes[1], shift=RIGHT * 0.2), run_time=0.4)
        self.play(Create(arrows[1]), run_time=0.3)
        self.play(FadeIn(boxes[2], shift=RIGHT * 0.2), run_time=0.4)

        # Fill each box TEAL with a check (one-call animate per box)
        for vg in boxes:
            self.play(vg[0].animate.set_fill(TEAL, 1), run_time=0.5)
        self.wait(0.5)

        # Second file
        file_lbl2 = SerifLabel("file-02.pdf", accent=TEAL, size=24)
        file_lbl2.next_to(chain, DOWN, buff=0.9)
        chain2 = chain.copy().next_to(file_lbl2, DOWN, buff=0.3)
        # reset fill for visual contrast
        for vg in chain2[::2]:
            vg[0].set_fill(SLATE, 0.15).set_stroke(SLATE, 2)

        self.play(FadeIn(file_lbl2, shift=DOWN * 0.2),
                  FadeIn(chain2, shift=DOWN * 0.2), run_time=0.6)
        for vg in chain2[::2]:
            self.play(vg[0].animate.set_fill(TEAL, 1), run_time=0.4)
        self.wait(3.0)


class B05_InvisibleFiles(Scene):
    """TEAL chain on left; CRIMSON file icons on right; dashed divider."""

    def construct(self):
        # Left: TEAL processed files — keep inside safe area (x <= 6.3)
        left_label = Text("Agent reached:", font=DISPLAY, color=INK, font_size=26)
        left_label.move_to(LEFT * 4.5 + UP * 2.5)

        teal_files = VGroup()
        labels_left = ["report_A.md", "report_B.md", "report_C.md",
                       "brief_v1.md", "notes.md"]
        for name in labels_left:
            lbl = Text(name, font=SERIF, color=INK, font_size=20)
            box = SurroundingRectangle(lbl, buff=0.12, color=TEAL,
                                       fill_color=TEAL, fill_opacity=0.3)
            teal_files.add(VGroup(box, lbl))
        teal_files.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        teal_files.next_to(left_label, DOWN, buff=0.3, aligned_edge=LEFT)

        # Center divider
        divider = DashedLine(UP * 3.2, DOWN * 3.2, color=SLATE, stroke_width=1.5)
        divider.move_to(ORIGIN)

        # Right: CRIMSON unreachable files — keep inside safe area (x <= 6.3)
        right_label = Text("Agent could not see:", font=DISPLAY, color=CRIMSON, font_size=26)
        right_label.move_to(RIGHT * 3.5 + UP * 2.5)

        reasons = ["no access", "unreadable scan", "not listed"]
        crimson_files = VGroup()
        for reason in reasons:
            lbl = Text(reason, font=SERIF, color=INK, font_size=20)
            box = SurroundingRectangle(lbl, buff=0.12, color=CRIMSON,
                                       fill_color=CRIMSON, fill_opacity=0.3)
            crimson_files.add(VGroup(box, lbl))
        crimson_files.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        crimson_files.next_to(right_label, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(FadeIn(left_label, shift=RIGHT * 0.2), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(f, shift=RIGHT * 0.15) for f in teal_files],
                               lag_ratio=0.12, run_time=1.4))
        self.play(Create(divider), run_time=0.6)
        self.play(FadeIn(right_label, shift=LEFT * 0.2), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(f, shift=LEFT * 0.15) for f in crimson_files],
                               lag_ratio=0.2, run_time=1.2))
        self.wait(5.5)


class B07_CountMismatch(Scene):
    """Two rows of squares: top 23 TEAL (report); bottom 23 TEAL + 3 CRIMSON (folder)."""

    def construct(self):
        n_read = 23
        n_unread = 3
        sq_size = 0.22
        gap = 0.07

        # Top row label
        report_lbl = SerifLabel("Report says: 23 processed", accent=TEAL, size=26)
        report_lbl.move_to(UP * 2.2 + LEFT * 0.5)

        # Top row squares (TEAL)
        top_squares = VGroup()
        for i in range(n_read):
            sq = Square(sq_size).set_fill(TEAL, 1).set_stroke(width=0)
            sq.move_to(RIGHT * (i % 12) * (sq_size + gap) + DOWN * (i // 12) * (sq_size + gap))
            top_squares.add(sq)
        top_squares.next_to(report_lbl, DOWN, buff=0.3).align_to(report_lbl, LEFT)

        # Bottom row label
        folder_lbl = SerifLabel("Folder held: 26 files", accent=CRIMSON, size=26)
        folder_lbl.next_to(top_squares, DOWN, buff=0.7).align_to(report_lbl, LEFT)

        # Bottom row squares (23 TEAL + 3 CRIMSON)
        bot_squares = VGroup()
        for i in range(n_read + n_unread):
            color = TEAL if i < n_read else CRIMSON
            sq = Square(sq_size).set_fill(color, 1).set_stroke(width=0)
            sq.move_to(RIGHT * (i % 12) * (sq_size + gap) + DOWN * (i // 12) * (sq_size + gap))
            bot_squares.add(sq)
        bot_squares.next_to(folder_lbl, DOWN, buff=0.3).align_to(folder_lbl, LEFT)

        self.play(FadeIn(report_lbl, shift=DOWN * 0.2), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(sq, scale=0.7) for sq in top_squares],
                               lag_ratio=0.02, run_time=2.0))
        self.wait(0.5)
        self.play(FadeIn(folder_lbl, shift=DOWN * 0.2), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(sq, scale=0.7) for sq in bot_squares[:n_read]],
                               lag_ratio=0.02, run_time=1.5))
        self.play(LaggedStart(*[FadeIn(sq, scale=1.2) for sq in bot_squares[n_read:]],
                               lag_ratio=0.15, run_time=0.9))
        # Label the 3 CRIMSON as absent
        absent_lbl = LabelChip("never in report", accent=CRIMSON, size=20)
        absent_lbl.next_to(bot_squares[n_read], RIGHT, buff=0.5)
        self.play(FadeIn(absent_lbl, shift=LEFT * 0.2), run_time=0.6)
        self.wait(4.5)


class B08_MayaExample(Scene):
    """Maya: 12 file icons, 9 TEAL, 3 CRIMSON; arrow to DIGEST doc."""

    def construct(self):
        # Header
        header = Text("Maya's 12 PDFs", font=DISPLAY, color=INK, font_size=30)
        header.to_edge(UP, buff=0.7)

        # 12 file icons in 4x3 grid
        icons = VGroup()
        for i in range(12):
            color = TEAL if i < 9 else CRIMSON
            icon = Square(0.5).set_fill(color, 1).set_stroke(width=0)
            icons.add(icon)
        icons.arrange_in_grid(rows=3, cols=4, buff=0.2)
        icons.next_to(header, DOWN, buff=0.5).shift(LEFT * 2.5)

        # Labels under CRIMSON icons
        scan_lbl = LabelChip("scan — unreadable", accent=CRIMSON, size=16)
        scan_lbl.next_to(icons[9:], DOWN, buff=0.3)

        # Arrow to digest
        digest_box = Rectangle(width=2.2, height=1.0)
        digest_box.set_fill(SLATE, 0.15).set_stroke(SLATE, 2)
        digest_lbl = Text("DIGEST", font=DISPLAY, color=INK, font_size=22, weight="BOLD")
        old_target = Text("old targets", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
        digest_lbl.move_to(digest_box.get_center() + UP * 0.18)
        old_target.move_to(digest_box.get_center() + DOWN * 0.2)
        digest = VGroup(digest_box, digest_lbl, old_target)
        digest.next_to(icons, RIGHT, buff=1.2).shift(UP * 0.5)

        arrow = Arrow(icons[4].get_right(), digest.get_left(), buff=0.1,
                      stroke_width=2, color=TEAL,
                      max_tip_length_to_length_ratio=0.15)

        # Q4 label on one CRIMSON icon
        q4_lbl = SerifLabel("Q4 revision", accent=CRIMSON, size=18)
        q4_lbl.next_to(icons[10], UP, buff=0.2)

        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(ic, scale=0.8) for ic in icons[:9]],
                               lag_ratio=0.05, run_time=1.2))
        self.play(LaggedStart(*[FadeIn(ic, scale=1.0) for ic in icons[9:]],
                               lag_ratio=0.1, run_time=0.7))
        self.play(FadeIn(scan_lbl, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(q4_lbl, shift=DOWN * 0.15), run_time=0.4)
        self.play(Create(arrow), FadeIn(digest, shift=LEFT * 0.2), run_time=0.8)
        self.wait(4.5)


class B09_InventoryCheck(Scene):
    """Three stacked inventory questions animate in; skipped row lights CRIMSON."""

    def construct(self):
        title = Text("Before accepting the report:", font=DISPLAY,
                     color=INK, font_size=28)
        title.to_edge(UP, buff=0.9)

        questions = [
            ("In scope:", "26", TEAL),
            ("Processed:", "23", TEAL),
            ("Skipped / failed:", "3", CRIMSON),
        ]
        rows = VGroup()
        for q_text, value, color in questions:
            q_lbl = Text(q_text, font=SERIF, color=INK, font_size=30)
            v_lbl = Text(value, font="PT Mono", color=color, font_size=38, weight="BOLD")
            row = VGroup(q_lbl, v_lbl).arrange(RIGHT, buff=0.5)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.6).move_to(ORIGIN)

        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        for i, (row, (_, _, color)) in enumerate(zip(rows, questions)):
            self.play(FadeIn(row[0], shift=RIGHT * 0.2), run_time=0.5)
            self.play(FadeIn(row[1], scale=0.8), run_time=0.4)
            if color == CRIMSON:
                # Highlight the whole row
                highlight = SurroundingRectangle(row, buff=0.2, color=CRIMSON,
                                                 fill_color=CRIMSON, fill_opacity=0.08)
                self.play(FadeIn(highlight), run_time=0.5)
            self.wait(0.3)

        gap_lbl = SerifLabel("count mismatch -- the gap exists", accent=CRIMSON, size=24)
        gap_lbl.next_to(rows, DOWN, buff=0.6)
        self.play(FadeIn(gap_lbl, shift=UP * 0.2), run_time=0.6)
        self.wait(4.0)


class B11_CrashVsSilent(Scene):
    """Two columns: CRASH (problem visible) vs SILENT OMISSION (problem invisible)."""

    def construct(self):
        # Left: CRASH column
        crash_title = Text("CRASH", font=DISPLAY, color=CRIMSON, font_size=30, weight="BOLD")
        crash_title.move_to(LEFT * 3.5 + UP * 2.0)

        crash_box = Rectangle(width=3.0, height=1.4)
        crash_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        crash_text = Text("ERROR: cannot parse\nfile-09.pdf", font=SERIF,
                          color=CRIMSON, font_size=22)
        crash_text.move_to(crash_box)
        crash_widget = VGroup(crash_box, crash_text)
        crash_widget.next_to(crash_title, DOWN, buff=0.35)

        visible_lbl = SerifLabel("problem visible", accent=TEAL, size=22)
        visible_lbl.next_to(crash_widget, DOWN, buff=0.35)

        # Right: SILENT OMISSION column
        silent_title = Text("SILENT OMISSION", font=DISPLAY, color=INK, font_size=30, weight="BOLD")
        silent_title.move_to(RIGHT * 3.0 + UP * 2.0)

        silent_box = Rectangle(width=3.0, height=1.4)
        silent_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        silent_text = Text("COMPLETE", font=DISPLAY, color=TEAL, font_size=28, weight="BOLD")
        silent_text.move_to(silent_box)
        silent_widget = VGroup(silent_box, silent_text)
        silent_widget.next_to(silent_title, DOWN, buff=0.35)

        invisible_lbl = SerifLabel("problem invisible", accent=CRIMSON, size=22)
        invisible_lbl.next_to(silent_widget, DOWN, buff=0.35)

        # Gap label below silent column
        gap_arrow = Arrow(invisible_lbl.get_bottom(),
                          invisible_lbl.get_bottom() + DOWN * 0.9,
                          buff=0.05, stroke_width=2, color=CRIMSON,
                          max_tip_length_to_length_ratio=0.2)
        gap_lbl = LabelChip("gap in brief", accent=CRIMSON, size=20)
        gap_lbl.next_to(gap_arrow, DOWN, buff=0.1)

        # Vertical divider
        divider = Line(UP * 2.8, DOWN * 3.0, stroke_width=1.5, color=SLATE)
        divider.move_to(ORIGIN)

        self.play(FadeIn(crash_title, shift=UP * 0.2), FadeIn(silent_title, shift=UP * 0.2),
                  run_time=0.6)
        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(crash_widget, shift=DOWN * 0.2), run_time=0.5)
        self.play(FadeIn(silent_widget, shift=DOWN * 0.2), run_time=0.5)
        self.play(FadeIn(visible_lbl, shift=UP * 0.15), run_time=0.4)
        self.play(FadeIn(invisible_lbl, shift=UP * 0.15), run_time=0.4)
        self.play(Create(gap_arrow), FadeIn(gap_lbl, shift=UP * 0.15), run_time=0.7)
        self.wait(5.0)
