import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR.update({b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]})
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0,opacity=0)
def ax(): return Axes(x_range=[-5,5,1],y_range=[-4,4,1],x_length=11,y_length=6,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.25)
def labels(a): return VGroup(Text("control parameter λ",font=MONO,font_size=21,color=INK).next_to(a,DOWN),Text("energy",font=MONO,font_size=20,color=INK).rotate(PI/2).next_to(a,LEFT))

class B02_UncoupledCrossing(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg()); title=Text("NO COUPLING: THE BARE LEVELS CROSS",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35); a=ax(); l1=a.plot(lambda x:.65*x,x_range=[-5,5],color=TEAL,stroke_width=5); l2=a.plot(lambda x:-.65*x,x_range=[-5,5],color=CRIMSON,stroke_width=5); cross=Dot(a.c2p(0,0),color=INK,radius=.16); note=Text("g = 0",font=MONO,font_size=27,color=INK).move_to(RIGHT*4+UP*2)
  self.play(FadeIn(title),Create(a),FadeIn(labels(a)),run_time=1); self.play(Create(l1),Create(l2),GrowFromCenter(cross),FadeIn(note),run_time=1.3); self.wait(max(.1,d-2.3))
class B03_WeakFarMixing(Scene):
 def construct(self):
  d=DUR.get("B03",9); self.add(bg()); title=Text("FAR APART: COUPLING BARELY MIXES THEM",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); a=ax(); g=.65; up=a.plot(lambda x:np.sqrt((.65*x)**2+g*g),x_range=[-5,5],color=CRIMSON,stroke_width=5); dn=a.plot(lambda x:-np.sqrt((.65*x)**2+g*g),x_range=[-5,5],color=TEAL,stroke_width=5); left=VGroup(Dot(a.c2p(-4,np.sqrt((2.6)**2+g*g)),color=CRIMSON,radius=.14),Dot(a.c2p(-4,-np.sqrt((2.6)**2+g*g)),color=TEAL,radius=.14)); sep=DoubleArrow(left[1].get_center(),left[0].get_center(),color=INK,buff=.15); lab=Text("large ΔE → weak mixing",font=MONO,font_size=23,color=INK).move_to(RIGHT*3.5+DOWN*2.7)
  self.play(FadeIn(title),Create(a),Create(up),Create(dn),run_time=1.3); self.play(FadeIn(left),GrowFromCenter(sep),FadeIn(lab),run_time=.9); self.wait(max(.1,d-2.2))
class B04_StrongNearMixing(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg()); title=Text("NEAR DEGENERACY: THE STATES HYBRIDIZE",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35); left=RoundedRectangle(width=4.5,height=2.4,corner_radius=.15).set_fill(TEAL,.1).set_stroke(TEAL,2).move_to(LEFT*3.5); right=left.copy().set_fill(CRIMSON,.1).set_stroke(CRIMSON,2).move_to(RIGHT*3.5); bridge=DoubleArrow(left.get_right(),right.get_left(),color=INK,buff=.15); mix=VGroup(Text("mostly A",font=MONO,font_size=27,color=TEAL).move_to(left),Text("mostly B",font=MONO,font_size=27,color=CRIMSON).move_to(right)); hybrid=Text("A ± B mixtures",font=DISPLAY,font_size=35,color=INK).move_to(DOWN*2.5)
  self.play(FadeIn(title),FadeIn(left),FadeIn(right),FadeIn(mix),run_time=.8); self.play(GrowFromCenter(bridge),Transform(mix,hybrid),run_time=1.2); self.wait(max(.1,d-2))
class B05_CloserStronger(Scene):
 def construct(self):
  d=DUR.get("B05",7); self.add(bg()); top=Text("SMALLER BARE GAP",font=DISPLAY,font_size=37,color=TEAL).move_to(UP*1.3); arrow=Arrow(LEFT*1.4,RIGHT*1.4,color=INK); bot=Text("STRONGER COUPLED SPLITTING",font=DISPLAY,font_size=34,color=CRIMSON).move_to(DOWN*1.3); self.add(top,arrow,bot); self.wait(d)
class B06_MinimumGap(Scene):
 def construct(self):
  d=DUR.get("B06",11); self.add(bg()); title=Text("NONZERO g OPENS A MINIMUM GAP",font=DISPLAY,font_size=32,color=INK).move_to(UP*3.35); a=ax(); g=.8; up=a.plot(lambda x:np.sqrt((.65*x)**2+g*g),x_range=[-5,5],color=CRIMSON,stroke_width=5); dn=a.plot(lambda x:-np.sqrt((.65*x)**2+g*g),x_range=[-5,5],color=TEAL,stroke_width=5); gap=DoubleArrow(a.c2p(0,-g),a.c2p(0,g),color=INK,buff=.08); gl=Text("2 |g|",font=MONO,font_size=29,color=INK).next_to(gap,RIGHT); center=DashedLine(a.c2p(0,-3.5),a.c2p(0,3.5),color=INK,stroke_opacity=.35)
  self.play(FadeIn(title),Create(a),Create(up),Create(dn),run_time=1.4); self.play(Create(center),GrowFromCenter(gap),FadeIn(gl),run_time=.9); self.wait(max(.1,d-2.3))
class B07_BareVsDressed(Scene):
 def construct(self):
  d=DUR.get("B07",10); self.add(bg()); title=Text("BARE LINES CROSS — COUPLED ENERGIES AVOID",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35); a=ax(); bare=VGroup(a.plot(lambda x:.65*x,x_range=[-5,5],color=INK,stroke_width=2),a.plot(lambda x:-.65*x,x_range=[-5,5],color=INK,stroke_width=2)).set_opacity(.35); g=.75; dressed=VGroup(a.plot(lambda x:np.sqrt((.65*x)**2+g*g),x_range=[-5,5],color=CRIMSON,stroke_width=5),a.plot(lambda x:-np.sqrt((.65*x)**2+g*g),x_range=[-5,5],color=TEAL,stroke_width=5)); labs=VGroup(Text("uncoupled reference",font=MONO,font_size=20,color=INK).move_to(LEFT*3.5+UP*2.5),Text("physical eigenvalues",font=MONO,font_size=20,color=CRIMSON).move_to(RIGHT*3.5+UP*2.5))
  self.play(FadeIn(title),Create(a),Create(bare),run_time=1); self.play(Create(dressed),FadeIn(labs),run_time=1.3); self.wait(max(.1,d-2.3))
class B08_CharacterExchange(Scene):
 def construct(self):
  d=DUR.get("B08",11); self.add(bg()); title=Text("THE BRANCHES EXCHANGE STATE CHARACTER",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); positions=(-5,-1.6,1.6,5); tops=VGroup(); bottoms=VGroup(); grad=color_gradient([TEAL,CRIMSON],4)
  for i,x in enumerate(positions):
   tc=grad[i]; bc=grad[3-i]; tops.add(RoundedRectangle(width=2.1,height=1.2,corner_radius=.15).set_fill(tc,.25).set_stroke(tc,2).move_to(RIGHT*x+UP*1.35)); bottoms.add(RoundedRectangle(width=2.1,height=1.2,corner_radius=.15).set_fill(bc,.25).set_stroke(bc,2).move_to(RIGHT*x+DOWN*1.35))
  arrows=VGroup(*[Arrow(tops[i].get_right(),tops[i+1].get_left(),color=INK,buff=.1) for i in range(3)],*[Arrow(bottoms[i].get_right(),bottoms[i+1].get_left(),color=INK,buff=.1) for i in range(3)]); labs=VGroup(Text("LOWER BRANCH",font=MONO,font_size=17,color=INK).move_to(LEFT*6.05+DOWN*2.45),Text("UPPER BRANCH",font=MONO,font_size=17,color=INK).move_to(LEFT*6.05+UP*2.45),Text("A",font=DISPLAY,font_size=26,color=TEAL).move_to(LEFT*5+DOWN*1.35),Text("B",font=DISPLAY,font_size=26,color=CRIMSON).move_to(RIGHT*5+DOWN*1.35))
  self.play(FadeIn(title),FadeIn(tops),FadeIn(bottoms),FadeIn(labs),run_time=1); self.play(LaggedStart(*[GrowArrow(x) for x in arrows],lag_ratio=.1),run_time=1.2); self.wait(max(.1,d-2.2))
class B09_InverseGap(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg()); title=Text("PERTURBATIVE INFLUENCE GROWS AS THE GAP SHRINKS",font=DISPLAY,font_size=27,color=INK).move_to(UP*3.35); gaps=(3.2,2.1,1.1,.5); groups=VGroup()
  for i,g in enumerate(gaps):
   x=-5.2+i*3.45; lines=VGroup(Line(LEFT*.8,RIGHT*.8,color=TEAL).move_to(RIGHT*x+UP*g/2),Line(LEFT*.8,RIGHT*.8,color=CRIMSON).move_to(RIGHT*x+DOWN*g/2)); arrow=DoubleArrow(RIGHT*x+DOWN*g/2,RIGHT*x+UP*g/2,color=INK,buff=.08); glow=Circle(radius=.25+.18*i,color=CRIMSON,stroke_opacity=.5).move_to(RIGHT*x); groups.add(VGroup(lines,arrow,glow))
  eq=Text("smaller ΔE  →  stronger mixing / larger shift",font=MONO,font_size=25,color=INK).move_to(DOWN*3)
  self.play(FadeIn(title),LaggedStart(*[FadeIn(g) for g in groups],lag_ratio=.15),FadeIn(eq),run_time=1.4); self.wait(max(.1,d-1.4))
class B10_CrossingException(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg()); title=Text("THE EXCEPTION: g = 0 RESTORES A TRUE CROSSING",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35); a1=Axes(x_range=[-3,3,1],y_range=[-2.5,2.5,1],x_length=5.2,y_length=4.5,axis_config={"color":INK,"include_ticks":False}).move_to(LEFT*3.7+DOWN*.3); a2=a1.copy().move_to(RIGHT*3.7+DOWN*.3); cross=VGroup(a1.plot(lambda x:.6*x,x_range=[-3,3],color=TEAL),a1.plot(lambda x:-.6*x,x_range=[-3,3],color=CRIMSON)); g=.65; avoid=VGroup(a2.plot(lambda x:np.sqrt((.6*x)**2+g*g),x_range=[-3,3],color=CRIMSON),a2.plot(lambda x:-np.sqrt((.6*x)**2+g*g),x_range=[-3,3],color=TEAL)); labs=VGroup(Text("g = 0\nCROSS",font=MONO,font_size=24,color=INK).move_to(LEFT*3.7+DOWN*3),Text("g ≠ 0\nAVOID",font=MONO,font_size=24,color=INK).move_to(RIGHT*3.7+DOWN*3),Text("symmetry can force g=0",font=MONO,font_size=21,color=CRIMSON).move_to(UP*2.4))
  self.play(FadeIn(title),Create(a1),Create(a2),Create(cross),Create(avoid),FadeIn(labs),run_time=1.5); self.wait(max(.1,d-1.5))
class B11_ConditionalRule(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg()); title=Text("THE CONDITIONAL RULE",font=DISPLAY,font_size=32,color=INK).move_to(UP*3); l=RoundedRectangle(width=5.7,height=2.8,corner_radius=.15).set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(LEFT*3.2); r=l.copy().set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(RIGHT*3.2); lt=Text("COUPLED\nlevels avoid",font=DISPLAY,font_size=31,color=CRIMSON,line_spacing=1.2).move_to(l); rt=Text("UNCOUPLED\nlevels may cross",font=DISPLAY,font_size=31,color=TEAL,line_spacing=1.2).move_to(r); self.add(title,l,r,lt,rt); self.wait(d)
