"""scenes.py — Manim scenes for 'What is Brutalist?' (what-is-brutalist)

One Scene subclass per GRAPHIC beat with shot.source == 'own'.
Beats: B00B, B01, B02, B03, B05, B06, B07, B08, B08B, B09, B11, B14.
Palette: teardown — flat white GROUND, ink INK, red CRIMSON, teal TEAL.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
from animated_graphics import *
import numpy as np

# ── teardown palette (imported from animated_graphics, duplicated here for clarity)
# GROUND = "#FFFFFF" · INK = "#2A1A0E" · CRIMSON = "#C8102E" · TEAL = "#1F6F5C" (in teardown TEAL==INK)
# Per the palette registry: TEAL = "#2A1A0E" in teardown. We use the beat-sheet teal #1F6F5C as ACCENT_TEAL.
ACCENT_TEAL = "#1F6F5C"   # "good/kept" — only for beats that call for it


# ──────────────────────────────────────────────────────────
# B00B — REVIEW LABEL (17s)
# Explains the small review label visible in every beat.
# ──────────────────────────────────────────────────────────
class B00B_ReviewLabel(Scene):
    LABEL_STR = "B01  MANIM  FILLED   9.5s  +9.4s"

    def construct(self):
        # Section chip (UL)
        section = LabelChip("REVIEW LABEL", accent=ACCENT_TEAL, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Mock video-frame border — represents one beat's clip
        frame = Rectangle(
            width=10.2, height=5.75,
            fill_color="#F5F5F5", fill_opacity=1,
            stroke_color="#BBBBBB", stroke_width=1.5,
        ).move_to(ORIGIN + DOWN * 0.15)
        frame_label = Text("(video frame)", font=SERIF, color="#BBBBBB", font_size=22)
        frame_label.move_to(frame.get_center())
        self.play(FadeIn(frame), FadeIn(frame_label), run_time=0.6)

        # Review label chip — dark semi-transparent, white text, lower-left of frame
        lbl_txt = Text(self.LABEL_STR, font=MONO, font_size=17, color=WHITE)
        lbl_bg = Rectangle(
            width=lbl_txt.width + 0.26,
            height=lbl_txt.height + 0.18,
            fill_color="#000000", fill_opacity=0.62,
            stroke_width=0,
        )
        lbl_bg.move_to(lbl_txt)
        chip = VGroup(lbl_bg, lbl_txt)
        chip.move_to(
            frame.get_corner(DL)
            + RIGHT * (chip.width / 2 + 0.18)
            + UP   * (chip.height / 2 + 0.18)
        )
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(0.4)

        # Highlight ring around the chip
        ring = Ellipse(
            width=chip.width + 0.52, height=chip.height + 0.48,
            stroke_color=CRIMSON, stroke_width=3, fill_opacity=0,
        ).move_to(chip)
        self.play(Create(ring), run_time=0.7)
        self.wait(0.3)

        # Fade out the mock frame; bring chip + ring to center-left for callout phase
        target_center = LEFT * 1.8 + UP * 1.4
        chip_target = chip.copy().scale(1.55).move_to(target_center)
        ring_target = ring.copy().scale(1.55).move_to(target_center)
        self.play(
            FadeOut(frame), FadeOut(frame_label), FadeOut(section),
            Transform(chip, chip_target),
            Transform(ring, ring_target),
            run_time=0.7,
        )
        self.wait(0.2)

        # Callout boxes: each field in the label explained
        # Fields: "B01" | "MANIM" | "FILLED" | "9.5s" | "+9.4s"
        callout_data = [
            ("beat id",          CRIMSON,      LEFT * 1.8 + DOWN * 0.4),
            ("engine\n(Manim / Remotion / AI)", ACCENT_TEAL, LEFT * 4.5 + UP * 0.6),
            ("status",           INK,           RIGHT * 0.6 + UP * 0.0),
            ("start on\ntimeline", "#7A5A3A",  RIGHT * 2.8 + UP * 0.8),
            ("beat\nduration",   "#7A5A3A",    RIGHT * 4.0 + DOWN * 0.4),
        ]

        anchors_x = [-3.45, -2.35, -1.15, -0.1, 0.85]
        chip_y_bottom = chip.get_bottom()[1]

        callout_groups = []
        for i, (caption, color, box_pos) in enumerate(callout_data):
            cap_text = Text(caption, font=SERIF, font_size=20, color=color,
                            line_spacing=0.9)
            cap_box = auto_box(cap_text, h_pad=0.22, v_pad=0.14,
                               fill_color=GROUND, stroke_color=color, stroke_width=2)
            cap_box.move_to(box_pos)
            cap_text.move_to(cap_box)

            anchor = np.array([anchors_x[i], chip_y_bottom, 0])
            box_top = cap_box.get_top()
            line = Line(
                anchor, box_top,
                stroke_color=color, stroke_width=1.5,
            )
            grp = VGroup(line, cap_box, cap_text)
            callout_groups.append(grp)
            self.play(
                Create(line),
                FadeIn(cap_box, shift=UP * 0.12),
                FadeIn(cap_text, shift=UP * 0.12),
                run_time=0.45,
            )

        self.wait(0.8)

        # Summary serif line
        summary = SerifLabel("every beat · labelled · every frame", accent=INK, size=22)
        summary.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(summary), run_time=0.7)
        self.wait(1.2)


# ──────────────────────────────────────────────────────────
# B01 — ONE-CLICK SLOP (8s)
# ──────────────────────────────────────────────────────────
class B01_OneClickSlop(Scene):
    def construct(self):
        # Button
        btn_box = Rectangle(width=3.2, height=1.1, fill_color=GROUND, fill_opacity=1,
                            stroke_color=INK, stroke_width=3)
        btn_lbl = Text("MAKE VIDEO", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        btn_lbl.move_to(btn_box)
        button = VGroup(btn_box, btn_lbl).move_to(UP * 1.2)

        # Filmstrip (3 frames side by side)
        frames = []
        for i in range(3):
            f = Rectangle(width=1.1, height=1.5, fill_color="#EEEEEE", fill_opacity=1,
                          stroke_color=INK, stroke_width=1.5)
            # sprocket holes top + bottom
            for dy in [0.6, -0.6]:
                hole = Rectangle(width=0.18, height=0.22, fill_color=INK, fill_opacity=1,
                                 stroke_width=0)
                hole.move_to(f.get_center() + np.array([0, dy, 0]))
                f = VGroup(f, hole)
            frames.append(f)
        filmstrip = VGroup(*frames).arrange(RIGHT, buff=0.08).move_to(DOWN * 0.5)

        # Red SLOP stamp
        slop_lbl = Text("SLOP", font=DISPLAY, color=CRIMSON, font_size=72, weight=BOLD,
                         slant=ITALIC)
        slop_line = Line(slop_lbl.get_corner(DL) + DOWN * 0.08,
                         slop_lbl.get_corner(DR) + DOWN * 0.08,
                         stroke_width=4, color=CRIMSON)
        slop = VGroup(slop_lbl, slop_line).move_to(DOWN * 0.5).rotate(-0.2)

        # Animate
        self.play(FadeIn(button, shift=DOWN * 0.2), run_time=0.7)
        self.wait(0.5)
        # Button click — brief scale-down
        self.play(button.animate.scale(0.92), run_time=0.2)
        self.play(button.animate.scale(1.0 / 0.92), run_time=0.15)
        # Filmstrip drops out
        self.play(FadeIn(filmstrip, shift=UP * 0.3), run_time=0.8)
        self.wait(0.8)
        # Stamp lands
        slop.scale(0.01)
        self.play(slop.animate.scale(100), run_time=0.5)
        self.wait(3.3)


# ──────────────────────────────────────────────────────────
# B02 — CANNOT WATCH (8s)
# ──────────────────────────────────────────────────────────
class B02_CannotWatch(Scene):
    def construct(self):
        # Screen (right side)
        screen = Rectangle(width=3.0, height=2.0, fill_color="#1A1A1A", fill_opacity=1,
                            stroke_color=INK, stroke_width=2).shift(RIGHT * 2.8)
        # inner content bars (suggesting a playing video)
        for i, col in enumerate(["#C8102E", "#EEEEEE", "#555555"]):
            bar = Rectangle(width=2.4, height=0.3, fill_color=col, fill_opacity=0.7,
                             stroke_width=0)
            bar.move_to(screen.get_center() + UP * (0.4 - i * 0.4))
            screen.add(bar)
        screen_lbl = Text("video", font=SERIF, color="#AAAAAA", font_size=22, slant=ITALIC)
        screen_lbl.move_to(screen.get_center() + DOWN * 0.75)
        screen = VGroup(screen, screen_lbl)

        # AI node (left side) — circle with "AI" label
        ai_circle = Circle(radius=0.7, fill_color=GROUND, fill_opacity=1,
                           stroke_color=INK, stroke_width=2.5).shift(LEFT * 2.8)
        ai_lbl = Text("AI", font=DISPLAY, color=INK, font_size=34, weight=BOLD)
        ai_lbl.move_to(ai_circle)

        # Eye crossed out (small, on the AI node)
        eye_outer = Ellipse(width=0.5, height=0.3, stroke_color=SLATE, stroke_width=2)
        eye_dot = Dot(radius=0.08, color=SLATE)
        eye = VGroup(eye_outer, eye_dot).next_to(ai_circle, UP, buff=0.05)
        cross1 = Line(eye.get_corner(UL), eye.get_corner(DR), stroke_color=CRIMSON, stroke_width=3)
        cross2 = Line(eye.get_corner(UR), eye.get_corner(DL), stroke_color=CRIMSON, stroke_width=3)
        eye_crossed = VGroup(eye, cross1, cross2)

        ai_node = VGroup(ai_circle, ai_lbl, eye_crossed)

        # Dashed line that "never connects" — stops short of screen
        dash_start = ai_circle.get_right() + RIGHT * 0.1
        dash_end   = screen[0].get_left() + LEFT * 0.6
        dashed = DashedLine(dash_start, dash_end, dash_length=0.22,
                            dashed_ratio=0.5, stroke_color=SLATE, stroke_width=2)

        # Animate
        self.play(FadeIn(ai_node, shift=RIGHT * 0.2), run_time=0.8)
        self.play(FadeIn(screen, shift=LEFT * 0.2), run_time=0.8)
        self.wait(0.6)
        self.play(Create(dashed), run_time=1.0)
        self.wait(4.8)


# ──────────────────────────────────────────────────────────
# B03 — TASTE GAPS (11s)
# ──────────────────────────────────────────────────────────
class B03_TasteGaps(Scene):
    def construct(self):
        questions = ["funny?", "interesting?", "did it land?"]
        cards = VGroup()
        for q in questions:
            checkbox = Square(side_length=0.32, stroke_color=INK, stroke_width=2,
                              fill_opacity=0)
            label = Text(q, font=SERIF, color=INK, font_size=32, slant=ITALIC)
            row = VGroup(checkbox, label).arrange(RIGHT, buff=0.25)
            # auto_box: card grows to fit the question text
            box = auto_box(row, h_pad=0.30, v_pad=0.26,
                           fill_color=GROUND, stroke_color=INK, stroke_width=2)
            card = VGroup(box, checkbox, label)
            cards.add(card)

        cards.arrange(DOWN, buff=0.35).move_to(LEFT * 0.8)

        # Human checkmark group (to be revealed on each card)
        checks = VGroup()
        for card in cards:
            checkbox = card[1]
            chk = Text("✓", font=DISPLAY, color=ACCENT_TEAL, font_size=28, weight=BOLD)
            chk.move_to(checkbox.get_center())
            checks.add(chk)

        # Human silhouette label (simple text stand-in)
        human_lbl = Text("human", font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        human_lbl.to_edge(RIGHT, buff=1.2)

        self.play(FadeIn(human_lbl), run_time=0.5)
        for i, (card, chk) in enumerate(zip(cards, checks)):
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.7)
            self.wait(0.6)
            self.play(FadeIn(chk, scale=1.3), run_time=0.5)
            self.wait(0.5)
        self.wait(3.2)


# ──────────────────────────────────────────────────────────
# B05 — TWENTY-HOUR BUG (11s)
# ──────────────────────────────────────────────────────────
class B05_TwentyHourBug(Scene):
    def construct(self):
        # Left: human + clock + red error
        clock_lbl = Text("20:00:00", font="PT Mono", color=INK, font_size=52, weight=BOLD)
        clock_lbl.shift(LEFT * 3.2 + UP * 1.2)
        clock_sub = Text("human, debugging", font=SERIF, color=SLATE, font_size=22)
        clock_sub.next_to(clock_lbl, DOWN, buff=0.2)

        error_line = Rectangle(width=2.8, height=0.38, fill_color=CRIMSON, fill_opacity=0.12,
                                stroke_color=CRIMSON, stroke_width=2)
        error_line.next_to(clock_sub, DOWN, buff=0.4)
        error_text = Text("ERROR: render failed", font="PT Mono", color=CRIMSON, font_size=18)
        error_text.move_to(error_line)
        human_side = VGroup(clock_lbl, clock_sub, error_line, error_text)

        # Divider
        divider = Line(UP * 3, DOWN * 3, stroke_color=HAIRLINE, stroke_width=2)

        # Right: machine — resolves fast
        machine_lbl = Text("0:00:03", font="PT Mono", color=INK, font_size=52, weight=BOLD)
        machine_lbl.shift(RIGHT * 3.2 + UP * 1.2)
        machine_sub = Text("machine, fixed", font=SERIF, color=ACCENT_TEAL, font_size=22)
        machine_sub.next_to(machine_lbl, DOWN, buff=0.2)
        ok_chip = LabelChip("OK", accent=ACCENT_TEAL, size=22)
        ok_chip.next_to(machine_sub, DOWN, buff=0.4)
        machine_side = VGroup(machine_lbl, machine_sub, ok_chip)

        # Waste bar under human side (red, draining)
        waste_bar_bg = Rectangle(width=2.8, height=0.22, fill_color=HAIRLINE, fill_opacity=1,
                                  stroke_width=0)
        waste_bar_bg.next_to(human_side, DOWN, buff=0.5)
        waste_bar = Rectangle(width=2.8, height=0.22, fill_color=CRIMSON, fill_opacity=0.7,
                               stroke_width=0)
        waste_bar.align_to(waste_bar_bg, LEFT).align_to(waste_bar_bg, UP)
        waste_lbl = Text("wasted time", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
        waste_lbl.next_to(waste_bar_bg, DOWN, buff=0.1)

        self.play(FadeIn(human_side), Create(divider), FadeIn(machine_side), run_time=1.0)
        self.wait(1.0)
        self.play(FadeIn(waste_bar_bg), FadeIn(waste_bar), FadeIn(waste_lbl), run_time=0.6)
        self.wait(1.0)
        # Drain the waste bar (transform to near-zero width, pinned left)
        empty = Rectangle(width=0.01, height=0.22, fill_color=CRIMSON, fill_opacity=0.7,
                          stroke_width=0)
        empty.align_to(waste_bar_bg, LEFT).align_to(waste_bar_bg, UP)
        self.play(Transform(waste_bar, empty), run_time=2.5)
        self.wait(4.9)


# ──────────────────────────────────────────────────────────
# B06 — TWO FAILURE MODES (14s)
# ──────────────────────────────────────────────────────────
class B06_TwoFailureModes(Scene):
    def construct(self):
        # Balance beam: horizontal bar pivoting on a fulcrum
        pivot = Triangle(fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.35)
        pivot.move_to(DOWN * 1.8)
        beam = Line(LEFT * 4.5, RIGHT * 4.5, stroke_color=INK, stroke_width=4)
        beam.move_to(DOWN * 1.1)

        # Left pan label: "all human" sinking
        left_pan_lbl = Text("all human\n(time-sink)", font=SERIF, color=INK, font_size=26,
                            line_spacing=0.8)
        left_pan_lbl.move_to(LEFT * 3.5 + UP * 0.4)

        # Clock icons on left — three tiny rectangles
        clocks = VGroup()
        for i in range(3):
            c = Rectangle(width=0.4, height=0.4, stroke_color=INK, stroke_width=1.5,
                          fill_opacity=0)
            c.move_to(LEFT * (3.5 + i * 0.5 - 0.5) + DOWN * 0.4)
            clocks.add(c)

        # Right pan label: "all machine" SLOP
        right_pan_lbl = Text("all machine\n(AI slop)", font=SERIF, color=INK, font_size=26,
                              line_spacing=0.8)
        right_pan_lbl.move_to(RIGHT * 3.5 + UP * 0.4)

        slop_chip = LabelChip("SLOP", accent=CRIMSON, size=24)
        slop_chip.move_to(RIGHT * 3.5 + DOWN * 0.45)

        # Left side sinks: beam tilts left
        left_group = VGroup(left_pan_lbl, clocks)
        right_group = VGroup(right_pan_lbl, slop_chip)

        # Middle marker: "here" in teal
        middle_arrow = Arrow(UP * 0.5, DOWN * 0.1, stroke_color=ACCENT_TEAL, stroke_width=4,
                              tip_length=0.25).move_to(UP * 0.4)
        middle_lbl = LabelChip("BRUTALIST", accent=ACCENT_TEAL, size=22)
        middle_lbl.next_to(middle_arrow, UP, buff=0.15)

        self.play(Create(beam), FadeIn(pivot), run_time=0.7)
        self.play(FadeIn(left_group, shift=DOWN * 0.2), run_time=0.8)
        self.wait(0.6)
        self.play(FadeIn(right_group, shift=DOWN * 0.2), run_time=0.8)
        self.wait(0.8)
        # Tilt left (left side heavy)
        self.play(
            beam.animate.rotate(-0.18, about_point=beam.get_center()),
            left_group.animate.shift(DOWN * 0.4),
            right_group.animate.shift(UP * 0.3),
            run_time=1.2
        )
        self.wait(1.5)
        # Show the middle balance point
        self.play(FadeIn(middle_arrow, shift=DOWN * 0.1), FadeIn(middle_lbl), run_time=0.8)
        self.wait(5.8)


# ──────────────────────────────────────────────────────────
# B07 — YOU ARE THE CONDUCTOR (7s)  ← HERO BEAT
# ──────────────────────────────────────────────────────────
class B07_YouAreTheConductor(Scene):
    def construct(self):
        # Dark canvas for this hero beat
        self.camera.background_color = "#2A1A0E"

        # Baton stroke — a confident horizontal line drawn across the canvas
        baton = Line(LEFT * 5.5, RIGHT * 5.5, stroke_color=WHITE, stroke_width=6)
        baton.shift(UP * 0.8)

        # Title in EB Garamond
        title = Text("YOU ARE THE CONDUCTOR", font=SERIF, color=WHITE,
                     font_size=54, weight=BOLD)
        title.move_to(ORIGIN)

        # Red underline accent
        underline = Line(title.get_corner(DL) + DOWN * 0.1,
                         title.get_corner(DR) + DOWN * 0.1,
                         stroke_color=CRIMSON, stroke_width=5)

        # Faint tool labels below (the orchestra)
        tools = ["Manim", "Remotion", "ffmpeg"]
        tool_row = VGroup(*[
            Text(t, font=DISPLAY, color=WHITE, font_size=20, weight="MEDIUM")
            for t in tools
        ]).arrange(RIGHT, buff=1.4)
        tool_row.shift(DOWN * 1.8).set_opacity(0.35)

        # Animate: baton stroke first, then title resolves
        self.play(Create(baton), run_time=0.9)
        self.wait(0.2)
        self.play(Write(title), run_time=1.1)
        self.play(Create(underline), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(tool_row, shift=UP * 0.1), run_time=0.7)
        self.wait(3.3)


# ──────────────────────────────────────────────────────────
# B08 — THE SCORE AND THE PLAYING (13s)
# ──────────────────────────────────────────────────────────
class B08_ScoreAndPlaying(Scene):
    def construct(self):
        # Vertical divider
        divider = Line(UP * 3.2, DOWN * 3.2, stroke_color=HAIRLINE, stroke_width=2)

        # LEFT: score (annotated staff lines)
        score_lbl = SerifLabel("the score is yours", accent=CRIMSON, size=28)
        score_lbl.move_to(LEFT * 3.2 + UP * 2.2)

        staff_lines = VGroup(*[
            Line(LEFT * 5.2, ORIGIN + LEFT * 0.3,
                 stroke_color=INK, stroke_width=1.2).shift(UP * (0.8 - i * 0.4))
            for i in range(5)
        ])

        # Red circle on one line (the wrong note)
        wrong_note = Circle(radius=0.22, stroke_color=CRIMSON, stroke_width=3, fill_opacity=0)
        wrong_note.move_to(LEFT * 2.8 + UP * 0.4)

        # Hand annotation mark (a short red mark)
        annotation = Text("✗", font=DISPLAY, color=CRIMSON, font_size=36)
        annotation.next_to(wrong_note, UP, buff=0.1)

        left_group = VGroup(score_lbl, staff_lines, wrong_note, annotation)

        # RIGHT: tool-orchestra playing
        play_lbl = SerifLabel("the playing is its", accent=ACCENT_TEAL, size=28)
        play_lbl.move_to(RIGHT * 3.2 + UP * 2.2)

        tools = [("Manim", "animations"), ("Remotion", "graphics"), ("ffmpeg", "cuts")]
        tool_cards = VGroup()
        for i, (tool, role) in enumerate(tools):
            t = Text(tool, font=DISPLAY, color=INK, font_size=22, weight=BOLD)
            r = Text(role, font=SERIF, color=SLATE, font_size=18)
            content = VGroup(t, r).arrange(RIGHT, buff=0.25)
            # auto_box sizes the card to fit the text — fixes the narrow-box bug
            card = auto_box(content, h_pad=0.28, v_pad=0.16,
                            fill_color="#F5F5F5", stroke_color=INK, stroke_width=1)
            tc = VGroup(card, content).shift(RIGHT * 3.2 + UP * (0.6 - i * 0.85))
            tool_cards.add(tc)

        # Baton arrow from left to right
        baton_arrow = Arrow(LEFT * 0.3, RIGHT * 0.3, stroke_color=ACCENT_TEAL,
                            stroke_width=4, tip_length=0.3).move_to(UP * 0.1)

        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(left_group, shift=RIGHT * 0.2), FadeIn(play_lbl), run_time=1.0)
        self.wait(0.6)
        self.play(LaggedStart(*[FadeIn(tc, shift=LEFT * 0.2) for tc in tool_cards],
                               lag_ratio=0.3, run_time=1.4))
        self.wait(0.8)
        self.play(GrowArrow(baton_arrow), run_time=0.8)
        self.wait(7.0)


# ──────────────────────────────────────────────────────────
# B08B — FIX THE BOXES (14s)  ← the conductor loop, live
# ──────────────────────────────────────────────────────────
class B08B_FixTheBoxes(Scene):
    """Demonstrates the conductor loop: human spots a wrong note (narrow box),
    gives a plain-language instruction, machine fixes it on-screen."""

    # Shared geometry for the "before" and "after" card
    TOOL = "Remotion"
    ROLE = "graphics"
    FONT_SZ_TOOL = 22
    FONT_SZ_ROLE = 18
    # The old fixed width that caused the overflow
    OLD_W = 2.4
    OLD_H = 0.6

    def construct(self):
        # ── SECTION LABEL ──────────────────────────────────────
        section = LabelChip("THE CONDUCTOR LOOP", accent=CRIMSON, size=18)
        section.to_corner(UL, buff=0.6)
        self.play(FadeIn(section, shift=DOWN * 0.1), run_time=0.4)

        # ── BEFORE: narrow box, text overflowing ───────────────
        before_lbl = SerifLabel("BEFORE", accent=CRIMSON, size=24)
        before_lbl.move_to(LEFT * 3.8 + UP * 1.8)

        t_before = Text(self.TOOL, font=DISPLAY, color=INK,
                        font_size=self.FONT_SZ_TOOL, weight=BOLD)
        r_before = Text(self.ROLE, font=SERIF, color=SLATE, font_size=self.FONT_SZ_ROLE)
        content_before = VGroup(t_before, r_before).arrange(RIGHT, buff=0.25)
        # The old fixed-width box — does NOT fit the text
        narrow_box = Rectangle(width=self.OLD_W, height=self.OLD_H,
                               fill_color="#F5F5F5", fill_opacity=1,
                               stroke_color=INK, stroke_width=1)
        narrow_box.move_to(LEFT * 3.8 + UP * 0.6)
        content_before.move_to(narrow_box)

        # Red overflow flags: short lines at the left/right edges where text bleeds
        left_flag = Line(narrow_box.get_corner(UL) + LEFT * 0.05,
                         narrow_box.get_corner(DL) + LEFT * 0.05,
                         stroke_color=CRIMSON, stroke_width=4)
        right_flag = Line(narrow_box.get_corner(UR) + RIGHT * 0.05,
                          narrow_box.get_corner(DR) + RIGHT * 0.05,
                          stroke_color=CRIMSON, stroke_width=4)
        overflow_note = Text("text overflows", font=SERIF, color=CRIMSON,
                             font_size=18, slant=ITALIC)
        overflow_note.next_to(narrow_box, DOWN, buff=0.18)

        before_group = VGroup(before_lbl, narrow_box, content_before,
                              left_flag, right_flag, overflow_note)

        self.play(FadeIn(before_lbl, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(narrow_box), FadeIn(content_before), run_time=0.7)
        self.wait(0.5)
        self.play(Create(left_flag), Create(right_flag), run_time=0.6)
        self.play(FadeIn(overflow_note), run_time=0.4)
        self.wait(1.2)

        # ── INSTRUCTION: human's spoken correction ─────────────
        instruction_bg = Rectangle(width=8.5, height=0.72,
                                   fill_color="#FFF8F8", fill_opacity=1,
                                   stroke_color=CRIMSON, stroke_width=1.5)
        instruction_bg.move_to(DOWN * 0.5)
        instruction_txt = Text(
            '"make the boxes wider to hold the text"',
            font=SERIF, color=INK, font_size=24, slant=ITALIC,
        )
        instruction_txt.move_to(instruction_bg)
        speaker_chip = LabelChip("CONDUCTOR", accent=CRIMSON, size=16)
        speaker_chip.next_to(instruction_bg, LEFT, buff=0.2)

        self.play(FadeIn(instruction_bg), FadeIn(instruction_txt),
                  FadeIn(speaker_chip), run_time=0.8)
        self.wait(1.5)

        # ── AFTER: auto-sized box, text fits cleanly ────────────
        after_lbl = SerifLabel("AFTER", accent=ACCENT_TEAL, size=24)
        after_lbl.move_to(RIGHT * 3.8 + UP * 1.8)

        t_after = Text(self.TOOL, font=DISPLAY, color=INK,
                       font_size=self.FONT_SZ_TOOL, weight=BOLD)
        r_after = Text(self.ROLE, font=SERIF, color=INK, font_size=self.FONT_SZ_ROLE)
        content_after = VGroup(t_after, r_after).arrange(RIGHT, buff=0.25)
        # auto_box: sizes to content with consistent padding
        wide_box = auto_box(content_after, h_pad=0.28, v_pad=0.16,
                            fill_color="#F5F5F5", stroke_color=ACCENT_TEAL, stroke_width=2)
        wide_box.move_to(RIGHT * 3.8 + UP * 0.6)
        content_after.move_to(wide_box)

        ok_tick = Text("✓ fits", font=SERIF, color=ACCENT_TEAL, font_size=18)
        ok_tick.next_to(wide_box, DOWN, buff=0.18)

        self.play(FadeIn(after_lbl, shift=LEFT * 0.2), run_time=0.5)
        self.play(FadeIn(wide_box), FadeIn(content_after), run_time=0.6)
        self.play(FadeIn(ok_tick), run_time=0.4)
        self.wait(1.2)

        # ── SUMMARY LINE ────────────────────────────────────────
        summary = SerifLabel("wrong note caught · machine fixed it", accent=INK, size=22)
        summary.move_to(DOWN * 2.2)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.7)
        self.wait(4.0)


# ──────────────────────────────────────────────────────────
# B09 — BEAT SHEET HEART (9s)
# ──────────────────────────────────────────────────────────
class B09_BeatSheetHeart(Scene):
    def construct(self):
        # Build text stack first — box sized to fit at render time
        heart_lbl = Text("beat_sheet.json", font="PT Mono", color=INK, font_size=28, weight=BOLD)
        beat_rows = Text("B01 · B02 · … · B14", font="PT Mono", color=CRIMSON, font_size=18)
        text_stack = VGroup(heart_lbl, beat_rows).arrange(DOWN, buff=0.22)
        heart_box = surround_box(text_stack, buff=0.32,
                                 fill_color=GROUND, stroke_color=CRIMSON, stroke_width=3)
        heart = VGroup(heart_box, text_stack)

        # Three derived views with arrows
        targets = [
            (UP * 2.6, "todo.json", SLATE),
            (RIGHT * 4.8, "STATUS.md", SLATE),
            (DOWN * 2.4, "the cut", ACCENT_TEAL),
        ]
        arrows_and_lbls = VGroup()
        for pos, label, col in targets:
            direction = pos / np.linalg.norm(pos)
            # 2.5 clears the box boundary for any plausible text width
            start = heart_box.get_center() + direction * 2.5
            end = heart_box.get_center() + pos * 0.82
            arr = Arrow(start, end, stroke_color=col, stroke_width=2.5,
                        tip_length=0.22)
            lbl = Text(label, font="PT Mono", color=col, font_size=22)
            lbl.move_to(heart_box.get_center() + pos * 1.0)
            arrows_and_lbls.add(arr, lbl)

        # Pulse animation: heart glows red briefly
        glow = heart_box.copy().set_stroke(CRIMSON, 6).set_fill(opacity=0)

        self.play(FadeIn(heart, scale=0.9), run_time=0.9)
        self.play(Create(glow), glow.animate.set_opacity(0), run_time=0.8)
        self.wait(0.4)
        for i in range(0, len(arrows_and_lbls), 2):
            arr = arrows_and_lbls[i]
            lbl = arrows_and_lbls[i + 1]
            direction = np.array(arr.get_end()) - np.array(arr.get_start())
            norm = np.linalg.norm(direction)
            shift_vec = direction / norm * 0.1 if norm > 0 else np.array([0, 0, 0])
            self.play(GrowArrow(arr), FadeIn(lbl, shift=shift_vec), run_time=0.7)
        self.wait(4.2)


# ──────────────────────────────────────────────────────────
# B11 — REQUEST CARD → PANTRY → CONFORMED CUT (15s)
# ──────────────────────────────────────────────────────────
class B11_RequestCardPantry(Scene):
    def construct(self):
        # Step 1: Request card — arrange contents first, box sized to fit
        card_icon = Text("[ ? ]", font="PT Mono", color=CRIMSON, font_size=40)
        card_lbl = Text("REQUEST CARD", font=DISPLAY, color=CRIMSON, font_size=20, weight=BOLD)
        card_prompt = Text("suggested prompt:", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        card_prompt_text = Text('"archival aerial footage, city"', font="PT Mono",
                                 color=INK, font_size=16)
        card_contents = VGroup(card_icon, card_lbl, card_prompt, card_prompt_text)
        card_contents.arrange(DOWN, buff=0.18)
        card_box = surround_box(card_contents, buff=0.30,
                                fill_color="#FFF8F8", stroke_color=CRIMSON,
                                stroke_width=2.5)
        request_card = VGroup(card_box, card_contents)
        request_card.shift(LEFT * 3.6 + UP * 0.3)

        # Arrow 1: request card → pantry
        arrow1 = Arrow(request_card.get_right() + RIGHT * 0.1,
                       request_card.get_right() + RIGHT * 1.4,
                       stroke_color=INK, stroke_width=2.5, tip_length=0.22)
        arrow1.shift(RIGHT * 0.0)

        # Step 2: Pantry bin
        pantry_box = Rectangle(width=1.8, height=2.2, fill_color="#F0F0F0", fill_opacity=1,
                                stroke_color=INK, stroke_width=2)
        pantry_lbl = Text("pantry/", font="PT Mono", color=SLATE, font_size=20)
        pantry_lbl.next_to(pantry_box, UP, buff=0.18)
        clip = Rectangle(width=1.2, height=0.6, fill_color=ACCENT_TEAL, fill_opacity=0.8,
                          stroke_width=0)
        clip_lbl = Text("clip.mp4", font="PT Mono", color=WHITE, font_size=14)
        clip_lbl.move_to(clip)
        pantry_clip = VGroup(clip, clip_lbl)
        pantry = VGroup(pantry_box, pantry_lbl)
        pantry.move_to(ORIGIN + UP * 0.3)
        arrow1.put_start_and_end_on(request_card.get_right() + RIGHT * 0.15,
                                     pantry.get_left() + LEFT * 0.15)

        # Arrow 2: pantry → timeline
        arrow2 = Arrow(ORIGIN, ORIGIN + RIGHT * 1.5, stroke_color=INK,
                        stroke_width=2.5, tip_length=0.22)

        # Step 3: Timeline slot
        timeline_box = Rectangle(width=3.2, height=0.7, fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=2)
        beat_slot = Rectangle(width=1.2, height=0.5, fill_color=ACCENT_TEAL, fill_opacity=1,
                               stroke_width=0)
        beat_slot_lbl = Text("B11 ✓", font="PT Mono", color=WHITE, font_size=18, weight=BOLD)
        beat_slot_lbl.move_to(beat_slot)
        timeline = VGroup(timeline_box, beat_slot, beat_slot_lbl)
        timeline.shift(RIGHT * 3.8 + UP * 0.3)
        arrow2.put_start_and_end_on(pantry.get_right() + RIGHT * 0.15,
                                     timeline.get_left() + LEFT * 0.15)

        # Step labels
        lbl1 = Text("request card", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        lbl1.next_to(request_card, DOWN, buff=0.35)
        lbl2 = Text("you drop it in", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        lbl2.next_to(pantry, DOWN, buff=0.35)
        lbl3 = Text("auto-conformed", font=SERIF, color=ACCENT_TEAL, font_size=20, slant=ITALIC)
        lbl3.next_to(timeline, DOWN, buff=0.35)

        # Animate
        self.play(FadeIn(request_card, shift=RIGHT * 0.3), FadeIn(lbl1), run_time=0.9)
        self.wait(1.0)
        self.play(GrowArrow(arrow1), run_time=0.6)
        self.play(FadeIn(pantry, shift=LEFT * 0.2), FadeIn(lbl2), run_time=0.7)
        # Clip drops into pantry
        pantry_clip.move_to(pantry_box.get_center() + UP * 1.5)
        self.play(FadeIn(pantry_clip), pantry_clip.animate.move_to(pantry_box.get_center()),
                  run_time=0.8)
        self.wait(0.8)
        self.play(GrowArrow(arrow2), run_time=0.6)
        self.play(FadeIn(timeline, shift=LEFT * 0.2), FadeIn(lbl3), run_time=0.7)
        self.wait(7.2)


# ──────────────────────────────────────────────────────────
# B14 — THE PLAYLIST (14s)
# ──────────────────────────────────────────────────────────
class B14_ThePlaylist(Scene):
    def construct(self):
        playlist_title = SerifLabel("Brutalist — Claude for Video Production", accent=CRIMSON, size=26)
        playlist_title.to_edge(UP, buff=0.7)

        # Playlist entries: title + command
        entries = [
            ("What is Brutalist?",  "./art explainer-video"),
            ("sketch-explainer",    "./art sketch-explainer"),
            ("explainer",           "./art explainer"),
            ("deck-lecture",        "./art deck-lecture"),
            ("music-video",         "./art music-video"),
        ]
        cards = VGroup()
        for title, cmd in entries:
            thumb = Rectangle(width=1.9, height=1.1, fill_color="#EEEEEE", fill_opacity=1,
                              stroke_color=INK, stroke_width=1.5)
            # red play-button triangle inside thumbnail
            tri = Triangle(fill_color=CRIMSON, fill_opacity=0.8, stroke_width=0).scale(0.22)
            tri.move_to(thumb)
            title_txt = Text(title, font=DISPLAY, color=INK, font_size=14, weight=BOLD)
            title_txt.next_to(thumb, DOWN, buff=0.08)
            title_txt.scale_to_fit_width(min(title_txt.width, thumb.width * 0.98))
            cmd_txt = Text(cmd, font="PT Mono", color=CRIMSON, font_size=12)
            cmd_txt.next_to(title_txt, DOWN, buff=0.06)
            card = VGroup(thumb, tri, title_txt, cmd_txt)
            cards.add(card)

        cards.arrange(RIGHT, buff=0.35).move_to(DOWN * 0.6)
        # Center and scale to fit frame
        if cards.width > 13.0:
            cards.scale_to_fit_width(13.0)

        self.play(FadeIn(playlist_title, shift=DOWN * 0.2), run_time=0.7)
        self.wait(0.3)
        self.play(
            LaggedStart(*[FadeIn(card, shift=UP * 0.3) for card in cards],
                         lag_ratio=0.25, run_time=3.5)
        )
        self.wait(9.5)
