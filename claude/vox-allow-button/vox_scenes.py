import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

# vox-allow-button — Why "Allow?" Is Not an Approval Gate
# AGENTIC AI · ~90s · 7 beats
# Color law: TEAL = functioning gate/complete information; CRIMSON = missing info/rubber stamp/no oversight

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B02_EmptyGate(Scene):
    """Sparse 'Allow?' dialog box, CRIMSON outline; three identical dialogs stack up showing 40 clicks."""

    def construct(self):
        # Three stacked dialogs suggesting repeated identical approvals
        dialogs = VGroup()
        for i in range(3):
            box = Rectangle(width=4.8, height=2.5)
            box.set_fill(GROUND, 0.9).set_stroke(CRIMSON, 2)
            title = Text("Claude wants to run a command.", font=SERIF, color=INK, font_size=18)
            title.move_to(box.get_center() + UP * 0.4)
            btn_box = Rectangle(width=1.4, height=0.5)
            btn_box.set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2)
            btn_box.move_to(box.get_center() + DOWN * 0.4)
            btn_lbl = Text("Allow?", font=DISPLAY, color=CRIMSON, font_size=20, weight="BOLD")
            btn_lbl.move_to(btn_box)
            d = VGroup(box, title, btn_box, btn_lbl)
            d.move_to(UP * (0.3 * (2 - i)) + RIGHT * (0.3 * (2 - i)))
            dialogs.add(d)

        # Counter
        counter_40 = Text("Click #40", font=DISPLAY, color=CRIMSON, font_size=28, weight="BOLD")
        counter_40.to_edge(UP, buff=0.7)

        # Missing info chips on the side
        missing_chip = LabelChip("what did it do?", accent=CRIMSON, size=18)
        missing_chip.move_to(RIGHT * 4.5 + UP * 0.5)

        zero_note = SerifLabel("zero information, every time", accent=CRIMSON, size=20)
        zero_note.to_edge(DOWN, buff=0.9)

        # Show bottom dialog first (oldest)
        self.play(FadeIn(dialogs[2], shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(dialogs[1], shift=UP * 0.2), run_time=0.35)
        self.play(FadeIn(dialogs[0], shift=UP * 0.2), run_time=0.35)
        self.play(FadeIn(counter_40, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(missing_chip, shift=LEFT * 0.1), run_time=0.4)
        self.play(FadeIn(zero_note, shift=UP * 0.1), run_time=0.4)
        self.wait(6.0)


class B04_GateFills(Scene):
    """Sparse dialog starts CRIMSON; six fields fill in one by one turning TEAL — gate transforms."""

    def construct(self):
        # Sparse dialog (CRIMSON = no info)
        sparse_box = Rectangle(width=6.5, height=4.5)
        sparse_box.set_fill(GROUND, 0.9).set_stroke(CRIMSON, 3)
        sparse_box.move_to(ORIGIN)

        sparse_txt = Text("Claude wants to run a command.", font=SERIF, color=INK, font_size=20)
        sparse_txt.move_to(ORIGIN + UP * 0.2)
        sparse_allow = Text("Allow?", font=DISPLAY, color=CRIMSON, font_size=26, weight="BOLD")
        sparse_allow.move_to(ORIGIN + DOWN * 0.6)

        self.play(FadeIn(sparse_box), FadeIn(sparse_txt), FadeIn(sparse_allow), run_time=0.5)
        self.wait(0.3)

        # Transform: stroke to TEAL as fields fill in
        self.play(sparse_box.animate.set_stroke(TEAL, 3), run_time=0.4)
        self.play(FadeOut(sparse_allow), run_time=0.3)

        # Replace heading
        gate_hdr = Text("Before this action:", font=DISPLAY, color=INK, font_size=18, weight="BOLD")
        gate_hdr.move_to(ORIGIN + UP * 2.0)
        self.play(Transform(sparse_txt, gate_hdr), run_time=0.4)

        # Field 1: Action
        action_box = Rectangle(width=5.5, height=0.48)
        action_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 1.5)
        action_box.move_to(LEFT * 0.3 + UP * 1.35)
        action_lbl = Text("Action:  delete /projects/client-alpha/archive/", font=SERIF, color=INK, font_size=14)
        action_lbl.move_to(action_box)
        self.play(FadeIn(action_box), FadeIn(action_lbl, shift=RIGHT * 0.1), run_time=0.4)

        # Field 2: Target
        target_box = Rectangle(width=5.5, height=0.48)
        target_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 1.5)
        target_box.move_to(LEFT * 0.3 + UP * 0.75)
        target_lbl = Text("Target:  14 files, last modified 2022", font=SERIF, color=INK, font_size=14)
        target_lbl.move_to(target_box)
        self.play(FadeIn(target_box), FadeIn(target_lbl, shift=RIGHT * 0.1), run_time=0.4)

        # Field 3: Reason
        reason_box = Rectangle(width=5.5, height=0.48)
        reason_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 1.5)
        reason_box.move_to(LEFT * 0.3 + UP * 0.15)
        reason_lbl = Text("Reason:  matches inactive project pattern", font=SERIF, color=INK, font_size=14)
        reason_lbl.move_to(reason_box)
        self.play(FadeIn(reason_box), FadeIn(reason_lbl, shift=RIGHT * 0.1), run_time=0.4)

        # Field 4: Risk (CRIMSON — this is the dangerous field)
        risk_box = Rectangle(width=5.5, height=0.48)
        risk_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 1.5)
        risk_box.move_to(LEFT * 0.3 + DOWN * 0.45)
        risk_lbl = Text("Risk:  permanent if no backup exists", font=SERIF, color=INK, font_size=14)
        risk_lbl.move_to(risk_box)
        self.play(FadeIn(risk_box), FadeIn(risk_lbl, shift=RIGHT * 0.1), run_time=0.4)

        # Field 5: Reversible (CRIMSON)
        rev_box = Rectangle(width=5.5, height=0.48)
        rev_box.set_fill(CRIMSON, 0.15).set_stroke(CRIMSON, 1.5)
        rev_box.move_to(LEFT * 0.3 + DOWN * 1.05)
        rev_lbl = Text("Reversible:  no — no backup currently active", font=SERIF, color=INK, font_size=14)
        rev_lbl.move_to(rev_box)
        self.play(FadeIn(rev_box), FadeIn(rev_lbl, shift=RIGHT * 0.1), run_time=0.4)

        # Field 6: Check afterward
        check_box = Rectangle(width=5.5, height=0.48)
        check_box.set_fill(TEAL, 0.15).set_stroke(TEAL, 1.5)
        check_box.move_to(LEFT * 0.3 + DOWN * 1.65)
        check_lbl = Text("Check after:  confirm file count = 0 in archive", font=SERIF, color=INK, font_size=14)
        check_lbl.move_to(check_box)
        self.play(FadeIn(check_box), FadeIn(check_lbl, shift=RIGHT * 0.1), run_time=0.4)

        self.wait(5.5)


class B06_Approval31(Scene):
    """Counter shows 31, identical sparse dialog, six functions turn CRIMSON as deleted, config connection broken."""

    def construct(self):
        # Counter at top
        counter = Text("Approval #31", font=DISPLAY, color=CRIMSON, font_size=28, weight="BOLD")
        counter.to_edge(UP, buff=0.7)

        # Sparse dialog (same as B02)
        dialog_box = Rectangle(width=4.5, height=2.2)
        dialog_box.set_fill(GROUND, 0.9).set_stroke(CRIMSON, 2)
        dialog_box.move_to(UP * 0.5 + LEFT * 2.5)

        dialog_txt = Text("Claude wants to run a command.", font=SERIF, color=INK, font_size=17)
        dialog_txt.move_to(dialog_box.get_center() + UP * 0.3)
        allow_small = Text("Allow?", font=DISPLAY, color=CRIMSON, font_size=20, weight="BOLD")
        allow_small.move_to(dialog_box.get_center() + DOWN * 0.3)
        dialog = VGroup(dialog_box, dialog_txt, allow_small)

        # Functions column (right side)
        fn_labels = ["fn_config_load()", "fn_config_read()", "fn_config_init()",
                     "fn_logger()", "fn_parser()", "fn_main()"]
        fn_group = VGroup()
        for i, name in enumerate(fn_labels):
            box = Rectangle(width=2.8, height=0.45)
            box.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.5)
            lbl = Text(name, font=MONO, color=INK, font_size=13)
            lbl.move_to(box)
            fn = VGroup(box, lbl)
            fn.move_to(RIGHT * 3.5 + UP * (1.8 - i * 0.62))
            fn_group.add(fn)

        fn_hdr = Text("functions", font=DISPLAY, color=INK, font_size=18, weight="BOLD")
        fn_hdr.next_to(fn_group, UP, buff=0.2)

        # Production config note
        prod_box = Rectangle(width=3.0, height=0.65)
        prod_box.set_fill(TEAL, 0.2).set_stroke(TEAL, 2)
        prod_lbl = Text("production config", font=SERIF, color=INK, font_size=16)
        prod_lbl.move_to(prod_box)
        prod_widget = VGroup(prod_box, prod_lbl)
        prod_widget.move_to(DOWN * 2.5 + RIGHT * 3.5)

        # Connection lines (functions -> config)
        conn_lines = VGroup(*[
            Line(fn_group[i].get_bottom(), prod_widget.get_top(), stroke_width=1.2, color=TEAL)
            for i in range(3)
        ])

        self.play(FadeIn(counter, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(dialog, scale=0.9), run_time=0.5)
        self.play(FadeIn(fn_hdr), LaggedStart(*[FadeIn(f) for f in fn_group],
                                               lag_ratio=0.1, run_time=0.8))
        self.play(FadeIn(prod_widget, shift=UP * 0.1), run_time=0.4)
        self.play(LaggedStart(*[Create(c) for c in conn_lines], lag_ratio=0.1, run_time=0.6))

        self.wait(0.5)

        # Delete first 3 functions (the ones that matter) — separate play calls per attribute
        for i in range(3):
            self.play(fn_group[i][0].animate.set_fill(CRIMSON, 0.3), run_time=0.3)
            self.play(fn_group[i][0].animate.set_stroke(CRIMSON, 2), run_time=0.2)
            self.play(conn_lines[i].animate.set_color(CRIMSON), run_time=0.2)

        # Broken connection label
        broken_lbl = LabelChip("never read by agent", accent=CRIMSON, size=16)
        broken_lbl.next_to(prod_widget, DOWN, buff=0.15)
        self.play(FadeIn(broken_lbl, shift=UP * 0.1), run_time=0.4)

        self.wait(5.0)
