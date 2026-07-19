import sys, json, os, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ─────────────────────────────────────────────────────────────────────────────
# B01 — Title card
# ─────────────────────────────────────────────────────────────────────────────
class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why the Restriction Point", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Is a One-Way Gate", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ─────────────────────────────────────────────────────────────────────────────
# B02 — Cell A state: pre-restriction
# ─────────────────────────────────────────────────────────────────────────────
class B02_CellAState(Scene):
    def construct(self):
        total = DUR["B02"]
        # Label chip
        chip = LabelChip("Cell A  pre-restriction", accent=CRIMSON, size=24)
        chip.to_edge(UP, buff=0.7)

        # State labels
        lbl_gf = Text("Growth signals", font=SERIF, color=INK, font_size=26)
        lbl_cd = SerifLabel("Cyclin D rising", accent=CRIMSON, size=24)
        lbl_rb = SerifLabel("Rb hypophosphorylated", accent=CRIMSON, size=24)
        lbl_e2f = SerifLabel("E2F captured", accent=CRIMSON, size=24)

        state_group = VGroup(lbl_gf, lbl_cd, lbl_rb, lbl_e2f).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        state_group.move_to(LEFT * 2.5 + DOWN * 0.3)

        # Arrow from GF to cyclin D
        arrow = Arrow(lbl_gf.get_right() + RIGHT * 0.05,
                      lbl_cd.get_left() + LEFT * 0.05,
                      buff=0.1, color=INK, stroke_width=2, max_tip_length_to_length_ratio=0.15)

        # Gate: Rb as a rectangle blocking E2F
        gate = Rectangle(width=1.6, height=0.7).set_fill(CRIMSON, 0.25).set_stroke(CRIMSON, 2)
        gate_label = Text("Rb GATE", font=DISPLAY, color=CRIMSON, font_size=18)
        gate_label.move_to(gate)
        rb_block = VGroup(gate, gate_label)
        rb_block.move_to(RIGHT * 3.5 + DOWN * 0.3)

        locked = Text("E2F locked", font=DISPLAY, color=INK, font_size=20)
        locked.next_to(rb_block, DOWN, buff=0.3)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(lbl_gf), run_time=0.5)
        self.play(GrowArrow(arrow), FadeIn(lbl_cd), run_time=0.7)
        self.play(FadeIn(lbl_rb), FadeIn(rb_block), run_time=0.7)
        self.play(FadeIn(lbl_e2f), FadeIn(locked), run_time=0.6)
        self.wait(max(0.3, total - 3.0))


# ─────────────────────────────────────────────────────────────────────────────
# B03 — Cell B state: post-restriction
# ─────────────────────────────────────────────────────────────────────────────
class B03_CellBState(Scene):
    def construct(self):
        total = DUR["B03"]
        chip = LabelChip("Cell B  post-restriction", accent=TEAL, size=24)
        chip.to_edge(UP, buff=0.7)

        lbl_ce = SerifLabel("Cyclin E transcribed", accent=TEAL, size=24)
        lbl_cdk = SerifLabel("CDK2 phosphorylating Rb", accent=TEAL, size=24)
        lbl_rb = SerifLabel("Rb hyperphosphorylated", accent=TEAL, size=24)
        lbl_e2f = SerifLabel("E2F free", accent=TEAL, size=24)

        state_group = VGroup(lbl_ce, lbl_cdk, lbl_rb, lbl_e2f).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        state_group.move_to(LEFT * 2.5 + DOWN * 0.3)

        # Gate: open
        gate = Rectangle(width=1.6, height=0.7).set_fill(TEAL, 0.25).set_stroke(TEAL, 2)
        gate_label = Text("Rb OPEN", font=DISPLAY, color=TEAL, font_size=18)
        gate_label.move_to(gate)
        rb_open = VGroup(gate, gate_label)
        rb_open.move_to(RIGHT * 3.5 + UP * 0.5)

        free = Text("E2F free", font=DISPLAY, color=TEAL, font_size=20)
        free.next_to(rb_open, DOWN, buff=0.3)

        sphase = Text("S-phase genes ON", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        sphase.next_to(free, DOWN, buff=0.3)

        # Feedback loop indicator
        fb_label = SerifLabel("positive feedback running", accent=TEAL, size=22)
        fb_label.move_to(RIGHT * 3.5 + DOWN * 1.8)

        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(lbl_ce), run_time=0.5)
        self.play(FadeIn(lbl_cdk), FadeIn(rb_open), run_time=0.7)
        self.play(FadeIn(lbl_rb), FadeIn(free), run_time=0.6)
        self.play(FadeIn(lbl_e2f), FadeIn(sphase), run_time=0.6)
        self.play(FadeIn(fb_label), run_time=0.5)
        self.wait(max(0.3, total - 3.4))


# ─────────────────────────────────────────────────────────────────────────────
# B04 — The Question card
# ─────────────────────────────────────────────────────────────────────────────
class B04_Question(Scene):
    def construct(self):
        total = DUR["B04"]
        q1 = Text("Growth factor withdrawal should stop division.", font=SERIF, color=INK,
                  font_size=32, weight=BOLD)
        q1.move_to(UP * 0.9)
        dek = Text("Same signal removed. One cell stops. One cell does not.", font=SERIF,
                   color=INK, font_size=26)
        dek.next_to(q1, DOWN, buff=0.5)
        ask = Text("Why does timing relative to the restriction point determine everything?",
                   font=SERIF, color=CRIMSON, font_size=26)
        ask.next_to(dek, DOWN, buff=0.5)
        u = Line(ask.get_corner(DL) + DOWN * 0.1, ask.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)
        box = SurroundingRectangle(q1, buff=0.22).set_fill(SLATE, 0.07).set_stroke(SLATE, 1.2)

        self.play(FadeIn(box), FadeIn(q1), run_time=0.8)
        self.play(FadeIn(dek), run_time=0.7)
        self.play(FadeIn(ask), Create(u), run_time=0.9)
        self.wait(max(0.3, total - 2.4))


# ─────────────────────────────────────────────────────────────────────────────
# B05 — Naive dial model
# ─────────────────────────────────────────────────────────────────────────────
class B05_NaiveDial(Scene):
    def construct(self):
        total = DUR["B05"]
        title = SerifLabel("Naive model: commitment as a dial", accent=CRIMSON, size=26)
        title.to_edge(UP, buff=0.85)

        # Horizontal axis
        axis = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=2).shift(DOWN * 0.5)
        ax_label = Text("Growth Signal", font=SERIF, color=INK, font_size=22)
        ax_label.next_to(axis, DOWN, buff=0.2)
        low = Text("0", font=MONO, color=INK, font_size=20).next_to(axis.get_left(), DOWN, buff=0.1)
        high = Text("HIGH", font=MONO, color=INK, font_size=20).next_to(axis.get_right(), DOWN, buff=0.1)

        # Diagonal arrow representing proportional commitment
        diag = Arrow(axis.get_left() + UP * 0.05, axis.get_right() + UP * 2.5,
                     buff=0, color=CRIMSON, stroke_width=3)
        diag_label = Text("Commitment (proportional)", font=SERIF, color=CRIMSON, font_size=24)
        diag_label.next_to(diag.get_tip(), UP, buff=0.15)

        claim = Text("More signal, more division. Remove signal, commitment drops.", font=SERIF,
                     color=INK, font_size=22)
        claim.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(title), Create(axis), FadeIn(ax_label), FadeIn(low), FadeIn(high),
                  run_time=0.9)
        self.play(GrowArrow(diag), FadeIn(diag_label), run_time=0.9)
        self.play(FadeIn(claim), run_time=0.6)
        self.wait(max(0.3, total - 2.4))


# ─────────────────────────────────────────────────────────────────────────────
# B06 — Dial model fails
# ─────────────────────────────────────────────────────────────────────────────
class B06_DialFails(Scene):
    def construct(self):
        total = DUR["B06"]
        title = SerifLabel("Same withdrawal — opposite outcomes", accent=CRIMSON, size=26)
        title.to_edge(UP, buff=0.85)

        # Two columns
        col_a = VGroup(
            LabelChip("Cell A", accent=CRIMSON, size=22),
            Text("Signal removed", font=SERIF, color=INK, font_size=22),
            Text("Commitment drops", font=SERIF, color=INK, font_size=22),
            Text("-- Dial model: correct", font=SERIF, color=INK, font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        col_a.move_to(LEFT * 3.2 + DOWN * 0.4)

        col_b = VGroup(
            LabelChip("Cell B", accent=TEAL, size=22),
            Text("Signal removed", font=SERIF, color=INK, font_size=22),
            Text("Commitment stays", font=SERIF, color=TEAL, font_size=22, weight=BOLD),
            Text("?? Dial model: fails", font=SERIF, color=CRIMSON, font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        col_b.move_to(RIGHT * 2.8 + DOWN * 0.4)

        # Divider
        divider = Line(UP * 2.0, DOWN * 2.5, color=SLATE, stroke_width=1.5)

        # X mark over B prediction
        cross_line1 = Line(col_b[3].get_corner(UL), col_b[3].get_corner(DR),
                           color=CRIMSON, stroke_width=3)
        cross_line2 = Line(col_b[3].get_corner(UR), col_b[3].get_corner(DL),
                           color=CRIMSON, stroke_width=3)

        self.play(FadeIn(title), Create(divider), run_time=0.6)
        self.play(FadeIn(col_a), run_time=0.8)
        self.play(FadeIn(col_b[0]), FadeIn(col_b[1]), FadeIn(col_b[2]), run_time=0.8)
        self.play(FadeIn(col_b[3]), run_time=0.5)
        self.play(Create(cross_line1), Create(cross_line2), run_time=0.6)
        self.wait(max(0.3, total - 3.3))


# ─────────────────────────────────────────────────────────────────────────────
# B08 — Positive feedback loop
# ─────────────────────────────────────────────────────────────────────────────
class B08_FeedbackLoop(Scene):
    def construct(self):
        total = DUR["B08"]
        title = SerifLabel("Positive feedback: the switch, not the ramp", accent=TEAL, size=26)
        title.to_edge(UP, buff=0.75)

        # Four nodes in a loop
        import numpy as np
        cx, cy, r = 0.0, -0.6, 2.0
        angles = [90, 0, 270, 180]  # top, right, bottom, left
        positions = [np.array([cx + r * np.cos(np.radians(a)),
                               cy + r * np.sin(np.radians(a)), 0]) for a in angles]
        labels = ["Cyclin E", "CDK2 active", "Rb hyperP", "E2F free"]

        nodes = VGroup()
        node_boxes = []
        for pos, lbl in zip(positions, labels):
            box = RoundedRectangle(width=2.0, height=0.65, corner_radius=0.12)
            box.set_fill(TEAL, 0.18).set_stroke(TEAL, 1.8)
            txt = Text(lbl, font=DISPLAY, color=INK, font_size=20)
            txt.move_to(box)
            grp = VGroup(box, txt).move_to(pos)
            nodes.add(grp)
            node_boxes.append(grp)

        # Curved arrows between nodes (top->right->bottom->left->top)
        arrows = VGroup()
        for i in range(4):
            src = node_boxes[i]
            dst = node_boxes[(i + 1) % 4]
            arr = CurvedArrow(src.get_right() if i == 0 else
                              src.get_bottom() if i == 1 else
                              src.get_left() if i == 2 else
                              src.get_top(),
                              dst.get_top() if i == 0 else
                              dst.get_left() if i == 1 else
                              dst.get_bottom() if i == 2 else
                              dst.get_right(),
                              color=TEAL, stroke_width=2.5,
                              angle=-TAU / 8)
            arrows.add(arr)

        fb_chip = LabelChip("positive feedback", accent=TEAL, size=20)
        fb_chip.move_to(np.array([cx, cy, 0]))

        self.play(FadeIn(title), run_time=0.5)
        for n in node_boxes:
            self.play(FadeIn(n), run_time=0.35)
        for arr in arrows:
            self.play(Create(arr), run_time=0.4)
        self.play(FadeIn(fb_chip), run_time=0.5)
        self.wait(max(0.3, total - 3.5))


# ─────────────────────────────────────────────────────────────────────────────
# B10 — Ball pre-restriction: rolls back to G0
# ─────────────────────────────────────────────────────────────────────────────
class B10_BallPreRestriction(Scene):
    def construct(self):
        total = DUR["B10"]
        import numpy as np

        title = SerifLabel("Cell A: signal stops, ball rolls back", accent=CRIMSON, size=24)
        title.to_edge(UP, buff=0.75)

        # Energy landscape hill
        def hill_y(x):
            # Two wells connected by a hill
            # Left well center at x=-3, right well at x=3, hill at x=0
            return 0.8 * np.exp(-0.5 * ((x + 3) / 0.9) ** 2) * (-1) + \
                   1.8 * np.exp(-0.5 * (x / 1.0) ** 2) + \
                   0.8 * np.exp(-0.5 * ((x - 3) / 0.9) ** 2) * (-1)

        xs = np.linspace(-5.5, 5.5, 200)
        ys = np.array([hill_y(x) for x in xs])
        # Normalize so baseline is visible
        ys = ys - ys.min() + 0.2
        # Scale to frame
        ys = ys * 1.2

        points = [np.array([x * 1.0, y - 1.8, 0]) for x, y in zip(xs, ys)]
        curve = VMobject(color=INK, stroke_width=2.5)
        curve.set_points_smoothly(points)

        # Labels
        left_label = Text("G0", font=DISPLAY, color=CRIMSON, font_size=22)
        left_label.move_to(np.array([-3.0, -1.5, 0]))
        right_label = Text("S phase", font=DISPLAY, color=TEAL, font_size=22)
        right_label.move_to(np.array([3.0, -1.5, 0]))
        hill_label = Text("Restriction\nPoint", font=DISPLAY, color=INK, font_size=18)
        hill_label.move_to(np.array([0.0, 1.0, 0]))

        # Dashed vertical at hill
        hill_line = DashedLine(np.array([0.0, -1.6, 0]), np.array([0.0, 0.8, 0]),
                               color=SLATE, stroke_width=1.5, dash_length=0.15)

        # Ball starts in left well area (pre-restriction)
        ball = Circle(radius=0.22).set_fill(CRIMSON, 1).set_stroke(width=0)
        ball.move_to(np.array([-3.0, -0.85, 0]))

        # GF signal arrow
        gf_arrow = Arrow(np.array([-5.0, 0.5, 0]), np.array([-3.8, 0.0, 0]),
                         color=INK, stroke_width=2, buff=0.05)
        gf_label = Text("Growth signal", font=SERIF, color=INK, font_size=20)
        gf_label.next_to(gf_arrow, LEFT, buff=0.1)

        self.play(FadeIn(title), Create(curve), run_time=0.9)
        self.play(FadeIn(left_label), FadeIn(right_label), FadeIn(hill_label),
                  Create(hill_line), run_time=0.6)
        self.play(FadeIn(ball), run_time=0.4)
        self.play(FadeIn(gf_arrow), FadeIn(gf_label), run_time=0.5)

        # Ball pushed partway up hill
        self.play(ball.animate.shift(RIGHT * 1.5 + UP * 0.5), run_time=1.2)
        # Signal removed
        self.play(FadeOut(gf_arrow), FadeOut(gf_label), run_time=0.5)
        # Ball rolls back
        self.play(ball.animate.shift(LEFT * 1.5 + DOWN * 0.5), run_time=1.0)

        result = Text("Cyclin D falls. Rb hypophosphorylated. E2F captured. G0.", font=SERIF,
                      color=CRIMSON, font_size=20)
        result.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(result), run_time=0.6)
        self.wait(max(0.3, total - 5.7))


# ─────────────────────────────────────────────────────────────────────────────
# B11 — Ball post-restriction: stays in S-phase well
# ─────────────────────────────────────────────────────────────────────────────
class B11_BallPostRestriction(Scene):
    def construct(self):
        total = DUR["B11"]
        import numpy as np

        title = SerifLabel("Cell B: signal gone, ball stays committed", accent=TEAL, size=24)
        title.to_edge(UP, buff=0.75)

        # Same landscape
        def hill_y(x):
            return 0.8 * np.exp(-0.5 * ((x + 3) / 0.9) ** 2) * (-1) + \
                   1.8 * np.exp(-0.5 * (x / 1.0) ** 2) + \
                   0.8 * np.exp(-0.5 * ((x - 3) / 0.9) ** 2) * (-1)

        xs = np.linspace(-5.5, 5.5, 200)
        ys = np.array([hill_y(x) for x in xs])
        ys = ys - ys.min() + 0.2
        ys = ys * 1.2

        points = [np.array([x * 1.0, y - 1.8, 0]) for x, y in zip(xs, ys)]
        curve = VMobject(color=INK, stroke_width=2.5)
        curve.set_points_smoothly(points)

        left_label = Text("G0", font=DISPLAY, color=CRIMSON, font_size=22)
        left_label.move_to(np.array([-3.0, -1.5, 0]))
        right_label = Text("S phase", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        right_label.move_to(np.array([3.0, -1.5, 0]))
        hill_label = Text("Restriction\nPoint", font=DISPLAY, color=INK, font_size=18)
        hill_label.move_to(np.array([0.0, 1.0, 0]))
        hill_line = DashedLine(np.array([0.0, -1.6, 0]), np.array([0.0, 0.8, 0]),
                               color=SLATE, stroke_width=1.5, dash_length=0.15)

        # Ball starts in RIGHT well (post-restriction, committed)
        ball = Circle(radius=0.22).set_fill(TEAL, 1).set_stroke(width=0)
        ball.move_to(np.array([3.0, -0.85, 0]))

        # Strikethrough growth signal
        no_gf = Text("Growth signal: removed", font=SERIF, color=INK, font_size=20)
        no_gf.to_edge(UP, buff=2.0)
        strike = Line(no_gf.get_left() + LEFT * 0.1, no_gf.get_right() + RIGHT * 0.1,
                      color=CRIMSON, stroke_width=3)

        fb_running = SerifLabel("Feedback loop still running", accent=TEAL, size=22)
        fb_running.to_edge(DOWN, buff=0.9)
        result = Text("S phase proceeds on schedule.", font=SERIF, color=TEAL, font_size=20,
                      weight=BOLD)
        result.to_edge(DOWN, buff=0.45)

        self.play(FadeIn(title), Create(curve), run_time=0.8)
        self.play(FadeIn(left_label), FadeIn(right_label), FadeIn(hill_label),
                  Create(hill_line), FadeIn(ball), run_time=0.7)
        self.play(FadeIn(no_gf), run_time=0.4)
        self.play(Create(strike), run_time=0.5)
        # Ball does NOT move
        self.play(Wiggle(ball, scale_value=1.08), run_time=0.8)
        self.play(FadeIn(fb_running), FadeIn(result), run_time=0.7)
        self.wait(max(0.3, total - 3.9))


# ─────────────────────────────────────────────────────────────────────────────
# B12 — Two-cell comparison example (illustrative numbers)
# ─────────────────────────────────────────────────────────────────────────────
class B12_TwoCellsExample(Scene):
    def construct(self):
        total = DUR["B12"]

        title = Text("Same withdrawal. Opposite fates.", font=DISPLAY, color=INK,
                     font_size=28, weight=BOLD)
        title.to_edge(UP, buff=0.7)

        illus = Text("(numbers illustrative)", font=SERIF, color=SLATE, font_size=18)
        illus.next_to(title, RIGHT, buff=0.3)

        # Divider
        divider = Line(UP * 2.5, DOWN * 2.8, color=SLATE, stroke_width=1.5)

        # ── Cell A column ──
        chip_a = LabelChip("Cell A  pre-restriction", accent=CRIMSON, size=20)
        chip_a.move_to(LEFT * 3.5 + UP * 1.8)

        event = Text("t = 0: GF withdrawn", font=MONO, color=INK, font_size=19)
        event.move_to(LEFT * 3.5 + UP * 1.1)

        cd_row = VGroup(
            Text("Cyclin D half-life: 15 min", font=SERIF, color=INK, font_size=19),
        )
        cd_row.move_to(LEFT * 3.5 + UP * 0.4)

        gone_row = Text("Gone in 30 min", font=SERIF, color=CRIMSON, font_size=19)
        gone_row.move_to(LEFT * 3.5 + DOWN * 0.2)

        rb_row = Text("Rb hypophosphorylated", font=SERIF, color=INK, font_size=19)
        rb_row.move_to(LEFT * 3.5 + DOWN * 0.75)

        e2f_row = Text("E2F captured", font=SERIF, color=INK, font_size=19)
        e2f_row.move_to(LEFT * 3.5 + DOWN * 1.25)

        fate_a = LabelChip("G0", accent=CRIMSON, size=22)
        fate_a.move_to(LEFT * 3.5 + DOWN * 1.95)

        # ── Cell B column ──
        chip_b = LabelChip("Cell B  post-restriction", accent=TEAL, size=20)
        chip_b.move_to(RIGHT * 3.2 + UP * 1.8)

        event_b = Text("t = 0: GF withdrawn", font=MONO, color=INK, font_size=19)
        event_b.move_to(RIGHT * 3.2 + UP * 1.1)

        ce_row = Text("Cyclin E: E2F-driven, stays high", font=SERIF, color=TEAL, font_size=19)
        ce_row.move_to(RIGHT * 3.2 + UP * 0.4)

        cdk_row = Text("CDK2 still phosphorylating Rb", font=SERIF, color=TEAL, font_size=19)
        cdk_row.move_to(RIGHT * 3.2 + DOWN * 0.2)

        no_effect = Text("GF removal has no effect", font=SERIF, color=INK, font_size=19)
        no_effect.move_to(RIGHT * 3.2 + DOWN * 0.75)

        fb_row = Text("Feedback loop self-sustaining", font=SERIF, color=TEAL, font_size=19)
        fb_row.move_to(RIGHT * 3.2 + DOWN * 1.25)

        fate_b = LabelChip("S phase", accent=TEAL, size=22)
        fate_b.move_to(RIGHT * 3.2 + DOWN * 1.95)

        self.play(FadeIn(title), FadeIn(illus), Create(divider), run_time=0.7)
        self.play(FadeIn(chip_a), FadeIn(chip_b), run_time=0.5)
        self.play(FadeIn(event), FadeIn(event_b), run_time=0.5)
        self.play(FadeIn(cd_row), FadeIn(ce_row), run_time=0.6)
        self.play(FadeIn(gone_row), FadeIn(cdk_row), run_time=0.6)
        self.play(FadeIn(rb_row), FadeIn(no_effect), run_time=0.6)
        self.play(FadeIn(e2f_row), FadeIn(fb_row), run_time=0.6)
        self.play(FadeIn(fate_a), FadeIn(fate_b), run_time=0.7)
        self.wait(max(0.3, total - 5.3))


# ─────────────────────────────────────────────────────────────────────────────
# B13 — Endcard / RECAP
# ─────────────────────────────────────────────────────────────────────────────
class B13_Endcard(Scene):
    def construct(self):
        total = DUR["B13"]

        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)

        q_line = Text("Why does the same withdrawal stop one cell and not the other?",
                      font=SERIF, color=INK, font_size=24, slant=ITALIC)

        a_line = Text("The Rb/E2F switch is bistable.", font=DISPLAY, color=INK,
                      font_size=28, weight=BOLD)
        a_sub = Text("Once the feedback loop crosses threshold, the signal that triggered it is no longer needed.",
                     font=SERIF, color=INK, font_size=22)

        block = VGroup(q_line, a_line, a_sub).arrange(DOWN, buff=0.35)
        u = Line(a_line.get_corner(DL) + DOWN * 0.1, a_line.get_corner(DR) + DOWN * 0.1,
                 color=GOLD, stroke_width=2)

        eye.next_to(block, UP, buff=0.5)
        full = VGroup(eye, block, u).move_to(ORIGIN)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(q_line), run_time=0.7)
        self.play(FadeIn(a_line), Create(u), run_time=0.8)
        self.play(FadeIn(a_sub), run_time=0.7)
        self.wait(max(0.3, total - 2.7))
