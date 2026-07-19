import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def analyzer(label,center):
 return VGroup(Rectangle(width=1.2,height=2.8,color=SLATE,fill_color=SLATE,fill_opacity=.12).move_to(center),Text(label,font=DISPLAY,font_size=30,color=INK).move_to(center))

class B02_Prepare(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg(),ttl("PREPARE A DEFINITE Z-UP BEAM")); z=analyzer("Z",ORIGIN); inc=Arrow(LEFT*5,LEFT*.8,color=INK,buff=0); up=Arrow(RIGHT*.8,RIGHT*5+UP*1.5,color=TEAL,buff=0,stroke_width=6); down=Arrow(RIGHT*.8,RIGHT*4+DOWN*1.4,color=SLATE,buff=0,stroke_opacity=.25); labs=VGroup(Text("keep Z+",font=MONO,font_size=27,color=TEAL).move_to(RIGHT*4+UP*2.3),Text("discard Z-",font=MONO,font_size=23,color=SLATE).move_to(RIGHT*4+DOWN*2)); self.play(FadeIn(z),GrowArrow(inc),run_time=.6); self.play(GrowArrow(up),GrowArrow(down),FadeIn(labs),run_time=.9); self.wait(max(.1,d-1.5))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",6); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=23,color=SLATE).move_to(UP*2.3),Text("How can measuring X",font=SERIF,font_size=44,color=INK).move_to(UP*.5),Text("destroy certainty in Z?",font=SERIF,font_size=44,color=CRIMSON).move_to(DOWN*.9)); self.wait(d)

class B04_Basis(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg(),ttl("Z-UP IS AN EQUAL SUPERPOSITION IN THE X BASIS")); eq=Text("|Z+> = ( |X+> + |X-> ) / sqrt(2)",font=MONO,font_size=34,color=INK).move_to(UP*1.5); left=Arrow(ORIGIN,LEFT*2+DOWN*1.2,color=CRIMSON,buff=0); right=Arrow(ORIGIN,RIGHT*2+DOWN*1.2,color=CRIMSON,buff=0); labs=VGroup(Text("50% X-",font=MONO,font_size=26,color=CRIMSON).next_to(left,DOWN),Text("50% X+",font=MONO,font_size=26,color=CRIMSON).next_to(right,DOWN)); self.play(Write(eq),run_time=.8); self.play(GrowArrow(left),GrowArrow(right),FadeIn(labs),run_time=.8); self.wait(max(.1,d-1.6))

class B05_XBranches(Scene):
 def construct(self):
  d=DUR.get("B05",10); self.add(bg(),ttl("THE X MEASUREMENT PREPARES A NEW EIGENSTATE")); x=analyzer("X",ORIGIN); inc=Arrow(LEFT*5,LEFT*.8,color=TEAL,buff=0); plus=Arrow(RIGHT*.8,RIGHT*5+UP*1.4,color=CRIMSON,buff=0,stroke_width=6); minus=Arrow(RIGHT*.8,RIGHT*5+DOWN*1.4,color=CRIMSON,buff=0,stroke_width=6); labs=VGroup(Text("X+  1/2",font=MONO,font_size=27,color=CRIMSON).next_to(plus,UP),Text("X-  1/2",font=MONO,font_size=27,color=CRIMSON).next_to(minus,DOWN)); self.play(FadeIn(x),GrowArrow(inc),run_time=.6); self.play(GrowArrow(plus),GrowArrow(minus),FadeIn(labs),run_time=.9); self.wait(max(.1,d-1.5))

class B06_Selected(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg(),ttl("SELECT X+, THEN MEASURE Z")); z=analyzer("Z",ORIGIN); inc=Arrow(LEFT*5,LEFT*.8,color=CRIMSON,buff=0); up=Arrow(RIGHT*.8,RIGHT*5+UP*1.4,color=TEAL,buff=0); down=Arrow(RIGHT*.8,RIGHT*5+DOWN*1.4,color=TEAL,buff=0); labs=VGroup(Text("Z+  50%",font=MONO,font_size=27,color=TEAL).next_to(up,UP),Text("Z-  50%",font=MONO,font_size=27,color=TEAL).next_to(down,DOWN)); self.play(FadeIn(z),GrowArrow(inc),run_time=.6); self.play(GrowArrow(up),GrowArrow(down),FadeIn(labs),run_time=.9); self.wait(max(.1,d-1.5))

class B07_BothBranches(Scene):
 def construct(self):
  d=DUR.get("B07",10); self.add(bg(),ttl("EITHER X OUTCOME GIVES THE SAME Z PROBABILITIES")); rows=[]
  for y,s in [(1.3,"X+"),(-1.3,"X-")]: rows.append(VGroup(Text(s,font=MONO,font_size=27,color=CRIMSON).move_to(LEFT*4+UP*y),Arrow(LEFT*2.8,LEFT*.5+UP*.7,color=TEAL,buff=0).shift(UP*y),Arrow(LEFT*2.8,LEFT*.5+DOWN*.7,color=TEAL,buff=0).shift(UP*y),Text("Z+ 1/2    Z- 1/2",font=MONO,font_size=24,color=INK).move_to(RIGHT*3+UP*y)))
  note=Text("condition or forget X: final Z is 50/50",font=SERIF,font_size=28,color=INK).move_to(DOWN*3); self.play(FadeIn(VGroup(*rows),note),run_time=1); self.wait(max(.1,d-1))

class B08_Sequences(Scene):
 def construct(self):
  d=DUR.get("B08",11); self.add(bg(),ttl("MEASUREMENT ORDER CHANGES THE RESULT")); direct=VGroup(Text("Z+ → Z",font=MONO,font_size=30,color=TEAL),Text("100% Z+",font=DISPLAY,font_size=32,color=TEAL)).arrange(DOWN,buff=.8).move_to(LEFT*3.5); indirect=VGroup(Text("Z+ → X → Z",font=MONO,font_size=30,color=CRIMSON),Text("50% Z+ · 50% Z-",font=DISPLAY,font_size=28,color=CRIMSON)).arrange(DOWN,buff=.8).move_to(RIGHT*3.5); div=Line(UP*2.2,DOWN*2.2,color=SLATE); self.play(FadeIn(direct,indirect),Create(div),run_time=1); self.wait(max(.1,d-1))

class B09_NotReveal(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("X DOES NOT REVEAL A PRE-EXISTING VALUE AND LEAVE Z INTACT")); old=Text("definite Z+",font=MONO,font_size=31,color=TEAL).move_to(LEFT*3.8); new=Text("definite X±",font=MONO,font_size=31,color=CRIMSON).move_to(RIGHT*3.8); arrow=Arrow(LEFT*2.2,RIGHT*2.2,color=INK,buff=.1); lab=Text("measurement changes the state",font=SERIF,font_size=31,color=INK).move_to(DOWN*2); self.play(FadeIn(old,new),GrowArrow(arrow),run_time=.8); self.play(FadeIn(lab),run_time=.7); self.wait(max(.1,d-1.5))

class B10_Incompatible(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg(),ttl("CERTAINTY IS BASIS-DEPENDENT")); axes=VGroup(Arrow(DOWN*2,UP*2,color=TEAL,buff=0),Arrow(LEFT*2,RIGHT*2,color=CRIMSON,buff=0)); labs=VGroup(Text("Z basis",font=MONO,font_size=26,color=TEAL).move_to(UP*2.6),Text("X basis",font=MONO,font_size=26,color=CRIMSON).move_to(RIGHT*2.9),Text("definite on one axis = superposition on the other",font=SERIF,font_size=28,color=INK).move_to(DOWN*3)); self.play(GrowFromCenter(axes),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B11_AngleScan(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("ROTATE THE MIDDLE ANALYZER")); ax=Axes(x_range=[0,90,30],y_range=[.5,1,.1],x_length=9,y_length=4,tips=False).move_to(DOWN*.2); curve=ax.plot(lambda a:.5+.5*np.cos(np.deg2rad(a))**2,x_range=[0,90],color=TEAL); labs=VGroup(Text("middle-axis angle",font=MONO,font_size=23,color=INK).next_to(ax,DOWN),Text("final P(Z+)",font=MONO,font_size=23,color=INK).next_to(ax,LEFT),Text("0°: certain",font=SERIF,font_size=25,color=TEAL).move_to(LEFT*3.8+UP*2.4),Text("90°: 50/50",font=SERIF,font_size=25,color=CRIMSON).move_to(RIGHT*3.8+UP*2.4)); self.play(Create(ax),Create(curve),FadeIn(labs),run_time=1.1); self.wait(max(.1,d-1.1))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("Z+ WAS CERTAIN",font=DISPLAY,font_size=31,color=TEAL).move_to(UP*1.8),Text("X PREPARED A NEW STATE",font=DISPLAY,font_size=31,color=CRIMSON),Text("the final Z measurement splits 50/50",font=SERIF,font_size=31,color=INK).move_to(DOWN*1.8)); self.wait(d)
