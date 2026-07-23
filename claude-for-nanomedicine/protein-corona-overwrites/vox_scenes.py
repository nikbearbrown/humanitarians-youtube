import sys, json, pathlib, numpy as np
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


class B04_ProteinCorona(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("PROTEIN CORONA: THE BODY OVERWRITES YOUR DESIGN",font="Georgia",
                   font_size=19,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        # Central NP circle
        np_circle=Circle(radius=0.5,fill_color=ManimColor(GOLD),fill_opacity=0.9,stroke_width=2,stroke_color=ManimColor(INK))
        np_circle.move_to([0,0.5,0])
        np_bg=Rectangle(width=2.0,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,1.7,0])
        np_t=Text("ENGINEERED NANOPARTICLE",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([0,1.7,0])
        np_stage=VGroup(np_circle,np_bg,np_t)
        # Targeting ligands: 8 small lines radiating outward
        angles=np.linspace(0,2*np.pi,8,endpoint=False)
        ligands=VGroup(*[
            Line([0.5*np.cos(a)+0.0, 0.5*np.sin(a)+0.5, 0],
                 [0.8*np.cos(a)+0.0, 0.8*np.sin(a)+0.5, 0],
                 stroke_width=3,color=ManimColor(CRIMSON))
            for a in angles
        ])
        lig_bg=Rectangle(width=2.4,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-2.5,0.5,0])
        lig_t=Text("targeting ligands",font="Georgia",font_size=13,color=ManimColor(CRIMSON)).move_to([-2.5,0.5,0])
        lig_arr=Arrow([-1.3,0.5,0],[-0.85,0.5,0],stroke_width=1.5,color=ManimColor(CRIMSON),buff=0.05,max_tip_length_to_length_ratio=0.3)
        lig_stage=VGroup(ligands,lig_bg,lig_t,lig_arr)
        # Soft corona: dots at r=0.9
        soft_dots=VGroup(*[
            Dot([0.9*np.cos(a), 0.9*np.sin(a)+0.5, 0], radius=0.07, color=ManimColor(SLATE))
            for a in np.linspace(0,2*np.pi,12,endpoint=False)
        ])
        soft_bg=Rectangle(width=2.8,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,1.6,0])
        soft_t=Text("t<30s: albumin adsorbs (soft corona)",font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([3.0,1.6,0])
        soft_stage=VGroup(soft_dots,soft_bg,soft_t)
        # Hard corona: thicker outer ring
        hard_ring=Circle(radius=1.1,fill_opacity=0,stroke_width=6,stroke_color=ManimColor(SLATE))
        hard_ring.move_to([0,0.5,0])
        hard_bg=Rectangle(width=3.2,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,0.5,0])
        hard_t=Text("hard corona buries ligands (t<1 min)",font="Georgia",font_size=13,color=ManimColor(CRIMSON)).move_to([3.0,0.5,0])
        hard_stage=VGroup(hard_ring,hard_bg,hard_t)
        # Macrophage: simple Rectangle approaching from left (Gate A safe, no VMobject smoothly)
        mac_box=Rectangle(width=1.4,height=0.9,fill_color=ManimColor(SLATE),fill_opacity=0.5,stroke_width=1.5,stroke_color=ManimColor(INK),stroke_opacity=1.0)
        mac_box.move_to([-3.8,-0.5,0])
        mac_bg=Rectangle(width=1.8,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-3.8,-1.4,0])
        mac_t=Text("MPS CLEARANCE",font="Georgia",font_size=13,color=ManimColor(CRIMSON)).move_to([-3.8,-1.4,0])
        macrophage=VGroup(mac_box,mac_bg,mac_t)
        # Final annotation
        ann_bg=Rectangle(width=4.0,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-2.2,0])
        ann_t=Text("The cell sees the corona. Not your targeting ligands.",font="Georgia",font_size=14,color=ManimColor(CRIMSON)).move_to([0,-2.2,0])
        footer=Line([-5.0,-2.9,0],[-4.2,-2.9,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(np_stage))                                         # 1
        self.play(FadeIn(lig_stage))                                                       # 2
        self.play(FadeIn(soft_stage))                                                      # 3
        self.play(FadeIn(hard_stage))                                                      # 4
        self.play(FadeIn(macrophage))                                                      # 5
        self.play(FadeIn(ann_bg),FadeIn(ann_t))                                           # 6
        self.play(FadeIn(footer))                                                          # 7
