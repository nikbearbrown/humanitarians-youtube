import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35)
def level(y,label,col=INK):
 l=Line(LEFT*3,RIGHT*3,color=col,stroke_width=4).move_to(UP*y); t=Text(label,font=MONO,font_size=22,color=col).next_to(l,RIGHT); return VGroup(l,t)

class B02_CurrentDips(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg(),ttl("COLLECTOR CURRENT: RISE, DIP, REPEAT")); ax=Axes(x_range=[0,16,2],y_range=[0,1.3,.2],x_length=11,y_length=5,tips=True).move_to(DOWN*.35); xs=np.linspace(0,16,500); pts=[ax.c2p(x,.16+.75*((x%4.9)/4.9)+.012*x) for x in xs]; curve=VMobject(color=TEAL,stroke_width=4).set_points_as_corners(pts); dips=VGroup(*[DashedLine(ax.c2p(x,0),ax.c2p(x,1.1),color=CRIMSON) for x in [4.9,9.8,14.7]]); labels=VGroup(Text("accelerating voltage",font=MONO,font_size=21,color=INK).next_to(ax,DOWN),Text("current",font=MONO,font_size=21,color=INK).next_to(ax,LEFT),Text("spacing ≈ 4.9 V",font=MONO,font_size=23,color=CRIMSON).move_to(UP*2.4)); self.play(Create(ax),run_time=.7); self.play(Create(curve),FadeIn(dips),FadeIn(labels),run_time=1.1); self.wait(max(.1,d-1.8))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",8); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=22,color=SLATE).move_to(UP*2.4),Text("Why can mercury absorb about 4.9 eV,\nbut not an arbitrary smaller amount?",font=SERIF,font_size=38,color=INK,line_spacing=1.3)); self.wait(d)

class B04_ContinuumGuess(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg(),ttl("CLASSICAL GUESS: A CONTINUUM OF ENERGY TRANSFERS")); bar=Rectangle(width=11,height=1,color=SLATE,fill_color=SLATE,fill_opacity=.15); grad=VGroup(*[Rectangle(width=.22,height=.75,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.15+.015*i).move_to(LEFT*5.2+RIGHT*.22*i) for i in range(48)]); labs=VGroup(Text("small transfer",font=MONO,font_size=22,color=INK).move_to(LEFT*4+DOWN*1.2),Text("any amount allowed",font=MONO,font_size=24,color=CRIMSON).move_to(DOWN*1.2),Text("large transfer",font=MONO,font_size=22,color=INK).move_to(RIGHT*4+DOWN*1.2)); self.play(GrowFromCenter(bar),FadeIn(grad),run_time=.9); self.play(FadeIn(labs),run_time=.6); self.wait(max(.1,d-1.5))

class B05_MercuryLevels(Scene):
 def construct(self):
  d=DUR.get("B05",10); self.add(bg(),ttl("MERCURY HAS DISCRETE INTERNAL LEVELS")); g=level(-1.5,"ground state"); e=level(1.8,"excited state",TEAL); arr=DoubleArrow(LEFT*3.8+DOWN*1.45,LEFT*3.8+UP*1.75,color=CRIMSON,buff=0); gap=Text("≈ 4.9 eV",font=MONO,font_size=30,color=CRIMSON).next_to(arr,LEFT); empty=Text("no stationary levels in between",font=SERIF,font_size=27,color=INK); self.play(Create(g),Create(e),run_time=.8); self.play(GrowArrow(arr),FadeIn(gap),FadeIn(empty),run_time=.8); self.wait(max(.1,d-1.6))

class B06_ClosedChannel(Scene):
 def construct(self):
  d=DUR.get("B06",5); self.add(bg(),Text("BELOW 4.9 eV",font=DISPLAY,font_size=27,color=SLATE).move_to(UP*1.8),Text("excitation channel",font=SERIF,font_size=39,color=INK),Text("CLOSED",font=DISPLAY,font_size=50,color=CRIMSON).move_to(DOWN*1.3)); self.wait(d)

class B07_ElasticBounce(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg(),ttl("SUBTHRESHOLD COLLISION: MOSTLY ELASTIC")); atom=Circle(radius=1.0,color=SLATE,fill_color=SLATE,fill_opacity=.15).move_to(RIGHT*2); electron=Dot(LEFT*5,radius=.28,color=TEAL); incoming=Arrow(LEFT*4.6,RIGHT*.7,color=TEAL,buff=.2,stroke_width=5); outgoing=Arrow(RIGHT*.7,LEFT*4+UP*2,color=TEAL,buff=.2,stroke_width=5); labs=VGroup(Text("K < 4.9 eV",font=MONO,font_size=25,color=TEAL).move_to(LEFT*2+DOWN*.8),Text("atom remains in ground state",font=MONO,font_size=23,color=INK).move_to(RIGHT*2+DOWN*2)); self.play(FadeIn(atom),FadeIn(electron),GrowArrow(incoming),run_time=.8); self.play(GrowArrow(outgoing),FadeIn(labs),run_time=.9); self.wait(max(.1,d-1.7))

class B08_ExcitationTransfer(Scene):
 def construct(self):
  d=DUR.get("B08",11); self.add(bg(),ttl("ABOVE THRESHOLD: ONE EXCITATION QUANTUM TRANSFERS")); g=level(-1.6,"ground"); e=level(1.6,"excited",TEAL); arr=Arrow(DOWN*1.45,UP*1.45,color=CRIMSON,buff=0,stroke_width=5); photon=Text("electron loses ≈ 4.9 eV",font=MONO,font_size=29,color=CRIMSON).move_to(LEFT*3.8); weak=Text("may fail retarding barrier",font=DISPLAY,font_size=25,color=INK).move_to(DOWN*2.8); self.play(Create(g),Create(e),run_time=.7); self.play(GrowArrow(arr),FadeIn(photon),FadeIn(weak),run_time=.9); self.wait(max(.1,d-1.6))

class B09_Recovery(Scene):
 def construct(self):
  d=DUR.get("B09",9); self.add(bg(),ttl("MORE VOLTAGE → CURRENT RECOVERS")); track=Line(LEFT*5.5,RIGHT*5.5,color=INK,stroke_width=3); collision=Dot(LEFT*2,radius=.25,color=CRIMSON); electron=Dot(LEFT*5,radius=.22,color=TEAL); collector=Rectangle(width=.35,height=4,color=SLATE,fill_color=SLATE,fill_opacity=.3).move_to(RIGHT*5.5); a1=Arrow(LEFT*4.6,LEFT*2.4,color=TEAL,buff=.1); a2=Arrow(LEFT*1.6,RIGHT*5.1,color=TEAL,buff=.1); labs=VGroup(Text("lose 4.9 eV",font=MONO,font_size=22,color=CRIMSON).next_to(collision,UP),Text("accelerate again",font=MONO,font_size=22,color=TEAL).move_to(RIGHT*1.8+UP*.8),Text("collector reached",font=DISPLAY,font_size=23,color=INK).move_to(RIGHT*4+DOWN*1.3)); self.play(Create(track),FadeIn(electron),FadeIn(collector),GrowArrow(a1),run_time=.8); self.play(FadeIn(collision),GrowArrow(a2),FadeIn(labs),run_time=.9); self.wait(max(.1,d-1.7))

class B10_TwoExcitations(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg(),ttl("ANOTHER 4.9 V: TWO EXCITATIONS CAN OCCUR")); track=Line(LEFT*6,RIGHT*6,color=INK,stroke_width=3); c1=Dot(LEFT*2.6,radius=.25,color=CRIMSON); c2=Dot(RIGHT*2.0,radius=.25,color=CRIMSON); arrs=VGroup(Arrow(LEFT*5.7,LEFT*2.9,color=TEAL,buff=.1),Arrow(LEFT*2.3,RIGHT*1.7,color=TEAL,buff=.1),Arrow(RIGHT*2.3,RIGHT*5.7,color=SLATE,buff=.1)); labs=VGroup(Text("−4.9 eV",font=MONO,font_size=22,color=CRIMSON).next_to(c1,UP),Text("−4.9 eV",font=MONO,font_size=22,color=CRIMSON).next_to(c2,UP),Text("arrives depleted",font=DISPLAY,font_size=24,color=INK).move_to(RIGHT*4+DOWN*1.3)); self.play(Create(track),FadeIn(c1),FadeIn(c2),GrowFromCenter(arrs),FadeIn(labs),run_time=1.1); self.wait(max(.1,d-1.1))

class B11_DipSpacing(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("THE SPACING MEASURES THE EXCITATION ENERGY")); xs=[-4.5,0,4.5]; lines=VGroup(*[Line(UP*1.8,DOWN*1.8,color=CRIMSON,stroke_width=4).move_to(RIGHT*x) for x in xs]); labels=VGroup(*[Text(s,font=MONO,font_size=24,color=INK).next_to(lines[i],DOWN) for i,s in enumerate(["dip n","dip n+1","dip n+2"])]); a1=DoubleArrow(LEFT*4.4,LEFT*.1,color=TEAL,buff=0).shift(UP*2.4); a2=DoubleArrow(RIGHT*.1,RIGHT*4.4,color=TEAL,buff=0).shift(UP*2.4); gaps=VGroup(Text("≈ 4.9 V",font=MONO,font_size=24,color=TEAL).next_to(a1,UP),Text("≈ 4.9 V",font=MONO,font_size=24,color=TEAL).next_to(a2,UP)); note=Text("contact potentials may shift all dips together",font=SERIF,font_size=26,color=INK).move_to(DOWN*2.8); self.play(FadeIn(lines),FadeIn(labels),run_time=.7); self.play(GrowArrow(a1),GrowArrow(a2),FadeIn(gaps),FadeIn(note),run_time=.9); self.wait(max(.1,d-1.6))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("AN ELECTRICAL RULER FOR AN ATOMIC GAP",font=DISPLAY,font_size=27,color=SLATE).move_to(UP*2.3),Text("one allowed excitation quantum",font=SERIF,font_size=39,color=TEAL).move_to(UP*.6),Text("≈ 4.9 eV",font=MONO,font_size=46,color=CRIMSON).move_to(DOWN*.7),Text("or the atom stays in the lower state",font=SERIF,font_size=28,color=INK).move_to(DOWN*2)); self.wait(d)
