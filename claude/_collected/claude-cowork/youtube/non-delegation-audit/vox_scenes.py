import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_DelegationTree(Scene):
    def construct(self):
        total = DUR.get("B04", 20.0)

        # State 1: Title appears
        title = Text("NON-DELEGATION CLASSIFIER", font=DISPLAY, color=INK,
                     font_size=30, weight=BOLD)
        title.move_to(UP * 3.2)
        self.play(Write(title), run_time=0.6)

        # State 2: Four test boxes appear in a column (centered, no task labels)
        test_labels = ["REGULATED?", "IRREVERSIBLE?", "RELATIONSHIP?", "VERIFIABLE?"]
        test_y = [1.8, 0.9, 0.0, -0.9]
        test_boxes = VGroup()
        test_texts = VGroup()
        for label, y in zip(test_labels, test_y):
            box = Rectangle(width=3.5, height=0.6)
            box.set_stroke(color=INK, width=2, opacity=1)
            box.set_fill(opacity=0)
            box.move_to(UP * y)
            txt = Text(label, font=DISPLAY, color=INK, font_size=20, weight=BOLD)
            txt.move_to(box.get_center())
            test_boxes.add(box)
            test_texts.add(txt)

        self.play(Create(test_boxes), Write(test_texts), run_time=0.8)

        # State 3: Outcome boxes appear (left and right)
        dont_box = Rectangle(width=2.8, height=0.9)
        dont_box.set_stroke(color=CRIMSON, width=2, opacity=1)
        dont_box.set_fill(color=CRIMSON, opacity=0.15)
        dont_box.move_to(RIGHT * 5.0 + UP * 0.5)
        dont_txt = Text("DO NOT\nDELEGATE", font=DISPLAY, color=CRIMSON,
                        font_size=18, weight=BOLD)
        dont_txt.move_to(dont_box.get_center())

        delegate_box = Rectangle(width=2.8, height=0.9)
        delegate_box.set_stroke(color=INK, width=2, opacity=1)
        delegate_box.set_fill(color=CREAM, opacity=0.9)
        delegate_box.move_to(LEFT * 5.0 + UP * 0.5)
        delegate_txt = Text("DELEGATE", font=DISPLAY, color=INK,
                            font_size=20, weight=BOLD)
        delegate_txt.move_to(delegate_box.get_center())

        self.play(Create(dont_box), Write(dont_txt),
                  Create(delegate_box), Write(delegate_txt), run_time=0.7)

        # State 4: REGULATED? fails → crimson highlight + routing arrow to DO NOT DELEGATE
        crimson_reg = Rectangle(width=3.5, height=0.6)
        crimson_reg.set_stroke(color=CRIMSON, width=2, opacity=1)
        crimson_reg.set_fill(color=CRIMSON, opacity=0.25)
        crimson_reg.move_to(UP * 1.8)

        route1 = Line(test_boxes[0].get_right(), dont_box.get_left() + UP * 0.15,
                      color=CRIMSON, stroke_width=2)
        route1.set_stroke(opacity=1)

        # YES label well below line path, with cream background
        yes1_bg = Rectangle(width=0.6, height=0.3, stroke_width=0, stroke_opacity=0)
        yes1_bg.set_fill(color=CREAM, opacity=1)
        yes1_txt = Text("YES", font=DISPLAY, color=CRIMSON, font_size=15, weight=BOLD)
        yes1_grp = VGroup(yes1_bg, yes1_txt)
        yes1_grp.move_to(UP * 1.2 + RIGHT * 2.5)

        self.play(Create(crimson_reg), Create(route1), FadeIn(yes1_grp), run_time=0.5)

        # State 5: VERIFIABLE? passes → route to DELEGATE (task passes all 4 tests)
        route2 = Line(test_boxes[3].get_left(), delegate_box.get_right() + DOWN * 0.15,
                      color=INK, stroke_width=2)
        route2.set_stroke(opacity=0.7)

        # ALL NO label — placed at DOWN * -2.0 area, well away from lines
        no_bg = Rectangle(width=1.2, height=0.32, stroke_width=0, stroke_opacity=0)
        no_bg.set_fill(color=CREAM, opacity=1)
        no_txt = Text("ALL NO", font=DISPLAY, color=INK, font_size=14)
        no_grp = VGroup(no_bg, no_txt)
        no_grp.move_to(DOWN * 2.0 + LEFT * 3.0)

        self.play(Create(route2), FadeIn(no_grp), run_time=0.5)

        # State 6: IRREVERSIBLE? fails → crimson highlight + second routing arrow
        crimson_irr = Rectangle(width=3.5, height=0.6)
        crimson_irr.set_stroke(color=CRIMSON, width=2, opacity=1)
        crimson_irr.set_fill(color=CRIMSON, opacity=0.25)
        crimson_irr.move_to(UP * 0.9)

        route3 = Line(test_boxes[1].get_right(), dont_box.get_left() + DOWN * 0.15,
                      color=CRIMSON, stroke_width=2)
        route3.set_stroke(opacity=1)

        irr_bg = Rectangle(width=1.8, height=0.32, stroke_width=0, stroke_opacity=0)
        irr_bg.set_fill(color=CREAM, opacity=1)
        irr_txt = Text("IRREVERSIBLE", font=DISPLAY, color=CRIMSON, font_size=14, weight=BOLD)
        irr_grp = VGroup(irr_bg, irr_txt)
        irr_grp.move_to(DOWN * 2.0 + RIGHT * 2.5)

        self.play(Create(crimson_irr), Create(route3), FadeIn(irr_grp), run_time=0.5)

        # State 7: Tally — shown in bottom center
        tally_bg = Rectangle(width=5.5, height=0.45, stroke_width=0, stroke_opacity=0)
        tally_bg.set_fill(color=CREAM, opacity=1)
        tally_txt = Text("2 → DO NOT DELEGATE   ·   3 → DELEGATE",
                         font=MONO, color=INK, font_size=16)
        tally_grp = VGroup(tally_bg, tally_txt)
        tally_grp.move_to(DOWN * 2.8)
        self.play(FadeIn(tally_grp, shift=UP * 0.1), run_time=0.4)

        self.wait(max(0.5, total - 5.0))


class B06_DelegationTreeFive(Scene):
    def construct(self):
        total = DUR.get("B06", 14.0)

        # State 1: Title
        title = Text("NON-DELEGATION CLASSIFIER — 5 TESTS", font=DISPLAY, color=INK,
                     font_size=26, weight=BOLD)
        title.move_to(UP * 3.2)
        self.play(Write(title), run_time=0.5)

        # State 2: Five test boxes in a column
        test_labels = ["REGULATED?", "IRREVERSIBLE?", "RELATIONSHIP?", "VERIFIABLE?", "GROUND TRUTH?"]
        test_y = [2.0, 1.2, 0.4, -0.4, -1.2]
        test_boxes = VGroup()
        test_texts = VGroup()
        for label, y in zip(test_labels, test_y):
            box = Rectangle(width=3.5, height=0.55)
            box.set_stroke(color=INK, width=2, opacity=1)
            box.set_fill(opacity=0)
            box.move_to(UP * y)
            txt = Text(label, font=DISPLAY, color=INK, font_size=18, weight=BOLD)
            txt.move_to(box.get_center())
            test_boxes.add(box)
            test_texts.add(txt)

        self.play(Create(test_boxes), Write(test_texts), run_time=0.8)

        # State 3: Outcome boxes
        dont_box = Rectangle(width=2.8, height=0.8)
        dont_box.set_stroke(color=CRIMSON, width=2, opacity=1)
        dont_box.set_fill(color=CRIMSON, opacity=0.15)
        dont_box.move_to(RIGHT * 5.0 + UP * 0.4)
        dont_txt = Text("DO NOT\nDELEGATE", font=DISPLAY, color=CRIMSON,
                        font_size=16, weight=BOLD)
        dont_txt.move_to(dont_box.get_center())

        delegate_box = Rectangle(width=2.8, height=0.8)
        delegate_box.set_stroke(color=INK, width=2, opacity=1)
        delegate_box.set_fill(color=CREAM, opacity=0.9)
        delegate_box.move_to(LEFT * 5.0 + UP * 0.4)
        delegate_txt = Text("DELEGATE", font=DISPLAY, color=INK,
                            font_size=18, weight=BOLD)
        delegate_txt.move_to(delegate_box.get_center())

        self.play(Create(dont_box), Write(dont_txt),
                  Create(delegate_box), Write(delegate_txt), run_time=0.6)

        # State 4: Borderline task — show it passing first 4 tests via NO markers inside boxes
        # Small "NO" badges placed well inside each of the first 4 test boxes
        no_badges = VGroup()
        for i in range(4):
            badge_bg = Rectangle(width=0.45, height=0.28, stroke_width=0, stroke_opacity=0)
            badge_bg.set_fill(color=INK, opacity=0.1)
            badge_txt = Text("NO", font=DISPLAY, color=INK, font_size=12)
            badge = VGroup(badge_bg, badge_txt)
            badge.move_to(test_boxes[i].get_right() + LEFT * 0.3)
            no_badges.add(badge)

        pass_line = Line(test_boxes[3].get_bottom(), test_boxes[4].get_top(),
                         color=INK, stroke_width=1.5)
        pass_line.set_stroke(opacity=0.6)

        self.play(FadeIn(no_badges), Create(pass_line), run_time=0.5)

        # State 5: GROUND TRUTH? box highlighted — fails
        gt_highlight = Rectangle(width=3.5, height=0.55)
        gt_highlight.set_stroke(color=CRIMSON, width=2, opacity=1)
        gt_highlight.set_fill(color=CRIMSON, opacity=0.25)
        gt_highlight.move_to(UP * (-1.2))

        self.play(Create(gt_highlight), run_time=0.4)

        # State 6: Route to DO NOT DELEGATE with reason label below
        fail_route = Line(test_boxes[4].get_right(), dont_box.get_left() + DOWN * 0.2,
                          color=CRIMSON, stroke_width=2)
        fail_route.set_stroke(opacity=1)

        reason_bg = Rectangle(width=4.5, height=0.38, stroke_width=0, stroke_opacity=0)
        reason_bg.set_fill(color=CREAM, opacity=1)
        reason_txt = Text("no external ground truth to verify", font=MONO,
                          color=CRIMSON, font_size=13)
        reason_grp = VGroup(reason_bg, reason_txt)
        reason_grp.move_to(DOWN * 2.2)

        self.play(Create(fail_route), FadeIn(reason_grp), run_time=0.5)

        # State 7: Final annotation
        note_bg = Rectangle(width=5.5, height=0.42, stroke_width=0, stroke_opacity=0)
        note_bg.set_fill(color=CREAM, opacity=1)
        note_txt = Text("5th test reclassified 1 task: DELEGATE → DO NOT DELEGATE",
                        font=MONO, color=INK, font_size=13)
        note_grp = VGroup(note_bg, note_txt)
        note_grp.move_to(DOWN * 2.8)
        self.play(FadeIn(note_grp, shift=UP * 0.1), run_time=0.4)

        self.wait(max(0.5, total - 4.2))
