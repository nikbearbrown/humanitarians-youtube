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


class B04_PutPayoff(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title = Text("PUT OPTION: FLOOR YOUR DOWNSIDE", font="Georgia",
                     font_size=26, color=ManimColor(INK), weight=BOLD).move_to([0, 3.2, 0])
        # Map S∈[140,220] → x∈[-5.0,5.0]: scale=10/80=0.125 per dollar
        # Map profit∈[-30,55] → y∈[-2.8,2.5]: scale=5.3/85 per dollar
        K=170; S0=185; prem=5.16
        def s2x(S): return -5.0 + (S-140)/80*10.0
        def p2y(P): return -2.8 + (P+30)/85*5.3
        xK=s2x(K)      # = -1.25
        xBE=s2x(190.16) # = 1.27
        y0=p2y(0)       # = -0.93
        # Axes
        x_axis=Line([-5.2,-3.0,0],[5.2,-3.0,0],stroke_width=2,color=ManimColor(INK))
        zero_bg=Rectangle(width=10.5,height=0.04,fill_color=ManimColor(SLATE),fill_opacity=0.3,stroke_width=0,stroke_opacity=0).move_to([0,y0,0])
        zero_line=Line([-5.0,y0,0],[5.0,y0,0],stroke_width=1.5,color=ManimColor(SLATE))
        # Strike marker
        k_line=Line([xK,-3.0,0],[xK,2.5,0],stroke_width=1,color=ManimColor(SLATE))
        k_bg=Rectangle(width=0.7,height=0.25,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([xK-0.6,2.2,0])
        k_lbl=Text("K=170",font="Georgia",font_size=15,color=ManimColor(SLATE)).move_to([xK-0.6,2.2,0])
        # Put payoff net profit: at S=140: max(170-140,0)-5.16=24.84; at S>170: -5.16
        put_left=Line([s2x(140),p2y(24.84),0],[xK,p2y(-prem),0],stroke_width=3,color=ManimColor(CRIMSON))
        put_right=Line([xK,p2y(-prem),0],[s2x(220),p2y(-prem),0],stroke_width=3,color=ManimColor(CRIMSON))
        prem_bg=Rectangle(width=1.4,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,p2y(-prem)-0.25,0])
        prem_lbl=Text("-$5.16 prem",font="Georgia",font_size=14,color=ManimColor(CRIMSON)).move_to([3.0,p2y(-prem)-0.25,0])
        # Combined: floor=K-S0-prem=-20.16; slope up after K; end at S=220: 29.84
        comb_left=Line([s2x(140),p2y(-20.16),0],[xK,p2y(-20.16),0],stroke_width=3,color=ManimColor(GOLD))
        comb_right=Line([xK,p2y(-20.16),0],[s2x(220),p2y(29.84),0],stroke_width=3,color=ManimColor(GOLD))
        floor_bg=Rectangle(width=2.0,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-3.5,p2y(-20.16)-0.25,0])
        floor_lbl=Text("FLOOR: -$20.16/sh",font="Georgia",font_size=14,color=ManimColor(GOLD)).move_to([-3.5,p2y(-20.16)-0.25,0])
        be_bg=Rectangle(width=1.8,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([xBE+1.0,y0+0.8,0])
        be_lbl=Text("B/E: $190.16",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([xBE+1.0,y0+0.8,0])
        # Legend
        pc=Rectangle(width=0.3,height=0.12,fill_color=ManimColor(CRIMSON),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,2.2,0])
        pt=Text("PUT alone",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([3.8,2.2,0])
        gc=Rectangle(width=0.3,height=0.12,fill_color=ManimColor(GOLD),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,1.9,0])
        gt=Text("Protective put",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([3.95,1.9,0])
        legend=VGroup(pc,pt,gc,gt)
        s_lbl=Text("STOCK PRICE ($)",font="Georgia",font_size=15,color=ManimColor(SLATE)).move_to([0,-3.3,0])
        footer=Line([-5.0,-3.3,0],[-4.2,-3.3,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title), FadeIn(x_axis), FadeIn(zero_line), FadeIn(zero_bg))     # 1
        self.play(FadeIn(k_line), FadeIn(k_bg), FadeIn(k_lbl))                           # 2
        self.play(FadeIn(put_left), FadeIn(put_right), FadeIn(prem_bg), FadeIn(prem_lbl)) # 3
        self.play(FadeIn(comb_left), FadeIn(comb_right))                                  # 4
        self.play(FadeIn(floor_bg), FadeIn(floor_lbl), FadeIn(be_bg), FadeIn(be_lbl))    # 5
        self.play(FadeIn(legend), FadeIn(s_lbl))                                          # 6
        self.play(FadeIn(footer))                                                          # 7
