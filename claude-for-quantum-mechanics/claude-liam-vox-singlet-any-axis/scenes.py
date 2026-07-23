import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR.update({b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]})
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0,opacity=0)
def analyzer(c,angle=PI/2,color=INK):
 axis=Line(c-2*np.array([np.cos(angle),np.sin(angle),0]),c+2*np.array([np.cos(angle),np.sin(angle),0]),color=color,stroke_width=4)
 return VGroup(Circle(radius=1.2,color=color).move_to(c),axis)
def needle(c,angle,color): return Arrow(c,c+np.array([np.cos(angle),np.sin(angle),0]),color=color,buff=0,stroke_width=6)

class B02_SingletState(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg()); title=Text("ONE JOINT STATE — NOT TWO PRIVATE ARROWS",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); box=RoundedRectangle(width=13,height=2.5,corner_radius=.16).set_fill(TEAL,.06).set_stroke(TEAL,2); eq=Text("|ψ⁻〉 = ( |↑↓〉 − |↓↑〉 ) / √2",font=MONO,font_size=43,color=INK); terms=VGroup(Text("first up • second down",font=MONO,font_size=21,color=TEAL).move_to(LEFT*3+DOWN*2.2),Text("first down • second up",font=MONO,font_size=21,color=CRIMSON).move_to(RIGHT*3+DOWN*2.2))
  self.play(FadeIn(title),Create(box),run_time=.7); self.play(Write(eq),FadeIn(terms),run_time=1.2); self.wait(max(.1,d-1.9))
class B03_ZOutcomes(Scene):
 def construct(self):
  d=DUR.get("B03",10); self.add(bg()); title=Text("MEASURE BOTH ALONG z",font=DISPLAY,font_size=34,color=INK).move_to(UP*3.35); l=RoundedRectangle(width=5.5,height=3,corner_radius=.15).set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(LEFT*3.2); r=l.copy().set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(RIGHT*3.2); lt=Text("↑   ↓\n50%",font=MONO,font_size=40,color=TEAL,line_spacing=1.2).move_to(l); rt=Text("↓   ↑\n50%",font=MONO,font_size=40,color=CRIMSON,line_spacing=1.2).move_to(r); no=Text("↑↑ : 0%      ↓↓ : 0%",font=MONO,font_size=28,color=INK).move_to(DOWN*3)
  self.play(FadeIn(title),FadeIn(l),FadeIn(r),run_time=.8); self.play(FadeIn(lt),FadeIn(rt),FadeIn(no),run_time=.9); self.wait(max(.1,d-1.7))
class B04_LocalVsJoint(Scene):
 def construct(self):
  d=DUR.get("B04",8); self.add(bg()); top=Text("EACH SIDE: 50 / 50 RANDOM",font=DISPLAY,font_size=37,color=CRIMSON).move_to(UP*1.3); bot=Text("THE PAIR: 100% OPPOSITE",font=DISPLAY,font_size=39,color=TEAL).move_to(DOWN*1.2); self.add(top,bot); self.wait(d)
class B05_RotateAnalyzers(Scene):
 def construct(self):
  d=DUR.get("B05",11); self.add(bg()); title=Text("ROTATE BOTH ANALYZERS TOGETHER",font=DISPLAY,font_size=32,color=INK).move_to(UP*3.35); c1=LEFT*3.5; c2=RIGHT*3.5; ang=ValueTracker(PI/2); a1=always_redraw(lambda:analyzer(c1,ang.get_value(),INK)); a2=always_redraw(lambda:analyzer(c2,ang.get_value(),INK)); n1=always_redraw(lambda:needle(c1,ang.get_value(),TEAL)); n2=always_redraw(lambda:needle(c2,ang.get_value()+PI,CRIMSON)); state=Text("|+n,−n〉 − |−n,+n〉",font=MONO,font_size=29,color=INK).move_to(DOWN*3)
  self.play(FadeIn(title),FadeIn(a1),FadeIn(a2),FadeIn(n1),FadeIn(n2),FadeIn(state),run_time=1); self.play(ang.animate.set_value(0),run_time=2); self.play(ang.animate.set_value(PI/3),run_time=1.3); self.wait(max(.1,d-4.3))
class B06_TotalZero(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg()); title=Text("TOTAL ANGULAR MOMENTUM j = 0",font=DISPLAY,font_size=35,color=INK).move_to(UP*3.35); ring=Circle(radius=2.2,color=INK); axes=VGroup(*[Line(2.2*np.array([np.cos(a),np.sin(a),0]),-2.2*np.array([np.cos(a),np.sin(a),0]),color=TEAL,stroke_opacity=.35) for a in np.linspace(0,PI,8,endpoint=False)]); zero=Text("0",font=DISPLAY,font_size=80,color=CRIMSON); lab=Text("NO PREFERRED DIRECTION",font=MONO,font_size=29,color=INK).move_to(DOWN*3)
  self.play(FadeIn(title),Create(ring),FadeIn(zero),run_time=1); self.play(LaggedStart(*[Create(x) for x in axes],lag_ratio=.08),FadeIn(lab),run_time=1.3); self.play(Rotate(axes,angle=PI/4),run_time=1); self.wait(max(.1,d-3.3))
class B07_XOutcomes(Scene):
 def construct(self):
  d=DUR.get("B07",10); self.add(bg()); title=Text("MEASURE BOTH ALONG x — SAME PROMISE",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35); eq=Text("|ψ⁻〉 = ( |+x,−x〉 − |−x,+x〉 ) / √2",font=MONO,font_size=34,color=INK).move_to(UP*1.5); outcomes=VGroup(Text("+x   −x\n50%",font=MONO,font_size=36,color=TEAL,line_spacing=1.2).move_to(LEFT*3+DOWN*.8),Text("−x   +x\n50%",font=MONO,font_size=36,color=CRIMSON,line_spacing=1.2).move_to(RIGHT*3+DOWN*.8)); verdict=Text("same signs: 0%",font=MONO,font_size=27,color=INK).move_to(DOWN*3)
  self.play(FadeIn(title),FadeIn(eq),run_time=.8); self.play(FadeIn(outcomes),FadeIn(verdict),run_time=.9); self.wait(max(.1,d-1.7))
class B08_AnyAxis(Scene):
 def construct(self):
  d=DUR.get("B08",11); self.add(bg()); title=Text("ANY SHARED AXIS n: OPPOSITE EVERY TIME",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); c1=LEFT*3.5; c2=RIGHT*3.5; angle=ValueTracker(.2); a1=always_redraw(lambda:analyzer(c1,angle.get_value(),INK)); a2=always_redraw(lambda:analyzer(c2,angle.get_value(),INK)); n1=always_redraw(lambda:needle(c1,angle.get_value(),TEAL)); n2=always_redraw(lambda:needle(c2,angle.get_value()+PI,CRIMSON)); corr=Text("product of signs = −1",font=MONO,font_size=29,color=INK).move_to(DOWN*3)
  self.play(FadeIn(title),FadeIn(a1),FadeIn(a2),FadeIn(n1),FadeIn(n2),FadeIn(corr),run_time=1); self.play(angle.animate.set_value(2.6),run_time=3,rate_func=linear); self.play(angle.animate.set_value(1.15),run_time=2); self.wait(max(.1,d-6))
class B09_NoHiddenArrow(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg()); title=Text("NO LOCAL POLARIZATION TO REVEAL",font=DISPLAY,font_size=32,color=INK).move_to(UP*3.35); ball=Circle(radius=2,color=TEAL); arrows=VGroup(*[Arrow(ORIGIN,1.5*np.array([np.cos(a),np.sin(a),0]),color=CRIMSON,buff=0) for a in np.linspace(0,TAU,8,endpoint=False)]); cross=VGroup(Line(LEFT*2+UP*2,RIGHT*2+DOWN*2,color=CRIMSON,stroke_width=8),Line(LEFT*2+DOWN*2,RIGHT*2+UP*2,color=CRIMSON,stroke_width=8)); rho=Text("local state = ½ I",font=MONO,font_size=34,color=INK).move_to(DOWN*3)
  self.play(FadeIn(title),Create(ball),FadeIn(arrows),run_time=1); self.play(FadeIn(cross),FadeOut(arrows),FadeIn(rho),run_time=1.2); self.wait(max(.1,d-2.2))
class B10_SpinVsTotal(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg()); title=Text("DO NOT CONFUSE THESE TWO STATEMENTS",font=DISPLAY,font_size=30,color=INK).move_to(UP*3); l=RoundedRectangle(width=5.6,height=2.7,corner_radius=.15).set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(LEFT*3.2); r=l.copy().set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(RIGHT*3.2); lt=Text("EACH PARTICLE\nspin ½",font=DISPLAY,font_size=31,color=TEAL,line_spacing=1.25).move_to(l); rt=Text("THE PAIR\ntotal spin 0",font=DISPLAY,font_size=31,color=CRIMSON,line_spacing=1.25).move_to(r); self.add(title,l,r,lt,rt); self.wait(d)
class B11_RelationalPromise(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg()); title=Text("THE SINGLET'S RELATIONAL PROMISE",font=DISPLAY,font_size=31,color=INK).move_to(UP*3); rows=VGroup(Text("NO PREFERRED AXIS",font=MONO,font_size=28,color=TEAL),Text("RANDOM LOCAL ANSWERS",font=MONO,font_size=28,color=CRIMSON),Text("PERFECTLY OPPOSITE SAME-AXIS PAIRS",font=MONO,font_size=28,color=INK)).arrange(DOWN,buff=.75); self.add(title,rows); self.wait(d)
