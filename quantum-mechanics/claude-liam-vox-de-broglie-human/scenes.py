import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)

class B02_DiffractionMatch(Scene):
 def construct(self):
  d=DUR.get("B02",9); self.add(bg(),ttl("DIFFRACTION NEEDS COMPARABLE SCALES")); wave=VGroup(*[Line(UP*1.5,DOWN*1.5,color=TEAL).move_to(LEFT*4+RIGHT*i*.45) for i in range(7)]); crystal=VGroup(*[Dot(RIGHT*1.5+RIGHT*i*.6+UP*j*.6,radius=.11,color=INK) for i in range(7) for j in range(-2,3)]); eq=Text("wavelength ~ grating spacing",font=MONO,font_size=30,color=CRIMSON).move_to(DOWN*2.5); arr=Arrow(LEFT*1.2,RIGHT*.8,color=SLATE,buff=0); self.play(FadeIn(wave,crystal),GrowArrow(arr),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",6); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=23,color=SLATE).move_to(UP*2.3),Text("What wavelength belongs",font=SERIF,font_size=43,color=INK).move_to(UP*.5),Text("to a walking human?",font=SERIF,font_size=45,color=CRIMSON).move_to(DOWN*.9)); self.wait(d)

class B04_Formula(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg(),ttl("DE BROGLIE'S RELATION")); eqs=VGroup(Text("lambda = h / p",font=MONO,font_size=48,color=TEAL),Text("p = m v",font=MONO,font_size=38,color=INK),Text("lambda = h / (m v)",font=MONO,font_size=42,color=CRIMSON)).arrange(DOWN,buff=.7); self.play(Write(eqs[0]),run_time=.7); self.play(FadeIn(eqs[1]),run_time=.5); self.play(FadeIn(eqs[2]),run_time=.6); self.wait(max(.1,d-1.8))

class B05_Calculate(Scene):
 def construct(self):
  d=DUR.get("B05",11); self.add(bg(),ttl("A 70 kg PERSON WALKING AT 1 m/s")); eqs=VGroup(Text("p = 70 kg m/s",font=MONO,font_size=31,color=INK),Text("lambda = 6.626e-34 / 70",font=MONO,font_size=31,color=INK),Text("lambda ≈ 9.5e-36 m",font=MONO,font_size=45,color=CRIMSON)).arrange(DOWN,buff=.75); self.play(FadeIn(eqs[:2]),run_time=.8); self.play(FadeIn(eqs[2],scale=1.2),run_time=.8); self.wait(max(.1,d-1.6))

class B06_LogScale(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg(),ttl("A LOGARITHMIC WAVELENGTH DROP")); line=Line(LEFT*5.5,RIGHT*5.5,color=INK,stroke_width=3); points=[(-5.2,"atom\n10^-10 m",TEAL),(-3.0,"proton scale\n10^-15 m",INK),(5.2,"human\n10^-35 m",CRIMSON)]; dots=VGroup(*[Dot(np.array([x,0,0]),radius=.18,color=c) for x,_,c in points]); labs=VGroup(*[Text(s,font=MONO,font_size=22,color=c).move_to(np.array([x,-1.1,0])) for x,s,c in points]); gaps=Text("5 orders",font=SERIF,font_size=24,color=INK).move_to(LEFT*4.1+UP*.7); gaps2=Text("20 orders",font=SERIF,font_size=26,color=CRIMSON).move_to(RIGHT*1.1+UP*.7); self.play(Create(line),FadeIn(dots,labs,gaps,gaps2),run_time=1); self.wait(max(.1,d-1))

class B07_Doorway(Scene):
 def construct(self):
  d=DUR.get("B07",10); self.add(bg(),ttl("A ONE-METER DOORWAY IS ENORMOUS TO THIS WAVE")); door=VGroup(Line(LEFT*2+UP*2.5,LEFT*2+DOWN*2.5,color=INK,stroke_width=7),Line(RIGHT*2+UP*2.5,RIGHT*2+DOWN*2.5,color=INK,stroke_width=7),Line(LEFT*2+UP*2.5,RIGHT*2+UP*2.5,color=INK,stroke_width=7)); width=DoubleArrow(LEFT*1.9,RIGHT*1.9,color=TEAL,buff=0).shift(DOWN*1.8); labs=VGroup(Text("a ≈ 1 m",font=MONO,font_size=28,color=TEAL).next_to(width,DOWN),Text("a / lambda ≈ 10^35",font=MONO,font_size=38,color=CRIMSON).move_to(UP*1)); self.play(Create(door),GrowArrow(width),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B08_Angle(Scene):
 def construct(self):
  d=DUR.get("B08",11); self.add(bg(),ttl("THE DIFFRACTION ANGLE IS EFFECTIVELY ZERO")); origin=LEFT*4; center=Line(origin,RIGHT*5,color=INK,stroke_width=3); upper=Line(origin,RIGHT*5+UP*.45,color=CRIMSON,stroke_width=3); arc=Arc(radius=2,start_angle=0,angle=.05,color=TEAL,arc_center=origin); eqs=VGroup(Text("theta ~ lambda / a",font=MONO,font_size=32,color=INK),Text("~ 10^-35 rad",font=MONO,font_size=43,color=CRIMSON)).arrange(DOWN,buff=.6).move_to(UP*2); self.play(Create(center),Create(upper),Create(arc),FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))

class B09_Aperture(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("VISIBLE DIFFRACTION WOULD REQUIRE AN IMPOSSIBLE APERTURE")); scale=VGroup(*[Rectangle(width=w,height=.7,color=c,fill_color=c,fill_opacity=.15) for w,c in [(10,SLATE),(6,TEAL),(2,CRIMSON),(.2,CRIMSON)]]).arrange(DOWN,buff=.5); labs=VGroup(Text("1 m",font=MONO,font_size=22,color=INK).move_to(RIGHT*5.7+UP*1.8),Text("10^-35 m target",font=MONO,font_size=25,color=CRIMSON).move_to(RIGHT*4+DOWN*1.7)); note=Text("not physically realizable for a human",font=SERIF,font_size=29,color=INK).move_to(DOWN*3); self.play(GrowFromCenter(scale),FadeIn(labs,note),run_time=1); self.wait(max(.1,d-1))

class B10_Molecules(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg(),ttl("LARGE MOLECULES CAN STILL DIFFRACT")); molecule=VGroup(*[Dot(np.array([np.cos(a),np.sin(a),0]),radius=.16,color=TEAL) for a in np.linspace(0,TAU,12,endpoint=False)]).move_to(LEFT*3.5); grating=VGroup(*[Rectangle(width=.25,height=4,color=INK,fill_color=INK,fill_opacity=.2).move_to(RIGHT*1.5+RIGHT*i*.65) for i in range(7)]); arrow=Arrow(LEFT*1.8,RIGHT*.8,color=CRIMSON,buff=0); labs=VGroup(Text("picometer wavelength",font=MONO,font_size=24,color=TEAL).move_to(LEFT*3.5+DOWN*2),Text("nanometer grating + coherence",font=MONO,font_size=23,color=INK).move_to(RIGHT*3.5+DOWN*2.6)); self.play(FadeIn(molecule,grating),GrowArrow(arrow),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B11_Decoherence(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("DECOHERENCE IS AN ADDITIONAL OBSTACLE")); person=Circle(radius=1.1,color=TEAL).move_to(LEFT*3); env=VGroup(*[Arrow(RIGHT*4+UP*y,LEFT*.8+UP*(y*.3),color=CRIMSON,buff=.1) for y in [-2,-1,0,1,2]]); labs=VGroup(Text("air · thermal photons · internal motion",font=MONO,font_size=24,color=CRIMSON).move_to(RIGHT*3+DOWN*2.8),Text("path phase leaks to environment",font=SERIF,font_size=29,color=INK).move_to(UP*2.4),Text("but lambda/a already kills the doorway effect",font=SERIF,font_size=27,color=TEAL).move_to(DOWN*2.2)); self.play(FadeIn(person),GrowFromCenter(env),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("QUANTUM MECHANICS STILL APPLIES",font=DISPLAY,font_size=31,color=TEAL).move_to(UP*1.7),Text("human momentum makes lambda ≈ 10^-35 m",font=MONO,font_size=32,color=CRIMSON),Text("the doorway is unimaginably wide in wave units",font=SERIF,font_size=29,color=INK).move_to(DOWN*1.8)); self.wait(d)
