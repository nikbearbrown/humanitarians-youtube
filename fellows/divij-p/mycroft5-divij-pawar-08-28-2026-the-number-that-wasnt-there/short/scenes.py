"""short/scenes.py — 9:16 portrait re-layout of six beats kept in the Short.

Portrait rendering (manim -r 1080,1920) keeps frame_height at 8 units but
shrinks frame_width to ~4.5 (half-width ~2.25) — every horizontal
arrangement in the parent reel's scenes.py assumed the 16:9 frame_width
(~14.2) and would clip off-frame here. Every beat below is restacked
vertically instead, never a center-cut of the 16:9 version, per shorts.py's
"Manim GRAPHIC beats are re-laid-out for portrait" rule and the precedent
in ../../STEM5/short/scenes.py (same convention: BID_Name916, graphics_lib
imported unchanged, frame_width ~4.5 assumed throughout).

Safe frame used throughout: x in [-2.0, 2.0], y in [-3.5, 3.5] (a slightly
tighter margin than the 16:9 parent's [-6.4,6.4]/[-3.6,3.6] — portrait's
narrow width leaves much less room for anything to drift before it bleeds
off the side edge).
"""
from graphics_lib import *

BG = "#FAF9F5"
INK = "#3D3929"
ACC = "#D97757"
SOFT = "#73705F"
GHOST = "#A9A491"

GREEN = "#4C9A6A"
AMBER = "#C9932E"
RED = "#B0473A"


def hold_to(scene, target, minimum=0.4):
    try:
        elapsed = float(scene.renderer.time)
    except Exception:
        scene.wait(minimum)
        return
    scene.wait(max(minimum, target - elapsed))


def boxed(inner, color=INK, h_pad=0.35, v_pad=0.24, **kw):
    b = auto_box(inner, h_pad=h_pad, v_pad=v_pad, color=color, **kw)
    return VGroup(b, inner)


def scorecard_v(state, y=3.05, active_idx=None):
    """Portrait scorecard: same 5-slot semantics as the parent's scorecard(),
    but narrower chips (0.72 wide, buff 0.1) so all five fit inside the
    ~4.0-unit safe width instead of the parent's 1.15-wide/0.24-buff chips,
    which total 6.71 units — nearly 3x the portrait frame's usable width."""
    chips = VGroup()
    for i in range(5):
        col = state[i]
        is_active = (active_idx == i) and col is None
        stroke = col if col else (ACC if is_active else GHOST)
        fill = col if col else BG
        txt_color = "#FFFFFF" if col else (ACC if is_active else GHOST)
        t = mono(f"T{i + 1}", size=14, color=txt_color)
        box = Rectangle(width=0.72, height=0.42,
                         stroke_width=(2.4 if is_active else 1.8),
                         color=stroke, fill_color=fill,
                         fill_opacity=(0.88 if col else 0.05))
        chip = VGroup(box, t)
        t.move_to(box)
        chips.add(chip)
    chips.arrange(RIGHT, buff=0.1).move_to([0, y, 0])
    return chips


# ─────────────────────────────────────────────────────────────────────────────
#  B02_InputVsInvented916   (target ~33s)
# ─────────────────────────────────────────────────────────────────────────────
class B02_InputVsInvented916(Scene):
    TARGET = 33.15

    def construct(self):
        self.camera.background_color = BG

        moved = label_chip("RAN ON A MODEL\nSET UP LOCALLY", ACC, size=18)
        moved.move_to([0, 2.8, 0])
        self.play(FadeIn(moved), run_time=0.5)
        self.wait(1.2)
        self.play(FadeOut(moved), run_time=0.4)

        head_a = label("PRODUCER A — REAL INPUTS", size=18, weight="BOLD",
                       color=SOFT).move_to([0, 2.9, 0])
        inputs = VGroup(*[
            VGroup(auto_box(mono(t, size=20, color=INK), h_pad=0.22, v_pad=0.16,
                             color=INK), mono(t, size=20, color=INK))
            for t in ("Assets", "Revenues", "NetIncomeLoss")
        ])
        for pair in inputs:
            pair[1].move_to(pair[0])
        inputs.arrange(RIGHT, buff=0.22).move_to([0, 1.9, 0])
        self.play(FadeIn(head_a), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in inputs],
                              lag_ratio=0.3), run_time=1.2)
        self.wait(1.4)
        self.play(FadeOut(VGroup(head_a, inputs)), run_time=0.4)

        head_b = label("WHAT IT WROTE", size=18, weight="BOLD",
                       color=SOFT).move_to([0, 2.9, 0])
        claim = serif("\"debt-to-equity ratio\nas 0.34\"", size=24, color=ACC,
                      line_spacing=0.8)
        claim_box = boxed(claim, color=ACC).move_to([0, 1.9, 0])
        qsrc = DashedVMobject(
            Rectangle(width=0.9, height=0.62, color=GHOST, stroke_width=2.2),
            num_dashes=16, color=GHOST)
        qmark = label("?", size=36, color=GHOST)
        qmark.move_to(qsrc)
        qgroup = VGroup(qsrc, qmark)
        qgroup.next_to(claim_box, DOWN, buff=0.3)
        qlbl = label("source data", size=16, color=GHOST).next_to(qgroup, DOWN, buff=0.12)

        self.play(FadeIn(head_b), run_time=0.4)
        self.play(FadeIn(claim_box), run_time=0.5)
        self.wait(1.0)
        self.play(Create(qsrc), FadeIn(qmark), FadeIn(qlbl), run_time=0.5)
        self.wait(1.6)

        verdict = label("NOT CLOSE. NOT DERIVED.\nNOT IN THE DATA AT ALL.",
                        size=20, weight="BOLD", color=ACC, line_spacing=0.75)
        verdict.move_to([0, -1.7, 0])
        self.play(FadeIn(verdict), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_ScorecardIntro916   (target ~16s)
# ─────────────────────────────────────────────────────────────────────────────
class B03_ScorecardIntro916(Scene):
    TARGET = 15.77

    def construct(self):
        self.camera.background_color = BG

        card = scorecard_v([None] * 5, y=2.85)
        head = label("ONE SURPRISING\nRESULT COULD BE NOISE", size=18,
                    weight="BOLD", color=SOFT, line_spacing=0.85).next_to(card, UP, buff=0.22)
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(card, scale=0.94), run_time=0.6)
        self.wait(0.8)

        row1 = VGroup(*[mono(t, size=14, color=SOFT) for t in
                        ("WHAT", "WHY", "GOOD RESULT")]).arrange(RIGHT, buff=0.3)
        row2 = VGroup(*[mono(t, size=14, color=SOFT) for t in
                        ("GIVEN", "HAPPENED", "MEANS")]).arrange(RIGHT, buff=0.3)
        fields = VGroup(row1, row2).arrange(DOWN, buff=0.24).move_to([0, 1.1, 0])
        self.play(LaggedStart(FadeIn(row1), FadeIn(row2), lag_ratio=0.3),
                  run_time=1.0)
        self.wait(1.0)

        cap = label("not a quick pass or fail —\nthe full six-field\ntreatment, each test",
                   size=19, weight="BOLD", color=INK, line_spacing=0.75)
        cap.move_to([0, -1.1, 0])
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(1.2)

        five = label_chip("HERE'S ALL FIVE", ACC, size=20)
        five.move_to([0, -2.6, 0])
        self.play(FadeIn(five), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B09_ScorecardComplete916   (target ~13s)
# ─────────────────────────────────────────────────────────────────────────────
class B09_ScorecardComplete916(Scene):
    TARGET = 13.14

    def construct(self):
        self.camera.background_color = BG

        card = scorecard_v([AMBER, AMBER, GREEN, GREEN, RED])
        self.play(FadeIn(card, scale=1.05), run_time=0.5)
        self.wait(1.0)

        labels = VGroup(*[
            label(f"T{i + 1} — {t}", size=16, color=c) for i, (t, c) in enumerate([
                ("upstream gap", AMBER), ("informative outlier", AMBER),
                ("worked as intended", GREEN), ("clean structural pass", GREEN),
                ("real, redirecting flaw", RED),
            ])
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        labels.move_to([0, -0.3, 0])
        self.play(FadeIn(labels), run_time=0.6)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B11_ElevenToSeven916   (target ~25s)
# ─────────────────────────────────────────────────────────────────────────────
class B11_ElevenToSeven916(Scene):
    TARGET = 24.98

    def construct(self):
        self.camera.background_color = BG

        chip = label_chip("SAME 12 COMPANIES.\nRECALCULATED, NOT RE-RUN.", ACC,
                          size=15)
        chip.move_to([0, 3.05, 0])
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(1.0)

        x0, sc = 0.0, 1.6 / 11.0
        bar = Rectangle(width=0.9, height=11 * sc, color=ACC, stroke_width=2,
                       fill_opacity=0.75, fill_color=ACC)
        bar.move_to([x0, 0.5, 0], aligned_edge=DOWN)
        old_lbl = label("OLD RULE: 11", size=18, weight="BOLD", color=ACC)
        old_lbl.next_to(bar, UP, buff=0.2)
        base = Line([-1.9, -0.4, 0], [1.9, -0.4, 0], color=GHOST, stroke_width=1.4)

        self.play(Create(base), run_time=0.3)
        self.play(GrowFromEdge(bar, DOWN), FadeIn(old_lbl), run_time=0.7)
        self.wait(1.2)

        new_h = 7 * sc
        self.play(bar.animate.stretch_to_fit_height(new_h).move_to(
            [x0, -0.4 + new_h / 2, 0]),
            old_lbl.animate.next_to(bar, UP, buff=0.2),
            run_time=0.9)
        new_lbl = label("NEW RULE: 7", size=18, weight="BOLD", color=ACC)
        new_lbl.next_to(bar, UP, buff=0.2)
        self.play(FadeOut(old_lbl), FadeIn(new_lbl), run_time=0.4)
        self.wait(1.2)

        tiles = VGroup(*[Rectangle(width=0.55, height=0.4, color=ACC,
                                   stroke_width=1.8, fill_opacity=0.28,
                                   fill_color=ACC) for _ in range(4)])
        tiles.arrange(RIGHT, buff=0.16).move_to([0, -1.3, 0])
        self.play(FadeIn(tiles), run_time=0.5)
        self.wait(0.6)
        self.play(*[t.animate.set_stroke(color=GHOST, width=1.8).set_fill(
            color=GHOST, opacity=0.1) for t in tiles], run_time=0.7)
        flip_cap = label("one agent hadn't quantified\nanything — false alarm, gone",
                        size=15, color=SOFT, line_spacing=0.7)
        flip_cap.next_to(tiles, DOWN, buff=0.22)
        self.play(FadeIn(flip_cap), run_time=0.4)
        self.wait(1.6)

        cap = label("still flagged — real numbers,\ndifferent concepts",
                   size=18, weight="BOLD", color=INK, line_spacing=0.8)
        # next_to the actual flip_cap object, not a guessed fixed y — the
        # fixed y=-2.7 undershot flip_cap's real rendered height and
        # collided with it (caught in portrait QC).
        cap.next_to(flip_cap, DOWN, buff=0.3)
        self.play(FadeIn(cap), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B12_TwoChipsHonestLedger916   (target ~28s)
# ─────────────────────────────────────────────────────────────────────────────
class B12_TwoChipsHonestLedger916(Scene):
    TARGET = 27.73

    def construct(self):
        self.camera.background_color = BG

        # Every element below is chained via next_to() off the ACTUAL
        # previous mobject, never a guessed fixed y — the first pass used
        # fixed y-coordinates for the header and both boxes and they
        # collided in three places at once (caught in portrait QC: the
        # header ran into INFRASTRUCTURE's label, and INFRASTRUCTURE's own
        # list ran into JUDGMENT's label below the box). Box height is
        # also reduced (2.5 -> 1.9) so both boxes plus the header
        # comfortably fit the portrait frame's 7-unit safe height with
        # real margin, instead of nearly filling it edge to edge.
        head = label("TWO SEPARATE QUESTIONS,\nTWO SEPARATE ANSWERS", size=17,
                    weight="BOLD", color=SOFT, line_spacing=0.7)
        head.move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(1.0)

        # ── infrastructure: solid, upper half ────────────────────────────────
        infra_lbl = label("INFRASTRUCTURE", size=16, weight="BOLD", color=INK)
        infra_lbl.next_to(head, DOWN, buff=0.4)
        infra_outline = Rectangle(width=3.6, height=1.9, color=INK, stroke_width=2.6)
        infra_outline.next_to(infra_lbl, DOWN, buff=0.16)
        self.play(Create(infra_outline), FadeIn(infra_lbl), run_time=0.6)
        self.play(infra_outline.animate.set_fill(color=GREEN, opacity=0.85)
                  .set_stroke(color=GREEN), run_time=0.7)
        infra_list = VGroup(*[
            label(t, size=12, color="#FFFFFF") for t in
            ("real filings", "real independent reasoning",
             "full audit trail", "24/24 guardrail held")
        ]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        # "real independent reasoning" is the widest line — at size 12 it
        # rendered wider than the 3.6-unit box and spilled white text past
        # both edges onto the cream background (caught in portrait QC,
        # visible as near-invisible white slivers outside the green fill).
        # Scale to fit with real margin rather than trusting the guessed
        # font size was narrow enough.
        max_w = infra_outline.width - 0.3
        if infra_list.width > max_w:
            infra_list.scale(max_w / infra_list.width)
        infra_list.move_to(infra_outline)
        self.play(FadeIn(infra_list), run_time=0.5)
        self.wait(1.4)

        # ── judgment: half-filled, lower half ────────────────────────────────
        judg_lbl = label("JUDGMENT", size=16, weight="BOLD", color=INK)
        judg_lbl.next_to(infra_outline, DOWN, buff=0.4)
        judg_outline = Rectangle(width=3.6, height=1.9, color=INK, stroke_width=2.6)
        judg_outline.next_to(judg_lbl, DOWN, buff=0.16)
        self.play(Create(judg_outline), FadeIn(judg_lbl), run_time=0.6)

        half = Rectangle(width=3.6, height=0.95, color=ACC, stroke_width=0,
                         fill_color=ACC, fill_opacity=0.85)
        half.move_to(judg_outline.get_bottom(), aligned_edge=DOWN)
        self.play(GrowFromEdge(half, DOWN), run_time=0.7)
        not_yet = label("NOT YET PROVEN", size=15, weight="BOLD", color="#FFFFFF")
        not_yet.move_to(half)
        self.play(FadeIn(not_yet), run_time=0.4)
        self.wait(0.8)

        judg_list = VGroup(*[
            label(t, size=12, color=INK) for t in
            ("mostly disjoint concepts,\nnot real contradictions",
             "one fabrication caught\nby a human, not the system")
        ]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        # Same fit-not-guess rule as the parent: size to the zone strictly
        # above the fill, never a fixed offset that might not clear it.
        zone_top = judg_outline.get_top()[1]
        zone_bottom = half.get_top()[1]
        zone_h = zone_top - zone_bottom
        max_w = judg_outline.width - 0.3
        if judg_list.height > zone_h * 0.9:
            judg_list.scale((zone_h * 0.9) / judg_list.height)
        if judg_list.width > max_w:
            judg_list.scale(max_w / judg_list.width)
        judg_list.move_to([judg_outline.get_center()[0], (zone_top + zone_bottom) / 2, 0])
        self.play(FadeIn(judg_list), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B13_CaughtByAHuman916   (target ~20s)
# ─────────────────────────────────────────────────────────────────────────────
class B13_CaughtByAHuman916(Scene):
    TARGET = 19.86

    def construct(self):
        self.camera.background_color = BG

        quote = serif("\"Calculated the\ndebt-to-equity\nratio as 0.34\"",
                     size=24, color=INK, italic=True, line_spacing=0.8)
        src = mono("[SOURCE: SEC Filings]", size=15, color=SOFT)
        group = VGroup(quote, src).arrange(DOWN, buff=0.22).move_to([0, 2.2, 0])
        self.play(FadeIn(group), run_time=0.6)
        self.wait(1.2)

        stamp = label_chip("CAUGHT BY A HUMAN,\nNOT THE SYSTEM", ACC, size=16)
        stamp.next_to(group, DOWN, buff=0.35)
        self.play(FadeIn(stamp, scale=1.05), run_time=0.6)
        self.wait(1.2)

        told = label("told on itself, twice,\nin two days", size=17, color=SOFT,
                     line_spacing=0.8)
        told.next_to(stamp, DOWN, buff=0.28)
        self.play(FadeIn(told), run_time=0.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(group, stamp, told)), run_time=0.5)

        card_lines = VGroup(
            mono("24/24 structural passes,\n0 halts", size=15, color=INK, line_spacing=0.85),
            mono("contradiction flag:\n11/12 -> 7/12 after the fix", size=15,
                 color=ACC, line_spacing=0.85),
            mono("disjoint-concept false\npositives still open", size=15,
                 color=SOFT, line_spacing=0.85),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        card_box = auto_box(card_lines, h_pad=0.35, v_pad=0.3, color=GHOST)
        card = VGroup(card_box, card_lines).move_to([0, 0.6, 0])
        self.play(Create(card_box), run_time=0.4)
        self.play(FadeIn(card_lines), run_time=0.5)
        self.wait(1.4)

        source = label("source: logs/RUN_LOG.md, 2026-08-28/29", size=13, color=GHOST)
        source.next_to(card, DOWN, buff=0.3)
        self.play(FadeIn(source), run_time=0.4)
        self.wait(1.0)

        land = serif("proved the plumbing.\nnot yet the judgment.",
                    size=22, color=INK, line_spacing=0.9)
        land.move_to([0, -2.6, 0])
        self.play(FadeIn(land), run_time=0.6)
        hold_to(self, self.TARGET)
