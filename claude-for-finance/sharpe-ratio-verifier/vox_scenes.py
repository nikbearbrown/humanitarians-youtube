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


class B04_SharpeBar(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title = Text("SHARPE RATIO: WINDOW VS. CONVENTION", font="Georgia",
                     font_size=26, color=ManimColor(INK), weight=BOLD).move_to([0, 3.2, 0])
        x_axis = Line([-5.5, -2.0, 0], [5.5, -2.0, 0], stroke_width=2, color=ManimColor(INK))
        y_axis = Line([-5.5, -2.0, 0], [-5.5, 2.5, 0], stroke_width=2, color=ManimColor(INK))
        BASE_Y = -2.0; SCALE = 1.5; BAR_W = 0.55
        G1_X = -2.5; G2_X = 2.5
        # Values: NVDA Sharpe 3yr=1.52, 5yr=1.15 / SPY 3yr=0.52, 5yr=0.45
        def bar(cx, val, clr):
            h = val * SCALE
            r = Rectangle(width=BAR_W, height=h, fill_color=ManimColor(clr),
                           fill_opacity=1.0, stroke_width=0, stroke_opacity=0)
            r.move_to([cx, BASE_Y + h/2, 0])
            return r
        b_n3 = bar(G1_X-0.3, 1.52, GOLD); b_s3 = bar(G1_X+0.3, 0.52, SLATE)
        b_n5 = bar(G2_X-0.3, 1.15, GOLD); b_s5 = bar(G2_X+0.3, 0.45, SLATE)
        def val_lbl(cx, val, txt):
            y = BASE_Y + val*SCALE + 0.35
            bg = Rectangle(width=0.8, height=0.32, fill_color=ManimColor(CREAM),
                            fill_opacity=1.0, stroke_width=0, stroke_opacity=0).move_to([cx, y, 0])
            t = Text(txt, font="Georgia", font_size=17, color=ManimColor(INK)).move_to([cx, y, 0])
            return VGroup(bg, t)
        lbl_n3=val_lbl(G1_X-0.3,1.52,"1.52"); lbl_s3=val_lbl(G1_X+0.3,0.52,"0.52")
        lbl_n5=val_lbl(G2_X-0.3,1.15,"1.15"); lbl_s5=val_lbl(G2_X+0.3,0.45,"0.45")
        grp1=Text("3-YEAR",font="Georgia",font_size=18,color=ManimColor(SLATE)).move_to([G1_X,-2.45,0])
        grp2=Text("5-YEAR",font="Georgia",font_size=18,color=ManimColor(SLATE)).move_to([G2_X,-2.45,0])
        # Legend
        nb=Rectangle(width=0.3,height=0.2,fill_color=ManimColor(GOLD),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.5,2.0,0])
        nt=Text("NVDA",font="Georgia",font_size=16,color=ManimColor(INK)).move_to([4.1,2.0,0])
        sb=Rectangle(width=0.3,height=0.2,fill_color=ManimColor(SLATE),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.5,1.6,0])
        st=Text("SPY",font="Georgia",font_size=16,color=ManimColor(INK)).move_to([4.0,1.6,0])
        legend=VGroup(nb,nt,sb,st)
        # "AI Rally" annotation arrow above NVDA 3yr bar
        # NVDA_3yr top y = BASE_Y + 1.52*SCALE = -2.0+2.28 = 0.28
        arr_tip=[G1_X-0.3, 0.18, 0]; arr_base=[G1_X+0.5, 1.0, 0]
        arrow=Arrow(arr_base, arr_tip, stroke_width=2, color=ManimColor(CRIMSON),
                    buff=0.05, max_tip_length_to_length_ratio=0.2)
        ann_bg=Rectangle(width=1.4,height=0.28,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([G1_X+0.5,1.0,0])
        ann_t=Text("AI RALLY",font="Georgia",font_size=15,color=ManimColor(CRIMSON)).move_to([G1_X+0.5,1.0,0])
        annotation=VGroup(arrow,ann_bg,ann_t)
        x_lbl=Text("WINDOW",font="Georgia",font_size=16,color=ManimColor(SLATE)).move_to([0,-2.8,0])
        y_lbl=Text("SHARPE",font="Georgia",font_size=16,color=ManimColor(SLATE)).move_to([-5.2,0.5,0])
        footer=Line([-5.5,-3.1,0],[-4.7,-3.1,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title), FadeIn(x_axis), FadeIn(y_axis))                          # 1
        self.play(FadeIn(b_n3), FadeIn(b_n5))                                             # 2
        self.play(FadeIn(b_s3), FadeIn(b_s5))                                             # 3
        self.play(FadeIn(lbl_n3), FadeIn(lbl_s3), FadeIn(lbl_n5), FadeIn(lbl_s5))        # 4
        self.play(FadeIn(grp1), FadeIn(grp2), FadeIn(legend))                             # 5
        self.play(FadeIn(annotation))                                                      # 6
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), FadeIn(footer))                          # 7
