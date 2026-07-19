import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# vox-fluency-trap — Why a Polished Output Is Not Evidence the Work Is Correct
# AGENTIC AI · ~150s · 9 beats
# Color law: TEAL = verified/correct; CRIMSON = unverified/wrong/broken

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B02_BrokenCitations(Scene):
    """Three citation lines: each starts TEAL then snaps to CRIMSON with failure label."""

    def construct(self):
        # Summary doc label
        doc_lbl = Text("SUMMARY", font=DISPLAY, color=INK, font_size=28, weight="BOLD")
        doc_box = Rectangle(width=3.0, height=3.5)
        doc_box.set_fill(TEAL, 0.1).set_stroke(TEAL, 2)
        doc_lbl.move_to(doc_box.get_top() + DOWN * 0.4)
        doc = VGroup(doc_box, doc_lbl).move_to(LEFT * 4.5)

        # Citation anchors on the doc
        cit_anchors = [
            doc_box.get_center() + UP * 0.8,
            doc_box.get_center() + ORIGIN,
            doc_box.get_center() + DOWN * 0.8,
        ]

        # Source icons (right side)
        source_labels = ["Source 1", "Source 2", "Source 3"]
        sources = VGroup()
        for i, name in enumerate(source_labels):
            lbl = Text(name, font=SERIF, color=INK, font_size=22)
            box = Rectangle(width=2.0, height=0.8)
            box.set_fill(TEAL, 0.15).set_stroke(TEAL, 1.5)
            lbl.move_to(box)
            src = VGroup(box, lbl)
            src.move_to(RIGHT * 4.0 + UP * (0.8 - i * 1.4))
            sources.add(src)

        # Connection lines (start TEAL)
        lines = VGroup(*[
            Line(cit_anchors[i], sources[i].get_left(), stroke_width=2, color=TEAL)
            for i in range(3)
        ])

        # Failure labels
        failures = ["does not exist", "says opposite", "wrong domain"]
        fail_lbl_colors = [CRIMSON, CRIMSON, CRIMSON]

        self.play(FadeIn(doc, shift=RIGHT * 0.3), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(s, shift=LEFT * 0.2) for s in sources],
                               lag_ratio=0.2, run_time=1.0))
        self.play(LaggedStart(*[Create(l) for l in lines],
                               lag_ratio=0.2, run_time=0.9))

        # Snap each line to CRIMSON with failure label
        for i, (line, fail) in enumerate(zip(lines, failures)):
            fail_chip = LabelChip(fail, accent=CRIMSON, size=18)
            fail_chip.next_to(line.get_center(), UP, buff=0.15)
            self.play(line.animate.set_color(CRIMSON), run_time=0.4)
            self.play(sources[i][0].animate.set_stroke(CRIMSON, 2), run_time=0.3)
            self.play(FadeIn(fail_chip, shift=DOWN * 0.1), run_time=0.4)
            self.wait(0.4)

        self.wait(5.0)


class B04_TrainingObjective(Scene):
    """Two bars: FLUENCY (tall, TEAL) vs ACCURACY (shorter, CRIMSON with question mark)."""

    def construct(self):
        # X-axis
        x_axis = Line(LEFT * 3.0, RIGHT * 3.0, stroke_width=2, color=SLATE)
        x_axis.move_to(DOWN * 2.5)

        # FLUENCY bar (tall, TEAL)
        fluency_height = 3.8
        fluency_bar = Rectangle(width=2.0, height=fluency_height)
        fluency_bar.set_fill(TEAL, 0.5).set_stroke(TEAL, 2)
        fluency_bar.move_to(LEFT * 2.0 + DOWN * (2.5 - fluency_height / 2))

        fluency_lbl = Text("FLUENCY", font=DISPLAY, color=INK, font_size=24, weight="BOLD")
        fluency_lbl.next_to(fluency_bar, DOWN, buff=0.2)

        # Training objective arrow
        obj_arrow = Arrow(LEFT * 2.0 + UP * 2.5, LEFT * 2.0 + UP * 1.5,
                          buff=0, stroke_width=2, color=TEAL,
                          max_tip_length_to_length_ratio=0.3)
        obj_lbl = Text("training objective", font=SERIF, color=TEAL, font_size=20, slant=ITALIC)
        obj_lbl.next_to(obj_arrow, LEFT, buff=0.2)

        # ACCURACY bar (shorter, CRIMSON)
        accuracy_height = 1.8
        accuracy_bar = Rectangle(width=2.0, height=accuracy_height)
        accuracy_bar.set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2)
        accuracy_bar.move_to(RIGHT * 2.0 + DOWN * (2.5 - accuracy_height / 2))

        accuracy_lbl = Text("ACCURACY", font=DISPLAY, color=INK, font_size=24, weight="BOLD")
        accuracy_lbl.next_to(accuracy_bar, DOWN, buff=0.2)

        q_mark = Text("?", font=SERIF, color=CRIMSON, font_size=48)
        q_mark.move_to(accuracy_bar.get_center())

        self.play(Create(x_axis), run_time=0.4)
        self.play(GrowFromEdge(fluency_bar, DOWN), run_time=0.8)
        self.play(FadeIn(fluency_lbl, shift=UP * 0.1), run_time=0.3)
        self.play(Create(obj_arrow), FadeIn(obj_lbl, shift=RIGHT * 0.1), run_time=0.5)
        self.play(GrowFromEdge(accuracy_bar, DOWN), run_time=0.7)
        self.play(FadeIn(accuracy_lbl, shift=UP * 0.1),
                  FadeIn(q_mark, scale=0.8), run_time=0.5)
        self.wait(7.5)


class B06_ReportVsEvidence(Scene):
    """Two columns: AGENT REPORT (clipboard) vs EVIDENCE (source PDF), arrow blocked."""

    def construct(self):
        # Left: AGENT REPORT
        report_hdr = Text("AGENT REPORT", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        report_hdr.move_to(LEFT * 3.5 + UP * 2.5)

        report_box = Rectangle(width=3.2, height=2.0)
        report_box.set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        report_box.next_to(report_hdr, DOWN, buff=0.3)
        report_text = Text("verified sources", font=SERIF, color=TEAL, font_size=22, slant=ITALIC)
        report_text.move_to(report_box)
        report_widget = VGroup(report_box, report_text)

        # Right: SOURCE PDF
        source_hdr = Text("EVIDENCE", font=DISPLAY, color=INK, font_size=26, weight="BOLD")
        source_hdr.move_to(RIGHT * 3.5 + UP * 2.5)

        source_box = Rectangle(width=3.2, height=2.0)
        source_box.set_fill(CRIMSON, 0.12).set_stroke(CRIMSON, 2)
        source_box.next_to(source_hdr, DOWN, buff=0.3)
        source_text = Text("source PDF", font=SERIF, color=CRIMSON, font_size=22, slant=ITALIC)
        source_text.move_to(source_box)
        source_widget = VGroup(source_box, source_text)

        # Blocked arrow
        arrow = Arrow(report_widget.get_right(), source_widget.get_left(),
                      buff=0.15, stroke_width=2, color=SLATE,
                      max_tip_length_to_length_ratio=0.15)

        x_block = Text("X", font=DISPLAY, color=CRIMSON, font_size=42, weight="BOLD")
        x_block.move_to(ORIGIN + UP * 0.3)

        # Divider
        divider = Line(UP * 3.5, DOWN * 2.0, stroke_width=1.5, color=SLATE)
        divider.move_to(ORIGIN)

        note_lbl = SerifLabel("not the same thing", accent=CRIMSON, size=22)
        note_lbl.move_to(DOWN * 2.2)

        self.play(FadeIn(report_hdr, shift=UP * 0.2),
                  FadeIn(source_hdr, shift=UP * 0.2),
                  Create(divider), run_time=0.6)
        self.play(FadeIn(report_widget, shift=DOWN * 0.2), run_time=0.5)
        self.play(FadeIn(source_widget, shift=DOWN * 0.2), run_time=0.5)
        self.play(Create(arrow), run_time=0.5)
        self.play(FadeIn(x_block, scale=1.3), run_time=0.4)
        self.play(FadeIn(note_lbl, shift=UP * 0.1), run_time=0.4)
        self.wait(7.5)


class B07_CarlosExample(Scene):
    """5 report icons: 2 TEAL (read), 3 CRIMSON (locked); claim 2 marked wrong."""

    def construct(self):
        hdr = Text("Carlos: 5 cited reports", font=DISPLAY, color=INK, font_size=28)
        hdr.to_edge(UP, buff=0.8)

        # Five report icons
        icons = VGroup()
        labels = ["Report 1", "Report 2", "Report 3", "Report 4", "Report 5"]
        sub_labels = ["read", "read", "locked", "locked", "locked"]
        for i, (name, sub) in enumerate(zip(labels, sub_labels)):
            color = TEAL if i < 2 else CRIMSON
            box = Rectangle(width=1.8, height=1.0)
            box.set_fill(color, 0.25).set_stroke(color, 2)
            lbl = Text(name, font=SERIF, color=INK, font_size=18)
            lbl.move_to(box.get_center() + UP * 0.12)
            sub_lbl = Text(sub, font=SERIF, color=color, font_size=14, slant=ITALIC)
            sub_lbl.move_to(box.get_center() + DOWN * 0.2)
            icons.add(VGroup(box, lbl, sub_lbl))

        icons.arrange(RIGHT, buff=0.25).next_to(hdr, DOWN, buff=0.5)

        # Brief with 5 citations below
        brief_box = Rectangle(width=9.0, height=1.2)
        brief_box.set_fill(SLATE, 0.08).set_stroke(SLATE, 1.5)
        brief_lbl = Text("policy brief: 5 claims, 5 citations", font=SERIF, color=INK, font_size=20)
        brief_lbl.move_to(brief_box)
        brief_widget = VGroup(brief_box, brief_lbl)
        brief_widget.next_to(icons, DOWN, buff=0.6)

        # Claim 2 marker
        wrong_marker = LabelChip("claim 2: says opposite", accent=CRIMSON, size=18)
        wrong_marker.next_to(brief_widget, DOWN, buff=0.3)

        self.play(FadeIn(hdr, shift=DOWN * 0.2), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(ic, scale=0.85) for ic in icons[:2]],
                               lag_ratio=0.2, run_time=0.8))
        self.play(LaggedStart(*[FadeIn(ic, scale=0.85) for ic in icons[2:]],
                               lag_ratio=0.2, run_time=0.8))
        self.play(FadeIn(brief_widget, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(wrong_marker, scale=1.1), run_time=0.5)
        self.wait(5.5)


class B08_SourceCheck(Scene):
    """Two-step: brief claim -> arrow 'open the document' -> source PDF -> check result."""

    def construct(self):
        # Step 1: claim box
        step1_lbl = Text("STEP 1", font=DISPLAY, color=SLATE, font_size=20, weight="BOLD")
        step1_lbl.move_to(LEFT * 4.5 + UP * 2.0)

        claim_box = Rectangle(width=3.5, height=1.5)
        claim_box.set_fill(SLATE, 0.1).set_stroke(SLATE, 1.5)
        claim_text = Text("brief claim\n+ citation", font=SERIF, color=INK, font_size=22)
        claim_text.move_to(claim_box)
        claim_widget = VGroup(claim_box, claim_text)
        claim_widget.next_to(step1_lbl, DOWN, buff=0.3)

        # Arrow with label
        open_arrow = Arrow(claim_widget.get_right(), claim_widget.get_right() + RIGHT * 2.8,
                           buff=0.1, stroke_width=2, color=TEAL,
                           max_tip_length_to_length_ratio=0.15)
        open_lbl = Text("open the document", font=SERIF, color=TEAL, font_size=18, slant=ITALIC)
        open_lbl.next_to(open_arrow, UP, buff=0.1)

        # Step 2: source box
        step2_lbl = Text("STEP 2", font=DISPLAY, color=SLATE, font_size=20, weight="BOLD")
        step2_lbl.move_to(RIGHT * 3.5 + UP * 2.0)

        source_box = Rectangle(width=3.5, height=1.5)
        source_box.set_fill(TEAL, 0.12).set_stroke(TEAL, 2)
        source_text = Text("source PDF\n(find the passage)", font=SERIF, color=INK, font_size=22)
        source_text.move_to(source_box)
        source_widget = VGroup(source_box, source_text)
        source_widget.next_to(step2_lbl, DOWN, buff=0.3)

        # Result: TEAL check or CRIMSON mark
        result_lbl = SerifLabel("does it match? check yourself.", accent=TEAL, size=24)
        result_lbl.move_to(DOWN * 1.8)

        self.play(FadeIn(step1_lbl, shift=DOWN * 0.2), run_time=0.3)
        self.play(FadeIn(claim_widget, shift=DOWN * 0.2), run_time=0.5)
        self.play(Create(open_arrow), FadeIn(open_lbl, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(step2_lbl, shift=DOWN * 0.2), run_time=0.3)
        self.play(FadeIn(source_widget, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(result_lbl, shift=UP * 0.2), run_time=0.5)
        self.wait(5.5)
