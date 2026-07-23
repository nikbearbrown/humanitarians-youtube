import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 _bs=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in _bs["beats"]}
except Exception: pass
def hold(s,b,u=1): s.wait(max(.1,DUR.get(b,10)-u))
def heading(t): return Text(t,font=DISPLAY,font_size=29,color=INK).to_edge(UP)
def hline(x,y,w,c=INK): return Line(LEFT*w/2,RIGHT*w/2,color=c).move_to(RIGHT*x+UP*y)

class B02_NormalTriplet(Scene):
 def construct(self):
  levels=VGroup(*[hline(0,y,7,c) for y,c in [(-1,TEAL),(0,INK),(1,CRIMSON)]]); labs=VGroup(*[Text(m,font=MONO,font_size=28,color=c).next_to(levels[i],RIGHT) for i,(m,c) in enumerate([("m_l = −1",TEAL),("m_l = 0",INK),("m_l = +1",CRIMSON)])]); gap=DoubleArrow(DOWN*.9,UP*.9,color=CRIMSON).shift(LEFT*3); note=Text("equal orbital spacing: μ_B B",font=MONO,font_size=31,color=INK).shift(DOWN*2.55)
  self.play(FadeIn(heading("THE ORBITAL-ONLY CARTOON: A REGULAR TRIPLET")),FadeIn(levels),FadeIn(labs),GrowArrow(gap),FadeIn(note),run_time=1.1); hold(self,"B02",1.1)

class B03_AddSpin(Scene):
 def construct(self):
  l=Arrow(ORIGIN,UP*2+LEFT*.8,color=TEAL); s=Arrow(ORIGIN,UP*1.5+RIGHT*1.5,color=CRIMSON); j=Arrow(ORIGIN,l.get_end()+s.get_end(),color=INK); labs=VGroup(Text("L  g=1",font=MONO,font_size=28,color=TEAL).next_to(l,LEFT),Text("S  g≈2",font=MONO,font_size=28,color=CRIMSON).next_to(s,RIGHT),Text("J=L+S",font=MONO,font_size=32,color=INK).next_to(j,RIGHT)); note=Text("magnetic moments do not weight L and S equally",font=SERIF,font_size=28,color=INK).shift(DOWN*2.55)
  self.play(FadeIn(heading("THE MISSING MAGNETIC MOMENT IS SPIN")),GrowArrow(l),GrowArrow(s),GrowArrow(j),FadeIn(labs),FadeIn(note),run_time=1.2); hold(self,"B03",1.2)

class B04_WeakFieldFormula(Scene):
 def construct(self):
  g=VGroup(Text("weak field",font=DISPLAY,font_size=35,color=TEAL),Text("μ_B B  ≪  ΔE_fine",font=MONO,font_size=36,color=CRIMSON),Text("ΔE = g_J μ_B B m_J",font=MONO,font_size=45,color=INK),Text("good labels: n, l, j, m_J",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.5)
  self.play(FadeIn(heading("L AND S STAY COUPLED")),FadeIn(g),run_time=1); hold(self,"B04")

class B05_LandeRouter(Scene):
 def construct(self):
  ins=VGroup(*[Text(x,font=MONO,font_size=38,color=c) for x,c in [("l",TEAL),("s",CRIMSON),("j",INK)]]).arrange(DOWN,buff=.45).move_to(LEFT*4); box=RoundedRectangle(width=2.6,height=2.2,corner_radius=.2,color=CRIMSON); label=Text("Landé\ng_J",font=DISPLAY,font_size=31,color=INK,line_spacing=1.1).move_to(box); out=VGroup(Text("level slope",font=SERIF,font_size=27,color=INK),Text("g_J μ_B m_J",font=MONO,font_size=29,color=TEAL)).arrange(DOWN,buff=.35).move_to(RIGHT*4); a=Arrow(LEFT*2.9,LEFT*1.45,color=INK,buff=0); b=Arrow(RIGHT*1.45,RIGHT*2.85,color=INK,buff=0)
  self.play(FadeIn(heading("ONE FACTOR PACKS THE ANGULAR-MOMENTUM GEOMETRY")),FadeIn(ins),GrowArrow(a),FadeIn(box),FadeIn(label),GrowArrow(b),FadeIn(out),run_time=1.2); hold(self,"B05",1.2)

class B06_TwoFans(Scene):
 def construct(self):
  fan1=VGroup(*[hline(-3,y,3.4,TEAL) for y in [-1.5,-.5,.5,1.5]]); fan2=VGroup(*[hline(3,y,3.4,CRIMSON) for y in [-.5,.5]]); labs=VGroup(Text("2P₃/₂   g=4/3",font=MONO,font_size=29,color=TEAL).move_to(LEFT*3+DOWN*2.25),Text("2P₁/₂   g=2/3",font=MONO,font_size=29,color=CRIMSON).move_to(RIGHT*3+DOWN*2.25)); note=Text("regular fans • different rulers",font=SERIF,font_size=29,color=INK).shift(DOWN*2.8)
  self.play(FadeIn(heading("TWO J MANIFOLDS FAN AT DIFFERENT SLOPES")),FadeIn(fan1),FadeIn(fan2),FadeIn(labs),FadeIn(note),run_time=1); hold(self,"B06")

class B07_SpacingCorrection(Scene):
 def construct(self):
  left=VGroup(Text("2P₃/₂ adjacent",font=SERIF,font_size=29,color=TEAL),Text("(4/3) μ_B B",font=MONO,font_size=40,color=TEAL)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("2P₁/₂ total doublet",font=SERIF,font_size=29,color=CRIMSON),Text("(2/3) μ_B B",font=MONO,font_size=40,color=CRIMSON)).arrange(DOWN,buff=.5).move_to(RIGHT*3); ratio=Text("ratio = 2",font=MONO,font_size=38,color=INK).shift(DOWN*2.45)
  self.play(FadeIn(heading("ADJACENT SPACING IS NOT THE SAME QUANTITY")),FadeIn(left),FadeIn(right),FadeIn(ratio),run_time=1); hold(self,"B07")

class B08_TransitionComb(Scene):
 def construct(self):
  upper=VGroup(*[hline(0,y,6,TEAL) for y in [1.1,1.8,2.5]]); lower=VGroup(*[hline(0,y,6,CRIMSON) for y in [-2,-1.4,-.8]]); arrows=VGroup(Arrow(LEFT*2.2+UP*.9,LEFT*1.5+DOWN*.65,color=INK),Arrow(ORIGIN+UP*1.6,ORIGIN+DOWN*.65,color=CRIMSON),Arrow(RIGHT*2.2+UP*2.3,RIGHT*1.2+DOWN*1.25,color=INK)); note=Text("Δm_J = 0, ±1 • different g values → uneven frequency shifts",font=SERIF,font_size=27,color=INK).shift(DOWN*2.75)
  self.play(FadeIn(heading("SPECTRA SAMPLE DIFFERENCES BETWEEN TWO FANS")),FadeIn(upper),FadeIn(lower),LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.1),FadeIn(note),run_time=1.2); hold(self,"B08",1.2)

class B09_PositionsIntensity(Scene):
 def construct(self):
  left=VGroup(Text("LINE POSITIONS",font=DISPLAY,font_size=31,color=TEAL),Text("energies + g_J + B",font=MONO,font_size=29,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("LINE INTENSITIES",font=DISPLAY,font_size=31,color=CRIMSON),Text("matrix elements\npopulations\npolarization + geometry",font=SERIF,font_size=25,color=INK,line_spacing=1.15)).arrange(DOWN,buff=.45).move_to(RIGHT*3); neq=Text("≠",font=DISPLAY,font_size=58,color=CRIMSON)
  self.play(FadeIn(heading("THE g FACTOR DOES NOT PREDICT BRIGHTNESS ALONE")),FadeIn(left),FadeIn(right),FadeIn(neq),run_time=1); hold(self,"B09")

class B10_FieldCrossover(Scene):
 def construct(self):
  ax=Axes(x_range=[0,10,2],y_range=[-3,3,1],x_length=9,y_length=4.5,axis_config={"color":INK},tips=False).shift(DOWN*.3); curves=VGroup(*[ax.plot(lambda x,a=a,b=b:a*x+b*np.tanh((x-5)/2),x_range=[0,10],color=TEAL if i%2==0 else CRIMSON) for i,(a,b) in enumerate([(.15,.5),(-.12,.7),(.28,-.8),(-.25,-.6)])]); labs=Text("weak field      intermediate diagonalization      strong field",font=SERIF,font_size=25,color=INK).shift(DOWN*2.65)
  self.play(FadeIn(heading("FIELD STRENGTH CHANGES THE GOOD BASIS")),FadeIn(ax),LaggedStart(*[Create(c) for c in curves],lag_ratio=.08),FadeIn(labs),run_time=1.3); hold(self,"B10",1.3)

class B11_PaschenBack(Scene):
 def construct(self):
  coupled=VGroup(Text("weak",font=DISPLAY,font_size=31,color=TEAL),Text("|j,m_J〉",font=MONO,font_size=37,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); unc=VGroup(Text("strong",font=DISPLAY,font_size=31,color=CRIMSON),Text("|m_l,m_s〉",font=MONO,font_size=37,color=INK),Text("ΔE≈μ_BB(m_l+2m_s)",font=MONO,font_size=25,color=CRIMSON)).arrange(DOWN,buff=.45).move_to(RIGHT*3); arrow=Arrow(LEFT*.8,RIGHT*.8,color=CRIMSON)
  self.play(FadeIn(heading("PASCHEN–BACK: L AND S UNCOUPLE")),FadeIn(coupled),GrowArrow(arrow),FadeIn(unc),run_time=1); hold(self,"B11")

class B12_YourTurn(Scene):
 def construct(self):
  g=VGroup(Text("YOUR TURN — B = 1 T",font=DISPLAY,font_size=34,color=INK),Text("μ_B B = 5.788 × 10⁻⁵ eV",font=MONO,font_size=34,color=TEAL),Text("spacing = g_J μ_B B",font=MONO,font_size=37,color=CRIMSON),Text("g_J = 4/3  vs.  2/3",font=MONO,font_size=34,color=INK)).arrange(DOWN,buff=.55); self.play(FadeIn(g),run_time=1); hold(self,"B12")

class B13_Answer(Scene):
 def construct(self):
  g=VGroup(Text("ANSWER",font=DISPLAY,font_size=35,color=INK),Text("(4/3):  7.72 × 10⁻⁵ eV",font=MONO,font_size=35,color=TEAL),Text("(2/3):  3.86 × 10⁻⁵ eV",font=MONO,font_size=35,color=CRIMSON),Text("ratio = 2",font=MONO,font_size=44,color=INK)).arrange(DOWN,buff=.52); self.play(FadeIn(g),run_time=1); hold(self,"B13")

class B14_Verdict(Scene):
 def construct(self):
  g=VGroup(Text("REGULAR WITHIN EACH J",font=DISPLAY,font_size=34,color=TEAL),Text("+",font=DISPLAY,font_size=40,color=CRIMSON),Text("DIFFERENT g FACTORS BETWEEN J LEVELS",font=DISPLAY,font_size=31,color=INK),Text("= accountable multiplet",font=SERIF,font_size=33,color=CRIMSON)).arrange(DOWN,buff=.5); self.play(FadeIn(g),run_time=1); hold(self,"B14")

class B15_CorrectTitleOutro(Scene):
 def construct(self):
  self.camera.background_color="#201F1C"; title=Text("The Anomalous Zeeman Effect Isn't Anomalous",font=DISPLAY,font_size=32,color="#F2EFE8"); credit=Text("Liam, in for Bear",font=SERIF,font_size=20,color="#D97757").next_to(title,DOWN,buff=.45); self.play(FadeIn(title),FadeIn(credit),run_time=1); hold(self,"B15")
