"""scenes.py — Manim scenes for why-agents-fail (claude-divij).

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757, soft #73705F,
ghost #A9A491 — the Claude fidelity palette per ai-explainer SKILL.md. ONE
accent per beat. The source script's green success box is deliberately NOT
carried: good/bad here is carried by label and column position, so the frame
stays legible in grayscale and under any colour vision. No blue, no green.

Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF,
editorial voice only) / PT Mono (MONO, logs + code + data only) — see
graphics_lib.py. Boxes are content-fitted via auto_box, never hand-measured.

Pace: normal-speed creates/fades with deliberate HOLDS sized to the
narration. Targets below are against `estimated_duration_s` in
beat_sheet.json; re-check against `actual_duration_s` once Kokoro has run.

The four-mode legend persists across B02-B06 as the reel's spine — the active
mode is the only terracotta element in the frame, and B06 lights each mode's
tick as that mode fires inside the worked trace.
"""
import numpy as np
from graphics_lib import *

# ── Palette (claude-stage retint, per ai-explainer SKILL.md) ──────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")

MODES = ["Infinite Loops", "Context Drift",
         "Hallucinated Arguments", "Confidently Wrong"]

# The legend runs the four names on ONE line, so it uses shortened forms —
# the full names are established on B01's panels. At size 24 (the legibility
# floor) the full names measure ~14.1u wide, which overruns the title-safe
# inset; these fit with room to spare.
MODES_SHORT = ["Infinite Loops", "Context Drift",
               "Bad Arguments", "Confidently Wrong"]

LEGEND_MAX_W = 12.4   # title-safe span (SAFE x is ±6.3 of a 14.22u frame)


def mode_legend(active=None, lit=(), y=3.25):
    """The four-mode spine, parked at the top of frame.

    `active` (0-3) renders terracotta; anything in `lit` renders ink (already
    covered); everything else stays ghost. Returns a VGroup of labels.
    """
    chips = VGroup()
    for i, name in enumerate(MODES_SHORT):
        if i == active:
            col, wt = ACC, "BOLD"
        elif i in lit:
            col, wt = INK, None
        else:
            col, wt = GHOST, None
        chips.add(label(name, size=24, color=col, weight=wt))
    chips.arrange(RIGHT, buff=0.5)
    # Guard rather than trust the estimate — bold weight on the active chip
    # widens the row, so measure and clamp.
    if chips.width > LEGEND_MAX_W:
        chips.scale(LEGEND_MAX_W / chips.width)
    chips.move_to([0, y, 0])
    return chips


def strike(mobj, color=None):
    """A struck-through line sized to the mobject it cancels."""
    return Line(mobj.get_left() + LEFT * 0.08, mobj.get_right() + RIGHT * 0.08,
                color=color if color is not None else ACC, stroke_width=3.0)


def counter(value, prefix="attempt ", y=-3.3, x=5.0, color=None):
    return label(f"{prefix}{value}", size=28,
                 color=color if color is not None else SOFT).move_to([x, y, 0])


# ─────────────────────────────────────────────────────────────────────────────
#  B01_FourFailures   (target ~12s)
#  The framework beat: all four modes named as empty panels before any is filled.
# ─────────────────────────────────────────────────────────────────────────────
class B01_FourFailures(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Four Ways Agents Fail", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(0.8)

        # Uniform panels sized from the widest/tallest label rather than a
        # guessed literal, then the row clamped to the title-safe span — four
        # 3.0u panels plus gaps overran ±6.4.
        txts = [label(n.replace(" ", "\n"), size=27, color=SOFT, line_spacing=0.8)
                for n in MODES]
        pw = max(t.width for t in txts) + 0.65
        ph = max(t.height for t in txts) + 0.70
        panels = VGroup(*[
            VGroup(Rectangle(width=pw, height=ph, stroke_width=2.5, color=GHOST,
                             fill_color=GHOST, fill_opacity=0.08).move_to(t), t)
            for t in txts
        ]).arrange(RIGHT, buff=0.32)
        if panels.width > 12.6:
            panels.scale(12.6 / panels.width)
        panels.move_to(DOWN * 0.3)

        for p in panels:
            self.play(FadeIn(p, shift=UP * 0.25), run_time=0.45)
            self.wait(0.55)
        self.wait(1.4)

        # A single terracotta tick marks which panel gets filled first.
        tick = Triangle(color=ACC, fill_color=ACC, fill_opacity=1.0,
                        stroke_width=0).scale(0.16).rotate(PI)
        tick.next_to(panels[0], UP, buff=0.22)
        self.play(FadeIn(tick, shift=DOWN * 0.15), run_time=0.4)
        self.wait(4.8)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_InfiniteLoop   (target ~40s)
#  The ring runs correctly, then keeps running. Same failure, climbing counter.
# ─────────────────────────────────────────────────────────────────────────────
class B02_InfiniteLoop(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mode_legend(active=0)
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(0.6)

        stages = ["Observe", "Decide", "Act", "Check Result"]
        R = 2.0
        centre = np.array([-2.6, -0.4, 0])
        angles = [PI / 2, 0, -PI / 2, PI]
        nodes = VGroup()
        for name, a in zip(stages, angles):
            pos = centre + np.array([R * np.cos(a), R * np.sin(a), 0])
            txt = label(name, size=26, color=INK)
            bx = auto_box(txt, h_pad=0.3, v_pad=0.22, color=INK,
                          fill_color=BG, fill_opacity=1.0)
            nodes.add(VGroup(bx, txt).move_to(pos))

        ring = Circle(radius=R, color=GHOST, stroke_width=2.5).move_to(centre)
        self.play(Create(ring), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.22),
                  run_time=1.2)
        self.wait(1.4)

        # Caption sits BELOW the ring, not inside it — at size 27 this string
        # renders close to the ring's own 4.0 diameter, so centering it on
        # `centre` pokes past the circle's stroke on both sides. Placed here
        # it clears the Act node's box (bottom of ring, ~y=-2.8) with margin
        # and stays inside the frame-safe y range.
        engine = label("the whole engine", size=27, color=SOFT)
        engine.move_to(centre + np.array([0, -R - 0.9, 0]))
        self.play(FadeIn(engine), run_time=0.4)
        self.wait(2.0)

        # ── One calm, correct lap ─────────────────────────────────────────────
        pulse = Dot(radius=0.15, color=ACC).move_to(centre + np.array([0, R, 0]))
        self.play(FadeIn(pulse), run_time=0.3)
        for i in range(4):
            self.play(Rotate(pulse, angle=-PI / 2, about_point=centre),
                      nodes[i].animate.set_color(ACC), run_time=0.7)
            self.play(nodes[i].animate.set_color(INK), run_time=0.2)
        self.wait(2.4)

        # ── The test that keeps failing the same way ──────────────────────────
        self.play(FadeOut(engine), run_time=0.3)
        test = mono("test: FAIL", size=30, color=ACC).move_to([3.6, 1.5, 0])
        test_box = auto_box(test, h_pad=0.4, v_pad=0.3, color=ACC,
                            fill_color=ACC, fill_opacity=0.07)
        self.play(Create(test_box), FadeIn(test), run_time=0.6)
        self.wait(2.8)

        cnt = counter(1, x=3.6, y=0.2)
        self.play(FadeIn(cnt), run_time=0.4)
        self.wait(1.6)

        # ── It accelerates. Nothing inside the loop notices. ──────────────────
        # Transform between digit-mismatched Text morphs into an illegible
        # smear mid-transition (found in 4K visual QC) — fade-swap instead.
        for n, rt in ((2, 0.9), (3, 0.7), (5, 0.55), (8, 0.42), (13, 0.34)):
            self.play(Rotate(pulse, angle=-2 * PI, about_point=centre), run_time=rt)
            new_cnt = counter(n, x=3.6, y=0.2, color=ACC)
            self.play(FadeOut(cnt, run_time=0.1), run_time=0.1)
            cnt = new_cnt
            self.play(FadeIn(cnt, run_time=0.1), run_time=0.1)
        self.wait(1.8)

        # ── The check the agent does not have ─────────────────────────────────
        thought = label('"I\'ve tried this three times…"', size=27, color=GHOST)
        thought.move_to([3.6, -1.3, 0])
        self.play(FadeIn(thought), run_time=0.5)
        self.wait(1.6)
        self.play(Create(strike(thought, color=GHOST)), run_time=0.5)
        self.wait(2.6)

        # ── Only an external stop works ───────────────────────────────────────
        land = serif("Only something outside the loop stops it.",
                     size=32, color=ACC).move_to(DOWN * 3.15)
        self.play(FadeIn(land), run_time=0.5)
        self.play(Rotate(pulse, angle=-4 * PI, about_point=centre), run_time=1.0)
        self.wait(4.0)  # retimed to real audio (35.80s) — was 8.2


# ─────────────────────────────────────────────────────────────────────────────
#  B03_ContextDrift   (target ~39s)
#  The goal block is physically shoved to the edge and faded as newer blocks
#  pack in behind it.
# ─────────────────────────────────────────────────────────────────────────────
class B03_ContextDrift(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mode_legend(active=1)
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(0.6)

        W, H = 12.0, 2.1
        window = Rectangle(width=W, height=H, stroke_width=2.5, color=INK,
                           fill_color=INK, fill_opacity=0.03).move_to(UP * 0.75)
        wlab = label("context window — everything it can attend to at once",
                     size=26, color=SOFT).next_to(window, UP, buff=0.3)
        self.play(Create(window), FadeIn(wlab), run_time=0.8)
        self.wait(3.2)

        left_edge = window.get_left()[0]

        # ── The goal seats first, at the left edge ────────────────────────────
        goal_txt = label("Original\nGoal", size=25, color=ACC, line_spacing=0.75)
        goal_bx = Rectangle(width=goal_txt.width + 0.34, height=H - 0.35,
                            stroke_width=2.5, color=ACC,
                            fill_color=ACC, fill_opacity=0.16).move_to(goal_txt)
        goal = VGroup(goal_bx, goal_txt)
        goal.move_to([left_edge + goal.width / 2 + 0.14, 0.75, 0])
        self.play(FadeIn(goal), run_time=0.6)
        self.wait(2.4)

        # ── Newer content packs in behind it ──────────────────────────────────
        # Block width is derived from the widest label, and the packed row is
        # clamped to the window's interior — both were hand-measured literals
        # before, which is the recurring overflow bug.
        fills = ["tool\nresult", "tool\nresult", "error", "retry",
                 "error", "side\nchat", "retry", "error"]
        btxts = [label(f, size=24, color=SOFT, line_spacing=0.75) for f in fills]
        bw = max(t.width for t in btxts) + 0.24
        blocks = VGroup(*[
            VGroup(Rectangle(width=bw, height=H - 0.35, stroke_width=2,
                             color=SOFT, fill_color=SOFT,
                             fill_opacity=0.09).move_to(t), t)
            for t in btxts
        ]).arrange(RIGHT, buff=0.05)
        blocks.next_to(goal, RIGHT, buff=0.10)
        room = (window.get_right()[0] - 0.14) - blocks.get_left()[0]
        if blocks.width > room:
            blocks.scale(room / blocks.width, about_point=blocks.get_left())

        for b in blocks[:4]:
            self.play(FadeIn(b, shift=LEFT * 0.3), run_time=0.35)
            self.wait(0.75)
        self.wait(1.2)

        for b in blocks[4:]:
            self.play(FadeIn(b, shift=LEFT * 0.3), run_time=0.3)
            self.wait(0.45)
        self.wait(1.4)

        # ── The goal is shoved out and dimmed ─────────────────────────────────
        ago = label("three hundred messages ago", size=26, color=GHOST)
        ago.next_to(window, DOWN, buff=0.45).align_to(window, LEFT)
        # 0.40, not more — a larger shove pushes the goal block past the
        # title-safe inset and it reads as clipped rather than crowded out.
        self.play(
            goal.animate.shift(LEFT * 0.40).set_opacity(0.28),
            blocks.animate.shift(LEFT * 0.40),
            FadeIn(ago), run_time=1.2,
        )
        self.wait(3.0)

        # ── What it optimizes for now, versus what you asked ──────────────────
        now = VGroup(
            label("optimizing for:", size=26, color=SOFT),
            label("“make this error go away”", size=30, color=INK),
        ).arrange(RIGHT, buff=0.35)
        want = VGroup(
            label("instead of:", size=26, color=SOFT),
            label("what you actually asked for", size=30, color=GHOST),
        ).arrange(RIGHT, buff=0.35)
        pair = VGroup(now, want).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        pair.move_to([0, -2.2, 0])

        self.play(FadeIn(now), run_time=0.5)
        self.wait(2.6)
        self.play(FadeIn(want), run_time=0.5)
        self.wait(3.0)

        land = label("not forgotten — deprioritized", size=28, color=ACC)
        land.move_to(DOWN * 3.4)
        self.play(FadeIn(land), run_time=0.5)
        self.wait(9.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_HallucinatedArgs   (target ~37s)
#  The invented argument is indistinguishable from the real ones until marked.
# ─────────────────────────────────────────────────────────────────────────────
class B04_HallucinatedArgs(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mode_legend(active=2, lit=(0, 1))
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(0.6)

        # ── What the tool actually accepts ────────────────────────────────────
        schema_rows = VGroup(*[
            mono(r, size=25, color=INK) for r in (
                "path      : string",
                "mode      : \"r\" | \"w\"",
                "encoding  : string",
            )
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        schema_box = auto_box(schema_rows, h_pad=0.45, v_pad=0.35, color=INK)
        schema_head = label("what the tool accepts", size=26, color=SOFT)
        schema = VGroup(schema_box, schema_rows).move_to([-3.7, 0.35, 0])
        schema_head.next_to(schema, UP, buff=0.3)

        self.play(Create(schema_box), FadeIn(schema_head), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(r) for r in schema_rows], lag_ratio=0.25),
                  run_time=0.9)
        self.wait(4.0)

        # ── What the model produced — every line looks right ──────────────────
        call_rows = VGroup(*[
            mono(r, size=25, color=INK) for r in (
                "path           : \"config.yml\"",
                "mode           : \"w\"",
                "encoding       : \"utf-8\"",
                "priority_level : \"high\"",
            )
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        call_box = auto_box(call_rows, h_pad=0.45, v_pad=0.35, color=SOFT)
        call_head = label("what the model produced", size=26, color=SOFT)
        call = VGroup(call_box, call_rows).move_to([3.5, 0.35, 0])
        call_head.next_to(call, UP, buff=0.3)

        self.play(Create(call_box), FadeIn(call_head), run_time=0.6)
        for r in call_rows:
            self.play(FadeIn(r), run_time=0.28)
            self.wait(0.62)
        self.wait(1.6)

        # ── All four read as clean ────────────────────────────────────────────
        ok = label("plausible · well-formatted · confident", size=26, color=SOFT)
        ok.next_to(call, DOWN, buff=0.4)
        self.play(FadeIn(ok), run_time=0.5)
        self.wait(3.0)

        # ── One has no match in the schema ────────────────────────────────────
        bad = call_rows[3]
        ring = surround_box(bad, buff=0.16, color=ACC, stroke_width=3.0)
        self.play(Create(ring), bad.animate.set_color(ACC), run_time=0.6)
        self.wait(1.4)

        probe = DashedLine(ring.get_left(), schema_box.get_right(),
                           color=ACC, stroke_width=2.5, dash_length=0.14)
        no_match = label("no match", size=26, color=ACC)
        no_match.next_to(probe, UP, buff=0.14)
        self.play(Create(probe), FadeIn(no_match), run_time=0.8)
        self.wait(3.2)

        # ── Two ways it goes wrong; the quiet one is worse ────────────────────
        self.play(FadeOut(ok), FadeOut(schema_head), FadeOut(call_head),
                  run_time=0.4)
        b1 = label("throws an error", size=28, color=SOFT)
        b2 = label("silently does something else", size=28, color=ACC)
        branches = VGroup(b1, b2).arrange(DOWN, buff=0.35).move_to(DOWN * 2.45)
        self.play(FadeIn(b1), run_time=0.4)
        self.wait(1.4)
        self.play(FadeIn(b2), run_time=0.4)
        self.wait(3.2)

        land = serif("It doesn't look like a guess. It looks like a fact.",
                     size=32, color=ACC).move_to(DOWN * 3.45)
        self.play(FadeOut(branches), FadeIn(land), run_time=0.6)
        self.wait(8.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B05_ConfidentlyWrong   (target ~32s)
#  What happened and what was reported, held side by side, gap measured.
#  The falsifiability beat: the reel's subject is undetectable by reading
#  what the agent says.
# ─────────────────────────────────────────────────────────────────────────────
class B05_ConfidentlyWrong(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mode_legend(active=3, lit=(0, 1, 2))
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(0.6)

        h_left = label("what actually happened", size=27, color=SOFT).move_to([-3.9, 2.35, 0])
        h_right = label("what it reported", size=27, color=SOFT).move_to([3.9, 2.35, 0])
        self.play(FadeIn(h_left), FadeIn(h_right), run_time=0.5)
        self.wait(2.6)

        # ── Ten failures stack on the left ────────────────────────────────────
        logs = VGroup(*[
            mono(f"attempt {i:>2}   FAIL", size=25, color=ACC)
            for i in range(1, 11)
        ]).arrange(DOWN, buff=0.13, aligned_edge=LEFT).move_to([-3.9, -0.25, 0])

        for lg in logs:
            self.play(FadeIn(lg, shift=UP * 0.08), run_time=0.13)
            self.wait(0.28)
        self.wait(2.4)

        # ── One calm card on the right ────────────────────────────────────────
        done = VGroup(
            label("Task completed", size=32, color=INK, weight="BOLD"),
            label("successfully.", size=32, color=INK, weight="BOLD"),
        ).arrange(DOWN, buff=0.14)
        done_box = auto_box(done, h_pad=0.6, v_pad=0.45, color=INK,
                            fill_color=INK, fill_opacity=0.05)
        VGroup(done_box, done).move_to([3.9, -0.25, 0])
        self.play(Create(done_box), FadeIn(done), run_time=0.8)
        self.wait(3.4)

        # ── The gap, measured ─────────────────────────────────────────────────
        gap = DoubleArrow(logs.get_right() + RIGHT * 0.2,
                          done_box.get_left() + LEFT * 0.2,
                          color=ACC, stroke_width=3, buff=0.1,
                          max_tip_length_to_length_ratio=0.09)
        gap_lab = label("the gap", size=28, color=ACC).next_to(gap, UP, buff=0.2)
        self.play(Create(gap), FadeIn(gap_lab), run_time=0.7)
        self.wait(3.2)

        # ── Why it is the dangerous one ───────────────────────────────────────
        pair = VGroup(
            label("a stuck human looks stuck", size=27, color=SOFT),
            label("a stuck agent looks identical to one that won", size=27, color=ACC),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 3.05)
        self.play(FadeIn(pair[0]), run_time=0.45)
        self.wait(1.8)
        self.play(FadeIn(pair[1]), run_time=0.45)
        self.wait(10.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_TwelveAttempts   (target ~46s)
#  The worked example — three of the four modes firing inside one real trace,
#  each lighting its tick in the legend as it fires.
# ─────────────────────────────────────────────────────────────────────────────
class B06_TwelveAttempts(Scene):

    def construct(self):
        self.camera.background_color = BG
        legend = mode_legend(active=None)
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(0.8)

        # DISPLAY, not MONO — a spoken instruction is prose, and MONO is
        # reserved for data/code/numbers (DESIGN.md typography). The numbered
        # trace lines below ARE log data and correctly stay MONO.
        task = label("deploy this small website update", size=27, color=INK)
        task_box = auto_box(task, h_pad=0.45, v_pad=0.3, color=ACC,
                            fill_color=ACC, fill_opacity=0.10)
        # 2.40, not 2.30 — Montserrat sets taller and wider than the PT Mono
        # this chip used to carry, so auto_box grew and the chip's lower edge
        # cut through step 1. Neighbours are suspect after any font change.
        task_grp = VGroup(task_box, task).move_to([0, 2.40, 0])
        self.play(Create(task_box), FadeIn(task), run_time=0.7)
        self.wait(3.4)

        # ── The trace builds, step by spoken step ─────────────────────────────
        steps = [
            "1.  run deploy",
            "2.  FAIL — missing env var",
            "3.  guess a value, write it to config",
            "4.  FAIL — guessed value wrong",
            "5.  try a different guess",
            "6.  FAIL — same error, new guess",
        ]
        lines = VGroup(*[mono(s, size=26, color=INK) for s in steps])
        lines.arrange(DOWN, buff=0.22, aligned_edge=LEFT).move_to([-1.2, 0.05, 0])

        for i, ln in enumerate(lines):
            if "FAIL" in steps[i]:
                ln.set_color(ACC)
            self.play(FadeIn(ln, shift=RIGHT * 0.15), run_time=0.3)
            self.wait(1.35)
        self.wait(0.8)

        # ── Mode 3 fires: the guessed value was invented ──────────────────────
        ring = surround_box(lines[2], buff=0.14, color=ACC, stroke_width=2.5)
        self.play(Create(ring),
                  legend[2].animate.set_color(ACC), run_time=0.6)
        self.wait(1.8)

        # ── Mode 1 fires: it just keeps going ─────────────────────────────────
        cnt = counter(6, x=4.6, y=0.35)
        self.play(FadeIn(cnt), legend[0].animate.set_color(ACC), run_time=0.5)
        # Transform between digit-mismatched Text morphs into an illegible
        # smear mid-transition (confirmed in 4K visual QC) — fade-swap instead.
        for n in (8, 10, 12):
            new_cnt = counter(n, x=4.6, y=0.35, color=ACC)
            self.play(FadeOut(cnt, run_time=0.15), run_time=0.15)
            cnt = new_cnt
            self.play(FadeIn(cnt, run_time=0.15), run_time=0.15)
            self.wait(0.5)
        self.wait(2.2)

        # ── Mode 2 fires: the window packs, the instruction is buried ─────────
        self.play(FadeOut(ring), FadeOut(lines), run_time=0.5)
        bars = VGroup(*[
            Rectangle(width=7.2, height=0.17, stroke_width=0,
                      fill_color=SOFT, fill_opacity=0.35)
            for _ in range(13)
        ]).arrange(DOWN, buff=0.07).move_to([-1.2, -0.15, 0])
        pack_lab = label("failed deploy logs", size=26, color=SOFT)
        pack_lab.next_to(bars, DOWN, buff=0.3)

        self.play(LaggedStart(*[FadeIn(b) for b in bars], lag_ratio=0.06),
                  run_time=1.3)
        self.play(FadeIn(pack_lab), legend[1].animate.set_color(ACC), run_time=0.5)
        self.wait(1.6)

        # Shrink AND move left: `buried` sits to its right and is ~6.7u wide,
        # so leaving the chip centred pushed the label off the frame edge.
        self.play(task_grp.animate.scale(0.72).set_opacity(0.22)
                  .move_to([-3.5, 2.05, 0]), run_time=1.0)
        buried = label("buried under eleven rounds of errors", size=26, color=GHOST)
        buried.next_to(task_grp, RIGHT, buff=0.5)
        self.play(FadeIn(buried), run_time=0.5)
        self.wait(3.0)

        # ── The question it never asked ───────────────────────────────────────
        self.play(FadeOut(bars), FadeOut(pack_lab), FadeOut(cnt), run_time=0.5)
        never = serif('"I don\'t know this value. Can you tell me?"',
                      size=34, color=GHOST, italic=True).move_to(DOWN * 1.0)
        self.play(FadeIn(never), run_time=0.6)
        self.wait(1.8)
        self.play(Create(strike(never, color=ACC)), run_time=0.6)
        never_lab = label("never asked, not once, unprompted", size=27, color=ACC)
        never_lab.next_to(never, DOWN, buff=0.55)
        self.play(FadeIn(never_lab), run_time=0.5)
        self.wait(3.7)  # retimed to real audio (40.49s) — was 9.2
