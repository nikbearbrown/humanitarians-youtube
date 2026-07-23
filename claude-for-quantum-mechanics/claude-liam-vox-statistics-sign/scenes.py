import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR.update({b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]})
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0,opacity=0)
def axes(): return Axes(x_range=[-4,6,1],y_range=[0,4,1],x_length=11,y_length=5.7,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.35)

class B02_OccupationQuestion(Scene):
 def construct(self):
  d=DUR.get("B02",9); self.add(bg()); title=Text("HOW MANY PARTICLES OCCUPY EACH ENERGY STATE?",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35)
  rs=VGroup(*[Line(LEFT*4,RIGHT*4,color=TEAL,stroke_width=3).move_to(DOWN*2.2+UP*i*1.05) for i in range(5)]); labs=VGroup(*[Text(f"E{i}",font=MONO,font_size=21,color=INK).next_to(rs[i],LEFT,buff=.25) for i in range(5)]); qs=VGroup(*[Text("?",font=DISPLAY,font_size=32,color=CRIMSON).move_to(rs[i].get_center()) for i in range(5)])
  self.play(FadeIn(title),LaggedStart(*[Create(r) for r in rs],lag_ratio=.12),FadeIn(labs),run_time=1.4); self.play(LaggedStart(*[FadeIn(q) for q in qs],lag_ratio=.15),run_time=.8); self.wait(max(.1,d-2.2))
class B03_FermionFill(Scene):
 def construct(self):
  d=DUR.get("B03",11); self.add(bg()); title=Text("FERMI–DIRAC:  +1  CAPS OCCUPATION",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35); eq=Text("n = 1 / ( eˣ + 1 )",font=MONO,font_size=32,color=CRIMSON).move_to(RIGHT*4+UP*2.3)
  rs=VGroup(*[Line(LEFT*5,LEFT*.5,color=TEAL,stroke_width=3).move_to(DOWN*2.3+UP*i*.9) for i in range(6)]); labs=VGroup(*[Text(f"E{i}",font=MONO,font_size=18,color=INK).next_to(rs[i],LEFT,buff=.2) for i in range(6)]); dots=VGroup(*[Dot(rs[i].get_center(),color=CRIMSON,radius=.16) for i in range(5)])
  cap=Text("≤ 1 per state",font=MONO,font_size=27,color=INK).move_to(RIGHT*4+UP*.5)
  self.play(FadeIn(title),FadeIn(eq),FadeIn(rs),FadeIn(labs),run_time=1); self.play(LaggedStart(*[GrowFromCenter(x) for x in dots],lag_ratio=.18),FadeIn(cap),run_time=1.2); self.wait(max(.1,d-2.2))
class B04_FermiStep(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg()); title=Text("LOW TEMPERATURE → A SHARP FERMI EDGE",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35); ax=Axes(x_range=[-4,4,1],y_range=[0,1.3,.25],x_length=10,y_length=5,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.4); cold=ax.plot(lambda x:1/(np.exp(4*x)+1),x_range=[-4,4],color=CRIMSON,stroke_width=5); warm=ax.plot(lambda x:1/(np.exp(x)+1),x_range=[-4,4],color=TEAL,stroke_width=3); mu=DashedLine(ax.c2p(0,0),ax.c2p(0,1.15),color=INK); labs=VGroup(Text("cold",font=MONO,font_size=21,color=CRIMSON).move_to(ax.c2p(1,.15)),Text("warmer",font=MONO,font_size=21,color=TEAL).move_to(ax.c2p(1,.5)),Text("μ",font=MONO,font_size=22,color=INK).next_to(mu,DOWN))
  self.play(FadeIn(title),Create(ax),Create(warm),run_time=1.2); self.play(TransformFromCopy(warm,cold),Create(mu),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-2.4))
class B05_FermionRule(Scene):
 def construct(self):
  d=DUR.get("B05",6); self.add(bg()); self.add(Text("FERMIONS STACK ACROSS STATES\nNOT INSIDE ONE STATE",font=DISPLAY,font_size=38,color=INK,line_spacing=1.3)); self.wait(d)
class B06_BosonPile(Scene):
 def construct(self):
  d=DUR.get("B06",11); self.add(bg()); title=Text("BOSE–EINSTEIN:  −1  REMOVES THE CAP",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35); eq=Text("n = 1 / ( eˣ − 1 )",font=MONO,font_size=32,color=CRIMSON).move_to(RIGHT*4+UP*2.3)
  seat=RoundedRectangle(width=3.4,height=1.4,corner_radius=.15).set_fill(TEAL,.07).set_stroke(TEAL,2).move_to(LEFT*3); lab=Text("one state",font=MONO,font_size=22,color=INK).next_to(seat,DOWN); dots=VGroup(*[Dot(LEFT*4.1+RIGHT*(i%5)*.55+UP*((i//5)-1)*.42,color=(CRIMSON if i%2 else TEAL),radius=.14) for i in range(15)]); count=Text("1, 10, 1000, …",font=MONO,font_size=28,color=INK).move_to(RIGHT*3+DOWN*.4)
  self.play(FadeIn(title),FadeIn(eq),FadeIn(seat),FadeIn(lab),run_time=1); self.play(LaggedStart(*[GrowFromCenter(x) for x in dots],lag_ratio=.06),FadeIn(count),run_time=1.5); self.wait(max(.1,d-2.5))
class B07_BoseSurge(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg()); title=Text("BOSONS CAN SURGE INTO THE LOWEST STATE",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); ax=Axes(x_range=[0,5,1],y_range=[0,5,1],x_length=9,y_length=5.6,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.4); curve=ax.plot(lambda x:1/(np.exp(x)-1),x_range=[.2,5],color=CRIMSON,stroke_width=5,use_smoothing=False); xl=Text("x = (E−μ)/kBT  > 0",font=MONO,font_size=22,color=INK).next_to(ax,DOWN); pile=VGroup(*[Dot(ax.c2p(.35,.5+i*.38),color=TEAL,radius=.11) for i in range(10)]); note=Text("ground-state pile can become macroscopic",font=MONO,font_size=21,color=TEAL).move_to(RIGHT*2+UP*2.3)
  self.play(FadeIn(title),Create(ax),FadeIn(xl),run_time=1); self.play(Create(curve),LaggedStart(*[GrowFromCenter(p) for p in pile],lag_ratio=.08),FadeIn(note),run_time=1.5); self.wait(max(.1,d-2.5))
class B08_SharedAxis(Scene):
 def construct(self):
  d=DUR.get("B08",10); self.add(bg()); title=Text("ONE AXIS — TWO LOW-TEMPERATURE WORLDS",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35); ax=axes(); fd=ax.plot(lambda x:1/(np.exp(x)+1),x_range=[-4,6],color=TEAL,stroke_width=5); be=ax.plot(lambda x:1/(np.exp(x)-1),x_range=[.27,6],color=CRIMSON,stroke_width=5,use_smoothing=False); cap=DashedLine(ax.c2p(-4,1),ax.c2p(6,1),color=TEAL); pole=DashedLine(ax.c2p(0,0),ax.c2p(0,4),color=CRIMSON); labs=VGroup(Text("FD ≤ 1",font=MONO,font_size=22,color=TEAL).move_to(ax.c2p(-2,1.35)),Text("BE, x>0",font=MONO,font_size=22,color=CRIMSON).move_to(ax.c2p(1.5,2.7)),Text("x=(E−μ)/kBT",font=MONO,font_size=21,color=INK).next_to(ax,DOWN))
  self.play(FadeIn(title),Create(ax),Create(fd),run_time=1.2); self.play(Create(be),Create(cap),Create(pole),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-2.4))
class B09_DomainWarning(Scene):
 def construct(self):
  d=DUR.get("B09",9); self.add(bg()); top=Text("BOSE CURVE: READ ONLY x > 0",font=DISPLAY,font_size=38,color=CRIMSON).move_to(UP*1.4); mid=Text("x = (E−μ) / kBT",font=MONO,font_size=34,color=INK); bot=Text("Crossing the pole would invent negative occupation.",font=SERIF,font_size=29,color=TEAL).move_to(DOWN*1.5); self.add(top,mid,bot); self.wait(d)
class B10_ClassicalLimit(Scene):
 def construct(self):
  d=DUR.get("B10",11); self.add(bg()); title=Text("HIGH TEMPERATURE / LOW DENSITY → SAME TAIL",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); ax=Axes(x_range=[0,6,1],y_range=[0,1.2,.2],x_length=10,y_length=5,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.4); fd=ax.plot(lambda x:1/(np.exp(x)+1),x_range=[.35,6],color=TEAL,stroke_width=4); be=ax.plot(lambda x:1/(np.exp(x)-1),x_range=[.35,6],color=CRIMSON,stroke_width=4); mb=ax.plot(lambda x:np.exp(-x),x_range=[.35,6],color=INK,stroke_width=3); labs=VGroup(Text("FD",font=MONO,font_size=20,color=TEAL).move_to(ax.c2p(.7,.2)),Text("BE",font=MONO,font_size=20,color=CRIMSON).move_to(ax.c2p(.7,1)),Text("Maxwell–Boltzmann tail",font=MONO,font_size=21,color=INK).move_to(ax.c2p(3,.35)))
  self.play(FadeIn(title),Create(ax),Create(fd),Create(be),run_time=1.3); self.play(Create(mb),FadeIn(labs),run_time=1); self.wait(max(.1,d-2.3))
class B11_SymmetryMeaning(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg()); title=Text("THE SIGN ENCODED THE SYMMETRY",font=DISPLAY,font_size=32,color=INK).move_to(UP*3); l=RoundedRectangle(width=5.7,height=2.7,corner_radius=.15).set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(LEFT*3.3); r=l.copy().set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(RIGHT*3.3); lt=Text("ANTISYMMETRIC\nfermions exclude",font=DISPLAY,font_size=29,color=TEAL,line_spacing=1.25).move_to(l); rt=Text("SYMMETRIC\nbosons can collect",font=DISPLAY,font_size=29,color=CRIMSON,line_spacing=1.25).move_to(r); self.add(title,l,r,lt,rt); self.wait(d)
