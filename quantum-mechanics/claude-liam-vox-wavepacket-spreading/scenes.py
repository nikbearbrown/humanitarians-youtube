import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in _BS["beats"]})
except Exception:
    pass

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0,opacity=0)
def graph(origin, xs, ys, color=TEAL, width=4):
    m=VMobject(color=color,stroke_width=width)
    m.set_points_smoothly([origin+RIGHT*x+UP*y for x,y in zip(xs,ys)])
    return m
def gaussian(origin, center, sigma, height, color=TEAL):
    xs=np.linspace(-5.2,5.2,160); ys=height*np.exp(-((xs-center)/sigma)**2)
    return graph(origin,xs,ys,color)

class B02_Superposition(Scene):
    def construct(self):
        duration=DUR.get("B02",13); self.add(bg())
        title=Text("LOCALIZATION REQUIRES MANY WAVES",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35)
        waves=VGroup()
        for i,k in enumerate((1.8,2.05,2.3,2.55)):
            y=2.0-i*.75
            waves.add(ParametricFunction(lambda x,k=k,y=y: np.array([x,y+.18*np.sin(k*x),0]),t_range=[-6,1.5,.04],color=SLATE,stroke_width=2))
        o=LEFT*.5+DOWN*1.8; xs=np.linspace(-.5,6.2,150); env=np.exp(-((xs-2.4)/1.0)**2); ys=1.35*env*np.cos(8*(xs-2.4))
        packet=graph(o,xs,ys,TEAL,4)
        bracket=Brace(waves,RIGHT,color=CRIMSON); plus=Text("ADD PHASES",font=DISPLAY,font_size=20,color=CRIMSON).next_to(bracket,RIGHT)
        self.play(FadeIn(title),LaggedStart(*[Create(w) for w in waves],lag_ratio=.15),run_time=2)
        self.play(Create(bracket),FadeIn(plus),run_time=.6); self.play(Create(packet),run_time=1.8)
        self.wait(max(.1,duration-4.4))

class B03_RigidCounterfactual(Scene):
    def construct(self):
        duration=DUR.get("B03",13); self.add(bg())
        title=Text("IF EVERY COMPONENT HAD THE SAME SPEED…",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.3)
        axis=Line(LEFT*6,RIGHT*6,color=INK).move_to(DOWN*1.6)
        p0=gaussian(LEFT*5+DOWN*1.6,0,1.1,3.2,TEAL); p1=p0.copy().shift(RIGHT*6)
        shape=Text("same width • same height",font=MONO,font_size=23,color=TEAL).move_to(DOWN*2.5)
        verdict=Text("That would be a non-dispersive packet.",font=SERIF,font_size=27,color=INK).move_to(UP*2.2)
        self.play(FadeIn(title),Create(axis),Create(p0),run_time=1.1)
        self.play(Transform(p0,p1),run_time=3); self.play(FadeIn(shape),FadeIn(verdict),run_time=.7)
        self.wait(max(.1,duration-4.8))

class B04_DispersionRelation(Scene):
    def construct(self):
        duration=DUR.get("B04",16); self.add(bg())
        title=Text("FREE PARTICLE:  ω ∝ k²",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35)
        o=LEFT*5+DOWN*2.5; axes=VGroup(Line(o,o+RIGHT*10,color=INK),Line(o,o+UP*5,color=INK))
        xs=np.linspace(0,9.3,120); ys=.055*xs**2; parabola=graph(o,xs,ys,TEAL)
        ks=(2.8,5.2,7.7); dots=VGroup(*[Dot(o+RIGHT*k+UP*(.055*k*k),color=CRIMSON) for k in ks])
        slopes=VGroup(*[Line(LEFT*.8,RIGHT*.8,color=CRIMSON).rotate(np.arctan(.11*k)).move_to(o+RIGHT*k+UP*(.055*k*k)) for k in ks])
        lab=Text("v_g = dω/dk = ℏk/m",font=MONO,font_size=29,color=INK).move_to(RIGHT*3+DOWN*3.15)
        speeds=Text("larger k  →  steeper slope  →  faster",font=SERIF,font_size=25,color=CRIMSON).move_to(UP*2.6)
        self.play(FadeIn(title),Create(axes),run_time=.7); self.play(Create(parabola),run_time=1.8)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots],lag_ratio=.2),LaggedStart(*[Create(s) for s in slopes],lag_ratio=.2),run_time=1.5)
        self.play(Write(lab),FadeIn(speeds),run_time=.8); self.wait(max(.1,duration-4.8))

class B05_Mechanism(Scene):
    def construct(self):
        d=DUR.get("B05",3); self.add(bg(),RoundedRectangle(width=12,height=1.6,corner_radius=.12).set_fill(TEAL,.07).set_stroke(TEAL,2),Text("DIFFERENT MOMENTA • DIFFERENT SPEEDS",font=DISPLAY,font_size=35,color=INK)); self.wait(d)

class B06_ComponentFan(Scene):
    def construct(self):
        duration=DUR.get("B06",14); self.add(bg())
        title=Text("THE MOMENTUM COMPONENTS FAN APART",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35)
        axis=Line(LEFT*6,RIGHT*6,color=INK).move_to(DOWN*1.6)
        start=LEFT*5+DOWN*1.6
        dots=VGroup(Dot(start,color=SLATE),Dot(start,color=TEAL),Dot(start,color=CRIMSON))
        labels=VGroup(Text("slow",font=MONO,font_size=20,color=SLATE),Text("mean",font=MONO,font_size=20,color=TEAL),Text("fast",font=MONO,font_size=20,color=CRIMSON))
        ends=(LEFT*1.8+DOWN*1.6,RIGHT*.8+DOWN*1.6,RIGHT*4.5+DOWN*1.6)
        arrows=VGroup(*[Arrow(start+UP*.25,e+UP*.25,color=c,buff=.15,stroke_width=3) for e,c in zip(ends,(SLATE,TEAL,CRIMSON))])
        packet0=gaussian(LEFT*5+DOWN*1.6,0,.8,3,TEAL); packet1=gaussian(LEFT*1+DOWN*1.6,1.4,2.2,1.45,TEAL)
        self.play(FadeIn(title),Create(axis),Create(packet0),run_time=1)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.2),run_time=1.4)
        self.play(*[dots[i].animate.move_to(ends[i]) for i in range(3)],Transform(packet0,packet1),run_time=3)
        for i,l in enumerate(labels): l.next_to(dots[i],DOWN,buff=.2)
        self.play(FadeIn(labels),run_time=.5); self.wait(max(.1,duration-5.9))

class B07_ProbabilityBroadens(Scene):
    def construct(self):
        duration=DUR.get("B07",13); self.add(bg())
        title=Text("PROBABILITY IS CONSERVED; WIDTH IS NOT",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35)
        o=LEFT*5.5+DOWN*2.2; axis=Line(o,o+RIGHT*11,color=INK)
        narrow=gaussian(o,1.4,.75,4.2,TEAL); broad=gaussian(o,4.1,1.65,1.9,TEAL)
        a0=Text("area = 1",font=MONO,font_size=22,color=TEAL).move_to(LEFT*4.1+UP*2.1)
        a1=Text("area = 1",font=MONO,font_size=22,color=TEAL).move_to(RIGHT*1.1+UP*1.1)
        center=Arrow(o+RIGHT*1.4+UP*4.4,o+RIGHT*4.1+UP*2.2,color=CRIMSON,buff=.2)
        self.play(FadeIn(title),Create(axis),Create(narrow),FadeIn(a0),run_time=1.2)
        self.play(GrowArrow(center),Transform(narrow,broad),Transform(a0,a1),run_time=3)
        self.play(Indicate(narrow,color=TEAL),run_time=.8); self.wait(max(.1,duration-5))

class B08_Implication(Scene):
    def construct(self):
        d=DUR.get("B08",3); self.add(bg(),Text("THE CENTER TRAVELS.  THE CLOUD SPREADS.",font=DISPLAY,font_size=36,color=INK)); self.wait(d)

class B09_DispersionNotDiffusion(Scene):
    def construct(self):
        duration=DUR.get("B09",15); self.add(bg())
        title=Text("DISPERSION ≠ DIFFUSION",font=DISPLAY,font_size=32,color=INK).move_to(UP*3.35)
        divider=Line(UP*2.8,DOWN*2.8,color=INK,stroke_opacity=.3)
        left=RoundedRectangle(width=7,height=5.2,corner_radius=.15).set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(LEFT*3.8)
        right=RoundedRectangle(width=7,height=5.2,corner_radius=.15).set_fill(CRIMSON,.05).set_stroke(CRIMSON,2).move_to(RIGHT*3.8)
        lt=Text("COHERENT DISPERSION",font=DISPLAY,font_size=24,color=TEAL).move_to(LEFT*3.8+UP*2)
        rt=Text("RANDOM DIFFUSION",font=DISPLAY,font_size=24,color=CRIMSON).move_to(RIGHT*3.8+UP*2)
        ll=Text("unitary evolution\nno collisions\nphases determine width",font=SERIF,font_size=25,color=INK,line_spacing=1.35).move_to(LEFT*3.8)
        rr=Text("environmental kicks\nstochastic paths\nnoise drives width",font=SERIF,font_size=25,color=INK,line_spacing=1.35).move_to(RIGHT*3.8)
        cause=Text("Here: curvature of E(k), not an environment",font=MONO,font_size=23,color=TEAL).move_to(DOWN*3.25)
        self.play(FadeIn(title),Create(divider),FadeIn(left),FadeIn(right),run_time=.8)
        self.play(FadeIn(lt),FadeIn(rt),Write(ll),Write(rr),run_time=1.5); self.play(FadeIn(cause),run_time=.5)
        self.wait(max(.1,duration-2.8))

class B10_ThreeTimes(Scene):
    def construct(self):
        duration=DUR.get("B10",16); self.add(bg())
        title=Text("ONE PACKET • THREE TIMES • EQUAL AREA",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35)
        o=LEFT*6+DOWN*2.5; axis=Line(o,o+RIGHT*12,color=INK)
        c0=gaussian(o,1.0,.65,4.2,CRIMSON); c1=gaussian(o,3.0,1.1,2.45,SLATE); c2=gaussian(o,4.6,1.65,1.75,TEAL)
        labels=VGroup(Text("t = 0",font=MONO,font_size=21,color=CRIMSON).move_to(LEFT*5+UP*2.1),Text("t = 1",font=MONO,font_size=21,color=SLATE).move_to(LEFT*2.8+UP*.8),Text("t = 2",font=MONO,font_size=21,color=TEAL).move_to(LEFT*.9+UP*.25))
        widths=Text("peak ↓     center →     width ↑",font=DISPLAY,font_size=26,color=INK).move_to(DOWN*3.25)
        self.play(FadeIn(title),Create(axis),run_time=.6); self.play(Create(c0),FadeIn(labels[0]),run_time=1.2)
        self.play(Create(c1),FadeIn(labels[1]),run_time=1.2); self.play(Create(c2),FadeIn(labels[2]),run_time=1.2)
        self.play(FadeIn(widths),run_time=.5); self.wait(max(.1,duration-4.7))

class B11_Recap(Scene):
    def construct(self):
        duration=DUR.get("B11",15); self.add(bg())
        title=Text("THE ANSWER",font=DISPLAY,font_size=22,color=TEAL).move_to(UP*2.8)
        box=RoundedRectangle(width=12.5,height=2.5,corner_radius=.12).set_fill(TEAL,.07).set_stroke(TEAL,2)
        ans=Text("Localization needs many momenta.\nDifferent momenta move at different speeds.",font=DISPLAY,font_size=31,color=INK,line_spacing=1.25)
        kicker=Text("NO FORCE NEEDED — FREE-PARTICLE DISPERSION",font=MONO,font_size=22,color=CRIMSON).move_to(DOWN*2.4)
        self.play(FadeIn(title),Create(box),run_time=.7); self.play(FadeIn(ans),FadeIn(kicker),run_time=.7); self.wait(max(.1,duration-1.4))
