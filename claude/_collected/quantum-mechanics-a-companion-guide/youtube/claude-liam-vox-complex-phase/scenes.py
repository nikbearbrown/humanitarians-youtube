import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR.update({b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]})
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0,opacity=0)
def plane(center=ORIGIN,scale=1): return VGroup(Line(LEFT*2.8*scale,RIGHT*2.8*scale,color=INK),Line(DOWN*2.8*scale,UP*2.8*scale,color=INK)).move_to(center)

class B02_AddThenSquare(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg()); title=Text("ADD AMPLITUDES — THEN SQUARE THE LENGTH",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35)
  source=Dot(LEFT*6,color=CRIMSON,radius=.16); barrier=VGroup(Line(LEFT*2+DOWN*3,LEFT*2+DOWN*.5,color=INK,stroke_width=5),Line(LEFT*2+UP*.5,LEFT*2+UP*1.2,color=INK,stroke_width=5),Line(LEFT*2+UP*2.2,LEFT*2+UP*3,color=INK,stroke_width=5)); screen=Line(RIGHT*6+DOWN*3,RIGHT*6+UP*3,color=TEAL,stroke_width=5); point=Dot(RIGHT*6+UP*.8,color=CRIMSON,radius=.14); paths=VGroup(Line(source.get_center(),LEFT*2+UP*1.7,color=TEAL),Line(LEFT*2+UP*1.7,point.get_center(),color=TEAL),Line(source.get_center(),LEFT*2,color=CRIMSON),Line(LEFT*2,point.get_center(),color=CRIMSON)); eq=Text("P = | ψ₁ + ψ₂ |²",font=MONO,font_size=38,color=INK).move_to(DOWN*3.25)
  self.play(FadeIn(title),FadeIn(source),FadeIn(barrier),FadeIn(screen),FadeIn(point),run_time=1); self.play(LaggedStart(*[Create(x) for x in paths],lag_ratio=.12),FadeIn(eq),run_time=1.3); self.wait(max(.1,d-2.3))
class B03_Reinforce(Scene):
 def construct(self):
  d=DUR.get("B03",9); self.add(bg()); title=Text("RELATIVE PHASE 0°: REINFORCEMENT",font=DISPLAY,font_size=32,color=INK).move_to(UP*3.35); p=plane(); a=Arrow(ORIGIN,RIGHT*2,color=TEAL,buff=0); b=Arrow(RIGHT*2,RIGHT*4,color=CRIMSON,buff=0); result=Arrow(ORIGIN,RIGHT*4,color=INK,buff=0,stroke_width=7); lab=Text("|ψ₁ + ψ₂| = 2A   →   BRIGHT",font=MONO,font_size=28,color=INK).move_to(DOWN*2.7)
  self.play(FadeIn(title),Create(p),GrowArrow(a),run_time=1); self.play(GrowArrow(b),run_time=.7); self.play(GrowArrow(result),FadeIn(lab),run_time=.7); self.wait(max(.1,d-2.4))
class B04_Cancel(Scene):
 def construct(self):
  d=DUR.get("B04",9); self.add(bg()); title=Text("RELATIVE PHASE 180°: CANCELLATION",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35); p=plane(); a=Arrow(ORIGIN,RIGHT*2,color=TEAL,buff=0); b=Arrow(RIGHT*2,ORIGIN,color=CRIMSON,buff=0); zero=Dot(ORIGIN,color=INK,radius=.18); lab=Text("ψ₁ + ψ₂ = 0   →   DARK",font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*2.7)
  self.play(FadeIn(title),Create(p),GrowArrow(a),run_time=1); self.play(GrowArrow(b),run_time=.8); self.play(Flash(zero,color=CRIMSON),FadeIn(zero),FadeIn(lab),run_time=.8); self.wait(max(.1,d-2.6))
class B05_ContinuousAngles(Scene):
 def construct(self):
  d=DUR.get("B05",7); self.add(bg()); ring=Circle(radius=2.2,color=TEAL); dots=VGroup(*[Dot(ring.point_at_angle(a),color=CRIMSON,radius=.1) for a in np.linspace(0,TAU,16,endpoint=False)]); t=Text("THE SCREEN NEEDS EVERY RELATIVE ANGLE",font=DISPLAY,font_size=35,color=INK).move_to(DOWN*3); self.add(ring,dots,t); self.wait(d)
class B06_UnitPhase(Scene):
 def construct(self):
  d=DUR.get("B06",11); self.add(bg()); title=Text("eⁱᶲ ROTATES WITHOUT CHANGING LENGTH",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35); p=plane(); ring=Circle(radius=2.2,color=TEAL); arrow=Arrow(ORIGIN,RIGHT*2.2,color=CRIMSON,buff=0,stroke_width=6); tracker=ValueTracker(0); arrow.add_updater(lambda m:m.become(Arrow(ORIGIN,2.2*np.array([np.cos(tracker.get_value()),np.sin(tracker.get_value()),0]),color=CRIMSON,buff=0,stroke_width=6))); lab=Text("|eⁱᶲ| = 1",font=MONO,font_size=33,color=INK).move_to(RIGHT*4+UP*2)
  self.play(FadeIn(title),Create(p),Create(ring),GrowArrow(arrow),FadeIn(lab),run_time=1.3); self.play(tracker.animate.set_value(TAU),run_time=2.5,rate_func=linear); arrow.clear_updaters(); self.wait(max(.1,d-3.8))
class B07_RotatingSum(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg()); title=Text("TURN ONE PHASOR — WATCH THE SUM BREATHE",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); p=plane(); a=Arrow(ORIGIN,RIGHT*1.8,color=TEAL,buff=0); tracker=ValueTracker(0); b=always_redraw(lambda:Arrow(RIGHT*1.8,RIGHT*1.8+1.8*np.array([np.cos(tracker.get_value()),np.sin(tracker.get_value()),0]),color=CRIMSON,buff=0)); s=always_redraw(lambda:Arrow(ORIGIN,RIGHT*1.8+1.8*np.array([np.cos(tracker.get_value()),np.sin(tracker.get_value()),0]),color=INK,buff=0,stroke_width=7)); lab=DecimalNumber(3.6,num_decimal_places=2,font_size=30,color=INK).move_to(DOWN*2.8); lab.add_updater(lambda m:m.set_value(np.linalg.norm(s.get_end()-s.get_start())))
  self.play(FadeIn(title),Create(p),GrowArrow(a),FadeIn(b),FadeIn(s),FadeIn(lab),run_time=1.2); self.play(tracker.animate.set_value(TAU),run_time=4,rate_func=linear); self.wait(max(.1,d-5.2))
class B08_Fringe(Scene):
 def construct(self):
  d=DUR.get("B08",11); self.add(bg()); title=Text("SQUARE THE SUM → BRIGHT AND DARK FRINGES",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); ax=Axes(x_range=[-3.2,3.2,1],y_range=[0,2.2,.5],x_length=11,y_length=5.4,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.4); curve=ax.plot(lambda x:2*np.cos(2.4*x)**2,x_range=[-3.2,3.2],color=CRIMSON,stroke_width=5); zeros=VGroup(*[Dot(ax.c2p(x,0),color=TEAL,radius=.11) for x in (-5*np.pi/4.8,-3*np.pi/4.8,-np.pi/4.8,np.pi/4.8,3*np.pi/4.8,5*np.pi/4.8)]); lab=Text("P ∝ cos²(Δφ / 2)",font=MONO,font_size=29,color=INK).move_to(UP*2.35)
  self.play(FadeIn(title),Create(ax),FadeIn(lab),run_time=1); self.play(Create(curve),LaggedStart(*[GrowFromCenter(z) for z in zeros],lag_ratio=.12),run_time=1.8); self.wait(max(.1,d-2.8))
class B09_LineVsPlane(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg()); title=Text("ONE REAL COORDINATE VS A COMPLEX PLANE",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); line=Line(LEFT*6,LEFT*.7,color=INK,stroke_width=4); ends=VGroup(Text("−",font=DISPLAY,font_size=35,color=CRIMSON).next_to(line,LEFT),Text("+",font=DISPLAY,font_size=35,color=TEAL).next_to(line,RIGHT)); p=plane(RIGHT*3.4,.75); ring=Circle(radius=1.65,color=CRIMSON).move_to(RIGHT*3.4); labels=VGroup(Text("real line",font=MONO,font_size=23,color=INK).move_to(LEFT*3.3+DOWN*2),Text("continuous phase",font=MONO,font_size=23,color=INK).move_to(RIGHT*3.4+DOWN*2.5))
  self.play(FadeIn(title),Create(line),FadeIn(ends),run_time=.8); self.play(Create(p),Create(ring),FadeIn(labels),run_time=1.2); self.wait(max(.1,d-2))
class B10_DoubleDimension(Scene):
 def construct(self):
  d=DUR.get("B10",11); self.add(bg()); title=Text("REAL REFORMULATION? DOUBLE THE DIMENSION",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35); z=RoundedRectangle(width=4,height=2.4,corner_radius=.15).set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(LEFT*3.5); pair=RoundedRectangle(width=5,height=2.4,corner_radius=.15).set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(RIGHT*3.5); zt=Text("z = a + ib\n1 complex coordinate",font=MONO,font_size=28,color=CRIMSON,line_spacing=1.2).move_to(z); pt=Text("(a, b)\n2 real coordinates",font=MONO,font_size=28,color=TEAL,line_spacing=1.2).move_to(pair); arrow=Arrow(z.get_right(),pair.get_left(),color=INK); sub=Text("the imaginary part returns as geometry",font=SERIF,font_size=28,color=INK).move_to(DOWN*2.5)
  self.play(FadeIn(title),FadeIn(z),FadeIn(zt),run_time=.8); self.play(GrowArrow(arrow),FadeIn(pair),FadeIn(pt),FadeIn(sub),run_time=1.1); self.wait(max(.1,d-1.9))
class B11_PhaseGenerator(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg()); top=Text("i IS NOT DECORATION",font=DISPLAY,font_size=41,color=CRIMSON).move_to(UP*1.5); mid=Text("i generates continuous phase rotation",font=MONO,font_size=30,color=INK); bot=Text("relative phase is what interference measures",font=SERIF,font_size=29,color=TEAL).move_to(DOWN*1.5); self.add(top,mid,bot); self.wait(d)
