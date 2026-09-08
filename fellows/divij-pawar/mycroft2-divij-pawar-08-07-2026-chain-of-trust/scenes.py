"""scenes.py — Manim scenes for chain-of-trust (claude-divij, Video 2).

Palette: cream #FAF9F5, ink #3D3929, terracotta #D97757, soft #73705F, ghost #A9A491.
Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF, editorial
voice only) / PT Mono (MONO, data+code only) — see graphics_lib.py. Boxes are
sized to their actual content via auto_box, never hand-measured. Standalone
✓/✕/≠ glyphs render via plain Text (no font override) — Montserrat has no
glyph for ✓/✕ and silently renders a '.notdef' box instead of erroring.
"""
import numpy as np
from graphics_lib import *

BG = "#FAF9F5"
INK = "#3D3929"
ACC = "#D97757"
SOFT = "#73705F"
GHOST = "#A9A491"


# ─────────────────────────────────────────────────────────────────────────────
#  B01_ChainOpen   (target ~9.1s)
#  Video 1's B09 end card, frozen, cracks open, new title revealed
# ─────────────────────────────────────────────────────────────────────────────
class B01_ChainOpen(Scene):
    def construct(self):
        self.camera.background_color = BG

        old_title = title("The Accountability Mesh", size=48, color=INK)
        old_title.move_to(ORIGIN + UP * 0.5)
        self.play(FadeIn(old_title), run_time=0.5)
        self.wait(1.5)

        crack_line = Line(UP * 2, DOWN * 2, color=ACC, stroke_width=3)
        self.play(Create(crack_line), run_time=0.4)
        self.wait(0.5)

        self.play(FadeOut(old_title), FadeOut(crack_line), run_time=0.4)
        self.wait(0.2)

        new_title = title("THE CHAIN OF TRUST", size=48, color=INK)
        new_title.move_to(ORIGIN + UP * 0.5)
        self.play(FadeIn(new_title), run_time=0.5)
        self.wait(5.1)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_SecurityCamera   (target ~15.7s)
#  Split screen: foggy thought-bubble vs sharp execution log
# ─────────────────────────────────────────────────────────────────────────────
class B02_SecurityCamera(Scene):
    def construct(self):
        self.camera.background_color = BG

        split_line = Line(UP * 3, DOWN * 3, color=GHOST, stroke_width=2)
        self.play(Create(split_line), run_time=0.3)
        self.wait(0.2)

        # LEFT: foggy thought bubble
        left_bubble = Circle(radius=1.6, color=SOFT, stroke_width=1.5, fill_opacity=0.1)
        left_bubble.move_to(LEFT * 3.6)
        squiggles = VGroup(
            *[Line(LEFT * 3.6 + UP * y + LEFT * 0.55, LEFT * 3.6 + UP * y + RIGHT * 0.55, color=SOFT, stroke_width=1.5)
              for y in [0.5, 0, -0.5]]
        )
        left_label = label("WHAT IT SAYS\nIT DID", size=26, color=SOFT).next_to(left_bubble, DOWN, buff=0.4)

        self.play(Create(left_bubble), FadeIn(squiggles), FadeIn(left_label), run_time=0.5)
        self.wait(1.0)

        # RIGHT: sharp execution log
        log_lines = VGroup(
            mono("FETCH_COMPANY_FACTS · 0.8s", size=22, color=INK),
            mono("LLM_CALL · 1.7s", size=22, color=INK),
            mono("OUTPUT", size=22, color=INK),
        ).arrange(DOWN, buff=0.32)
        right_box = auto_box(log_lines, h_pad=0.5, v_pad=0.4, color=GHOST, fill_opacity=0.04)
        VGroup(right_box, log_lines).move_to(RIGHT * 3.6)
        right_label = label("WHAT A CAMERA\nACTUALLY SAW", size=26, color=SOFT).next_to(right_box, DOWN, buff=0.4)

        self.play(Create(right_box), FadeIn(log_lines), FadeIn(right_label), run_time=0.6)
        self.wait(4.0)

        # Contrast pop
        self.play(
            squiggles.animate.set_opacity(0.3),
            left_bubble.animate.set_stroke(color=SOFT, width=0.5),
            right_box.animate.set_stroke(width=3, color=ACC),
            run_time=0.5
        )
        self.wait(7.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_ChainOfTrust   (target ~17.7s)
#  Four chain links: three green & solid, fourth broken/dotted
# ─────────────────────────────────────────────────────────────────────────────
class B03_ChainOfTrust(Scene):
    def construct(self):
        self.camera.background_color = BG

        t = title("The Chain of Trust", size=44, color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        link_positions = [LEFT * 5.0, LEFT * 1.7, RIGHT * 1.7, RIGHT * 5.0]
        link_names = ["CALLED\nTHE TOOL", "DATA WAS\nREAL", "MATCHES\nTHE FILING", "CAUSED\nTHE ANSWER"]

        for i, (pos, name) in enumerate(zip(link_positions, link_names)):
            link = Circle(radius=0.4, color=ACC, stroke_width=2.5).move_to(pos + UP * 1.5)

            if i < 3:
                chip = label_chip(name, ACC, size=18).next_to(link, DOWN, buff=0.45)
                self.play(Create(link), FadeIn(chip), run_time=0.4)
                self.wait(1.0)
                self.play(link.animate.set_fill(ACC, opacity=0.3), run_time=0.3)
                self.wait(0.5)

                if i < 2:
                    connector = Line(pos + UP * 1.5 + RIGHT * 0.4, link_positions[i + 1] + UP * 1.5 + LEFT * 0.4,
                                      color=ACC, stroke_width=2.5)
                    self.play(Create(connector), run_time=0.3)
                    self.wait(0.2)
            else:
                chip = label_chip(name, GHOST, size=18).next_to(pos + UP * 1.5, DOWN, buff=0.45)
                link_dotted = DashedLine(pos + UP * 1.5 + LEFT * 0.4, pos + UP * 1.5 + RIGHT * 0.4,
                                          color=ACC, stroke_width=2.5)
                self.play(Create(link_dotted), FadeIn(chip), run_time=0.5)
                spark1 = Circle(radius=0.12, color=ACC).move_to(pos + UP * 1.5 + RIGHT * 0.5)
                spark2 = Circle(radius=0.12, color=ACC).move_to(pos + UP * 1.5 + LEFT * 0.5)
                self.play(FadeIn(spark1), FadeIn(spark2), run_time=0.2)
                self.wait(0.3)
                self.play(FadeOut(spark1), FadeOut(spark2), run_time=0.2)
                self.wait(1.0)

        self.wait(7.1)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_ThreeWaysFooled   (target ~21.7s)
#  Three fast vignettes: rooster/sun, timeline loops, access control
# ─────────────────────────────────────────────────────────────────────────────
class B04_ThreeWaysFooled(Scene):
    def construct(self):
        self.camera.background_color = BG

        t = title("What Not to Trust", size=44, color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        # Vignette 1: Rooster and sun
        rooster_label = label("Rooster", size=26, color=ACC).move_to(LEFT * 4 + UP * 1)
        rooster = Circle(radius=0.32, color=ACC, fill_opacity=0.5).move_to(LEFT * 4 + UP * 0.15)
        sun = Circle(radius=0.55, color=ACC, fill_opacity=0.3, stroke_width=0).move_to(UP * 2)
        not_causes = label_chip("Not the same as caused", ACC, size=22).move_to(DOWN * 1.0)

        self.play(FadeIn(rooster_label), Create(rooster), Create(sun), FadeIn(not_causes), run_time=0.6)
        self.wait(5.0)
        self.play(FadeOut(rooster_label), FadeOut(rooster), FadeOut(sun), FadeOut(not_causes), run_time=0.4)
        self.wait(0.3)

        # Vignette 2: Timeline loops
        short_timeline = Line(LEFT * 2.2 + UP * 1, RIGHT * 0.6 + UP * 1, color=SOFT, stroke_width=3)
        long_timeline = Line(LEFT * 2.2 + DOWN * 0.5, RIGHT * 3.0 + DOWN * 0.5, color=SOFT, stroke_width=3)
        short_check = Text("✓", font_size=28, color=ACC).move_to(RIGHT * 0.95 + UP * 1)
        long_check = Text("✓", font_size=28, color=ACC).move_to(RIGHT * 3.35 + DOWN * 0.5)
        more_steps = label_chip("More steps ≠ more true", ACC, size=22).move_to(DOWN * 1.7)

        self.play(Create(short_timeline), Create(long_timeline), FadeIn(more_steps), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(short_check), FadeIn(long_check), run_time=0.3)
        self.wait(5.0)
        self.play(FadeOut(short_timeline), FadeOut(long_timeline), FadeOut(short_check), FadeOut(long_check),
                  FadeOut(more_steps), run_time=0.4)
        self.wait(0.3)

        # Vignette 3: Access control
        footage_text = label("FOOTAGE", size=22, color=SOFT)
        footage_box = auto_box(footage_text, h_pad=0.4, v_pad=0.3, color=SOFT)
        VGroup(footage_box, footage_text).move_to(LEFT * 2.2)
        auditor_label = label("Auditor only", size=22, color=SOFT).next_to(footage_box, UP, buff=0.3)

        investor_silhouette = Circle(radius=0.42, color=INK, fill_opacity=0.6).move_to(RIGHT * 1.4)
        investor_label = label("Investor", size=24, color=INK).next_to(investor_silhouette, DOWN, buff=0.3)

        alert = Circle(radius=0.32, color=ACC, fill_opacity=0.85, stroke_width=0).move_to(DOWN * 0.2)
        leak_label = label_chip("Wrong audience = leak", ACC, size=22).move_to(DOWN * 1.9)

        self.play(Create(footage_box), FadeIn(footage_text), FadeIn(auditor_label), FadeIn(investor_silhouette),
                  FadeIn(investor_label), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(alert), FadeIn(leak_label), run_time=0.3)
        self.wait(5.0)
        self.play(FadeOut(footage_box), FadeOut(footage_text), FadeOut(auditor_label), FadeOut(investor_silhouette),
                  FadeOut(investor_label), FadeOut(alert), FadeOut(leak_label), run_time=0.4)

        self.wait(2.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_HonestCeiling   (target ~8.4s)
#  Two-line text card, slow zoom, mirrors Video 1 B06 pacing
# ─────────────────────────────────────────────────────────────────────────────
class B05_HonestCeiling(Scene):
    def construct(self):
        self.camera.background_color = BG

        t = title("The Honest Ceiling", size=44, color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        line1 = label("PROOF OF WHAT RAN.", size=34, color=INK, weight="BOLD")
        line2 = label("NOT PROOF IT WAS RIGHT.", size=34, color=INK, weight="BOLD")

        text_group = VGroup(line1, line2).arrange(DOWN, buff=0.5)

        self.play(FadeIn(line1), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(line2), run_time=0.5)
        self.wait(1.5)

        self.play(text_group.animate.scale(1.2), run_time=0.8)
        self.wait(3.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_ToolboxPartOne   (target ~21.7s)
#  Toolbox opens, two tools slide out, third slot empty for B07
# ─────────────────────────────────────────────────────────────────────────────
class B06_ToolboxPartOne(Scene):
    def construct(self):
        self.camera.background_color = BG

        t = title("Closing the Gap (1/2)", size=44, color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        toolbox = Rectangle(width=9.6, height=5.2, color=INK, stroke_width=2.5).move_to(DOWN * 0.2)
        toolbox_label = label("TOOLS", size=26, color=INK, weight="BOLD").move_to(toolbox.get_top() + DOWN * 0.5)
        self.play(Create(toolbox), FadeIn(toolbox_label), run_time=0.5)
        self.wait(0.5)

        # Tool 1: Jenga tower
        tool1 = Rectangle(width=0.8, height=1.8, color=ACC, stroke_width=2, fill_opacity=0.1).move_to(
            toolbox.get_center() + LEFT * 3.0 + DOWN * 0.2)
        tool1_chip = label_chip("Pull the fact out", ACC, size=20).next_to(tool1, UP, buff=0.4)

        self.play(FadeIn(tool1), FadeIn(tool1_chip), run_time=0.4)
        self.wait(3.0)

        # Tool 2: Locked circuit
        tool2 = Circle(radius=0.5, color=ACC, stroke_width=2.5, fill_opacity=0.1).move_to(
            toolbox.get_center() + RIGHT * 3.0 + UP * 0.2)
        tool2_chip = label_chip("Look inside", ACC, size=20).next_to(tool2, UP, buff=0.4)
        tool2_caption = label("(locked, for now)", size=20, color=SOFT).next_to(tool2, DOWN, buff=0.3)
        tool2_lock = Line(tool2.get_top(), tool2.get_bottom(), color=ACC, stroke_width=2.5)

        self.play(FadeIn(tool2), FadeIn(tool2_lock), FadeIn(tool2_chip), FadeIn(tool2_caption), run_time=0.5)
        self.wait(5.0)

        # Empty slot hint (dashed rectangle)
        empty_box = DashedVMobject(
            Rectangle(width=1.6, height=1.6).move_to(toolbox.get_center() + DOWN * 1.6),
            num_dashes=24, color=GHOST
        )
        empty_label = label("?", size=40, color=GHOST).move_to(toolbox.get_center() + DOWN * 1.6)

        self.play(Create(empty_box), FadeIn(empty_label), run_time=0.4)
        self.wait(8.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B07_ToolboxPartTwo   (target ~15.1s)
#  Continues from B06, tool 3 slides in, toolbox closes
# ─────────────────────────────────────────────────────────────────────────────
class B07_ToolboxPartTwo(Scene):
    def construct(self):
        self.camera.background_color = BG

        t = title("Closing the Gap (2/2)", size=44, color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        # Toolbox (recreate from B06 end state)
        toolbox = Rectangle(width=9.6, height=5.2, color=INK, stroke_width=2.5).move_to(DOWN * 0.2)
        toolbox_label = label("TOOLS", size=26, color=INK, weight="BOLD").move_to(toolbox.get_top() + DOWN * 0.5)

        tool1 = Rectangle(width=0.8, height=1.8, color=ACC, stroke_width=2, fill_opacity=0.1).move_to(
            toolbox.get_center() + LEFT * 3.0 + DOWN * 0.2)
        tool1_chip = label_chip("Pull the fact out", ACC, size=20).next_to(tool1, UP, buff=0.4)

        tool2 = Circle(radius=0.5, color=ACC, stroke_width=2.5, fill_opacity=0.1).move_to(
            toolbox.get_center() + RIGHT * 3.0 + UP * 0.2)
        tool2_chip = label_chip("Look inside", ACC, size=20).next_to(tool2, UP, buff=0.4)
        tool2_caption = label("(locked, for now)", size=20, color=SOFT).next_to(tool2, DOWN, buff=0.3)
        tool2_lock = Line(tool2.get_top(), tool2.get_bottom(), color=ACC, stroke_width=2.5)

        empty_box = DashedVMobject(
            Rectangle(width=1.6, height=1.6).move_to(toolbox.get_center() + DOWN * 1.6),
            num_dashes=24, color=GHOST
        )

        self.play(Create(toolbox), FadeIn(toolbox_label), FadeIn(tool1), FadeIn(tool1_chip),
                  FadeIn(tool2), FadeIn(tool2_lock), FadeIn(tool2_chip), FadeIn(tool2_caption),
                  Create(empty_box), run_time=0.5)
        self.wait(0.5)

        # Tool 3: Forecaster
        tool3 = Circle(radius=0.45, color=ACC, stroke_width=2.5, fill_opacity=0.1).move_to(
            toolbox.get_center() + DOWN * 1.6)
        checkmarks = VGroup(*[Text("✓", font_size=24, color=ACC) for _ in range(3)]).arrange(
            RIGHT, buff=0.2).next_to(tool3, RIGHT, buff=0.45)
        tool3_chip = label_chip("Grade the track record", ACC, size=20).next_to(tool3, DOWN, buff=0.45)

        self.play(FadeOut(empty_box), FadeIn(tool3), FadeIn(checkmarks), FadeIn(tool3_chip), run_time=0.5)
        self.wait(3.0)

        # Close toolbox
        self.play(toolbox.animate.scale(0.95), run_time=0.5)
        self.wait(8.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B08_WhatsHoldingUsBack   (target ~20.8s)
#  Three quick vignettes: locked box, calendar, dashboard choice
# ─────────────────────────────────────────────────────────────────────────────
class B08_WhatsHoldingUsBack(Scene):
    def construct(self):
        self.camera.background_color = BG

        t = title("What's Holding Us Back", size=40, color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        # Vignette 1: Locked box
        box1 = Rectangle(width=1.8, height=1.8, color=INK, stroke_width=2.5, fill_opacity=0.15).move_to(LEFT * 3.8)
        lock1 = Circle(radius=0.3, color=ACC, fill_opacity=0.7).move_to(box1.get_center())
        label1 = label("Frontier models:", size=22, color=SOFT).next_to(box1, DOWN, buff=0.4)
        chip1 = label_chip("Closed", ACC, size=20).next_to(label1, DOWN, buff=0.2)

        self.play(Create(box1), FadeIn(lock1), FadeIn(label1), FadeIn(chip1), run_time=0.5)
        self.wait(4.5)
        self.play(FadeOut(box1), FadeOut(lock1), FadeOut(label1), FadeOut(chip1), run_time=0.3)

        # Vignette 2: Calendar
        months = VGroup(*[label(m, size=20, color=INK) for m in ("JAN", "FEB", "MAR", "APR")]).arrange(RIGHT, buff=0.25)
        cal_rect = auto_box(months, h_pad=0.4, v_pad=0.3, color=SOFT)
        VGroup(cal_rect, months).move_to(UP * 0.2)
        label2 = label("Calibration needs", size=22, color=SOFT).next_to(cal_rect, DOWN, buff=0.4)
        chip2 = label_chip("Real time", ACC, size=20).next_to(label2, DOWN, buff=0.2)

        self.play(Create(cal_rect), FadeIn(months), FadeIn(label2), FadeIn(chip2), run_time=0.5)
        self.wait(4.5)
        self.play(FadeOut(cal_rect), FadeOut(months), FadeOut(label2), FadeOut(chip2), run_time=0.3)

        # Vignette 3: Two dashboards
        dash_l = Rectangle(width=2.2, height=1.4, color=SOFT, stroke_width=1.8).move_to(LEFT * 2.2)
        dash_r = Rectangle(width=2.2, height=1.4, color=ACC, stroke_width=2.5).move_to(RIGHT * 2.2)
        cost_l = label("costs 10x more\ntakes 6 months", size=20, color=SOFT).next_to(dash_l, DOWN, buff=0.4)
        cost_r = label_chip("Ships Friday", ACC, size=20).next_to(dash_r, DOWN, buff=0.4)
        cursor = Circle(radius=0.18, color=ACC, fill_opacity=0.85, stroke_width=0).move_to(dash_r.get_center() + UP * 0.35)

        self.play(Create(dash_l), Create(dash_r), FadeIn(cost_l), FadeIn(cost_r), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(cursor), run_time=0.2)
        self.wait(8.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B09_Scorecard   (target ~20.7s)
#  Two-column table: PROVEN / STILL OPEN
# ─────────────────────────────────────────────────────────────────────────────
class B09_Scorecard(Scene):
    def construct(self):
        self.camera.background_color = BG

        t = title("Where This Project Ends", size=40, color=INK)
        self.play(Write(t), run_time=0.5)
        self.wait(0.3)

        # Headers
        header_proven = label_chip("Proven", ACC, size=24).move_to(LEFT * 2.4 + UP * 2)
        header_open = label_chip("Still open", SOFT, size=24).move_to(RIGHT * 2.4 + UP * 2)

        self.play(FadeIn(header_proven), FadeIn(header_open), run_time=0.4)
        self.wait(1.0)

        # Proven items
        proven_items = VGroup(
            checked("Structure enforced", size=22, color=ACC, trailing=True),
            checked("Claims checked vs filings", size=22, color=ACC, trailing=True),
            checked("Behavior fully traceable", size=22, color=ACC, trailing=True),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(LEFT * 2.4 + ORIGIN)

        for item in proven_items:
            self.play(FadeIn(item), run_time=0.3)
            self.wait(2.2)

        # Still open item
        question_mark = label("?", size=34, color=SOFT, weight="BOLD")
        open_item = label("Is the reasoning\ngenuine?", size=22, color=SOFT)
        open_group = VGroup(question_mark, open_item).arrange(RIGHT, buff=0.25).move_to(RIGHT * 2.4 + ORIGIN)

        self.play(FadeIn(open_group), run_time=0.4)
        self.wait(10.5)
