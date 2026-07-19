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


class B04_VolatilityPaths(Scene):
    def construct(self):
        import numpy as np
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        title=Text("VOLATILITY DRAG: THE GEOMETRIC PENALTY",font="Georgia",
                   font_size=22,color=ManimColor(INK),weight=BOLD).move_to([0,3.2,0])
        N=60; MU=0.004; SIGMA=0.06
        # Map t->x in [-5.0,4.5], log-return->y
        # log-return range ~[-0.3, 0.45], map to y in [-2.8,2.2]
        def tx(t): return -5.0+t/N*9.5
        def ry(r): return -2.8+(r+0.30)/0.75*5.0
        # Stochastic paths
        path_vgs=[]
        for seed in range(14):
            rng=np.random.RandomState(seed*11+3)
            steps=rng.normal(MU,SIGMA,N)
            cum=np.concatenate([[0],np.cumsum(steps)])
            pts=[[tx(t), max(-3.0,min(2.5,ry(cum[t]))),0] for t in range(N+1)]
            segs=VGroup(*[Line(pts[i],pts[i+1],stroke_width=1.2,
                               color=ManimColor(SLATE),stroke_opacity=0.45)
                           for i in range(N)])
            path_vgs.append(segs)
        all_paths=VGroup(*path_vgs)
        # Deterministic path A (arithmetic mean, no variance penalty)
        det=[MU*t for t in range(N+1)]
        det_pts=[[tx(t),ry(det[t]),0] for t in range(N+1)]
        det_path=VGroup(*[Line(det_pts[i],det_pts[i+1],stroke_width=3.5,color=ManimColor(INK))
                           for i in range(N)])
        # Geometric/median end: mu*N - sigma^2/2 * N
        geo_end=MU*N - SIGMA**2/2*N   # = 0.24 - 0.108 = 0.132
        det_end=MU*N                   # = 0.24
        drag_gap=det_end-geo_end        # = 0.108
        # Drag annotation at x=tx(N)=4.5
        y_geo=ry(geo_end); y_det=ry(det_end)
        drag_arr=Line([4.0,y_geo,0],[4.0,y_det,0],stroke_width=2.5,color=ManimColor(CRIMSON))
        drag_bg=Rectangle(width=2.6,height=0.55,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([1.8,(y_geo+y_det)/2,0])
        drag_t=Text(f"DRAG: s2/2*t\n= {drag_gap:.2f}",font="Georgia",font_size=14,color=ManimColor(CRIMSON)).move_to([1.8,(y_geo+y_det)/2,0])
        # Axes
        x_axis=Line([-5.2,-3.0,0],[5.0,-3.0,0],stroke_width=2,color=ManimColor(INK))
        y_axis=Line([-5.2,-3.0,0],[-5.2,2.5,0],stroke_width=2,color=ManimColor(INK))
        # Legend — placed in the title row (far right of title, no path overlap)
        legend=VGroup()
        xl_bg=Rectangle(width=1.5,height=0.24,fill_color=ManimColor(CREAM),fill_opacity=1.0,stroke_width=0,stroke_opacity=0).move_to([0,-3.3,0])
        xl=Text("TIME (days)",font="Georgia",font_size=14,color=ManimColor(SLATE)).move_to([0,-3.3,0])
        footer=Line([-5.2,-3.3,0],[-4.4,-3.3,0],stroke_width=2,color=ManimColor(CRIMSON))
        self.play(FadeIn(title),FadeIn(x_axis),FadeIn(y_axis),FadeIn(xl_bg),FadeIn(xl))  # 1
        self.play(FadeIn(all_paths))                                                       # 2
        self.play(FadeIn(det_path))                                                        # 3
        self.play(FadeIn(drag_arr),FadeIn(drag_bg),FadeIn(drag_t))                        # 4
        self.play(FadeIn(legend))                                                          # 5
        self.play(FadeIn(footer))                                                          # 6
