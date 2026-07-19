import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B02_AgentLoop(Scene):
    """Agent reads 2 of 5 reports, generates output, self-checks — all in CRIMSON loop."""

    def construct(self):
        dur = DUR.get("B02", 14.0)

        # Five report rectangles across the top
        report_colors = [TEAL, TEAL, SLATE, SLATE, SLATE]
        report_labels = ["R1", "R2", "R3", "R4", "R5"]
        report_xs = [-4.5, -2.5, -0.5, 1.5, 3.5]

        reports = []
        for i in range(5):
            box = Rectangle(width=1.4, height=1.8)
            box.set_fill(report_colors[i], 0.25)
            box.set_stroke(report_colors[i], 2.5)
            box.move_to([report_xs[i], 2.2, 0.0])
            lbl = Text(report_labels[i], font=SANS, font_size=18, color=WHITE)
            lbl.move_to([report_xs[i], 2.2, 0.0])
            reports.append(VGroup(box, lbl))

        # Show all reports
        for r in reports:
            self.play(FadeIn(r), run_time=0.25)

        # "Read" label on first two
        read_lbl1 = Text("READ", font=SANS, font_size=13, color=TEAL)
        read_lbl1.move_to([report_xs[0], 1.1, 0.0])
        read_lbl2 = Text("READ", font=SANS, font_size=13, color=TEAL)
        read_lbl2.move_to([report_xs[1], 1.1, 0.0])
        self.play(FadeIn(read_lbl1), FadeIn(read_lbl2), run_time=0.3)

        # Skip label on last three
        skip_lbl = Text("SKIPPED", font=SANS, font_size=13, color=SLATE)
        skip_lbl.move_to([1.5, 1.1, 0.0])
        self.play(FadeIn(skip_lbl), run_time=0.3)

        # Agent box
        agent_box = Rectangle(width=2.4, height=1.0)
        agent_box.set_fill(SLATE, 0.3)
        agent_box.set_stroke(SLATE, 2)
        agent_box.move_to([-1.0, 0.0, 0.0])
        agent_lbl = Text("AGENT", font=SANS, font_size=18, color=WHITE)
        agent_lbl.move_to([-1.0, 0.0, 0.0])
        self.play(FadeIn(agent_box), FadeIn(agent_lbl), run_time=0.4)

        # Output box
        out_box = Rectangle(width=2.4, height=1.0)
        out_box.set_fill(SLATE, 0.2)
        out_box.set_stroke(SLATE, 1.5)
        out_box.move_to([2.5, 0.0, 0.0])
        out_lbl = Text("OUTPUT", font=SANS, font_size=18, color=WHITE)
        out_lbl.move_to([2.5, 0.0, 0.0])
        self.play(FadeIn(out_box), FadeIn(out_lbl), run_time=0.4)

        # Arrow agent → output
        arr1 = Line([0.2, 0.0, 0.0], [1.3, 0.0, 0.0], stroke_width=2.5, color=SLATE)
        self.play(Create(arr1), run_time=0.3)

        # Self-check arc (CRIMSON) — from output back to agent
        # Use a curved line approximated by two lines forming a V below
        sc_line1 = Line([2.5, -0.5, 0.0], [0.75, -1.5, 0.0], stroke_width=2.5, color=CRIMSON)
        sc_line2 = Line([0.75, -1.5, 0.0], [-1.0, -0.5, 0.0], stroke_width=2.5, color=CRIMSON)
        sc_lbl = Text("SELF-CHECK", font=SANS, font_size=15, color=CRIMSON)
        sc_lbl.move_to([0.75, -1.85, 0.0])

        self.play(Create(sc_line1), run_time=0.3)
        self.play(Create(sc_line2), run_time=0.3)
        self.play(FadeIn(sc_lbl), run_time=0.3)

        # "PASS" label — placed to the right of sc_line1 to avoid crossing it
        pass_lbl = Text("PASS ✓", font=SANS, font_size=20, color=CRIMSON)
        pass_lbl.move_to([3.8, -0.9, 0.0])
        self.play(FadeIn(pass_lbl), run_time=0.4)

        self.wait(max(0.1, dur - 4.5))


class B04_OverlapCircles(Scene):
    """Two overlapping CRIMSON circles (Generation + Self-Check) vs separate TEAL circle (Source)."""

    def construct(self):
        dur = DUR.get("B04", 18.0)

        # Generation circle (CRIMSON)
        gen_circle = Circle(radius=1.8)
        gen_circle.set_fill(CRIMSON, 0.18)
        gen_circle.set_stroke(CRIMSON, 2.5)
        gen_circle.move_to([-1.2, 0.4, 0.0])

        gen_lbl = Text("Generation\nContext", font=SANS, font_size=18, color=CRIMSON)
        gen_lbl.move_to([-2.2, 1.3, 0.0])

        self.play(Create(gen_circle), run_time=0.6)
        self.play(FadeIn(gen_lbl), run_time=0.3)

        # Self-check circle (CRIMSON) — overlapping
        sc_circle = Circle(radius=1.8)
        sc_circle.set_fill(CRIMSON, 0.18)
        sc_circle.set_stroke(CRIMSON, 2.5)
        sc_circle.move_to([0.8, 0.4, 0.0])

        sc_lbl = Text("Self-Check\nContext", font=SANS, font_size=18, color=CRIMSON)
        sc_lbl.move_to([1.2, 1.3, 0.0])

        self.play(Create(sc_circle), run_time=0.6)
        self.play(FadeIn(sc_lbl), run_time=0.3)

        # Overlap label
        overlap_lbl = Text("shared\nblind spots", font=SANS, font_size=14, color=WHITE)
        overlap_lbl.move_to([-0.2, 0.4, 0.0])
        self.play(FadeIn(overlap_lbl), run_time=0.3)

        # Source circle (TEAL) — far right, separate
        src_circle = Circle(radius=1.4)
        src_circle.set_fill(TEAL, 0.2)
        src_circle.set_stroke(TEAL, 2.5)
        src_circle.move_to([4.5, 0.4, 0.0])

        src_lbl = Text("Source\nDocuments", font=SANS, font_size=18, color=TEAL)
        src_lbl.move_to([4.5, 2.0, 0.0])

        self.play(Create(src_circle), run_time=0.6)
        self.play(FadeIn(src_lbl), run_time=0.3)

        # Divider line between CRIMSON group and TEAL circle
        div = Line([2.8, -2.0, 0.0], [2.8, 2.8, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(div), run_time=0.4)

        # Labels at bottom
        left_lbl = Text("same context", font=SANS, font_size=14, color=CRIMSON)
        left_lbl.move_to([-0.2, -1.8, 0.0])
        right_lbl = Text("independent reference", font=SANS, font_size=14, color=TEAL)
        right_lbl.move_to([4.5, -1.8, 0.0])

        self.play(FadeIn(left_lbl), run_time=0.3)
        self.play(FadeIn(right_lbl), run_time=0.3)

        # Accent line under TEAL circle (distinct 5th state)
        teal_underline = Line([3.2, -1.3, 0.0], [5.8, -1.3, 0.0], stroke_width=2.5, color=TEAL)
        self.play(Create(teal_underline), run_time=0.3)

        # Accent line under CRIMSON group (distinct 6th state)
        crimson_underline = Line([-3.4, -1.3, 0.0], [2.4, -1.3, 0.0], stroke_width=2.5, color=CRIMSON)
        self.play(Create(crimson_underline), run_time=0.3)

        # Small separator tick on divider (distinct 7th state)
        tick = Line([2.8, 0.6, 0.0], [2.8, 0.2, 0.0], stroke_width=3.0, color=GOLD)
        self.play(Create(tick), run_time=0.25)

        self.wait(max(0.1, dur - 6.0))


class B06_JaeExample(Scene):
    """Jae: source says 15%, agent recalls 50%, self-check passes, human opens PDF: 15%."""

    def construct(self):
        dur = DUR.get("B06", 20.0)

        # PDF source box
        pdf_box = Rectangle(width=2.0, height=2.4)
        pdf_box.set_fill(SLATE, 0.2)
        pdf_box.set_stroke(TEAL, 2.5)
        pdf_box.move_to([-4.5, 0.5, 0.0])

        pdf_lbl = Text("SOURCE\nPDF", font=SANS, font_size=15, color=TEAL)
        pdf_lbl.move_to([-4.5, 1.3, 0.0])

        # Value in source
        val_true = Text("15%", font=DISPLAY, font_size=28, color=TEAL)
        val_true.move_to([-4.5, 0.0, 0.0])

        self.play(FadeIn(pdf_box), run_time=0.4)
        self.play(FadeIn(pdf_lbl), run_time=0.3)
        # Source value starts hidden (revealed at end)

        # Agent recall box
        recall_box = Rectangle(width=2.0, height=1.2)
        recall_box.set_fill(CRIMSON, 0.15)
        recall_box.set_stroke(CRIMSON, 2)
        recall_box.move_to([-1.5, 1.0, 0.0])

        recall_lbl = Text("Agent\nRecall", font=SANS, font_size=15, color=CRIMSON)
        recall_lbl.move_to([-1.5, 1.0, 0.0])

        # Recall shows wrong value
        val_wrong1 = Text("50%", font=DISPLAY, font_size=26, color=CRIMSON)
        val_wrong1.move_to([-1.5, 0.0, 0.0])

        self.play(FadeIn(recall_box), run_time=0.4)
        self.play(FadeIn(recall_lbl), run_time=0.3)

        # Arrow: PDF → agent recall (wrong)
        arr1 = Line([-3.5, 0.5, 0.0], [-2.5, 0.8, 0.0], stroke_width=2.5, color=CRIMSON)
        self.play(Create(arr1), run_time=0.3)
        self.play(FadeIn(val_wrong1), run_time=0.3)

        # Summary box
        summ_box = Rectangle(width=2.0, height=1.2)
        summ_box.set_fill(CRIMSON, 0.15)
        summ_box.set_stroke(CRIMSON, 2)
        summ_box.move_to([1.5, 1.0, 0.0])

        summ_lbl = Text("Summary", font=SANS, font_size=15, color=CRIMSON)
        summ_lbl.move_to([1.5, 1.0, 0.0])

        val_wrong2 = Text("50%", font=DISPLAY, font_size=26, color=CRIMSON)
        val_wrong2.move_to([1.5, 0.0, 0.0])

        self.play(FadeIn(summ_box), run_time=0.4)
        self.play(FadeIn(summ_lbl), run_time=0.3)

        arr2 = Line([-0.5, 0.8, 0.0], [0.5, 0.8, 0.0], stroke_width=2.5, color=CRIMSON)
        self.play(Create(arr2), run_time=0.3)
        self.play(FadeIn(val_wrong2), run_time=0.3)

        # Self-check arc back
        sc_line1 = Line([1.5, -0.7, 0.0], [0.0, -1.6, 0.0], stroke_width=2.5, color=CRIMSON)
        sc_line2 = Line([0.0, -1.6, 0.0], [-1.5, -0.7, 0.0], stroke_width=2.5, color=CRIMSON)
        sc_lbl = Text("SELF-CHECK: MATCH ✓", font=SANS, font_size=14, color=CRIMSON)
        sc_lbl.move_to([0.0, -2.0, 0.0])

        self.play(Create(sc_line1), run_time=0.3)
        self.play(Create(sc_line2), run_time=0.3)
        self.play(FadeIn(sc_lbl), run_time=0.3)

        # Human opens PDF — reveal actual value
        reveal_box = Rectangle(width=2.2, height=1.0)
        reveal_box.set_fill(TEAL, 0.2)
        reveal_box.set_stroke(TEAL, 3)
        reveal_box.move_to([4.5, 0.5, 0.0])

        reveal_lbl = Text("PDF opened:\n15%", font=SANS, font_size=16, color=TEAL)
        reveal_lbl.move_to([4.5, 0.5, 0.0])

        self.play(FadeIn(reveal_box), run_time=0.4)
        self.play(FadeIn(reveal_lbl), run_time=0.4)

        # Show true value in source box
        self.play(FadeIn(val_true), run_time=0.4)

        self.wait(max(0.1, dur - 7.5))


class B07_TwoVerifyPaths(Scene):
    """Two columns: CRIMSON self-check loop vs TEAL independent verify."""

    def construct(self):
        dur = DUR.get("B07", 20.0)

        # Column divider
        div = Line([0.0, 3.0, 0.0], [0.0, -3.0, 0.0], stroke_width=1.5, color=SLATE)
        self.play(Create(div), run_time=0.3)

        # Left column header (CRIMSON)
        left_hdr = Text("Self-Check", font=DISPLAY, font_size=22, color=CRIMSON)
        left_hdr.move_to([-3.0, 2.7, 0.0])
        self.play(FadeIn(left_hdr), run_time=0.3)

        # Right column header (TEAL)
        right_hdr = Text("Independent Verify", font=DISPLAY, font_size=22, color=TEAL)
        right_hdr.move_to([3.0, 2.7, 0.0])
        self.play(FadeIn(right_hdr), run_time=0.3)

        # Left column: Summary → Recall → Check (loop)
        lsum = Rectangle(width=2.8, height=0.7)
        lsum.set_fill(CRIMSON, 0.15)
        lsum.set_stroke(CRIMSON, 2)
        lsum.move_to([-3.0, 1.6, 0.0])
        lsum_lbl = Text("Summary", font=SANS, font_size=16, color=WHITE)
        lsum_lbl.move_to([-3.0, 1.6, 0.0])
        self.play(FadeIn(lsum), FadeIn(lsum_lbl), run_time=0.3)

        larr1 = Line([-3.0, 1.2, 0.0], [-3.0, 0.7, 0.0], stroke_width=2, color=CRIMSON)
        self.play(Create(larr1), run_time=0.2)

        lrec = Rectangle(width=2.8, height=0.7)
        lrec.set_fill(CRIMSON, 0.15)
        lrec.set_stroke(CRIMSON, 2)
        lrec.move_to([-3.0, 0.35, 0.0])
        lrec_lbl = Text("Agent Recall", font=SANS, font_size=16, color=WHITE)
        lrec_lbl.move_to([-3.0, 0.35, 0.0])
        self.play(FadeIn(lrec), FadeIn(lrec_lbl), run_time=0.3)

        larr2 = Line([-3.0, 0.0, 0.0], [-3.0, -0.5, 0.0], stroke_width=2, color=CRIMSON)
        self.play(Create(larr2), run_time=0.2)

        lpass = Text("PASS ✓", font=SANS, font_size=18, color=CRIMSON)
        lpass.move_to([-3.0, -0.8, 0.0])
        self.play(FadeIn(lpass), run_time=0.3)

        # X mark at bottom left — still circular
        lx = Text("circular", font=SANS, font_size=14, color=CRIMSON)
        lx.move_to([-3.0, -1.5, 0.0])
        self.play(FadeIn(lx), run_time=0.3)

        # Right column: Summary → Open Source → Compare → Catch
        rsum = Rectangle(width=2.8, height=0.7)
        rsum.set_fill(TEAL, 0.15)
        rsum.set_stroke(TEAL, 2)
        rsum.move_to([3.0, 1.6, 0.0])
        rsum_lbl = Text("Summary", font=SANS, font_size=16, color=WHITE)
        rsum_lbl.move_to([3.0, 1.6, 0.0])
        self.play(FadeIn(rsum), FadeIn(rsum_lbl), run_time=0.3)

        rarr1 = Line([3.0, 1.2, 0.0], [3.0, 0.7, 0.0], stroke_width=2, color=TEAL)
        self.play(Create(rarr1), run_time=0.2)

        rsrc = Rectangle(width=2.8, height=0.7)
        rsrc.set_fill(TEAL, 0.15)
        rsrc.set_stroke(TEAL, 2)
        rsrc.move_to([3.0, 0.35, 0.0])
        rsrc_lbl = Text("Open Source PDF", font=SANS, font_size=14, color=WHITE)
        rsrc_lbl.move_to([3.0, 0.35, 0.0])
        self.play(FadeIn(rsrc), FadeIn(rsrc_lbl), run_time=0.3)

        rarr2 = Line([3.0, 0.0, 0.0], [3.0, -0.5, 0.0], stroke_width=2, color=TEAL)
        self.play(Create(rarr2), run_time=0.2)

        rcatch = Text("CATCHES ERROR ✓", font=SANS, font_size=16, color=TEAL)
        rcatch.move_to([3.0, -0.8, 0.0])
        self.play(FadeIn(rcatch), run_time=0.3)

        rindep = Text("independent", font=SANS, font_size=14, color=TEAL)
        rindep.move_to([3.0, -1.5, 0.0])
        self.play(FadeIn(rindep), run_time=0.3)

        self.wait(max(0.1, dur - 6.5))


class B08_VerifyChecklist(Scene):
    """Three TEAL checklist chips appear sequentially."""

    def construct(self):
        dur = DUR.get("B08", 18.0)

        # Title
        title = Text("After any agent task:", font=DISPLAY, font_size=24, color=TEAL)
        title.move_to([0.0, 2.8, 0.0])
        self.play(FadeIn(title), run_time=0.4)

        steps = [
            ("1", "Open cited sources"),
            ("2", "Find the exact claim"),
            ("3", "Compare to source text"),
        ]

        chip_ys = [1.3, 0.1, -1.1]

        for i, (num, text) in enumerate(steps):
            y = chip_ys[i]

            # Number circle
            num_circle = Circle(radius=0.38)
            num_circle.set_fill(TEAL, 0.35)
            num_circle.set_stroke(TEAL, 2)
            num_circle.move_to([-4.0, y, 0.0])

            num_lbl = Text(num, font=DISPLAY, font_size=22, color=WHITE)
            num_lbl.move_to([-4.0, y, 0.0])

            # Chip box
            chip_box = Rectangle(width=7.0, height=0.75)
            chip_box.set_fill(TEAL, 0.12)
            chip_box.set_stroke(TEAL, 1.5)
            chip_box.move_to([0.5, y, 0.0])

            step_lbl = Text(text, font=SANS, font_size=20, color=WHITE)
            step_lbl.move_to([0.5, y, 0.0])

            self.play(FadeIn(num_circle), FadeIn(num_lbl), run_time=0.3)
            self.play(FadeIn(chip_box), FadeIn(step_lbl), run_time=0.35)

        # Separator line
        sep = Line([-5.5, -2.0, 0.0], [5.5, -2.0, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(sep), run_time=0.3)

        # Final note
        note = Text("A passing self-check is not evidence the work is correct.", font=SANS, font_size=16, color=SLATE)
        note.move_to([0.0, -2.6, 0.0])
        self.play(FadeIn(note), run_time=0.4)

        self.wait(max(0.1, dur - 4.5))
