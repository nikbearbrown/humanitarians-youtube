import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR.update({b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]})
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0,opacity=0)
def barrier_axes(): return Axes(x_range=[0,10,1],y_range=[-2,8,1],x_length=12,y_length=6,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.25)
def potential(ax):
 return VGroup(Line(ax.c2p(0,-1),ax.c2p(2,-1),color=TEAL,stroke_width=5),Line(ax.c2p(2,-1),ax.c2p(2,7),color=TEAL,stroke_width=5),ax.plot(lambda x:14/x,x_range=[2,10],color=TEAL,stroke_width=5))

class B02_NuclearBarrier(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg()); title=Text("AN ALPHA PARTICLE FACES A COULOMB HILL",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.4)
  ax=barrier_axes(); p=potential(ax); a=Dot(ax.c2p(1,-.3),color=CRIMSON,radius=.18); labs=VGroup(Text("nuclear well",font=MONO,font_size=20,color=TEAL).move_to(ax.c2p(1,-1.6)),Text("electric repulsion",font=MONO,font_size=20,color=TEAL).move_to(ax.c2p(6,3.4)),Text("α",font=DISPLAY,font_size=24,color=GROUND).move_to(a))
  self.play(FadeIn(title),Create(ax),Create(p),run_time=1.5); self.play(GrowFromCenter(a),FadeIn(labs),run_time=.8); self.wait(max(.1,d-2.3))
class B03_ClassicalPrison(Scene):
 def construct(self):
  d=DUR.get("B03",9); self.add(bg()); title=Text("CLASSICAL VERDICT: NO ESCAPE",font=DISPLAY,font_size=34,color=CRIMSON).move_to(UP*3.4); ax=barrier_axes(); p=potential(ax); e=Line(ax.c2p(0,2),ax.c2p(10,2),color=CRIMSON,stroke_width=4); lab=Text("E < barrier top",font=MONO,font_size=23,color=CRIMSON).next_to(e,UP)
  self.play(FadeIn(title),Create(ax),Create(p),run_time=1.3); self.play(Create(e),FadeIn(lab),run_time=.8); self.play(Flash(ax.c2p(2,2),color=CRIMSON),run_time=.7); self.wait(max(.1,d-2.8))
class B04_WaveLeak(Scene):
 def construct(self):
  d=DUR.get("B04",11); self.add(bg()); title=Text("QUANTUM VERDICT: A TINY TAIL GETS THROUGH",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.4); ax=barrier_axes(); p=potential(ax)
  left=ax.plot(lambda x:.7*np.sin(7*x)-.1,x_range=[.15,2],color=CRIMSON,stroke_width=4); tail=ax.plot(lambda x:.7*np.exp(-.65*(x-2))*np.cos(2*(x-2))-.1,x_range=[2,8.5],color=CRIMSON,stroke_width=4); out=ax.plot(lambda x:.04*np.sin(6*x)-.1,x_range=[8.5,10],color=CRIMSON,stroke_width=4)
  self.play(FadeIn(title),Create(ax),Create(p),run_time=1.2); self.play(Create(left),Create(tail),Create(out),run_time=2); self.wait(max(.1,d-3.2))
class B05_TinyNotZero(Scene):
 def construct(self):
  d=DUR.get("B05",7); self.add(bg()); box=RoundedRectangle(width=12,height=2.2,corner_radius=.15).set_fill(TEAL,.07).set_stroke(TEAL,2); t=Text("TINY ≠ ZERO\nATTEMPTS × PROBABILITY = DECAY RATE",font=DISPLAY,font_size=33,color=INK,line_spacing=1.2); self.add(box,t); self.wait(d)
class B06_Exponential(Scene):
 def construct(self):
  d=DUR.get("B06",11); self.add(bg()); title=Text("THE EXPONENT IS EVERYTHING",font=DISPLAY,font_size=35,color=INK).move_to(UP*3.35); eq=Text("T  ~  exp( − barrier factor )",font=MONO,font_size=42,color=CRIMSON).move_to(UP*1.4)
  bars=VGroup(*[Rectangle(width=.65,height=.25+.47*i).set_fill(TEAL,.25).set_stroke(TEAL,1).move_to(LEFT*4.5+RIGHT*i*1.1+DOWN*1.2+UP*(.25+.47*i)/2) for i in range(9)]); labels=Text("small exponent change  →  huge probability ratio",font=MONO,font_size=23,color=INK).move_to(DOWN*3)
  self.play(FadeIn(title),FadeIn(eq),run_time=.8); self.play(LaggedStart(*[GrowFromEdge(b,DOWN) for b in bars],lag_ratio=.1),FadeIn(labels),run_time=1.5); self.wait(max(.1,d-2.3))
class B07_EnergyComparison(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg()); title=Text("HIGHER ENERGY SHORTENS THE FORBIDDEN REGION",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
  ax=barrier_axes(); p=potential(ax); low=Line(ax.c2p(0,1.5),ax.c2p(9.3,1.5),color=CRIMSON,stroke_width=3); high=Line(ax.c2p(0,3.2),ax.c2p(4.4,3.2),color=INK,stroke_width=3); bl=BraceBetweenPoints(ax.c2p(2,1.3),ax.c2p(9.3,1.3),DOWN,color=CRIMSON); bh=BraceBetweenPoints(ax.c2p(2,3.4),ax.c2p(4.4,3.4),UP,color=INK)
  labs=VGroup(Text("lower E: wide barrier",font=MONO,font_size=20,color=CRIMSON).next_to(bl,DOWN),Text("higher E: narrow barrier",font=MONO,font_size=20,color=INK).next_to(bh,UP))
  self.play(FadeIn(title),Create(ax),Create(p),run_time=1.2); self.play(Create(low),Create(high),GrowFromCenter(bl),GrowFromCenter(bh),FadeIn(labs),run_time=1.5); self.wait(max(.1,d-2.7))
class B08_Polonium(Scene):
 def construct(self):
  d=DUR.get("B08",10); self.add(bg()); title=Text("POLONIUM-212",font=DISPLAY,font_size=38,color=INK).move_to(UP*3); e=Text("8.78 MeV",font=MONO,font_size=44,color=TEAL).move_to(LEFT*3); clock=Circle(radius=1.5,color=CRIMSON,stroke_width=5).move_to(RIGHT*3); hand=Line(clock.get_center(),clock.get_center()+UP*1.1,color=CRIMSON,stroke_width=5); life=Text("≈ 0.3 μs",font=MONO,font_size=38,color=CRIMSON).next_to(clock,DOWN,buff=.45)
  self.play(FadeIn(title),FadeIn(e),Create(clock),Create(hand),run_time=1); self.play(Rotate(hand,angle=TAU,about_point=clock.get_center()),FadeIn(life),run_time=1.3); self.wait(max(.1,d-2.3))
class B09_Thorium(Scene):
 def construct(self):
  d=DUR.get("B09",11); self.add(bg()); title=Text("THORIUM-232",font=DISPLAY,font_size=38,color=INK).move_to(UP*3); e=Text("4.01 MeV",font=MONO,font_size=44,color=TEAL).move_to(LEFT*3); rings=VGroup(*[Circle(radius=r,color=CRIMSON,stroke_opacity=.75-i*.12) for i,r in enumerate((.5,.8,1.1,1.4,1.7))]).move_to(RIGHT*3); life=Text("≈ 14 billion years",font=MONO,font_size=32,color=CRIMSON).next_to(rings,DOWN,buff=.35); ratio=Text("energy ÷ ~2   •   lifetime × ~10²⁴",font=MONO,font_size=25,color=INK).move_to(DOWN*3.3)
  self.play(FadeIn(title),FadeIn(e),LaggedStart(*[Create(r) for r in rings],lag_ratio=.15),run_time=1.5); self.play(FadeIn(life),FadeIn(ratio),run_time=.8); self.wait(max(.1,d-2.3))
class B10_GeigerNuttall(Scene):
 def construct(self):
  d=DUR.get("B10",12); self.add(bg()); title=Text("GEIGER–NUTTALL: THE EXPONENTIAL BECOMES A LINE",font=DISPLAY,font_size=27,color=INK).move_to(UP*3.35); ax=Axes(x_range=[0,5,1],y_range=[0,6,1],x_length=9,y_length=5,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.35); xl=Text("1 / √E",font=MONO,font_size=24,color=INK).next_to(ax,DOWN); yl=Text("log half-life",font=MONO,font_size=22,color=INK).rotate(PI/2).next_to(ax,LEFT)
  lines=VGroup(*[Line(ax.c2p(.5,.6+j*.65),ax.c2p(4.7,4.9+j*.2),color=(TEAL,CRIMSON,INK)[j],stroke_width=3) for j in range(3)]); pts=VGroup(*[Dot(lines[j].point_from_proportion(t),color=(TEAL,CRIMSON,INK)[j],radius=.09) for j in range(3) for t in (.12,.3,.5,.7,.9)])
  self.play(FadeIn(title),Create(ax),FadeIn(xl),FadeIn(yl),run_time=1); self.play(LaggedStart(*[Create(l) for l in lines],lag_ratio=.2),LaggedStart(*[GrowFromCenter(p) for p in pts],lag_ratio=.03),run_time=1.8); self.wait(max(.1,d-2.8))
class B11_LogTakeaway(Scene):
 def construct(self):
  d=DUR.get("B11",9); self.add(bg()); top=Text("STRAIGHT ON A LOG PLOT",font=DISPLAY,font_size=36,color=TEAL).move_to(UP*1.2); bot=Text("DOZENS OF ZEROS ON AN ORDINARY CLOCK",font=DISPLAY,font_size=34,color=CRIMSON).move_to(DOWN*1.1); self.add(top,bot); self.wait(d)
