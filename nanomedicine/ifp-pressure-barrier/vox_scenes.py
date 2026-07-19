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


class B04_IFPGradient(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("INTERSTITIAL FLUID PRESSURE: PHYSICS FIGHTS DELIVERY",font="Georgia",
                   font_size=19,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        # Divider
        div=Line([0,-3.1,0],[0,2.8,0],stroke_width=1.5,color=ManimColor(SLATE))
        # Panel labels
        norm_bg=Rectangle(width=2.2,height=0.3,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-2.8,2.5,0])
        norm_t=Text("NORMAL TISSUE",font="Georgia",font_size=16,color=ManimColor(INK),weight=BOLD).move_to([-2.8,2.5,0])
        tum_bg=Rectangle(width=1.8,height=0.3,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([2.8,2.5,0])
        tum_t=Text("SOLID TUMOR",font="Georgia",font_size=16,color=ManimColor(CRIMSON),weight=BOLD).move_to([2.8,2.5,0])
        # Blood vessels (rectangles)
        bv_norm=Rectangle(width=3.5,height=0.4,fill_color=ManimColor(CRIMSON),fill_opacity=0.7,stroke_width=0,stroke_opacity=0)
        bv_norm.move_to([-2.8,1.5,0])
        bv_norm_t=Text("blood vessel",font="Georgia",font_size=12,color=ManimColor(CREAM)).move_to([-2.8,1.5,0])
        bv_tum=Rectangle(width=3.5,height=0.4,fill_color=ManimColor(CRIMSON),fill_opacity=0.7,stroke_width=0,stroke_opacity=0)
        bv_tum.move_to([2.8,1.5,0])
        bv_tum_t=Text("LEAKY vessel",font="Georgia",font_size=12,color=ManimColor(CREAM)).move_to([2.8,1.5,0])
        blood_vessels=VGroup(bv_norm,bv_norm_t,bv_tum,bv_tum_t)
        # Pressure arrows
        # Normal: arrows pointing INWARD to tissue (down from vessel)
        norm_arrows=VGroup(*[
            Arrow([-2.8+dx,1.2,0],[-2.8+dx,0.6,0],stroke_width=1.5,color=ManimColor(SLATE),
                   buff=0.0,max_tip_length_to_length_ratio=0.25)
            for dx in [-0.8,0.0,0.8]
        ])
        # Tumor: arrows pointing OUTWARD (upward from tissue into vessel — reversed gradient)
        tum_arrows=VGroup(*[
            Arrow([2.8+dx,0.6,0],[2.8+dx,1.2,0],stroke_width=1.5,color=ManimColor(CRIMSON),
                   buff=0.0,max_tip_length_to_length_ratio=0.25)
            for dx in [-0.8,0.0,0.8]
        ])
        # Lymphatics (normal side)
        lymn=Rectangle(width=3.5,height=0.3,fill_color=ManimColor(GOLD),fill_opacity=0.8,stroke_width=0,stroke_opacity=0)
        lymn.move_to([-2.8,-0.5,0])
        lymn_t=Text("lymphatics (drainage)",font="Georgia",font_size=11,color=ManimColor(INK)).move_to([-2.8,-0.5,0])
        # Lymphatic drainage arrows (from tissue to lymphatic)
        lym_arrows_n=VGroup(*[
            Arrow([-2.8+dx,-0.1,0],[-2.8+dx,-0.35,0],stroke_width=1.5,color=ManimColor(GOLD),
                   buff=0.0,max_tip_length_to_length_ratio=0.3)
            for dx in [-0.6,0.0,0.6]
        ])
        # Tumor: X mark (no lymphatics)
        no_lym=Line([2.0,-0.65,0],[3.6,-0.35,0],stroke_width=3,color=ManimColor(CRIMSON))
        no_lym2=Line([2.0,-0.35,0],[3.6,-0.65,0],stroke_width=3,color=ManimColor(CRIMSON))
        no_lym_bg=Rectangle(width=2.4,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([2.8,-1.25,0])
        no_lym_t=Text("NO functional lymphatics",font="Georgia",font_size=12,color=ManimColor(CRIMSON)).move_to([2.8,-1.25,0])
        # IFP values
        ifp_norm_bg=Rectangle(width=2.0,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-2.8,-1.7,0])
        ifp_norm_t=Text("IFP: 0-3 mmHg",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([-2.8,-1.7,0])
        ifp_tum_bg=Rectangle(width=2.2,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([2.8,-1.7,0])
        ifp_tum_t=Text("IFP: 20-60 mmHg",font="Georgia",font_size=14,color=ManimColor(CRIMSON),weight=BOLD).move_to([2.8,-1.7,0])
        # Rim-dominant drug distribution in tumor (ring around a pale center)
        rim_ring=Circle(radius=0.7,fill_opacity=0,stroke_width=8,stroke_color=ManimColor(GOLD),stroke_opacity=0.6)
        rim_ring.move_to([2.8,0.3,0])
        rim_inner=Circle(radius=0.42,fill_color=ManimColor(CREAM),fill_opacity=0.8,stroke_width=0,stroke_opacity=0)
        rim_inner.move_to([2.8,0.3,0])
        rim_bg=Rectangle(width=2.5,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([2.8,-1.55,0])
        rim_t=Text("drug: rim only, pale center",font="Georgia",font_size=12,color=ManimColor(GOLD)).move_to([2.8,-1.55,0])
        rim_dist=VGroup(rim_ring,rim_inner,rim_bg,rim_t)
        footer=Line([-5.0,-3.1,0],[-4.2,-3.1,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(div),FadeIn(norm_bg),FadeIn(norm_t),FadeIn(tum_bg),FadeIn(tum_t))  # 1
        self.play(FadeIn(blood_vessels))                                                                    # 2
        self.play(FadeIn(norm_arrows),FadeIn(tum_arrows))                                                  # 3
        self.play(FadeIn(lymn),FadeIn(lymn_t),FadeIn(lym_arrows_n),FadeIn(no_lym),FadeIn(no_lym2),FadeIn(no_lym_bg),FadeIn(no_lym_t))  # 4
        self.play(FadeIn(ifp_norm_bg),FadeIn(ifp_norm_t),FadeIn(ifp_tum_bg),FadeIn(ifp_tum_t))           # 5
        self.play(FadeIn(rim_dist))                                                                         # 6
        self.play(FadeIn(footer))                                                                           # 7
