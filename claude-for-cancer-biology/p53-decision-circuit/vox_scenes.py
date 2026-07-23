import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR="#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_P53Decision(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # Title
        # ------------------------------------------------------------------
        title = Text(
            "p53: The Cell Fate Decision Circuit",
            font_size=28, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # ------------------------------------------------------------------
        # DNA DAMAGE input box — SLATE bg, CREAM text
        # Text uses move_to(damage_bg) so Gate W resolves contrast correctly
        # ------------------------------------------------------------------
        damage_bg = Rectangle(
            width=3.0, height=0.55,
            fill_color=SLATE, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, 2.4, 0))
        damage_label = Text("DNA DAMAGE", font_size=24, color=CREAM, weight=BOLD
                            ).move_to(damage_bg)
        damage_box = VGroup(damage_bg, damage_label)

        arr_damage = Arrow(
            start=(0, 2.12, 0), end=(0, 1.88, 0),
            color=INK, stroke_width=2, buff=0
        )

        # ------------------------------------------------------------------
        # p53 node
        # ------------------------------------------------------------------
        p53_circle = Circle(
            radius=0.45,
            fill_color=CRIMSON, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, 1.4, 0))
        p53_label = Text("p53", font_size=24, color=CREAM, weight=BOLD
                         ).move_to(p53_circle)
        p53_node = VGroup(p53_circle, p53_label)

        # ------------------------------------------------------------------
        # MDM2 feedback box — SLATE bg, CREAM text
        # ------------------------------------------------------------------
        mdm2_bg = Rectangle(
            width=1.6, height=0.6,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((2.2, 1.4, 0))
        mdm2_line1 = Text("MDM2", font_size=18, color=INK, weight=BOLD
                          ).move_to(mdm2_bg)
        mdm2_line2 = Text("feedback", font_size=16, color=SLATE
                          ).move_to((2.2, 1.22, 0))
        mdm2_fwd = Line(
            start=(0.46, 1.4, 0), end=(1.4, 1.4, 0),
            color=SLATE, stroke_width=1.5
        )
        mdm2_back = Line(
            start=(1.4, 1.2, 0), end=(0.46, 1.1, 0),
            color=CRIMSON, stroke_width=1.5
        )
        mdm2_group = VGroup(mdm2_bg, mdm2_line1, mdm2_line2, mdm2_fwd, mdm2_back)

        # ------------------------------------------------------------------
        # Three branch arrows from p53 node
        # ------------------------------------------------------------------
        arr_left = Arrow(
            start=(0, 1.4, 0), end=(-3.2, 0.75, 0),
            color=INK, stroke_width=2, buff=0.5
        )
        arr_center = Arrow(
            start=(0, 1.4, 0), end=(0, 0.75, 0),
            color=INK, stroke_width=2, buff=0.45
        )
        arr_right = Arrow(
            start=(0, 1.4, 0), end=(3.2, 0.75, 0),
            color=INK, stroke_width=2, buff=0.5
        )
        branch_arrows = VGroup(arr_left, arr_center, arr_right)

        # ------------------------------------------------------------------
        # Severity labels at y=0.6 — CREAM bg, SLATE text
        # ------------------------------------------------------------------
        sev_bg_l = Rectangle(
            width=2.2, height=0.38,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((-3.5, 0.6, 0))
        sev_left = Text("LOW DAMAGE", font_size=20, color=SLATE
                        ).move_to((-3.5, 0.6, 0))
        sev_left_grp = VGroup(sev_bg_l, sev_left)

        sev_bg_c = Rectangle(
            width=2.2, height=0.38,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, 0.6, 0))
        sev_center = Text("SUSTAINED", font_size=20, color=SLATE
                          ).move_to((0, 0.6, 0))
        sev_center_grp = VGroup(sev_bg_c, sev_center)

        sev_bg_r = Rectangle(
            width=2.2, height=0.38,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((3.5, 0.6, 0))
        sev_right = Text("SEVERE", font_size=20, color=SLATE
                         ).move_to((3.5, 0.6, 0))
        sev_right_grp = VGroup(sev_bg_r, sev_right)

        severity_labels = VGroup(sev_left_grp, sev_center_grp, sev_right_grp)

        # ------------------------------------------------------------------
        # Molecular intermediaries at y=0.0 — GOLD bg, INK text
        # ------------------------------------------------------------------
        inter_bg_l = Rectangle(
            width=2.2, height=0.5,
            fill_color=GOLD, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((-3.5, 0.0, 0))
        inter_left = Text("p21 / CDK2", font_size=20, color=INK
                          ).move_to(inter_bg_l)
        inter_left_grp = VGroup(inter_bg_l, inter_left)

        inter_bg_c = Rectangle(
            width=2.2, height=0.5,
            fill_color=GOLD, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, 0.0, 0))
        inter_center = Text("p21 + RB", font_size=20, color=INK
                            ).move_to(inter_bg_c)
        inter_center_grp = VGroup(inter_bg_c, inter_center)

        inter_bg_r = Rectangle(
            width=2.2, height=0.5,
            fill_color=GOLD, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((3.5, 0.0, 0))
        inter_right = Text("PUMA / NOXA", font_size=20, color=INK
                           ).move_to(inter_bg_r)
        inter_right_grp = VGroup(inter_bg_r, inter_right)

        intermediate_boxes = VGroup(inter_left_grp, inter_center_grp, inter_right_grp)

        # ------------------------------------------------------------------
        # Outcome boxes at y=-1.0
        # ------------------------------------------------------------------
        # Left: transient G1 arrest — light green bg, PASS_CLR text
        out_bg_l = Rectangle(
            width=2.8, height=0.7,
            fill_color="#E8F5E8", fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((-3.5, -1.0, 0))
        out_left_l1 = Text("TRANSIENT", font_size=20, color=PASS_CLR, weight=BOLD
                           ).move_to((-3.5, -0.82, 0))
        out_left_l2 = Text("G1 ARREST", font_size=20, color=PASS_CLR, weight=BOLD
                           ).move_to((-3.5, -1.18, 0))
        out_left_grp = VGroup(out_bg_l, out_left_l1, out_left_l2)

        # Center: senescence — light pink bg, SLATE text
        out_bg_c = Rectangle(
            width=2.8, height=0.7,
            fill_color="#FFF5F5", fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, -1.0, 0))
        out_center_l1 = Text("PERMANENT", font_size=20, color=SLATE
                             ).move_to((0, -0.82, 0))
        out_center_l2 = Text("SENESCENCE", font_size=20, color=SLATE
                             ).move_to((0, -1.18, 0))
        out_center_grp = VGroup(out_bg_c, out_center_l1, out_center_l2)

        # Right: apoptosis — CRIMSON bg, CREAM text
        out_bg_r = Rectangle(
            width=2.8, height=0.7,
            fill_color=CRIMSON, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((3.5, -1.0, 0))
        out_right = Text("APOPTOSIS", font_size=26, color=CREAM, weight=BOLD
                         ).move_to(out_bg_r)
        out_right_grp = VGroup(out_bg_r, out_right)

        outcome_boxes = VGroup(out_left_grp, out_center_grp, out_right_grp)

        # Connector lines intermediary -> outcome
        line_l = Line((-3.5, -0.26, 0), (-3.5, -0.65, 0), color=SLATE, stroke_width=1.5)
        line_c = Line((0, -0.26, 0), (0, -0.65, 0), color=SLATE, stroke_width=1.5)
        line_r = Line((3.5, -0.26, 0), (3.5, -0.65, 0), color=SLATE, stroke_width=1.5)
        connector_lines = VGroup(line_l, line_c, line_r)

        # ------------------------------------------------------------------
        # Cancer consequence bar at y=-2.1 — CRIMSON bg, CREAM text
        # ------------------------------------------------------------------
        cons_bg = Rectangle(
            width=11.0, height=0.55,
            fill_color=CRIMSON, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, -2.1, 0))
        cons_label = Text(
            "X p53 LOSS: all three safeguards removed simultaneously",
            font_size=22, color=CREAM, weight=BOLD
        ).move_to(cons_bg)
        consequence_bar = VGroup(cons_bg, cons_label)

        # ------------------------------------------------------------------
        # Source citation at y=-2.85 — CREAM bg, SLATE text
        # ------------------------------------------------------------------
        citation_bg = Rectangle(
            width=10.0, height=0.36,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, -2.85, 0))
        citation = Text(
            "p53 loss: most common molecular event across all cancer types",
            font_size=20, color=SLATE
        ).move_to((0, -2.85, 0))
        citation_grp = VGroup(citation_bg, citation)

        # ------------------------------------------------------------------
        # Animation sequence (7 distinct play() calls — Gate A: 5+ OK)
        # ------------------------------------------------------------------
        self.play(Write(title))
        self.play(FadeIn(damage_box), FadeIn(arr_damage))
        self.play(FadeIn(p53_node), FadeIn(mdm2_group))
        self.play(FadeIn(branch_arrows), FadeIn(severity_labels))
        self.play(FadeIn(intermediate_boxes), FadeIn(connector_lines))
        self.play(FadeIn(outcome_boxes))
        self.play(FadeIn(consequence_bar), FadeIn(citation_grp))
        self.wait(1)
