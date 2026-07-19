import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR.update({b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]})
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0,opacity=0)
def ball(radius=2):
 c=Circle(radius=radius,color=TEAL,stroke_width=4).set_fill(TEAL,.06); mer=Ellipse(width=radius*.7,height=radius*2,color=TEAL,stroke_opacity=.45); equ=Ellipse(width=radius*2,height=radius*.65,color=TEAL,stroke_opacity=.45); return VGroup(c,mer,equ)

class B02_ClassicalCartoon(Scene):
 def construct(self):
  d=DUR.get("B02",9); self.add(bg()); title=Text("THE TEMPTING CARTOON",font=DISPLAY,font_size=35,color=INK).move_to(UP*3.35); b=ball(2); dot=Dot(RIGHT*2,color=CRIMSON,radius=.15); arrow=CurvedArrow(UP*2.3+LEFT*.7,UP*2.3+RIGHT*.7,angle=-PI/2,color=CRIMSON); labels=VGroup(Text("charged material sphere",font=MONO,font_size=24,color=TEAL).move_to(DOWN*2.8),Text("literal rotation",font=MONO,font_size=23,color=CRIMSON).next_to(arrow,UP))
  self.play(FadeIn(title),Create(b),GrowFromCenter(dot),Create(arrow),FadeIn(labels),run_time=1.4); self.play(Rotate(b,angle=PI),MoveAlongPath(dot,Circle(radius=2)),run_time=2); self.wait(max(.1,d-3.4))
class B03_RadiusAssumption(Scene):
 def construct(self):
  d=DUR.get("B03",11); self.add(bg()); title=Text("ASSUME r = 2.82 FEMTOMETERS",font=DISPLAY,font_size=34,color=INK).move_to(UP*3.35); b=ball(2); radius=DoubleArrow(ORIGIN,RIGHT*2,color=CRIMSON,buff=.05); rlab=Text("2.82 × 10⁻¹⁵ m",font=MONO,font_size=29,color=CRIMSON).next_to(radius,UP); note=Text("classical electromagnetic length scale\nNOT a measured material surface",font=MONO,font_size=25,color=INK,line_spacing=1.25).move_to(DOWN*2.8)
  self.play(FadeIn(title),Create(b),GrowFromCenter(radius),FadeIn(rlab),run_time=1.2); self.play(FadeIn(note),run_time=.7); self.wait(max(.1,d-1.9))
class B04_CharitableTarget(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg()); title=Text("GIVE THE CARTOON CHARITABLE ASSUMPTIONS",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35); l=RoundedRectangle(width=5.4,height=2.8,corner_radius=.15).set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(LEFT*3.2); r=l.copy().set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(RIGHT*3.2); lt=Text("UNIFORM\nSOLID SPHERE",font=DISPLAY,font_size=31,color=TEAL,line_spacing=1.2).move_to(l); rt=Text("TARGET ONLY\nL = h-bar / 2",font=DISPLAY,font_size=29,color=CRIMSON,line_spacing=1.2).move_to(r); sub=Text("one spin projection — not the larger spin magnitude",font=MONO,font_size=22,color=INK).move_to(DOWN*2.8)
  self.play(FadeIn(title),FadeIn(l),FadeIn(r),FadeIn(lt),FadeIn(rt),FadeIn(sub),run_time=1.1); self.wait(max(.1,d-1.1))
class B05_ClassicalRelations(Scene):
 def construct(self):
  d=DUR.get("B05",8); self.add(bg()); box=RoundedRectangle(width=12.5,height=2.6,corner_radius=.15).set_fill(TEAL,.07).set_stroke(TEAL,2); eq=Text("L = I omega     •     v_rim = omega r",font=MONO,font_size=36,color=INK); note=Text("classical rotating-body relations",font=SERIF,font_size=27,color=CRIMSON).move_to(DOWN*2.4); self.add(box,eq,note); self.wait(d)
class B06_Substitution(Scene):
 def construct(self):
  d=DUR.get("B06",11); self.add(bg()); title=Text("THE NUMBERS FORCE A SUPERLUMINAL RIM",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35); inputs=VGroup(Text("h-bar = 1.055×10⁻³⁴ J·s",font=MONO,font_size=23,color=TEAL),Text("m_e = 9.11×10⁻³¹ kg",font=MONO,font_size=23,color=TEAL),Text("r = 2.82×10⁻¹⁵ m",font=MONO,font_size=23,color=TEAL)).arrange(DOWN,buff=.45).move_to(LEFT*3.8); arrow=Arrow(LEFT*.8,RIGHT*.8,color=INK); formula=Text("v = 5 h-bar / (4 m_e r)",font=MONO,font_size=30,color=CRIMSON).move_to(RIGHT*3.4+UP*1); answer=Text("≈ 5.1 × 10¹⁰ m/s",font=MONO,font_size=35,color=INK).move_to(RIGHT*3.4+DOWN*.7)
  self.play(FadeIn(title),LaggedStart(*[FadeIn(x) for x in inputs],lag_ratio=.15),run_time=1); self.play(GrowArrow(arrow),FadeIn(formula),FadeIn(answer),run_time=1); self.wait(max(.1,d-2))
class B07_SpeedGauge(Scene):
 def construct(self):
  d=DUR.get("B07",9); self.add(bg()); title=Text("THE GAUGE DOES NOT SURVIVE",font=DISPLAY,font_size=35,color=INK).move_to(UP*3.35); arc=Arc(radius=2.6,start_angle=0,angle=PI,color=INK,stroke_width=8); ticks=VGroup(*[Line(2.35*np.array([np.cos(a),np.sin(a),0]),2.7*np.array([np.cos(a),np.sin(a),0]),color=(CRIMSON if i==1 else INK),stroke_width=4) for i,a in enumerate(np.linspace(PI,0,7))]); cmark=Text("c",font=MONO,font_size=30,color=CRIMSON).move_to(2.9*np.array([np.cos(5*PI/6),np.sin(5*PI/6),0])); needle=Arrow(ORIGIN,2.1*LEFT,color=TEAL,buff=0,stroke_width=8); value=Text("170 c",font=DISPLAY,font_size=56,color=CRIMSON).move_to(DOWN*2); smash=Line(LEFT*3.5,RIGHT*3.5,color=CRIMSON,stroke_width=10).rotate(-.2)
  self.play(FadeIn(title),Create(arc),FadeIn(ticks),FadeIn(cmark),GrowArrow(needle),run_time=1); self.play(Rotate(needle,angle=-5*PI/6,about_point=ORIGIN),run_time=1.5); self.play(Create(smash),FadeIn(value),run_time=.7); self.wait(max(.1,d-3.2))
class B08_RelativityImpact(Scene):
 def construct(self):
  d=DUR.get("B08",9); self.add(bg()); top=Text("MATERIAL MOTION CANNOT EXCEED c",font=DISPLAY,font_size=39,color=CRIMSON).move_to(UP*1.2); bot=Text("THE LITERAL SPHERE CONTRADICTS RELATIVITY",font=DISPLAY,font_size=31,color=INK).move_to(DOWN*1.2); self.add(top,bot); self.wait(d)
class B09_ShrinkWorsens(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg()); title=Text("SHRINKING THE BALL MAKES IT WORSE",font=DISPLAY,font_size=32,color=INK).move_to(UP*3.35); big=Circle(radius=1.7,color=TEAL).move_to(LEFT*3.5); small=Circle(radius=.8,color=CRIMSON).move_to(RIGHT*3.5); arr=Arrow(LEFT*1.2,RIGHT*1.2,color=INK); labs=VGroup(Text("r",font=MONO,font_size=29,color=TEAL).move_to(LEFT*3.5),Text("r / 2",font=MONO,font_size=29,color=CRIMSON).move_to(RIGHT*3.5),Text("v",font=MONO,font_size=27,color=TEAL).next_to(big,DOWN),Text("2v",font=MONO,font_size=32,color=CRIMSON).next_to(small,DOWN)); eq=Text("v ∝ 1 / r",font=MONO,font_size=36,color=INK).move_to(DOWN*3)
  self.play(FadeIn(title),Create(big),FadeIn(labs[0]),FadeIn(labs[2]),run_time=.8); self.play(GrowArrow(arr),TransformFromCopy(big,small),FadeIn(labs[1]),FadeIn(labs[3]),FadeIn(eq),run_time=1.1); self.wait(max(.1,d-1.9))
class B10_RealSpin(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg()); title=Text("SPIN IS REAL ANGULAR MOMENTUM",font=DISPLAY,font_size=33,color=INK).move_to(UP*3.35); magnet=VGroup(RoundedRectangle(width=2.5,height=4,corner_radius=.3).set_fill(TEAL,.08).set_stroke(TEAL,3),Text("N\n\nS",font=DISPLAY,font_size=32,color=INK)).move_to(LEFT*4); beam=Arrow(LEFT*2.5,RIGHT*1,color=INK); spots=VGroup(Dot(RIGHT*4+UP*1.2,color=CRIMSON,radius=.22),Dot(RIGHT*4+DOWN*1.2,color=TEAL,radius=.22)); labels=VGroup(Text("+h-bar/2",font=MONO,font_size=22,color=CRIMSON).next_to(spots[0],RIGHT),Text("−h-bar/2",font=MONO,font_size=22,color=TEAL).next_to(spots[1],RIGHT),Text("quantized projections",font=MONO,font_size=23,color=INK).move_to(DOWN*3))
  self.play(FadeIn(title),FadeIn(magnet),GrowArrow(beam),run_time=1); self.play(FadeIn(spots),FadeIn(labels),run_time=.9); self.wait(max(.1,d-1.9))
class B11_Intrinsic(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg()); title=Text("KEEP THE WORD — RETIRE THE MECHANISM",font=DISPLAY,font_size=30,color=INK).move_to(UP*3); l=RoundedRectangle(width=5.7,height=2.8,corner_radius=.15).set_fill(CRIMSON,.06).set_stroke(CRIMSON,2).move_to(LEFT*3.2); r=l.copy().set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(RIGHT*3.2); lt=Text("NOT\nmaterial rotation",font=DISPLAY,font_size=31,color=CRIMSON,line_spacing=1.2).move_to(l); rt=Text("INTRINSIC\nquantum property",font=DISPLAY,font_size=31,color=TEAL,line_spacing=1.2).move_to(r); self.add(title,l,r,lt,rt); self.wait(d)
