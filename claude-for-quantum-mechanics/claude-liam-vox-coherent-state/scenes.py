import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def gauss(mu=0,sig=1,amp=2,color=TEAL): return FunctionGraph(lambda x:amp*np.exp(-((x-mu)**2)/(2*sig**2)),x_range=[-6,6],color=color,stroke_width=5)
def bowl(): return FunctionGraph(lambda x:.11*x*x-2.2,x_range=[-6,6],color=INK,stroke_width=4)

class B02_FreeSpread(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg(),ttl("A FREE GAUSSIAN SPREADS")); narrow=gauss(-3,.65,2.2,TEAL); wide=gauss(3,1.5,1.15,CRIMSON); arr=Arrow(LEFT*.8,RIGHT*.8,color=SLATE,buff=0); labs=VGroup(Text("t = 0",font=MONO,font_size=27,color=TEAL).move_to(LEFT*3+DOWN*2),Text("later",font=MONO,font_size=27,color=CRIMSON).move_to(RIGHT*3+DOWN*2)); self.play(Create(narrow),GrowArrow(arr),Create(wide),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B03_InBowl(Scene):
 def construct(self):
  d=DUR.get("B03",7); self.add(bg(),ttl("PUT A GROUND-WIDTH GAUSSIAN IN A PARABOLIC WELL")); p=bowl(); g=gauss(-2,.7,1.6,CRIMSON).shift(DOWN*1.55); lab=Text("V(x) = 1/2 m omega^2 x^2",font=MONO,font_size=29,color=INK).move_to(UP*2.1); self.play(Create(p),FadeIn(g,lab),run_time=1); self.wait(max(.1,d-1))
class B04_Center(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg(),ttl("THE CENTER FOLLOWS THE CLASSICAL EQUATION")); eqs=VGroup(Text("x_c'' + omega^2 x_c = 0",font=MONO,font_size=42,color=CRIMSON),Text("x_c(t) = A cos(omega t + delta)",font=MONO,font_size=36,color=INK)).arrange(DOWN,buff=.8); path=Line(LEFT*4,RIGHT*4,color=SLATE).move_to(DOWN*2); dot=Dot(LEFT*3+DOWN*2,radius=.22,color=TEAL); self.play(Write(eqs),Create(path),FadeIn(dot),run_time=1); self.play(dot.animate.move_to(RIGHT*3+DOWN*2),rate_func=there_and_back,run_time=min(2,d-1)); self.wait(max(.1,d-3))
class B05_Width(Scene):
 def construct(self):
  d=DUR.get("B05",10); self.add(bg(),ttl("CENTER MOTION IS NOT WIDTH MOTION")); gs=VGroup(gauss(-3,.7,1.5,TEAL),gauss(0,.7,1.5,TEAL),gauss(3,.7,1.5,TEAL)); eq=Text("sigma_x = sqrt[hbar / (2 m omega)]",font=MONO,font_size=38,color=CRIMSON).move_to(DOWN*2.3); marks=VGroup(*[DoubleArrow(np.array([x-.7,-.4,0]),np.array([x+.7,-.4,0]),color=INK,buff=0) for x in [-3,0,3]]); self.play(FadeIn(gs,marks,eq),run_time=1); self.wait(max(.1,d-1))
class B06_PhaseSpace(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg(),ttl("HARMONIC EVOLUTION IS A RIGID ROTATION")); axes=VGroup(Line(LEFT*4,RIGHT*4,color=SLATE),Line(DOWN*2.7,UP*2.7,color=SLATE)); orbit=Circle(radius=2,color=INK); patch=Circle(radius=.45,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.15).move_to(RIGHT*2); arr=CurvedArrow(RIGHT*2+UP*.7,UP*2+RIGHT*.7,color=TEAL); labs=VGroup(Text("scaled position",font=MONO,font_size=22,color=INK).move_to(RIGHT*5.3+DOWN*.35),Text("scaled momentum",font=MONO,font_size=22,color=INK).rotate(PI/2).move_to(LEFT*.45+UP*3)); self.play(Create(axes),Create(orbit),FadeIn(patch,labs,arr),run_time=1); self.wait(max(.1,d-1))
class B07_Slosh(Scene):
 def construct(self):
  d=DUR.get("B07",9); self.add(bg(),ttl("THE GAUSSIAN SLIDES WITHOUT BROADENING"),bowl()); gs=VGroup(gauss(-3,.65,1.3,CRIMSON),gauss(0,.65,1.3,TEAL),gauss(3,.65,1.3,CRIMSON)).shift(DOWN*1.5); lab=Text("same sigma_x at every center",font=MONO,font_size=29,color=INK).move_to(UP*2); self.play(LaggedStart(*[FadeIn(g) for g in gs],lag_ratio=.25),FadeIn(lab),run_time=1.5); self.wait(max(.1,d-1.5))
class B08_Uncertainty(Scene):
 def construct(self):
  d=DUR.get("B08",9); self.add(bg(),ttl("MINIMUM UNCERTAINTY AT EVERY TIME")); eq=Text("sigma_x sigma_p = hbar / 2",font=MONO,font_size=47,color=CRIMSON); note=Text("center moves · covariance stays fixed",font=SERIF,font_size=31,color=TEAL).move_to(DOWN*1.5); self.play(Write(eq),FadeIn(note),run_time=1); self.wait(max(.1,d-1))
class B09_Squeezed(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("A SQUEEZED STATE BREATHES")); a=Ellipse(width=3.8,height=1.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.12).move_to(LEFT*3); b=Ellipse(width=1.2,height=3.8,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.12).move_to(RIGHT*3); arr=Arrow(LEFT*.8,RIGHT*.8,color=TEAL,buff=0); labs=VGroup(Text("wide x",font=MONO,font_size=28,color=INK).move_to(LEFT*3+DOWN*2),Text("narrow x",font=MONO,font_size=28,color=INK).move_to(RIGHT*3+DOWN*2)); self.play(FadeIn(a,b,labs),GrowArrow(arr),run_time=1); self.wait(max(.1,d-1))
class B10_Anharmonic(Scene):
 def construct(self):
  d=DUR.get("B10",9); self.add(bg(),ttl("ANHARMONICITY SHEARS THE PACKET")); good=Circle(radius=1,color=TEAL).move_to(LEFT*3); bad=Polygon(RIGHT*2+LEFT*.8+UP,RIGHT*4+UP*.4,RIGHT*3.4+DOWN*1.2,RIGHT*1.8+DOWN*.5,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.12); arr=Arrow(LEFT*.8,RIGHT*.8,color=SLATE,buff=0); labs=VGroup(Text("rigid rotation",font=MONO,font_size=25,color=TEAL).move_to(LEFT*3+DOWN*2),Text("different rates -> shear",font=MONO,font_size=25,color=CRIMSON).move_to(RIGHT*3+DOWN*2)); self.play(FadeIn(good,bad,labs),GrowArrow(arr),run_time=1); self.wait(max(.1,d-1))
class B11_Light(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("THE SAME MATHEMATICS DESCRIBES ONE OPTICAL MODE")); wave=FunctionGraph(lambda x:.8*np.sin(2.5*x),x_range=[-5,5],color=CRIMSON,stroke_width=4); mode=Text("single-mode coherent light",font=MONO,font_size=32,color=INK).move_to(UP*2); caveat=Text("real lasers: loss · noise · multiple modes",font=SERIF,font_size=29,color=TEAL).move_to(DOWN*2.2); self.play(Create(wave),FadeIn(mode,caveat),run_time=1); self.wait(max(.1,d-1))
class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("THE LOCKED WIDTH",font=DISPLAY,font_size=35,color=TEAL).move_to(UP*2.3),Text("harmonic phase-space rotation",font=MONO,font_size=32,color=INK).move_to(UP*.7),Text("+ circular ground-state covariance",font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*.5),Text("= motion without spreading",font=MONO,font_size=40,color=TEAL).move_to(DOWN*2)); self.wait(d)
