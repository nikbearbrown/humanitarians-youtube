"""
scenes.py — claude-liam-cwc-workshop-how-we-claude-code
How Anthropic Actually Builds Products with Claude.
Source: Anthropic CwC Workshop — how-we-claude-code

Palette: Claude brand
  PAGE   #FAF9F5  cream ground
  INK    #3D3929  warm near-black
  SPARK  #D97757  terracotta — ONE accent per beat
  SOFT   #73705F  secondary text
  GHOST  #A9A491  caption / ghost text
  BORDER #E5E2D9  subtle divider

Render:
  manim -qh --fps 30 -r 1920,1080 scenes.py B01_ThreePhases
  mv media/videos/scenes/*/B01_ThreePhases.mp4 manim/B01.mp4
  manim -qh --fps 30 -r 1920,1080 scenes.py B02_FourDirections
  mv media/videos/scenes/*/B02_FourDirections.mp4 manim/B02.mp4
  manim -qh --fps 30 -r 1920,1080 scenes.py B03_VerificationMatrix
  mv media/videos/scenes/*/B03_VerificationMatrix.mp4 manim/B03.mp4
"""

from manim import *

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE


def source_caption(scene):
    cap = Text(
        "After Anthropic CwC Workshop — how-we-claude-code",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_ThreePhases(Scene):
    def construct(self):
        dur = 18.5

        title = Text("Three Phases. No Code Until Phase Three.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        phases = [
            ("Phase 1", "Interview &\nBrainstorm", "Claude interviews\nyou as a user.\nOutputs a spec.", INK),
            ("Phase 2", "Design\nDirections", "Four static HTML\nmockups with\ndifferent philosophies.", INK),
            ("Phase 3", "Verifiable\nArchitecture", "DOM contracts +\ntest runner.\nbun run verify.", SPARK),
        ]

        col_xs = [-4.2, 0.0, 4.2]
        boxes = []
        for (num, label, detail, col), x in zip(phases, col_xs):
            box = RoundedRectangle(
                width=3.6, height=3.8, corner_radius=0.2,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
            ).move_to([x, -0.4, 0])
            num_txt = Text(num, font_size=17, color=col)
            num_txt.next_to(box, UP, buff=-3.5).shift(LEFT * 1.2)
            lbl_txt = Text(label, font_size=22, color=col, weight=BOLD)
            lbl_txt.move_to(box).shift(UP * 0.9)
            detail_txt = Text(detail, font_size=17, color=SOFT)
            detail_txt.move_to(box).shift(DOWN * 0.4)
            boxes.append(VGroup(box, num_txt, lbl_txt, detail_txt))

        # Arrows between boxes
        arr1 = Arrow(boxes[0].get_right() + RIGHT * 0.05, boxes[1].get_left() + LEFT * 0.05,
                     color=GHOST, stroke_width=2, buff=0.05)
        arr2 = Arrow(boxes[1].get_right() + RIGHT * 0.05, boxes[2].get_left() + LEFT * 0.05,
                     color=GHOST, stroke_width=2, buff=0.05)

        callout = Text("The verification surface is what you audit — not the code.", font_size=20, color=SPARK, weight=BOLD)
        callout.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(boxes[0]), run_time=0.6)
        self.play(GrowArrow(arr1), run_time=0.5)
        self.play(FadeIn(boxes[1]), run_time=0.6)
        self.play(GrowArrow(arr2), run_time=0.5)
        self.play(FadeIn(boxes[2]), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(callout), run_time=0.6)
        self.wait(dur - 6.1)


class B02_FourDirections(Scene):
    def construct(self):
        dur = 20.0

        title = Text("Phase 2: Four Divergent Design Directions.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        directions = [
            ("A", "Flat Minimal", "Clean type,\nno chrome,\nno gradients."),
            ("B", "Card-Based", "Grouped data,\nborder shadows,\nexpandable rows."),
            ("C", "Dashboard", "Summary at top,\ntable below,\nstatus badges."),
            ("D", "Mobile-First", "Single column,\nbig tap targets,\nlarge type."),
        ]

        positions = [
            [-4.0, 1.4],
            [0.8, 1.4],
            [-4.0, -1.8],
            [0.8, -1.8],
        ]

        for (letter, label, detail), (x, y) in zip(directions, positions):
            is_spark = letter == "C"
            box_col = SPARK if is_spark else BORDER
            box = Rectangle(
                width=4.6, height=2.6, color=box_col,
                fill_color=PAGE, fill_opacity=1, stroke_width=1.8
            ).move_to([x, y, 0])
            letter_txt = Text(letter, font_size=26, color=box_col, weight=BOLD)
            letter_txt.move_to(box).shift(UP * 0.75 + LEFT * 1.7)
            lbl_txt = Text(label, font_size=20, color=INK, weight=BOLD)
            lbl_txt.move_to(box).shift(UP * 0.75 + RIGHT * 0.1)
            detail_txt = Text(detail, font_size=16, color=SOFT)
            detail_txt.move_to(box).shift(DOWN * 0.2)
            grp = VGroup(box, letter_txt, lbl_txt, detail_txt)
            self.play(FadeIn(grp), run_time=0.5)

        note = Text("Static HTML mockups — cheap bets on visual philosophy.", font_size=19, color=SOFT)
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(dur - 4.5)


class B03_VerificationMatrix(Scene):
    def construct(self):
        dur = 20.4

        title = Text("Phase 3: Machine-Readable DOM Contracts.", font_size=36, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Table headers
        col_xs = [-4.5, 0.5, 4.0]
        hdrs = ["Component", "Invariant", "Status"]
        hdr_cols = [INK, INK, INK]

        for hdr, x, c in zip(hdrs, col_xs, hdr_cols):
            h = Text(hdr, font_size=20, color=c, weight=BOLD)
            h.move_to([x, 2.0, 0])
            self.add(h)

        divider = Line(LEFT * 6.5, RIGHT * 6.5, color=BORDER, stroke_width=1.5).shift(UP * 1.65)
        self.add(divider)

        rows = [
            ("SplitTotal", "sum(splits) == total", "PASS"),
            ("ParticipantRow", "name ≠ empty, amount > 0", "PASS"),
            ("AddButton", "click → new row appended", "PASS"),
            ("ErrorBanner", "shown iff total mismatch", "FAIL"),
        ]

        row_ys = [1.1, 0.2, -0.7, -1.6]
        status_colors = {"PASS": INK, "FAIL": SPARK}

        for (comp, inv, status), y in zip(rows, row_ys):
            c_txt = Text(comp, font_size=17, color=INK)
            c_txt.move_to([col_xs[0], y, 0])
            i_txt = Text(inv, font_size=16, color=SOFT)
            i_txt.move_to([col_xs[1], y, 0])
            s_col = status_colors[status]
            s_txt = Text(status, font_size=17, color=s_col, weight=BOLD)
            s_txt.move_to([col_xs[2], y, 0])
            self.play(Write(c_txt), Write(i_txt), run_time=0.4)
            self.play(FadeIn(s_txt), run_time=0.3)
            self.wait(0.15)

        # Highlight FAIL row
        fail_bg = Rectangle(
            width=13.0, height=0.6, color=SPARK,
            fill_color=SPARK, fill_opacity=0.12, stroke_width=1.5
        ).move_to([0, -1.6, 0])

        callout = Text("bun run verify — the output is what you audit, not the code.", font_size=20, color=SPARK, weight=BOLD)
        callout.to_edge(DOWN, buff=0.55)

        self.play(Create(fail_bg), run_time=0.5)
        self.play(FadeIn(callout), run_time=0.5)
        self.wait(dur - 7.0)
