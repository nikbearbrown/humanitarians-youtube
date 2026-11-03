"""scenes.py — Manim scenes for how-do-you-know-it-worked (claude-divij).

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757, soft #73705F,
ghost #A9A491 — the Claude fidelity palette per ai-explainer SKILL.md. ONE
accent per beat. The source script's [VISUAL] color cues ("green checkmark",
"red strike") are deliberately NOT carried literally, same retint rule used
on why-agents-fail (STEM2): good/bad is carried by label, position, and
ink-vs-terracotta, so the frame stays legible in grayscale and under any
colour vision. No blue, no green, no red.

Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF,
editorial voice only) / PT Mono (MONO, logs + code + data only) — see
graphics_lib.py. Boxes are content-fitted via auto_box, never hand-measured.
graphics_lib.py's label()/title()/serif()/mono() apply the house
letter_spacing correction automatically — this file never calls raw Text()
for body copy.

Pace: normal-speed creates/fades with deliberate HOLDS sized to the
narration. Targets below are against `estimated_duration_s` in
beat_sheet.json; RETIME against `actual_duration_s` once Kokoro has run
(see BUILD-PROMPT.md Step 3 — not yet done, this reel is pre-audio / GATE P).

The three-mechanism legend persists across B01 (named, empty) through B09
(collapsed into rules) as the reel's spine — the active mechanism is the
only terracotta element in frame, mirroring the four-mode legend pattern
used in why-agents-fail (STEM2). B02-B06 additionally thread ONE worked
example (the "34% YoY, source: 10-K" line, declared illustrative in
SOURCES.md) through claim extraction, verification, and consistency
probing, so the worked example is walked live rather than three unrelated
illustrations.
"""
import numpy as np
from graphics_lib import *

# ── Palette (claude-stage retint, per ai-explainer SKILL.md) ──────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")

MECHS = ["Claim Extraction", "Verify Reality", "Consistency Probe"]
LEGEND_MAX_W = 12.4   # title-safe span (SAFE x is ~-6.3..6.3 of a 14.22u frame)


def mech_legend(active=None, lit=(), y=3.25):
    """The three-mechanism spine, parked at the top of frame.

    `active` (0-2) renders terracotta; anything in `lit` renders ink (already
    covered); everything else stays ghost. Returns a VGroup of labels.
    """
    chips = VGroup()
    for i, name in enumerate(MECHS):
        if i == active:
            col, wt = ACC, "BOLD"
        elif i in lit:
            col, wt = INK, None
        else:
            col, wt = GHOST, None
        chips.add(label(name, size=24, color=col, weight=wt))
    chips.arrange(RIGHT, buff=0.6)
    if chips.width > LEGEND_MAX_W:
        chips.scale(LEGEND_MAX_W / chips.width)
    chips.move_to([0, y, 0])
    return chips


def strike(mobj, color=None):
    """A struck-through line sized to the mobject it cancels."""
    return Line(mobj.get_left() + LEFT * 0.08, mobj.get_right() + RIGHT * 0.08,
                color=color if color is not None else ACC, stroke_width=3.0)


WORKED_LINE = "Revenue grew 34% YoY, driven by international\nexpansion — source: 10-K"


# ─────────────────────────────────────────────────────────────────────────────
#  B01_TheTrustProblem   (target ~45s)
#  Executive-summary beat: the reasoning-vs-narration gap, the thesis line,
#  then the three mechanisms previewed as empty panels — before any is filled.
# ─────────────────────────────────────────────────────────────────────────────
class B01_TheTrustProblem(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Trust Problem", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.31)

        # ── Split screen: blank reality vs. confident narration ───────────────
        L, R = -3.6, 3.6
        h_left = label("What Actually\nHappened", size=26, color=SOFT, line_spacing=0.85)
        h_right = label("What the Model\nSays Happened", size=26, color=SOFT, line_spacing=0.85)
        box_l = Rectangle(width=4.6, height=3.0, stroke_width=2.5, color=GHOST,
                           fill_color=GHOST, fill_opacity=0.06).move_to([L, -0.2, 0])
        box_r = Rectangle(width=4.6, height=3.0, stroke_width=2.5, color=INK,
                           fill_color=INK, fill_opacity=0.04).move_to([R, -0.2, 0])
        h_left.next_to(box_l, UP, buff=0.25)
        h_right.next_to(box_r, UP, buff=0.25)
        self.play(Create(box_l), Create(box_r), FadeIn(h_left), FadeIn(h_right),
                   run_time=0.8)
        self.wait(1.96)

        qmark = label("?", size=54, color=GHOST).move_to(box_l)
        prose = VGroup(*[
            label(ln, size=20, color=INK) for ln in (
                "\"I checked the numbers,\"",
                "\"cross-referenced the filing,\"",
                "\"and concluded X.\"",
            )
        ]).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        if prose.width > box_r.width - 0.5:
            prose.scale((box_r.width - 0.5) / prose.width)
        prose.move_to(box_r)
        self.play(FadeIn(qmark), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(p) for p in prose], lag_ratio=0.3), run_time=1.0)
        self.wait(2.62)

        # Anchored BELOW both boxes at a fixed y, not box_l.get_right()/
        # box_r.get_left() — those return the edge midpoint, which sits at
        # the boxes' vertical center (y=-0.2) and drew the dashed line and
        # its label directly through the right box's text (caught in
        # mid-scene QC). A fixed y below both boxes' bottom edge (-1.7)
        # clears the text entirely.
        conn_y = box_l.get_bottom()[1] - 0.35
        dotted = DashedLine([box_l.get_right()[0], conn_y, 0],
                             [box_r.get_left()[0], conn_y, 0], color=SOFT,
                             stroke_width=2.5, dash_length=0.15)
        dlab = label("assumed to be the same thing", size=24, color=SOFT)
        dlab.next_to(dotted, DOWN, buff=0.2)
        self.play(Create(dotted), FadeIn(dlab), run_time=0.7)
        self.wait(2.95)

        fluency = label("fluency and accuracy are different properties",
                         size=23, color=SOFT).move_to(DOWN * 3.0)
        self.play(FadeIn(fluency), run_time=0.5)
        self.wait(3.6)

        # ── The thesis line, alone on screen ───────────────────────────────────
        self.play(FadeOut(VGroup(box_l, box_r, h_left, h_right, qmark, prose,
                                  dotted, dlab, fluency)), run_time=0.6)
        thesis = serif("The log is evidence of output —\nnot evidence of process.",
                        size=36, color=ACC, line_spacing=1.0).move_to(UP * 0.2)
        self.play(Write(thesis), run_time=1.2)
        self.wait(4.91)

        question = label("can it be checked against something outside the model?",
                          size=25, color=INK).move_to(DOWN * 2.4)
        self.play(FadeIn(question), run_time=0.6)
        self.wait(3.27)

        # ── Frame preview: three mechanisms, named, empty ─────────────────────
        self.play(FadeOut(thesis), FadeOut(question), run_time=0.5)
        txts = [label(n.replace(" ", "\n"), size=25, color=SOFT, line_spacing=0.8)
                for n in MECHS]
        pw = max(x.width for x in txts) + 0.65
        ph = max(x.height for x in txts) + 0.70
        panels = VGroup(*[
            VGroup(Rectangle(width=pw, height=ph, stroke_width=2.5, color=GHOST,
                              fill_color=GHOST, fill_opacity=0.08).move_to(x), x)
            for x in txts
        ]).arrange(RIGHT, buff=0.5)
        if panels.width > 11.5:
            panels.scale(11.5 / panels.width)
        panels.move_to(DOWN * 0.2)

        for p in panels:
            self.play(FadeIn(p, shift=UP * 0.25), run_time=0.45)
            self.wait(0.73)
        self.wait(1.64)

        tick = Triangle(color=ACC, fill_color=ACC, fill_opacity=1.0,
                         stroke_width=0).scale(0.16).rotate(PI)
        tick.next_to(panels[0], UP, buff=0.22)
        self.play(FadeIn(tick, shift=DOWN * 0.15), run_time=0.4)
        self.wait(5.89)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_ClaimExtraction   (target ~63s)
#  A wall of prose feeds through a shredder and comes out as four typed
#  claim-type index cards; one worked line then gets tagged three ways at once.
# ─────────────────────────────────────────────────────────────────────────────
class B02_ClaimExtraction(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mech_legend(active=0)
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(1.33)

        # ── The wall of prose ──────────────────────────────────────────────────
        prose_lines = VGroup(*[
            label(ln, size=19, color=SOFT) for ln in (
                "the reasoning trace is dense, confident prose",
                "one continuous story, hard to check as a whole",
                "so it gets fed through a parser instead",
            )
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        prose_box = auto_box(prose_lines, h_pad=0.4, v_pad=0.3, color=SOFT)
        prose = VGroup(prose_box, prose_lines).move_to(UP * 1.9)
        self.play(Create(prose_box), FadeIn(prose_lines), run_time=0.8)
        self.wait(4.79)

        # ── The shredder ───────────────────────────────────────────────────────
        shred_w = prose_box.width * 0.9
        teeth = VGroup(*[
            Triangle(color=INK, fill_color=INK, fill_opacity=1.0, stroke_width=0)
            .scale(0.12).rotate(PI)
            for _ in range(9)
        ]).arrange(RIGHT, buff=0.08)
        shred_body = Rectangle(width=shred_w, height=0.5, stroke_width=2,
                                color=INK, fill_color=INK, fill_opacity=0.06)
        shredder = VGroup(shred_body, teeth.move_to(shred_body.get_bottom()))
        shredder.move_to(UP * 0.55)
        self.play(Create(shredder), run_time=0.6)
        self.play(prose.animate.next_to(shredder, UP, buff=0.05), run_time=0.5)
        self.wait(1.6)
        self.play(prose.animate.shift(DOWN * 0.9).set_opacity(0.0), run_time=0.9)
        # The shredder itself was never removed here — it lingered behind/
        # through the card row for the rest of the scene (caught in
        # mid-scene QC, invisible in a final-frame-only check since the
        # cards visually dominate by then).
        self.play(FadeOut(shredder), FadeOut(prose), run_time=0.4)
        self.wait(0.4)

        # ── Four cards emerge, the real ClaimType set ─────────────────────────
        names = ["CITATION", "QUANTITATIVE", "HEDGE", "CAUSAL"]
        cards = VGroup()
        for name in names:
            head = label(name, size=23, color=ACC, weight="BOLD")
            box = auto_box(head, h_pad=0.32, v_pad=0.24, color=INK,
                            fill_color=BG, fill_opacity=1.0)
            cards.add(VGroup(box, head))
        cards.arrange(RIGHT, buff=0.35)
        if cards.width > 12.4:
            cards.scale(12.4 / cards.width)
        cards.move_to(UP * 0.1)

        for c in cards:
            self.play(FadeIn(c, shift=DOWN * 0.3), run_time=0.4)
            self.wait(1.86)
        self.wait(2.13)

        code = mono("ClaimType: citation | quantitative | hedge | causal",
                     size=17, color=SOFT)
        code.next_to(cards, DOWN, buff=0.35)
        self.play(FadeIn(code), run_time=0.5)
        self.wait(4.79)

        # ── The worked example, tagged three ways at once ─────────────────────
        self.play(FadeOut(code), run_time=0.3)
        worked = mono(WORKED_LINE, size=18, color=INK, line_spacing=1.0)
        worked.move_to(DOWN * 1.5)
        self.play(FadeIn(worked), run_time=0.6)
        self.wait(3.73)

        # Draw a tag-line from the worked example to each matching card.
        targets = {0: cards[0], 1: cards[1], 3: cards[3]}  # CITATION, QUANTITATIVE, CAUSAL
        lines = VGroup()
        for idx in targets:
            ln = DashedLine(worked.get_top(), targets[idx].get_bottom(),
                             color=ACC, stroke_width=2, dash_length=0.12)
            lines.add(ln)
            targets[idx][1].set_color(ACC)
        self.play(*[Create(ln) for ln in lines], run_time=0.9)
        self.wait(5.33)

        hedges = label("approximately · unclear · assumed", size=21, color=GHOST)
        hedges.next_to(worked, DOWN, buff=0.4)
        self.play(FadeIn(hedges), run_time=0.5)
        self.wait(4.79)

        caption = label("no second AI — just pattern matching", size=25, color=INK)
        caption.move_to(DOWN * 3.15)
        self.play(FadeOut(hedges), FadeIn(caption), run_time=0.5)
        self.wait(9.04)


# ─────────────────────────────────────────────────────────────────────────────
#  B03_VerifyAgainstReality   (target ~52s)
#  The citation card leaves the model entirely, fetches a real source, and
#  resolves to one of three honest states — including the one that admits
#  it can't tell.
# ─────────────────────────────────────────────────────────────────────────────
class B03_VerifyAgainstReality(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mech_legend(active=1, lit=(0,))
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(0.86)

        cite = mono("CITATION: source: 10-K", size=22, color=INK)
        cite_box = auto_box(cite, h_pad=0.32, v_pad=0.24, color=INK,
                             fill_color=BG, fill_opacity=1.0)
        cite_grp = VGroup(cite_box, cite).move_to([-4.1, 1.7, 0])
        self.play(FadeIn(cite_grp), run_time=0.5)
        self.wait(1.7)

        filing = label("independently\nfetched source", size=21, color=SOFT,
                        line_spacing=0.8)
        filing_box = auto_box(filing, h_pad=0.32, v_pad=0.28, color=SOFT)
        filing_grp = VGroup(filing_box, filing).move_to([4.0, 1.7, 0])
        arrow = Arrow(cite_box.get_right(), filing_box.get_left(), buff=0.15,
                      color=ACC, stroke_width=3)
        self.play(Create(arrow), FadeIn(filing_grp), run_time=0.7)
        self.wait(2.39)

        paths = VGroup(
            label("government filing → structured data", size=18, color=SOFT),
            label("generic page → raw text search", size=18, color=SOFT),
        ).arrange(DOWN, buff=0.16)
        paths.next_to(filing_grp, DOWN, buff=0.3)
        self.play(FadeIn(paths), run_time=0.5)
        self.wait(3.41)

        code = mono("_close_enough(a, b, tol=0.01)  # within ~1%", size=18, color=SOFT)
        code.move_to(DOWN * 0.3)
        self.play(FadeIn(code), run_time=0.5)
        self.wait(4.09)

        # ── Three honest outcomes ──────────────────────────────────────────────
        # `code` was left on screen here (DOWN*0.3) and collided with
        # `redflag`/`nojudge` once those landed near the same height below
        # the chip row (caught in mid-scene QC) — fade it out with the rest.
        self.play(FadeOut(VGroup(cite_grp, arrow, filing_grp, paths, code)), run_time=0.5)
        outs = [
            ("reachable,\nnumber matches", "✓", INK),
            ("reachable,\nnothing matches", "✕", ACC),
            ("fetch failed —\nunattainable", "–", SOFT),
        ]
        chips = VGroup()
        for txt, sym, col in outs:
            c = checked(txt, size=18, color=col, symbol=sym)
            box = auto_box(c, h_pad=0.3, v_pad=0.24, color=col)
            chips.add(VGroup(box, c))
        chips.arrange(RIGHT, buff=0.4).move_to(UP * 1.0)
        if chips.width > 12.4:
            chips.scale(12.4 / chips.width)

        for c in chips:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.5)
            self.wait(1.7)
        self.wait(1.37)

        redflag = label("a real red flag", size=22, color=ACC)
        redflag.next_to(chips[1], DOWN, buff=0.35)
        self.play(FadeIn(redflag), run_time=0.4)
        self.wait(2.72)

        nojudge = label("no judgment possible either way", size=22, color=SOFT)
        nojudge.next_to(chips[2], DOWN, buff=0.35)
        self.play(FadeIn(nojudge), run_time=0.4)
        self.wait(3.07)

        land = serif("An honest system can say: I don't know.",
                      size=30, color=ACC).move_to(DOWN * 2.9)
        self.play(FadeOut(redflag), FadeOut(nojudge), FadeIn(land), run_time=0.6)
        self.wait(6.14)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_VerificationRollup   (target ~44s)
#  The worked example resolves and rolls up into one rate a reviewer can act
#  on — then an honest caveat about the real pooling behavior in verification.py.
# ─────────────────────────────────────────────────────────────────────────────
class B04_VerificationRollup(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mech_legend(active=1, lit=(0,))
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(0.96)

        worked = checked("34% — CONFIRMED", size=24, color=INK, symbol="✓")
        worked_box = auto_box(worked, h_pad=0.35, v_pad=0.26, color=INK)
        VGroup(worked_box, worked).move_to(UP * 1.7)
        self.play(FadeIn(worked_box), FadeIn(worked), run_time=0.6)
        self.wait(3.08)

        rate = label("verification rate", size=22, color=SOFT)
        counter = mono("6 of 9 confirmed — 67%", size=30, color=ACC)
        rollup = VGroup(rate, counter).arrange(DOWN, buff=0.25).move_to(UP * 0.1)
        self.play(FadeIn(rollup), run_time=0.6)
        self.wait(4.24)

        caption = label("a number a human reviewer can actually act on",
                         size=23, color=INK)
        caption.next_to(rollup, DOWN, buff=0.5)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(4.24)

        # ── The honest caveat: pooled numbers, not per-citation scoping ───────
        self.play(FadeOut(VGroup(worked_box, worked, rollup, caption)), run_time=0.5)

        pool_head = label("every quantitative claim in the trace", size=21, color=SOFT)
        pool_head.move_to(UP * 1.6)
        pool_nums = VGroup(*[
            mono(n, size=20, color=SOFT) for n in ("34%", "$4.2M", "12x", "9%")
        ]).arrange(RIGHT, buff=0.5)
        pool_nums.next_to(pool_head, DOWN, buff=0.35)
        self.play(FadeIn(pool_head), FadeIn(pool_nums), run_time=0.6)
        self.wait(3.08)

        this_cite = mono("this citation's source", size=20, color=INK)
        this_box = auto_box(this_cite, h_pad=0.3, v_pad=0.22, color=INK)
        VGroup(this_box, this_cite).move_to(DOWN * 0.6)
        self.play(FadeIn(this_box), FadeIn(this_cite), run_time=0.5)
        self.wait(1.93)

        unrelated = pool_nums[3]  # "9%" — not the one actually near this citation
        ring = surround_box(unrelated, buff=0.1, color=ACC, stroke_width=2.5)
        arrow = Arrow(unrelated.get_bottom(), this_box.get_top(), buff=0.1,
                      color=ACC, stroke_width=2.5)
        self.play(Create(ring), Create(arrow), run_time=0.6)
        self.wait(3.08)

        caveat = label("confirmed by an unrelated number", size=23, color=ACC)
        caveat.move_to(DOWN * 2.2)
        self.play(FadeIn(caveat), run_time=0.5)
        self.wait(3.86)

        land = serif("A real gap — not a rounding error.",
                      size=28, color=ACC).move_to(DOWN * 3.1)
        self.play(FadeIn(land), run_time=0.5)
        self.wait(6.56)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_AskTwice   (target ~48s)
#  One input duplicates into two independent runs; the comparison
#  mechanism itself is set up before either result resolves.
# ─────────────────────────────────────────────────────────────────────────────
class B05_AskTwice(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mech_legend(active=2, lit=(0, 1))
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(1.45)

        inp = label("same query", size=24, color=INK)
        inp_box = auto_box(inp, h_pad=0.35, v_pad=0.25, color=INK,
                            fill_color=INK, fill_opacity=0.05)
        inp_grp = VGroup(inp_box, inp).move_to(UP * 1.9)
        self.play(FadeIn(inp_grp), run_time=0.5)
        self.wait(2.32)

        agent_l = label("run A", size=22, color=SOFT)
        agent_r = label("run B", size=22, color=SOFT)
        box_l = auto_box(agent_l, h_pad=0.3, v_pad=0.22, color=SOFT)
        box_r = auto_box(agent_r, h_pad=0.3, v_pad=0.22, color=SOFT)
        agent_l_grp = VGroup(box_l, agent_l).move_to([-3.4, 0.8, 0])
        agent_r_grp = VGroup(box_r, agent_r).move_to([3.4, 0.8, 0])
        arr_l = Arrow(inp_box.get_bottom(), agent_l_grp.get_top(), buff=0.1,
                      color=GHOST, stroke_width=2.5)
        arr_r = Arrow(inp_box.get_bottom(), agent_r_grp.get_top(), buff=0.1,
                      color=GHOST, stroke_width=2.5)
        self.play(Create(arr_l), Create(arr_r), FadeIn(agent_l_grp),
                   FadeIn(agent_r_grp), run_time=0.7)
        self.wait(4.06)

        concl_l = mono("conclusion", size=18, color=GHOST)
        concl_r = mono("conclusion", size=18, color=GHOST)
        concl_l.next_to(agent_l_grp, DOWN, buff=0.5)
        concl_r.next_to(agent_r_grp, DOWN, buff=0.5)
        self.play(FadeIn(concl_l), FadeIn(concl_r), run_time=0.5)
        self.wait(3.48)

        weight = label("word overlap × 0.4   ·   number overlap × 0.6",
                        size=21, color=SOFT)
        weight.move_to(DOWN * 1.7)
        self.play(FadeIn(weight), run_time=0.5)
        self.wait(6.96)

        cap1 = label("real evidence lands in roughly the same place twice",
                      size=22, color=INK)
        cap1.move_to(DOWN * 2.6)
        self.play(FadeIn(cap1), run_time=0.5)
        self.wait(6.96)

        land = serif("A fabricated number is harder to repeat than a fabricated vibe.",
                      size=26, color=ACC).move_to(DOWN * 3.25)
        self.play(FadeOut(cap1), FadeIn(land), run_time=0.6)
        self.wait(11.6)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_ConsistencyFlag   (target ~35s)
#  The real HIGH/MEDIUM/LOW thresholds applied to the worked example twice —
#  once agreeing, once diverging with a hard flag on the mismatched number.
# ─────────────────────────────────────────────────────────────────────────────
class B06_ConsistencyFlag(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mech_legend(active=2, lit=(0, 1))
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(0.91)

        scale = mono("LOW < 0.40  ·  MEDIUM 0.40-0.70  ·  HIGH ≥ 0.70",
                      size=19, color=SOFT)
        scale.move_to(UP * 1.9)
        self.play(FadeIn(scale), run_time=0.6)
        self.wait(2.91)

        # ── Example A: agreement ───────────────────────────────────────────────
        runs_a = mono("Run 1: 34%   ·   Run 2: 34%", size=22, color=INK)
        runs_a.move_to(UP * 0.6)
        high = label("HIGH agreement — 0.82", size=26, color=INK, weight="BOLD")
        high_box = auto_box(high, h_pad=0.35, v_pad=0.25, color=INK)
        VGroup(high_box, high).next_to(runs_a, DOWN, buff=0.35)
        self.play(FadeIn(runs_a), run_time=0.5)
        self.wait(1.82)
        self.play(FadeIn(high_box), FadeIn(high), run_time=0.5)
        self.wait(3.64)

        # ── Example B: divergence ──────────────────────────────────────────────
        self.play(FadeOut(runs_a), FadeOut(high_box), FadeOut(high), run_time=0.4)
        run1 = mono("Run 1: 34%", size=22, color=INK)
        run2 = mono("Run 2: 41%", size=22, color=ACC)
        runs_b = VGroup(run1, run2).arrange(RIGHT, buff=0.7).move_to(UP * 0.6)
        ring = surround_box(run2, buff=0.1, color=ACC, stroke_width=2.5)
        low = label("LOW agreement — 0.21", size=26, color=ACC, weight="BOLD")
        low_box = auto_box(low, h_pad=0.35, v_pad=0.25, color=ACC)
        VGroup(low_box, low).next_to(runs_b, DOWN, buff=0.35)
        self.play(FadeIn(runs_b), run_time=0.5)
        self.wait(1.46)
        self.play(Create(ring), run_time=0.5)
        self.wait(1.46)
        self.play(FadeIn(low_box), FadeIn(low), run_time=0.5)
        self.wait(2.91)

        flag = label("number in one run, not the other", size=22, color=ACC)
        flag.next_to(VGroup(low_box, low), DOWN, buff=0.35)
        self.play(FadeIn(flag), run_time=0.5)
        self.wait(3.64)

        land = serif("A fabrication can't easily fake genuine drift.",
                      size=28, color=ACC).move_to(DOWN * 3.1)
        self.play(FadeIn(land), run_time=0.5)
        self.wait(5.82)


# ─────────────────────────────────────────────────────────────────────────────
#  B07_ProofToEvidence   (target ~37s)
#  Falsifiability (i): PROOF struck through and replaced with EVIDENCE.
# ─────────────────────────────────────────────────────────────────────────────
class B07_ProofToEvidence(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mech_legend(active=None, lit=(0, 1, 2))
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(1.8)

        proof = label("PROOF", size=64, color=INK, weight="BOLD").move_to(UP * 1.0)
        self.play(Write(proof), run_time=0.8)
        self.wait(3.15)

        line = strike(proof, color=ACC)
        self.play(Create(line), run_time=0.6)
        self.wait(1.12)

        evidence = label("EVIDENCE", size=44, color=ACC, weight="BOLD")
        evidence.next_to(proof, DOWN, buff=0.55)
        self.play(FadeIn(evidence, shift=UP * 0.2), run_time=0.6)
        self.wait(3.59)

        l1 = label("high consistency = weak positive evidence", size=21, color=SOFT)
        l2 = label("two runs can agree while both are confidently wrong", size=21, color=SOFT)
        l3 = label("\"unattainable\" tells you nothing either way", size=21, color=SOFT)
        stack = VGroup(l1, l2, l3).arrange(DOWN, buff=0.28)
        stack.next_to(evidence, DOWN, buff=0.55)
        self.play(FadeIn(l1), run_time=0.4)
        self.wait(3.15)
        self.play(FadeIn(l2), run_time=0.4)
        self.wait(3.15)
        self.play(FadeIn(l3), run_time=0.4)
        self.wait(4.04)

        self.play(FadeOut(proof), FadeOut(line), FadeOut(stack), run_time=0.6)
        self.wait(8.99)


# ─────────────────────────────────────────────────────────────────────────────
#  B08_GoodAtCatching   (target ~33s)
#  Falsifiability (ii): the one direction these mechanisms are strong in,
#  set against the one claim they can never make.
# ─────────────────────────────────────────────────────────────────────────────
class B08_GoodAtCatching(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mech_legend(active=None, lit=(0, 1, 2))
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(1.65)

        head_l = label("Good at catching", size=25, color=INK, weight="BOLD")
        rows_l = VGroup(*[
            label(t, size=22, color=SOFT) for t in
            ("fabrication", "drift", "absent evidence")
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        col_l = VGroup(head_l, rows_l).arrange(DOWN, buff=0.32, aligned_edge=LEFT)

        head_r = label("Cannot prove", size=25, color=ACC, weight="BOLD")
        rows_r = VGroup(*[
            label(t, size=22, color=SOFT) for t in
            ("correct causal reasoning", "sound judgment")
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        col_r = VGroup(head_r, rows_r).arrange(DOWN, buff=0.32, aligned_edge=LEFT)

        cols = VGroup(col_l, col_r).arrange(RIGHT, buff=1.7).move_to(UP * 0.2)
        divider = Line(UP * 1.6, DOWN * 1.6, color=GHOST, stroke_width=2)
        divider.move_to(cols.get_center())

        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(col_l), run_time=0.6)
        self.wait(3.84)
        self.play(FadeIn(col_r), run_time=0.6)
        self.wait(6.58)

        caption = label("checked ≠ correct", size=24, color=SOFT)
        caption.next_to(cols, DOWN, buff=0.55)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(4.39)

        land = serif("Catching wrong is not the same as certifying right.",
                      size=28, color=ACC).move_to(DOWN * 3.1)
        self.play(FadeOut(caption), FadeIn(land), run_time=0.6)
        self.wait(9.33)


# ─────────────────────────────────────────────────────────────────────────────
#  B09_TheFramework   (target ~35s)
#  The three mechanisms collapse into three named, transferable rules.
# ─────────────────────────────────────────────────────────────────────────────
class B09_TheFramework(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Framework", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(2.5)

        rules_spec = [
            ("1", "grade the claims, not the story"),
            ("2", "check what's checkable; log what isn't"),
            ("3", "make it disagree with itself on purpose"),
        ]
        rows = VGroup()
        for num, text in rules_spec:
            n = label(num, size=30, color=ACC, weight="BOLD")
            n_box = Circle(radius=0.32, color=ACC, stroke_width=2.5).move_to(n)
            t2 = label(text, size=27, color=INK)
            row = VGroup(VGroup(n_box, n), t2).arrange(RIGHT, buff=0.4)
            rows.add(row)
        rows.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        rows.move_to(DOWN * 0.1)

        for r in rows:
            self.play(FadeIn(r[0]), run_time=0.35)
            self.play(FadeIn(r[1], shift=RIGHT * 0.2), run_time=0.45)
            self.wait(4.0)
        self.wait(3.0)

        footnote = serif("None of these prove truth. All three narrow what's plausible.",
                          size=27, color=ACC).move_to(DOWN * 3.25)
        self.play(FadeIn(footnote), run_time=0.6)
        self.wait(8.4)
