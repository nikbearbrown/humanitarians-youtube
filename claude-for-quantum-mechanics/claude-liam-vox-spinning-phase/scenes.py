import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def clock(center=ORIGIN,angle=PI/4,col=CRIMSON):
 c=Circle(radius=1.45,color=SLATE).move_to(center); a=Arrow(center,center+1.25*np.array([np.cos(angle),np.sin(angle),0]),buff=0,color=col,stroke_width=6); return VGroup(c,a,Dot(center,radius=.1,color=INK))

class B02_Histograms(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg(),ttl("REPEAT THE POSITION MEASUREMENT")); xs=np.linspace(-4,4,19); bars=[]
  for shift in [-3.8,0,3.8]:
   for x in xs:
    h=2.1*np.exp(-.5*(x/1.45)**2); bars.append(Rectangle(width=.28,height=h,color=TEAL,fill_color=TEAL,fill_opacity=.35).move_to(np.array([shift+x*.38,-1.5+h/2,0])))
  labs=VGroup(*[Text(s,font=MONO,font_size=23,color=INK).move_to(np.array([x,-2.4,0])) for x,s in zip([-3.8,0,3.8],["time t0","time t1","time t2"])]); self.play(FadeIn(VGroup(*bars)),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",6); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=23,color=SLATE).move_to(UP*2.3),Text("If the histogram stands still,",font=SERIF,font_size=40,color=INK).move_to(UP*.5),Text("what is spinning?",font=SERIF,font_size=45,color=CRIMSON).move_to(DOWN*.9)); self.wait(d)

class B04_SeparatedState(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg(),ttl("AN ENERGY EIGENSTATE SEPARATES")); eq=Text("psi(x,t) = phi(x)  exp(-i E t / hbar)",font=MONO,font_size=34,color=INK); brace1=Line(LEFT*5,LEFT*.7,color=TEAL,stroke_width=7).shift(DOWN*1.1); brace2=Line(RIGHT*.6,RIGHT*5,color=CRIMSON,stroke_width=7).shift(DOWN*1.1); labs=VGroup(Text("fixed spatial shape",font=SERIF,font_size=28,color=TEAL).next_to(brace1,DOWN),Text("rotating time factor",font=SERIF,font_size=28,color=CRIMSON).next_to(brace2,DOWN)); self.play(Write(eq),run_time=.8); self.play(Create(brace1),Create(brace2),FadeIn(labs),run_time=.8); self.wait(max(.1,d-1.6))

class B05_UnitPhase(Scene):
 def construct(self):
  d=DUR.get("B05",11); self.add(bg(),ttl("THE TIME FACTOR IS A UNIT-LENGTH CLOCK HAND")); axes=VGroup(Line(LEFT*2,RIGHT*2,color=SLATE),Line(DOWN*2,UP*2,color=SLATE)); c=clock(); lab=Text("angle = -E t / hbar",font=MONO,font_size=30,color=CRIMSON).move_to(DOWN*2.8); unit=Text("length = 1",font=MONO,font_size=25,color=TEAL).move_to(RIGHT*3.5); self.add(axes); self.play(FadeIn(c),FadeIn(lab,unit),run_time=.8); self.play(Rotate(c[1],angle=-TAU,about_point=ORIGIN),run_time=min(4,d*.45),rate_func=linear); self.wait(max(.1,d-min(4,d*.45)-.8))

class B06_WholeState(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg(),ttl("EVERY AMPLITUDE ROTATES BY THE SAME ANGLE")); centers=[np.array([-4,0,0]),np.array([0,0,0]),np.array([4,0,0])]; clocks=VGroup(*[clock(c,a).scale(.75) for c,a in zip(centers,[.3,.8,1.3])]); labs=VGroup(*[Text(s,font=MONO,font_size=22,color=INK).move_to(c+DOWN*2) for c,s in zip(centers,["psi(x1)","psi(x2)","psi(x3)"])]); self.play(FadeIn(clocks,labs),run_time=.8); self.play(*[Rotate(x[1],angle=-PI,about_point=x[0].get_center()) for x in clocks],run_time=2); self.wait(max(.1,d-2.8))

class B07_Cancel(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg(),ttl("THE GLOBAL PHASE CANCELS IN PROBABILITY")); eqs=VGroup(Text("|psi|^2 = psi* psi",font=MONO,font_size=32,color=INK),Text("= |phi|^2 exp(+iEt/hbar) exp(-iEt/hbar)",font=MONO,font_size=28,color=INK),Text("= |phi|^2",font=MONO,font_size=42,color=TEAL)).arrange(DOWN,buff=.7); cross=VGroup(Line(LEFT*.6+UP*.18,RIGHT*.6+DOWN*.18,color=CRIMSON,stroke_width=5),Line(LEFT*.6+DOWN*.18,RIGHT*.6+UP*.18,color=CRIMSON,stroke_width=5)).move_to(eqs[1].get_center()+RIGHT*2.3); self.play(FadeIn(eqs[:2]),run_time=.9); self.play(Create(cross),FadeIn(eqs[2]),run_time=.8); self.wait(max(.1,d-1.7))

class B08_Shadow(Scene):
 def construct(self):
  d=DUR.get("B08",10); self.add(bg(),ttl("THE CLOCK MOVES; ITS SHADOW DOES NOT")); c=clock(LEFT*3); shadow=Line(LEFT*1.25,RIGHT*1.25,color=TEAL,stroke_width=12).move_to(RIGHT*3); arr=Arrow(LEFT*1.2,RIGHT*1.2,color=SLATE,buff=.1); labs=VGroup(Text("wave function",font=MONO,font_size=25,color=CRIMSON).move_to(LEFT*3+DOWN*2.2),Text("|psi|^2",font=MONO,font_size=27,color=TEAL).move_to(RIGHT*3+DOWN*2.2)); self.play(FadeIn(c,shadow),GrowArrow(arr),FadeIn(labs),run_time=.9); self.play(Rotate(c[1],angle=-TAU,about_point=LEFT*3),run_time=3,rate_func=linear); self.wait(max(.1,d-3.9))

class B09_GlobalPhase(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("A GLOBAL PHASE CANNOT BE OBSERVED ALONE")); left=Text("psi",font=MONO,font_size=48,color=INK).move_to(LEFT*4); right=Text("exp(i alpha) psi",font=MONO,font_size=36,color=CRIMSON).move_to(RIGHT*4); eq=Text("same measurement probabilities",font=SERIF,font_size=33,color=TEAL).move_to(DOWN*2); arrow=DoubleArrow(LEFT*1.15,RIGHT*1.15,color=SLATE,buff=0); self.play(FadeIn(left,right),GrowArrow(arrow),run_time=.8); self.play(FadeIn(eq),run_time=.7); self.wait(max(.1,d-1.5))

class B10_RelativePhase(Scene):
 def construct(self):
  d=DUR.get("B10",12); self.add(bg(),ttl("TWO ENERGIES CREATE A CHANGING RELATIVE PHASE")); c1=clock(LEFT*3,0,TEAL); c2=clock(RIGHT*3,0,CRIMSON); labs=VGroup(Text("E1 / hbar",font=MONO,font_size=24,color=TEAL).move_to(LEFT*3+DOWN*2.2),Text("E2 / hbar",font=MONO,font_size=24,color=CRIMSON).move_to(RIGHT*3+DOWN*2.2),Text("relative angle changes",font=SERIF,font_size=30,color=INK).move_to(DOWN*3)); self.play(FadeIn(c1,c2,labs),run_time=.8); self.play(Rotate(c1[1],angle=-PI,about_point=LEFT*3),Rotate(c2[1],angle=-2*PI,about_point=RIGHT*3),run_time=4,rate_func=linear); self.wait(max(.1,d-4.8))

class B11_Boundary(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("WHERE 'STATIONARY' STOPS")); left=VGroup(Text("ONE ENERGY",font=DISPLAY,font_size=27,color=TEAL),Text("fixed |psi|^2",font=MONO,font_size=28,color=INK)).arrange(DOWN,buff=.7).move_to(LEFT*3.5); right=VGroup(Text("TWO ENERGIES",font=DISPLAY,font_size=27,color=CRIMSON),Text("interference can move",font=MONO,font_size=26,color=INK)).arrange(DOWN,buff=.7).move_to(RIGHT*3.5); div=Line(UP*2.4,DOWN*2.4,color=SLATE); self.play(FadeIn(left,right),Create(div),run_time=1); self.wait(max(.1,d-1))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("A SPINNING QUANTUM CLOCK",font=DISPLAY,font_size=30,color=CRIMSON).move_to(UP*2),Text("casts a stationary probability shadow",font=SERIF,font_size=39,color=TEAL),Text("stationary does not mean frozen",font=SERIF,font_size=28,color=INK).move_to(DOWN*2)); self.wait(d)
