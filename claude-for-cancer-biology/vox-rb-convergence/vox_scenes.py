"""vox_scenes.py — Why the Rb Gate Has Six Different Keys — and Losing Any One Opens It
(vox-rb-convergence, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat.
B02 and B12 are STILL·ai slots — no scenes here.

Color law: TEAL #1F6F5C = gate held / brake applied / cell in check (the good state);
CRIMSON #BF3339 = gate forced open / lost brake / S-phase (the bad state).
GOLD #F5D061 = editor's-pen highlight fill only — used ONCE (B14, never as text color).
Two accents max, never swapped mid-film.

Gate B convention: every zero-width stroke is also zero-opacity.

Manim move: accumulate (B08, B10, B13 — the key narrative beats).
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

# ── Duration table (word-count estimates; updated by audio lock) ──────────────
DUR = {
    "B01": 11.0, "B03": 13.0, "B04": 13.0, "B05": 14.0, "B06": 13.0,
    "B07": 13.0, "B08": 16.0, "B09": 13.0, "B10": 15.0, "B11": 14.0,
    "B13": 15.0, "B14": 13.0, "B15": 14.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ── Shared helpers ─────────────────────────────────────────────────────────────

def _chip(text, accent=TEAL, size=24):
    return LabelChip(text, accent=accent, size=size)


def _rect(w, h, fill_color, fill_opacity=1.0, stroke_color=None, stroke_w=0):
    r = Rectangle(width=w, height=h)
    sc = stroke_color if stroke_color else fill_color
    r.set_fill(fill_color, fill_opacity)
    if stroke_w > 0:
        r.set_stroke(sc, stroke_w)
    else:
        r.set_stroke(width=0, opacity=0)
    return r


def _junction_box(center, label_text, accent=CRIMSON):
    """A bordered rectangle representing the CDK4/6 -> Rb junction."""
    box = _rect(3.2, 1.1, accent, 0.12, accent, 2.5)
    box.move_to(center)
    lbl = SerifLabel(label_text, accent, size=22)
    lbl.move_to(center)
    return VGroup(box, lbl)


def _cable(start, end, color=CRIMSON, stroke_w=5):
    return Line(start, end, color=color, stroke_width=stroke_w)


def _node_chip(text, accent=CRIMSON, size=20):
    return LabelChip(text, accent=accent, size=size)


# ── Scenes ─────────────────────────────────────────────────────────────────────

class B01_Title(Scene):
    """Title card — eyebrow CANCER BIOLOGY in TEAL, title in INK."""
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Why the Rb gate has six different keys —", font=DISPLAY,
                  color=INK, font_size=38, weight=BOLD)
        t2 = Text("and losing any one opens it", font=DISPLAY,
                  color=INK, font_size=38, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.65)
        sub = Text("the convergence problem", font=SERIF, color=INK,
                   font_size=26)
        sub.next_to(block, DOWN, buff=0.45)
        self.play(FadeIn(eye, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.6))


class B03_Question(Scene):
    """Question card — the film's question on screen."""
    def construct(self):
        total = DUR["B03"]
        lines = [
            "BRAF inhibition should shut down",
            "the proliferative signal in a",
            "BRAF-mutant melanoma. Here BRAF",
            "is blocked, yet the cancer keeps",
            "dividing. Why?",
        ]
        line_mobs = VGroup(*[
            Text(l, font=SERIF, color=INK, font_size=38)
            for l in lines
        ]).arrange(DOWN, buff=0.2).move_to(UP * 0.1)
        u = Line(
            line_mobs[-1].get_corner(DL) + DOWN * 0.12,
            line_mobs[-1].get_corner(DR) + DOWN * 0.12,
            color=CRIMSON, stroke_width=2,
        )
        self.play(FadeIn(line_mobs, shift=UP * 0.15), run_time=1.0)
        self.play(Create(u), run_time=0.6)
        self.wait(max(0.5, total - 1.6))


class B04_SectionGate(Scene):
    """Section card — The Gate."""
    def construct(self):
        total = DUR["B04"]
        t = Text("The Gate", font=DISPLAY, color=INK,
                 font_size=64, weight=BOLD)
        s = Text("one switch, many inputs", font=SERIF, color=INK, font_size=28)
        s.next_to(t, DOWN, buff=0.4)
        u = Line(s.get_corner(DL) + DOWN * 0.1, s.get_corner(DR) + DOWN * 0.1,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(t, scale=0.95), run_time=0.7)
        self.play(FadeIn(s), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.4))


class B05_RbGate(Scene):
    """Rb grips E2F — gate closed in healthy cell. Teal throughout."""
    def construct(self):
        total = DUR["B05"]
        # Gate posts
        gate_h = 2.8
        cx = 0.0
        lpost = Line([cx - 0.7, -gate_h / 2, 0], [cx - 0.7, gate_h / 2, 0],
                     color=INK, stroke_width=5)
        rpost = Line([cx + 0.7, -gate_h / 2, 0], [cx + 0.7, gate_h / 2, 0],
                     color=INK, stroke_width=5)
        lintel = Line([cx - 0.9, gate_h / 2, 0], [cx + 0.9, gate_h / 2, 0],
                      color=INK, stroke_width=5)
        gate_group = VGroup(lpost, rpost, lintel).shift(DOWN * 0.1)

        # Labels
        g1_lbl = SerifLabel("G1", TEAL, size=30).move_to(LEFT * 3.8 + DOWN * 0.1)
        sphase_lbl = SerifLabel("S phase", INK, size=30).move_to(RIGHT * 3.8 + DOWN * 0.1)
        # barrier indicator
        barrier = _rect(0.22, 2.2, INK, 0.85).move_to([cx, -0.1, 0])

        # Rb and E2F mobjects
        rb_box = _rect(1.6, 0.78, TEAL, 0.25, TEAL, 2.5)
        rb_box.move_to(LEFT * 2.2 + DOWN * 0.1)
        rb_lbl = Text("Rb", font=SERIF, color=INK, font_size=30, weight=BOLD)
        rb_lbl.move_to(rb_box.get_center())
        rb_group = VGroup(rb_box, rb_lbl)

        e2f_circ = Circle(radius=0.48).set_fill(TEAL, 0.25).set_stroke(TEAL, 2.5)
        e2f_circ.move_to(RIGHT * 2.2 + DOWN * 0.1)
        e2f_lbl = Text("E2F", font=SERIF, color=INK, font_size=24, weight=BOLD)
        e2f_lbl.move_to(e2f_circ.get_center())
        e2f_group = VGroup(e2f_circ, e2f_lbl)

        # Grip arrow (Rb holds E2F)
        grip = Arrow(rb_box.get_right(), e2f_circ.get_left(),
                     color=TEAL, stroke_width=3, tip_length=0.18, buff=0.08)

        rb_label_serif = SerifLabel("active Rb", TEAL, size=20)
        rb_label_serif.next_to(rb_box, DOWN, buff=0.22)
        e2f_label_serif = SerifLabel("E2F — held", TEAL, size=20)
        e2f_label_serif.next_to(e2f_circ, DOWN, buff=0.22)

        self.play(Create(gate_group), run_time=0.8)
        self.play(FadeIn(g1_lbl), FadeIn(sphase_lbl), FadeIn(barrier), run_time=0.6)
        self.play(FadeIn(rb_group, shift=RIGHT * 0.3), run_time=0.6)
        self.play(Create(grip), FadeIn(e2f_group, shift=LEFT * 0.3), run_time=0.7)
        self.play(FadeIn(rb_label_serif), FadeIn(e2f_label_serif), run_time=0.5)
        self.wait(max(0.5, total - 3.2))


class B06_NormalSignal(Scene):
    """Normal conditional opening: growth signal -> cyclin D-CDK4/6 -> Rb released -> E2F free."""
    def construct(self):
        total = DUR["B06"]
        # Step 1: growth signal chip at top
        sig_chip = _chip("growth signal", TEAL, 24)
        sig_chip.move_to(UP * 3.0 + LEFT * 3.5)

        # Step 2: cyclin D-CDK4/6 chip
        cdk_chip = _chip("cyclin D-CDK4/6", TEAL, 22)
        cdk_chip.move_to(UP * 1.0 + LEFT * 3.5)

        arr1 = Arrow(sig_chip.get_bottom(), cdk_chip.get_top(),
                     color=TEAL, stroke_width=3, tip_length=0.2, buff=0.1)

        # Step 3: Rb (phosphorylated) chip
        rb_chip = _chip("Rb-P", TEAL, 22)
        rb_chip.move_to(UP * 1.0)

        arr2 = Arrow(cdk_chip.get_right(), rb_chip.get_left(),
                     color=TEAL, stroke_width=3, tip_length=0.2, buff=0.1)

        phos_dot = Dot(radius=0.14, color=GOLD)
        phos_dot.next_to(rb_chip, UR, buff=-0.05)

        # Step 4: E2F freed chip
        e2f_chip = _chip("E2F", TEAL, 22)
        e2f_chip.move_to(UP * 1.0 + RIGHT * 3.5)

        arr3 = Arrow(rb_chip.get_right(), e2f_chip.get_left(),
                     color=TEAL, stroke_width=3, tip_length=0.2, buff=0.1)

        # Step 5: S phase endpoint
        sphase_box = _rect(2.2, 0.7, TEAL, 0.15, TEAL, 2)
        sphase_box.move_to(DOWN * 0.9 + RIGHT * 3.5)
        sphase_lbl = SerifLabel("S phase", TEAL, size=24).move_to(sphase_box.get_center())

        arr4 = Arrow(e2f_chip.get_bottom(), sphase_box.get_top(),
                     color=TEAL, stroke_width=3, tip_length=0.2, buff=0.1)

        note = SerifLabel("conditional — signal required", TEAL, size=20)
        note.move_to(DOWN * 2.5 + LEFT * 2.5)

        self.play(FadeIn(sig_chip, shift=DOWN * 0.3), run_time=0.5)
        self.play(Create(arr1), FadeIn(cdk_chip, shift=DOWN * 0.3), run_time=0.6)
        self.play(Create(arr2), FadeIn(rb_chip), FadeIn(phos_dot), run_time=0.6)
        self.play(Create(arr3), FadeIn(e2f_chip, shift=LEFT * 0.3), run_time=0.6)
        self.play(Create(arr4), FadeIn(sphase_box), FadeIn(sphase_lbl), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 3.4))


class B07_SectionSixKeys(Scene):
    """Section card — Six Keys."""
    def construct(self):
        total = DUR["B07"]
        t = Text("Six Keys", font=DISPLAY, color=INK,
                 font_size=72, weight=BOLD)
        s = Text("different lesions, one gate", font=SERIF, color=INK, font_size=28)
        s.next_to(t, DOWN, buff=0.4)
        u = Line(s.get_corner(DL) + DOWN * 0.1, s.get_corner(DR) + DOWN * 0.1,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t, scale=0.95), run_time=0.7)
        self.play(FadeIn(s), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.4))


class B08_SixInputs(Scene):
    """Six crimson lesions accumulate one at a time toward a single E2F-free endpoint."""
    def construct(self):
        total = DUR["B08"]
        lesions = [
            "Rb loss",
            "p16 loss",
            "Cyclin D amplified",
            "CDK4/6 amplified",
            "CDK4 activating mutation",
            "Hyperactive upstream signaling",
        ]
        # Endpoint chip on right
        endpoint = _chip("E2F free", CRIMSON, 26)
        endpoint.move_to(RIGHT * 4.2)

        # Layout: 6 chips stacked on left, arrows pointing right to endpoint
        n = len(lesions)
        ys = [2.4 - i * 0.95 for i in range(n)]
        x_chip = -4.2

        chips = []
        arrows = []
        for i, (label, y) in enumerate(zip(lesions, ys)):
            c = _chip(label, CRIMSON, 20)
            c.move_to([x_chip, y, 0])
            chips.append(c)
            a = Arrow(c.get_right(), endpoint.get_left(),
                      color=CRIMSON, stroke_width=2.5, tip_length=0.16,
                      buff=0.1, max_tip_length_to_length_ratio=0.25)
            arrows.append(a)

        # Animate accumulate
        self.play(FadeIn(endpoint, scale=0.9), run_time=0.5)
        dt = max(0.3, (total - 2.5) / n)
        for c, a in zip(chips, arrows):
            self.play(FadeIn(c, shift=RIGHT * 0.3), Create(a), run_time=dt)
        self.wait(max(0.5, 1.0))


class B09_SectionMelanoma(Scene):
    """Section card — Three Inputs, One Melanoma."""
    def construct(self):
        total = DUR["B09"]
        t = Text("Three Inputs, One Melanoma", font=DISPLAY, color=INK,
                 font_size=46, weight=BOLD)
        s = Text("BRAF V600E — the convergence case", font=SERIF, color=INK, font_size=26)
        t.move_to(UP * 0.3)
        s.next_to(t, DOWN, buff=0.4)
        u = Line(s.get_corner(DL) + DOWN * 0.1, s.get_corner(DR) + DOWN * 0.1,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t, scale=0.95), run_time=0.7)
        self.play(FadeIn(s), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.4))


class B10_ThreeInputs(Scene):
    """Three cables accumulate into the CDK4/6 junction box. Accumulate motion."""
    def construct(self):
        total = DUR["B10"]
        # Junction box at center-right
        jbox_center = RIGHT * 2.6
        jbox = _junction_box(jbox_center, "CDK4/6  Rb", CRIMSON)

        # S phase endpoint at far right
        ep_center = RIGHT * 5.8
        ep_box = _rect(2.0, 0.7, CRIMSON, 0.15, CRIMSON, 2)
        ep_box.move_to(ep_center)
        ep_lbl = SerifLabel("E2F free / S phase", CRIMSON, size=20)
        ep_lbl.move_to(ep_center)
        ep_group = VGroup(ep_box, ep_lbl)
        ep_arr = Arrow(jbox_center + RIGHT * 1.65, ep_center + LEFT * 1.1,
                       color=CRIMSON, stroke_width=3, tip_length=0.18, buff=0.05)

        # Cable layouts — three input chains from left
        # Cable 1: BRAF V600E -> MAPK -> cyclin D1 (y = +1.8)
        c1_y = 1.8
        c1_nodes = [
            (_chip("BRAF V600E", CRIMSON, 19), LEFT * 5.8 + UP * c1_y),
            (_chip("MAPK", CRIMSON, 19), LEFT * 3.6 + UP * c1_y),
            (_chip("cyclin D1", CRIMSON, 19), LEFT * 1.4 + UP * c1_y),
        ]

        # Cable 2: p16 loss -> CDK4/6 uninhibited (y = 0.0)
        c2_y = 0.0
        c2_nodes = [
            (_chip("p16 loss", CRIMSON, 19), LEFT * 5.0 + UP * c2_y),
            (_chip("CDK4/6 uninhibited", CRIMSON, 19), LEFT * 2.4 + UP * c2_y),
        ]

        # Cable 3: PTEN loss -> AKT -> cyclin D1 stable (y = -1.8)
        c3_y = -1.8
        c3_nodes = [
            (_chip("PTEN loss", CRIMSON, 19), LEFT * 5.8 + UP * c3_y),
            (_chip("AKT", CRIMSON, 19), LEFT * 3.6 + UP * c3_y),
            (_chip("cyclin D1 stable", CRIMSON, 19), LEFT * 1.4 + UP * c3_y),
        ]

        def _place_nodes(node_spec):
            result = []
            for chip, pos in node_spec:
                chip.move_to(pos)
                result.append(chip)
            return result

        def _chain_arrows(chips, end_point=None, end_color=CRIMSON):
            arrs = []
            for i in range(len(chips) - 1):
                a = Arrow(chips[i].get_right(), chips[i + 1].get_left(),
                          color=CRIMSON, stroke_width=3, tip_length=0.16, buff=0.08,
                          max_tip_length_to_length_ratio=0.3)
                arrs.append(a)
            if end_point is not None:
                a = Arrow(chips[-1].get_right(), end_point,
                          color=CRIMSON, stroke_width=3, tip_length=0.16, buff=0.08,
                          max_tip_length_to_length_ratio=0.3)
                arrs.append(a)
            return arrs

        c1_chips = _place_nodes(c1_nodes)
        c2_chips = _place_nodes(c2_nodes)
        c3_chips = _place_nodes(c3_nodes)

        jbox_left = jbox_center + LEFT * 1.65
        c1_arrs = _chain_arrows(c1_chips, jbox_left)
        c2_arrs = _chain_arrows(c2_chips, jbox_left)
        c3_arrs = _chain_arrows(c3_chips, jbox_left)

        # Reveal junction box and endpoint first
        self.play(FadeIn(jbox, scale=0.92), run_time=0.6)
        self.play(FadeIn(ep_group, shift=LEFT * 0.2), run_time=0.4)

        # Cable 1 accumulates
        dt = max(0.35, (total - 4.0) / 3.0)
        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.2) for c in c1_chips], lag_ratio=0.3),
            LaggedStart(*[Create(a) for a in c1_arrs], lag_ratio=0.3),
            run_time=dt,
        )
        # Cable 2 accumulates
        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.2) for c in c2_chips], lag_ratio=0.4),
            LaggedStart(*[Create(a) for a in c2_arrs], lag_ratio=0.4),
            run_time=dt,
        )
        # Cable 3 accumulates
        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.2) for c in c3_chips], lag_ratio=0.3),
            LaggedStart(*[Create(a) for a in c3_arrs], lag_ratio=0.3),
            run_time=dt,
        )
        # Final arrow from junction to endpoint
        self.play(Create(ep_arr), run_time=0.5)
        self.wait(max(0.5, 0.5))


class B11_BrafBlock(Scene):
    """BRAFi blocks cable 1 — cable goes gray; cables 2 and 3 stay crimson; junction lit."""
    def construct(self):
        total = DUR["B11"]
        # Rebuild simplified end state: 3 cable labels + junction + endpoint
        jbox_center = RIGHT * 2.0
        jbox = _junction_box(jbox_center, "CDK4/6  Rb", CRIMSON)

        ep_center = RIGHT * 5.4
        ep_box = _rect(2.2, 0.65, CRIMSON, 0.15, CRIMSON, 2)
        ep_box.move_to(ep_center)
        ep_lbl = SerifLabel("E2F free / S phase", CRIMSON, size=20)
        ep_lbl.move_to(ep_center)
        ep_group = VGroup(ep_box, ep_lbl)
        ep_arr = Arrow(jbox_center + RIGHT * 1.65, ep_center + LEFT * 1.15,
                       color=CRIMSON, stroke_width=3, tip_length=0.18, buff=0.05)

        GRAY = "#C9C2B4"

        # Three cable summary chips (simplified to single node per cable for clarity)
        c1 = _chip("BRAF -> MAPK -> cyclin D1", CRIMSON, 20)
        c1.move_to(LEFT * 3.8 + UP * 1.8)
        c2 = _chip("p16 loss -> CDK4/6 uninhibited", CRIMSON, 20)
        c2.move_to(LEFT * 3.5 + UP * 0.0)
        c3 = _chip("PTEN -> AKT -> cyclin D1 stable", CRIMSON, 20)
        c3.move_to(LEFT * 3.8 + DOWN * 1.8)

        jbox_left = jbox_center + LEFT * 1.65
        a1 = Arrow(c1.get_right(), jbox_left, color=CRIMSON, stroke_width=3,
                   tip_length=0.16, buff=0.08, max_tip_length_to_length_ratio=0.3)
        a2 = Arrow(c2.get_right(), jbox_left, color=CRIMSON, stroke_width=3,
                   tip_length=0.16, buff=0.08, max_tip_length_to_length_ratio=0.3)
        a3 = Arrow(c3.get_right(), jbox_left, color=CRIMSON, stroke_width=3,
                   tip_length=0.16, buff=0.08, max_tip_length_to_length_ratio=0.3)

        self.play(
            FadeIn(jbox), FadeIn(ep_group), FadeIn(ep_arr),
            FadeIn(c1), FadeIn(c2), FadeIn(c3),
            FadeIn(a1), FadeIn(a2), FadeIn(a3),
            run_time=1.0,
        )

        # BRAFi block mark
        brafi_lbl = SerifLabel("BRAFi", GRAY, size=22)
        brafi_lbl.move_to(c1.get_center() + UP * 0.55)
        block_line = Line(c1.get_left() + LEFT * 0.05, c1.get_right() + RIGHT * 0.05,
                          color=GRAY, stroke_width=5)
        block_line._qc_intentional = True  # deliberate strike-through: exempt Gate B

        self.play(FadeIn(brafi_lbl, shift=DOWN * 0.2), run_time=0.5)
        self.play(Create(block_line), run_time=0.5)

        # Cable 1 fades to gray — set_fill sets fill opacity
        c1_gray = _chip("BRAF -> MAPK -> cyclin D1", GRAY, 20)
        c1_gray.move_to(c1.get_center())
        a1_gray = Arrow(c1_gray.get_right(), jbox_left, color=GRAY, stroke_width=3,
                        tip_length=0.16, buff=0.08, max_tip_length_to_length_ratio=0.3)
        self.play(
            ReplacementTransform(c1, c1_gray),
            ReplacementTransform(a1, a1_gray),
            run_time=0.7,
        )

        # "gate stays open" label below junction
        open_lbl = SerifLabel("gate stays open", CRIMSON, size=24)
        open_lbl.next_to(jbox, DOWN, buff=0.35)
        self.play(FadeIn(open_lbl, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.3))


class B13_CdkBlock(Scene):
    """CDK4/6i blocks the junction — gate restored, S phase arrested. Teal resolution."""
    def construct(self):
        total = DUR["B13"]
        GRAY = "#C9C2B4"

        # Start state from B11: cable 1 gray, cables 2+3 crimson, junction crimson, endpoint lit
        jbox_center = RIGHT * 2.0
        jbox = _junction_box(jbox_center, "CDK4/6  Rb", CRIMSON)

        ep_center = RIGHT * 5.4
        ep_box = _rect(2.2, 0.65, CRIMSON, 0.15, CRIMSON, 2)
        ep_box.move_to(ep_center)
        ep_lbl = SerifLabel("E2F free / S phase", CRIMSON, size=20)
        ep_lbl.move_to(ep_center)
        ep_group = VGroup(ep_box, ep_lbl)
        ep_arr = Arrow(jbox_center + RIGHT * 1.65, ep_center + LEFT * 1.15,
                       color=CRIMSON, stroke_width=3, tip_length=0.18, buff=0.05)

        c1 = _chip("BRAF -> MAPK -> cyclin D1", GRAY, 20)
        c1.move_to(LEFT * 3.8 + UP * 1.8)
        c2 = _chip("p16 loss -> CDK4/6 uninhibited", CRIMSON, 20)
        c2.move_to(LEFT * 3.5 + UP * 0.0)
        c3 = _chip("PTEN -> AKT -> cyclin D1 stable", CRIMSON, 20)
        c3.move_to(LEFT * 3.8 + DOWN * 1.8)

        jbox_left = jbox_center + LEFT * 1.65
        a1 = Arrow(c1.get_right(), jbox_left, color=GRAY, stroke_width=3,
                   tip_length=0.16, buff=0.08, max_tip_length_to_length_ratio=0.3)
        a2 = Arrow(c2.get_right(), jbox_left, color=CRIMSON, stroke_width=3,
                   tip_length=0.16, buff=0.08, max_tip_length_to_length_ratio=0.3)
        a3 = Arrow(c3.get_right(), jbox_left, color=CRIMSON, stroke_width=3,
                   tip_length=0.16, buff=0.08, max_tip_length_to_length_ratio=0.3)

        self.play(
            FadeIn(jbox), FadeIn(ep_group), FadeIn(ep_arr),
            FadeIn(c1), FadeIn(c2), FadeIn(c3),
            FadeIn(a1), FadeIn(a2), FadeIn(a3),
            run_time=1.0,
        )

        # CDK4/6i block label at junction
        cdki_lbl = SerifLabel("CDK4/6i", TEAL, size=24)
        cdki_lbl.next_to(jbox, UP, buff=0.3)
        self.play(FadeIn(cdki_lbl, shift=DOWN * 0.2), run_time=0.6)

        # Cables 2 and 3 fade to gray
        c2_gray = _chip("p16 loss -> CDK4/6 uninhibited", GRAY, 20)
        c2_gray.move_to(c2.get_center())
        c3_gray = _chip("PTEN -> AKT -> cyclin D1 stable", GRAY, 20)
        c3_gray.move_to(c3.get_center())
        a2_gray = Arrow(c2_gray.get_right(), jbox_left, color=GRAY, stroke_width=3,
                        tip_length=0.16, buff=0.08, max_tip_length_to_length_ratio=0.3)
        a3_gray = Arrow(c3_gray.get_right(), jbox_left, color=GRAY, stroke_width=3,
                        tip_length=0.16, buff=0.08, max_tip_length_to_length_ratio=0.3)
        self.play(
            ReplacementTransform(c2, c2_gray),
            ReplacementTransform(a2, a2_gray),
            run_time=0.6,
        )
        self.play(
            ReplacementTransform(c3, c3_gray),
            ReplacementTransform(a3, a3_gray),
            run_time=0.6,
        )

        # Junction box dims — replace with teal version
        jbox_teal = _junction_box(jbox_center, "CDK4/6  Rb", TEAL)
        self.play(ReplacementTransform(jbox, jbox_teal), run_time=0.7)

        # Endpoint changes to teal arrested state
        ep_box_teal = _rect(2.2, 0.65, TEAL, 0.15, TEAL, 2)
        ep_box_teal.move_to(ep_center)
        ep_lbl_teal = SerifLabel("E2F bound / G1 arrest", TEAL, size=20)
        ep_lbl_teal.move_to(ep_center)
        ep_arr_teal = Arrow(jbox_center + RIGHT * 1.65, ep_center + LEFT * 1.15,
                            color=TEAL, stroke_width=3, tip_length=0.18, buff=0.05)
        self.play(
            ReplacementTransform(ep_box, ep_box_teal),
            ReplacementTransform(ep_lbl, ep_lbl_teal),
            ReplacementTransform(ep_arr, ep_arr_teal),
            run_time=0.7,
        )

        # "junction dark" label
        dark_lbl = SerifLabel("junction dark", TEAL, size=24)
        dark_lbl.next_to(jbox_teal, DOWN, buff=0.35)
        self.play(FadeIn(dark_lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 4.7))


class B14_RationalCombination(Scene):
    """Three-step rational combination strategy; GOLD fill sweep on 'convergence point'."""
    def construct(self):
        total = DUR["B14"]
        labels = [
            "Map active inputs",
            "Find convergence point",
            "Block at convergence",
        ]
        ys = [1.4, 0.0, -1.4]
        boxes = []
        for lbl, y in zip(labels, ys):
            b = _rect(4.8, 0.78, TEAL, 0.1, TEAL, 2)
            b.move_to(LEFT * 1.8 + UP * y)
            t = Text(lbl, font=SERIF, color=INK, font_size=26)
            t.move_to(b.get_center())
            boxes.append(VGroup(b, t))

        # Teal bracket on the left of all three boxes
        bracket_group = VGroup(*[b for b in boxes])
        brace = Brace(bracket_group, RIGHT, color=TEAL, buff=0.18)
        combo_lbl = Text("rational\ncombination", font=SERIF, color=TEAL,
                         font_size=26, line_spacing=1.3)
        combo_lbl.next_to(brace, RIGHT, buff=0.25)

        # GOLD highlight — fill Rectangle behind "Find convergence point" box
        gold_bar = _rect(4.9, 0.82, GOLD, 0.35)
        gold_bar.move_to(boxes[1].get_center())

        # Animate: boxes draw on one by one, then brace, then gold sweep
        for box in boxes:
            self.play(FadeIn(box, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(brace), FadeIn(combo_lbl), run_time=0.6)
        # Gold highlight sweeps (scale from zero width to full)
        gold_bar.set_opacity(0)
        self.play(gold_bar.animate.set_opacity(0.35), run_time=0.5)
        self.wait(max(0.5, total - 2.6 - len(boxes) * 0.5))


class B15_End(Scene):
    """Endcard — CANCER BIOLOGY eyebrow in TEAL; question -> answer recap."""
    def construct(self):
        total = DUR["B15"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Blocking one input cannot", font=DISPLAY, color=INK,
                  font_size=40, weight=BOLD)
        t2 = Text("close a gate with two others active.", font=DISPLAY, color=INK,
                  font_size=40, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.6)
        sub = Text("the convergence point is where the combination must act",
                   font=SERIF, color=INK, font_size=24)
        sub.next_to(u, DOWN, buff=0.45)
        self.play(FadeIn(eye, shift=DOWN * 0.2), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 2.3))
