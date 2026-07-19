import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def wav(x0,x1,k,y=0,col=TEAL):
 xs=np.linspace(x0,x1,300); return VMobject(color=col,stroke_width=3).set_points_smoothly([np.array([x,.55*np.sin(k*x)+y,0]) for x in xs])
def step(): return VGroup(Line(LEFT*6,ORIGIN,color=INK,stroke_width=4).shift(UP*1.2),Line(ORIGIN,RIGHT*6,color=INK,stroke_width=4).shift(DOWN*1.2),Line(UP*1.2,DOWN*1.2,color=INK,stroke_width=4))

class B02_Classical(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg(),ttl("CLASSICAL DOWNHILL STEP: SPEED UP, KEEP GOING")); s=step(); ball=Dot(LEFT*4+UP*1.55,radius=.24,color=CRIMSON); a1=Arrow(LEFT*3.5,LEFT*.5,color=TEAL,buff=0); a2=Arrow(RIGHT*.5+DOWN*1.55,RIGHT*5+DOWN*1.55,color=TEAL,buff=0,stroke_width=7); labs=VGroup(Text("lower V",font=MONO,font_size=25,color=INK).move_to(RIGHT*4+DOWN*2),Text("larger kinetic energy",font=SERIF,font_size=27,color=TEAL).move_to(RIGHT*3+UP*.3)); self.play(Create(s),FadeIn(ball),GrowArrow(a1),run_time=.8); self.play(GrowArrow(a2),FadeIn(labs),run_time=.8); self.wait(max(.1,d-1.6))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",6); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=23,color=SLATE).move_to(UP*2.3),Text("What can send an allowed",font=SERIF,font_size=42,color=INK).move_to(UP*.5),Text("quantum wave backward?",font=SERIF,font_size=44,color=CRIMSON).move_to(DOWN*.9)); self.wait(d)

class B04_Wavelength(Scene):
 def construct(self):
  d=DUR.get("B04",11); self.add(bg(),ttl("LOWER POTENTIAL → LARGER k → SHORTER WAVELENGTH")); s=step(); w1=wav(-6,0,2,1.2,TEAL); w2=wav(0,6,4,-1.2,TEAL); labs=VGroup(Text("k1",font=MONO,font_size=28,color=INK).move_to(LEFT*3+UP*2.3),Text("k2 > k1",font=MONO,font_size=28,color=CRIMSON).move_to(RIGHT*3+DOWN*2.3)); self.play(Create(s),Create(w1),run_time=.7); self.play(Create(w2),FadeIn(labs),run_time=.9); self.wait(max(.1,d-1.6))

class B05_Matching(Scene):
 def construct(self):
  d=DUR.get("B05",11); self.add(bg(),ttl("ONE INCOMING WAVE CANNOT MATCH BOTH VALUE AND SLOPE")); boundary=Line(UP*2.4,DOWN*2.4,color=INK,stroke_width=4); left=wav(-6,0,2,0,TEAL); right=wav(0,6,4,0,SLATE); marks=VGroup(Text("psi continuous",font=MONO,font_size=25,color=INK).move_to(UP*2),Text("dpsi/dx continuous",font=MONO,font_size=25,color=INK).move_to(DOWN*2),Text("mismatch",font=DISPLAY,font_size=30,color=CRIMSON).move_to(RIGHT*3+UP*2)); self.play(Create(left),Create(right),Create(boundary),run_time=.9); self.play(FadeIn(marks),run_time=.8); self.wait(max(.1,d-1.7))

class B06_ThreeWaves(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg(),ttl("THE BOUNDARY SOLUTION SPLITS THE WAVE")); b=Line(UP*2.3,DOWN*2.3,color=INK); inc=Arrow(LEFT*5,LEFT*.5,color=TEAL,buff=0,stroke_width=6).shift(UP*1); ref=Arrow(LEFT*.5,LEFT*4,color=CRIMSON,buff=0,stroke_width=4).shift(DOWN*.2); trans=Arrow(RIGHT*.5,RIGHT*5,color=TEAL,buff=0,stroke_width=7).shift(DOWN*1.2); labs=VGroup(Text("incident",font=MONO,font_size=23,color=TEAL).next_to(inc,UP),Text("reflected",font=MONO,font_size=23,color=CRIMSON).next_to(ref,DOWN),Text("transmitted",font=MONO,font_size=23,color=TEAL).next_to(trans,DOWN)); self.play(Create(b),GrowArrow(inc),run_time=.6); self.play(GrowArrow(ref),GrowArrow(trans),FadeIn(labs),run_time=.9); self.wait(max(.1,d-1.5))

class B07_Coefficient(Scene):
 def construct(self):
  d=DUR.get("B07",12); self.add(bg(),ttl("ABRUPT-STEP REFLECTION")); eqs=VGroup(Text("r = (k1 - k2) / (k1 + k2)",font=MONO,font_size=35,color=INK),Text("R = |r|^2",font=MONO,font_size=42,color=CRIMSON),Text("both k1 and k2 are real",font=SERIF,font_size=28,color=TEAL)).arrange(DOWN,buff=.8); self.play(Write(eqs[0]),run_time=.8); self.play(FadeIn(eqs[1:]),run_time=.8); self.wait(max(.1,d-1.6))

class B08_Mismatch(Scene):
 def construct(self):
  d=DUR.get("B08",10); self.add(bg(),ttl("MORE WAVE-NUMBER MISMATCH → MORE REFLECTION")); ax=Axes(x_range=[1,5,1],y_range=[0,0.5,.1],x_length=9,y_length=4,tips=False).move_to(DOWN*.2); curve=ax.plot(lambda q:((1-q)/(1+q))**2,x_range=[1,5],color=CRIMSON); labs=VGroup(Text("k2 / k1",font=MONO,font_size=22,color=INK).next_to(ax,DOWN),Text("R",font=MONO,font_size=23,color=INK).next_to(ax,LEFT),Text("R = 0 when k2 = k1",font=SERIF,font_size=26,color=TEAL).move_to(UP*2.5)); self.play(Create(ax),Create(curve),FadeIn(labs),run_time=1.1); self.wait(max(.1,d-1.1))

class B09_Allowed(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("NO FORBIDDEN REGION IS REQUIRED")); left=VGroup(Rectangle(width=4.8,height=3.6,color=TEAL,fill_color=TEAL,fill_opacity=.08),Text("LEFT",font=DISPLAY,font_size=25,color=INK),Text("E > V1",font=MONO,font_size=31,color=TEAL)).arrange(DOWN,buff=.45).move_to(LEFT*3.4); right=VGroup(Rectangle(width=4.8,height=3.6,color=TEAL,fill_color=TEAL,fill_opacity=.08),Text("RIGHT",font=DISPLAY,font_size=25,color=INK),Text("E > V2",font=MONO,font_size=31,color=TEAL)).arrange(DOWN,buff=.45).move_to(RIGHT*3.4); note=Text("propagating waves on both sides",font=SERIF,font_size=30,color=CRIMSON).move_to(DOWN*3); self.play(FadeIn(left,right,note),run_time=1); self.wait(max(.1,d-1))

class B10_Smooth(Scene):
 def construct(self):
  d=DUR.get("B10",11); self.add(bg(),ttl("ABRUPT EDGE VERSUS SMOOTH RAMP")); hard=VGroup(Line(LEFT*2,ORIGIN,color=INK,stroke_width=4).shift(UP*.8),Line(ORIGIN,RIGHT*2,color=INK,stroke_width=4).shift(DOWN*.8),Line(UP*.8,DOWN*.8,color=INK,stroke_width=4)).move_to(LEFT*3.5); xs=np.linspace(-2,2,100); smooth=VMobject(color=INK,stroke_width=4).set_points_smoothly([np.array([x, -.8*np.tanh(x),0]) for x in xs]).move_to(RIGHT*3.5); labs=VGroup(Text("more reflection",font=MONO,font_size=25,color=CRIMSON).move_to(LEFT*3.5+DOWN*2),Text("less reflection",font=MONO,font_size=25,color=TEAL).move_to(RIGHT*3.5+DOWN*2)); self.play(Create(hard),Create(smooth),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B11_CliffRamp(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("WAVES NOTICE HOW FAST THE MEDIUM CHANGES")); cliff=Text("CLIFF",font=DISPLAY,font_size=33,color=CRIMSON).move_to(LEFT*3.5+UP*1.5); ramp=Text("RAMP",font=DISPLAY,font_size=33,color=TEAL).move_to(RIGHT*3.5+UP*1.5); a1=Arrow(LEFT*2.5,LEFT*4.5,color=CRIMSON,buff=0); a2=Arrow(RIGHT*2.5,RIGHT*4.5,color=TEAL,buff=0); labs=VGroup(Text("backward component",font=SERIF,font_size=27,color=INK).next_to(a1,DOWN),Text("mostly forward",font=SERIF,font_size=27,color=INK).next_to(a2,DOWN)); self.play(FadeIn(cliff,ramp),GrowArrow(a1),GrowArrow(a2),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("ENOUGH ENERGY",font=DISPLAY,font_size=32,color=TEAL).move_to(UP*1.6),Text("does not guarantee zero reflection",font=SERIF,font_size=40,color=INK),Text("a sudden wavelength mismatch splits the wave",font=SERIF,font_size=28,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
