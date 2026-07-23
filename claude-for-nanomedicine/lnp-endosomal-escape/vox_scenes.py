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


class B04_LNPEscape(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("LNP ENDOSOMAL ESCAPE: 1-2% SUCCESS RATE",font="Georgia",
                   font_size=22,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        # Stage 1: BLOODSTREAM — LNP circle at top
        lnp=Circle(radius=0.4,fill_color=ManimColor(GOLD),fill_opacity=0.9,stroke_width=2,stroke_color=ManimColor(INK))
        lnp.move_to([0,2.2,0])
        lnp_bg=Rectangle(width=1.0,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([1.2,2.2,0])
        lnp_t=Text("LNP (mRNA)",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([1.2,2.2,0])
        stage1=VGroup(lnp,lnp_bg,lnp_t)
        # Arrow down to endosome
        arr1=Arrow([0,1.8,0],[0,1.2,0],stroke_width=2,color=ManimColor(INK),buff=0.0,max_tip_length_to_length_ratio=0.25)
        end_box=Rectangle(width=3.0,height=0.8,fill_color=ManimColor(SLATE),fill_opacity=0.3,stroke_width=2,stroke_color=ManimColor(INK),stroke_opacity=1.0)
        end_box.move_to([0,0.5,0])
        end_bg=Rectangle(width=1.0,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,0.7,0])
        end_t=Text("ENDOSOME",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([0,0.7,0])
        endosome=VGroup(end_box,end_bg,end_t)
        # pH annotation — separate from endosome VGroup for distinct play #3 reveal
        ph_bg=Rectangle(width=2.0,height=0.24,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,0.25,0])
        ph_t=Text("pH drops 7.4 -> 5.5; lipid ionizes",font="Georgia",font_size=12,color=ManimColor(CRIMSON)).move_to([0,0.25,0])
        ionize_lbl_bg=Rectangle(width=2.4,height=0.24,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.2,0.5,0])
        ionize_lbl=Text("ALC-0315 / SM-102 (ionizable lipid)",font="Georgia",font_size=12,color=ManimColor(CRIMSON)).move_to([3.2,0.5,0])
        ph_reveal=VGroup(ph_bg,ph_t,ionize_lbl_bg,ionize_lbl)
        # Two branches from endosome
        # Left: Lysosome (98-99% degraded) — CRIMSON
        arr_lys=Arrow([-0.5,0.1,0],[-2.5,-0.9,0],stroke_width=2,color=ManimColor(CRIMSON),buff=0.05,max_tip_length_to_length_ratio=0.25)
        lys_box=Rectangle(width=3.2,height=0.7,fill_color=ManimColor(CRIMSON),fill_opacity=0.5,stroke_width=0,stroke_opacity=0)
        lys_box.move_to([-2.8,-1.5,0])
        lys_t=Text("LYSOSOME\n98-99% DEGRADED",font="Georgia",font_size=14,color=ManimColor(CREAM)).move_to([-2.8,-1.5,0])
        lysosome=VGroup(lys_box,lys_t)
        # Right: Cytoplasm (1-2% escape) — GOLD
        arr_cyt=Arrow([0.5,0.1,0],[2.5,-0.9,0],stroke_width=2,color=ManimColor(GOLD),buff=0.05,max_tip_length_to_length_ratio=0.25)
        cyt_box=Rectangle(width=3.2,height=0.7,fill_color=ManimColor(GOLD),fill_opacity=0.9,stroke_width=0,stroke_opacity=0)
        cyt_box.move_to([2.8,-1.5,0])
        cyt_t=Text("CYTOPLASM\n1-2% escape -> protein",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([2.8,-1.5,0])
        cytoplasm=VGroup(cyt_box,cyt_t)
        # Implication annotation
        imp_bg=Rectangle(width=5.5,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-2.5,0])
        imp_t=Text("If endosomal escape improved 10x: mRNA medicines 10x more potent",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([0,-2.5,0])
        footer=Line([-5.0,-3.1,0],[-4.2,-3.1,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(stage1))                                           # 1
        self.play(FadeIn(arr1),FadeIn(endosome))                                          # 2
        self.play(FadeIn(ph_reveal))                                                      # 3 — pH + ionizable lipid label revealed separately
        self.play(FadeIn(arr_lys),FadeIn(lysosome))                                      # 4
        self.play(FadeIn(arr_cyt),FadeIn(cytoplasm))                                     # 5
        self.play(FadeIn(imp_bg),FadeIn(imp_t))                                          # 6
        self.play(FadeIn(footer))                                                          # 7
