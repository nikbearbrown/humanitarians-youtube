"""vox_scenes.py — Why the Spindle Checkpoint Pause Protects Every Division
(vox-spindle-checkpoint, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B02 is STILL (ai media
slot) and has no scene here — it renders as a slate until the plate lands.

Render everything:
  bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-spindle-checkpoint

Color law: TEAL = attached/ready/normal separation/checkpoint satisfied;
           CRIMSON = unattached kinetochore/inhibitory signal/checkpoint veto.
GOLD = editor's pen highlight, once only (B09 veto convergence label).
Exclusions: no G1/S checkpoint, no Rb/E2F, no G2/M/ATM/ATR cascade,
no CDK biochemistry, no CDK4/6 therapy, SAC-aneuploidy-cancer = one sentence.

Gate B: every zero-width stroke is also zero-opacity.
"""
import sys, json, pathlib, os

sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

# Required header per SLATE-RUNNER spec
_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- helpers

def _node(label, color, w=2.4, h=0.68):
    """Rounded rectangle node with white Montserrat label."""
    box = RoundedRectangle(width=w, height=h, corner_radius=0.13)
    box.set_fill(color, 1).set_stroke(width=0, opacity=0)
    txt = Text(label, font=DISPLAY, color=WHITE,
               font_size=int(21 * 0.88), weight="MEDIUM")
    if txt.width > w * 0.85:
        txt.scale_to_fit_width(w * 0.85)
    txt.move_to(box.get_center())
    return VGroup(box, txt)


def _arrow(start, end, color=INK):
    return Arrow(start, end, color=color, stroke_width=3,
                 max_tip_length_to_length_ratio=0.18, buff=0.1)


def _bar(w, h, color, opacity=1.0):
    b = Rectangle(width=w, height=h)
    b.set_fill(color, opacity).set_stroke(width=0, opacity=0)
    return b


def _chromosome(color=TEAL, scale=0.18):
    """Simple X-shaped chromosome from two rounded rectangles."""
    h = RoundedRectangle(width=scale * 3.0, height=scale * 1.0,
                         corner_radius=scale * 0.35)
    v = RoundedRectangle(width=scale * 1.0, height=scale * 3.0,
                         corner_radius=scale * 0.35)
    h.set_fill(color, 1).set_stroke(width=0, opacity=0)
    v.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return VGroup(h, v)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why the Spindle Checkpoint", font=DISPLAY, color=INK, font_size=28, weight=BOLD)
        t2 = Text("Pause Protects Every Division", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL)+DOWN*0.13, t2.get_corner(DR)+DOWN*0.13, color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B03_Question(Scene):
    """THE QUESTION beat: gap formula on screen AND in narration."""
    def construct(self):
        total = DUR["B03"]
        q_label = Text("THE QUESTION", font=DISPLAY, color=SLATE,
                        font_size=int(20 * 0.88), weight="MEDIUM")
        q1 = Text("Why does the cell pause", font=SERIF, color=INK,
                   font_size=42, weight=BOLD)
        q2 = Text("when chromosomes appear ready to separate?", font=SERIF,
                   color=INK, font_size=36, weight=BOLD)
        block = VGroup(q1, q2).arrange(DOWN, buff=0.14).move_to(UP * 0.1)
        if block.width > 12.5:
            block.scale_to_fit_width(12.5)
        q_label.next_to(block, UP, buff=0.75)
        u = Line(q2.get_corner(DL)+DOWN*0.13, q2.get_corner(DR)+DOWN*0.13,
                 color=TEAL, stroke_width=2)
        self.play(FadeIn(q_label), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.4, total - 1.7))


class B04_NaiveExpectation(Scene):
    """THE PROBLEM: naive expectation — alignment looks like readiness.
    Chromosomes at plate, all TEAL fibers, question arrow."""
    def construct(self):
        total = DUR["B04"]
        hdr = SerifLabel("the naive expectation", SLATE, size=26)
        hdr.to_edge(UP, buff=0.7)

        # Metaphase plate line
        plate = Line(LEFT * 0.02, RIGHT * 0.02,
                     color=INK, stroke_width=1.5)
        plate.set_stroke(opacity=0.3)

        # 8 stylized chromosomes at the plate (X shapes in a row)
        chroms = VGroup()
        positions = np.linspace(-3.2, 3.2, 8)
        for x in positions:
            ch = _chromosome(TEAL, scale=0.2)
            ch.move_to(np.array([x, -0.1, 0]))
            chroms.add(ch)

        # Spindle fibers from poles (UP and DOWN)
        fibers_top = VGroup()
        fibers_bot = VGroup()
        for x in positions:
            ft = Line(np.array([x, 2.8, 0]), np.array([x, 0.18, 0]),
                      color=TEAL, stroke_width=1.5)
            fb = Line(np.array([x, -0.38, 0]), np.array([x, -2.8, 0]),
                      color=TEAL, stroke_width=1.5)
            ft.set_stroke(opacity=0.7)
            fb.set_stroke(opacity=0.7)
            fibers_top.add(ft)
            fibers_bot.add(fb)

        # Question arrow and chip
        arrow = Arrow(RIGHT * 5.8 + UP * 0.4, RIGHT * 5.8 + DOWN * 0.6,
                       color=CRIMSON, stroke_width=3,
                       max_tip_length_to_length_ratio=0.25)
        q_chip = LabelChip("separate now?", accent=CRIMSON, size=22)
        q_chip.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in chroms],
                               lag_ratio=0.07, run_time=1.2))
        self.play(LaggedStart(*[Create(f) for f in list(fibers_top) + list(fibers_bot)],
                               lag_ratio=0.04, run_time=0.9))
        self.play(GrowArrow(arrow), FadeIn(q_chip, shift=LEFT * 0.2), run_time=0.7)
        self.wait(max(0.3, total - 3.3))


class B05_IrreversibilityStakes(Scene):
    """THE PROBLEM: cohesin holds sister chromatids; once cut, irreversible."""
    def construct(self):
        total = DUR["B05"]
        hdr = SerifLabel("chromosome separation is irreversible", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.7)

        # Left sister chromatid
        lc = RoundedRectangle(width=0.7, height=2.4, corner_radius=0.25)
        lc.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        lc.move_to(LEFT * 1.1 + DOWN * 0.2)

        # Right sister chromatid
        rc = RoundedRectangle(width=0.7, height=2.4, corner_radius=0.25)
        rc.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
        rc.move_to(RIGHT * 1.1 + DOWN * 0.2)

        # Cohesin bridge (TEAL horizontal bar connecting them)
        cohesin = Rectangle(width=2.2, height=0.4)
        cohesin.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        cohesin.move_to(DOWN * 0.2)
        cohesin_label = SerifLabel("cohesin", TEAL, size=22)
        cohesin_label.next_to(cohesin, DOWN, buff=0.18)

        # "intact" label
        intact_chip = LabelChip("held together", accent=TEAL, size=22)
        intact_chip.move_to(DOWN * 1.9)

        # Separase (CRIMSON cutter)
        sep = LabelChip("separase cuts", accent=CRIMSON, size=22)
        sep.move_to(UP * 1.4)

        # Post-cut target positions
        lc_left = lc.copy().move_to(LEFT * 3.8 + DOWN * 0.2)
        rc_right = rc.copy().move_to(RIGHT * 3.8 + DOWN * 0.2)
        lc_left.set_fill(TEAL, 0.6)
        rc_right.set_fill(TEAL, 0.6)

        # "irreversible" label after snap
        irrev = SerifLabel("irreversible in seconds", CRIMSON, size=26)
        irrev.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(GrowFromCenter(lc), GrowFromCenter(rc),
                  GrowFromCenter(cohesin), FadeIn(cohesin_label), run_time=0.9)
        self.play(FadeIn(intact_chip, shift=UP * 0.15), run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(sep, shift=DOWN * 0.2), run_time=0.5)
        self.play(cohesin.animate.scale(0.05),
                  FadeOut(cohesin_label), FadeOut(intact_chip), run_time=0.6)
        self.play(Transform(lc, lc_left), Transform(rc, rc_right), run_time=0.9)
        self.play(FadeIn(irrev, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 4.5))


class B06_SectionMechanism(Scene):
    """Section card: THE SPINDLE ASSEMBLY CHECKPOINT."""
    def construct(self):
        total = DUR["B06"]
        label = Text("THE SPINDLE ASSEMBLY CHECKPOINT",
                     font=DISPLAY, color=SLATE,
                     font_size=int(30 * 0.88), weight="MEDIUM")
        if label.width > 12.0:
            label.scale_to_fit_width(12.0)
        label.move_to(ORIGIN)
        u = Line(label.get_corner(DL)+DOWN*0.14, label.get_corner(DR)+DOWN*0.14,
                 color=SLATE, stroke_width=1.5)
        self.play(FadeIn(label), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 0.8))


class B07_OneUnattachedKinetochore(Scene):
    """46 chromosomes at metaphase plate: 45 TEAL (attached), 1 CRIMSON
    (unattached kinetochore emitting inhibitory signal cloud).
    Key visual object from the card."""
    def construct(self):
        total = DUR["B07"]
        hdr = SerifLabel("one unattached kinetochore · out of 92", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.65)

        # Plate line (faint)
        plate = Line(LEFT * 6.5, RIGHT * 6.5,
                     color=INK, stroke_width=1.2)
        plate.set_stroke(opacity=0.2)
        plate.move_to(DOWN * 0.15)

        # 46 chromosome dots: 7 rows x 6–7 per row, centered at plate
        positions = []
        cols_per_row = [6, 7, 7, 6, 7, 7, 6]
        y_start = 1.6
        for row_i, n_cols in enumerate(cols_per_row):
            y = y_start - row_i * 0.52
            x_start = -(n_cols - 1) * 0.88 / 2
            for col_i in range(n_cols):
                x = x_start + col_i * 0.88
                positions.append(np.array([x, y, 0]))
        # Take exactly 46
        positions = positions[:46]

        attached = VGroup()
        for pos in positions[:-1]:  # 45 attached
            dot = Dot(radius=0.16, color=TEAL)
            dot.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
            dot.move_to(pos)
            attached.add(dot)

        # The one unattached chromosome (CRIMSON)
        unattached_pos = positions[-1] + np.array([0.0, 0.3, 0])
        stray = Dot(radius=0.22, color=CRIMSON)
        stray.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        stray.move_to(unattached_pos)

        # Inhibitory signal cloud — concentric arcs from the stray kinetochore
        signal_arcs = VGroup()
        for r in [0.45, 0.75, 1.05]:
            arc = Circle(radius=r)
            arc.set_stroke(CRIMSON, width=max(1.0, 2.5 - r * 1.5), opacity=0.55)
            arc.set_fill(opacity=0)
            arc.move_to(unattached_pos)
            signal_arcs.add(arc)

        # Label for the stray
        stray_label = SerifLabel("unattached kinetochore", CRIMSON, size=20)
        stray_label.next_to(stray, RIGHT, buff=0.3)
        if stray_label.get_right()[0] > 6.5:
            stray_label.next_to(stray, LEFT, buff=0.3)

        # "inhibitory signal" chip
        sig_chip = LabelChip("inhibitory signal", accent=CRIMSON, size=20)
        sig_chip.next_to(signal_arcs, DOWN, buff=0.15)

        # Teal spindle fibers for attached dots (abbreviated: just top+bottom pole lines)
        # positioned well below the hdr (hdr is at y~3.3 from top edge, poles at y=2.2/−2.2)
        top_pole = Line(LEFT * 5.5 + UP * 2.2, RIGHT * 5.5 + UP * 2.2,
                        color=TEAL, stroke_width=1.0)
        top_pole.set_stroke(opacity=0.35)
        bot_pole = Line(LEFT * 5.5 + DOWN * 2.2, RIGHT * 5.5 + DOWN * 2.2,
                        color=TEAL, stroke_width=1.0)
        bot_pole.set_stroke(opacity=0.35)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(Create(plate), run_time=0.3)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in attached],
                               lag_ratio=0.018, run_time=1.6))
        self.play(GrowFromCenter(stray), FadeIn(stray_label), run_time=0.6)
        self.play(LaggedStart(*[Create(arc) for arc in signal_arcs],
                               lag_ratio=0.18, run_time=0.9))
        self.play(FadeIn(sig_chip, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 4.3))


class B08_MCCCascade(Scene):
    """MCC cascade: unattached kinetochore -> MCC -> APC/C blocked ->
    securin intact -> separase locked. Chain of inhibition."""
    def construct(self):
        total = DUR["B08"]
        hdr = SerifLabel("the checkpoint cascade", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.65)

        # Nodes in a left-to-right chain
        kinet = _node("UNATTACHED\nKINETOCHORE", CRIMSON, w=2.6, h=0.85)
        kinet.move_to(LEFT * 5.2 + DOWN * 0.1)

        mcc = _node("MCC", CRIMSON, w=1.6, h=0.68)
        mcc.move_to(LEFT * 2.4 + DOWN * 0.1)

        apc = _node("APC/C\nBLOCKED", CRIMSON, w=2.0, h=0.85)
        apc.move_to(RIGHT * 0.3 + DOWN * 0.1)

        securin = _node("SECURIN\nINTACT", TEAL, w=2.0, h=0.85)
        securin.move_to(RIGHT * 2.9 + DOWN * 0.1)

        separase = _node("SEPARASE\nINACTIVE", CRIMSON, w=2.0, h=0.85)
        separase.move_to(RIGHT * 5.5 + DOWN * 0.1)

        a1 = _arrow(kinet.get_right(), mcc.get_left(), color=CRIMSON)
        a2 = _arrow(mcc.get_right(), apc.get_left(), color=CRIMSON)
        a3 = _arrow(apc.get_right(), securin.get_left(), color=CRIMSON)
        a4 = _arrow(securin.get_right(), separase.get_left(), color=CRIMSON)

        # "CELL ARRESTED" label below
        arrested = LabelChip("cell arrested", accent=CRIMSON, size=22)
        arrested.to_edge(DOWN, buff=0.75)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(GrowFromCenter(kinet), run_time=0.6)
        self.play(Create(a1), GrowFromCenter(mcc), run_time=0.6)
        self.play(Create(a2), GrowFromCenter(apc), run_time=0.6)
        self.play(Create(a3), GrowFromCenter(securin), run_time=0.6)
        self.play(Create(a4), GrowFromCenter(separase), run_time=0.6)
        self.play(FadeIn(arrested, shift=UP * 0.15), run_time=0.4)
        self.wait(max(0.3, total - 3.9))


class B09_VetoLogicCard(Scene):
    """CARD section bridge: one unattached kinetochore — whole cell arrested.
    Rhythm break between B08 and B10."""
    def construct(self):
        total = DUR["B09"]
        line1 = Text("ONE UNATTACHED KINETOCHORE", font=DISPLAY,
                      color=CRIMSON, font_size=int(32 * 0.88), weight="MEDIUM")
        line2 = Text("WHOLE CELL ARRESTED", font=DISPLAY,
                      color=SLATE, font_size=int(32 * 0.88), weight="MEDIUM")
        block = VGroup(line1, line2).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        if block.width > 12.2:
            block.scale_to_fit_width(12.2)
        u = Line(line2.get_corner(DL)+DOWN*0.13, line2.get_corner(DR)+DOWN*0.13,
                 color=SLATE, stroke_width=1.5)
        self.play(FadeIn(line1), run_time=0.6)
        self.play(FadeIn(line2), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 1.4))


class B10_ResolutionCascade(Scene):
    """Checkpoint resolution: final kinetochore captured -> MCC dissolves ->
    APC/C fires -> securin gone -> separase active -> cohesin cut ->
    chromosomes separate. The collapse."""
    def construct(self):
        total = DUR["B10"]
        hdr = SerifLabel("the last kinetochore attaches", TEAL, size=26)
        hdr.to_edge(UP, buff=0.65)

        # Final kinetochore (was CRIMSON) now getting captured (TEAL fiber arrives)
        stray = Dot(radius=0.22, color=CRIMSON)
        stray.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        stray.move_to(LEFT * 4.5 + UP * 0.4)

        # Microtubule arriving (TEAL line growing toward stray)
        mt_start = LEFT * 4.5 + DOWN * 2.0
        mt = Line(mt_start, stray.get_bottom(), color=TEAL, stroke_width=3)
        mt.set_stroke(opacity=0.0)

        # MCC cloud (starts CRIMSON, fades)
        mcc_cloud = Circle(radius=0.6)
        mcc_cloud.set_fill(CRIMSON, 0.3).set_stroke(CRIMSON, 2, opacity=0.7)
        mcc_cloud.move_to(LEFT * 4.5 + UP * 0.4)
        mcc_label = Text("MCC", font=DISPLAY, color=CRIMSON,
                          font_size=int(20 * 0.88), weight="MEDIUM")
        mcc_label.move_to(mcc_cloud.get_center())

        # Downstream cascade (right side): APC/C fires, securin gone, separase active
        apc_fire = _node("APC/C FIRES", TEAL, w=2.0, h=0.68)
        apc_fire.move_to(RIGHT * 0.5 + UP * 1.2)

        securin_gone = _node("securin degraded", CRIMSON, w=2.2, h=0.68)
        securin_gone.move_to(RIGHT * 0.5 + DOWN * 0.1)

        sep_active = _node("separase active", TEAL, w=2.2, h=0.68)
        sep_active.move_to(RIGHT * 0.5 + DOWN * 1.4)

        cohesin_cut = _node("cohesin cut", TEAL, w=2.0, h=0.68)
        cohesin_cut.move_to(RIGHT * 3.8 + DOWN * 0.1)

        a_apc_sec = _arrow(apc_fire.get_bottom(), securin_gone.get_top(), color=TEAL)
        a_sec_sep = _arrow(securin_gone.get_bottom(), sep_active.get_top(), color=TEAL)
        a_sep_coh = _arrow(sep_active.get_right(), cohesin_cut.get_left(), color=TEAL)

        # "chromosomes separate" final label
        final = LabelChip("chromosomes separate", accent=TEAL, size=22)
        final.to_edge(DOWN, buff=0.7)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(GrowFromCenter(stray), FadeIn(mcc_cloud), FadeIn(mcc_label),
                  run_time=0.6)
        # Microtubule grows to capture the kinetochore
        self.play(mt.animate.set_stroke(opacity=0.85), run_time=0.7)
        self.play(stray.animate.set_fill(TEAL, 1),
                  FadeOut(mcc_cloud), FadeOut(mcc_label), run_time=0.7)
        # Cascade builds left to right
        self.play(GrowFromCenter(apc_fire), run_time=0.5)
        self.play(Create(a_apc_sec), GrowFromCenter(securin_gone), run_time=0.5)
        self.play(securin_gone.animate.scale(0.5), run_time=0.4)
        self.play(Create(a_sec_sep), GrowFromCenter(sep_active), run_time=0.5)
        self.play(Create(a_sep_coh), GrowFromCenter(cohesin_cut), run_time=0.5)
        self.play(FadeIn(final, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 4.8))


class B11_AneuploidyResult(Scene):
    """THE IMPLICATION: aneuploidy — two daughter cells with wrong chromosome
    counts. One-sentence cancer connection."""
    def construct(self):
        total = DUR["B11"]
        hdr = SerifLabel("checkpoint failure -> aneuploidy", CRIMSON, size=26)
        hdr.to_edge(UP, buff=0.65)

        # Two daughter cell circles
        left_cell = Circle(radius=1.6)
        left_cell.set_fill(GROUND, 1).set_stroke(INK, 2, opacity=0.7)
        left_cell.move_to(LEFT * 3.6 + DOWN * 0.3)

        right_cell = Circle(radius=1.6)
        right_cell.set_fill(GROUND, 1).set_stroke(INK, 2, opacity=0.7)
        right_cell.move_to(RIGHT * 3.6 + DOWN * 0.3)

        # Left cell: too many chromosomes (extra CRIMSON dots)
        left_chroms = VGroup()
        normal_positions = [(0.0, 0.4), (-0.55, 0.0), (0.55, 0.0),
                            (0.0, -0.4), (-0.55, -0.8), (0.55, -0.8)]
        extra_positions = [(-0.9, 0.5), (0.9, 0.5)]  # extras
        for px, py in normal_positions:
            d = Dot(radius=0.14, color=TEAL)
            d.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
            d.move_to(LEFT * 3.6 + np.array([px, py - 0.3, 0]))
            left_chroms.add(d)
        extra_chroms = VGroup()
        for px, py in extra_positions:
            d = Dot(radius=0.16, color=CRIMSON)
            d.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
            d.move_to(LEFT * 3.6 + np.array([px, py - 0.3, 0]))
            extra_chroms.add(d)

        # Right cell: too few (missing = shown as empty outlines)
        right_chroms = VGroup()
        for px, py in normal_positions:
            d = Dot(radius=0.14, color=TEAL)
            d.set_fill(TEAL, 1).set_stroke(width=0, opacity=0)
            d.move_to(RIGHT * 3.6 + np.array([px, py - 0.3, 0]))
            right_chroms.add(d)
        missing_placeholder = VGroup()
        for px, py in [(-0.9, 0.5), (0.9, 0.5)]:
            d = Dot(radius=0.16)
            d.set_fill(opacity=0).set_stroke(CRIMSON, 2.5, opacity=0.8)
            d.move_to(RIGHT * 3.6 + np.array([px, py - 0.3, 0]))
            missing_placeholder.add(d)

        # Labels under each cell
        too_many = LabelChip("extra chromosomes", accent=CRIMSON, size=20)
        too_many.next_to(left_cell, DOWN, buff=0.2)
        too_few = LabelChip("missing chromosomes", accent=CRIMSON, size=20)
        too_few.next_to(right_cell, DOWN, buff=0.2)

        # Aneuploidy chip — placed below hdr (hdr is at top edge ~3.3), well clear
        aneu_chip = LabelChip("aneuploidy", accent=CRIMSON, size=22)
        aneu_chip.move_to(UP * 2.1)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(Create(left_cell), Create(right_cell), run_time=0.7)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in left_chroms],
                               lag_ratio=0.06, run_time=0.8),
                  LaggedStart(*[GrowFromCenter(d) for d in right_chroms],
                               lag_ratio=0.06, run_time=0.8))
        self.play(LaggedStart(*[GrowFromCenter(d) for d in extra_chroms],
                               lag_ratio=0.15, run_time=0.6),
                  LaggedStart(*[Create(d) for d in missing_placeholder],
                               lag_ratio=0.15, run_time=0.6))
        self.play(FadeIn(too_many, shift=UP * 0.1),
                  FadeIn(too_few, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(aneu_chip, shift=DOWN * 0.2), run_time=0.4)
        self.wait(max(0.3, total - 3.5))


class B12_CheckpointWalkthrough(Scene):
    """THE EXAMPLE: illustrative walkthrough. 46 align -> 45 attached, 1 stray ->
    MCC -> wait (clock) -> capture -> 90s -> separate. Top-to-bottom timeline."""
    def construct(self):
        total = DUR["B12"]
        hdr = SerifLabel("illustrative  ·  one cell, one checkpoint cycle", SLATE, size=24)
        hdr.to_edge(UP, buff=0.55)

        # Timeline axis (vertical on the left)
        axis = Line(UP * 3.0 + LEFT * 5.8, DOWN * 3.0 + LEFT * 5.8,
                    color=INK, stroke_width=1.8)
        axis.set_stroke(opacity=0.45)

        # Step labels down the timeline
        steps_data = [
            (UP * 2.5, "46 chromosomes align", SLATE, "B12_step1"),
            (UP * 1.3, "45 attached  ·  1 kinetochore unattached", CRIMSON, "B12_step2"),
            (UP * 0.1, "MCC forms  ·  APC/C blocked  ·  cell waits 4 min", CRIMSON, "B12_step3"),
            (DOWN * 1.1, "microtubule captures last kinetochore", TEAL, "B12_step4"),
            (DOWN * 2.3, "MCC dissolves  ·  90 s  ·  chromosomes separate", TEAL, "B12_step5"),
        ]

        step_nodes = VGroup()
        for pos, label_text, color, _ in steps_data:
            chip = LabelChip(label_text, accent=color, size=19)
            chip.move_to(pos + RIGHT * 1.8)
            if chip.width > 10.5:
                chip.scale_to_fit_width(10.5)
            step_nodes.add(chip)

        # Tick marks on the axis
        ticks = VGroup()
        tick_y_vals = [2.5, 1.3, 0.1, -1.1, -2.3]
        for y in tick_y_vals:
            tick = Line(LEFT * 5.8 + UP * y + LEFT * 0.18,
                        LEFT * 5.8 + UP * y + RIGHT * 0.18,
                        color=INK, stroke_width=1.8)
            tick.set_stroke(opacity=0.5)
            ticks.add(tick)

        # "illustrative" label bottom right
        illu = SerifLabel("illustrative", SLATE, size=20)
        illu.to_corner(DR, buff=0.55)

        self.play(FadeIn(hdr), run_time=0.5)
        self.play(Create(axis), run_time=0.4)
        # Reveal steps one by one
        for i, (chip, tick) in enumerate(zip(step_nodes, ticks)):
            self.play(Create(tick), FadeIn(chip, shift=RIGHT * 0.3), run_time=0.7)
            if i < len(step_nodes) - 1:
                self.wait(0.5)
        self.play(FadeIn(illu, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.4, total - (0.5 + 0.4 + 5 * 0.7 + 4 * 0.5 + 0.4)))


class B13_End(Scene):
    """Endcard: question -> answer, CANCER BIOLOGY kicker."""
    def construct(self):
        total = DUR["B13"]
        topic = Text("CANCER BIOLOGY", font=DISPLAY, color=TEAL,
                      font_size=int(22 * 0.88), weight="MEDIUM")
        topic.to_edge(UP, buff=0.7)

        q = SerifLabel("why does the cell pause at metaphase?", CRIMSON, size=26)
        q.move_to(UP * 0.9)

        a1 = Text("One unattached kinetochore generates a diffusing veto", font=SERIF,
                   color=INK, font_size=32, weight=BOLD)
        a2 = Text("that arrests the whole cell — a single-condition block,", font=SERIF,
                   color=INK, font_size=32, weight=BOLD)
        a3 = Text("not a readiness vote.", font=SERIF, color=INK,
                   font_size=32, weight=BOLD)
        block = VGroup(a1, a2, a3).arrange(DOWN, buff=0.12).move_to(DOWN * 0.5)
        if block.width > 13.0:
            block.scale_to_fit_width(13.0)
        u = Line(a3.get_corner(DL)+DOWN*0.13, a3.get_corner(DR)+DOWN*0.13,
                 color=TEAL, stroke_width=2)

        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(q), run_time=0.6)
        self.play(FadeIn(a1), run_time=0.7)
        self.play(FadeIn(a2), run_time=0.7)
        self.play(FadeIn(a3), Create(u), run_time=0.8)
        self.wait(max(0.3, total - 3.3))
