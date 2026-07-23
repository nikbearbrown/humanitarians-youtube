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


class B04_CorrelationPanels(Scene):
    def construct(self):
        import numpy as np
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("CORRELATION SPIKES WHEN YOU NEED IT LOWEST",font="Georgia",
                   font_size=20,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        N=60  # time steps (5 years simplified)
        # Map t->x
        def tx(t): return -5.0+t/N*9.5
        # Upper panel (correlation): y in [0.3,2.5], c in [0.4,1.0]
        def cy(c): return 0.3+(c-0.4)/0.6*2.2
        # Lower panel (vol): y in [-3.0,-0.5], v in [0.10,0.50]
        def vy(v): return -3.0+(v-0.10)/0.40*2.5
        # Simplified time series
        corr=np.full(N+1,0.65)
        pvol=np.full(N+1,0.20)
        avol=np.full(N+1,0.28)  # simple average vol (constant reference)
        # Stress period: t=38..50
        stress_start,stress_end=38,50
        for t in range(N+1):
            if stress_start<=t<=stress_end:
                c=0.65+0.27*np.sin(np.pi*(t-stress_start)/(stress_end-stress_start))
                corr[t]=c
                pvol[t]=0.20+0.28*np.sin(np.pi*(t-stress_start)/(stress_end-stress_start))
        # Separator line
        sep=Line([-5.2,0.1,0],[5.0,0.1,0],stroke_width=1,color=ManimColor(SLATE))
        # Stress zone highlight (both panels)
        xs=tx(stress_start); xe=tx(stress_end)
        stress_upper=Rectangle(width=xe-xs,height=2.2,fill_color=ManimColor(CRIMSON),fill_opacity=0.08,stroke_width=0,stroke_opacity=0)
        stress_upper.move_to([(xs+xe)/2,1.4,0])
        stress_lower=Rectangle(width=xe-xs,height=2.5,fill_color=ManimColor(CRIMSON),fill_opacity=0.08,stroke_width=0,stroke_opacity=0)
        stress_lower.move_to([(xs+xe)/2,-1.75,0])
        stress_zones=VGroup(stress_upper,stress_lower)
        # Correlation line
        corr_pts=[[tx(t),cy(corr[t]),0] for t in range(N+1)]
        corr_segs=VGroup(*[Line(corr_pts[i],corr_pts[i+1],stroke_width=2.5,color=ManimColor(INK))
                            for i in range(N)])
        # Portfolio vol line
        pvol_pts=[[tx(t),vy(pvol[t]),0] for t in range(N+1)]
        pvol_segs=VGroup(*[Line(pvol_pts[i],pvol_pts[i+1],stroke_width=2.5,color=ManimColor(GOLD))
                            for i in range(N)])
        # Average vol reference line (constant)
        avol_line=Line([tx(0),vy(avol[0]),0],[tx(N),vy(avol[N]),0],
                        stroke_width=1.5,color=ManimColor(SLATE))
        # Panel labels — positioned away from lines using CREAM backgrounds
        cu_bg=Rectangle(width=2.0,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-4.0,2.3,0])
        cu_t=Text("ROLLING CORR",font="Georgia",font_size=14,color=ManimColor(INK)).move_to([-4.0,2.3,0])
        cl_bg=Rectangle(width=2.5,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([-3.8,-0.7,0])
        cl_t=Text("PORTFOLIO VOL",font="Georgia",font_size=14,color=ManimColor(GOLD)).move_to([-3.8,-0.7,0])
        av_bg=Rectangle(width=2.8,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([3.0,-2.6,0])
        av_t=Text("avg vol (naive)",font="Georgia",font_size=13,color=ManimColor(SLATE)).move_to([3.0,-2.6,0])
        # "Diversification collapses" annotation at stress peak
        peak_t=(stress_start+stress_end)//2
        ann_x=tx(peak_t); ann_cy=cy(corr[peak_t])
        ann_bg=Rectangle(width=3.0,height=0.26,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([ann_x-0.8,ann_cy+0.4,0])
        ann_t_lbl=Text("diversification collapses",font="Georgia",font_size=13,color=ManimColor(CRIMSON)).move_to([ann_x-0.8,ann_cy+0.4,0])
        stress_lbl_bg=Rectangle(width=1.2,height=0.24,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([ann_x,-0.2,0])
        stress_lbl=Text("2022",font="Georgia",font_size=13,color=ManimColor(CRIMSON)).move_to([ann_x,-0.2,0])
        footer=Line([-5.2,-3.3,0],[-4.4,-3.3,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(sep),FadeIn(cu_bg),FadeIn(cu_t),FadeIn(cl_bg),FadeIn(cl_t))   # 1
        self.play(FadeIn(stress_zones),FadeIn(stress_lbl_bg),FadeIn(stress_lbl))                      # 2
        self.play(FadeIn(corr_segs))                                                                   # 3
        self.play(FadeIn(pvol_segs),FadeIn(avol_line),FadeIn(av_bg),FadeIn(av_t))                    # 4
        self.play(FadeIn(ann_bg),FadeIn(ann_t_lbl))                                                   # 5
        self.play(FadeIn(footer))                                                                       # 6
