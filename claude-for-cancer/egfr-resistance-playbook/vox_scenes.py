"""vox_scenes.py — egfr-resistance-playbook
B04 only: animated clinical decision tree for EGFR acquired resistance.
Palette: teardown — INK=#2A1A0E CREAM=#FFFFFF CRIMSON=#C8102E SLATE=#545454 GOLD=#F6D8DC
NEVER use: Axes, ParametricFunction, weight=NORMAL
ALWAYS: Manual Line for connectors; CREAM Rectangle backgrounds behind text near Lines.
"""
import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_EGFRTree(Scene):
    """Animated clinical decision tree: EGFR resistance mechanisms."""

    def construct(self):
        dur = DUR.get("B04", 20.0)

        # ── Title ──────────────────────────────────────────────────────────────
        title = Text("EGFR RESISTANCE DECISION TREE", font_size=28, color=INK,
                     weight=BOLD)
        title.move_to(UP * 3.2)

        # ── Root box ───────────────────────────────────────────────────────────
        root_bg = Rectangle(width=4.0, height=0.8)
        root_bg.set_fill(CREAM, opacity=1).set_stroke(color=INK, width=2)
        root_bg.move_to(UP * 1.8)
        root_txt = Text("EGFR-mutant NSCLC\nOsimertinib", font_size=16, color=INK)
        root_txt.move_to(root_bg.get_center())

        # ── Branch lines from root bottom (0, 1.4) ────────────────────────────
        branch_left = Line(start=[0, 1.4, 0], end=[-4.0, 0.4, 0],
                           color=INK, stroke_width=1.5)
        branch_mid  = Line(start=[0, 1.4, 0], end=[ 0.0, 0.4, 0],
                           color=INK, stroke_width=1.5)
        branch_right= Line(start=[0, 1.4, 0], end=[ 4.0, 0.4, 0],
                           color=INK, stroke_width=1.5)

        # ── Resistance mechanism boxes at y=0.0 ───────────────────────────────
        def res_box(cx, label):
            bg = Rectangle(width=2.8, height=0.8)
            bg.set_fill(CREAM, opacity=1).set_stroke(color=CRIMSON, width=2)
            bg.move_to([cx, 0.0, 0])
            txt = Text(label, font_size=13, color=CRIMSON)
            txt.move_to(bg.get_center())
            return VGroup(bg, txt)

        box_c797s = res_box(-4.0, "C797S\nMutation")
        box_met   = res_box( 0.0, "MET\nAmplification\n~15-20%")
        box_sclc  = res_box( 4.0, "SCLC\nTransformation\n~5%")

        # ── Connector lines: resistance boxes → detection boxes ────────────────
        conn_l1 = Line(start=[-4.0, -0.4, 0], end=[-4.0, -1.05, 0],
                       color=INK, stroke_width=1.2)
        conn_m1 = Line(start=[ 0.0, -0.4, 0], end=[ 0.0, -1.05, 0],
                       color=INK, stroke_width=1.2)
        conn_r1 = Line(start=[ 4.0, -0.4, 0], end=[ 4.0, -1.05, 0],
                       color=INK, stroke_width=1.2)

        # ── Detection boxes at y=-1.4 ─────────────────────────────────────────
        def det_box(cx, label):
            bg = Rectangle(width=2.8, height=0.7)
            bg.set_fill(GOLD, opacity=1).set_stroke(color=INK, width=1)
            bg.move_to([cx, -1.4, 0])
            txt = Text(label, font_size=13, color=INK)
            txt.move_to(bg.get_center())
            return VGroup(bg, txt)

        det_left  = det_box(-4.0, "ctDNA\nDeep Seq")
        det_mid   = det_box( 0.0, "FISH or\nctDNA")
        det_right = det_box( 4.0, "Tissue\nBiopsy Req.")

        # ── Connector lines: detection boxes → therapy labels ──────────────────
        conn_l2 = Line(start=[-4.0, -1.75, 0], end=[-4.0, -2.1, 0],
                       color=INK, stroke_width=1.2)
        conn_m2 = Line(start=[ 0.0, -1.75, 0], end=[ 0.0, -2.1, 0],
                       color=INK, stroke_width=1.2)
        conn_r2 = Line(start=[ 4.0, -1.75, 0], end=[ 4.0, -2.1, 0],
                       color=INK, stroke_width=1.2)

        # ── Therapy labels at y=-2.5 with CREAM background ────────────────────
        def therapy_label(cx, label, col):
            bg = Rectangle(width=3.0, height=0.7)
            bg.set_fill(CREAM, opacity=1).set_stroke(width=0, opacity=0)
            bg.move_to([cx, -2.5, 0])
            txt = Text(label, font_size=11, color=col)
            txt.move_to(bg.get_center())
            return VGroup(bg, txt)

        th_left  = therapy_label(-4.0, "EAI045 (invest.)\nNo approved std of care", SLATE)
        th_mid   = therapy_label( 0.0, "Osi + Savolitinib\n(TATTON data)", INK)
        th_right = therapy_label( 4.0, "EP/EC chemo\n(SCLC protocol)", INK)

        # ── Bottom crimson rule ────────────────────────────────────────────────
        PAD = 6.0
        bottom_rule = Line(start=[-PAD, -3.2, 0], end=[PAD * 0.9, -3.2, 0],
                           color=CRIMSON, stroke_width=2)

        # ── Animation sequence (7 states) ─────────────────────────────────────
        t_unit = dur / 7.0

        # State 1: title
        self.play(FadeIn(title), run_time=t_unit * 0.8)
        self.wait(t_unit * 0.2)

        # State 2: root box
        self.play(Create(root_bg), FadeIn(root_txt), run_time=t_unit * 0.8)
        self.wait(t_unit * 0.2)

        # State 3: three branch lines
        self.play(
            Create(branch_left), Create(branch_mid), Create(branch_right),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 4: three resistance boxes
        self.play(
            FadeIn(box_c797s),
            FadeIn(box_met),
            FadeIn(box_sclc),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 5: detection connectors + detection boxes
        self.play(
            Create(conn_l1), Create(conn_m1), Create(conn_r1),
            FadeIn(det_left), FadeIn(det_mid), FadeIn(det_right),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 6: therapy labels
        self.play(
            Create(conn_l2), Create(conn_m2), Create(conn_r2),
            FadeIn(th_left), FadeIn(th_mid), FadeIn(th_right),
            run_time=t_unit * 0.8
        )
        self.wait(t_unit * 0.2)

        # State 7: bottom crimson rule
        self.play(Create(bottom_rule), run_time=t_unit * 0.6)
        self.wait(t_unit * 0.4)
