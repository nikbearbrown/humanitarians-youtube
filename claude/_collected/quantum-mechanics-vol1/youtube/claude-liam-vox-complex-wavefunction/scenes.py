import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def sine(sign=1,y=0,col=TEAL):
 xs=np.linspace(-5,5,350); return VMobject(color=col,stroke_width=3).set_points_smoothly([np.array([x,.7*np.sin(sign*2.5*x)+y,0]) for x in xs])
def gauss(center=0,col=TEAL):
 xs=np.linspace(-6,6,350); return VMobject(color=col,stroke_width=4).set_points_smoothly([np.array([x,1.6*np.exp(-.5*((x-center)/1.5)**2),0]) for x in xs])

class B02_OppositeWinding(Scene):
 def construct(self):
  d=DUR.get("B02",11); self.add(bg(),ttl("SAME MAGNITUDE · OPPOSITE COMPLEX WINDING")); r=sine(1,1.3,TEAL); l=sine(-1,-1.3,CRIMSON); labs=VGroup(Text("exp(+ikx)  right-moving",font=MONO,font_size=25,color=TEAL).move_to(LEFT*3.5+UP*2.3),Text("exp(-ikx)  left-moving",font=MONO,font_size=25,color=CRIMSON).move_to(LEFT*3.5+DOWN*2.3)); arrows=VGroup(Arrow(RIGHT*3,RIGHT*5,color=TEAL,buff=0),Arrow(LEFT*3,LEFT*5,color=CRIMSON,buff=0)); self.play(Create(r),Create(l),FadeIn(labs),GrowFromCenter(arrows),run_time=1.2); self.wait(max(.1,d-1.2))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",6); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=23,color=SLATE).move_to(UP*2.3),Text("If |psi|^2 is identical,",font=SERIF,font_size=42,color=INK).move_to(UP*.5),Text("where does direction live?",font=SERIF,font_size=43,color=CRIMSON).move_to(DOWN*.9)); self.wait(d)

class B04_EqualDensity(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg(),ttl("MAGNITUDE SQUARED ERASES THE SIGN OF k")); eqs=VGroup(Text("|exp(+ikx)|^2 = 1",font=MONO,font_size=35,color=TEAL),Text("|exp(-ikx)|^2 = 1",font=MONO,font_size=35,color=CRIMSON),Text("same position density",font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.8); self.play(FadeIn(eqs[:2]),run_time=.8); self.play(FadeIn(eqs[2]),run_time=.7); self.wait(max(.1,d-1.5))

class B05_Phasors(Scene):
 def construct(self):
  d=DUR.get("B05",11); self.add(bg(),ttl("AS x INCREASES, THE PHASE ANGLE WINDS")); centers=[np.array([-4+i*2,1.2,0]) for i in range(5)]+[np.array([-4+i*2,-1.5,0]) for i in range(5)]; circles=VGroup(*[Circle(radius=.55,color=SLATE).move_to(c) for c in centers]); arrows=VGroup(*[Arrow(c,c+.45*np.array([np.cos(a),np.sin(a),0]),buff=0,color=TEAL if i<5 else CRIMSON) for i,(c,a) in enumerate(zip(centers,[0,.8,1.6,2.4,3.2,0,-.8,-1.6,-2.4,-3.2]))]); labs=VGroup(Text("+k: angle advances",font=MONO,font_size=24,color=TEAL).move_to(LEFT*4+UP*2.4),Text("-k: angle retreats",font=MONO,font_size=24,color=CRIMSON).move_to(LEFT*4+DOWN*2.7)); self.play(FadeIn(circles),GrowFromCenter(arrows),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))

class B06_PhaseGradient(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg(),ttl("AMPLITUDE AND PHASE CARRY DIFFERENT INFORMATION")); eq=Text("psi(x) = R(x) exp(i theta(x))",font=MONO,font_size=36,color=INK).move_to(UP*1.2); dens=Text("density = R(x)^2",font=MONO,font_size=31,color=TEAL).move_to(LEFT*3+DOWN*.8); flow=Text("direction from d theta/dx",font=MONO,font_size=29,color=CRIMSON).move_to(RIGHT*3+DOWN*.8); self.play(Write(eq),run_time=.8); self.play(FadeIn(dens,flow),run_time=.8); self.wait(max(.1,d-1.6))

class B07_Current(Scene):
 def construct(self):
  d=DUR.get("B07",12); self.add(bg(),ttl("PROBABILITY CURRENT REVEALS THE SIGN")); eq=Text("j = (hbar/m) Im[ psi* dpsi/dx ]",font=MONO,font_size=30,color=INK).move_to(UP*1.8); right=VGroup(Text("exp(+ikx)",font=MONO,font_size=28,color=TEAL),Arrow(LEFT*1.1,RIGHT*1.1,color=TEAL,buff=0),Text("j > 0",font=MONO,font_size=29,color=TEAL)).arrange(DOWN,buff=.5).move_to(LEFT*3.5+DOWN*.7); left=VGroup(Text("exp(-ikx)",font=MONO,font_size=28,color=CRIMSON),Arrow(RIGHT*1.1,LEFT*1.1,color=CRIMSON,buff=0),Text("j < 0",font=MONO,font_size=29,color=CRIMSON)).arrange(DOWN,buff=.5).move_to(RIGHT*3.5+DOWN*.7); self.play(Write(eq),run_time=.8); self.play(FadeIn(right,left),run_time=.9); self.wait(max(.1,d-1.7))

class B08_Cosine(Scene):
 def construct(self):
  d=DUR.get("B08",10); self.add(bg(),ttl("A REAL COSINE CONTAINS BOTH DIRECTIONS")); top=VGroup(Text("exp(+ikx)",font=MONO,font_size=27,color=TEAL),Text("+",font=SERIF,font_size=35,color=INK),Text("exp(-ikx)",font=MONO,font_size=27,color=CRIMSON)).arrange(RIGHT,buff=.5).move_to(UP*1.5); arr=Arrow(UP*.7,DOWN*.5,color=SLATE,buff=.1); result=Text("2 cos(kx)    =>    j = 0",font=MONO,font_size=35,color=INK).move_to(DOWN*1); note=Text("standing pattern",font=SERIF,font_size=28,color=SLATE).move_to(DOWN*2.3); self.play(FadeIn(top),GrowArrow(arr),run_time=.8); self.play(FadeIn(result,note),run_time=.8); self.wait(max(.1,d-1.6))

class B09_ReIm(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("REAL + IMAGINARY = A CONTINUOUS PHASE ANGLE")); axes=VGroup(Line(LEFT*2.2,RIGHT*2.2,color=SLATE),Line(DOWN*2.2,UP*2.2,color=SLATE)); arr=Arrow(ORIGIN,RIGHT*1.5+UP*1.2,color=CRIMSON,buff=0,stroke_width=6); labs=VGroup(Text("Re psi",font=MONO,font_size=24,color=INK).move_to(RIGHT*3),Text("Im psi",font=MONO,font_size=24,color=INK).move_to(UP*2.7),Text("phase carries flow",font=SERIF,font_size=31,color=TEAL).move_to(DOWN*2.8)); self.play(Create(axes),GrowArrow(arr),FadeIn(labs),run_time=1); self.play(Rotate(arr,angle=PI,about_point=ORIGIN),run_time=2); self.wait(max(.1,d-3))

class B10_Packets(Scene):
 def construct(self):
  d=DUR.get("B10",11); self.add(bg(),ttl("SAME ENVELOPE · OPPOSITE MEAN MOMENTUM")); g1=gauss(0,TEAL).shift(UP*1.25); g2=gauss(0,CRIMSON).shift(DOWN*1.25); arrows=VGroup(Arrow(LEFT*1.2,RIGHT*1.2,color=TEAL,buff=0).shift(UP*.8),Arrow(RIGHT*1.2,LEFT*1.2,color=CRIMSON,buff=0).shift(DOWN*.8)); labs=VGroup(Text("+ phase ramp",font=MONO,font_size=24,color=TEAL).move_to(LEFT*4+UP*2.1),Text("- phase ramp",font=MONO,font_size=24,color=CRIMSON).move_to(LEFT*4+DOWN*2.1),Text("same Gaussian |psi|^2",font=SERIF,font_size=28,color=INK).move_to(DOWN*3)); self.play(FadeIn(g1,g2),GrowFromCenter(arrows),FadeIn(labs),run_time=1.1); self.wait(max(.1,d-1.1))

class B11_Qualification(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("THE CAREFUL CLAIM")); yes=Text("A state may be real at one chosen instant.",font=SERIF,font_size=35,color=TEAL).move_to(UP*.9); but=Text("General evolution needs complex phase.",font=SERIF,font_size=36,color=CRIMSON).move_to(DOWN*.7); line=Line(LEFT*5,RIGHT*5,color=SLATE).move_to(ORIGIN); self.play(FadeIn(yes),run_time=.6); self.play(Create(line),FadeIn(but),run_time=.8); self.wait(max(.1,d-1.4))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("MAGNITUDE ANSWERS WHERE",font=DISPLAY,font_size=31,color=TEAL).move_to(UP*1.6),Text("COMPLEX PHASE ANSWERS HOW IT FLOWS",font=DISPLAY,font_size=31,color=CRIMSON),Text("left and right can share the same |psi|^2",font=SERIF,font_size=27,color=INK).move_to(DOWN*1.8)); self.wait(d)
