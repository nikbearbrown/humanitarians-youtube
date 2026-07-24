import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
    _bs=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in _bs["beats"]}
except Exception: pass
def hold(scene,beat,used=1): scene.wait(max(.1,DUR.get(beat,10)-used))
def heading(text): return Text(text,font=DISPLAY,font_size=29,color=INK).to_edge(UP)
def hydrogens():
    return VGroup(*[Dot(np.array([1.35*np.cos(a),.55*np.sin(a),0]),radius=.18,color=INK) for a in [0,2*np.pi/3,4*np.pi/3]])

class B02_TwoGeometries(Scene):
    def construct(self):
        h1=hydrogens().move_to(LEFT*3); h2=hydrogens().move_to(RIGHT*3); n1=Dot(LEFT*3+UP*1.3,radius=.24,color=TEAL); n2=Dot(RIGHT*3+DOWN*1.3,radius=.24,color=CRIMSON)
        plane=VGroup(Line(LEFT*4.7,LEFT*1.3,color=SLATE),Line(RIGHT*1.3,RIGHT*4.7,color=SLATE)); labs=VGroup(Text("|L〉",font=MONO,font_size=34,color=TEAL).move_to(LEFT*3+DOWN*2.2),Text("|R〉",font=MONO,font_size=34,color=CRIMSON).move_to(RIGHT*3+DOWN*2.2),Text("same classical energy",font=SERIF,font_size=28,color=INK).shift(DOWN*2.8))
        self.play(FadeIn(heading("NITROGEN ABOVE OR BELOW THE HYDROGEN PLANE")),FadeIn(h1),FadeIn(h2),FadeIn(n1),FadeIn(n2),FadeIn(plane),FadeIn(labs),run_time=1.2); hold(self,"B02",1.2)

class B03_DoubleWell(Scene):
    def construct(self):
        ax=Axes(x_range=[-3,3,1],y_range=[0,5,1],x_length=9,y_length=4.5,axis_config={"color":INK},tips=False).shift(DOWN*.35); curve=ax.plot(lambda x:.12*(x*x-4)**2+.45,x_range=[-3,3],color=TEAL,stroke_width=4); barrier=DashedLine(ax.c2p(0,.4),ax.c2p(0,2.4),color=CRIMSON); labs=VGroup(Text("L",font=MONO,font_size=30,color=TEAL).move_to(ax.c2p(-2,.2)),Text("R",font=MONO,font_size=30,color=CRIMSON).move_to(ax.c2p(2,.2)),Text("planar barrier",font=SERIF,font_size=25,color=CRIMSON).move_to(ax.c2p(.9,2.65)))
        self.play(FadeIn(heading("THE INVERSION COORDINATE IS A DOUBLE WELL")),FadeIn(ax),Create(curve),Create(barrier),FadeIn(labs),run_time=1.2); hold(self,"B03",1.2)

class B04_TunnelOverlap(Scene):
    def construct(self):
        ax=Axes(x_range=[-4,4,2],y_range=[0,1.2,.4],x_length=10,y_length=4,axis_config={"color":INK},tips=False).shift(DOWN*.35); l=ax.plot(lambda x:np.exp(-.65*(x+1.8)**2),x_range=[-4,4],color=TEAL); r=ax.plot(lambda x:np.exp(-.65*(x-1.8)**2),x_range=[-4,4],color=CRIMSON); overlap=Text("overlap → tunneling coupling A",font=SERIF,font_size=30,color=INK).shift(UP*2.0)
        self.play(FadeIn(heading("THE WAVEFUNCTIONS LEAK THROUGH THE BARRIER")),FadeIn(ax),Create(l),Create(r),FadeIn(overlap),run_time=1.2); hold(self,"B04",1.2)

class B05_TrueEigenstates(Scene):
    def construct(self):
        plus=VGroup(Text("symmetric",font=DISPLAY,font_size=31,color=TEAL),Text("|+〉 = (|L〉 + |R〉)/√2",font=MONO,font_size=31,color=INK)).arrange(DOWN,buff=.35).shift(UP*.8); minus=VGroup(Text("antisymmetric",font=DISPLAY,font_size=31,color=CRIMSON),Text("|−〉 = (|L〉 − |R〉)/√2",font=MONO,font_size=31,color=INK)).arrange(DOWN,buff=.35).shift(DOWN*1.1)
        self.play(FadeIn(heading("LOCALIZED SHAPES ARE NOT THE ENERGY EIGENSTATES")),FadeIn(plus),FadeIn(minus),run_time=1); hold(self,"B05")

class B06_EnergySplit(Scene):
    def construct(self):
        base=Line(LEFT*3,RIGHT*3,color=SLATE); up=Line(LEFT*3,RIGHT*3,color=CRIMSON).shift(UP*1.1); down=Line(LEFT*3,RIGHT*3,color=TEAL).shift(DOWN*1.1); labs=VGroup(Text("E0 + A",font=MONO,font_size=31,color=CRIMSON).next_to(up,RIGHT),Text("E0 − A",font=MONO,font_size=31,color=TEAL).next_to(down,RIGHT),Text("ΔE = 2A",font=MONO,font_size=39,color=INK).shift(DOWN*2.65))
        self.play(FadeIn(heading("TUNNEL COUPLING SPLITS THE DEGENERACY")),Create(base),run_time=.5); self.play(TransformFromCopy(base,up),TransformFromCopy(base,down),FadeIn(labs),run_time=.8); hold(self,"B06",1.3)

class B07_ProbabilityOscillation(Scene):
    def construct(self):
        ax=Axes(x_range=[0,2*np.pi,np.pi/2],y_range=[0,1.1,.5],x_length=9,y_length=4,axis_config={"color":INK},tips=False).shift(DOWN*.3); pl=ax.plot(lambda x:np.cos(x/2)**2,x_range=[0,2*np.pi],color=TEAL); pr=ax.plot(lambda x:np.sin(x/2)**2,x_range=[0,2*np.pi],color=CRIMSON); labs=VGroup(Text("P(L)",font=MONO,font_size=26,color=TEAL).move_to(ax.c2p(5.7,.9)),Text("P(R)",font=MONO,font_size=26,color=CRIMSON).move_to(ax.c2p(5.7,.12)),Text("localized superposition",font=SERIF,font_size=27,color=INK).shift(DOWN*2.55))
        self.play(FadeIn(heading("WHAT OSCILLATES IS LOCALIZATION PROBABILITY")),FadeIn(ax),Create(pl),Create(pr),FadeIn(labs),run_time=1.2); hold(self,"B07",1.2)

class B08_InversionLine(Scene):
    def construct(self):
        g=VGroup(Text("ν = 23.87 GHz",font=MONO,font_size=48,color=TEAL),Text("ΔE = hν",font=MONO,font_size=42,color=INK),Text("≈ 9.87 × 10⁻⁵ eV",font=MONO,font_size=43,color=CRIMSON),Text("microwave inversion line",font=SERIF,font_size=28,color=INK)).arrange(DOWN,buff=.5)
        self.play(FadeIn(heading("A TINY SPLITTING, A PRECISE SPECTRAL LINE")),LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.12),run_time=1.2); hold(self,"B08",1.2)

class B09_NotClassicalHopping(Scene):
    def construct(self):
        left=VGroup(Text("energy eigenstate",font=DISPLAY,font_size=31,color=TEAL),Text("stationary density",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3); right=VGroup(Text("localized superposition",font=DISPLAY,font_size=29,color=CRIMSON),Text("P(L) ↔ P(R)",font=MONO,font_size=34,color=INK)).arrange(DOWN,buff=.5).move_to(RIGHT*3); neq=Text("≠ classical bead",font=SERIF,font_size=32,color=CRIMSON).shift(DOWN*2.4)
        self.play(FadeIn(heading("THE 24-GIGAHERTZ CARTOON NEEDS A QUALIFIER")),FadeIn(left),FadeIn(right),FadeIn(neq),run_time=1); hold(self,"B09")

class B10_MaserSorting(Scene):
    def construct(self):
        source=VGroup(*[Dot(LEFT*5+UP*(i*.35-1),radius=.09,color=TEAL if i%2==0 else CRIMSON) for i in range(7)]); field=VGroup(Line(LEFT*2.3+UP*2,LEFT*1.5+DOWN*2,color=INK),Line(LEFT*1.5+UP*2,LEFT*2.3+DOWN*2,color=INK)); selected=VGroup(*[Arrow(LEFT*1.3+UP*(i*.3-.6),RIGHT*4+UP*(i*.15-.3),color=CRIMSON,buff=0) for i in range(5)]); lab=Text("upper inversion state focused toward cavity",font=SERIF,font_size=28,color=INK).shift(DOWN*2.6)
        self.play(FadeIn(heading("THE MOLECULAR BEAM CREATES POPULATION INVERSION")),FadeIn(source),FadeIn(field),LaggedStart(*[GrowArrow(a) for a in selected],lag_ratio=.08),FadeIn(lab),run_time=1.3); hold(self,"B10",1.3)

class B11_StimulatedEmission(Scene):
    def construct(self):
        cavity=RoundedRectangle(width=8,height=3.5,corner_radius=.3,color=INK); upper=Line(LEFT*1.5,RIGHT*1.5,color=CRIMSON).shift(UP*.8); lower=Line(LEFT*1.5,RIGHT*1.5,color=TEAL).shift(DOWN*.8); drop=Arrow(UP*.65,DOWN*.65,color=CRIMSON); waves=VGroup(*[Arc(radius=.3+i*.17,start_angle=-.7,angle=1.4,color=TEAL).shift(RIGHT*(1.9+i*.3)) for i in range(4)]); lab=Text("one coherent cavity mode gains photons",font=SERIF,font_size=28,color=INK).shift(DOWN*2.6)
        self.play(FadeIn(heading("STIMULATED EMISSION AMPLIFIES MICROWAVES")),Create(cavity),Create(upper),Create(lower),GrowArrow(drop),LaggedStart(*[Create(w) for w in waves],lag_ratio=.1),FadeIn(lab),run_time=1.3); hold(self,"B11",1.3)

class B12_ModelLimits(Scene):
    def construct(self):
        items=["barrier height and width","inversion reduced mass","multidimensional molecular motion","rotational-state structure","field and cavity selection"]
        rows=VGroup(*[Text("• "+x,font=SERIF,font_size=28,color=TEAL if i%2==0 else CRIMSON) for i,x in enumerate(items)]).arrange(DOWN,aligned_edge=LEFT,buff=.42)
        self.play(FadeIn(heading("THE SPLITTING IS EXPONENTIALLY SENSITIVE")),LaggedStart(*[FadeIn(r) for r in rows],lag_ratio=.08),run_time=1.2); hold(self,"B12",1.2)

class B13_YourTurn(Scene):
    def construct(self):
        g=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=35,color=INK),Text("h = 4.136 × 10⁻¹⁵ eV·s",font=MONO,font_size=34,color=TEAL),Text("ν = 23.87 × 10⁹ s⁻¹",font=MONO,font_size=34,color=CRIMSON),Text("ΔE = hν = ?",font=MONO,font_size=39,color=INK),Text("Name the two eigenstates.",font=SERIF,font_size=28,color=INK)).arrange(DOWN,buff=.4)
        self.play(FadeIn(g),run_time=1); hold(self,"B13")

class B14_Answer(Scene):
    def construct(self):
        g=VGroup(Text("ANSWER",font=DISPLAY,font_size=35,color=INK),Text("ΔE ≈ 9.87 × 10⁻⁵ eV",font=MONO,font_size=43,color=TEAL),Text("symmetric:  |L〉 + |R〉",font=MONO,font_size=31,color=INK),Text("antisymmetric:  |L〉 − |R〉",font=MONO,font_size=31,color=CRIMSON)).arrange(DOWN,buff=.55)
        self.play(FadeIn(g),run_time=1); hold(self,"B14")

class B15_CorrectTitleOutro(Scene):
    def construct(self):
        self.camera.background_color="#201F1C"; title=Text("Ammonia Inversion: The Molecule That Tunnels Through Itself",font=DISPLAY,font_size=29,color="#F2EFE8"); credit=Text("Kore, in for Humanitarians AI",font=SERIF,font_size=20,color="#D97757").next_to(title,DOWN,buff=.45)
        self.play(FadeIn(title),FadeIn(credit),run_time=1); hold(self,"B15")
