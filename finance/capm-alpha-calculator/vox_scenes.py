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


class B04_AlphaBars(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("NVDA ALPHA: CAPM EXPECTED VS ACTUAL",font="Georgia",
                   font_size=22,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        BASE_Y=-1.8; SCALE=0.04; BAR_W=0.5
        # CAPM expected = 14.4% for all windows (beta=1.7, ERP=6%, rf=4.2% -> CAPM=14.4%)
        CAPM=14.4; capm_h=CAPM*SCALE
        x_axis=Line([-5.5,BASE_Y,0],[5.5,BASE_Y,0],stroke_width=2,color=ManimColor(INK))
        y_axis=Line([-5.5,BASE_Y,0],[-5.5,2.5,0],stroke_width=2,color=ManimColor(INK))
        GROUPS=[(-3.5,82.0,"24-MONTH","R2=0.70"),
                (0.0, 78.0,"36-MONTH","R2=0.68"),
                (3.5, 45.0,"60-MONTH","R2=0.62")]
        grp_vgs=[]
        for gx,actual,lbl_txt,r2_txt in GROUPS:
            act_h=actual*SCALE
            alpha_h=(actual-CAPM)*SCALE
            # CAPM bar
            cb=Rectangle(width=BAR_W,height=capm_h,fill_color=ManimColor(SLATE),fill_opacity=0.85,stroke_width=0,stroke_opacity=0)
            cb.move_to([gx-0.3,BASE_Y+capm_h/2,0])
            # Actual bar
            ab=Rectangle(width=BAR_W,height=act_h,fill_color=ManimColor(GOLD),fill_opacity=1.0,stroke_width=0,stroke_opacity=0)
            ab.move_to([gx+0.3,BASE_Y+act_h/2,0])
            # Alpha shading (CRIMSON overlay on actual bar above CAPM level)
            ash=Rectangle(width=BAR_W,height=alpha_h,fill_color=ManimColor(CRIMSON),fill_opacity=0.35,stroke_width=0,stroke_opacity=0)
            ash.move_to([gx+0.3,BASE_Y+capm_h+alpha_h/2,0])
            # Group label
            gl=Text(lbl_txt,font="Georgia",font_size=14,color=ManimColor(SLATE)).move_to([gx,BASE_Y-0.35,0])
            # Alpha value label above actual bar
            alpha_val=actual-CAPM
            al_bg=Rectangle(width=1.4,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([gx+0.3,BASE_Y+act_h+0.3,0])
            al_t=Text(f"+{alpha_val:.0f}pp a",font="Georgia",font_size=14,color=ManimColor(CRIMSON)).move_to([gx+0.3,BASE_Y+act_h+0.3,0])
            # R2 label
            r2_bg=Rectangle(width=1.3,height=0.24,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([gx,BASE_Y-0.65,0])
            r2_t=Text(r2_txt,font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([gx,BASE_Y-0.65,0])
            grp_vgs.append(VGroup(cb,ab,ash,gl,al_bg,al_t,r2_bg,r2_t))
        # Legend
        lb=Rectangle(width=0.3,height=0.18,fill_color=ManimColor(GOLD),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.6,2.4,0])
        lt=Text("Actual return",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([4.5,2.4,0])
        sb=Rectangle(width=0.3,height=0.18,fill_color=ManimColor(SLATE),fill_opacity=0.85,stroke_width=0,stroke_opacity=0).move_to([3.6,2.1,0])
        st=Text("CAPM expected",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([4.6,2.1,0])
        legend=VGroup(lb,lt,sb,st)
        footer=Line([-5.5,-3.0,0],[-4.7,-3.0,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(x_axis),FadeIn(y_axis))    # 1
        self.play(FadeIn(grp_vgs[0]))                              # 2
        self.play(FadeIn(grp_vgs[1]))                              # 3
        self.play(FadeIn(grp_vgs[2]))                              # 4
        self.play(FadeIn(legend))                                   # 5
        self.play(FadeIn(footer))                                   # 6
