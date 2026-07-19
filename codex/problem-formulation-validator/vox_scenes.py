"""vox_scenes.py — Validate Your Build Problem Formulation Before Running Codex
(problem-formulation-validator, slate cut, 16:9)

B04 and B06 are MANIM type — animated traffic light scenes.
All other beats are SLATE.

Color law: CRIMSON = fail / vague / unresolved; GREEN = pass / specific / ready.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
GREEN = "#4CAF50"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---- B04: FormulationTrafficLight
# Three question cards, each with an answer and a traffic light circle.
# Q1 fails (CRIMSON), Q2 and Q3 pass (GREEN).

class B04_FormulationTrafficLight(Scene):
    def construct(self):
        total = DUR.get("B04", 20.0)

        # Title
        title = Text("FORMULATION TEST", font=DISPLAY, color=INK,
                     font_size=36, weight="BOLD")
        title.move_to(UP * 3.2)

        # Three question cards — Rectangle at y=1.5, 0.0, -1.5, x=-1.5
        card_data = [
            ("Q1: WHAT DOES IT DO?",       1.5,  "build a feedback notifier",
             False, "Missing: input format, output location"),
            ("Q2: WHAT DOES IT TOUCH?",    0.0,  "reads JSON from playtests/, writes one .md",
             True,  None),
            ("Q3: WHAT DOES IT NEVER TOUCH?", -1.5, "never writes to src/ or game code",
             True,  None),
        ]

        cards = VGroup()
        answers = VGroup()
        lights = VGroup()
        annotations = VGroup()

        for label_text, card_y, answer_text, passed, annotation_text in card_data:
            # Card rectangle
            card = Rectangle(width=5.0, height=0.8)
            card.set_fill(CREAM, opacity=1).set_stroke(color=INK, width=1.5)
            card.move_to(LEFT * 1.5 + UP * card_y)
            card_label = Text(label_text, font=DISPLAY, color=INK, font_size=20,
                              weight="BOLD")
            card_label.move_to(card.get_center())
            if card_label.width > 4.6:
                card_label.scale_to_fit_width(4.6)
            cards.add(VGroup(card, card_label))

            # Answer text
            ans = Text(answer_text, font=SERIF, color=SLATE, font_size=16,
                       slant=ITALIC)
            ans.move_to(LEFT * 1.5 + UP * (card_y - 0.65))
            if ans.width > 5.0:
                ans.scale_to_fit_width(5.0)
            answers.add(ans)

            # Traffic light circle
            light_color = GREEN if passed else CRIMSON
            light = Circle(radius=0.25)
            light.set_fill(light_color, opacity=1).set_stroke(width=0)
            light.move_to(RIGHT * 2.5 + UP * card_y)
            lights.add(light)

            # Annotation for failed cards
            if annotation_text:
                # CREAM background behind annotation
                ann_text = Text(annotation_text, font=DISPLAY, color=CRIMSON,
                                font_size=14, weight="BOLD")
                ann_text.move_to(RIGHT * 2.5 + UP * (card_y - 0.55))
                ann_bg = Rectangle(
                    width=ann_text.width + 0.2,
                    height=ann_text.height + 0.1
                ).set_fill(CREAM, opacity=1).set_stroke(width=0, opacity=0)
                ann_bg.move_to(ann_text.get_center())
                annotations.add(VGroup(ann_bg, ann_text))

        # Legend at bottom
        leg_green = Circle(radius=0.15).set_fill(GREEN, 1).set_stroke(width=0)
        leg_green.move_to(LEFT * 2.0 + DOWN * 3.2)
        leg_green_label = Text("PASS", font=DISPLAY, color=INK, font_size=16,
                               weight="BOLD")
        leg_green_label.next_to(leg_green, RIGHT, buff=0.2)

        leg_red = Circle(radius=0.15).set_fill(CRIMSON, 1).set_stroke(width=0)
        leg_red.move_to(RIGHT * 0.5 + DOWN * 3.2)
        leg_red_label = Text("FAIL", font=DISPLAY, color=INK, font_size=16,
                             weight="BOLD")
        leg_red_label.next_to(leg_red, RIGHT, buff=0.2)

        legend = VGroup(leg_green, leg_green_label, leg_red, leg_red_label)

        # Animation sequence (6 states)
        # 1. Title appears
        self.play(FadeIn(title), run_time=0.6)
        # 2. All 3 question cards appear
        self.play(LaggedStart(*[FadeIn(c) for c in cards], lag_ratio=0.25, run_time=1.0))
        # 3. Answer texts appear
        self.play(LaggedStart(*[FadeIn(a) for a in answers], lag_ratio=0.25, run_time=0.9))
        # 4. Traffic light circles appear
        self.play(LaggedStart(*[FadeIn(l) for l in lights], lag_ratio=0.25, run_time=0.9))
        # 5. Q1 annotation appears
        self.play(FadeIn(annotations), run_time=0.6)
        # 6. Legend appears
        self.play(FadeIn(legend), run_time=0.5)

        self.wait(max(0.5, total - 4.5))


# ---- B06: FormulationAllGreen
# Same three cards, Q1 now corrected and turning green.

class B06_FormulationAllGreen(Scene):
    def construct(self):
        total = DUR.get("B06", 14.0)

        # Title
        title = Text("FORMULATION TEST", font=DISPLAY, color=INK,
                     font_size=36, weight="BOLD")
        title.move_to(UP * 3.2)

        # Three question cards with updated Q1 answer
        card_data = [
            ("Q1: WHAT DOES IT DO?",       1.5,
             "reads JSON exports, filters build version, groups by system,\nwrites one .md to playtests/v{build}.md"),
            ("Q2: WHAT DOES IT TOUCH?",    0.0,
             "reads JSON from playtests/, writes one .md"),
            ("Q3: WHAT DOES IT NEVER TOUCH?", -1.5,
             "never writes to src/ or game code"),
        ]

        cards = VGroup()
        answers = VGroup()

        for label_text, card_y, answer_text in card_data:
            card = Rectangle(width=5.0, height=0.8)
            card.set_fill(CREAM, opacity=1).set_stroke(color=INK, width=1.5)
            card.move_to(LEFT * 1.5 + UP * card_y)
            card_label = Text(label_text, font=DISPLAY, color=INK, font_size=20,
                              weight="BOLD")
            card_label.move_to(card.get_center())
            if card_label.width > 4.6:
                card_label.scale_to_fit_width(4.6)
            cards.add(VGroup(card, card_label))

            ans = Text(answer_text, font=SERIF, color=SLATE, font_size=14,
                       slant=ITALIC)
            ans.move_to(LEFT * 1.5 + UP * (card_y - 0.70))
            if ans.width > 5.2:
                ans.scale_to_fit_width(5.2)
            answers.add(ans)

        # Traffic lights — Q1 starts CRIMSON, transitions to GREEN
        q1_light = Circle(radius=0.25)
        q1_light.set_fill(CRIMSON, opacity=1).set_stroke(width=0)
        q1_light.move_to(RIGHT * 2.5 + UP * 1.5)

        q2_light = Circle(radius=0.25)
        q2_light.set_fill("#4CAF50", opacity=1).set_stroke(width=0)
        q2_light.move_to(RIGHT * 2.5 + UP * 0.0)

        q3_light = Circle(radius=0.25)
        q3_light.set_fill("#4CAF50", opacity=1).set_stroke(width=0)
        q3_light.move_to(RIGHT * 2.5 + DOWN * 1.5)

        # FORMULATION READY text
        ready_text = Text("FORMULATION READY", font=DISPLAY, color=INK,
                          font_size=28, weight="BOLD")
        ready_text.move_to(DOWN * 2.8)
        ready_bg = Rectangle(
            width=ready_text.width + 0.4,
            height=ready_text.height + 0.2
        ).set_fill(CREAM, opacity=1).set_stroke(width=0, opacity=0)
        ready_bg.move_to(ready_text.get_center())

        # Animation sequence (6 states)
        # 1. Title appears
        self.play(FadeIn(title), run_time=0.5)
        # 2. Three cards appear with answers
        self.play(LaggedStart(*[FadeIn(c) for c in cards], lag_ratio=0.2, run_time=0.8))
        self.play(LaggedStart(*[FadeIn(a) for a in answers], lag_ratio=0.2, run_time=0.7))
        # 3. Q1 circle appears CRIMSON (starting state)
        self.play(FadeIn(q1_light), run_time=0.4)
        # 4. Q2 and Q3 circles appear green
        self.play(FadeIn(q2_light), FadeIn(q3_light), run_time=0.5)
        # 5. Q1 circle animates to green
        self.play(q1_light.animate.set_fill("#4CAF50"), run_time=0.8)
        # 6. FORMULATION READY appears
        self.play(FadeIn(ready_bg), FadeIn(ready_text), run_time=0.6)

        self.wait(max(0.5, total - 4.3))
