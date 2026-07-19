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


class B04_StagingTree(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("TNM + MOLECULAR MODIFIERS: THE DOWNGRADE",font="Georgia",
                   font_size=22,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        tnm=[("T2",1.5),("N0",0.3),("M0",-0.9)]
        tnm_nodes=VGroup(*[
            VGroup(
                Rectangle(width=0.9,height=0.55,fill_color=ManimColor(SLATE),fill_opacity=0.5,stroke_width=0,stroke_opacity=0).move_to([-4.5,ty,0]),
                Text(tt,font="Georgia",font_size=18,color=ManimColor(CREAM),weight=BOLD).move_to([-4.5,ty,0])
            ) for tt,ty in tnm
        ])
        anat_x=-1.3; anat_y=0.3
        tnm_arrows=VGroup(*[
            Arrow([-4.0,ty,0],[anat_x-0.7,anat_y,0],stroke_width=1.5,color=ManimColor(SLATE),
                   buff=0.05,max_tip_length_to_length_ratio=0.2)
            for _,ty in tnm
        ])
        anat_box=Rectangle(width=2.2,height=0.75,fill_color=ManimColor(SLATE),fill_opacity=0.4,stroke_width=1.5,stroke_color=ManimColor(INK),stroke_opacity=1.0)
        anat_box.move_to([anat_x,anat_y,0])
        anat_bg=Rectangle(width=2.2,height=0.75,fill_color=ManimColor(CREAM),fill_opacity=0.0,stroke_width=0,stroke_opacity=0).move_to([anat_x,anat_y,0])
        anat_t=Text("ANATOMIC\nSTAGE IIA",font="Georgia",font_size=15,color=ManimColor(INK),weight=BOLD).move_to([anat_x,anat_y,0])
        anat_stage=VGroup(anat_box,anat_bg,anat_t)
        mods=[("ER+",1.5),("HER2-",0.3),("Oncotype\nDX = 10",-0.9)]
        mod_x=1.5
        mod_nodes=VGroup(*[
            VGroup(
                Rectangle(width=1.5,height=0.55,fill_color=ManimColor(GOLD),fill_opacity=0.85,stroke_width=0,stroke_opacity=0).move_to([mod_x,my,0]),
                Text(mt,font="Georgia",font_size=14,color=ManimColor(INK)).move_to([mod_x,my,0])
            ) for mt,my in mods
        ])
        prog_x=3.8; prog_y=0.3
        anat_to_prog=Arrow([anat_x+1.1,anat_y,0],[prog_x-1.1,prog_y,0],stroke_width=2,color=ManimColor(GOLD),buff=0.05,max_tip_length_to_length_ratio=0.2)
        mod_arrows=VGroup(*[
            Arrow([mod_x+0.75,my,0],[prog_x-1.1,prog_y,0],stroke_width=1.5,color=ManimColor(GOLD),buff=0.05,max_tip_length_to_length_ratio=0.2)
            for _,my in mods
        ])
        prog_box=Rectangle(width=2.2,height=0.75,fill_color=ManimColor(GOLD),fill_opacity=1.0,stroke_width=0,stroke_opacity=0)
        prog_box.move_to([prog_x,prog_y,0])
        prog_t=Text("PROGNOSTIC\nSTAGE IA",font="Georgia",font_size=15,color=ManimColor(INK),weight=BOLD).move_to([prog_x,prog_y,0])
        prog_stage=VGroup(prog_box,prog_t)
        dn_bg=Rectangle(width=2.5,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([prog_x,-0.6,0])
        dn_t=Text("IIA -> IA downgrade",font="Georgia",font_size=14,color=ManimColor(GOLD),weight=BOLD).move_to([prog_x,-0.6,0])
        tx_bg=Rectangle(width=5.5,height=0.52,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-2.0,0])
        tx_t=Text("TAILORx trial: Oncotype DX <= 25 -> no chemotherapy benefit\nSame anatomy, different decision.",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([0,-2.0,0])
        footer=Line([-5.5,-2.8,0],[-4.7,-2.8,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(tnm_nodes))
        self.play(FadeIn(tnm_arrows),FadeIn(anat_stage))
        self.play(FadeIn(mod_nodes))
        self.play(FadeIn(mod_arrows),FadeIn(anat_to_prog),FadeIn(prog_stage))
        self.play(FadeIn(dn_bg),FadeIn(dn_t))
        self.play(FadeIn(tx_bg),FadeIn(tx_t))
        self.play(FadeIn(footer))
