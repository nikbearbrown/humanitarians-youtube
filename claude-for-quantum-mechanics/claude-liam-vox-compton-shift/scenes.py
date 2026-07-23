import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35)

class B02_TwoPeaks(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg(),ttl("SCATTERED THROUGH 90°: TWO WAVELENGTH COMPONENTS")); ax=Axes(x_range=[0,10,1],y_range=[0,1.2,.2],x_length=11,y_length=5,tips=True).move_to(DOWN*.3); p1=ax.plot(lambda x:np.exp(-((x-3)/.35)**2),x_range=[0,10],color=SLATE,stroke_width=4); p2=ax.plot(lambda x:.75*np.exp(-((x-7)/.45)**2),x_range=[0,10],color=TEAL,stroke_width=4); labs=VGroup(Text("unshifted λ",font=MONO,font_size=22,color=SLATE).move_to(ax.c2p(3,1.1)),Text("shifted λ'",font=MONO,font_size=22,color=TEAL).move_to(ax.c2p(7,.9)),Text("λ' − λ ≈ 2.43 pm",font=MONO,font_size=24,color=INK).move_to(DOWN*3.25)); self.play(Create(ax),run_time=.7); self.play(Create(p1),Create(p2),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.9))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",8); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=22,color=SLATE).move_to(UP*2.4),Text("Why does part of the scattered beam\nreturn at a longer wavelength?",font=SERIF,font_size=38,color=INK,line_spacing=1.3)); self.wait(d)

class B04_ClassicalPrediction(Scene):
 def construct(self):
  d=DUR.get("B04",10); self.add(bg(),ttl("CLASSICAL DRIVEN OSCILLATOR: SAME FREQUENCY OUT")); e=Dot(radius=.35,color=INK); incoming=Arrow(LEFT*6,e.get_left(),color=CRIMSON,buff=.15,stroke_width=5); outgoing=Arrow(e.get_right(),RIGHT*6,color=CRIMSON,buff=.15,stroke_width=5); waves=VGroup(Text("incoming ν",font=MONO,font_size=25,color=CRIMSON).move_to(LEFT*3+UP*.7),Text("reradiated ν",font=MONO,font_size=25,color=CRIMSON).move_to(RIGHT*3+UP*.7),Text("prediction: λ' = λ",font=MONO,font_size=30,color=INK).move_to(DOWN*2.2)); self.play(GrowArrow(incoming),FadeIn(e),run_time=.8); self.play(GrowArrow(outgoing),FadeIn(waves),run_time=1); self.wait(max(.1,d-1.8))

class B05_PhotonCollision(Scene):
 def construct(self):
  d=DUR.get("B05",11); self.add(bg(),ttl("PHOTON + ELECTRON → PHOTON + RECOILING ELECTRON")); o=LEFT*1.2+DOWN*.4; electron=Dot(o,radius=.32,color=INK); pin=Arrow(LEFT*6,o,color=TEAL,buff=.35,stroke_width=6); pout=Arrow(o,o+RIGHT*4+UP*2.5,color=TEAL,buff=.35,stroke_width=5); recoil=Arrow(o,o+RIGHT*3+DOWN*2.2,color=CRIMSON,buff=.35,stroke_width=5); labs=VGroup(Text("pγ = h/λ",font=MONO,font_size=23,color=TEAL).move_to(LEFT*3+UP*.5),Text("pγ' = h/λ'",font=MONO,font_size=23,color=TEAL).next_to(pout,UP),Text("electron recoil",font=MONO,font_size=23,color=CRIMSON).next_to(recoil,DOWN)); self.play(GrowArrow(pin),FadeIn(electron),run_time=.8); self.play(GrowArrow(pout),GrowArrow(recoil),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-2))

class B06_EnergyCard(Scene):
 def construct(self):
  d=DUR.get("B06",5); self.add(bg(),Text("PHOTON ENERGY LOSS",font=DISPLAY,font_size=24,color=SLATE).move_to(UP*2),Text("electron recoil energy",font=SERIF,font_size=42,color=CRIMSON),Text("↓",font=DISPLAY,font_size=36,color=INK).move_to(DOWN*.9),Text("longer photon wavelength",font=SERIF,font_size=37,color=TEAL).move_to(DOWN*1.8)); self.wait(d)

class B07_MomentumTriangle(Scene):
 def construct(self):
  d=DUR.get("B07",12); self.add(bg(),ttl("MOMENTUM VECTORS MUST CLOSE")); o=LEFT*3+DOWN*1.5; a=Arrow(o,o+RIGHT*7,color=INK,buff=0,stroke_width=5); b=Arrow(o,o+RIGHT*4.3+UP*3.1,color=TEAL,buff=0,stroke_width=5); c=Arrow(b.get_end(),a.get_end(),color=CRIMSON,buff=0,stroke_width=5); arc=Arc(radius=1.15,start_angle=0,angle=np.arctan2(3.1,4.3),arc_center=o,color=GOLD,stroke_width=3); labs=VGroup(Text("pγ",font=MONO,font_size=24,color=INK).next_to(a,DOWN),Text("pγ'",font=MONO,font_size=24,color=TEAL).next_to(b,UP),Text("pe",font=MONO,font_size=24,color=CRIMSON).next_to(c,RIGHT),Text("θ",font=MONO,font_size=25,color=GOLD).move_to(o+RIGHT*1.4+UP*.45)); self.play(GrowArrow(a),run_time=.6); self.play(GrowArrow(b),GrowArrow(c),Create(arc),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.8))

class B08_ShiftFormula(Scene):
 def construct(self):
  d=DUR.get("B08",10); self.add(bg(),ttl("COMPTON SHIFT")); eq=Text("Δλ = λ' − λ = (h / mₑc)(1 − cos θ)",font=MONO,font_size=36,color=TEAL); brace=Line(LEFT*2.1,RIGHT*2.1,color=GOLD,stroke_width=3).move_to(DOWN*.75); lab=Text("λC = h / mₑc = 2.426 pm",font=MONO,font_size=27,color=INK).move_to(DOWN*1.45); note=Text("angle controls the energy transfer",font=SERIF,font_size=28,color=INK).move_to(DOWN*2.65); self.play(FadeIn(eq),run_time=.8); self.play(Create(brace),FadeIn(lab),FadeIn(note),run_time=.8); self.wait(max(.1,d-1.6))

class B09_ZeroNinety(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("LANDMARK ANGLES")); left=VGroup(Text("θ = 0°",font=DISPLAY,font_size=31,color=INK),Text("1 − cos θ = 0",font=MONO,font_size=25,color=INK),Text("Δλ = 0",font=MONO,font_size=34,color=CRIMSON)).arrange(DOWN,buff=.45).move_to(LEFT*3.8); right=VGroup(Text("θ = 90°",font=DISPLAY,font_size=31,color=INK),Text("1 − cos θ = 1",font=MONO,font_size=25,color=INK),Text("Δλ = 2.426 pm",font=MONO,font_size=34,color=TEAL)).arrange(DOWN,buff=.45).move_to(RIGHT*3.8); div=Line(UP*2.5,DOWN*2.5,color=INK,stroke_width=1).set_opacity(.3); self.play(FadeIn(left),FadeIn(right),Create(div),run_time=1.1); self.wait(max(.1,d-1.1))

class B10_Backscatter(Scene):
 def construct(self):
  d=DUR.get("B10",9); self.add(bg(),ttl("BACKSCATTER: THE MAXIMUM SHIFT")); e1=Dot(RIGHT*3+UP*.8,radius=.28,color=INK); inc=Arrow(LEFT*5+UP*.8,e1.get_left(),color=TEAL,buff=.15,stroke_width=5); e2=Dot(RIGHT*3+DOWN*.8,radius=.28,color=INK); out=Arrow(e2.get_left(),LEFT*5+DOWN*.8,color=CRIMSON,buff=.15,stroke_width=5); labs=VGroup(Text("before: photon →",font=MONO,font_size=22,color=TEAL).move_to(LEFT*1.5+UP*1.45),Text("after: photon ←",font=MONO,font_size=22,color=CRIMSON).move_to(LEFT*1.5+DOWN*1.45)); eq=Text("θ = 180°   →   Δλ = 2λC = 4.853 pm",font=MONO,font_size=31,color=INK).move_to(DOWN*2.7); self.play(GrowArrow(inc),FadeIn(e1),run_time=.7); self.play(GrowArrow(out),FadeIn(e2),FadeIn(labs),FadeIn(eq),run_time=.9); self.wait(max(.1,d-1.6))

class B11_AngleCurve(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("SHIFT VS SCATTERING ANGLE")); ax=Axes(x_range=[0,180,30],y_range=[0,2.2,.5],x_length=10.5,y_length=5,tips=True).move_to(DOWN*.3); curve=ax.plot(lambda x:1-np.cos(np.pi*x/180),x_range=[0,180],color=TEAL,stroke_width=5); p0=Dot(ax.c2p(0,0),radius=.12,color=CRIMSON); p90=Dot(ax.c2p(90,1),radius=.12,color=CRIMSON); p180=Dot(ax.c2p(180,2),radius=.12,color=CRIMSON); pts=VGroup(p0,p90,p180); labels=VGroup(Text("0°",font=MONO,font_size=19,color=INK).next_to(p0,UP),Text("90°",font=MONO,font_size=19,color=INK).next_to(p90,DOWN),Text("180°",font=MONO,font_size=19,color=INK).next_to(p180,DOWN),Text("Δλ / λC",font=MONO,font_size=21,color=INK).next_to(ax,LEFT)); self.play(Create(ax),run_time=.7); self.play(Create(curve),FadeIn(pts),FadeIn(labels),run_time=1.1); self.wait(max(.1,d-1.8))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("RECOIL BOOKKEEPING",font=DISPLAY,font_size=24,color=SLATE).move_to(UP*2.3),Text("photon gives energy + momentum",font=SERIF,font_size=35,color=INK).move_to(UP*.8),Text("↓",font=DISPLAY,font_size=35,color=CRIMSON),Text("electron recoils",font=SERIF,font_size=35,color=CRIMSON).move_to(DOWN*.9),Text("photon leaves with longer λ",font=SERIF,font_size=38,color=TEAL).move_to(DOWN*2.1)); self.wait(d)
