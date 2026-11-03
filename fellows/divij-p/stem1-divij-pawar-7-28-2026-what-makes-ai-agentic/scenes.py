"""scenes.py — Manim scenes for what-makes-ai-agentic (claude-divij).

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757, soft #73705F,
ghost #A9A491 — the Claude fidelity palette per ai-explainer SKILL.md. ONE
accent per beat; good/bad is carried by label and position, never by a second
hue. No blue, no green.

Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF,
editorial voice only) / PT Mono (MONO, data + code only) — see graphics_lib.py.
Boxes are sized to their actual content via auto_box/surround_box, never
hand-measured.

Pace: normal-speed creates/fades (0.3-0.8s) with deliberate HOLDS sized to the
narration. Each scene's runtime is tuned to land close to its beat's audio
duration so compile.py's crop step does not need to time-stretch it. Targets
below are against `estimated_duration_s` in beat_sheet.json; re-check them
against `actual_duration_s` once Kokoro has run.

Negative space ~15-35%. The four-tier strip persists across B02-B06 as the
reel's spine — the active tier is the only terracotta element in the frame.
"""
import numpy as np
from graphics_lib import *

# ── Palette (claude-stage retint, per ai-explainer SKILL.md) ──────────────────
BG    = ManimColor("#F2F0E9")   # claude cream
INK   = ManimColor("#3D3929")   # warm ink — primary text / marks
ACC   = ManimColor("#D97757")   # terracotta — the ONE accent
SOFT  = ManimColor("#73705F")   # secondary text
GHOST = ManimColor("#A9A491")   # dimmed, inactive, placeholder

TIERS = ["Tier 0", "Tier 1", "Tier 2", "Tier 3"]


def spectrum_strip(active=None, width=11.0, y=3.25):
    """The four-tier spine, thin, parked at the top of frame.

    Persists across B02-B06 so the viewer always knows which tier is being
    described. `active` (0-3) is the only terracotta element in the frame.
    Returns VGroup(segments, labels).
    """
    seg_w = width / 4
    segs = VGroup()
    for i in range(4):
        on = (i == active)
        segs.add(Rectangle(
            width=seg_w, height=0.32, stroke_width=2,
            color=ACC if on else GHOST,
            fill_color=ACC if on else GHOST,
            fill_opacity=0.85 if on else 0.10,
        ))
    segs.arrange(RIGHT, buff=0.14).move_to([0, y, 0])

    labs = VGroup()
    for i, seg in enumerate(segs):
        on = (i == active)
        labs.add(label(TIERS[i], size=24, color=ACC if on else SOFT,
                       weight="BOLD" if on else None).next_to(seg, DOWN, buff=0.15))
    return VGroup(segs, labs)


def strike(mobj, color=None):
    """A struck-through line sized to the mobject it cancels."""
    return Line(mobj.get_left() + LEFT * 0.08, mobj.get_right() + RIGHT * 0.08,
                color=color if color is not None else ACC, stroke_width=3.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_TierSpectrum   (target ~15s)
#  The framework beat. One task fixed, four tiers laid out, nothing lit yet.
# ─────────────────────────────────────────────────────────────────────────────
class B01_TierSpectrum(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("One Task, Four Tiers", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(0.4)

        task = serif('"book me a flight to Chicago next Friday"',
                     size=38, color=INK, italic=True).move_to(UP * 1.5)
        task_box = auto_box(task, h_pad=0.55, v_pad=0.4, color=SOFT,
                            fill_color=SOFT, fill_opacity=0.05)
        self.play(Create(task_box), FadeIn(task), run_time=0.7)
        self.wait(1.4)

        # ── The bar itself: four ghosted segments, drawn left to right ────────
        seg_w = 12.0 / 4
        segs = VGroup(*[
            Rectangle(width=seg_w, height=0.9, stroke_width=2.5,
                      color=GHOST, fill_color=GHOST, fill_opacity=0.10)
            for _ in range(4)
        ]).arrange(RIGHT, buff=0.18).move_to(DOWN * 0.9)

        self.play(LaggedStart(*[Create(s) for s in segs], lag_ratio=0.25),
                  run_time=1.4)
        self.wait(0.6)

        labs = VGroup(*[
            label(TIERS[i], size=30, color=SOFT).next_to(segs[i], DOWN, buff=0.3)
            for i in range(4)
        ])
        self.play(LaggedStart(*[FadeIn(l) for l in labs], lag_ratio=0.25),
                  run_time=1.2)
        self.wait(2.2)

        # ── A marker parks at the floor, waiting for B02 ──────────────────────
        marker = Triangle(color=ACC, fill_color=ACC, fill_opacity=1.0,
                          stroke_width=0).scale(0.18).rotate(PI)
        marker.next_to(segs[0], UP, buff=0.22)
        self.play(FadeIn(marker, shift=DOWN * 0.2), run_time=0.5)
        self.wait(1.2)

        spec = label("a spectrum, not a yes-or-no label", size=28, color=SOFT)
        spec.next_to(labs, DOWN, buff=0.7)
        self.play(FadeIn(spec), run_time=0.5)
        self.wait(4.2)


# ─────────────────────────────────────────────────────────────────────────────
#  B02_TierZero   (target ~35s)
#  A chat exchange with the tool row locked out, then the prediction
#  mechanism enacted token by token.
# ─────────────────────────────────────────────────────────────────────────────
class B02_TierZero(Scene):

    def construct(self):
        self.camera.background_color = BG
        strip = spectrum_strip(active=0)
        self.play(FadeIn(strip), run_time=0.5)
        self.wait(0.8)

        # ── The ask, left ─────────────────────────────────────────────────────
        # DISPLAY, not MONO — this is a typed sentence, and MONO is reserved
        # for data/code/numbers, never running prose (DESIGN.md typography).
        ask = label("book me a flight to Chicago next Friday", size=26, color=INK)
        ask_box = auto_box(ask, h_pad=0.4, v_pad=0.3, color=SOFT,
                           fill_color=SOFT, fill_opacity=0.06)
        ask_grp = VGroup(ask_box, ask).move_to([-2.6, 1.55, 0])
        self.play(Create(ask_box), FadeIn(ask), run_time=0.7)
        self.wait(3.0)

        # ── The reply, right — words only ─────────────────────────────────────
        reply_lines = VGroup(
            label("Try Google Flights, compare a few", size=26, color=INK),
            label("times, book whichever fits.", size=26, color=INK),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        reply_box = auto_box(reply_lines, h_pad=0.4, v_pad=0.3, color=INK,
                             fill_color=INK, fill_opacity=0.05)
        VGroup(reply_box, reply_lines).move_to([2.4, 0.35, 0])
        self.play(Create(reply_box), FadeIn(reply_lines), run_time=0.7)
        self.wait(4.2)

        verdict = VGroup(
            label("Helpful advice.", size=28, color=SOFT),
            label("Zero action.", size=28, color=ACC, weight="BOLD"),
        ).arrange(RIGHT, buff=0.4).move_to([0, -1.3, 0])
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(1.4)

        # ── The locked tool row ───────────────────────────────────────────────
        # Uniform chips sized from the WIDEST label rather than a guessed
        # literal — a fixed width clips the moment a name or font size changes.
        tool_txts = [label(n, size=24, color=GHOST)
                     for n in ("search", "browser", "payment")]
        tw = max(t.width for t in tool_txts) + 0.55
        th = max(t.height for t in tool_txts) + 0.42
        tools = VGroup(*[
            VGroup(Rectangle(width=tw, height=th, stroke_width=2, color=GHOST,
                             fill_color=GHOST, fill_opacity=0.10).move_to(t), t)
            for t in tool_txts
        ]).arrange(RIGHT, buff=0.5).move_to([0, -2.5, 0])
        lock = label("no tools available", size=26, color=GHOST)
        lock.next_to(tools, DOWN, buff=0.32)

        self.play(LaggedStart(*[FadeIn(t) for t in tools], lag_ratio=0.2),
                  FadeIn(lock), run_time=0.9)
        self.wait(3.2)

        # ── Clear, then enact the mechanism ───────────────────────────────────
        self.play(FadeOut(ask_grp), FadeOut(reply_box), FadeOut(reply_lines),
                  FadeOut(verdict), FadeOut(tools), FadeOut(lock), run_time=0.6)
        self.wait(0.3)

        head = label("the entire mechanism", size=32, color=SOFT).move_to(UP * 1.9)
        self.play(FadeIn(head), run_time=0.5)
        self.wait(0.9)

        # Tokens snap in one at a time — the sentence assembling itself.
        toks = ["Try", "Google", "Flights,", "compare", "a", "few", "times"]
        chips = VGroup(*[mono(w, size=28, color=INK) for w in toks])
        chips.arrange(RIGHT, buff=0.28).move_to(UP * 0.5)
        for c in chips:
            self.play(FadeIn(c, shift=UP * 0.12), run_time=0.22)
            self.wait(0.34)
        self.wait(1.6)

        pred = label("predicting the next likely word, over and over",
                     size=27, color=ACC).next_to(chips, DOWN, buff=0.7)
        self.play(FadeIn(pred), run_time=0.5)
        self.wait(3.0)

        # ── Three things that are not there ───────────────────────────────────
        absent = VGroup(*[
            label(n, size=27, color=GHOST)
            for n in ("no flight search", "no browser", "no bank card")
        ]).arrange(RIGHT, buff=0.85).move_to(DOWN * 2.35)
        self.play(LaggedStart(*[FadeIn(a) for a in absent], lag_ratio=0.25),
                  run_time=0.9)
        strikes = VGroup(*[strike(a) for a in absent])
        self.play(LaggedStart(*[Create(s) for s in strikes], lag_ratio=0.25),
                  run_time=0.9)
        self.wait(3.0)  # retimed to real audio (32.41s) — was 5.6


# ─────────────────────────────────────────────────────────────────────────────
#  B03_TierOne   (target ~39s)
#  One round trip through a real tool, then control visibly handed back.
# ─────────────────────────────────────────────────────────────────────────────
class B03_TierOne(Scene):

    def construct(self):
        self.camera.background_color = BG
        strip = spectrum_strip(active=1)
        self.play(FadeIn(strip), run_time=0.5)
        self.wait(0.8)

        you   = label_chip("You", INK)
        model = label_chip("AI Model", INK)
        api   = label_chip("Flight Search API", SOFT)
        for m, x in ((you, -5.0), (model, 0.0), (api, 5.0)):
            m.move_to([x, 1.7, 0])

        self.play(LaggedStart(FadeIn(you), FadeIn(model), FadeIn(api),
                              lag_ratio=0.3), run_time=1.2)
        self.wait(2.6)

        e1 = Arrow(you.get_right(), model.get_left(), color=SOFT,
                   stroke_width=3, buff=0.22, max_tip_length_to_length_ratio=0.12)
        e2 = Arrow(model.get_right(), api.get_left(), color=SOFT,
                   stroke_width=3, buff=0.22, max_tip_length_to_length_ratio=0.12)
        call = label("tool call", size=24, color=SOFT).next_to(e2, UP, buff=0.16)

        self.play(Create(e1), run_time=0.5)
        self.wait(2.0)
        self.play(Create(e2), FadeIn(call), run_time=0.6)
        self.wait(2.2)

        # ── The pulse goes out and comes back carrying data ───────────────────
        pulse = Dot(radius=0.15, color=ACC).move_to(model.get_right() + RIGHT * 0.2)
        self.play(FadeIn(pulse), run_time=0.3)
        self.play(pulse.animate.move_to(api.get_left() + LEFT * 0.2), run_time=1.0)
        self.wait(1.4)

        back = Arrow(api.get_left(), model.get_right(), color=ACC,
                     stroke_width=3, buff=0.22,
                     max_tip_length_to_length_ratio=0.12).shift(DOWN * 0.45)
        data = label("live prices + times", size=24, color=ACC)
        data.next_to(back, DOWN, buff=0.16)
        self.play(pulse.animate.move_to(back.get_start()), run_time=0.4)
        self.play(Create(back), FadeIn(data),
                  pulse.animate.move_to(back.get_end()), run_time=1.0)
        self.play(FadeOut(pulse), run_time=0.3)
        self.wait(2.0)

        # ── Three real options land ───────────────────────────────────────────
        rows = VGroup(*[
            mono(r, size=26, color=INK) for r in (
                "07:05   ORD   $148",
                "11:20   ORD   $131",
                "17:45   ORD   $206",
            )
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        rows_box = auto_box(rows, h_pad=0.5, v_pad=0.35, color=INK,
                            fill_color=INK, fill_opacity=0.05)
        VGroup(rows_box, rows).move_to([0, -0.75, 0])
        self.play(Create(rows_box), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.25),
                  run_time=1.0)
        self.wait(4.2)

        # ── The four steps, named ─────────────────────────────────────────────
        steps = VGroup(*[
            checked(s, size=26, color=SOFT)
            for s in ("recognized", "formatted", "waited", "used")
        ]).arrange(RIGHT, buff=0.6).move_to(DOWN * 2.45)
        for s in steps:
            self.play(FadeIn(s), run_time=0.3)
            self.wait(1.4)
        self.wait(1.6)

        # ── And then it stops ─────────────────────────────────────────────────
        self.play(FadeOut(steps), run_time=0.4)
        ret = Arrow(model.get_left() + DOWN * 0.1, you.get_right() + DOWN * 0.1,
                    color=ACC, stroke_width=3.5, buff=0.22,
                    max_tip_length_to_length_ratio=0.12).shift(UP * 0.55)
        stop_bar = Line([-5.0, 1.1, 0], [-5.0, 2.3, 0], color=ACC, stroke_width=5)
        self.play(Create(ret), run_time=0.7)
        self.play(Create(stop_bar), run_time=0.4)

        hand = label("control returns — you still buy it", size=28, color=ACC)
        hand.move_to(DOWN * 2.5)
        self.play(FadeIn(hand), run_time=0.5)
        self.wait(2.2)  # retimed to real audio (35.24s) — was 6.0


# ─────────────────────────────────────────────────────────────────────────────
#  B04_TierTwo   (target ~56s)
#  A plan building itself box by box, hitting a real conflict, stopping.
# ─────────────────────────────────────────────────────────────────────────────
class B04_TierTwo(Scene):

    def construct(self):
        self.camera.background_color = BG
        strip = spectrum_strip(active=2)
        self.play(FadeIn(strip), run_time=0.5)
        self.wait(0.6)

        ask = serif('"…but only if it doesn\'t clash with my calendar"',
                    size=32, color=INK, italic=True).move_to(UP * 2.0)
        ask_box = auto_box(ask, h_pad=0.5, v_pad=0.32, color=SOFT,
                           fill_color=SOFT, fill_opacity=0.05)
        self.play(Create(ask_box), FadeIn(ask), run_time=0.7)
        self.wait(10.0)  # narration sets up the tier before the plan starts

        # ── The plan builds one box at a time ─────────────────────────────────
        names = ["Check\ncalendar", "Search\nflights", "Cross-\nreference"]
        boxes = VGroup()
        for n in names:
            txt = label(n, size=26, color=INK, line_spacing=0.7)
            bx = auto_box(txt, h_pad=0.36, v_pad=0.28, color=INK)
            boxes.add(VGroup(bx, txt))
        boxes.arrange(RIGHT, buff=1.05).move_to([0, 0.55, 0])

        arrows = VGroup(*[
            Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), color=SOFT,
                  stroke_width=2.5, buff=0.14,
                  max_tip_length_to_length_ratio=0.16)
            for i in range(len(boxes) - 1)
        ])

        for i, b in enumerate(boxes):
            self.play(FadeIn(b), run_time=0.45)
            if i < len(arrows):
                self.play(Create(arrows[i]), run_time=0.3)
            self.wait(2.2)
        self.wait(1.6)

        # ── The conflict, found ───────────────────────────────────────────────
        cal = VGroup(*[
            Rectangle(width=0.85, height=0.5, stroke_width=2, color=GHOST,
                      fill_color=GHOST, fill_opacity=0.08)
            for _ in range(5)
        ]).arrange(RIGHT, buff=0.1).move_to([0, -1.15, 0])
        cal_lab = label("Friday", size=24, color=SOFT).next_to(cal, LEFT, buff=0.35)
        self.play(FadeIn(cal), FadeIn(cal_lab), run_time=0.5)
        self.wait(1.0)

        meet = cal[1]
        meet_txt = label("9 AM", size=24, color=ACC).next_to(meet, UP, buff=0.14)
        self.play(meet.animate.set_color(ACC).set_fill(ACC, opacity=0.25),
                  FadeIn(meet_txt), run_time=0.6)
        self.wait(3.5)

        # ── Two options, side by side, held for the comparison ────────────────
        opt_a = VGroup(
            mono("07:00", size=28, color=INK),
            label("clears the meeting", size=25, color=SOFT),
        ).arrange(RIGHT, buff=0.4)
        opt_b = VGroup(
            mono("11:00", size=28, color=INK),
            label("you miss the meeting", size=25, color=SOFT),
        ).arrange(RIGHT, buff=0.4)
        opts = VGroup(opt_a, opt_b).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        opts.move_to([0, -2.3, 0])

        self.play(FadeIn(opt_a), run_time=0.5)
        self.wait(2.5)
        self.play(FadeIn(opt_b), run_time=0.5)
        self.wait(1.6)
        # Keep the reference — an inline strike() would be orphaned by the
        # FadeOut below and leave a stray rule across the frame.
        opt_b_strike = strike(opt_b)
        self.play(Create(opt_b_strike), run_time=0.5)
        self.wait(5.0)

        # ── The chain halts at the human ──────────────────────────────────────
        self.play(FadeOut(cal), FadeOut(cal_lab), FadeOut(meet_txt),
                  FadeOut(opts), FadeOut(opt_b_strike), run_time=0.5)

        ask_txt = label("Ask you", size=26, color=ACC)
        ask_bx = auto_box(ask_txt, h_pad=0.36, v_pad=0.28, color=ACC)
        ask_node = VGroup(ask_bx, ask_txt).next_to(boxes, DOWN, buff=1.0)
        drop = Arrow(boxes[2].get_bottom(), ask_node.get_top(), color=ACC,
                     stroke_width=2.5, buff=0.12,
                     max_tip_length_to_length_ratio=0.2)
        self.play(Create(drop), FadeIn(ask_node), run_time=0.7)
        self.wait(1.2)

        halt = Line(ask_node.get_left() + LEFT * 0.5, ask_node.get_right() + RIGHT * 0.5,
                    color=ACC, stroke_width=5).next_to(ask_node, DOWN, buff=0.3)
        halt_lab = label("bounded — it stops before it spends", size=27, color=ACC)
        halt_lab.next_to(halt, DOWN, buff=0.3)
        self.play(Create(halt), FadeIn(halt_lab), run_time=0.6)
        self.wait(3.5)

        marks = VGroup(*[
            checked(s, size=25, color=SOFT)
            for s in ("ordered steps", "tools in sequence", "plan adapted")
        ]).arrange(RIGHT, buff=0.7).move_to(DOWN * 3.25)
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.3),
                  run_time=1.0)
        self.wait(2.3)  # retimed to real audio (48.28s) — was 10.0


# ─────────────────────────────────────────────────────────────────────────────
#  B05_TierThree   (target ~61s)
#  The loop actually runs: days tick, memory persists, it re-books itself.
# ─────────────────────────────────────────────────────────────────────────────
class B05_TierThree(Scene):

    def construct(self):
        self.camera.background_color = BG
        strip = spectrum_strip(active=3)
        self.play(FadeIn(strip), run_time=0.5)
        self.wait(0.6)

        # ── The ring ──────────────────────────────────────────────────────────
        stages = ["Monitor", "Decide", "Act", "Remember"]
        R = 1.85
        centre = np.array([-2.3, -0.15, 0])
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
                  run_time=1.3)
        self.wait(8.0)   # narration defines the tier before the loop moves

        # ── One slow lap, each stage lighting as the pulse passes ─────────────
        pulse = Dot(radius=0.15, color=ACC).move_to(centre + np.array([0, R, 0]))
        self.play(FadeIn(pulse), run_time=0.3)
        for i in range(4):
            self.play(
                Rotate(pulse, angle=-PI / 2, about_point=centre),
                nodes[i].animate.set_color(ACC),
                run_time=0.75,
            )
            self.play(nodes[i].animate.set_color(INK), run_time=0.25)
        self.wait(3.0)

        # ── Days start passing while it keeps going ───────────────────────────
        day = label("day 1", size=30, color=SOFT).move_to([4.3, 2.1, 0])
        self.play(FadeIn(day), run_time=0.4)
        for d in (4, 9, 17):
            self.play(Rotate(pulse, angle=-2 * PI, about_point=centre), run_time=1.0)
            # A straight Transform between digit-mismatched Text mobjects
            # morphs glyph curves into an illegible smear mid-transition
            # (found in 4K visual QC) — swap via a fast fade instead.
            new = label(f"day {d}", size=30, color=SOFT).move_to([4.3, 2.1, 0])
            self.play(FadeOut(day, run_time=0.15), run_time=0.15)
            day = new
            self.play(FadeIn(day, run_time=0.15), run_time=0.15)
        self.wait(3.5)

        # ── Memory chips drop in and stay ─────────────────────────────────────
        mem_head = label("carried forward", size=26, color=SOFT).move_to([4.0, 0.85, 0])
        self.play(FadeIn(mem_head), run_time=0.4)
        chips = VGroup(
            label_chip("aisle seat", ACC, size=24),
            label_chip("morning departure", ACC, size=24),
        ).arrange(DOWN, buff=0.3).next_to(mem_head, DOWN, buff=0.4)
        for c in chips:
            self.play(FadeIn(c, shift=LEFT * 0.25), run_time=0.5)
            self.wait(2.8)
        self.wait(3.5)

        # ── The airline cancels; the loop handles it without leaving ──────────
        cancel = label("flight cancelled", size=27, color=ACC).move_to([4.0, -1.5, 0])
        self.play(FadeIn(cancel), run_time=0.5)
        self.play(Create(strike(cancel, color=ACC)), run_time=0.4)
        self.wait(2.2)

        self.play(Rotate(pulse, angle=-2 * PI, about_point=centre), run_time=0.9)
        rebook = label("re-booked", size=27, color=INK).next_to(cancel, DOWN, buff=0.45)
        self.play(FadeIn(rebook), run_time=0.4)
        self.wait(1.0)
        note = label('"handled it."', size=26, color=SOFT).next_to(rebook, DOWN, buff=0.35)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(4.0)

        # ── The line that names it ────────────────────────────────────────────
        land = serif("Nothing restarted from zero.", size=34, color=ACC)
        land.move_to(DOWN * 3.2)
        self.play(FadeIn(land), run_time=0.6)
        self.play(Rotate(pulse, angle=-2 * PI, about_point=centre), run_time=1.0)
        self.wait(3.4)  # retimed to real audio (51.97s) — was 12.4


# ─────────────────────────────────────────────────────────────────────────────
#  B06_TheChecklist   (target ~40s)
#  Three diagnostic questions, then the framework turned on the market.
#  This is the falsifiability beat — the label mostly fails its own test.
# ─────────────────────────────────────────────────────────────────────────────
class B06_TheChecklist(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Teardown Checklist", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(2.0)

        qs = [
            ("Does it use tools, or just talk?", "just talk → tier 0"),
            ("Does it chain steps into a plan?", "chaining → tier 2"),
            ("Does it run on, and remember?", "both → tier 3"),
        ]
        rows = VGroup()
        for q, a in qs:
            qt = label(q, size=30, color=INK)
            at = label(a, size=26, color=ACC)
            rows.add(VGroup(qt, at).arrange(RIGHT, buff=0.7))
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to([0, 1.15, 0])

        for r in rows:
            self.play(FadeIn(r[0]), run_time=0.4)
            self.wait(3.0)
            self.play(FadeIn(r[1]), run_time=0.35)
            self.wait(2.4)
        self.wait(2.0)

        # ── Now turn it on the market ─────────────────────────────────────────
        self.play(FadeOut(t), rows.animate.scale(0.82).move_to([0, 2.35, 0]),
                  run_time=0.7)

        seg_w = 12.0 / 4
        segs = VGroup(*[
            Rectangle(width=seg_w, height=0.85, stroke_width=2.5, color=INK,
                      fill_color=INK, fill_opacity=0.12)
            for _ in range(4)
        ]).arrange(RIGHT, buff=0.18).move_to(DOWN * 0.85)
        labs = VGroup(*[
            label(TIERS[i], size=28, color=SOFT).next_to(segs[i], DOWN, buff=0.28)
            for i in range(4)
        ])
        self.play(FadeIn(segs), FadeIn(labs), run_time=0.7)
        self.wait(1.2)

        # The bracket: where products marketed as agentic actually land.
        span = VGroup(segs[1], segs[2])
        brace = Brace(span, direction=UP, color=ACC, buff=0.12)
        brace_lab = label("most products sold as “agentic”", size=27, color=ACC)
        brace_lab.next_to(brace, UP, buff=0.2)
        self.play(segs[1].animate.set_stroke(ACC, width=3.5).set_fill(ACC, opacity=0.2),
                  segs[2].animate.set_stroke(ACC, width=3.5).set_fill(ACC, opacity=0.2),
                  run_time=0.6)
        self.play(GrowFromCenter(brace), FadeIn(brace_lab), run_time=0.7)
        self.wait(4.6)

        # Tier 3 dims — rare, hard, unsolved.
        self.play(segs[3].animate.set_stroke(GHOST, width=2).set_fill(GHOST, opacity=0.06),
                  labs[3].animate.set_color(GHOST), run_time=0.6)
        rare = label("rare · harder to control · still being figured out",
                     size=26, color=GHOST)
        # Centred under the whole bar, not under labs[3] — anchoring it to the
        # rightmost label ran it off the frame edge.
        rare.next_to(labs, DOWN, buff=0.65)
        self.play(FadeIn(rare), run_time=0.5)
        self.wait(3.1)  # retimed to real audio (35.61s) — was 7.5
