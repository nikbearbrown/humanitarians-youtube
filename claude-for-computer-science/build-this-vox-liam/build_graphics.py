"""build_graphics.py — Manim scenes for build-this-vox-kore.

Render each scene and move the output to manim/<beat>.mp4:

  ART_PALETTE=newsprint manim -qh --fps 24 -r 1280,720 build_graphics.py B01_EngineerPool -o manim/B01.mp4
  ART_PALETTE=newsprint manim -qh --fps 24 -r 1280,720 build_graphics.py B02_MatchSpecSupport -o manim/B02.mp4
  ART_PALETTE=newsprint manim -qh --fps 24 -r 1280,720 build_graphics.py B03_PriceCompare -o manim/B03.mp4
  ART_PALETTE=newsprint manim -qh --fps 24 -r 1280,720 build_graphics.py B04_WinWin -o manim/B04.mp4

Durations are GROUND TRUTH from measured Kokoro audio:
  B01 = 12.01s  B02 = 13.44s  B03 = 16.62s  B04 = 7.49s
"""
from manim import *
import os

# ── palette (newsprint vox design tokens)
GROUND   = "#F3EBDD"   # cream
INK      = "#2F2A26"   # charcoal
TEAL     = "#3D5A80"   # dusty navy (good / cheap / grad)
CRIMSON  = "#BF3339"   # bad / expensive / cost
TERRA    = "#D35F43"   # terracotta accent
HAIRLINE = "#D4D4D4"
GOLD     = "#F5D061"

config.background_color = GROUND

SERIF   = "EB Garamond"
DISPLAY = "Montserrat"


# ── shared helpers ─────────────────────────────────────────────────

def ink_text(text, size=0.46, weight=NORMAL, slant=NORMAL, color=INK):
    return Text(text, font=SERIF, font_size=int(size * 48),
                weight=weight, slant=slant, color=color)

def cap_text(text, size=0.38, color=INK):
    return Text(text, font=DISPLAY, font_size=int(size * 48), color=color)

def hairline(width=12.0, stroke=1.2):
    return Line(LEFT * width / 2, RIGHT * width / 2,
                stroke_color=HAIRLINE, stroke_width=stroke)

def label_chip(text, fill=TEAL, text_color=WHITE, size=0.32):
    t = Text(text, font=DISPLAY, font_size=int(size * 48), color=text_color)
    box = RoundedRectangle(width=t.width + 0.4, height=t.height + 0.22,
                           corner_radius=0.08, fill_color=fill,
                           fill_opacity=1, stroke_width=0)
    box.move_to(t)
    return VGroup(box, t)


# ══════════════════════════════════════════════════════════════════════════════
# B01 — Engineer Pool + FAANG timeline  (12.01s)
# Isotype grid of 24 circles; 6 highlight crimson; FAANG timeline bar draws below.
# ══════════════════════════════════════════════════════════════════════════════

class B01_EngineerPool(Scene):
    def construct(self):
        DUR = 12.01

        # ── header
        header = cap_text("The Talent Pool", size=0.52, color=INK).to_edge(UP, buff=0.55)
        hl = hairline().next_to(header, DOWN, buff=0.14)
        self.add(header, hl)

        # ── 24 circles in a 6×4 grid
        N_TOTAL = 24
        N_HIGHLIGHT = 6
        COLS, ROWS = 6, 4
        R = 0.22
        H_GAP = 0.75
        V_GAP = 0.64

        grid_w = (COLS - 1) * H_GAP
        grid_h = (ROWS - 1) * V_GAP
        grid_origin = UP * 0.45 + LEFT * grid_w / 2

        circles = []
        for i in range(N_TOTAL):
            row, col = divmod(i, COLS)
            pos = grid_origin + RIGHT * col * H_GAP + DOWN * row * V_GAP
            c = Circle(radius=R, fill_color=INK, fill_opacity=0.18,
                       stroke_color=INK, stroke_width=2)
            c.move_to(pos)
            circles.append(c)

        # count-up reveal — lag-ratio stagger
        grid_group = VGroup(*circles)
        self.play(LaggedStart(*[FadeIn(c, scale=0.7) for c in circles],
                              lag_ratio=0.06, run_time=3.0))

        # highlight 6 circles (first 6 = top row)
        highlights = VGroup(*circles[:N_HIGHLIGHT])
        self.play(highlights.animate.set_fill(CRIMSON, opacity=0.9)
                                   .set_stroke(CRIMSON, width=2.5),
                  run_time=1.2)

        # label for highlighted
        chip = label_chip("the ones Bear knows", fill=CRIMSON, size=0.28)
        chip.next_to(highlights, RIGHT, buff=0.35).shift(UP * 0.12)
        self.play(FadeIn(chip, shift=LEFT * 0.2), run_time=0.6)

        # ── FAANG timeline bar
        bar_y = DOWN * 2.7
        bar_label = cap_text("FAANG job search", size=0.33, color=INK)
        bar_label.move_to(bar_y + LEFT * 3.2 + UP * 0.05)

        bar_track = Rectangle(width=6.5, height=0.28,
                              fill_color=HAIRLINE, fill_opacity=1, stroke_width=0)
        bar_fill  = Rectangle(width=0.0,  height=0.28,
                              fill_color=TEAL, fill_opacity=1, stroke_width=0)
        bar_track.move_to(bar_y + RIGHT * 0.8)
        bar_fill.move_to(bar_track.get_left()).shift(RIGHT * 0)
        bar_fill.align_to(bar_track, LEFT)

        months_label = cap_text("months", size=0.3, color=TEAL)
        months_label.next_to(bar_track, RIGHT, buff=0.18)

        self.play(FadeIn(bar_label), FadeIn(bar_track), run_time=0.5)
        self.play(
            bar_fill.animate.stretch_to_fit_width(6.5).align_to(bar_track, LEFT),
            run_time=2.0
        )
        self.play(FadeIn(months_label), run_time=0.4)

        # window chip
        window_chip = label_chip("FREE to build → that's the window", fill=TEAL, size=0.27)
        window_chip.next_to(bar_track, DOWN, buff=0.35)
        self.play(FadeIn(window_chip, shift=UP * 0.15), run_time=0.6)

        # hold to duration
        elapsed = 3.0 + 1.2 + 0.6 + 0.5 + 2.0 + 0.4 + 0.6
        hold = max(0.2, DUR - elapsed)
        self.wait(hold)


# ══════════════════════════════════════════════════════════════════════════════
# B02 — Match → Spec → Support  (13.44s)
# Three-column draw-on process map.
# ══════════════════════════════════════════════════════════════════════════════

class B02_MatchSpecSupport(Scene):
    def construct(self):
        DUR = 13.44

        header = cap_text("Not a Job Board", size=0.52, color=INK).to_edge(UP, buff=0.55)
        hl = hairline().next_to(header, DOWN, buff=0.14)
        self.add(header, hl)

        # column layout: three equal columns
        col_x = [-4.2, 0.0, 4.2]
        col_y  = 0.3

        def column(title, sub1, sub2, accent=TEAL):
            head = cap_text(title, size=0.45, color=accent)
            line = Line(LEFT * 0.9, RIGHT * 0.9,
                        stroke_color=accent, stroke_width=2)
            line.next_to(head, DOWN, buff=0.12)
            s1 = ink_text(sub1, size=0.36)
            s2 = ink_text(sub2, size=0.36)
            body = VGroup(s1, s2).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
            body.next_to(line, DOWN, buff=0.28)
            return VGroup(head, line, body)

        col1 = column("MATCH",   "web → web",      "AI → AI")
        col2 = column("SPEC",    "written first",   "before code")
        col3 = column("SUPPORT", "Bear on call",    "when you need it", accent=TERRA)

        col1.move_to([col_x[0], col_y, 0])
        col2.move_to([col_x[1], col_y, 0])
        col3.move_to([col_x[2], col_y, 0])

        # arrows between columns
        def draw_arrow(left_col, right_col):
            start = left_col.get_right() + RIGHT * 0.15
            end   = right_col.get_left()  + LEFT  * 0.15
            return Arrow(start, end, buff=0, stroke_color=INK,
                         stroke_width=2.5, max_tip_length_to_length_ratio=0.15,
                         tip_shape=ArrowTriangleFilledTip)

        arr1 = draw_arrow(col1, col2)
        arr2 = draw_arrow(col2, col3)

        # subtext below columns
        sub = ink_text(
            "So you see exactly what you're paying for.",
            size=0.34, slant=ITALIC, color=INK
        ).to_edge(DOWN, buff=0.7)

        # animate: col1 → arrow → col2 → arrow → col3
        self.play(FadeIn(col1, shift=UP * 0.2), run_time=1.4)
        self.play(GrowArrow(arr1), run_time=0.7)
        self.play(FadeIn(col2, shift=UP * 0.2), run_time=1.4)
        self.play(GrowArrow(arr2), run_time=0.7)
        self.play(FadeIn(col3, shift=UP * 0.2), run_time=1.4)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.7)

        elapsed = 1.4 + 0.7 + 1.4 + 0.7 + 1.4 + 0.7
        self.wait(max(0.2, DUR - elapsed))


# ══════════════════════════════════════════════════════════════════════════════
# B03 — $35/hr vs FAANG cost + hand-off guarantee  (16.62s)
# Two bars grow up; then a hand-off sequence below.
# ══════════════════════════════════════════════════════════════════════════════

class B03_PriceCompare(Scene):
    def construct(self):
        DUR    = 16.62
        FLOOR_Y = -0.3      # y of the floor line
        BAR_W   = 2.0
        MAX_H   = 3.0
        LEFT_X  = -2.6
        RIGHT_X =  2.6

        header = cap_text("The Price — and the Guarantee", size=0.46, color=INK)
        header.to_edge(UP, buff=0.55)
        hl = hairline().next_to(header, DOWN, buff=0.14)
        self.add(header, hl)

        floor = Line(LEFT * 6, RIGHT * 6,
                     stroke_color=INK, stroke_width=1.5)
        floor.move_to([0, FLOOR_Y, 0])
        self.add(floor)

        # bar geometry: bottom edge sits ON the floor
        h_cheap = MAX_H * 0.175
        bar_cheap_top_y = FLOOR_Y + h_cheap
        bar_cheap_cy    = FLOOR_Y + h_cheap / 2

        bar_faang_top_y = FLOOR_Y + MAX_H
        bar_faang_cy    = FLOOR_Y + MAX_H / 2

        bar_cheap = Rectangle(width=BAR_W, height=h_cheap,
                              fill_color=TEAL, fill_opacity=1, stroke_width=0)
        bar_cheap.move_to([LEFT_X, bar_cheap_cy, 0])

        bar_faang = Rectangle(width=BAR_W, height=MAX_H,
                              fill_color=CRIMSON, fill_opacity=1, stroke_width=0)
        bar_faang.move_to([RIGHT_X, bar_faang_cy, 0])

        # start as flat slivers
        bc0 = Rectangle(width=BAR_W, height=0.01,
                        fill_color=TEAL, fill_opacity=1, stroke_width=0)
        bc0.move_to([LEFT_X, FLOOR_Y, 0])
        bf0 = Rectangle(width=BAR_W, height=0.01,
                        fill_color=CRIMSON, fill_opacity=1, stroke_width=0)
        bf0.move_to([RIGHT_X, FLOOR_Y, 0])

        self.add(bc0, bf0)
        self.play(
            Transform(bc0, bar_cheap),
            Transform(bf0, bar_faang),
            run_time=2.5
        )

        lbl_cheap = cap_text("$35 / hr", size=0.44, color=WHITE)
        lbl_cheap.move_to([LEFT_X, bar_cheap_cy, 0])

        lbl_faang = cap_text("$200+ / hr", size=0.44, color=WHITE)
        lbl_faang.move_to([RIGHT_X, bar_faang_cy + 0.5, 0])
        sub_faang = ink_text("months to hire", size=0.32, color=WHITE)
        sub_faang.next_to(lbl_faang, DOWN, buff=0.2)

        self.play(FadeIn(lbl_cheap), FadeIn(lbl_faang), FadeIn(sub_faang), run_time=0.8)
        self.wait(2.5)

        chip = label_chip("same caliber — today", fill=TEAL, size=0.29)
        chip.move_to([LEFT_X, bar_cheap_top_y + 0.35, 0])
        self.play(FadeIn(chip), run_time=0.6)
        self.wait(1.5)

        # ── hand-off guarantee — below floor
        HO_Y = FLOOR_Y - 1.35   # y-center of hand-off group

        ho_header = cap_text("If they get the job →", size=0.35, color=INK)
        ho_header.move_to([-3.5, HO_Y + 0.55, 0])

        def person_icon(lbl_text, color=TEAL):
            head = Circle(radius=0.18, fill_color=color, fill_opacity=1, stroke_width=0)
            body = Rectangle(width=0.22, height=0.38,
                             fill_color=color, fill_opacity=1, stroke_width=0)
            body.next_to(head, DOWN, buff=0.04)
            t = ink_text(lbl_text, size=0.27, color=color)
            t.next_to(body, DOWN, buff=0.1)
            return VGroup(head, body, t)

        grad_a = person_icon("grad A")
        grad_b = person_icon("grad B")
        arr    = Arrow(LEFT * 0.5, RIGHT * 0.5, buff=0,
                       stroke_color=INK, stroke_width=2,
                       max_tip_length_to_length_ratio=0.25)
        no_day = ink_text("You don't lose a day.", size=0.36, slant=ITALIC)

        ho_group = VGroup(grad_a, arr, grad_b).arrange(RIGHT, buff=0.4)
        ho_group.move_to([0, HO_Y, 0])
        no_day.next_to(ho_group, DOWN, buff=0.28)

        self.play(FadeIn(ho_header), FadeIn(grad_a), run_time=0.5)
        self.play(GrowArrow(arr), run_time=0.6)
        self.play(FadeIn(grad_b), run_time=0.5)
        self.play(FadeIn(no_day, shift=UP * 0.1), run_time=0.6)

        elapsed = 2.5 + 0.8 + 2.5 + 0.6 + 1.5 + 0.5 + 0.6 + 0.5 + 0.6
        self.wait(max(0.2, DUR - elapsed))


# ══════════════════════════════════════════════════════════════════════════════
# B04 — Win-Win  (7.49s)
# Two columns: Grad | Founder. Benefits reveal left then right.
# ══════════════════════════════════════════════════════════════════════════════

class B04_WinWin(Scene):
    def construct(self):
        DUR = 7.49

        # central header
        header = cap_text("Win — Win", size=0.65, color=INK).to_edge(UP, buff=0.55)
        hl = hairline().next_to(header, DOWN, buff=0.14)
        self.add(header, hl)

        divider = Line(UP * 2.0, DOWN * 2.2,
                       stroke_color=HAIRLINE, stroke_width=1.8)
        self.add(divider)

        # left: Grad
        grad_head = cap_text("THE GRAD", size=0.42, color=TEAL)
        grad_b1   = ink_text("Real project income", size=0.37)
        grad_b2   = ink_text("Real portfolio work", size=0.37)
        grad_b3   = ink_text("While they search", size=0.37)
        grad_col  = VGroup(grad_head, grad_b1, grad_b2, grad_b3)
        grad_col.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        grad_col.move_to([-3.2, 0.0, 0])

        # right: Founder
        founder_head = cap_text("THE FOUNDER", size=0.42, color=TERRA)
        fnd_b1       = ink_text("Build ships — now", size=0.37)
        fnd_b2       = ink_text("Today's rate", size=0.37)
        fnd_b3       = ink_text("Before the window closes", size=0.37)
        fnd_col      = VGroup(founder_head, fnd_b1, fnd_b2, fnd_b3)
        fnd_col.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        fnd_col.move_to([2.1, 0.0, 0])

        self.play(FadeIn(grad_col, shift=RIGHT * 0.3), run_time=1.4)
        self.play(FadeIn(fnd_col,  shift=LEFT  * 0.3), run_time=1.4)

        elapsed = 1.4 + 1.4
        self.wait(max(0.2, DUR - elapsed))
