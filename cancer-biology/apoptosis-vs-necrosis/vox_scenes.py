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


class B04_CellDeathModes(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # Title
        # ------------------------------------------------------------------
        title = Text(
            "How Cancer Cells Die: Apoptosis vs. Necrosis vs. ICD",
            font_size=24, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # ------------------------------------------------------------------
        # Vertical divider
        # ------------------------------------------------------------------
        divider = Line((0.0, -1.4, 0), (0.0, 2.8, 0),
                       color=SLATE, stroke_width=1, stroke_opacity=0.5)

        # ------------------------------------------------------------------
        # Column headers — colored bg, CREAM text via move_to(bg_var)
        # ------------------------------------------------------------------
        left_hdr_bg = Rectangle(
            width=5.5, height=0.55,
            fill_color=SLATE, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((-3.0, 2.5, 0))
        left_hdr_txt = Text("APOPTOSIS", font_size=28, color=CREAM, weight=BOLD
                            ).move_to(left_hdr_bg)
        left_header = VGroup(left_hdr_bg, left_hdr_txt)

        right_hdr_bg = Rectangle(
            width=5.5, height=0.55,
            fill_color=CRIMSON, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((3.0, 2.5, 0))
        right_hdr_txt = Text("NECROSIS", font_size=28, color=CREAM, weight=BOLD
                             ).move_to(right_hdr_bg)
        right_header = VGroup(right_hdr_bg, right_hdr_txt)

        # ------------------------------------------------------------------
        # Left column steps (APOPTOSIS) at x=-3.0
        # All step boxes: CREAM bg, INK or PASS_CLR text
        # ------------------------------------------------------------------
        ls1_bg = Rectangle(width=4.8, height=0.5, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((-3.0, 1.7, 0))
        ls1_txt = Text("Cell shrinks, chromatin condenses",
                       font_size=19, color=INK).move_to((-3.0, 1.7, 0))
        ls1 = VGroup(ls1_bg, ls1_txt)

        ls2_bg = Rectangle(width=4.8, height=0.5, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((-3.0, 0.9, 0))
        ls2_txt = Text("Membrane blebs, apoptotic bodies",
                       font_size=19, color=INK).move_to((-3.0, 0.9, 0))
        ls2 = VGroup(ls2_bg, ls2_txt)

        ls3_bg = Rectangle(width=4.8, height=0.5, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((-3.0, 0.1, 0))
        ls3_txt = Text("Phagocytosis (silent)",
                       font_size=19, color=INK).move_to((-3.0, 0.1, 0))
        ls3 = VGroup(ls3_bg, ls3_txt)

        ls4_bg = Rectangle(width=4.8, height=0.5, fill_color="#E8F5E8", fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((-3.0, -0.7, 0))
        ls4_txt = Text("IMMUNOLOGICALLY SILENT",
                       font_size=19, color=PASS_CLR).move_to((-3.0, -0.7, 0))
        ls4 = VGroup(ls4_bg, ls4_txt)

        # ------------------------------------------------------------------
        # Right column steps (NECROSIS) at x=3.0
        # All step boxes: CREAM bg, INK or CRIMSON text
        # ------------------------------------------------------------------
        rs1_bg = Rectangle(width=4.8, height=0.5, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((3.0, 1.7, 0))
        rs1_txt = Text("Cell swells, organelles fail",
                       font_size=19, color=INK).move_to((3.0, 1.7, 0))
        rs1 = VGroup(rs1_bg, rs1_txt)

        rs2_bg = Rectangle(width=4.8, height=0.5, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((3.0, 0.9, 0))
        rs2_txt = Text("Membrane ruptures",
                       font_size=19, color=INK).move_to((3.0, 0.9, 0))
        rs2 = VGroup(rs2_bg, rs2_txt)

        rs3_bg = Rectangle(width=4.8, height=0.5, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((3.0, 0.1, 0))
        rs3_txt = Text("DAMPs released: HMGB1, IL-1b, ATP",
                       font_size=19, color=INK).move_to((3.0, 0.1, 0))
        rs3 = VGroup(rs3_bg, rs3_txt)

        rs4_bg = Rectangle(width=4.8, height=0.5, fill_color="#FFF5F5", fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to((3.0, -0.7, 0))
        rs4_txt = Text("INFLAMMATORY RESPONSE",
                       font_size=19, color=CRIMSON).move_to((3.0, -0.7, 0))
        rs4 = VGroup(rs4_bg, rs4_txt)

        # ------------------------------------------------------------------
        # ICD bridge box at y=-1.9 — GOLD bg, INK + SLATE text
        # ------------------------------------------------------------------
        icd_bg = Rectangle(
            width=11.4, height=0.85,
            fill_color=GOLD, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, -1.9, 0))
        icd_line1 = Text(
            "IMMUNOGENIC CELL DEATH (ICD) -- the bridge",
            font_size=22, color=INK, weight=BOLD
        ).move_to((0, -1.65, 0))
        icd_line2 = Text(
            "Anthracyclines + oxaliplatin: apoptosis WITH danger signals -> primes anti-tumor immunity",
            font_size=18, color=SLATE
        ).move_to((0, -2.05, 0))
        icd_bridge = VGroup(icd_bg, icd_line1, icd_line2)

        # ------------------------------------------------------------------
        # Clinical note at y=-2.8 — CREAM bg, SLATE text
        # ------------------------------------------------------------------
        clin_bg = Rectangle(
            width=9.0, height=0.36,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, -2.8, 0))
        clin_txt = Text(
            "Rationale for chemo + checkpoint inhibitor combinations",
            font_size=20, color=SLATE
        ).move_to((0, -2.8, 0))
        clinical_note = VGroup(clin_bg, clin_txt)

        # ------------------------------------------------------------------
        # Animation sequence (7 distinct play() calls — Gate A: 5+ OK)
        # ------------------------------------------------------------------
        self.play(Write(title))
        self.play(FadeIn(divider), FadeIn(left_header), FadeIn(right_header))
        self.play(FadeIn(ls1), FadeIn(rs1))
        self.play(FadeIn(ls2), FadeIn(rs2))
        self.play(FadeIn(ls3), FadeIn(rs3))
        self.play(FadeIn(ls4), FadeIn(rs4))
        self.play(FadeIn(icd_bridge), FadeIn(clinical_note))
        self.wait(1)
