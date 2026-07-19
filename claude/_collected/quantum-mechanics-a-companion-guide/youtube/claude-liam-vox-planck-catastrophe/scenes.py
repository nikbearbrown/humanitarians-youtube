import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
import numpy as np

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0) for b in _BS["beats"]})
except Exception:
    pass

def base():
    return Rectangle(width=16, height=9).set_fill(GROUND, 1).set_stroke(width=0, opacity=0)

def curve(origin, xs, ys, color, width=4):
    pts = [origin + RIGHT*x + UP*y for x, y in zip(xs, ys)]
    m = VMobject(color=color, stroke_width=width)
    m.set_points_smoothly(pts)
    return m

class B02_ClassicalModes(Scene):
    def construct(self):
        duration = DUR.get("B02", 18)
        self.add(base())
        title = Text("CLASSICAL CAVITY: EVERY MODE GETS kT", font=DISPLAY, font_size=29, color=INK).move_to(UP*3.35)
        box = Rectangle(width=11.5, height=4.1).set_fill(SLATE,.05).set_stroke(INK,2)
        modes = VGroup()
        for i,n in enumerate((1,2,3,4,5,6)):
            y = 1.55-i*.58
            wave = ParametricFunction(lambda t,n=n,y=y: np.array([t, y+.18*np.sin(n*np.pi*(t+5.2)/10.4), 0]),
                                      t_range=[-5.2,5.2,.04], color=TEAL, stroke_width=2)
            modes.add(wave)
        labels = VGroup(*[Text("kT",font=MONO,font_size=18,color=CRIMSON).move_to(RIGHT*6.2+UP*(1.55-i*.58)) for i in range(6)])
        formula = Text("u(ν) ∝ ν² kT   →   ∫₀∞ u(ν)dν = ∞", font=MONO, font_size=29, color=INK).move_to(DOWN*3.15)
        self.play(FadeIn(title), Create(box), run_time=.7)
        self.play(LaggedStart(*[Create(m) for m in modes],lag_ratio=.12), LaggedStart(*[FadeIn(x) for x in labels],lag_ratio=.12), run_time=2.5)
        self.play(Write(formula), run_time=1)
        self.play(Indicate(labels,color=CRIMSON), run_time=1)
        self.wait(max(.1,duration-5.2))

class B03_FiniteSpectrum(Scene):
    def construct(self):
        duration=DUR.get("B03",14)
        self.add(base())
        title=Text("THE REAL OVEN HAS A FINITE PEAK",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.3)
        o=LEFT*5+DOWN*2.5
        axes=VGroup(Line(o,o+RIGHT*10,color=INK),Line(o,o+UP*5,color=INK))
        xs=np.linspace(0,9.4,120); ys=4.2*(xs/2.4)**3*np.exp(-xs/2.4)
        ys=ys/max(ys)*4.0
        c=curve(o,xs,ys,TEAL)
        peak=Dot(o+RIGHT*7.2+UP*4,color=CRIMSON)
        q=Text("Classical: infinity.   Experiment: finite.   Why?",font=SERIF,font_size=28,color=INK).move_to(DOWN*3.25)
        self.play(FadeIn(title),Create(axes),run_time=.7); self.play(Create(c),run_time=2)
        self.play(GrowFromCenter(peak),FadeIn(q),run_time=.7); self.wait(max(.1,duration-3.4))

class B04_PlanckPackets(Scene):
    def construct(self):
        duration=DUR.get("B04",15)
        self.add(base())
        title=Text("PLANCK, 1900: ENERGY ARRIVES IN PACKETS",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.35)
        levels=VGroup(*[Line(LEFT*4,LEFT*.8,color=INK).shift(UP*(-2+i*1.05)) for i in range(5)])
        labs=VGroup(*[Text(f"{i}hν",font=MONO,font_size=21,color=TEAL).next_to(levels[i],LEFT,buff=.25) for i in range(5)])
        packets=VGroup(*[RoundedRectangle(width=.65,height=.65,corner_radius=.08).set_fill(CRIMSON,.65).set_stroke(CRIMSON,1).move_to(RIGHT*(.6+i*.85)+DOWN*.2) for i in range(6)])
        eq=Text("E = n hν     n = 0, 1, 2, …",font=MONO,font_size=34,color=INK).move_to(RIGHT*3+UP*1.8)
        sub=Text("continuous exchange → discrete rungs",font=SERIF,font_size=25,color=INK).move_to(RIGHT*3+DOWN*1.7)
        self.play(FadeIn(title),LaggedStart(*[Create(x) for x in levels],lag_ratio=.12),run_time=1.5)
        self.play(FadeIn(labs),LaggedStart(*[GrowFromCenter(p) for p in packets],lag_ratio=.1),run_time=1.5)
        self.play(Write(eq),FadeIn(sub),run_time=1); self.wait(max(.1,duration-4.2))

class B05_Mechanism(Scene):
    def construct(self):
        duration=DUR.get("B05",3)
        bg=base(); headline=Text("DISCRETE ENERGY PACKETS:  hν",font=DISPLAY,font_size=38,color=INK)
        box=RoundedRectangle(width=11,height=1.5,corner_radius=.12).set_fill(TEAL,.08).set_stroke(TEAL,2)
        self.add(bg,headline,box); self.wait(duration)

class B06_AffordPackets(Scene):
    def construct(self):
        duration=DUR.get("B06",16)
        self.add(base())
        title=Text("CAN THERMAL ENERGY AFFORD ONE PACKET?",font=DISPLAY,font_size=29,color=INK).move_to(UP*3.3)
        divider=Line(UP*2.7,DOWN*2.7,color=INK,stroke_opacity=.3)
        low=Text("LOW ν",font=DISPLAY,font_size=29,color=TEAL).move_to(LEFT*3.8+UP*2.3)
        high=Text("HIGH ν",font=DISPLAY,font_size=29,color=CRIMSON).move_to(RIGHT*3.8+UP*2.3)
        leq=Text("hν ≪ kT",font=MONO,font_size=35,color=TEAL).move_to(LEFT*3.8+UP*.9)
        heq=Text("hν ≫ kT",font=MONO,font_size=35,color=CRIMSON).move_to(RIGHT*3.8+UP*.9)
        cheap=VGroup(*[Square(.5).set_fill(TEAL,.55).set_stroke(TEAL,1).move_to(LEFT*5.3+RIGHT*(i%4)*1+DOWN*(i//4)*.8) for i in range(8)])
        empty=Rectangle(width=5.6,height=2).set_fill(SLATE,.04).set_stroke(CRIMSON,2).move_to(RIGHT*3.8+DOWN*1.2)
        no=Text("mode stays empty",font=SERIF,font_size=26,color=CRIMSON).move_to(RIGHT*3.8+DOWN*1.2)
        self.play(FadeIn(title),Create(divider),run_time=.7); self.play(FadeIn(low),FadeIn(high),Write(leq),Write(heq),run_time=1)
        self.play(LaggedStart(*[GrowFromCenter(x) for x in cheap],lag_ratio=.08),Create(empty),FadeIn(no),run_time=1.6)
        self.wait(max(.1,duration-3.5))

class B07_CurveComparison(Scene):
    def construct(self):
        duration=DUR.get("B07",13)
        self.add(base())
        title=Text("RAYLEIGH–JEANS vs PLANCK",font=DISPLAY,font_size=31,color=INK).move_to(UP*3.3)
        o=LEFT*5.5+DOWN*2.5; axes=VGroup(Line(o,o+RIGHT*11,color=INK),Line(o,o+UP*5.2,color=INK))
        xs=np.linspace(.1,10,150)
        classical=curve(o,xs,.045*xs**2,CRIMSON)
        py=(xs**3)/(np.exp(xs/2)-1); py=py/max(py)*4.2
        planck=curve(o,xs,py,TEAL)
        l1=Text("classical → ∞",font=MONO,font_size=22,color=CRIMSON).move_to(RIGHT*3.7+UP*2.7)
        l2=Text("Planck → 0",font=MONO,font_size=22,color=TEAL).move_to(RIGHT*3.7+UP*1.9)
        self.play(FadeIn(title),Create(axes),run_time=.7); self.play(Create(classical),run_time=1.5); self.play(Create(planck),run_time=1.5)
        self.play(FadeIn(l1),FadeIn(l2),run_time=.5); self.wait(max(.1,duration-4.2))

class B08_Implication(Scene):
    def construct(self):
        duration=DUR.get("B08",3)
        self.add(base(),Text("CLASSICAL IS UNCAPPED.  QUANTUM IS NOT.",font=DISPLAY,font_size=35,color=INK))
        self.wait(duration)

class B09_ExampleCard(Scene):
    def construct(self):
        duration=DUR.get("B09",2)
        self.add(base(),Text("300 K: MICROWAVE vs ULTRAVIOLET",font=DISPLAY,font_size=37,color=INK))
        self.wait(duration)

class B10_RoomTemperature(Scene):
    def construct(self):
        duration=DUR.get("B10",38)
        self.add(base())
        title=Text("ROOM TEMPERATURE: kT ≈ 0.025 eV",font=DISPLAY,font_size=30,color=INK).move_to(UP*3.35)
        divider=Line(UP*2.8,DOWN*2.8,color=INK,stroke_opacity=.3)
        left=RoundedRectangle(width=7,height=5.4,corner_radius=.15).set_fill(TEAL,.06).set_stroke(TEAL,2).move_to(LEFT*3.8)
        right=RoundedRectangle(width=7,height=5.4,corner_radius=.15).set_fill(CRIMSON,.05).set_stroke(CRIMSON,2).move_to(RIGHT*3.8)
        lh=Text("MICROWAVE • 10 GHz",font=DISPLAY,font_size=24,color=TEAL).move_to(LEFT*3.8+UP*2.15)
        rh=Text("ULTRAVIOLET • 10¹⁵ Hz",font=DISPLAY,font_size=24,color=CRIMSON).move_to(RIGHT*3.8+UP*2.15)
        le=Text("hν ≈ 0.00004 eV\nhν / kT ≈ 0.0016",font=MONO,font_size=23,color=TEAL,line_spacing=1.3).move_to(LEFT*3.8+UP*.8)
        re=Text("hν ≈ 4 eV\nhν / kT ≈ 160",font=MONO,font_size=23,color=CRIMSON,line_spacing=1.3).move_to(RIGHT*3.8+UP*.8)
        populated=VGroup(*[Square(.42).set_fill(TEAL,.55).set_stroke(TEAL,1).move_to(LEFT*5.7+RIGHT*(i%5)*.95+DOWN*(i//5)*.72) for i in range(15)])
        suppression=Text("e⁻¹⁶⁰ ≈ 0\nmode empty",font=MONO,font_size=29,color=CRIMSON,line_spacing=1.3).move_to(RIGHT*3.8+DOWN*1.25)
        verdict=Text("cheap packets fill • expensive packets vanish",font=SERIF,font_size=28,color=INK).move_to(DOWN*3.35)
        self.play(FadeIn(title),Create(divider),FadeIn(left),FadeIn(right),run_time=1)
        self.play(FadeIn(lh),FadeIn(rh),run_time=.6); self.play(Write(le),Write(re),run_time=1.2)
        self.play(LaggedStart(*[GrowFromCenter(x) for x in populated],lag_ratio=.06),FadeIn(suppression),run_time=1.8)
        self.play(FadeIn(verdict),run_time=.5); self.wait(max(.1,duration-5.1))

class B11_Recap(Scene):
    def construct(self):
        duration=DUR.get("B11",15)
        self.add(base())
        title=Text("THE ANSWER",font=DISPLAY,font_size=22,color=TEAL).move_to(UP*2.8)
        box=RoundedRectangle(width=12.5,height=2.3,corner_radius=.12).set_fill(TEAL,.07).set_stroke(TEAL,2)
        answer=Text("High-frequency modes demand packets\ntoo expensive for thermal energy to fill.",font=DISPLAY,font_size=31,color=INK,line_spacing=1.25)
        kicker=Text("QUANTIZED ENERGY EXCHANGE REMOVES THE CATASTROPHE",font=MONO,font_size=21,color=CRIMSON).move_to(DOWN*2.4)
        self.play(FadeIn(title),Create(box),run_time=.7); self.play(FadeIn(answer),FadeIn(kicker),run_time=.7)
        self.wait(max(.1,duration-1.4))
