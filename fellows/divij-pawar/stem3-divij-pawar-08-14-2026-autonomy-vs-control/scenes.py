"""scenes.py — Manim scenes for autonomy-vs-control (claude-divij).

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757, soft #73705F,
ghost #A9A491 — the Claude fidelity palette per ai-explainer SKILL.md. ONE
accent per beat. The source script's greyed→green send button is deliberately
NOT carried: state changes here are read from activation and label, never from
a second hue. No blue, no green.

Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF,
editorial voice only) / PT Mono (MONO, data only) — see graphics_lib.py.
Boxes are content-fitted via auto_box, never hand-measured.

Two doctrine notes specific to this reel:

  * B04's curves are QUALITATIVE. They carry no axis numbers, on purpose —
    the reel argues a shape (steady rise vs. flat-then-bend), it does not
    claim measured data. Do NOT add tick values later; that would convert a
    declared argument into a fabricated measurement (SOURCES.md).
  * B05's three precedents are drawn LINE MARKS, not photographs. Under
    nopunt only a genuine archival photograph is a legitimate HOLD; generic
    stock objects standing in for concepts are a PUNT.

Pace: normal-speed creates/fades with deliberate HOLDS sized to the
narration. Targets are against `estimated_duration_s` in beat_sheet.json;
re-check against `actual_duration_s` once Kokoro has run.
"""
import numpy as np
from graphics_lib import *

# ── Palette (claude-stage retint, per ai-explainer SKILL.md) ──────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")

TIERS = ["Read-Only", "Approval-Gated", "Full Autonomy"]


def strike(mobj, color=None):
    return Line(mobj.get_left() + LEFT * 0.08, mobj.get_right() + RIGHT * 0.08,
                color=color if color is not None else ACC, stroke_width=3.0)


def stake_bar(h, color):
    """A stake mark — height encodes what's at risk. Position + label carry
    the meaning too, so this reads in grayscale."""
    return Rectangle(width=0.5, height=h, stroke_width=0,
                     fill_color=color, fill_opacity=0.85)


# ─────────────────────────────────────────────────────────────────────────────
#  B01_TheBet   (target ~21s)
#  The BLUF: three permissions, three visibly different stakes, one of them
#  one-way.
# ─────────────────────────────────────────────────────────────────────────────
class B01_TheBet(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Every Permission Is a Bet", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(0.8)

        specs = [
            ("read your\ncalendar", 0.7, SOFT, "small bet"),
            ("send emails\non your behalf", 1.5, SOFT, "bigger bet"),
            ("move money ·\nrun live code", 2.7, ACC, "can't take back"),
        ]
        cols = VGroup()
        for name, h, col, note in specs:
            bar = stake_bar(h, col)
            lab = label(name, size=26, color=INK, line_spacing=0.75)
            lab.next_to(bar, DOWN, buff=0.35)
            nt = label(note, size=25, color=col)
            nt.next_to(bar, UP, buff=0.25)
            cols.add(VGroup(bar, lab, nt))

        # Align the bars on a common baseline so height reads as magnitude.
        for i, c in enumerate(cols):
            c.move_to([-4.2 + i * 4.2, 0, 0])
            c[0].align_to(np.array([0, -1.1, 0]), DOWN)
            c[1].next_to(c[0], DOWN, buff=0.35)
            c[2].next_to(c[0], UP, buff=0.25)

        for c in cols:
            self.play(FadeIn(c[1]), run_time=0.35)
            self.play(GrowFromEdge(c[0], DOWN), run_time=0.5)
            self.play(FadeIn(c[2]), run_time=0.3)
            self.wait(1.9)
        self.wait(1.2)

        # The one-way arrow only under the third.
        oneway = Arrow(cols[2].get_bottom() + DOWN * 0.15 + LEFT * 1.1,
                       cols[2].get_bottom() + DOWN * 0.15 + RIGHT * 1.1,
                       color=ACC, stroke_width=3, buff=0,
                       max_tip_length_to_length_ratio=0.14)
        self.play(Create(oneway), run_time=0.5)
        self.wait(1.6)

        land = serif("A decision you make without noticing you're making it.",
                     size=32, color=SOFT).move_to(DOWN * 3.35)
        self.play(FadeIn(land), run_time=0.6)
        self.wait(3.1)  # retimed to real audio (17.77s) — was 6.3


# ─────────────────────────────────────────────────────────────────────────────
#  B02_BlastRadius   (target ~33s)
#  The framework beat. Radii established physically, then transferred onto
#  permissions.
# ─────────────────────────────────────────────────────────────────────────────
class B02_BlastRadius(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Blast Radius", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(0.6)

        centre = np.array([-3.4, -0.5, 0])
        radii = [0.85, 1.7, 2.6]
        names = ["one bulb", "one room", "one building"]
        opac = [0.06, 0.10, 0.18]

        rings = VGroup()
        rlabs = VGroup()
        for r, n, o in zip(radii, names, opac):
            c = Circle(radius=r, color=SOFT, stroke_width=2.5,
                       fill_color=SOFT, fill_opacity=o).move_to(centre)
            rings.add(c)
            rlabs.add(label(n, size=25, color=SOFT).move_to(
                centre + np.array([0, r + 0.28, 0])))

        for c, l in zip(rings, rlabs):
            self.play(Create(c), FadeIn(l), run_time=0.55)
            self.wait(1.5)
        self.wait(1.4)

        # Wrapped and anchored off-center (x=3.2, not 0) — a single-line 54
        # char sentence at size 30 ran past the safe frame edge on the right.
        judge = serif("The mechanism that fails\ndoesn't have to be dramatic.",
                      size=28, color=INK, line_spacing=0.9).move_to([3.2, 1.6, 0])
        self.play(FadeIn(judge), run_time=0.6)
        self.wait(3.4)

        # ── Transfer: same shape, now measuring permissions ───────────────────
        self.play(FadeOut(judge), FadeOut(rlabs), run_time=0.5)
        head = label("every permission sets one", size=28, color=SOFT)
        head.move_to([3.4, 2.1, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(1.6)

        inner = VGroup(
            label("calendar, read-only", size=27, color=INK),
            label("→  a bad summary", size=26, color=SOFT),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to([3.4, 0.6, 0])
        self.play(rings[0].animate.set_stroke(INK, width=3).set_fill(INK, opacity=0.14),
                  FadeIn(inner), run_time=0.7)
        self.wait(3.2)

        outer = VGroup(
            label("bank account, full write", size=27, color=ACC),
            label("→  money moves", size=26, color=ACC),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to([3.4, -1.1, 0])
        self.play(rings[2].animate.set_stroke(ACC, width=3.5).set_fill(ACC, opacity=0.20),
                  FadeIn(outer), run_time=0.7)
        self.wait(3.4)

        land = label("same mistake · wildly different reach", size=29, color=ACC)
        land.move_to(DOWN * 3.4)
        self.play(FadeIn(land), run_time=0.5)
        self.wait(6.2)  # retimed to real audio (30.25s) — was 8.9


# ─────────────────────────────────────────────────────────────────────────────
#  B03_ThreeModels   (target ~62s)
#  One spectrum, three markers, each demonstrating its own stopping behaviour.
#  The longest beat in the series — one idea, three instances.
# ─────────────────────────────────────────────────────────────────────────────
class B03_ThreeModels(Scene):

    def construct(self):
        self.camera.background_color = BG

        line = Line([-5.6, 2.6, 0], [5.6, 2.6, 0], color=GHOST, stroke_width=3)
        self.play(Create(line), run_time=0.7)

        xs = [-4.4, 0.0, 4.4]
        marks = VGroup(*[Dot(radius=0.17, color=GHOST).move_to([x, 2.6, 0])
                         for x in xs])
        mlabs = VGroup(*[
            label(TIERS[i], size=27, color=SOFT).next_to(marks[i], UP, buff=0.28)
            for i in range(3)
        ])
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.25),
                  LaggedStart(*[FadeIn(l) for l in mlabs], lag_ratio=0.25),
                  run_time=1.3)
        self.wait(6.0)

        # ── 1. Read-only: it reaches, and is stopped ──────────────────────────
        self.play(marks[0].animate.set_color(ACC).scale(1.3),
                  mlabs[0].animate.set_color(ACC), run_time=0.5)

        # Seated below centre so the composition fills the frame rather than
        # clustering in the top third (FILL-THE-CANVAS LAW).
        agent = label_chip("Agent", INK).move_to([-3.9, -0.35, 0])
        files_txt = label("your\nfiles", size=24, color=SOFT, line_spacing=0.75)
        files = VGroup(auto_box(files_txt, h_pad=0.34, v_pad=0.28, color=SOFT),
                       files_txt).move_to([-0.9, -0.35, 0])
        bound = Circle(radius=1.25, color=ACC, stroke_width=2.5).move_to(agent)
        reach = Arrow(agent.get_right(), files.get_left(), color=SOFT,
                      stroke_width=2.5, buff=0.15,
                      max_tip_length_to_length_ratio=0.14)

        self.play(FadeIn(agent), FadeIn(files), run_time=0.6)
        self.wait(1.6)
        self.play(Create(reach), run_time=0.5)
        self.play(Create(bound), run_time=0.5)
        self.play(reach.animate.set_color(GHOST).set_opacity(0.35), run_time=0.4)
        self.wait(2.0)

        cost1 = label("cost: your time, reading a bad answer", size=26, color=SOFT)
        cost1.move_to([2.9, -0.35, 0])
        self.play(FadeIn(cost1), run_time=0.5)
        self.wait(4.5)

        # ── 2. Approval-gated: it proposes, then waits ────────────────────────
        self.play(FadeOut(agent), FadeOut(files), FadeOut(bound),
                  FadeOut(reach), FadeOut(cost1),
                  marks[0].animate.set_color(INK).scale(1 / 1.3),
                  mlabs[0].animate.set_color(SOFT), run_time=0.6)
        self.play(marks[1].animate.set_color(ACC).scale(1.3),
                  mlabs[1].animate.set_color(ACC), run_time=0.5)

        draft_rows = VGroup(*[
            label(r, size=25, color=INK) for r in
            ("To: the client", "Subject: revised timeline", "…")
        ]).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        draft_box = auto_box(draft_rows, h_pad=0.5, v_pad=0.35, color=INK)
        draft = VGroup(draft_box, draft_rows).move_to([-2.6, -0.45, 0])

        send_txt = label("Send", size=27, color=GHOST)
        send_box = auto_box(send_txt, h_pad=0.55, v_pad=0.3, color=GHOST,
                            fill_color=GHOST, fill_opacity=0.12)
        send = VGroup(send_box, send_txt).move_to([1.9, -0.45, 0])

        self.play(Create(draft_box), FadeIn(draft_rows), run_time=0.7)
        self.wait(1.8)
        self.play(FadeIn(send), run_time=0.5)
        waiting = label("nothing has left yet", size=26, color=SOFT)
        waiting.next_to(send, DOWN, buff=0.4)
        self.play(FadeIn(waiting), run_time=0.4)
        self.wait(4.6)

        # The human presses it — activation and label carry the change, not hue.
        hand = label("a person looks, and confirms", size=26, color=ACC)
        hand.next_to(send, UP, buff=0.45)
        self.play(FadeIn(hand), run_time=0.5)
        self.play(send_box.animate.set_stroke(ACC, width=3.5).set_fill(ACC, opacity=0.85),
                  send_txt.animate.set_color(BG), run_time=0.6)
        self.play(FadeOut(waiting), run_time=0.3)
        gone = label("now it goes", size=26, color=ACC).next_to(send, DOWN, buff=0.4)
        self.play(FadeIn(gone), run_time=0.4)
        self.wait(5.0)

        # ── 3. Full autonomy: no pause at all ─────────────────────────────────
        self.play(FadeOut(draft), FadeOut(send), FadeOut(hand), FadeOut(gone),
                  marks[1].animate.set_color(INK).scale(1 / 1.3),
                  mlabs[1].animate.set_color(SOFT), run_time=0.6)
        self.play(marks[2].animate.set_color(ACC).scale(1.3),
                  mlabs[2].animate.set_color(ACC), run_time=0.5)

        acts = VGroup(*[
            label(a, size=27, color=INK) for a in
            ("auto-pays the bills",
             "auto-deploys to production",
             "auto-replies to customers")
        ]).arrange(DOWN, buff=0.32).move_to([0, 0.55, 0])
        for a in acts:
            self.play(FadeIn(a, shift=LEFT * 0.2), run_time=0.3)
            self.wait(2.0)
        self.wait(1.6)

        after = label("you find out afterward — if at all", size=28, color=ACC)
        after.move_to(DOWN * 1.75)
        self.play(FadeIn(after), run_time=0.5)
        self.wait(2.6)

        both = VGroup(
            label("the most useful", size=28, color=INK),
            label("the most dangerous", size=28, color=ACC),
        ).arrange(RIGHT, buff=1.1).move_to(DOWN * 2.85)
        same = label("for exactly the same reason", size=26, color=SOFT)
        same.next_to(both, DOWN, buff=0.3)
        self.play(FadeIn(both), run_time=0.5)
        self.wait(1.4)
        self.play(FadeIn(same), run_time=0.4)
        self.wait(8.5)  # retimed to real audio (59.52s) — was 11.0


# ─────────────────────────────────────────────────────────────────────────────
#  B04_TheTradeoff   (target ~48s)
#  Two QUALITATIVE curves (no axis numbers — see module docstring), then one
#  financial agent walked across all three tiers. The worked example.
# ─────────────────────────────────────────────────────────────────────────────
class B04_TheTradeoff(Scene):

    def construct(self):
        self.camera.background_color = BG

        axes = Axes(
            x_range=[0, 3, 1], y_range=[0, 3, 1],
            x_length=9.2, y_length=4.2,
            axis_config={"color": SOFT, "stroke_width": 2.5,
                         "include_ticks": False, "include_tip": False},
        ).move_to([0, 0.35, 0])
        self.play(Create(axes), run_time=0.8)

        tier_x = [0.35, 1.5, 2.75]
        tlabs = VGroup(*[
            label(TIERS[i], size=25, color=SOFT).move_to(
                axes.c2p(tier_x[i], 0) + DOWN * 0.42)
            for i in range(3)
        ])
        self.play(LaggedStart(*[FadeIn(l) for l in tlabs], lag_ratio=0.25),
                  run_time=0.9)
        self.wait(3.0)

        # ── Usefulness: steady, even rise ─────────────────────────────────────
        useful = axes.plot(lambda x: 0.5 + 0.80 * x, x_range=[0, 3],
                           color=INK, stroke_width=5)
        ulab = label("Usefulness", size=27, color=INK).move_to(
            axes.c2p(3, 2.9) + RIGHT * 0.1 + UP * 0.25)
        self.play(Create(useful), FadeIn(ulab), run_time=1.6)
        self.wait(2.4)

        # ── Risk: flat, then a hard bend at the last step ─────────────────────
        def risk_fn(x):
            return 0.28 if x <= 1.9 else 0.28 + 2.55 * (x - 1.9) ** 2

        risk = axes.plot(risk_fn, x_range=[0, 3], color=ACC, stroke_width=5)
        rlab = label("Risk", size=27, color=ACC).move_to(
            axes.c2p(0.45, 0.28) + UP * 0.42)
        self.play(Create(risk), FadeIn(rlab), run_time=1.8)
        self.wait(3.2)

        cheap = label("a lot of usefulness, very little added risk",
                      size=26, color=SOFT).move_to(axes.c2p(1.0, 2.3) + UP * 0.15)
        self.play(FadeIn(cheap), run_time=0.5)
        self.wait(3.6)

        # cheap and lost sat at nearly the same height and OVERLAPPED
        # illegibly once both were on screen (found in 4K visual QC) — they
        # describe sequential clauses in the narration, so clear the first
        # before the second lands instead of holding both at once.
        self.play(FadeOut(cheap), run_time=0.4)

        # ── What disappears at the last step ──────────────────────────────────
        bend = DashedLine(axes.c2p(1.9, 0), axes.c2p(1.9, 3.0),
                          color=ACC, stroke_width=2, dash_length=0.12)
        lost = label("a person, looking, before anything happens",
                     size=26, color=ACC).move_to(axes.c2p(2.1, 2.5) + RIGHT * 0.2)
        self.play(Create(bend), run_time=0.5)
        self.play(FadeIn(lost), run_time=0.5)
        self.wait(1.2)
        # Keep the reference — an inline strike() would be orphaned by the
        # FadeOut below and leave a stray rule straight across the chart.
        lost_strike = strike(lost, color=ACC)
        self.play(Create(lost_strike), run_time=0.5)
        self.wait(3.0)

        # ── The worked example walks the same axis ────────────────────────────
        self.play(FadeOut(lost), FadeOut(lost_strike),
                  FadeOut(rlab), FadeOut(ulab), run_time=0.5)
        head = label("one financial agent, three settings", size=28, color=SOFT)
        head.move_to([0, 3.3, 0])
        self.play(FadeIn(head), run_time=0.5)

        agent = Dot(radius=0.16, color=ACC).move_to(axes.c2p(tier_x[0], 0.28))
        cap1 = label("shows your spending — safe, modestly useful",
                     size=26, color=SOFT).move_to([0, -2.75, 0])
        self.play(FadeIn(agent), FadeIn(cap1), run_time=0.6)
        self.wait(3.0)

        # Transform between differently-worded captions morphs glyph curves
        # into a distracting typographic smear mid-transition (same defect
        # class caught elsewhere in 4K visual QC) — fade-swap instead, timed
        # to land either side of the agent's move.
        cap2 = label("drafts a payment for approval — useful, still safe",
                     size=26, color=SOFT).move_to([0, -2.75, 0])
        self.play(agent.animate.move_to(axes.c2p(tier_x[1], 0.28)),
                  FadeOut(cap1, run_time=0.45), run_time=0.9)
        cap1 = cap2
        self.play(FadeIn(cap1), run_time=0.4)
        self.wait(2.8)

        cap3 = label("pays automatically — the most useful of the three",
                     size=26, color=SOFT).move_to([0, -2.75, 0])
        self.play(agent.animate.move_to(axes.c2p(tier_x[2], risk_fn(tier_x[2]))),
                  FadeOut(cap1, run_time=0.5), run_time=1.0)
        cap1 = cap3
        self.play(FadeIn(cap1), run_time=0.4)
        self.wait(2.0)

        # ── Until it doesn't ──────────────────────────────────────────────────
        wrong = VGroup(
            label("wrong amount", size=27, color=ACC),
            label("wrong account", size=27, color=ACC),
        ).arrange(RIGHT, buff=0.9).move_to([0, -3.35, 0])
        self.play(FadeIn(wrong), run_time=0.5)
        self.wait(1.4)
        nodraft = label("and no draft to catch it — there never was one",
                        size=27, color=ACC).move_to([0, -2.75, 0])
        self.play(FadeOut(cap1), FadeIn(nodraft), run_time=0.6)
        self.wait(3.5)  # retimed to real audio (42.33s) — was 9.2


# ─────────────────────────────────────────────────────────────────────────────
#  B05_SpeedAndVisibility   (target ~45s)
#  The falsifiability beat. The delegation analogy is granted in full across
#  three real precedents, then broken on one axis: elapsed time.
#  Precedents are drawn LINE MARKS, never photographs (see module docstring).
# ─────────────────────────────────────────────────────────────────────────────
class B05_SpeedAndVisibility(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("This Isn't New", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.8)

        # ── Three bounded delegations humans already make ─────────────────────
        # Bound lines wrapped to two lines each — the longest ("specific
        # accounts, specific limits") made its card wide enough that the
        # three-card row, naively arranged and centered, overflowed both
        # frame edges. The width cap below is a defensive second guard.
        precedents = [
            ("company card", "spending limit"),
            ("autopilot", "cruise only,\nnever takeoff"),
            ("power of attorney", "specific accounts,\nspecific limits"),
        ]
        cards = VGroup()
        for name, bound in precedents:
            nm = label(name, size=28, color=INK)
            rule = Line(LEFT * 1.3, RIGHT * 1.3, color=ACC, stroke_width=3)
            bd = label(bound, size=24, color=SOFT, line_spacing=0.85)
            body = VGroup(nm, rule, bd).arrange(DOWN, buff=0.26)
            bx = auto_box(body, h_pad=0.4, v_pad=0.35, color=SOFT)
            cards.add(VGroup(bx, body))
        cards.arrange(RIGHT, buff=0.5)
        if cards.width > 12.6:
            cards.scale(12.6 / cards.width)
        cards.move_to([0, 0.75, 0])

        for c in cards:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.5)
            self.wait(2.3)
        self.wait(1.2)

        granted = label("all of these are blast-radius decisions", size=28, color=SOFT)
        granted.move_to([0, -1.6, 0])
        self.play(FadeIn(granted), run_time=0.5)
        self.wait(3.4)

        # ── Where the analogy breaks: one shared time axis ────────────────────
        self.play(FadeOut(cards), FadeOut(granted), FadeOut(t), run_time=0.6)
        head = label("what's different: speed, and visibility", size=30, color=INK)
        head.move_to([0, 3.2, 0])
        self.play(FadeIn(head), run_time=0.5)
        self.wait(1.6)

        axis = Line([-5.8, -3.0, 0], [5.8, -3.0, 0], color=GHOST, stroke_width=2.5)
        axis_lab = label("time", size=25, color=GHOST).next_to(axis, DOWN, buff=0.2)
        self.play(Create(axis), FadeIn(axis_lab), run_time=0.6)

        # Human: warning signs spread out, catchable.
        h_line = Line([-5.8, 1.15, 0], [5.8, 1.15, 0], color=SOFT, stroke_width=2.5)
        h_lab = label("a human", size=27, color=SOFT).move_to([-5.0, 1.75, 0])
        self.play(Create(h_line), FadeIn(h_lab), run_time=0.6)

        signs = [("hesitation", -3.2), ("a question", -0.6), ("a paper trail", 2.2)]
        sign_grp = VGroup()
        for name, x in signs:
            tick = Line([x, 0.95, 0], [x, 1.35, 0], color=SOFT, stroke_width=3)
            lb = label(name, size=24, color=SOFT).next_to(tick, DOWN, buff=0.22)
            sign_grp.add(VGroup(tick, lb))
        for s in sign_grp:
            self.play(FadeIn(s), run_time=0.35)
            self.wait(1.1)

        act_h = Line([4.6, 0.95, 0], [4.6, 1.35, 0], color=ACC, stroke_width=4)
        act_h_lab = label("acts", size=24, color=ACC).next_to(act_h, UP, buff=0.18)
        self.play(Create(act_h), FadeIn(act_h_lab), run_time=0.4)
        catch = label("catchable, mid-process", size=25, color=SOFT)
        catch.move_to([0.4, 0.35, 0])
        self.play(FadeIn(catch), run_time=0.4)
        self.wait(3.0)

        # Agent: decision and action collapse to one tick.
        a_line = Line([-5.8, -1.35, 0], [5.8, -1.35, 0], color=SOFT, stroke_width=2.5)
        a_lab = label("an agent", size=27, color=SOFT).move_to([-5.0, -0.75, 0])
        self.play(Create(a_line), FadeIn(a_lab), run_time=0.6)
        self.wait(1.4)

        tick = Line([-3.2, -1.55, 0], [-3.2, -1.15, 0], color=ACC, stroke_width=5)
        tick_lab = label("decision + action", size=25, color=ACC)
        tick_lab.next_to(tick, UP, buff=0.2)
        self.play(Create(tick), FadeIn(tick_lab), run_time=0.5)
        self.wait(2.2)

        first = Line([3.9, -1.55, 0], [3.9, -1.15, 0], color=ACC, stroke_width=3)
        first_lab = label("the first sign anything went wrong",
                          size=25, color=ACC).next_to(first, DOWN, buff=0.22)
        self.play(Create(first), FadeIn(first_lab), run_time=0.5)
        self.wait(1.6)

        irr = label("already irreversible", size=27, color=ACC)
        irr.next_to(first_lab, DOWN, buff=0.25)
        self.play(FadeIn(irr), run_time=0.5)
        self.wait(7.4)  # retimed to real audio (42.88s) — was 9.5


# ─────────────────────────────────────────────────────────────────────────────
#  B06_TheQuestion   (target ~34s)
#  Rope and reach, measured — then the reel's question held alone.
#  The source's door motif resolves here (SOURCES.md).
# ─────────────────────────────────────────────────────────────────────────────
class B06_TheQuestion(Scene):

    def construct(self):
        self.camera.background_color = BG

        anchor = Dot(radius=0.13, color=INK).move_to([-5.4, 0.6, 0])
        anchor_lab = label("you", size=26, color=SOFT).next_to(anchor, DOWN, buff=0.3)
        self.play(FadeIn(anchor), FadeIn(anchor_lab), run_time=0.5)
        self.wait(2.2)

        # ── Minimum rope ──────────────────────────────────────────────────────
        rope = Line([-5.4, 0.6, 0], [-4.0, 0.6, 0], color=INK, stroke_width=4)
        ring = Circle(radius=0.55, color=SOFT, stroke_width=2.5,
                      fill_color=SOFT, fill_opacity=0.10).move_to([-4.0, 0.6, 0])
        r_lab = label("read-only", size=26, color=SOFT).next_to(ring, UP, buff=0.3)
        self.play(Create(rope), run_time=0.5)
        self.play(Create(ring), FadeIn(r_lab), run_time=0.5)
        self.wait(3.0)

        # ── All the rope, all the reach ───────────────────────────────────────
        rope2 = Line([-5.4, 0.6, 0], [3.5, 0.6, 0], color=INK, stroke_width=4)
        ring2 = Circle(radius=1.85, color=ACC, stroke_width=3,
                       fill_color=ACC, fill_opacity=0.13).move_to([3.5, 0.6, 0])
        r_lab2 = label("full autonomy", size=26, color=ACC).next_to(ring2, UP, buff=0.3)
        self.play(Transform(rope, rope2), run_time=1.2)
        self.play(Transform(ring, ring2), Transform(r_lab, r_lab2), run_time=0.9)
        self.wait(3.4)

        # ── The middle is where the work is ───────────────────────────────────
        span = Line([-4.0, -1.2, 0], [3.5, -1.2, 0], color=ACC, stroke_width=3)
        brace_lab = label("most of what actually matters happens here",
                          size=27, color=ACC).next_to(span, DOWN, buff=0.35)
        self.play(Create(span), FadeIn(brace_lab), run_time=0.8)
        self.wait(2.8)

        gates = VGroup(*[
            Line([x, -1.45, 0], [x, -0.95, 0], color=INK, stroke_width=4)
            for x in (-2.1, -0.3, 1.5)
        ])
        gate_lab = label("approval gates — chosen by hand", size=26, color=SOFT)
        gate_lab.next_to(brace_lab, DOWN, buff=0.3)
        self.play(LaggedStart(*[Create(g) for g in gates], lag_ratio=0.3),
                  run_time=0.9)
        self.play(FadeIn(gate_lab), run_time=0.4)
        self.wait(3.6)

        # ── Everything falls away but the question ────────────────────────────
        self.play(FadeOut(VGroup(anchor, anchor_lab, rope, ring, r_lab,
                                 span, brace_lab, gates, gate_lab)),
                  run_time=1.2)
        self.wait(0.6)

        q = serif("How much do you let it do without you?",
                  size=46, color=INK).move_to(ORIGIN)
        self.play(FadeIn(q), run_time=1.0)
        self.wait(5.2)  # retimed to real audio (28.80s) — was 10.4
