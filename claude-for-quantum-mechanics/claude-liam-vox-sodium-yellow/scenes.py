import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
D={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s',10)) for x in json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json')))['beats']}
def base(title): return [Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0),Text(title,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)]
def levels(items,split=False):
 g=VGroup()
 for i,(lab,y,c) in enumerate(items):
  line=Line(LEFT*1.5,RIGHT*1.5,color=c).shift(UP*y); txt=Text(lab,font=MONO,font_size=27,color=c).next_to(line,LEFT,buff=.3); g.add(line,txt)
 return g
class B02_Color(Scene):
 def construct(self):
  self.add(*base('THE COLOR')); bar=Rectangle(width=8,height=.8).set_fill('#E5B80B',1).set_stroke(width=0); lab=Text('sodium D light · near 589 nm',font=MONO,font_size=38,color=INK).next_to(bar,DOWN,buff=.6); self.play(GrowFromCenter(bar),FadeIn(lab)); self.wait(D['B02']-1)
class B03_Hydrogen(Scene):
 def construct(self):
  self.add(*base('IDEAL HYDROGEN: ENERGY DEPENDS ONLY ON n')); eq=Text('E_n = -13.6 eV / n^2',font=MONO,font_size=45,color=CRIMSON); sub=Text('not on ell · in the Coulomb model',font=SERIF,font_size=32,color=INK).next_to(eq,DOWN,buff=.7); self.play(FadeIn(eq,sub)); self.wait(D['B03']-1)
class B04_Degeneracy(Scene):
 def construct(self):
  self.add(*base('HYDROGEN n = 3: DIFFERENT SHAPES, SAME ENERGY')); lines=VGroup(*[Line(LEFT*.9,RIGHT*.9,color=c) for c in [TEAL,CRIMSON,INK]]).arrange(RIGHT,buff=1.3); labs=VGroup(*[Text(s,font=MONO,font_size=28,color=c).next_to(lines[i],UP,buff=.3) for i,(s,c) in enumerate([('3s',TEAL),('3p',CRIMSON),('3d',INK)])]); self.play(Create(lines),FadeIn(labs)); self.wait(D['B04']-1)
class B05_Sodium(Scene):
 def construct(self):
  self.add(*base('SODIUM: A CLOSED CORE + ONE VALENCE ELECTRON')); core=Circle(radius=1.6,color=INK).set_fill('#E8DED2',1); dots=VGroup(*[Dot(1.1*np.array([np.cos(a),np.sin(a),0]),color=TEAL) for a in np.linspace(0,2*np.pi,10,endpoint=False)]); val=Dot(RIGHT*4,color=CRIMSON,radius=.2); self.play(Create(core),FadeIn(dots,val)); self.wait(D['B05']-1)
class B06_Penetration(Scene):
 def construct(self):
  self.add(*base('PENETRATION BREAKS THE TIE')); core=Circle(radius=1.3,color=INK); s=ParametricFunction(lambda t:np.array([3*np.cos(t),1.2*np.sin(t),0]),t_range=[0,2*np.pi],color=CRIMSON); p=ParametricFunction(lambda t:np.array([4*np.cos(t),2.2*np.sin(t),0]),t_range=[0,2*np.pi],color=TEAL); labs=Text('3s samples the core more than 3p',font=MONO,font_size=34,color=INK).move_to(DOWN*3); self.play(Create(core),Create(s),Create(p),FadeIn(labs)); self.wait(D['B06']-1)
class B07_Split(Scene):
 def construct(self):
  self.add(*base('THE DEGENERATE LEVEL FANS APART')); common=Line(LEFT*1.2,RIGHT*1.2,color=INK).shift(LEFT*3); commonlab=Text('3s = 3p',font=MONO,font_size=28,color=INK).next_to(common,UP,buff=.3); b=levels([('3p',1,CRIMSON),('3s',-1,TEAL)]).shift(RIGHT*3); arrow=Arrow(LEFT,RIGHT,color=INK); self.play(Create(common),FadeIn(commonlab),GrowArrow(arrow),Create(b)); self.wait(D['B07']-1)
class B08_Emission(Scene):
 def construct(self):
  self.add(*base('3p FALLS TO 3s')); g=levels([('3p',1.4,CRIMSON),('3s',-1.4,TEAL)]); fall=Arrow(UP*.9,DOWN*.9,color=CRIMSON); photon=VGroup(*[Line(np.array([1.5+i*.35,.25*np.sin(i*np.pi/2),0]),np.array([1.85+i*.35,.25*np.sin((i+1)*np.pi/2),0]),color='#E5B80B') for i in range(9)]); eq=Text('Delta E = h c / lambda',font=MONO,font_size=34,color=INK).move_to(DOWN*3); self.play(Create(g),GrowArrow(fall),Create(photon),FadeIn(eq)); self.wait(D['B08']-1)
class B09_Number(Scene):
 def construct(self):
  self.add(*base('THE CHECKABLE NUMBER')); eq=VGroup(Text('lambda ≈ 589 nm',font=MONO,font_size=45,color=CRIMSON),Text('E ≈ 1240 / 589 = 2.1 eV',font=MONO,font_size=40,color=TEAL)).arrange(DOWN,buff=.8); self.play(FadeIn(eq)); self.wait(D['B09']-1)
class B10_Doublet(Scene):
 def construct(self):
  self.add(*base('REAL SODIUM HAS A CLOSE D-LINE DOUBLET')); g=VGroup(Line(DOWN*1.5,UP*1.5,color='#E5B80B').shift(LEFT*.35),Line(DOWN*1.5,UP*1.5,color='#D9A300').shift(RIGHT*.35)); labs=Text('589.0 nm      589.6 nm',font=MONO,font_size=34,color=INK).next_to(g,DOWN,buff=.6); cave=Text('mostly 3p spin-orbit splitting',font=SERIF,font_size=29,color=CRIMSON).move_to(DOWN*3); self.play(Create(g),FadeIn(labs,cave)); self.wait(D['B10']-1)
class B11_Defects(Scene):
 def construct(self):
  self.add(*base('MORE PRECISELY: ORBITAL-DEPENDENT QUANTUM DEFECTS')); txt=VGroup(Text('not one uniform screened charge',font=MONO,font_size=35,color=CRIMSON),Text('penetration → different core sampling',font=MONO,font_size=32,color=TEAL)).arrange(DOWN,buff=.8); self.play(FadeIn(txt)); self.wait(D['B11']-1)
class B12_YourTurn(Scene):
 def construct(self):
  self.add(*base('YOUR TURN')); q=VGroup(Text('1240 eV·nm / 589 nm = ?',font=MONO,font_size=43,color=INK),Text('≈ 2.1 eV',font=MONO,font_size=46,color=CRIMSON)).arrange(DOWN,buff=1); self.play(FadeIn(q[0])); self.wait(D['B12']*.55); self.play(FadeIn(q[1])); self.wait(D['B12']*.45-1)
class B13_Recap(Scene):
 def construct(self):
  self.add(*base("WHY SODIUM'S STREETLIGHT IS YELLOW")); rows=VGroup(Text('Coulomb hydrogen: same n → same energy',font=MONO,font_size=31,color=TEAL),Text('sodium core: 3s and 3p split',font=MONO,font_size=31,color=CRIMSON),Text('3p → 3s: yellow photon',font=MONO,font_size=34,color='#B68B00')).arrange(DOWN,buff=.75); self.play(FadeIn(rows)); self.wait(D['B13']-1)
