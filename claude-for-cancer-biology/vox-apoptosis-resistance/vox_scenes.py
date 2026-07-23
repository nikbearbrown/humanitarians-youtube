"""vox_scenes.py — Why Cancer Cells Are Harder to Kill With the Drug That
Should Kill Them Best (vox-apoptosis-resistance, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat whose source is 'own'.
B02 is the only STILL (ai media slot) and has no scene here.

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-apoptosis-resistance

Color law:
  TEAL     = apoptotic signal present / death pathway active / circuit working
  CRIMSON  = sabotage point / resistance mechanism / selection pressure
  GOLD     = editor's pen highlight (once, B12 only)
  SLATE    = structural entity cards

EXCLUSIONS honored: no extrinsic pathway, no venetoclax, no necroptosis/
pyroptosis/ferroptosis, no p53 transcriptional detail (PUMA/NOXA absent),
no IAP biochemistry beyond XIAP naming.

Gate B convention: every zero-width stroke is also zero-opacity.
Single-method .animate only (Gate A mock).
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B01": 9.0, "B03": 12.0, "B04": 14.0, "B05": 11.0,
    "B06": 8.0, "B07": 13.0, "B08": 12.0, "B09": 13.0,
    "B10": 13.0, "B11": 13.0, "B12": 10.0, "B13": 11.0,
    "B14": 12.0, "B15": 11.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- builders

def _node(label, color=TEAL, w=1.6, h=0.5):
    """Circuit node: filled rounded rectangle + white DISPLAY label."""
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 1).set_stroke(width=0, opacity=0)
    t = Text(label, font=DISPLAY, color=WHITE, font_size=18, weight="MEDIUM")
    if t.width > w * 0.88:
        t.scale_to_fit_width(w * 0.88)
    t.move_to(r.get_center())
    return VGroup(r, t)


def _arrow(start, end, color=TEAL):
    a = Arrow(start, end, color=color, stroke_width=3,
              tip_length=0.18, buff=0.06)
    a.set_stroke(width=0, opacity=0)  # zero-width default, but we use stroke_width=3 above
    # Reset correctly: non-zero width arrow with explicit stroke set
    a.set_stroke(color=color, width=3, opacity=1)
    return a


def _blocker(label, color=CRIMSON, w=1.3, h=0.38):
    """Crimson sabotage block that snaps onto a circuit node."""
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 1).set_stroke(width=0, opacity=0)
    t = Text(label, font=DISPLAY, color=WHITE, font_size=15, weight="MEDIUM")
    if t.width > w * 0.88:
        t.scale_to_fit_width(w * 0.88)
    t.move_to(r.get_center())
    return VGroup(r, t)


def _build_circuit(x_start=-5.8, y=0.3, spacing=1.95):
    """Build the six-node intrinsic pathway circuit. Returns (nodes, arrows).
    Nodes: DAMAGE, p53, BH3, BALANCE, MOMP, CASPASES, DEATH
    Positions left to right across screen."""
    labels = ["DAMAGE", "p53", "BH3\nSIGNAL", "BCL-2\nBALANCE", "MOMP", "CASPASES", "DEATH"]
    positions = [np.array([x_start + i * spacing, y, 0]) for i in range(len(labels))]
    nodes = VGroup(*[_node(lbl).move_to(pos) for lbl, pos in zip(labels, positions)])
    arrows = VGroup()
    for i in range(len(positions) - 1):
        a = Arrow(positions[i] + RIGHT * 0.82, positions[i + 1] + LEFT * 0.82,
                  color=TEAL, stroke_width=3, tip_length=0.18, buff=0.0)
        a.set_stroke(color=TEAL, width=3, opacity=1)
        arrows.add(a)
    return nodes, arrows


# Node index constants
N_DAMAGE   = 0
N_P53      = 1
N_BH3      = 2
N_BALANCE  = 3
N_MOMP     = 4
N_CASPASES = 5
N_DEATH    = 6


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        t1 = Text("Harder to kill", font=DISPLAY, color=INK,
                  font_size=54, weight=BOLD)
        t2 = Text("with every treatment.", font=DISPLAY, color=INK,
                  font_size=54, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.16).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.16,
                 t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.75)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        setup = Text(
            "Chemotherapy inflicts enough DNA damage to kill normal cells.",
            font=DISPLAY, color=INK, font_size=28,
        )
        setup.move_to(UP * 1.5)
        if setup.width > 13.0:
            setup.scale_to_fit_width(13.0)
        question = Text(
            "Why does the death signal arrive but not execute?",
            font=DISPLAY, color=INK, font_size=36, weight=BOLD,
        )
        question.move_to(DOWN * 0.2)
        if question.width > 13.0:
            question.scale_to_fit_width(13.0)
        u = Line(question.get_corner(DL) + DOWN * 0.14,
                 question.get_corner(DR) + DOWN * 0.14,
                 color=TEAL, stroke_width=2.5)
        self.play(FadeIn(setup, shift=UP * 0.2), run_time=0.9)
        self.play(FadeIn(question), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 2.1))


class B04_IntactCircuit(Scene):
    def construct(self):
        total = DUR["B04"]
        nodes, arrows = _build_circuit(x_start=-5.8, y=0.5, spacing=1.95)
        label = LabelChip("INTRINSIC PATHWAY", accent=TEAL, size=22)
        label.move_to(DOWN * 2.2)
        self.play(FadeIn(nodes[0]), run_time=0.4)
        for i in range(len(arrows)):
            self.play(
                Create(arrows[i]),
                FadeIn(nodes[i + 1], shift=RIGHT * 0.3),
                run_time=0.55,
            )
        self.play(FadeIn(label, scale=0.9), run_time=0.6)
        self.wait(max(0.5, total - 0.4 - len(arrows) * 0.55 - 0.6))


class B05_SignalBlocked(Scene):
    def construct(self):
        total = DUR["B05"]
        nodes, arrows = _build_circuit(x_start=-5.8, y=0.5, spacing=1.95)
        # Show full circuit instantly, then block it
        self.play(FadeIn(nodes), FadeIn(arrows), run_time=0.9)
        # Crimson STOP block appears above BCL-2 balance node (index 3)
        stop = _blocker("BLOCKED", CRIMSON, w=1.6, h=0.55)
        stop.move_to(nodes[N_BALANCE].get_center() + UP * 0.55)
        self.play(FadeIn(stop, shift=DOWN * 0.3), run_time=0.7)
        chip = LabelChip("SIGNAL STOPPED", accent=CRIMSON, size=24)
        chip.move_to(DOWN * 2.3)
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(max(0.5, total - 2.2))


class B06_SectionCard(Scene):
    def construct(self):
        total = DUR["B06"]
        eye = Text("THE MECHANISM", font=DISPLAY, color=CRIMSON,
                   font_size=20, weight="MEDIUM")
        t = Text("Five sabotage points.", font=DISPLAY, color=INK,
                 font_size=56, weight=BOLD)
        sub = Text("Each one selected by a chemotherapy exposure.",
                   font=DISPLAY, color=INK, font_size=30)
        block = VGroup(t, sub).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        eye.next_to(block, UP, buff=0.7)
        # Five crimson tick marks grow in (adds shape motion for Gate A)
        ticks = VGroup(*[
            Rectangle(width=0.22, height=0.22)
            .set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
            .move_to(np.array([-2.2 + i * 1.1, -2.6, 0]))
            for i in range(5)
        ])
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), run_time=0.8)
        self.play(FadeIn(ticks, lag_ratio=0.18), run_time=0.8)
        self.wait(max(0.5, total - 2.1))


class B07_Sabotage1(Scene):
    """BCL-2 overexpression: first block snaps onto circuit."""
    def construct(self):
        total = DUR["B07"]
        nodes, arrows = _build_circuit(x_start=-5.8, y=0.6, spacing=1.95)
        self.play(FadeIn(nodes), FadeIn(arrows), run_time=0.8)
        # Block 1: BCL-2 HIGH at MOMP (index 4)
        blk = _blocker("BCL-2 HIGH", CRIMSON, w=1.55, h=0.42)
        blk.move_to(nodes[N_MOMP].get_center() + UP * 0.58)
        self.play(FadeIn(blk, scale=0.7), run_time=0.8)
        label = SerifLabel("BAX held · no pore · no death", CRIMSON, size=25)
        label.move_to(DOWN * 2.2)
        self.play(FadeIn(label), run_time=0.6)
        chip = LabelChip("SABOTAGE 1", accent=CRIMSON, size=20)
        chip.move_to(DOWN * 3.0)
        self.play(FadeIn(chip, scale=0.9), run_time=0.4)
        self.wait(max(0.5, total - 2.6))


class B08_Sabotage2(Scene):
    """BAX lost: second block. Circuit with two crimson blockers."""
    def construct(self):
        total = DUR["B08"]
        nodes, arrows = _build_circuit(x_start=-5.8, y=0.6, spacing=1.95)
        # Block 1 already in place (shows circuit now has two)
        blk1 = _blocker("BCL-2 HIGH", CRIMSON, w=1.55, h=0.42)
        blk1.move_to(nodes[N_MOMP].get_center() + UP * 0.58)
        self.play(FadeIn(nodes), FadeIn(arrows), FadeIn(blk1), run_time=0.8)
        # Block 2: BAX LOST at effector (MOMP + 1 position, show below MOMP)
        blk2 = _blocker("BAX LOST", CRIMSON, w=1.55, h=0.42)
        blk2.move_to(nodes[N_MOMP].get_center() + DOWN * 0.62)
        self.play(FadeIn(blk2, scale=0.7), run_time=0.8)
        label = SerifLabel("no effector protein · pore impossible", CRIMSON, size=24)
        label.move_to(DOWN * 2.2)
        self.play(FadeIn(label), run_time=0.6)
        chip = LabelChip("SABOTAGE 2", accent=CRIMSON, size=20)
        chip.move_to(DOWN * 3.0)
        self.play(FadeIn(chip, scale=0.9), run_time=0.4)
        self.wait(max(0.5, total - 2.6))


class B09_Sabotage3(Scene):
    """XIAP: third block at caspase node."""
    def construct(self):
        total = DUR["B09"]
        nodes, arrows = _build_circuit(x_start=-5.8, y=0.6, spacing=1.95)
        blk1 = _blocker("BCL-2 HIGH", CRIMSON, w=1.55, h=0.42)
        blk1.move_to(nodes[N_MOMP].get_center() + UP * 0.58)
        blk2 = _blocker("BAX LOST", CRIMSON, w=1.55, h=0.42)
        blk2.move_to(nodes[N_MOMP].get_center() + DOWN * 0.62)
        existing = VGroup(blk1, blk2)
        self.play(FadeIn(nodes), FadeIn(arrows), FadeIn(existing), run_time=0.8)
        # Block 3: XIAP at caspase node (index 5)
        blk3 = _blocker("XIAP", CRIMSON, w=1.55, h=0.42)
        blk3.move_to(nodes[N_CASPASES].get_center() + UP * 0.58)
        self.play(FadeIn(blk3, scale=0.7), run_time=0.8)
        label = SerifLabel("caspases blocked at execution stage", CRIMSON, size=24)
        label.move_to(DOWN * 2.2)
        self.play(FadeIn(label), run_time=0.6)
        chip = LabelChip("SABOTAGE 3", accent=CRIMSON, size=20)
        chip.move_to(DOWN * 3.0)
        self.play(FadeIn(chip, scale=0.9), run_time=0.4)
        self.wait(max(0.5, total - 2.6))


class B10_Sabotage4(Scene):
    """PI3K-AKT inactivates BAD: fourth block at BH3 sensor node."""
    def construct(self):
        total = DUR["B10"]
        nodes, arrows = _build_circuit(x_start=-5.8, y=0.6, spacing=1.95)
        blk1 = _blocker("BCL-2 HIGH", CRIMSON, w=1.55, h=0.42)
        blk1.move_to(nodes[N_MOMP].get_center() + UP * 0.58)
        blk2 = _blocker("BAX LOST", CRIMSON, w=1.55, h=0.42)
        blk2.move_to(nodes[N_MOMP].get_center() + DOWN * 0.62)
        blk3 = _blocker("XIAP", CRIMSON, w=1.55, h=0.42)
        blk3.move_to(nodes[N_CASPASES].get_center() + UP * 0.58)
        existing = VGroup(blk1, blk2, blk3)
        self.play(FadeIn(nodes), FadeIn(arrows), FadeIn(existing), run_time=0.8)
        # Block 4: AKT-BAD at BH3 signal node (index 2)
        blk4 = _blocker("AKT · BAD", CRIMSON, w=1.55, h=0.42)
        blk4.move_to(nodes[N_BH3].get_center() + UP * 0.58)
        self.play(FadeIn(blk4, scale=0.7), run_time=0.8)
        label = SerifLabel("BAD inactivated · less pressure on BCL-2", CRIMSON, size=24)
        label.move_to(DOWN * 2.2)
        self.play(FadeIn(label), run_time=0.6)
        chip = LabelChip("SABOTAGE 4", accent=CRIMSON, size=20)
        chip.move_to(DOWN * 3.0)
        self.play(FadeIn(chip, scale=0.9), run_time=0.4)
        self.wait(max(0.5, total - 2.6))


class B11_Sabotage5(Scene):
    """p53 mutation: fifth block at the sensor node. All five blocks present."""
    def construct(self):
        total = DUR["B11"]
        nodes, arrows = _build_circuit(x_start=-5.8, y=0.6, spacing=1.95)
        blk1 = _blocker("BCL-2 HIGH", CRIMSON, w=1.55, h=0.42)
        blk1.move_to(nodes[N_MOMP].get_center() + UP * 0.58)
        blk2 = _blocker("BAX LOST", CRIMSON, w=1.55, h=0.42)
        blk2.move_to(nodes[N_MOMP].get_center() + DOWN * 0.62)
        blk3 = _blocker("XIAP", CRIMSON, w=1.55, h=0.42)
        blk3.move_to(nodes[N_CASPASES].get_center() + UP * 0.58)
        blk4 = _blocker("AKT · BAD", CRIMSON, w=1.55, h=0.42)
        blk4.move_to(nodes[N_BH3].get_center() + UP * 0.58)
        existing = VGroup(blk1, blk2, blk3, blk4)
        self.play(FadeIn(nodes), FadeIn(arrows), FadeIn(existing), run_time=0.8)
        # Block 5: p53 MUT at p53 sensor (index 1)
        blk5 = _blocker("p53 MUT", CRIMSON, w=1.55, h=0.42)
        blk5.move_to(nodes[N_P53].get_center() + UP * 0.58)
        self.play(FadeIn(blk5, scale=0.7), run_time=0.9)
        label = SerifLabel("damage sensor fires · message never arrives", CRIMSON, size=24)
        label.move_to(DOWN * 2.2)
        self.play(FadeIn(label), run_time=0.6)
        chip = LabelChip("SABOTAGE 5", accent=CRIMSON, size=20)
        chip.move_to(DOWN * 3.0)
        self.play(FadeIn(chip, scale=0.9), run_time=0.4)
        self.wait(max(0.5, total - 2.7))


class B12_FiveBlocksStatic(Scene):
    """All five blocks. GOLD signal arrow attempts to cross, stops at first block."""
    def construct(self):
        total = DUR["B12"]
        nodes, arrows = _build_circuit(x_start=-5.8, y=0.6, spacing=1.95)
        blk1 = _blocker("BCL-2 HIGH", CRIMSON, w=1.55, h=0.42)
        blk1.move_to(nodes[N_MOMP].get_center() + UP * 0.58)
        blk2 = _blocker("BAX LOST", CRIMSON, w=1.55, h=0.42)
        blk2.move_to(nodes[N_MOMP].get_center() + DOWN * 0.62)
        blk3 = _blocker("XIAP", CRIMSON, w=1.55, h=0.42)
        blk3.move_to(nodes[N_CASPASES].get_center() + UP * 0.58)
        blk4 = _blocker("AKT · BAD", CRIMSON, w=1.55, h=0.42)
        blk4.move_to(nodes[N_BH3].get_center() + UP * 0.58)
        blk5 = _blocker("p53 MUT", CRIMSON, w=1.55, h=0.42)
        blk5.move_to(nodes[N_P53].get_center() + UP * 0.58)
        all_blocks = VGroup(blk1, blk2, blk3, blk4, blk5)
        self.play(FadeIn(nodes), FadeIn(arrows), FadeIn(all_blocks), run_time=0.8)
        # GOLD signal arrow starts at DAMAGE and tries to move right
        sig_start = nodes[N_DAMAGE].get_center() + RIGHT * 0.85
        sig_stop = nodes[N_P53].get_center() + LEFT * 0.85
        sig_arrow = Arrow(sig_start, sig_stop, color=GOLD,
                          stroke_width=4, tip_length=0.22, buff=0.0)
        sig_arrow.set_stroke(color=GOLD, width=4, opacity=1)
        self.play(Create(sig_arrow), run_time=0.9)
        chip = LabelChip("SIGNAL PRESENT · CANNOT EXECUTE", accent=CRIMSON, size=22)
        chip.move_to(DOWN * 2.3)
        self.play(FadeIn(chip), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B13_SelectionStep1(Scene):
    """Clonal selection staircase, step 1: BCL-2 HIGH selected. Illustrative."""
    def construct(self):
        total = DUR["B13"]
        # Many cells as teal dots, most disappear, one BCL-2-high survives
        dot_positions = [
            np.array([-4.5 + (i % 8) * 0.55, 1.5 - (i // 8) * 0.55, 0])
            for i in range(32)
        ]
        dots = VGroup(*[Dot(radius=0.16).set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
                        .move_to(pos) for pos in dot_positions])
        self.play(FadeIn(dots, lag_ratio=0.03), run_time=0.8)
        # Exposure 1 arrow
        exp_label = LabelChip("EXPOSURE 1", accent=CRIMSON, size=22)
        exp_label.move_to(RIGHT * 3.5 + UP * 1.2)
        self.play(FadeIn(exp_label, shift=LEFT * 0.3), run_time=0.5)
        # Most dots fade (selection)
        dying_dots = VGroup(*[dots[i] for i in range(31)])
        self.play(FadeOut(dying_dots, scale=0.4), run_time=1.2)
        # Survivor grows large, TEAL, gets label
        survivor = dots[31].copy()
        survivor.set_fill(TEAL, 1)
        survivor.move_to(ORIGIN + DOWN * 0.3)
        self.play(survivor.animate.scale(2.5), run_time=0.8)
        chip = LabelChip("BCL-2 HIGH · SELECTED", accent=TEAL, size=24)
        chip.next_to(survivor, RIGHT, buff=0.35)
        note = SerifLabel("illustrative", INK, size=20)
        note.move_to(DOWN * 2.6)
        self.play(FadeIn(chip), run_time=0.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(max(0.5, total - 4.2))


class B14_SelectionSteps23(Scene):
    """Selection staircase steps 2 and 3: BAX LOST then XIAP UP. Illustrative."""
    def construct(self):
        total = DUR["B14"]
        # Staircase: three labeled steps going down-right
        step_x = [-3.8, -0.4, 3.0]
        step_y = [1.2, 0.0, -1.2]
        step_labels = ["BCL-2 HIGH", "BAX LOST", "XIAP UP"]
        step_colors = [TEAL, CRIMSON, CRIMSON]
        step_sizes = [0.38, 0.28, 0.22]   # shrinking survivor clone

        for i, (sx, sy, lbl, col, sz) in enumerate(
                zip(step_x, step_y, step_labels, step_colors, step_sizes)):
            dot = Dot(radius=sz).set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
            dot.move_to(np.array([sx, sy, 0]))
            chip = LabelChip(lbl, accent=col, size=20)
            chip.next_to(dot, RIGHT, buff=0.25)
            exp_chip = Text(f"Exposure {i + 1}", font=DISPLAY, color=INK,
                            font_size=18)
            exp_chip.move_to(np.array([sx, sy + 0.62, 0]))
            self.play(FadeIn(dot, scale=0.7), FadeIn(chip), FadeIn(exp_chip),
                      run_time=0.7)
            if i < 2:
                # Arrow downward to next step
                arr = Arrow(np.array([sx + 0.3, sy - sz - 0.1, 0]),
                            np.array([step_x[i + 1] - 0.15, step_y[i + 1] + step_sizes[i + 1] + 0.1, 0]),
                            color=CRIMSON, stroke_width=2.5,
                            tip_length=0.16, buff=0.0)
                arr.set_stroke(color=CRIMSON, width=2.5, opacity=1)
                pressure = Text("selection pressure", font=DISPLAY,
                                color=CRIMSON, font_size=14)
                pressure.next_to(arr, LEFT, buff=0.1)
                self.play(Create(arr), FadeIn(pressure), run_time=0.6)

        note = SerifLabel("illustrative · each exposure built the next layer", INK, size=22)
        note.move_to(DOWN * 3.2)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(max(0.5, total - 4.5))


class B15_Recap(Scene):
    def construct(self):
        total = DUR["B15"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                   font_size=22, weight="MEDIUM")
        q = Text("The death signal arrives. It always did.", font=DISPLAY,
                 color=INK, font_size=38, weight=BOLD)
        a = Text("The cancer built a five-layer wall against it.",
                 font=DISPLAY, color=INK, font_size=38, weight=BOLD)
        block = VGroup(q, a).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        u = Line(a.get_corner(DL) + DOWN * 0.14,
                 a.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.75)
        if q.width > 13.5:
            q.scale_to_fit_width(13.5)
        if a.width > 13.5:
            a.scale_to_fit_width(13.5)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(q), run_time=0.9)
        self.play(FadeIn(a), Create(u), run_time=1.0)
        self.wait(max(0.5, total - 2.4))
