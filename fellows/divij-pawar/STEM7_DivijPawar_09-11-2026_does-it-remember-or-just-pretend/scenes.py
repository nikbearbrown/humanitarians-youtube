"""scenes.py — Manim scenes for does-it-remember-or-just-pretend (claude-divij).

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757, soft #73705F,
ghost #A9A491 — the Claude fidelity palette per ai-explainer SKILL.md. ONE
accent per beat. The source script's [VISUAL] color cues (a "healthy" vs.
"corrupted" memory dot, a glowing vs. dim box) are retinted the same way
STEM2/STEM5/STEM6 handled their own green/red cues: good/bad carried by
label, position, and ink-vs-terracotta, never a second hue. No blue, no
green, no red.

Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF,
editorial voice only) / PT Mono (MONO, logs + code + data only) — see
graphics_lib.py. Boxes are content-fitted via auto_box/surround_box, never
hand-measured. This file never calls raw Text() for body copy.

Pace: normal-speed creates/fades with deliberate HOLDS sized to the
narration. Targets below are against `estimated_duration_s` in
beat_sheet.json; RETIME against `actual_duration_s` once Kokoro has run
(see BUILD-PROMPT.md Step 3 — not yet done, this reel is pre-audio).

B05 deliberately reprises the two-agent-nameplate visual language from
when-two-agents-disagree (STEM6) — the same `label_chip` nameplate look —
so the "same blind spot" claim is a shown callback, not just an assertion.
"""
import numpy as np
from graphics_lib import *

# ── Palette (claude-stage retint, per ai-explainer SKILL.md) ──────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")


def dot_field(n, color, seed, spread_x=6.0, spread_y=3.0, radius=0.05):
    """A scattered field of small dots standing in for stored memory
    fragments — a fixed seed so the layout is reproducible across
    re-renders/retiming passes."""
    rng = np.random.default_rng(seed)
    dots = VGroup()
    for _ in range(n):
        x = rng.uniform(-spread_x, spread_x)
        y = rng.uniform(-spread_y, spread_y)
        dots.add(Dot([x, y, 0], color=color, radius=radius))
    return dots


def clock_icon(color, radius=0.4):
    face = Circle(radius=radius, color=color, stroke_width=2.5)
    hour = Line(ORIGIN, UP * radius * 0.5, color=color, stroke_width=3)
    minute = Line(ORIGIN, RIGHT * radius * 0.7, color=color, stroke_width=2.5)
    return VGroup(face, hour, minute)


def tag_icon(color, width=0.7, height=0.4):
    """A small luggage-tag shape — a rounded rect with a string hole."""
    body = RoundedRectangle(corner_radius=0.06, width=width, height=height,
                             color=color, stroke_width=2.5)
    hole = Circle(radius=0.04, color=color, stroke_width=2)
    hole.move_to(body.get_left() + RIGHT * 0.1)
    return VGroup(body, hole)


def hourglass_icon(color, width=0.5, height=0.7):
    top = Polygon([-width / 2, height / 2, 0], [width / 2, height / 2, 0], [0, 0, 0],
                  color=color, stroke_width=2.5)
    bottom = Polygon([-width / 2, -height / 2, 0], [width / 2, -height / 2, 0], [0, 0, 0],
                      color=color, stroke_width=2.5)
    return VGroup(top, bottom)


def crossed_flag_icon(color, size=0.5):
    a = Line(UL * size * 0.5, DR * size * 0.5, color=color, stroke_width=3)
    b = Line(UR * size * 0.5, DL * size * 0.5, color=color, stroke_width=3)
    return VGroup(a, b)


def cabinet_icon(color, width=0.6, height=0.8):
    body = Rectangle(width=width, height=height, color=color, stroke_width=2.5)
    drawer1 = Line(body.get_corner(UL) + DOWN * height * 0.33,
                    body.get_corner(UR) + DOWN * height * 0.33, color=color, stroke_width=1.5)
    drawer2 = Line(body.get_corner(UL) + DOWN * height * 0.66,
                    body.get_corner(UR) + DOWN * height * 0.66, color=color, stroke_width=1.5)
    handle1 = Dot(body.get_left() + RIGHT * width * 0.15 + DOWN * height * 0.17,
                   color=color, radius=0.03)
    handle2 = Dot(body.get_left() + RIGHT * width * 0.15 + DOWN * height * 0.5,
                   color=color, radius=0.03)
    return VGroup(body, drawer1, drawer2, handle1, handle2)


def crack_line(rect, color, jitter=0.14):
    """A jagged VMobject cutting through rect's height — the same
    shared-contamination motif from when-two-agents-disagree (STEM6)."""
    top, bottom = rect.get_top(), rect.get_bottom()
    n = 6
    pts = []
    for i in range(n + 1):
        y = top[1] + (bottom[1] - top[1]) * i / n
        x = rect.get_center()[0] + (jitter if i % 2 == 0 else -jitter)
        pts.append([x, y, 0])
    line = VMobject(color=color, stroke_width=3)
    line.set_points_as_corners(pts)
    return line


# ─────────────────────────────────────────────────────────────────────────────
#  B01_OneWordTwoMechanisms   (target ~55s)
#  The framework/BLUF beat — one word splits into a box that evaporates and
#  a box that persists, establishing the episode's central distinction.
# ─────────────────────────────────────────────────────────────────────────────
class B01_OneWordTwoMechanisms(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("One Word, Two Mechanisms", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.6)

        word = label("Memory", size=52, color=INK, weight="BOLD").move_to(UP * 1.2)
        self.play(FadeIn(word, scale=1.1), run_time=0.7)
        self.wait(2.2)

        arr_l = Arrow(word.get_bottom(), [-3.6, -0.5, 0], buff=0.15, color=SOFT, stroke_width=2.5)
        arr_r = Arrow(word.get_bottom(), [3.6, -0.5, 0], buff=0.15, color=SOFT, stroke_width=2.5)
        self.play(Create(arr_l), Create(arr_r), run_time=0.7)
        self.wait(1.4)

        cw_txt = label("Context\nWindow", size=24, color=INK, line_spacing=0.85)
        cw_box = auto_box(cw_txt, h_pad=0.3, v_pad=0.24, color=INK)
        cw = VGroup(cw_box, cw_txt).move_to([-3.6, -1.4, 0])
        cw_tag = label("temporary", size=18, color=SOFT).next_to(cw, DOWN, buff=0.2)
        self.play(FadeIn(cw), FadeIn(cw_tag), run_time=0.6)
        self.wait(5.87)

        # ── The context window evaporates ──────────────────────────────────
        evap = label("gone the moment\nthe chat ends", size=18, color=ACC, line_spacing=0.85)
        evap.next_to(cw_tag, DOWN, buff=0.3)
        self.play(FadeIn(evap), run_time=0.5)
        self.wait(1.6)
        self.play(cw.animate.set_opacity(0.15).scale(0.85).shift(UP * 0.3),
                   FadeOut(cw_tag), FadeOut(evap), run_time=1.1)
        self.wait(2.4)

        pm_txt = label("Persistent\nMemory", size=26, color=INK, line_spacing=0.85, weight="BOLD")
        pm_box = auto_box(pm_txt, h_pad=0.34, v_pad=0.26, color=INK)
        pm = VGroup(pm_box, pm_txt).move_to([3.6, -1.2, 0])
        cabinet = cabinet_icon(SOFT).next_to(pm, DOWN, buff=0.3)
        link = Line(pm_box.get_bottom(), cabinet.get_top(), buff=0.06, color=SOFT, stroke_width=2)
        self.play(FadeIn(pm), Create(link), FadeIn(cabinet), run_time=0.7)
        self.wait(1.8)

        pm_tag = label("retrieved later", size=18, color=SOFT).next_to(cabinet, DOWN, buff=0.3)
        self.play(FadeIn(pm_tag), run_time=0.5)
        self.wait(2.9)

        caption = label("the model isn't recalling —\nit's reacting to re-inserted text",
                         size=21, color=INK, line_spacing=0.9)
        caption.move_to(DOWN * 3.0)
        self.play(FadeOut(VGroup(arr_l, arr_r, cw)), FadeIn(caption), run_time=0.7)
        self.wait(10.0)

        self.play(FadeOut(VGroup(word, pm, cabinet, link, pm_tag, caption)), run_time=0.6)
        land = serif("One name, two very different mechanisms.",
                      size=30, color=ACC).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(11.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_HowRetrievalWorks   (target ~55s)
#  A scattered field of memory fragments; a new query lights up only the
#  nearest ones — then the caveat that similarity is not the same axis as truth.
# ─────────────────────────────────────────────────────────────────────────────
class B02_HowRetrievalWorks(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("How Retrieval Actually Works", color=INK, size=42)
        self.play(Write(t), run_time=0.6)
        self.wait(1.6)

        field = dot_field(26, GHOST, seed=7, spread_x=5.8, spread_y=2.6)
        field.shift(DOWN * 0.4)
        self.play(LaggedStart(*[FadeIn(d) for d in field], lag_ratio=0.03), run_time=1.2)
        self.wait(1.8)

        query = Dot(DOWN * 0.4, color=ACC, radius=0.09)
        self.play(FadeIn(query, scale=2.0), run_time=0.6)
        self.play(Indicate(query, scale_factor=1.4, color=ACC), run_time=0.6)
        self.wait(1.4)

        near_idx = list(range(4))
        near = VGroup(*[field[i] for i in near_idx])
        self.play(*[d.animate.set_color(INK).scale(1.6) for d in near], run_time=0.8)
        self.wait(2.6)

        pair = VGroup(
            label("flight → aisle-seat note lights up", size=19, color=INK),
            label("recipe → same note stays dark", size=19, color=SOFT),
        ).arrange(DOWN, buff=0.22).move_to(UP * 2.3)
        self.play(FadeOut(field), FadeOut(query), FadeIn(pair), run_time=0.7)
        self.wait(5.5)

        caption = label('"similar meaning" ≠ "still true"', size=25, color=ACC)
        caption.move_to(DOWN * 0.8)
        self.play(FadeIn(caption), run_time=0.6)
        self.wait(5.9)

        dashes = label("no expiration  ·  no confidence  ·  no origin",
                        size=21, color=SOFT)
        dashes.next_to(caption, DOWN, buff=0.5)
        self.play(FadeIn(dashes), run_time=0.5)
        self.wait(10.8)

        self.play(FadeOut(VGroup(pair, caption, dashes)), run_time=0.6)
        land = serif("Blunt in a specific, important way.",
                      size=29, color=ACC).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(12.3)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_StaleMemory   (target ~37s)
#  A stored memory card sits unchanged while a clock ticks forward months,
#  then still fires on a new, unrelated-in-time query.
# ─────────────────────────────────────────────────────────────────────────────
class B03_StaleMemory(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Stale Memory", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.4)

        card_txt = mono("user: vegetarian", size=22, color=INK)
        card_box = auto_box(card_txt, h_pad=0.35, v_pad=0.26, color=INK)
        card = VGroup(card_box, card_txt).move_to(UP * 1.6)
        stamp = label("saved 8 months ago", size=17, color=SOFT).next_to(card, DOWN, buff=0.2)
        self.play(FadeIn(card), FadeIn(stamp), run_time=0.6)
        self.wait(2.4)

        clock = clock_icon(SOFT).move_to(DOWN * 0.6)
        self.play(FadeIn(clock), run_time=0.5)
        self.play(Rotate(clock[1], angle=5 * PI, about_point=clock.get_center(), run_time=2.2),
                   Rotate(clock[2], angle=1.2 * PI, about_point=clock.get_center(), run_time=2.2))
        self.wait(0.8)

        unchanged = label("the card never changes", size=19, color=SOFT)
        unchanged.next_to(clock, DOWN, buff=0.35)
        self.play(FadeIn(unchanged), run_time=0.5)
        self.wait(2.6)

        # `q` originally sat at y=-2.6, sharing the bottom third of the
        # frame with cap1/cap2 (both at DOWN*3.0) — its box bottom edge
        # directly touched cap2's text, caught in smoke-test QC. Moved up
        # to y=-0.4, well clear of the caption zone, still low enough for
        # a clean arrow up into `card`.
        query = label("recommend dinner", size=20, color=ACC)
        q_box = auto_box(query, h_pad=0.28, v_pad=0.2, color=ACC)
        q = VGroup(q_box, query).move_to([-4.2, -0.4, 0])
        arrow = Arrow(q.get_right(), card.get_left(), buff=0.15, color=ACC, stroke_width=2.5,
                       path_arc=-0.6)
        self.play(FadeOut(clock), FadeOut(unchanged), FadeIn(q), run_time=0.5)
        self.play(Create(arrow), card_box.animate.set_stroke(color=ACC), run_time=0.7)
        self.wait(3.1)

        cap1 = label("no built-in clock", size=22, color=ACC)
        cap1.move_to(DOWN * 3.0)
        self.play(FadeIn(cap1), run_time=0.5)
        self.wait(3.1)

        # cap1 and cap2 previously crossfaded simultaneously at the same
        # DOWN*3.0 anchor — two different strings briefly double-exposed
        # at full-ish opacity mid-transition, caught in low-res smoke-test
        # QC. Sequenced instead: cap1 fully clears before cap2 fades in.
        self.play(FadeOut(cap1), run_time=0.3)
        cap2 = label("something has to decide when to stop trusting it", size=19, color=SOFT)
        cap2.move_to(DOWN * 3.0)
        self.play(FadeIn(cap2), run_time=0.4)
        self.wait(3.1)

        self.play(FadeOut(VGroup(card, stamp, q, arrow, cap2)), run_time=0.6)
        land = serif("Steering answers on something no longer true.",
                      size=27, color=ACC).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(4.21)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_PoisonedMemory   (target ~37s)
#  A cracked memory dot sits dormant, ignored by an unrelated query, then
#  gets pulled into an answer by a later, semantically-close one.
# ─────────────────────────────────────────────────────────────────────────────
class B04_PoisonedMemory(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Poisoned Memory", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.4)

        field = dot_field(18, GHOST, seed=11, spread_x=5.0, spread_y=1.8)
        field.move_to(UP * 0.3)
        cracked = Dot(field[9].get_center(), color=ACC, radius=0.08)
        crack = crack_line(Rectangle(width=0.3, height=0.3).move_to(cracked), ACC, jitter=0.06)
        self.play(LaggedStart(*[FadeIn(d) for d in field], lag_ratio=0.03),
                   FadeIn(cracked), Create(crack), run_time=1.0)
        self.wait(1.8)

        q1 = label("query 1 (unrelated)", size=19, color=SOFT).move_to(DOWN * 2.6)
        self.play(FadeIn(q1), run_time=0.5)
        others = VGroup(*[field[i] for i in (2, 5, 14)])
        self.play(*[d.animate.set_color(INK).scale(1.5) for d in others], run_time=0.6)
        self.wait(1.2)

        waiting = label("waiting", size=18, color=GHOST).next_to(cracked, UP, buff=0.15)
        self.play(FadeIn(waiting), run_time=0.4)
        self.wait(1.6)

        self.play(FadeOut(q1), FadeOut(waiting),
                   *[d.animate.set_color(GHOST).scale(1 / 1.5) for d in others], run_time=0.6)

        q2 = label("query 2 (a later, different conversation)", size=19, color=ACC)
        q2.move_to(DOWN * 2.6)
        self.play(FadeIn(q2), run_time=0.5)
        self.play(cracked.animate.scale(1.8), Indicate(cracked, color=ACC), run_time=0.7)
        pulled = Arrow(cracked.get_center(), q2.get_top(), buff=0.15, color=ACC, stroke_width=2.5)
        self.play(Create(pulled), run_time=0.5)
        self.wait(2.4)

        # `cap` was anchored at UP*3.0, directly into the persistent title
        # (title's own bottom edge sits ~y=2.9, never fades in this scene)
        # — caught in low-res smoke-test QC. The whole diagram clears
        # first instead, so the caption gets a clean, uncontested frame.
        self.play(FadeOut(VGroup(field, cracked, crack, q2, pulled)), run_time=0.6)
        cap = label("one bad moment doesn't stay contained", size=23, color=ACC)
        cap.move_to(UP * 0.4)
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(6.2)

        self.play(FadeOut(cap), run_time=0.4)
        land = serif("It damages every future session it reaches back into.",
                      size=26, color=ACC).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(8.44)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_SameBlindSpot   (target ~41s)
#  The falsifiability beat — the multi-agent shared-contamination diagram
#  from when-two-agents-disagree (STEM6), beside its time-stretched twin.
# ─────────────────────────────────────────────────────────────────────────────
class B05_SameBlindSpot(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Where You've Seen This Before", color=INK, size=40)
        self.play(Write(t), run_time=0.6)
        self.wait(1.6)

        divider = Line(UP * 2.6, DOWN * 2.6, color=GHOST, stroke_width=2)
        self.play(Create(divider), run_time=0.5)
        self.wait(0.6)

        # ── Left: two agents, one shared poisoned source, same moment ────────
        a = label_chip("Agent A", SOFT, size=18).move_to([-4.6, 1.8, 0])
        b = label_chip("Agent B", SOFT, size=18).move_to([-2.2, 1.8, 0])
        doc_l = Rectangle(width=0.9, height=1.1, color=SOFT, stroke_width=2.5,
                           fill_color=SOFT, fill_opacity=0.05).move_to([-3.4, 0.2, 0])
        arr_al = Arrow(a.get_bottom(), doc_l.get_top() + LEFT * 0.2, buff=0.08, color=SOFT, stroke_width=2)
        arr_bl = Arrow(b.get_bottom(), doc_l.get_top() + RIGHT * 0.2, buff=0.08, color=SOFT, stroke_width=2)
        self.play(FadeIn(a), FadeIn(b), FadeIn(doc_l), Create(arr_al), Create(arr_bl), run_time=0.7)
        self.wait(1.0)
        self.play(a[0].animate.set_color(ACC), b[0].animate.set_color(ACC), run_time=0.5)
        crack_l = crack_line(doc_l, ACC, jitter=0.08)
        self.play(Create(crack_l), run_time=0.5)
        left_cap = label("same moment", size=17, color=SOFT).next_to(doc_l, DOWN, buff=0.7)
        self.play(FadeIn(left_cap), run_time=0.4)
        self.wait(2.4)

        # ── Right: one agent, two days, same poisoned memory ─────────────────
        day1 = label_chip("Day 1", SOFT, size=18).move_to([2.2, 1.8, 0])
        day30 = label_chip("Day 30", SOFT, size=18).move_to([4.6, 1.8, 0])
        doc_r = Rectangle(width=0.9, height=1.1, color=SOFT, stroke_width=2.5,
                           fill_color=SOFT, fill_opacity=0.05).move_to([3.4, 0.2, 0])
        arr_ar = Arrow(day1.get_bottom(), doc_r.get_top() + LEFT * 0.2, buff=0.08, color=SOFT, stroke_width=2)
        arr_br = Arrow(day30.get_bottom(), doc_r.get_top() + RIGHT * 0.2, buff=0.08, color=SOFT, stroke_width=2)
        self.play(FadeIn(day1), FadeIn(day30), FadeIn(doc_r), Create(arr_ar), Create(arr_br), run_time=0.7)
        self.wait(1.0)
        self.play(day1[0].animate.set_color(ACC), day30[0].animate.set_color(ACC), run_time=0.5)
        crack_r = crack_line(doc_r, ACC, jitter=0.08)
        self.play(Create(crack_r), run_time=0.5)
        right_cap = label("same memory,\ndifferent moments", size=17, color=SOFT, line_spacing=0.85)
        right_cap.next_to(doc_r, DOWN, buff=0.55)
        self.play(FadeIn(right_cap), run_time=0.4)
        self.wait(6.76)

        span_cap = label("a blind spot for input that never contradicts itself",
                          size=21, color=ACC)
        span_cap.move_to(DOWN * 3.2)
        self.play(FadeIn(span_cap), run_time=0.6)
        self.wait(9.5)

        self.play(FadeOut(VGroup(a, b, doc_l, arr_al, arr_bl, crack_l, left_cap,
                                  day1, day30, doc_r, arr_ar, arr_br, crack_r, right_cap,
                                  divider, span_cap)), run_time=0.6)
        land = serif("Persistence gives that blind spot a longer runway.",
                      size=27, color=ACC).move_to(DOWN * 0.2)
        self.play(Write(land), run_time=0.9)
        self.wait(9.53)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_TheFramework   (target ~65s)
#  Three transferable design requirements, each paired with its icon,
#  collected into a row before the bookends.
# ─────────────────────────────────────────────────────────────────────────────
class B06_TheFramework(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("What Responsible Memory Requires", color=INK, size=38)
        self.play(Write(t), run_time=0.6)
        self.wait(2.0)

        def rule_col(icon, name, desc):
            icon.scale_to_fit_height(0.6)
            nm = label(name, size=24, color=INK, weight="BOLD")
            ds = label(desc, size=17, color=SOFT, line_spacing=0.85)
            stack = VGroup(icon, nm, ds).arrange(DOWN, buff=0.28)
            return stack

        r1 = rule_col(tag_icon(ACC), "Provenance", "where it came from,\nand when")
        r2 = rule_col(hourglass_icon(ACC), "Decay", "not all facts age\nat the same rate")
        r3 = rule_col(crossed_flag_icon(ACC), "Contradiction\nChecks", "surfaced, not silently\noverwritten")

        row = VGroup(r1, r2, r3).arrange(RIGHT, buff=1.0).move_to(DOWN * 0.1)
        if row.width > 12.0:
            row.scale(12.0 / row.width)

        for r in (r1, r2, r3):
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.6)
            self.wait(6.5)

        checks = VGroup(*[
            label("✓", size=24, color=ACC).next_to(r, UP, buff=0.12) for r in (r1, r2, r3)
        ])
        self.play(LaggedStart(*[FadeIn(c) for c in checks], lag_ratio=0.2), run_time=0.8)
        self.wait(5.8)

        caption = label("not just storage — scrutiny", size=23, color=INK)
        caption.next_to(row, DOWN, buff=0.6)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(9.5)

        footnote = serif("Design requirements, not optional extras.",
                          size=27, color=ACC).move_to(DOWN * 3.2)
        self.play(FadeOut(caption), FadeIn(footnote), run_time=0.6)
        self.wait(11.63)
