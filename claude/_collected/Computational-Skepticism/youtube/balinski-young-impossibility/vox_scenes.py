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


class B04_ImpossibilityTriangles(Scene):
    def construct(self):
        def vertex_label(txt, pos, fontsize=22, color=INK):
            t = Text(txt, font_size=fontsize, color=color, weight=BOLD)
            t.move_to(pos)
            bw = max(t.width + 0.25, 0.5)
            bg = Rectangle(
                width=bw, height=0.38,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            return VGroup(bg, t)

        def meta_label(txt, pos, fontsize=20, color=SLATE):
            t = Text(txt, font_size=fontsize, color=color)
            t.move_to(pos)
            bw = max(t.width + 0.2, 0.5)
            bg = Rectangle(
                width=bw, height=0.34,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to(pos)
            return VGroup(bg, t)

        # ---- Title ----
        title = Text(
            "Impossibility Theorems: The Skeptic's Most Useful Result",
            font_size=26, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # ---- Left triangle: Arrow's theorem ----
        # Centroid at (-3.2, 0.2); side=2.8; height=2.425
        LC = (-3.2, 0.2)
        SIDE = 2.8
        H = SIDE * 0.866
        L_TOP  = (LC[0],           LC[1] + H * 2/3)
        L_BL   = (LC[0] - SIDE/2,  LC[1] - H / 3)
        L_BR   = (LC[0] + SIDE/2,  LC[1] - H / 3)

        left_edges = VGroup(
            Line((*L_TOP, 0), (*L_BL, 0), color=INK, stroke_width=2),
            Line((*L_BL,  0), (*L_BR, 0), color=INK, stroke_width=2),
            Line((*L_BR,  0), (*L_TOP, 0), color=INK, stroke_width=2),
        )

        left_top_lbl  = vertex_label("NON-DICTATOR", (L_TOP[0], L_TOP[1] + 0.28, 0))
        left_bl_lbl   = vertex_label("PARETO",       (L_BL[0] - 0.55, L_BL[1] - 0.30, 0))
        left_br_lbl   = vertex_label("IIA",          (L_BR[0] + 0.3,  L_BR[1] - 0.30, 0))
        left_vlabels  = VGroup(left_top_lbl, left_bl_lbl, left_br_lbl)

        left_X = Text("X", font_size=72, color=CRIMSON, weight=BOLD).move_to((*LC, 0))

        left_title_lbl = meta_label("ARROW 1951",                      (LC[0], LC[1] - 1.35, 0))
        left_case_lbl  = meta_label("Spoiler effect: 2000 US election", (LC[0], LC[1] - 1.78, 0), fontsize=18)
        left_meta = VGroup(left_title_lbl, left_case_lbl)

        # ---- Right triangle: Balinski-Young ----
        RC = (3.2, 0.2)
        R_TOP = (RC[0],           RC[1] + H * 2/3)
        R_BL  = (RC[0] - SIDE/2,  RC[1] - H / 3)
        R_BR  = (RC[0] + SIDE/2,  RC[1] - H / 3)

        right_edges = VGroup(
            Line((*R_TOP, 0), (*R_BL, 0), color=INK, stroke_width=2),
            Line((*R_BL,  0), (*R_BR, 0), color=INK, stroke_width=2),
            Line((*R_BR,  0), (*R_TOP, 0), color=INK, stroke_width=2),
        )

        right_top_lbl = vertex_label("QUOTA RULE", (R_TOP[0], R_TOP[1] + 0.28, 0))
        right_bl_lbl  = vertex_label("MONOTONE",   (R_BL[0] - 0.55, R_BL[1] - 0.30, 0))
        right_br_lbl  = vertex_label("NO PARADOX", (R_BR[0] + 0.5,  R_BR[1] - 0.30, 0))
        right_vlabels = VGroup(right_top_lbl, right_bl_lbl, right_br_lbl)

        right_X = Text("X", font_size=72, color=CRIMSON, weight=BOLD).move_to((*RC, 0))

        right_title_lbl = meta_label("BALINSKI-YOUNG 1982",            (RC[0], RC[1] - 1.35, 0))
        right_case_lbl  = meta_label("Alabama paradox: 1880 Census",   (RC[0], RC[1] - 1.78, 0), fontsize=18)
        right_meta = VGroup(right_title_lbl, right_case_lbl)

        # ---- Divider ----
        divider = Line((0.0, -2.0, 0), (0.0, 2.5, 0),
                       color=SLATE, stroke_width=1, stroke_opacity=0.4)

        # ---- Common callout ----
        callout_txt = "No system optimizing multiple fairness criteria can satisfy all simultaneously"
        callout_bg = Rectangle(
            width=11.0, height=0.46,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, -2.6, 0))
        callout_t = Text(callout_txt, font_size=22, color=INK).move_to((0, -2.6, 0))
        callout = VGroup(callout_bg, callout_t)

        # ---- Footer ----
        footer_txt = "Extension: ML fairness — accuracy vs. equalized odds vs. calibration (same triangular trade-off)"
        footer_bg = Rectangle(
            width=11.0, height=0.34,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, -3.15, 0))
        footer_t = Text(footer_txt, font_size=18, color=SLATE).move_to((0, -3.15, 0))
        footer = VGroup(footer_bg, footer_t)

        # ---- Animate (7 play calls) ----
        self.play(Write(title))
        self.play(Create(left_edges))
        self.play(FadeIn(left_vlabels), FadeIn(left_X), FadeIn(left_meta))
        self.play(Create(right_edges))
        self.play(FadeIn(right_vlabels), FadeIn(right_X), FadeIn(right_meta))
        self.play(FadeIn(divider), FadeIn(callout))
        self.play(FadeIn(footer))
        self.wait(1)
