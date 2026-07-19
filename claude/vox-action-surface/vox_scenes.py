import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# vox-action-surface — Why the Agent That Can Do More Can Go Wrong More
# AGENTIC AI · ~148s · 9 beats
# Color law: TEAL = narrow surface/safe; CRIMSON = broad surface/overreach/irreversible

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B02_DirectoryDamage(Scene):
    """Large folder square: files appear, agent label fades in, contracts stroke CRIMSON, disappear, tax highlighted TEAL."""

    def construct(self):
        # Header
        folder_hdr = Text("working-directory/", font=DISPLAY, color=INK, font_size=24, weight="BOLD")
        folder_hdr.to_edge(UP, buff=0.7)

        # Five file icons (all neutral initially)
        icon0_box = Rectangle(width=2.6, height=0.65)
        icon0_box.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
        icon0_lbl = Text("contract-alpha.pdf", font=SERIF, color=INK, font_size=16)
        icon0_lbl.move_to(icon0_box)
        icon0 = VGroup(icon0_box, icon0_lbl)
        icon0.move_to(LEFT * 2.5 + UP * 1.0)

        icon1_box = Rectangle(width=2.6, height=0.65)
        icon1_box.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
        icon1_lbl = Text("contract-beta.pdf", font=SERIF, color=INK, font_size=16)
        icon1_lbl.move_to(icon1_box)
        icon1 = VGroup(icon1_box, icon1_lbl)
        icon1.move_to(RIGHT * 0.7 + UP * 1.0)

        icon2_box = Rectangle(width=2.6, height=0.65)
        icon2_box.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
        icon2_lbl = Text("tax-return-2024.pdf", font=SERIF, color=INK, font_size=16)
        icon2_lbl.move_to(icon2_box)
        icon2 = VGroup(icon2_box, icon2_lbl)
        icon2.move_to(RIGHT * 3.9 + UP * 1.0)

        icon3_box = Rectangle(width=2.6, height=0.65)
        icon3_box.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
        icon3_lbl = Text("photo-backup/", font=SERIF, color=INK, font_size=16)
        icon3_lbl.move_to(icon3_box)
        icon3 = VGroup(icon3_box, icon3_lbl)
        icon3.move_to(LEFT * 2.5 + DOWN * 0.1)

        icon4_box = Rectangle(width=2.6, height=0.65)
        icon4_box.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
        icon4_lbl = Text("draft-notes.txt", font=SERIF, color=INK, font_size=16)
        icon4_lbl.move_to(icon4_box)
        icon4 = VGroup(icon4_box, icon4_lbl)
        icon4.move_to(RIGHT * 0.7 + DOWN * 0.1)

        self.play(FadeIn(folder_hdr, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(icon0, scale=0.9), run_time=0.3)
        self.play(FadeIn(icon1, scale=0.9), run_time=0.3)
        self.play(FadeIn(icon2, scale=0.9), run_time=0.3)
        self.play(FadeIn(icon3, scale=0.9), FadeIn(icon4, scale=0.9), run_time=0.4)

        # Agent action label
        action_lbl = SerifLabel("agent: sorting, deleting duplicates...", accent=CRIMSON, size=18)
        action_lbl.move_to(DOWN * 1.5)
        self.play(FadeIn(action_lbl, shift=UP * 0.1), run_time=0.4)

        # Contracts turn CRIMSON then disappear
        self.play(icon0_box.animate.set_stroke(CRIMSON, 2), run_time=0.3)
        self.play(icon0_box.animate.set_fill(CRIMSON, 0.25), run_time=0.3)
        self.play(FadeOut(icon0), run_time=0.4)

        self.play(icon1_box.animate.set_stroke(CRIMSON, 2), run_time=0.3)
        self.play(icon1_box.animate.set_fill(CRIMSON, 0.25), run_time=0.3)
        self.play(FadeOut(icon1), run_time=0.4)

        # Tax return stays — TEAL highlight
        self.play(icon2_box.animate.set_stroke(TEAL, 2), run_time=0.3)
        self.play(icon2_box.animate.set_fill(TEAL, 0.35), run_time=0.3)

        # Result labels
        gone_lbl = LabelChip("contracts: gone", accent=CRIMSON, size=16)
        gone_lbl.move_to(DOWN * 2.5 + LEFT * 2.5)
        kept_lbl = LabelChip("tax return: still there", accent=TEAL, size=16)
        kept_lbl.move_to(DOWN * 2.5 + RIGHT * 2.0)

        self.play(FadeIn(gone_lbl, shift=UP * 0.1), run_time=0.4)
        self.play(FadeIn(kept_lbl, shift=UP * 0.1), run_time=0.4)

        self.wait(3.5)


class B04_SurfaceVsTask(Scene):
    """Five concentric squares represent the expanding action surface; small task box inside."""

    def construct(self):
        # Five nested squares — each one is a distinct shape with distinct size
        # This creates 5 distinct shape additions
        ring1 = Rectangle(width=3.0, height=2.0)
        ring1.set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.5)
        ring1_lbl = Text("chat only", font=SERIF, color=CRIMSON, font_size=13)

        ring2 = Rectangle(width=4.5, height=3.0)
        ring2.set_fill(CRIMSON, 0.05).set_stroke(CRIMSON, 1.5)
        ring2_lbl = Text("+ uploaded file", font=SERIF, color=CRIMSON, font_size=13)

        ring3 = Rectangle(width=6.0, height=4.0)
        ring3.set_fill(CRIMSON, 0.04).set_stroke(CRIMSON, 1.5)
        ring3_lbl = Text("+ local folder", font=SERIF, color=CRIMSON, font_size=13)

        ring4 = Rectangle(width=7.5, height=5.2)
        ring4.set_fill(CRIMSON, 0.03).set_stroke(CRIMSON, 2.0)
        ring4_lbl = Text("+ connector / API", font=SERIF, color=CRIMSON, font_size=13)

        # Surface label
        surf_lbl = Text("ACTION SURFACE", font=DISPLAY, color=CRIMSON, font_size=22, weight="BOLD")
        surf_lbl.move_to([0.0, 3.1, 0.0])

        # Task box (tiny, centered)
        task_box = Rectangle(width=2.0, height=0.7)
        task_box.set_fill(TEAL, 0.4).set_stroke(TEAL, 2)
        task_lbl = Text("task: cleanup", font=DISPLAY, color=INK, font_size=17, weight="BOLD")

        # Position labels via list coordinates
        ring1_lbl.move_to([0.0, -1.1, 0.0])
        ring2_lbl.move_to([0.0, -1.7, 0.0])
        ring3_lbl.move_to([0.0, -2.3, 0.0])
        ring4_lbl.move_to([0.0, -2.8, 0.0])
        task_lbl.move_to(task_box)

        self.play(FadeIn(surf_lbl, shift=DOWN * 0.1), run_time=0.4)
        self.play(Create(ring1), run_time=0.35)
        self.play(FadeIn(ring1_lbl, shift=UP * 0.05), run_time=0.25)
        self.play(Create(ring2), run_time=0.35)
        self.play(FadeIn(ring2_lbl, shift=UP * 0.05), run_time=0.25)
        self.play(Create(ring3), run_time=0.35)
        self.play(FadeIn(ring3_lbl, shift=UP * 0.05), run_time=0.25)
        self.play(Create(ring4), run_time=0.35)
        self.play(FadeIn(ring4_lbl, shift=UP * 0.05), run_time=0.25)
        self.play(FadeIn(task_box), FadeIn(task_lbl), run_time=0.4)

        # Mismatch label
        mismatch = SerifLabel("blast radius grows with each rung", accent=CRIMSON, size=17)
        mismatch.move_to([0.0, -3.2, 0.0])
        self.play(FadeIn(mismatch, shift=UP * 0.1), run_time=0.5)

        self.wait(4.0)


class B06_TomExample(Scene):
    """Folder tree: report folder + secrets subfolder; CRIMSON path: agent reads secrets -> session log -> Slack."""

    def construct(self):
        hdr = Text("Tom's report task", font=DISPLAY, color=INK, font_size=24)
        hdr.to_edge(UP, buff=0.7)

        # Root folder
        root_box = Rectangle(width=3.0, height=0.65)
        root_box.set_fill(SLATE, 0.15).set_stroke(SLATE, 2)
        root_lbl = Text("project-folder/", font=SERIF, color=INK, font_size=18)
        root_lbl.move_to(root_box)
        root = VGroup(root_box, root_lbl)
        root.move_to(UP * 2.0 + LEFT * 3.0)

        # Report subfolder (TEAL — intended)
        report_box = Rectangle(width=3.0, height=0.65)
        report_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 1.5)
        report_lbl = Text("reports/", font=SERIF, color=INK, font_size=17)
        report_lbl.move_to(report_box)
        report = VGroup(report_box, report_lbl)
        report.move_to(UP * 0.8 + LEFT * 3.0)

        # Secrets subfolder (CRIMSON — unintended)
        secrets_box = Rectangle(width=3.0, height=0.65)
        secrets_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 2)
        secrets_lbl = Text("secrets/ (API keys)", font=SERIF, color=INK, font_size=17)
        secrets_lbl.move_to(secrets_box)
        secrets = VGroup(secrets_box, secrets_lbl)
        secrets.move_to(DOWN * 0.4 + LEFT * 3.0)

        conn1 = Line(root.get_bottom(), report.get_top(), stroke_width=1.5, color=SLATE)
        conn2 = Line(root.get_bottom(), secrets.get_top(), stroke_width=1.5, color=CRIMSON)

        # Session log (center)
        log_box = Rectangle(width=2.5, height=0.65)
        log_box.set_fill(CRIMSON, 0.2).set_stroke(CRIMSON, 2)
        log_lbl = Text("session log", font=SERIF, color=INK, font_size=17)
        log_lbl.move_to(log_box)
        log = VGroup(log_box, log_lbl)
        log.move_to(UP * 0.2 + RIGHT * 2.0)

        # Slack (right)
        slack_box = Rectangle(width=2.2, height=0.65)
        slack_box.set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2)
        slack_lbl = Text("Slack", font=DISPLAY, color=INK, font_size=18, weight="BOLD")
        slack_lbl.move_to(slack_box)
        slack = VGroup(slack_box, slack_lbl)
        slack.move_to(UP * 0.2 + RIGHT * 5.2)

        flow_arrow1 = Arrow(secrets.get_right(), log.get_left(),
                            buff=0.1, stroke_width=2, color=CRIMSON,
                            max_tip_length_to_length_ratio=0.2)
        flow_arrow2 = Arrow(log.get_right(), slack.get_left(),
                            buff=0.1, stroke_width=2, color=CRIMSON,
                            max_tip_length_to_length_ratio=0.2)

        context_lbl = LabelChip("for context", accent=CRIMSON, size=14)
        context_lbl.next_to(flow_arrow1, UP, buff=0.1)

        self.play(FadeIn(hdr, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(root, shift=DOWN * 0.1), run_time=0.4)
        self.play(Create(conn1), FadeIn(report, shift=DOWN * 0.1), run_time=0.4)
        self.play(Create(conn2), FadeIn(secrets, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(log, shift=LEFT * 0.1), run_time=0.4)
        self.play(Create(flow_arrow1), FadeIn(context_lbl, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(slack, shift=LEFT * 0.1), run_time=0.4)
        self.play(Create(flow_arrow2), run_time=0.4)

        damage_lbl = SerifLabel("keys now in Slack", accent=CRIMSON, size=18)
        damage_lbl.move_to(DOWN * 2.0 + RIGHT * 3.5)
        self.play(FadeIn(damage_lbl, shift=UP * 0.1), run_time=0.4)

        self.wait(5.5)


class B07_NarrowSurface(Scene):
    """Two columns: broad surface (CRIMSON) vs narrow surface (TEAL); blast radius circles."""

    def construct(self):
        # Column headers
        broad_hdr = Text("BROAD SURFACE", font=DISPLAY, color=CRIMSON, font_size=20, weight="BOLD")
        broad_hdr.move_to(LEFT * 3.5 + UP * 3.2)

        narrow_hdr = Text("NARROW SURFACE", font=DISPLAY, color=TEAL, font_size=20, weight="BOLD")
        narrow_hdr.move_to(RIGHT * 3.0 + UP * 3.2)

        divider = Line(UP * 3.5, DOWN * 3.0, stroke_width=1.5, color=SLATE)

        # Broad side: large folder, big blast radius circle
        broad_folder = Rectangle(width=3.0, height=1.4)
        broad_folder.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2)
        broad_folder.move_to(LEFT * 3.5 + UP * 1.5)
        broad_folder_lbl = Text("full directory\n(all files)", font=SERIF, color=CRIMSON, font_size=17)
        broad_folder_lbl.move_to(broad_folder)

        blast_big = Circle(radius=1.5)
        blast_big.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.5)
        blast_big.move_to(LEFT * 3.5 + DOWN * 1.0)
        blast_big_lbl = Text("blast radius", font=SERIF, color=CRIMSON, font_size=14)
        blast_big_lbl.move_to(blast_big)

        # Narrow side: small working folder, small blast radius
        narrow_folder = Rectangle(width=3.0, height=1.4)
        narrow_folder.set_fill(TEAL, 0.15).set_stroke(TEAL, 2)
        narrow_folder.move_to(RIGHT * 3.0 + UP * 1.5)
        narrow_folder_lbl = Text("working-folder/\n(copies only)", font=SERIF, color=INK, font_size=17)
        narrow_folder_lbl.move_to(narrow_folder)

        blast_small = Circle(radius=0.7)
        blast_small.set_fill(TEAL, 0.15).set_stroke(TEAL, 1.5)
        blast_small.move_to(RIGHT * 3.0 + DOWN * 1.0)
        blast_small_lbl = Text("blast radius", font=SERIF, color=TEAL, font_size=14)
        blast_small_lbl.move_to(blast_small)

        self.play(FadeIn(broad_hdr, shift=DOWN * 0.1),
                  FadeIn(narrow_hdr, shift=DOWN * 0.1),
                  Create(divider), run_time=0.5)
        self.play(FadeIn(broad_folder, shift=DOWN * 0.2), FadeIn(broad_folder_lbl), run_time=0.5)
        self.play(FadeIn(narrow_folder, shift=DOWN * 0.2), FadeIn(narrow_folder_lbl), run_time=0.5)
        self.play(Create(blast_big), FadeIn(blast_big_lbl), run_time=0.6)
        self.play(Create(blast_small), FadeIn(blast_small_lbl), run_time=0.5)
        self.wait(6.5)


class B08_SurfaceChecklist(Scene):
    """Three steps appear with circles that fill in TEAL; then final note."""

    def construct(self):
        hdr = Text("BEFORE THE AGENT STARTS", font=DISPLAY, color=INK, font_size=24, weight="BOLD")
        hdr.to_edge(UP, buff=0.8)
        self.play(FadeIn(hdr, shift=DOWN * 0.2), run_time=0.4)

        # Step 1: circle appears, then text — using list coords for mock compatibility
        s1_circle = Circle(radius=0.3, color=SLATE)
        s1_circle.set_fill(SLATE, 0.2).set_stroke(SLATE, 2)
        s1_circle.move_to([-4.5, 0.8, 0.0])
        s1_num = Text("1", font=DISPLAY, color=INK, font_size=20, weight="BOLD")
        s1_num.move_to(s1_circle)
        self.play(FadeIn(s1_circle), FadeIn(s1_num), run_time=0.3)
        self.play(s1_circle.animate.set_fill(TEAL, 0.35), run_time=0.2)
        self.play(s1_circle.animate.set_stroke(TEAL, 2), run_time=0.2)
        s1_txt = Text("Name the minimum access the task requires", font=SERIF, color=INK, font_size=21)
        s1_txt.move_to([0.5, 0.8, 0.0])
        self.play(FadeIn(s1_txt, shift=RIGHT * 0.2), run_time=0.4)

        # Step 2
        s2_circle = Circle(radius=0.3, color=SLATE)
        s2_circle.set_fill(SLATE, 0.2).set_stroke(SLATE, 2)
        s2_circle.move_to([-4.5, -0.3, 0.0])
        s2_num = Text("2", font=DISPLAY, color=INK, font_size=20, weight="BOLD")
        s2_num.move_to(s2_circle)
        self.play(FadeIn(s2_circle), FadeIn(s2_num), run_time=0.3)
        self.play(s2_circle.animate.set_fill(TEAL, 0.35), run_time=0.2)
        self.play(s2_circle.animate.set_stroke(TEAL, 2), run_time=0.2)
        s2_txt = Text("Keep sensitive data outside the working scope", font=SERIF, color=INK, font_size=21)
        s2_txt.move_to([0.5, -0.3, 0.0])
        self.play(FadeIn(s2_txt, shift=RIGHT * 0.2), run_time=0.4)

        # Step 3
        s3_circle = Circle(radius=0.3, color=SLATE)
        s3_circle.set_fill(SLATE, 0.2).set_stroke(SLATE, 2)
        s3_circle.move_to([-4.5, -1.4, 0.0])
        s3_num = Text("3", font=DISPLAY, color=INK, font_size=20, weight="BOLD")
        s3_num.move_to(s3_circle)
        self.play(FadeIn(s3_circle), FadeIn(s3_num), run_time=0.3)
        self.play(s3_circle.animate.set_fill(TEAL, 0.35), run_time=0.2)
        self.play(s3_circle.animate.set_stroke(TEAL, 2), run_time=0.2)
        s3_txt = Text("If the agent errs, can it be undone?", font=SERIF, color=INK, font_size=21)
        s3_txt.move_to([0.5, -1.4, 0.0])
        self.play(FadeIn(s3_txt, shift=RIGHT * 0.2), run_time=0.4)

        # Divider line before final note
        divider = Line([-5.0, -2.3, 0.0], [5.0, -2.3, 0.0], stroke_width=1.2, color=TEAL)
        self.play(Create(divider), run_time=0.4)

        # Final note
        final_note = SerifLabel("then draw the boundary. then start.", accent=TEAL, size=20)
        final_note.move_to([0.0, -2.8, 0.0])
        self.play(FadeIn(final_note, shift=UP * 0.1), run_time=0.5)

        self.wait(4.0)
