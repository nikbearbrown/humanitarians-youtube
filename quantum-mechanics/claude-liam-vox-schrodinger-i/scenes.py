import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR.update({b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]})
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0,opacity=0)
def mini_axes(center): return Axes(x_range=[-4,4,1],y_range=[-1.5,1.5,.5],x_length=6,y_length=3.6,axis_config={"color":INK,"include_ticks":False}).move_to(center)

class B02_TwoEquations(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg()); title=Text("SAME SPATIAL CURVATURE — DIFFERENT TIME RULE",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35); l=RoundedRectangle(width=6,height=3,corner_radius=.15).set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(LEFT*3.4); r=l.copy().set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(RIGHT*3.4); lt=Text("DIFFUSION\n∂u/∂t = D ∂²u/∂x²",font=MONO,font_size=27,color=CRIMSON,line_spacing=1.3).move_to(l); rt=Text("SCHRÖDINGER\ni h-bar ∂ψ/∂t = … ∂²ψ/∂x²",font=MONO,font_size=25,color=TEAL,line_spacing=1.3).move_to(r); self.play(FadeIn(title),FadeIn(l),FadeIn(r),FadeIn(lt),FadeIn(rt),run_time=1.2); self.wait(max(.1,d-1.2))
class B03_DecayingMode(Scene):
 def construct(self):
  d=DUR.get("B03",10); self.add(bg()); title=Text("DIFFUSION: ONE MODE SHRINKS AS exp(−Dk²t)",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35); a=Axes(x_range=[-6,6,1],y_range=[-1.5,1.5,.5],x_length=12,y_length=5,axis_config={"color":INK,"include_ticks":False}).shift(DOWN*.4); tracker=ValueTracker(1); wave=always_redraw(lambda:a.plot(lambda x:tracker.get_value()*np.sin(2*x),x_range=[-6,6],color=CRIMSON,stroke_width=4)); meter=DecimalNumber(1,num_decimal_places=2,font_size=30,color=CRIMSON).move_to(UP*2.3+RIGHT*4.5); meter.add_updater(lambda m:m.set_value(tracker.get_value()))
  self.play(FadeIn(title),Create(a),FadeIn(wave),FadeIn(meter),run_time=1); self.play(tracker.animate.set_value(.08),run_time=3,rate_func=linear); self.wait(max(.1,d-4))
class B04_HighKSmoothing(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg()); title=Text("SHARP RIPPLES DIE FIRST",font=DISPLAY,font_size=35,color=INK).move_to(UP*3.35); a1=mini_axes(LEFT*3.5); a2=mini_axes(RIGHT*3.5); low=a1.plot(lambda x:np.sin(x),x_range=[-4,4],color=TEAL,stroke_width=4); high=a2.plot(lambda x:np.sin(3*x),x_range=[-4,4],color=CRIMSON,stroke_width=4); labels=VGroup(Text("low k: slow decay",font=MONO,font_size=22,color=TEAL).next_to(a1,DOWN),Text("high k: fast decay",font=MONO,font_size=22,color=CRIMSON).next_to(a2,DOWN)); self.play(FadeIn(title),Create(a1),Create(a2),Create(low),Create(high),FadeIn(labels),run_time=1.4); self.play(high.animate.stretch(.12,dim=1,about_point=a2.c2p(0,0)),run_time=1.5); self.wait(max(.1,d-2.9))
class B05_Contraction(Scene):
 def construct(self):
  d=DUR.get("B05",7); self.add(bg()); self.add(Text("WITHOUT i: MAGNITUDES CONTRACT\nFINE STRUCTURE IS SMOOTHED AWAY",font=DISPLAY,font_size=36,color=INK,line_spacing=1.3)); self.wait(d)
class B06_PhaseCircle(Scene):
 def construct(self):
  d=DUR.get("B06",11); self.add(bg()); title=Text("WITH i: THE MODE ROTATES, |PHASE| STAYS 1",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); axes=VGroup(Line(LEFT*3,RIGHT*3,color=INK),Line(DOWN*3,UP*3,color=INK)); ring=Circle(radius=2.2,color=TEAL); t=ValueTracker(0); arrow=always_redraw(lambda:Arrow(ORIGIN,2.2*np.array([np.cos(t.get_value()),np.sin(t.get_value()),0]),color=CRIMSON,buff=0,stroke_width=7)); lab=Text("exp(−iωt)",font=MONO,font_size=32,color=INK).move_to(RIGHT*4.5+UP*2)
  self.play(FadeIn(title),Create(axes),Create(ring),FadeIn(arrow),FadeIn(lab),run_time=1.2); self.play(t.animate.set_value(-TAU),run_time=3,rate_func=linear); self.wait(max(.1,d-4.2))
class B07_RelativePhases(Scene):
 def construct(self):
  d=DUR.get("B07",10); self.add(bg()); title=Text("DIFFERENT k MODES ROTATE AT DIFFERENT RATES",font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35); centers=(LEFT*4,ORIGIN,RIGHT*4); speeds=(1,2,3); tracker=ValueTracker(0); rings=VGroup(*[Circle(radius=1.25,color=TEAL).move_to(c) for c in centers]); arrows=VGroup(*[always_redraw(lambda c=c,s=s:Arrow(c,c+1.25*np.array([np.cos(s*tracker.get_value()),np.sin(s*tracker.get_value()),0]),color=CRIMSON,buff=0)) for c,s in zip(centers,speeds)]); sumlab=Text("relative phase → motion • interference • reshaping",font=MONO,font_size=24,color=INK).move_to(DOWN*2.8)
  self.play(FadeIn(title),FadeIn(rings),FadeIn(arrows),FadeIn(sumlab),run_time=1); self.play(tracker.animate.set_value(TAU),run_time=3,rate_func=linear); self.wait(max(.1,d-4))
class B08_BothSpread(Scene):
 def construct(self):
  d=DUR.get("B08",10); self.add(bg()); title=Text("BOTH CAN SPREAD — ONLY ONE IS UNITARY",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.35); a1=mini_axes(LEFT*3.5); a2=mini_axes(RIGHT*3.5); narrow1=a1.plot(lambda x:np.exp(-x*x),x_range=[-4,4],color=CRIMSON,stroke_width=3); narrow2=a2.plot(lambda x:np.exp(-x*x),x_range=[-4,4],color=TEAL,stroke_width=3); wide1=a1.plot(lambda x:.45*np.exp(-x*x/5),x_range=[-4,4],color=CRIMSON,stroke_width=5); wide2=a2.plot(lambda x:.65*np.exp(-x*x/5),x_range=[-4,4],color=TEAL,stroke_width=5); labs=VGroup(Text("diffusion: smoothing",font=MONO,font_size=22,color=CRIMSON).next_to(a1,DOWN),Text("quantum: phase-coherent",font=MONO,font_size=22,color=TEAL).next_to(a2,DOWN)); self.play(FadeIn(title),Create(a1),Create(a2),Create(narrow1),Create(narrow2),run_time=1.2); self.play(Transform(narrow1,wide1),Transform(narrow2,wide2),FadeIn(labs),run_time=1.5); self.wait(max(.1,d-2.7))
class B09_Reversal(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg()); title=Text("IDEAL SCHRÖDINGER EVOLUTION CAN UNWIND",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35); timeline=Line(LEFT*5.5,RIGHT*5.5,color=INK,stroke_width=4); dots=VGroup(*[Dot(LEFT*5+RIGHT*i*2.5,color=TEAL,radius=.13) for i in range(5)]); fwd=Arrow(LEFT*4.8,RIGHT*4.8,color=TEAL); back=Arrow(RIGHT*4.8,LEFT*4.8,color=CRIMSON).shift(DOWN*1.2); labels=VGroup(Text("phase winds",font=MONO,font_size=24,color=TEAL).next_to(fwd,UP),Text("reverse time: phase unwinds",font=MONO,font_size=24,color=CRIMSON).next_to(back,DOWN),Text("diffusion backward: errors explode",font=MONO,font_size=23,color=INK).move_to(DOWN*3))
  self.play(FadeIn(title),Create(timeline),FadeIn(dots),GrowArrow(fwd),FadeIn(labels[0]),run_time=1); self.play(GrowArrow(back),FadeIn(labels[1]),FadeIn(labels[2]),run_time=1); self.wait(max(.1,d-2))
class B10_SpiralVsCircle(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg()); title=Text("CONTRACTION VS ROTATION",font=DISPLAY,font_size=35,color=INK).move_to(UP*3.35); c1=LEFT*3.5; c2=RIGHT*3.5; ring1=Circle(radius=2,color=INK,stroke_opacity=.25).move_to(c1); ring2=Circle(radius=2,color=TEAL).move_to(c2); spiral=ParametricFunction(lambda t:c1+np.exp(-.12*t)*2*np.array([np.cos(t),np.sin(t),0]),t_range=[0,5*PI,.04],color=CRIMSON,stroke_width=4); arrow=Arrow(c2,c2+RIGHT*2,color=CRIMSON,buff=0); labs=VGroup(Text("diffusion",font=MONO,font_size=25,color=CRIMSON).move_to(c1+DOWN*2.7),Text("quantum phase",font=MONO,font_size=25,color=TEAL).move_to(c2+DOWN*2.7)); self.play(FadeIn(title),Create(ring1),Create(ring2),run_time=.8); self.play(Create(spiral),GrowArrow(arrow),FadeIn(labs),run_time=1.6); self.play(Rotate(arrow,angle=TAU,about_point=c2),run_time=2); self.wait(max(.1,d-4.4))
class B11_Switch(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg()); top=Text("i IS THE ALGEBRAIC SWITCH",font=DISPLAY,font_size=40,color=CRIMSON).move_to(UP*1.5); mid=Text("dissipative contraction  →  norm-preserving rotation",font=MONO,font_size=28,color=INK); bot=Text("coherent superposition survives through time",font=SERIF,font_size=29,color=TEAL).move_to(DOWN*1.5); self.add(top,mid,bot); self.wait(d)
