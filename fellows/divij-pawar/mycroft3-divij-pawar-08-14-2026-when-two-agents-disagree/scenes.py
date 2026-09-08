"""scenes.py — Manim scenes for when-two-agents-disagree (claude-divij, Video 1).

Palette: cream #FAF9F5, ink #3D3929, terracotta #D97757, soft #73705F, ghost #A9A491.
Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF, editorial
voice only) / PT Mono (MONO, data+code only) — see graphics_lib.py. Boxes are
sized to their actual content via auto_box, never hand-measured.

Every scene ends with hold_to(self, TARGET) so its NATIVE duration matches the
beat's target length — compile.py then never has to stretch a short clip into
visible slow motion (tips.txt section 8). Re-tune the TARGET constants to
actual_duration_s after audio is generated.

Safe frame: x in [-6.4, 6.4], y in [-3.6, 3.6] (tips.txt section 7).
"""
import numpy as np
from graphics_lib import *

BG = "#FAF9F5"
INK = "#3D3929"
ACC = "#D97757"
SOFT = "#73705F"
GHOST = "#A9A491"

# EB Garamond renders word spaces too narrow to see at font_size <= 26 — verified
# by rendering the same string at 24/26/28/30/32/34/36: broken at 24 and 26,
# correct from 28 up. Montserrat and PT Mono are unaffected. It never errors and
# it is invisible at 480p, so it ships silently. graphics_lib's generic FLOOR=24
# is too low for this one font; shadow serif() here rather than editing the
# shared helper (tips.txt: copy graphics_lib.py reel-to-reel unchanged).
SERIF_FLOOR = 30
_serif = serif


def serif(text, size=34, **kw):  # noqa: F811 — deliberate shadow, see above
    return _serif(text, size=max(size, SERIF_FLOOR), **kw)


def muted_chip(text, size=24):
    """A de-emphasised chip. Never GHOST-filled — label_chip puts WHITE text on
    the fill, and white on #A9A491 is unreadable. SOFT is the muted floor."""
    return label_chip(text, SOFT, size=size)


def hold_to(scene, target, minimum=0.4):
    """Pad the scene out to `target` seconds of native runtime."""
    try:
        elapsed = float(scene.renderer.time)
    except Exception:
        scene.wait(minimum)
        return
    scene.wait(max(minimum, target - elapsed))


def agent(pos, tag=None, color=INK, r=0.42):
    """A single agent node: circle + optional tag label BELOW it (never beside —
    a sibling label reaches into the neighbouring column, tips.txt section 6)."""
    c = Circle(radius=r, color=color, stroke_width=3, fill_opacity=0.06,
               fill_color=color).move_to(pos)
    if tag is None:
        return VGroup(c)
    t = label(tag, size=24, color=color).next_to(c, DOWN, buff=0.22)
    return VGroup(c, t)


def doc(pos, tag=None, color=SOFT, w=1.25, h=1.6):
    """A document rectangle with its label stacked BELOW it.
    Index 0 is always the rectangle, index 1 the rule lines."""
    r = Rectangle(width=w, height=h, color=color, stroke_width=2.5,
                  fill_opacity=0.05, fill_color=color).move_to(pos)
    lines = VGroup(*[
        Line(r.get_left() + RIGHT * 0.2 + UP * y, r.get_right() + LEFT * 0.2 + UP * y,
             color=color, stroke_width=1.4)
        for y in (0.45, 0.2, -0.05, -0.3)
    ]).move_to(r.get_center() + UP * 0.08)
    if not tag:
        return VGroup(r, lines)
    t = label(tag, size=24, color=color).next_to(r, DOWN, buff=0.24)
    return VGroup(r, lines, t)


def fork(origin=ORIGIN, span=3.6, drop=3.2):
    """The SURFACE / RESOLVE two-path fork. Shared by B04 and B06 so the two
    beats show identical geometry (PEDAGOGY.md — series continuity)."""
    node = Dot(origin, radius=0.13, color=INK)
    node_lbl = label("DISAGREEMENT", size=24, color=INK).next_to(node, UP, buff=0.28)

    l_end = origin + LEFT * span + DOWN * drop
    r_end = origin + RIGHT * span + DOWN * drop
    l_line = Line(origin, l_end, color=GHOST, stroke_width=3)
    r_line = Line(origin, r_end, color=GHOST, stroke_width=3)

    l_txt = label("RESOLVE", size=26, color=GHOST)
    l_box = auto_box(l_txt, h_pad=0.36, v_pad=0.24, color=GHOST)
    l_grp = VGroup(l_box, l_txt).next_to(l_end, DOWN, buff=0.18)
    l_sub = label("launders shared error", size=24, color=GHOST).next_to(l_grp, DOWN, buff=0.2)

    r_txt = label("SURFACE", size=26, color=INK)
    r_box = auto_box(r_txt, h_pad=0.36, v_pad=0.24, color=INK)
    r_grp = VGroup(r_box, r_txt).next_to(r_end, DOWN, buff=0.18)
    r_sub = label("hand it to a person", size=24, color=INK).next_to(r_grp, DOWN, buff=0.2)

    return {
        "node": VGroup(node, node_lbl),
        "lines": VGroup(l_line, r_line),
        "left": VGroup(l_grp, l_sub),
        "right": VGroup(r_grp, r_sub),
        "right_box": r_box,
        "right_line": r_line,
    }


# ─────────────────────────────────────────────────────────────────────────────
#  B01_CorrectnessVsDisagreement   (target ~19s)   EXECUTIVE-SUMMARY LAW
#  Split screen: correctness needs an oracle / disagreement needs nothing.
# ─────────────────────────────────────────────────────────────────────────────
class B01_CorrectnessVsDisagreement(Scene):
    TARGET = 19.78  # actual_duration_s, Kokoro am_onyx

    def construct(self):
        self.camera.background_color = BG

        divider = DashedLine(UP * 3.2, DOWN * 3.2, color=GHOST, stroke_width=2,
                             dash_length=0.14)
        self.play(Create(divider), run_time=0.4)

        # ── LEFT: correctness ────────────────────────────────────────────────
        lx = -3.5
        l_head = label("CORRECTNESS", size=30, weight="BOLD", color=SOFT)
        l_head.move_to([lx, 3.0, 0])
        l_agent = agent([lx, 1.5, 0], "ONE AGENT", color=SOFT)
        l_ans = mono("revenue grew 12%", size=26, color=SOFT)
        l_ans_box = auto_box(l_ans, h_pad=0.34, v_pad=0.24, color=GHOST)
        VGroup(l_ans_box, l_ans).move_to([lx, -0.15, 0])

        self.play(FadeIn(l_head), FadeIn(l_agent), run_time=0.5)
        self.play(Create(l_ans_box), FadeIn(l_ans), run_time=0.5)
        self.wait(1.2)

        qmark = Text("?", font_size=88, color=GHOST).move_to([lx, -1.6, 0])
        q_cap = label("ground truth", size=24, color=GHOST).next_to(qmark, DOWN, buff=0.16)
        self.play(FadeIn(qmark, scale=0.8), FadeIn(q_cap), run_time=0.5)
        self.wait(1.4)

        l_chip = muted_chip("NEEDS AN ORACLE")
        l_chip.move_to([lx, -3.05, 0])
        self.play(FadeIn(l_chip), run_time=0.4)
        self.wait(1.4)

        # ── RIGHT: disagreement ──────────────────────────────────────────────
        rx = 3.5
        r_head = label("DISAGREEMENT", size=30, weight="BOLD", color=INK)
        r_head.move_to([rx, 3.0, 0])
        a1 = agent([rx - 1.35, 1.5, 0], "A", color=INK)
        a2 = agent([rx + 1.35, 1.5, 0], "B", color=INK)
        n1 = mono("12%", size=36, color=INK).move_to([rx - 1.35, -0.15, 0])
        n2 = mono("8%", size=36, color=INK).move_to([rx + 1.35, -0.15, 0])

        self.play(FadeIn(r_head), FadeIn(a1), FadeIn(a2), run_time=0.5)
        self.play(FadeIn(n1), FadeIn(n2), run_time=0.4)
        self.wait(1.0)

        neq = Text("≠", font_size=56, color=ACC).move_to([rx, -0.15, 0])
        self.play(FadeIn(neq, scale=1.4), run_time=0.4)
        self.wait(0.9)

        r_note = label("no oracle needed", size=24, color=SOFT).move_to([rx, -1.65, 0])
        self.play(FadeIn(r_note), run_time=0.35)
        self.wait(0.8)

        r_chip = label_chip("NEEDS NOTHING", ACC, size=24)
        r_chip.move_to([rx, -3.05, 0])
        self.play(FadeIn(r_chip), run_time=0.4)
        self.wait(1.6)

        # ── compress to one line ─────────────────────────────────────────────
        everything = VGroup(divider, l_head, l_agent, l_ans_box, l_ans, qmark,
                            q_cap, l_chip, r_head, a1, a2, n1, n2, neq, r_note, r_chip)
        self.play(FadeOut(everything, shift=DOWN * 0.25), run_time=0.7)

        thesis = serif("Not a truth detector.", size=46, color=INK)
        thesis2 = serif("A problem detector.", size=46, color=ACC)
        block = VGroup(thesis, thesis2).arrange(DOWN, buff=0.34).move_to(ORIGIN)
        self.play(FadeIn(thesis), run_time=0.5)
        self.play(FadeIn(thesis2), run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_QuoteWall   (target ~26s)
#  A plausible agent output; its reasoning greys out; then the builder wall.
# ─────────────────────────────────────────────────────────────────────────────
class B02_SelfGradedConsistency(Scene):
    TARGET = 28.48  # actual_duration_s, Kokoro am_onyx

    def construct(self):
        self.camera.background_color = BG

        # ── movement 1: the polished, uncheckable output ─────────────────────
        head = label("AGENT OUTPUT", size=26, color=SOFT)
        concl = serif("Revenue grew 12% on margin expansion.", size=34, color=INK)
        body = VGroup(
            label("Source: 10-K, FY2025, p.42", size=24, color=SOFT),
            label("Confidence: 0.91", size=24, color=SOFT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        reasoning = VGroup(
            label("REASONING", size=24, color=SOFT),
            serif("Segment mix shifted toward higher-margin", size=26, color=INK),
            serif("services, which lifted the blended rate.", size=26, color=INK),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        r_box = auto_box(reasoning, h_pad=0.36, v_pad=0.28, color=GHOST)
        r_unit = VGroup(r_box, reasoning)

        card_inner = VGroup(head, concl, body, r_unit).arrange(DOWN, buff=0.36,
                                                               aligned_edge=LEFT)
        card = auto_box(card_inner, h_pad=0.6, v_pad=0.45, color=INK, stroke_width=3)
        unit = VGroup(card, card_inner).move_to(ORIGIN)

        self.play(Create(card), run_time=0.5)
        self.play(FadeIn(head), FadeIn(concl), run_time=0.5)
        self.play(FadeIn(body), run_time=0.4)
        self.wait(2.4)
        self.play(Create(r_box), FadeIn(reasoning), run_time=0.6)
        self.wait(2.6)

        self.play(
            reasoning.animate.set_opacity(0.28),
            r_box.animate.set_stroke(color=GHOST, width=1.5),
            run_time=0.6,
        )
        cap = label("THIS IS ALSO A GENERATED ARTIFACT", size=26, color=ACC)
        cap.next_to(card, DOWN, buff=0.35)
        if cap.get_bottom()[1] < -3.5:
            cap.move_to([0, -3.35, 0])
        self.play(FadeIn(cap), run_time=0.45)
        self.wait(3.0)

        self.play(FadeOut(unit), FadeOut(cap), run_time=0.6)

        # ── movement 2: the same output, multiplied ──────────────────────────
        # No named individuals, no specific incident — the point is structural
        # (any self-graded system looks consistent), so the visual is anonymous
        # icons, not attributed quotes.
        head2 = label("GRADED ONLY BY ITS OWN OUTPUT", size=26, color=SOFT)
        head2.move_to([0, 2.9, 0])
        self.play(FadeIn(head2), run_time=0.4)

        cols, rows_n = 3, 2
        xs = np.linspace(-3.4, 3.4, cols)
        ys = [1.15, -0.35]
        icons = VGroup()
        stamps = VGroup()
        for y in ys:
            for x in xs:
                ic = agent([x, y, 0], color=GHOST, r=0.5)
                st = checked("CONSISTENT", size=20, color=SOFT).next_to(
                    ic, DOWN, buff=0.16)
                icons.add(ic)
                stamps.add(st)

        self.play(LaggedStart(*[FadeIn(g, scale=0.8) for g in icons],
                              lag_ratio=0.14), run_time=1.4)
        self.play(LaggedStart(*[FadeIn(s) for s in stamps], lag_ratio=0.12),
                  run_time=1.2)
        self.wait(1.4)

        cap2 = label("CONSISTENCY IS ALL IT WAS EVER ASKED TO PRODUCE",
                     size=26, weight="BOLD", color=ACC)
        cap2.move_to([0, -2.65, 0])
        self.play(FadeIn(cap2), run_time=0.45)
        self.wait(2.2)

        wall = VGroup(head2, icons, stamps, cap2)
        self.play(FadeOut(wall, shift=UP * 0.2), run_time=0.6)

        final = VGroup(
            label("THE SYSTEM RUNS.", size=40, weight="BOLD", color=INK),
            label("THAT WAS NEVER PROOF IT'S RIGHT.", size=36, weight="BOLD", color=ACC),
        ).arrange(DOWN, buff=0.34).move_to(ORIGIN)
        self.play(FadeIn(final[0]), run_time=0.45)
        self.play(FadeIn(final[1]), run_time=0.45)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_AskItTwice   (target ~26s)
#  Self-consistency, the docstring, and the agreement/disagreement asymmetry.
# ─────────────────────────────────────────────────────────────────────────────
class B03_AskItTwice(Scene):
    TARGET = 32.23  # actual_duration_s, Kokoro am_onyx

    def construct(self):
        self.camera.background_color = BG

        # ── one agent, run twice ─────────────────────────────────────────────
        src = agent([0, 2.5, 0], "ONE MODEL", color=INK)
        self.play(FadeIn(src), run_time=0.45)

        c1 = mono("12%", size=32, color=INK).move_to([-2.7, 0.5, 0])
        c1b = auto_box(c1, h_pad=0.4, v_pad=0.28, color=GHOST)
        c2 = mono("12%", size=32, color=INK).move_to([2.7, 0.5, 0])
        c2b = auto_box(c2, h_pad=0.4, v_pad=0.28, color=GHOST)
        l1 = Line(src[0].get_bottom() + DOWN * 0.55, c1b.get_top(), color=GHOST, stroke_width=2.5)
        l2 = Line(src[0].get_bottom() + DOWN * 0.55, c2b.get_top(), color=GHOST, stroke_width=2.5)
        run1 = label("run 1", size=24, color=SOFT).next_to(c1b, DOWN, buff=0.2)
        run2 = label("run 2", size=24, color=SOFT).next_to(c2b, DOWN, buff=0.2)

        self.play(Create(l1), Create(l2), run_time=0.45)
        self.play(FadeIn(c1b), FadeIn(c1), FadeIn(c2b), FadeIn(c2),
                  FadeIn(run1), FadeIn(run2), run_time=0.5)
        self.wait(1.0)

        meter_bg = Rectangle(width=3.0, height=0.34, color=GHOST, stroke_width=2)
        meter_bg.move_to([0, -1.5, 0])
        meter_fill = Rectangle(width=0.01, height=0.34, color=SOFT,
                               fill_opacity=1, stroke_width=0)
        meter_fill.align_to(meter_bg, LEFT).set_y(-1.5)
        meter_lbl = label("overlap", size=24, color=SOFT).next_to(meter_bg, DOWN, buff=0.22)
        self.play(FadeIn(meter_bg), FadeIn(meter_lbl), run_time=0.35)
        self.play(meter_fill.animate.stretch_to_fit_width(2.85).align_to(meter_bg, LEFT),
                  run_time=1.0)
        self.wait(2.1)

        stage1 = VGroup(src, l1, l2, c1b, c1, c2b, c2, run1, run2,
                        meter_bg, meter_fill, meter_lbl)
        self.play(FadeOut(stage1), run_time=0.55)

        # ── the docstring, verbatim (VERBATIM QUOTE LAW) ─────────────────────
        d1 = mono("Two identical confabulations", size=28, color=INK)
        d2 = mono("are still confabulations.", size=28, color=INK)
        d3 = mono("High consistency = weak positive evidence.", size=26, color=SOFT)
        d4 = mono("Low  consistency = strong negative evidence.", size=26, color=INK)
        block = VGroup(d1, d2, d3, d4).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        VGroup(d3, d4).shift(DOWN * 0.18)
        card = auto_box(block, h_pad=0.55, v_pad=0.45, color=GHOST, fill_opacity=0.04)
        unit = VGroup(card, block).move_to(ORIGIN)
        src_tag = label("consistency.py", size=24, color=SOFT).next_to(card, UP, buff=0.24)

        self.play(Create(card), FadeIn(src_tag), run_time=0.5)
        self.play(FadeIn(d1), FadeIn(d2), run_time=0.5)
        self.wait(2.5)
        self.play(FadeIn(d3), run_time=0.4)
        self.wait(1.5)
        self.play(FadeIn(d4), run_time=0.4)
        self.wait(3.0)
        self.play(FadeOut(unit), FadeOut(src_tag), run_time=0.5)

        # ── the asymmetry, as two chips ──────────────────────────────────────
        head = label("THE ASYMMETRY", size=28, weight="BOLD", color=SOFT)
        head.move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.35)

        ag_t = label("AGREEMENT", size=30, weight="BOLD", color=GHOST)
        ag_b = auto_box(ag_t, h_pad=0.4, v_pad=0.28, color=GHOST)
        ag = VGroup(ag_b, ag_t).move_to([-3.3, 1.7, 0])
        ag_s = label("proves almost\nnothing", size=26, color=GHOST,
                     line_spacing=0.6).next_to(ag, DOWN, buff=0.3)

        dg_t = label("DISAGREEMENT", size=30, weight="BOLD", color=INK)
        dg_b = auto_box(dg_t, h_pad=0.4, v_pad=0.28, color=ACC, stroke_width=4)
        dg = VGroup(dg_b, dg_t).move_to([3.3, 1.7, 0])
        dg_s = label("proves something\nreal", size=26, color=INK,
                     line_spacing=0.6).next_to(dg, DOWN, buff=0.3)

        self.play(FadeIn(ag), FadeIn(ag_s), run_time=0.45)
        self.wait(1.5)
        self.play(FadeIn(dg), FadeIn(dg_s), run_time=0.45)
        self.wait(2.5)

        # ── change who answers ───────────────────────────────────────────────
        # Agents sit at -1.4 so their tags bottom out near -2.2, leaving a full
        # unit of clearance above the caption (tips.txt section 6).
        two = VGroup(
            agent([-1.5, -1.4, 0], "MODEL A", color=INK),
            agent([1.5, -1.4, 0], "MODEL B", color=ACC),
        )
        cap = label("SAME QUESTION. DIFFERENT ANSWERER.", size=26, color=SOFT)
        cap.move_to([0, -3.2, 0])
        self.play(FadeIn(two, scale=0.9), run_time=0.5)
        self.play(FadeIn(cap), run_time=0.4)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_TwoTraps   (target ~27s)
#  Trap 1 information asymmetry; trap 2 correlated majority. Ends on the fork.
# ─────────────────────────────────────────────────────────────────────────────
class B04_TwoTraps(Scene):
    TARGET = 29.57  # actual_duration_s, Kokoro am_onyx

    def construct(self):
        self.camera.background_color = BG

        t1 = label("TRAP ONE · INFORMATION ASYMMETRY", size=28,
                   weight="BOLD", color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(t1), run_time=0.4)

        a1 = agent([-2.4, 1.6, 0], "A", color=INK)
        a2 = agent([2.4, 1.6, 0], "B", color=INK)
        d_one = doc([0, -0.9, 0], "ONE SOURCE", color=SOFT)
        e1 = Line(a1.get_bottom() + DOWN * 0.1, d_one[0].get_top() + LEFT * 0.3, color=GHOST, stroke_width=2.5)
        e2 = Line(a2.get_bottom() + DOWN * 0.1, d_one[0].get_top() + RIGHT * 0.3, color=GHOST, stroke_width=2.5)

        self.play(FadeIn(a1), FadeIn(a2), run_time=0.4)
        self.play(FadeIn(d_one), Create(e1), Create(e2), run_time=0.5)
        self.wait(2.0)

        chip1 = muted_chip("PERSUASION CONTEST").move_to([0, -3.2, 0])
        self.play(FadeIn(chip1), run_time=0.4)
        self.wait(2.2)

        # documents split
        d_l = doc([-2.4, -0.9, 0], "10K FILING", color=INK)
        d_r = doc([2.4, -0.9, 0], "EARNINGS CALL", color=INK)
        f1 = Line(a1.get_bottom() + DOWN * 0.1, d_l[0].get_top(), color=INK, stroke_width=2.5)
        f2 = Line(a2.get_bottom() + DOWN * 0.1, d_r[0].get_top(), color=INK, stroke_width=2.5)
        chip2 = label_chip("DIFFERENT EVIDENCE", ACC, size=24).move_to([0, -3.2, 0])

        self.play(FadeOut(d_one), FadeOut(e1), FadeOut(e2), FadeOut(chip1), run_time=0.4)
        self.play(FadeIn(d_l), FadeIn(d_r), Create(f1), Create(f2), run_time=0.6)
        self.play(FadeIn(chip2), run_time=0.35)
        self.wait(2.5)

        stage1 = VGroup(t1, a1, a2, d_l, d_r, f1, f2, chip2)
        self.play(FadeOut(stage1), run_time=0.5)

        # ── TRAP TWO ─────────────────────────────────────────────────────────
        t2 = label("TRAP TWO · THE CORRELATED MAJORITY", size=28,
                   weight="BOLD", color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(t2), run_time=0.4)

        xs = [-3.4, 0.0, 3.4]
        agents3 = VGroup(*[agent([x, 1.55, 0], t, color=INK)
                           for x, t in zip(xs, ["A", "B", "C"])])
        votes = VGroup(*[mono("12%", size=28, color=INK).move_to([x, 0.15, 0]) for x in xs])
        self.play(FadeIn(agents3), run_time=0.45)
        self.play(FadeIn(votes), run_time=0.4)
        self.wait(1.5)

        tally_t = label("MAJORITY\nVOTE", size=26, weight="BOLD", color=INK,
                        line_spacing=0.6)
        tally_b = auto_box(tally_t, h_pad=0.42, v_pad=0.28, color=INK)
        tally = VGroup(tally_b, tally_t).move_to([0, -1.35, 0])
        tally_top_y = tally_b.get_top()[1]
        vlines = VGroup(*[
            Line([x, -0.2, 0], [x * 0.25, tally_top_y, 0], color=GHOST, stroke_width=2.5)
            for x in xs
        ])
        answer = mono("12%", size=34, color=INK).move_to([0, -2.75, 0])
        ans_box = auto_box(answer, h_pad=0.42, v_pad=0.26, color=INK)

        self.play(Create(vlines), run_time=0.4)
        self.play(FadeIn(tally), run_time=0.4)
        self.play(FadeIn(ans_box), FadeIn(answer), run_time=0.4)
        self.wait(2.2)

        # replay: one shared source feeds all three
        shared = doc([-1.9, 3.0, 0], color=ACC, w=1.05, h=0.85)
        shared_lbl = label("ONE SHARED DISTRIBUTION", size=24, color=ACC)
        shared_lbl.next_to(shared[0], RIGHT, buff=0.32)
        slines = VGroup(*[Line(shared[0].get_bottom(), [x, 1.55 + 0.42, 0],
                               color=ACC, stroke_width=2.2) for x in xs])
        self.play(FadeOut(t2), run_time=0.25)
        self.play(FadeIn(shared[0]), FadeIn(shared[1]), FadeIn(shared_lbl), run_time=0.45)
        self.play(Create(slines), run_time=0.55)
        self.wait(1.8)

        stamp_t = label("WRONG", size=34, weight="BOLD", color=ACC)
        stamp_b = auto_box(stamp_t, h_pad=0.34, v_pad=0.2, color=ACC, stroke_width=4)
        stamp = VGroup(stamp_b, stamp_t).move_to(ans_box.get_center() + RIGHT * 2.6)
        self.play(FadeIn(stamp, scale=1.3), run_time=0.45)
        self.wait(2.5)

        stage2 = VGroup(agents3, votes, tally, vlines, answer, ans_box,
                        shared[0], shared[1], shared_lbl, slines, stamp)
        self.play(FadeOut(stage2), run_time=0.5)

        # ── the fork ─────────────────────────────────────────────────────────
        f = fork(origin=[0, 2.75, 0])
        self.play(FadeIn(f["node"]), run_time=0.35)
        self.play(Create(f["lines"]), run_time=0.5)
        self.play(FadeIn(f["left"]), FadeIn(f["right"]), run_time=0.5)
        self.play(f["right_box"].animate.set_stroke(color=ACC, width=5),
                  f["right_line"].animate.set_stroke(color=ACC, width=4),
                  run_time=0.5)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_FourKindsAndFunnel   (target ~31s)
#  The four-way taxonomy, then staged detection.
# ─────────────────────────────────────────────────────────────────────────────
class B05_FourKindsAndFunnel(Scene):
    TARGET = 37.72  # actual_duration_s, Kokoro am_onyx

    CARDS = [
        ("STYLISTIC",       "same substance,\ndifferent phrasing"),
        ("REASONING",       "different paths,\ndifferent conclusions"),
        ("HIGH-\nCONFIDENCE", "both sure,\nmutually exclusive"),
        ("ADVERSARIAL",     "agents faking\nagreement"),
    ]

    def construct(self):
        self.camera.background_color = BG

        head = label("FOUR KINDS OF DISAGREEMENT", size=28, weight="BOLD",
                     color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.4)

        centers = [[-3.3, 1.15, 0], [3.3, 1.15, 0], [-3.3, -1.75, 0], [3.3, -1.75, 0]]
        cards, boxes, titles = VGroup(), [], []
        for (nm, sub), c in zip(self.CARDS, centers):
            t = label(nm, size=28, weight="BOLD", color=INK, line_spacing=0.6)
            s = label(sub, size=24, color=SOFT, line_spacing=0.6)
            inner = VGroup(t, s).arrange(DOWN, buff=0.26)
            b = auto_box(inner, h_pad=0.55, v_pad=0.36, color=GHOST)
            grp = VGroup(b, inner).move_to(c)
            cards.add(grp)
            boxes.append(b)
            titles.append(t)

        for grp in cards:
            self.play(FadeIn(grp, scale=0.94), run_time=0.4)
            self.wait(1.6)

        self.wait(0.6)
        noise = label("NOISE", size=26, weight="BOLD", color=GHOST)
        noise.next_to(cards[0], UP, buff=0.20)
        signal = label("SIGNAL", size=26, weight="BOLD", color=ACC)
        signal.next_to(cards[1], UP, buff=0.20)

        self.play(cards[0].animate.set_opacity(0.32), FadeIn(noise), run_time=0.5)
        self.play(boxes[1].animate.set_stroke(color=ACC, width=4),
                  boxes[2].animate.set_stroke(color=ACC, width=4),
                  FadeIn(signal), run_time=0.5)
        self.wait(4.0)

        self.play(FadeOut(cards), FadeOut(noise), FadeOut(signal),
                  FadeOut(head), run_time=0.55)

        # ── staged detection funnel ──────────────────────────────────────────
        head2 = label("STAGED DETECTION", size=28, weight="BOLD",
                      color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(head2), run_time=0.35)

        top_y, mid_y, bot_y = 1.75, -0.35, -2.0
        fx = -1.35                      # funnel centre, left of frame centre so
                                        # the 73% arrow balances the composition
        funnel = Polygon(
            [fx - 3.0, top_y, 0], [fx + 3.0, top_y, 0],
            [fx + 0.8, mid_y, 0], [fx - 0.8, mid_y, 0],
            color=INK, stroke_width=3, fill_opacity=0.05, fill_color=SOFT,
        )
        f_lbl = label("CHEAP EMBEDDING CLASSIFIER", size=26, color=INK)
        f_lbl.next_to(funnel, UP, buff=0.28)
        self.play(Create(funnel), FadeIn(f_lbl), run_time=0.7)
        self.wait(1.6)

        out_arrow = Arrow([fx + 2.4, mid_y + 0.62, 0], [fx + 4.5, mid_y + 0.62, 0],
                          color=SOFT, stroke_width=4, buff=0.05,
                          max_tip_length_to_length_ratio=0.16)
        out_num = mono("73%", size=36, color=INK).move_to([fx + 5.35, mid_y + 1.05, 0])
        out_cap = label("no model call", size=24, color=SOFT).move_to([fx + 5.35, mid_y + 0.2, 0])
        self.play(Create(out_arrow), FadeIn(out_num), FadeIn(out_cap), run_time=0.6)
        self.wait(2.2)

        neck = label("threshold 0.7", size=24, color=SOFT).move_to([fx, mid_y - 0.42, 0])
        judge_t = label("LLM JUDGE", size=28, weight="BOLD", color=INK)
        judge_b = auto_box(judge_t, h_pad=0.45, v_pad=0.3, color=INK)
        judge = VGroup(judge_b, judge_t).move_to([fx, bot_y - 0.3, 0])
        drop = Line([fx, mid_y - 0.72, 0], judge_b.get_top(), color=INK, stroke_width=3)

        self.play(FadeIn(neck), run_time=0.35)
        self.play(Create(drop), FadeIn(judge), run_time=0.5)
        self.wait(2.0)

        figs = VGroup(
            mono("-62% API COST", size=28, color=INK),
            mono("90.8% ACCURACY", size=28, color=INK),
        # NOT at the judge's y — the figures row is ~6 units wide and its left
        # edge reaches back under the judge box, colliding with "LLM JUDGE".
        ).arrange(RIGHT, buff=1.1).move_to([0, -3.15, 0])
        self.play(FadeIn(figs), run_time=0.5)
        self.wait(3.0)

        self.play(FadeOut(VGroup(head2, funnel, f_lbl, out_arrow, out_num,
                                 out_cap, neck, drop, judge, figs)), run_time=0.5)
        cap = VGroup(
            label("A CHECK YOU CAN AFFORD", size=36, weight="BOLD", color=INK),
            label("TO RUN ON EVERYTHING", size=36, weight="BOLD", color=ACC),
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(cap[0]), run_time=0.4)
        self.play(FadeIn(cap[1]), run_time=0.4)
        hold_to(self, self.TARGET)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_AblationAndFork   (target ~34s)
#  A mature pipeline at scale, the ablation, and the fork resolving to SURFACE.
# ─────────────────────────────────────────────────────────────────────────────
class B06_AblationAndFork(Scene):
    TARGET = 43.97  # actual_duration_s, Kokoro am_onyx

    ROWS = [
        ("full system",                 0.889, "",       INK),
        ("without adversarial debate",  0.770, "-0.119", ACC),
        ("without terminal audit",      0.845, "-0.044", SOFT),
        ("without chain-of-custody",    0.857, "-0.032", SOFT),
        ("without authority weighting", 0.883, "-0.006", SOFT),
    ]

    def construct(self):
        self.camera.background_color = BG

        # ── movement 1: the pipeline, as scale only ──────────────────────────
        head = label("A MATURE PIPELINE", size=30, weight="BOLD", color=INK).move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.4)

        dots = VGroup()
        conns = VGroup()
        xs = np.linspace(-5.2, 5.2, 9)
        for i, x in enumerate(xs):
            y = 1.05 + (0.5 if i % 2 else -0.5) * 0.62
            d = Circle(radius=0.32, color=INK, stroke_width=2.5,
                       fill_opacity=0.08, fill_color=INK).move_to([x, y, 0])
            dots.add(d)
            if i:
                conns.add(Line(dots[i - 1].get_right(), d.get_left(),
                               color=GHOST, stroke_width=2))
        sub = label("several agents · many phases", size=28, color=SOFT).move_to([0, -0.85, 0])

        self.play(LaggedStart(*[FadeIn(d, scale=0.7) for d in dots],
                              lag_ratio=0.09), run_time=1.6)
        self.play(Create(conns), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.35)
        self.wait(1.4)

        chip = muted_chip("HUNDREDS OF QUESTIONS").move_to([0, -2.35, 0])
        self.play(FadeIn(chip), run_time=0.4)
        self.wait(2.0)
        self.play(FadeOut(VGroup(head, dots, conns, sub, chip)), run_time=0.5)

        # ── movement 2: the ablation ─────────────────────────────────────────
        head2 = label("FAITHFULNESS, ABLATED", size=28, weight="BOLD",
                      color=SOFT).move_to([0, 3.3, 0])
        self.play(FadeIn(head2), run_time=0.35)

        # x0 chosen so the whole composition (name column + bar + number column)
        # centres on the frame, not just the bars.
        x0, scale, base = -0.15, 7.5, 0.55
        ys = [2.25, 1.15, 0.05, -1.05, -2.15]
        for (name, val, delta, col), y in zip(self.ROWS, ys):
            nm = label(name, size=24, color=col if col is not SOFT else INK)
            nm.move_to([x0 - 0.35, y, 0], aligned_edge=RIGHT)
            bar = Rectangle(width=max(val - base, 0.02) * scale, height=0.40,
                            color=col, fill_opacity=0.85 if col is ACC else 0.35,
                            fill_color=col, stroke_width=2)
            bar.move_to([x0, y, 0], aligned_edge=LEFT)
            num = mono(("%0.3f" % val) + ("   " + delta if delta else ""),
                       size=24, color=col if col is ACC else SOFT)
            num.next_to(bar, RIGHT, buff=0.28)
            self.play(FadeIn(nm), GrowFromEdge(bar, LEFT), FadeIn(num), run_time=0.55)
            self.wait(1.4 if col is ACC else 0.6)

        # The bar axis starts at 0.55, not 0 — say so rather than let a truncated
        # axis quietly overstate the differences.
        axis_note = label("bar scale starts at 0.55", size=24, color=GHOST)
        axis_note.move_to([x0 + 1.6, -3.15, 0])
        self.play(FadeIn(axis_note), run_time=0.35)
        self.wait(2.0)
        self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=0.55)

        # ── the two boxes ────────────────────────────────────────────────────
        b1_t = VGroup(
            label("HAVING AN", size=26, color=INK),
            label("ADVERSARIAL CHECK", size=26, color=INK),
            mono("-0.119", size=40, color=ACC),
        ).arrange(DOWN, buff=0.22)
        b1 = auto_box(b1_t, h_pad=0.55, v_pad=0.4, color=ACC, stroke_width=4)
        g1 = VGroup(b1, b1_t).move_to([-3.2, 0.6, 0])

        b2_t = VGroup(
            label("TUNING HOW YOU", size=26, color=SOFT),
            label("WEIGHT SOURCES", size=26, color=SOFT),
            mono("-0.006", size=40, color=SOFT),
        ).arrange(DOWN, buff=0.22)
        b2 = auto_box(b2_t, h_pad=0.55, v_pad=0.4, color=GHOST)
        g2 = VGroup(b2, b2_t).move_to([3.2, 0.6, 0])

        self.play(FadeIn(g1), run_time=0.45)
        self.wait(1.0)
        self.play(FadeIn(g2), run_time=0.45)
        self.wait(2.6)
        self.play(FadeOut(g1), FadeOut(g2), run_time=0.5)

        # ── movement 3: the fork resolves ────────────────────────────────────
        f = fork(origin=[0, 2.75, 0])
        self.play(FadeIn(f["node"]), Create(f["lines"]), run_time=0.6)
        self.play(FadeIn(f["left"]), FadeIn(f["right"]), run_time=0.5)
        self.wait(1.4)
        self.play(f["left"].animate.set_opacity(0.25),
                  f["right_box"].animate.set_stroke(color=ACC, width=5),
                  f["right_line"].animate.set_stroke(color=ACC, width=4),
                  run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(VGroup(f["node"], f["lines"], f["left"], f["right"])),
                  run_time=0.5)

        final = VGroup(
            serif("Machines verify conformance.", size=40, color=INK),
            serif("Humans verify adequacy.", size=40, color=ACC),
        ).arrange(DOWN, buff=0.34).move_to(ORIGIN)
        self.play(FadeIn(final[0]), run_time=0.5)
        self.play(FadeIn(final[1]), run_time=0.5)
        hold_to(self, self.TARGET)
