"""vox_scenes.py — The Bronze Argument: How a Statue Makes a Political Claim
(vox-bronze-argument, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 and B10 are STILL
(archive slots) and have no scenes here. Durations read from this reel's
beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh writing-guide/youtube/vox-bronze-argument

Color law (teardown palette): CRIMSON = the composition's hierarchy claim
(what is being analyzed); TEAL/INK = the analytical reading. GOLD = once,
as fill only. Never swap mid-film.

Gate B convention: every zero-width stroke is also zero-opacity, or the layout
audit strikes it. _qc_intentional flags deliberate overlaps.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 10.5, "B03": 10.0, "B04": 9.5, "B05": 10.0,
    "B06": 10.0, "B07": 11.0, "B08": 11.5, "B09": 10.5,
    "B11": 12.5, "B12": 11.0, "B13": 10.5,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _figure_silhouette(center, height=1.4, color=INK, mounted=False):
    """A simple stick figure at center. If mounted=True, add a horse outline."""
    # head
    head = Circle(radius=0.13).set_fill(color, 1).set_stroke(width=0, opacity=0)
    # body
    body = Line(ORIGIN, DOWN * 0.55, color=color, stroke_width=3.5)
    # arms
    la = Line(DOWN * 0.18, DOWN * 0.18 + LEFT * 0.3 + DOWN * 0.2,
              color=color, stroke_width=3.0)
    ra = Line(DOWN * 0.18, DOWN * 0.18 + RIGHT * 0.3 + DOWN * 0.2,
              color=color, stroke_width=3.0)
    # legs
    ll = Line(DOWN * 0.55, DOWN * 0.55 + LEFT * 0.22 + DOWN * 0.38,
              color=color, stroke_width=3.0)
    rl = Line(DOWN * 0.55, DOWN * 0.55 + RIGHT * 0.22 + DOWN * 0.38,
              color=color, stroke_width=3.0)

    # Assemble: body, arms, legs relative to head
    body.next_to(head, DOWN, buff=0.02)
    la.move_to(body.get_center() + UP * 0.05)
    ra.move_to(body.get_center() + UP * 0.05)
    ll.next_to(body, DOWN, buff=0.0).shift(LEFT * 0.08)
    rl.next_to(body, DOWN, buff=0.0).shift(RIGHT * 0.08)
    fig = VGroup(head, body, la, ra, ll, rl)
    fig.scale(height / 1.3)
    fig.move_to(center)
    return fig


def _horse_and_rider(center, color=INK):
    """Simplified horse body + rider silhouette."""
    # horse body — oval
    horse = Ellipse(width=1.8, height=0.8)
    horse.set_fill(color, 0.18).set_stroke(color, 2.5)
    # rider on top
    rider_head = Circle(radius=0.12).set_fill(color, 1).set_stroke(width=0, opacity=0)
    rider_body = Line(ORIGIN, DOWN * 0.4, color=color, stroke_width=3.5)
    rider = VGroup(rider_head, rider_body)
    rider.next_to(horse, UP, buff=0.08).shift(RIGHT * 0.1)
    rider_head.move_to(rider_body.get_start() + UP * 0.12)
    group = VGroup(horse, rider)
    group.move_to(center)
    return group


def _elevation_line(bottom_pt, top_pt, color=CRIMSON):
    """A vertical measurement line with tick marks."""
    line = Line(bottom_pt, top_pt, color=color, stroke_width=1.8)
    tick_b = Line(bottom_pt + LEFT * 0.12, bottom_pt + RIGHT * 0.12,
                  color=color, stroke_width=1.8)
    tick_t = Line(top_pt + LEFT * 0.12, top_pt + RIGHT * 0.12,
                  color=color, stroke_width=1.8)
    return VGroup(line, tick_b, tick_t)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        kicker = LabelChip("WRITING", accent=CRIMSON, size=22)
        kicker.to_edge(UP, buff=0.8).shift(LEFT * 0.0)
        t1 = Text("The Bronze", font=DISPLAY, color=INK, font_size=64, weight="MEDIUM")
        t2 = Text("Argument", font=DISPLAY, color=INK, font_size=64, weight="MEDIUM")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.1).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.18,
                 t2.get_corner(DR) + DOWN * 0.18,
                 color=CRIMSON, stroke_width=2.5)
        sub = Text("how a statue makes a political claim",
                   font=SERIF, color=SLATE, font_size=28, slant=ITALIC)
        sub.next_to(u, DOWN, buff=0.45)
        self.play(FadeIn(kicker, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(block, shift=UP * 0.2), Create(u), run_time=1.2)
        self.play(FadeIn(sub, shift=UP * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 2.5))


class B03_ThreeFigures(Scene):
    """Cold open: three-figure diagram appears — Roosevelt elevated + named,
    two unnamed figures below on foot. Elevation lines drawn. Labels appear."""

    def construct(self):
        total = DUR["B03"]

        # positions: Roosevelt elevated center, two figures lateral and lower
        roosevelt_center = UP * 1.6 + RIGHT * 0.0
        left_center = DOWN * 0.5 + LEFT * 3.2
        right_center = DOWN * 0.5 + RIGHT * 3.2

        # baseline
        baseline_y = -2.2
        baseline = Line(LEFT * 6.5 + UP * baseline_y,
                        RIGHT * 6.5 + UP * baseline_y,
                        color=SLATE, stroke_width=1.5)

        # Roosevelt on horse
        roosevelt = _horse_and_rider(roosevelt_center, color=INK)

        # two walking figures
        fig_left = _figure_silhouette(left_center, height=1.2, color=INK)
        fig_right = _figure_silhouette(right_center, height=1.2, color=INK)

        # elevation lines from baseline to figure feet
        roo_elev = _elevation_line(
            UP * baseline_y + RIGHT * 0.0,
            UP * (roosevelt_center[1] - 0.7),
            color=CRIMSON
        )
        left_elev = _elevation_line(
            UP * baseline_y + LEFT * 3.2,
            UP * (left_center[1] - 0.6),
            color=SLATE
        )
        right_elev = _elevation_line(
            UP * baseline_y + RIGHT * 3.2,
            UP * (right_center[1] - 0.6),
            color=SLATE
        )

        # labels
        roo_name = SerifLabel("Roosevelt", CRIMSON, size=24)
        roo_name.next_to(roosevelt, UP, buff=0.28)
        roo_label = LabelChip("NAMED", accent=INK, size=20)
        roo_label.next_to(roo_name, RIGHT, buff=0.3)

        q_left = Text("?", font=SERIF, color=SLATE, font_size=44, weight=BOLD)
        q_left.next_to(fig_left, UP, buff=0.22)
        q_right = Text("?", font=SERIF, color=SLATE, font_size=44, weight=BOLD)
        q_right.next_to(fig_right, UP, buff=0.22)

        anon_chip = LabelChip("ANONYMOUS", accent=SLATE, size=18)
        anon_chip.move_to(DOWN * 1.7)

        # animate: baseline, then figures, then labels, then elevation
        self.play(Create(baseline), run_time=0.5)
        self.play(FadeIn(fig_left, shift=UP * 0.3),
                  FadeIn(fig_right, shift=UP * 0.3),
                  run_time=0.8)
        self.play(FadeIn(roosevelt, scale=0.9), run_time=0.8)
        # elevation lines
        self.play(Create(roo_elev), Create(left_elev), Create(right_elev),
                  run_time=0.9)
        # name labels
        self.play(FadeIn(roo_name), FadeIn(roo_label), run_time=0.7)
        self.play(FadeIn(q_left), FadeIn(q_right), run_time=0.6)
        self.play(FadeIn(anon_chip, scale=0.9), run_time=0.5)
        self.wait(max(0.4, total - 4.8))


class B04_Question(Scene):
    """THE QUESTION card."""

    def construct(self):
        total = DUR["B04"]
        kicker = LabelChip("WRITING", accent=CRIMSON, size=22)
        kicker.to_edge(UP, buff=0.9)
        q = Text("How does composition\nmake an argument?",
                 font=DISPLAY, color=INK, font_size=52, weight="MEDIUM",
                 line_spacing=1.2)
        q.move_to(ORIGIN + DOWN * 0.1)
        u = Line(q.get_corner(DL) + DOWN * 0.2,
                 q.get_corner(DR) + DOWN * 0.2,
                 color=CRIMSON, stroke_width=2.5)
        self.play(FadeIn(kicker, shift=DOWN * 0.15), run_time=0.5)
        self.play(FadeIn(q, shift=UP * 0.2), Create(u), run_time=1.1)
        self.wait(max(0.5, total - 1.6))


class B05_NaiveRead(Scene):
    """THE PROBLEM — two-panel: what you see vs. what it argues.
    Right panel (analysis) starts blank — arrives later to frame the gap."""

    def construct(self):
        total = DUR["B05"]

        # Left panel — naive reading
        left_box = Rectangle(width=5.0, height=3.6)
        left_box.set_fill(WHITE, 0.0).set_stroke(SLATE, 1.8)
        left_box.move_to(LEFT * 3.0)
        left_chip = LabelChip("WHAT YOU SEE", accent=SLATE, size=20)
        left_chip.next_to(left_box, UP, buff=0.25)

        # simple figure inside left panel
        fig_icon = _figure_silhouette(left_box.get_center(), height=1.3, color=INK)

        # Right panel — analytical reading (starts blank)
        right_box = Rectangle(width=5.0, height=3.6)
        right_box.set_fill(WHITE, 0.0).set_stroke(SLATE, 1.8)
        right_box.move_to(RIGHT * 3.0)
        right_chip = LabelChip("WHAT IT ARGUES", accent=CRIMSON, size=20)
        right_chip.next_to(right_box, UP, buff=0.25)

        # question mark in right panel — the gap
        gap_q = Text("?", font=DISPLAY, color=CRIMSON, font_size=90, weight="MEDIUM")
        gap_q.move_to(right_box.get_center())

        self.play(Create(left_box), FadeIn(left_chip, shift=DOWN * 0.2),
                  run_time=0.8)
        self.play(FadeIn(fig_icon, scale=0.9), run_time=0.6)
        self.play(Create(right_box), FadeIn(right_chip, shift=DOWN * 0.2),
                  run_time=0.8)
        self.play(FadeIn(gap_q, scale=0.85), run_time=0.6)
        self.wait(max(0.4, total - 2.8))


class B06_ThreeLayers(Scene):
    """THE PROBLEM — three stacked bands appear in sequence:
    DESCRIPTION, REFLECTION, ANALYSIS. ANALYSIS arrives last with upward motion."""

    def construct(self):
        total = DUR["B06"]

        band_w = 9.0
        band_h = 1.05
        gap = 0.28

        labels = ["DESCRIPTION", "REFLECTION", "ANALYSIS"]
        colors = [SLATE, SLATE, INK]
        sub_texts = [
            "what is in the frame",
            "what it evokes",
            "what formal choices produce the effect",
        ]

        bands = VGroup()
        for i, (lab, col, sub) in enumerate(zip(labels, colors, sub_texts)):
            box = Rectangle(width=band_w, height=band_h)
            box.set_fill(WHITE, 0.0).set_stroke(col, 1.8)
            chip = LabelChip(lab, accent=col, size=21)
            chip.move_to(box.get_left() + RIGHT * 1.5)
            sub_t = Text(sub, font=SERIF, color=SLATE, font_size=24, slant=ITALIC)
            sub_t.move_to(box.get_center() + RIGHT * 1.8)
            band_group = VGroup(box, chip, sub_t)
            bands.add(band_group)

        bands.arrange(DOWN, buff=gap)
        # Move bottom band up into ANALYSIS highlight position
        bands.move_to(ORIGIN)

        # ANALYSIS gets TEAL accent on its underline (it is the focus)
        analysis_u = Line(
            bands[2][0].get_corner(DL) + DOWN * 0.06,
            bands[2][0].get_corner(DR) + DOWN * 0.06,
            color=CRIMSON, stroke_width=2.5
        )

        self.play(FadeIn(bands[0], shift=RIGHT * 0.4), run_time=0.7)
        self.play(FadeIn(bands[1], shift=RIGHT * 0.4), run_time=0.7)
        # ANALYSIS arrives from below with upward motion
        self.play(FadeIn(bands[2], shift=UP * 0.35), run_time=0.8)
        self.play(Create(analysis_u), run_time=0.5)
        self.wait(max(0.4, total - 2.7))


class B07_ScanUp(Scene):
    """THE MECHANISM — scan animation. The three-figure diagram reappears.
    A camera-eye indicator (circle with serif 'eye') starts at the two lateral
    figures and moves upward to Roosevelt, tracing the hierarchy."""

    def construct(self):
        total = DUR["B07"]

        # Rebuild the three-figure diagram (condensed)
        baseline_y = -2.6
        baseline = Line(LEFT * 6.5 + UP * baseline_y,
                        RIGHT * 6.5 + UP * baseline_y,
                        color=SLATE, stroke_width=1.2)

        roo_center = UP * 1.5
        left_center = DOWN * 0.55 + LEFT * 3.0
        right_center = DOWN * 0.55 + RIGHT * 3.0

        roosevelt = _horse_and_rider(roo_center, color=INK)
        fig_left = _figure_silhouette(left_center, height=1.15, color=INK)
        fig_right = _figure_silhouette(right_center, height=1.15, color=INK)

        roo_name = SerifLabel("Roosevelt", CRIMSON, size=22)
        roo_name.next_to(roosevelt, UP, buff=0.22)

        # Camera-eye indicator — a circle with an arrow
        eye_r = 0.32
        eye_circle = Circle(radius=eye_r)
        eye_circle.set_fill(WHITE, 0.0).set_stroke(CRIMSON, 3.0)
        eye_dot = Dot(radius=0.08, color=CRIMSON)
        eye_dot.move_to(eye_circle.get_center())
        eye = VGroup(eye_circle, eye_dot)

        # Start position: at the level of the two foot-figures
        start_pos = DOWN * 0.55  # between the two lateral figures
        eye.move_to(start_pos)

        # Elevation arrows (upward) beside the center column
        arr1 = Arrow(UP * baseline_y + RIGHT * 0.3, roo_center + DOWN * 0.8 + RIGHT * 0.3,
                     color=CRIMSON, stroke_width=2.5, buff=0.1)
        arr1._qc_intentional = True  # arrow near figures — intentional

        # Show the diagram first
        self.play(
            FadeIn(baseline, run_time=0.4),
            FadeIn(fig_left, run_time=0.5),
            FadeIn(fig_right, run_time=0.5),
            FadeIn(roosevelt, run_time=0.6),
            FadeIn(roo_name, run_time=0.5),
            lag_ratio=0.15
        )
        # Show the eye at start (foot level)
        self.play(FadeIn(eye, scale=0.85), run_time=0.5)
        # Pause at foot level
        self.wait(0.4)
        # Scan upward through the three positions
        # 1) Move up to the lateral figures' chest level
        self.play(eye.animate.move_to(DOWN * 0.0), run_time=0.7)
        # 2) Draw the upward arrow as the eye continues up
        self.play(
            eye.animate.move_to(UP * 0.9),
            Create(arr1),
            run_time=1.0
        )
        # 3) Arrive at Roosevelt level
        self.play(eye.animate.move_to(roo_center + DOWN * 0.15), run_time=0.7)
        # 4) Pulse the eye at Roosevelt to mark arrival
        self.play(eye.animate.scale(1.25), run_time=0.35)
        self.play(eye.animate.scale(1.0 / 1.25), run_time=0.3)
        self.wait(max(0.4, total - 4.5 - 0.4))


class B08_ThreeChoices(Scene):
    """THE MECHANISM — three annotation label chips land beside the diagram.
    ELEVATION, NAMING, ARRANGEMENT appear one at a time."""

    def construct(self):
        total = DUR["B08"]

        # Compact three-figure diagram
        roo_center = UP * 1.4 + LEFT * 1.0
        left_center = DOWN * 0.5 + LEFT * 4.8
        right_center = DOWN * 0.5 + RIGHT * 1.6

        baseline_y = -2.4
        baseline = Line(LEFT * 7.0 + UP * baseline_y,
                        RIGHT * 4.5 + UP * baseline_y,
                        color=SLATE, stroke_width=1.2)

        roosevelt = _horse_and_rider(roo_center, color=INK)
        fig_left = _figure_silhouette(left_center, height=1.1, color=INK)
        fig_right = _figure_silhouette(right_center, height=1.1, color=INK)

        # --- ANNOTATION 1: ELEVATION ---
        elev_chip = LabelChip("ELEVATION", accent=CRIMSON, size=22)
        # Position right of center-column
        elev_chip.move_to(UP * 1.4 + RIGHT * 3.2)
        elev_arrow_line = Line(
            roo_center + RIGHT * 0.55,
            elev_chip.get_left() + LEFT * 0.15,
            color=CRIMSON, stroke_width=1.8
        )

        # --- ANNOTATION 2: NAMING ---
        naming_chip = LabelChip("NAMING", accent=CRIMSON, size=22)
        naming_chip.move_to(UP * 3.0 + LEFT * 1.0)
        naming_label = SerifLabel("named", INK, size=20)
        naming_label.next_to(roosevelt, UP, buff=0.22)
        q_l = Text("?", font=SERIF, color=SLATE, font_size=36, weight=BOLD)
        q_l.next_to(fig_left, UP, buff=0.18)
        q_r = Text("?", font=SERIF, color=SLATE, font_size=36, weight=BOLD)
        q_r.next_to(fig_right, UP, buff=0.18)

        # --- ANNOTATION 3: ARRANGEMENT ---
        arr_chip = LabelChip("ARRANGEMENT", accent=CRIMSON, size=22)
        arr_chip.to_edge(DOWN, buff=0.55).shift(LEFT * 0.5)

        # center bracket above Roosevelt
        ctr_brk_top = UP * baseline_y + RIGHT * (roo_center[0])
        ctr_line = DashedLine(
            roo_center + DOWN * 0.7,
            UP * baseline_y + RIGHT * roo_center[0],
            color=SLATE, stroke_width=1.5, dash_length=0.15
        )
        ctr_label = Text("centered", font=SERIF, color=SLATE, font_size=20,
                         slant=ITALIC)
        ctr_label.next_to(ctr_line, RIGHT, buff=0.12)

        # Build the scene
        self.play(
            FadeIn(baseline),
            FadeIn(fig_left),
            FadeIn(fig_right),
            FadeIn(roosevelt),
            run_time=0.8
        )
        # ELEVATION chip appears with connecting line
        self.play(
            FadeIn(elev_chip, shift=LEFT * 0.4),
            Create(elev_arrow_line),
            run_time=0.8
        )
        # NAMING chip + name label + question marks
        self.play(FadeIn(naming_chip, shift=DOWN * 0.3), run_time=0.6)
        self.play(FadeIn(naming_label), FadeIn(q_l), FadeIn(q_r), run_time=0.7)
        # ARRANGEMENT chip + center dashed line
        self.play(FadeIn(arr_chip, shift=UP * 0.3), run_time=0.6)
        self.play(Create(ctr_line), FadeIn(ctr_label), run_time=0.7)
        self.wait(max(0.4, total - 4.2))


class B09_ProseVsBronze(Scene):
    """THE IMPLICATION — two-column comparison:
    IN PROSE / IN BRONZE — the same argumentative moves."""

    def construct(self):
        total = DUR["B09"]

        divider = Line(UP * 3.2, DOWN * 3.2, color=SLATE, stroke_width=1.5)
        divider.move_to(ORIGIN)

        left_head = SerifLabel("in prose", INK, size=28)
        left_head.move_to(UP * 3.0 + LEFT * 3.0)
        right_head = SerifLabel("in bronze", CRIMSON, size=28)
        right_head.move_to(UP * 3.0 + RIGHT * 3.0)

        # Row pairs: prose concept | bronze equivalent
        rows = [
            ("who gets named", "Roosevelt labeled"),
            ("who gets abstracted", "two left unnamed"),
            ("what is foregrounded", "mounted, centered"),
            ("what is peripheral", "lateral, on foot"),
        ]

        left_items = VGroup()
        right_items = VGroup()
        for prose_t, bronze_t in rows:
            li = Text(prose_t, font=SERIF, color=INK, font_size=26, slant=ITALIC)
            ri = Text(bronze_t, font=SERIF, color=INK, font_size=26, slant=ITALIC)
            left_items.add(li)
            right_items.add(ri)

        left_items.arrange(DOWN, aligned_edge=LEFT, buff=0.52)
        left_items.move_to(LEFT * 3.1 + DOWN * 0.2)
        right_items.arrange(DOWN, aligned_edge=LEFT, buff=0.52)
        right_items.move_to(RIGHT * 2.8 + DOWN * 0.2)

        # Animate
        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(left_head), FadeIn(right_head), run_time=0.6)
        for li, ri in zip(left_items, right_items):
            self.play(FadeIn(li, shift=RIGHT * 0.3),
                      FadeIn(ri, shift=LEFT * 0.3),
                      run_time=0.55)
        self.wait(max(0.4, total - 0.5 - 0.6 - len(rows) * 0.55))


class B11_Example(Scene):
    """THE EXAMPLE — formal choices annotated with the arguments they produce.
    Two-column annotation diagram: formal choice (left) -> argument claim (right)."""

    def construct(self):
        total = DUR["B11"]

        # Small three-figure diagram at top
        roo_c = UP * 2.6 + LEFT * 0.0
        left_c = UP * 1.1 + LEFT * 2.8
        right_c = UP * 1.1 + RIGHT * 2.8

        roo_fig = _horse_and_rider(roo_c, color=INK)
        roo_fig.scale(0.7)
        roo_fig.move_to(roo_c)
        fig_l = _figure_silhouette(left_c, height=0.9, color=INK)
        fig_r = _figure_silhouette(right_c, height=0.9, color=INK)

        # Annotation pairs: formal choice -> argument
        pairs = [
            ("named, mounted, centered", "DOMINANCE"),
            ("unnamed, on foot, lateral", "SUBORDINATION"),
        ]

        arrow_y = [UP * 0.2, DOWN * 1.1]

        pair_groups = VGroup()
        for (choice, claim), y in zip(pairs, arrow_y):
            choice_t = Text(choice, font=SERIF, color=INK, font_size=26, slant=ITALIC)
            claim_chip = LabelChip(claim, accent=CRIMSON, size=24)

            choice_t.move_to(y + LEFT * 2.5)
            claim_chip.move_to(y + RIGHT * 2.8)

            arr = Arrow(
                choice_t.get_right() + RIGHT * 0.15,
                claim_chip.get_left() + LEFT * 0.15,
                color=CRIMSON, stroke_width=2.0, buff=0.0,
                max_tip_length_to_length_ratio=0.18
            )

            pair_groups.add(VGroup(choice_t, arr, claim_chip))

        # horizontal divider between the two claims
        div = DashedLine(LEFT * 6.0 + DOWN * 0.45,
                         RIGHT * 6.0 + DOWN * 0.45,
                         color=SLATE, stroke_width=1.2, dash_length=0.2)

        # "illustrative" footnote
        illus = Text("illustrative re-reading of the Roosevelt composition",
                     font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        illus.to_edge(DOWN, buff=0.5)

        self.play(
            FadeIn(roo_fig, scale=0.85),
            FadeIn(fig_l, scale=0.85),
            FadeIn(fig_r, scale=0.85),
            run_time=0.8
        )
        self.play(
            FadeIn(pair_groups[0][0]),
            Create(pair_groups[0][1]),
            FadeIn(pair_groups[0][2], shift=LEFT * 0.3),
            run_time=0.9
        )
        self.play(Create(div), run_time=0.4)
        self.play(
            FadeIn(pair_groups[1][0]),
            Create(pair_groups[1][1]),
            FadeIn(pair_groups[1][2], shift=LEFT * 0.3),
            run_time=0.9
        )
        self.play(FadeIn(illus, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.4, total - 3.5))


class B12_Practice(Scene):
    """THE PRACTICE — three diagnostic questions appear as a vertical list,
    one at a time, as the narration names each step."""

    def construct(self):
        total = DUR["B12"]

        header = SerifLabel("Analyze any image:", INK, size=30)
        header.to_edge(UP, buff=1.0).shift(LEFT * 3.0)

        questions = [
            ("1.", "What is visible?", "description — name without interpreting"),
            ("2.", "What do formal choices do?", "elevation, naming, arrangement"),
            ("3.", "Where is the argument?", "the composition tells you"),
        ]

        q_groups = VGroup()
        for num, q, sub in questions:
            n_t = Text(num, font=MONO, color=CRIMSON, font_size=32)
            q_t = Text(q, font=DISPLAY, color=INK, font_size=30, weight="MEDIUM")
            s_t = Text(sub, font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
            row = VGroup(n_t, q_t).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
            block = VGroup(row, s_t).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
            q_groups.add(block)

        q_groups.arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        q_groups.move_to(ORIGIN + DOWN * 0.15)

        self.play(FadeIn(header, shift=RIGHT * 0.3), run_time=0.6)
        for qg in q_groups:
            self.play(FadeIn(qg, shift=UP * 0.25), run_time=0.7)
        self.wait(max(0.4, total - 0.6 - len(q_groups) * 0.7))


class B13_End(Scene):
    """RECAP endcard."""

    def construct(self):
        total = DUR["B13"]
        kicker = LabelChip("WRITING", accent=CRIMSON, size=22)
        kicker.to_edge(UP, buff=0.85)

        q_line = Text("How does composition make an argument?",
                      font=SERIF, color=SLATE, font_size=28, slant=ITALIC)
        a_line = Text("The argument is in the arrangement.",
                      font=DISPLAY, color=INK, font_size=48, weight="MEDIUM")
        block = VGroup(q_line, a_line).arrange(DOWN, buff=0.35)
        block.move_to(ORIGIN + DOWN * 0.1)

        u = Line(a_line.get_corner(DL) + DOWN * 0.18,
                 a_line.get_corner(DR) + DOWN * 0.18,
                 color=CRIMSON, stroke_width=2.5)

        self.play(FadeIn(kicker, shift=DOWN * 0.2), run_time=0.5)
        self.play(FadeIn(q_line, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(a_line, shift=UP * 0.2), Create(u), run_time=0.9)
        self.wait(max(0.5, total - 2.1))
