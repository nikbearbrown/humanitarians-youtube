import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
class B02_Radio(Scene):
 def construct(self):
  d=DUR.get('B02',15); self.add(bg(),ttl('THE HYDROGEN REST LINE')); rows=VGroup(Text('f0 = 1420.4058 MHz',font=MONO,font_size=39,color=CRIMSON),Text('lambda = 21.106 cm',font=MONO,font_size=39,color=TEAL),Text('Doppler shift -> gas velocity',font=MONO,font_size=32,color=INK),Text('emission or absorption',font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.6); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B03_Multiplet(Scene):
 def construct(self):
  d=DUR.get('B03',15); self.add(bg(),ttl('TWO SPIN-HALVES MAKE 3 + 1 STATES')); top=VGroup(*[RoundedRectangle(width=2,height=1.2,corner_radius=.15,color=TEAL).set_fill(TEAL,.1) for _ in range(3)]).arrange(RIGHT,buff=.7).shift(UP*.8); bot=RoundedRectangle(width=2,height=1.2,corner_radius=.15,color=CRIMSON).set_fill(CRIMSON,.1).shift(DOWN*1.4); labs=VGroup(Text('F = 1 triplet',font=MONO,font_size=31,color=TEAL).move_to(UP*2.3),Text('F = 0 singlet',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*2.5)); self.play(Create(top),Create(bot),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B04_Sign(Scene):
 def construct(self):
  d=DUR.get('B04',15); self.add(bg(),ttl('ONE RELATIVE SIGN · DIFFERENT TOTAL SPIN')); eqs=VGroup(Text('(|up down> + |down up>) / sqrt(2)',font=MONO,font_size=34,color=TEAL),Text('versus',font=SERIF,font_size=30,color=INK),Text('(|up down> - |down up>) / sqrt(2)',font=MONO,font_size=34,color=CRIMSON)).arrange(DOWN,buff=.7); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B05_Relative(Scene):
 def construct(self):
  d=DUR.get('B05',13); self.add(bg(),ttl('GLOBAL PHASE IS NOT RELATIVE PHASE')); left=VGroup(Text('- (a|1> + b|2>)',font=MONO,font_size=32,color=SLATE),Text('same physical ray',font=SERIF,font_size=28,color=SLATE)).arrange(DOWN,buff=.5).shift(LEFT*3); right=VGroup(Text('a|1> - b|2>',font=MONO,font_size=34,color=CRIMSON),Text('different interference',font=SERIF,font_size=28,color=CRIMSON)).arrange(DOWN,buff=.5).shift(RIGHT*3); self.play(FadeIn(left,right),run_time=1); self.wait(max(.1,d-1))
class B06_Symmetry(Scene):
 def construct(self):
  d=DUR.get('B06',15); self.add(bg(),ttl('THE SIGN SELECTS EXCHANGE SYMMETRY')); plus=VGroup(Text('+',font=DISPLAY,font_size=70,color=TEAL),Text('symmetric',font=MONO,font_size=30,color=TEAL),Text('F = 1, m = 0',font=MONO,font_size=29,color=TEAL)).arrange(DOWN).shift(LEFT*3); minus=VGroup(Text('-',font=DISPLAY,font_size=70,color=CRIMSON),Text('antisymmetric',font=MONO,font_size=30,color=CRIMSON),Text('F = 0',font=MONO,font_size=29,color=CRIMSON)).arrange(DOWN).shift(RIGHT*3); self.play(FadeIn(plus,minus),run_time=1); self.wait(max(.1,d-1))
class B07_F2(Scene):
 def construct(self):
  d=DUR.get('B07',16); self.add(bg(),ttl('TOTAL-SPIN EIGENVALUES')); eqs=VGroup(Text('F^2 |F,m> = F(F+1) hbar^2 |F,m>',font=MONO,font_size=32,color=INK),Text('F = 1  ->  2 hbar^2',font=MONO,font_size=37,color=TEAL),Text('F = 0  ->  0',font=MONO,font_size=37,color=CRIMSON)).arrange(DOWN,buff=.7); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B08_Hyperfine(Scene):
 def construct(self):
  d=DUR.get('B08',16); self.add(bg(),ttl('HYPERFINE COUPLING TURNS SYMMETRY INTO ENERGY')); eq=Text('Se dot Ip = (F^2 - Se^2 - Ip^2) / 2',font=MONO,font_size=33,color=INK).move_to(UP*1.7); levels=VGroup(Line(LEFT*3,RIGHT*3,color=TEAL).shift(UP*.3),Line(LEFT*3,RIGHT*3,color=CRIMSON).shift(DOWN*1.5)); labs=VGroup(Text('triplet: + hbar^2/4',font=MONO,font_size=29,color=TEAL).move_to(UP*.7),Text('singlet: - 3 hbar^2/4',font=MONO,font_size=29,color=CRIMSON).move_to(DOWN*2)); self.play(FadeIn(eq),Create(levels),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B09_Chain(Scene):
 def construct(self):
  d=DUR.get('B09',15); self.add(bg(),ttl('ONE GAP · THREE EQUIVALENT SCALES')); chain=VGroup(Text('Delta E = 5.874 micro-eV',font=MONO,font_size=35,color=CRIMSON),Text('f = Delta E / h = 1420.4 MHz',font=MONO,font_size=33,color=INK),Text('lambda = c / f = 21.1 cm',font=MONO,font_size=35,color=TEAL)).arrange(DOWN,buff=.75); self.play(FadeIn(chain),run_time=1); self.wait(max(.1,d-1))
class B10_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B10',19); self.add(bg(),ttl('YOUR TURN: A 100 kHz REDSHIFT')); eqs=VGroup(Text('Delta f / f0 approx -v/c',font=MONO,font_size=36,color=INK),Text('v approx 21 km/s away',font=MONO,font_size=40,color=CRIMSON),Text('frequency shift -> line-of-sight velocity',font=SERIF,font_size=30,color=TEAL)).arrange(DOWN,buff=.75); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B11_Recap(Scene):
 def construct(self):
  d=DUR.get('B11',16); self.add(bg(),Text('WHY ONE MINUS SIGN LIGHTS UP THE GALAXY',font=DISPLAY,font_size=34,color=CRIMSON).move_to(UP*2.3),Text('relative sign -> total-spin symmetry',font=MONO,font_size=32,color=TEAL).move_to(UP*.8),Text('hyperfine coupling -> energy gap',font=MONO,font_size=32,color=INK).move_to(DOWN*.4),Text('gap -> 21 cm emission or absorption',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
