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


class B04_ADCMechanism(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        PASS_CLR="#2A7A2A"
        title=Text("T-DM1 vs T-DXd: THE LINKER THAT CHANGED PATIENTS",font="Georgia",
                   font_size=20,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        # Divider — stops at y=-2.0 so annotation below is not intersected
        div=Line([0,-2.0,0],[0,2.8,0],stroke_width=1.5,color=ManimColor(SLATE))
        # Panel titles
        tdm1_bg=Rectangle(width=2.4,height=0.32,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-2.8,2.5,0])
        tdm1_t=Text("T-DM1 (non-cleavable)",font="Georgia",font_size=16,color=ManimColor(INK),weight=BOLD).move_to([-2.8,2.5,0])
        tdxd_bg=Rectangle(width=2.4,height=0.32,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([2.8,2.5,0])
        tdxd_t=Text("T-DXd (cleavable)",font="Georgia",font_size=16,color=ManimColor(GOLD),weight=BOLD).move_to([2.8,2.5,0])
        # 3 cells on each side: HER2-high (y=1.2), HER2-low (y=0.0), HER2-neg (y=-1.2)
        cell_data=[("HER2-HIGH",1.2,0.70),("HER2-LOW",0.0,0.45),("HER2-NEG",-1.2,0.25)]
        CELL_R=0.38
        # Left cells (T-DM1)
        left_cells=[]; left_lbls=[]
        for name,cy,op in cell_data:
            c=Circle(radius=CELL_R,fill_color=ManimColor(SLATE),fill_opacity=op,stroke_width=1.5,stroke_color=ManimColor(INK))
            c.move_to([-3.0,cy,0])
            bg=Rectangle(width=1.2,height=0.22,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-4.5,cy,0])
            t=Text(name,font="Georgia",font_size=11,color=ManimColor(INK)).move_to([-4.5,cy,0])
            left_cells.append(c); left_lbls.append(VGroup(bg,t))
        # Right cells (T-DXd)
        right_cells=[]; right_lbls=[]
        for name,cy,op in cell_data:
            c=Circle(radius=CELL_R,fill_color=ManimColor(SLATE),fill_opacity=op,stroke_width=1.5,stroke_color=ManimColor(INK))
            c.move_to([3.0,cy,0])
            bg=Rectangle(width=1.2,height=0.22,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([4.5,cy,0])
            t=Text(name,font="Georgia",font_size=11,color=ManimColor(INK)).move_to([4.5,cy,0])
            right_cells.append(c); right_lbls.append(VGroup(bg,t))
        # T-DM1: Arrow from top (ADC binding HER2-high only) + kill mark on HER2-high
        tdm1_adc=Arrow([-3.0,2.1,0],[-3.0,1.6,0],stroke_width=2,color=ManimColor(INK),buff=0.05,max_tip_length_to_length_ratio=0.3)
        # Kill HER2-high cell (green check)
        kill_bg_L=Rectangle(width=0.3,height=0.3,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-3.0,1.2,0])
        kill_L=Text("V",font="Georgia",font_size=22,color=ManimColor(PASS_CLR)).move_to([-3.0,1.2,0])
        # X marks on HER2-low and HER2-neg (can't kill)
        lock_bg1=Rectangle(width=0.3,height=0.3,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-3.0,0.0,0])
        lock1=Text("X",font="Georgia",font_size=22,color=ManimColor(CRIMSON)).move_to([-3.0,0.0,0])
        lock_bg2=Rectangle(width=0.3,height=0.3,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-3.0,-1.2,0])
        lock2=Text("X",font="Georgia",font_size=22,color=ManimColor(CRIMSON)).move_to([-3.0,-1.2,0])
        tdm1_results=VGroup(kill_bg_L,kill_L,lock_bg1,lock1,lock_bg2,lock2)
        # T-DXd: Arrow + bystander diffusion arrows + kill all 3
        tdxd_adc=Arrow([3.0,2.1,0],[3.0,1.6,0],stroke_width=2,color=ManimColor(GOLD),buff=0.05,max_tip_length_to_length_ratio=0.3)
        # Bystander arrows from HER2-high cell downward (payload diffuses)
        byst1=Arrow([3.0,0.82,0],[3.0,0.40,0],stroke_width=1.5,color=ManimColor(GOLD),buff=0.0,max_tip_length_to_length_ratio=0.3)
        byst2=Arrow([3.0,-0.38,0],[3.0,-0.80,0],stroke_width=1.5,color=ManimColor(GOLD),buff=0.0,max_tip_length_to_length_ratio=0.3)
        byst_lbl_bg=Rectangle(width=2.4,height=0.22,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([4.8,0.21,0])
        byst_lbl=Text("DXd diffuses to neighbors",font="Georgia",font_size=12,color=ManimColor(GOLD)).move_to([4.8,0.21,0])
        bystander=VGroup(byst1,byst2,byst_lbl_bg,byst_lbl)
        # Kill all 3 on T-DXd side
        kR1_bg=Rectangle(width=0.3,height=0.3,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,1.2,0])
        kR1=Text("V",font="Georgia",font_size=22,color=ManimColor(PASS_CLR)).move_to([3.0,1.2,0])
        kR2_bg=Rectangle(width=0.3,height=0.3,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,0.0,0])
        kR2=Text("V",font="Georgia",font_size=22,color=ManimColor(PASS_CLR)).move_to([3.0,0.0,0])
        kR3_bg=Rectangle(width=0.3,height=0.3,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,-1.2,0])
        kR3=Text("V",font="Georgia",font_size=22,color=ManimColor(PASS_CLR)).move_to([3.0,-1.2,0])
        tdxd_results=VGroup(kR1_bg,kR1,kR2_bg,kR2,kR3_bg,kR3)
        # DESTINY-Breast04 annotation
        dest_bg=Rectangle(width=4.5,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-2.5,0])
        dest_t=Text("DESTINY-Breast04 (2022): HER2-low = new targetable entity",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([0,-2.5,0])
        footer=Line([-5.0,-3.1,0],[-4.2,-3.1,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(div),FadeIn(tdm1_bg),FadeIn(tdm1_t),FadeIn(tdxd_bg),FadeIn(tdxd_t))  # 1
        self.play(FadeIn(VGroup(*left_cells)),FadeIn(VGroup(*left_lbls)),
                  FadeIn(VGroup(*right_cells)),FadeIn(VGroup(*right_lbls)))                                    # 2
        self.play(FadeIn(tdm1_adc),FadeIn(tdxd_adc))                                                         # 3
        self.play(FadeIn(tdm1_results))                                                                       # 4
        self.play(FadeIn(bystander),FadeIn(tdxd_results))                                                     # 5
        self.play(FadeIn(dest_bg),FadeIn(dest_t))                                                             # 6
        self.play(FadeIn(footer))                                                                              # 7
