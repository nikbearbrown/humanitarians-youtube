"""vox_scenes.py — The Agent Said 'Done' — and Its Own Report Was Wrong
(vox-agent-said-done, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. Durations read from
this reel's beat_sheet.json (actuals after audio lock; estimates as fallback).
Render everything:
  bash scripts/vox_run.sh reels/vox-agent-said-done

Device: two tracks — terracotta = the agent's picture, blue = the world.
Boxes float ABOVE their track line (tick connectors), so no text ever sits on
a stroke (Gate B rule). The server/email box never takes a mark — untouched
is the claim. One ring: B08, on the contradicting chip pair.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {"B01": 8.0, "B03": 10.8, "B04": 9.6, "B05": 9.2, "B06": 9.6,
       "B07": 10.8, "B08": 9.6, "B09": 9.2, "B10": 10.0, "B11": 8.4}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 6.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ------------------------------------------------------------- the tracks

_AGENT_Y = 1.35     # track lines
_WORLD_Y = -1.85


def _tracks():
    a = Line([-5.6, _AGENT_Y, 0], [5.6, _AGENT_Y, 0], color=TERRA,
             stroke_width=3)
    w = Line([-5.6, _WORLD_Y, 0], [5.6, _WORLD_Y, 0], color=BLUE,
             stroke_width=3)
    la = SerifLabel("the agent's picture", TERRA, size=24)
    la.move_to(np.array([-3.8, 2.95, 0]))
    lw = SerifLabel("the world", BLUE, size=24)
    lw.move_to(np.array([-4.6, -3.0, 0]))
    return VGroup(a, w, la, lw)


def _box(text, x, track_y, color=INK, w=2.3, h=0.75):
    """A labeled box floating above its track, with a tick connector —
    text never sits on the track stroke."""
    box = Rectangle(width=w, height=h).set_fill(WHITE, 1)
    box.set_stroke("#D8D2C4", 1.5)
    yc = track_y + 0.65 + h / 2
    box.move_to(np.array([x, yc, 0]))
    t = Text(text, font=SERIF, color=color, font_size=24)
    if t.width > w - 0.35:
        t.scale_to_fit_width(w - 0.35)
    t.move_to(box)
    tick = Line([x, track_y + 0.06, 0], [x, yc - h / 2, 0], color=INK,
                stroke_width=2)
    return VGroup(box, t, tick)


def _strike(target):
    g = VGroup(
        Line(target.get_corner(UL) + UL * 0.08,
             target.get_corner(DR) + DR * 0.08, color=TERRA, stroke_width=6),
        Line(target.get_corner(UR) + UR * 0.08,
             target.get_corner(DL) + DL * 0.08, color=TERRA, stroke_width=6))
    for m in g:
        m._qc_intentional = True
    return g


def _chip_at(text, accent, x, track_y):
    c = LabelChip(text, accent=accent, size=24)
    if c.width > 3.1:
        c.scale_to_fit_width(3.1)
    c.move_to(np.array([x, track_y + 1.05, 0]))
    return c


def _state_b07():
    """Everything on the tracks at the end of B07 (for B08 to inherit)."""
    tracks = _tracks()
    client = _box("local client", -2.0, _AGENT_Y)
    server = _box("server — the email", -2.0, _WORLD_Y)
    setup = _box("owner's setup", 0.9, _WORLD_Y, w=2.1)
    x1 = _strike(client[0])
    x2 = _strike(setup[0])
    done = _chip_at("TASK COMPLETE", TERRA, 3.6, _AGENT_Y)
    still = _chip_at("email — still there", BLUE, 3.6, _WORLD_Y)
    return VGroup(tracks, client, server, setup, x1, x2, done, still)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("VALIDATING AGENTIC AI", font=SERIF, color=BLUE,
                   font_size=24)
        t1 = Text("The agent said 'done' —", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("and its own report was wrong", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        if t2.width > 12.0:
            t2.scale_to_fit_width(12.0)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TERRA, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_NoTool(Scene):
    def construct(self):
        total = DUR["B03"]
        title = SerifLabel("no tool for the task", NAVY, size=28)
        title.to_edge(UP, buff=0.55)
        names = ("send", "read", "files", "shell", "delete email")
        tray = VGroup()
        for i, name in enumerate(names):
            box = Rectangle(width=1.9, height=0.95)
            if i < 4:
                box.set_fill(WHITE, 1).set_stroke("#D8D2C4", 1.5)
                t = Text(name, font=SERIF, color=INK, font_size=24)
            else:
                box.set_fill(WHITE, 0.4).set_stroke("#B9B2A4", 1.5)
                t = Text(name, font=SERIF, color="#9A938A", font_size=22,
                         slant=ITALIC)
            if t.width > 1.55:
                t.scale_to_fit_width(1.55)
            box.move_to(np.array([-4.5 + i * 2.25, 1.1, 0]))
            t.move_to(box)
            tray.add(VGroup(box, t))
        self.play(FadeIn(title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(s, shift=DOWN * 0.12) for s in tray],
                              lag_ratio=0.12, run_time=1.6))
        arrow = Line(np.array([4.5, 0.5, 0]), np.array([1.6, -1.35, 0]),
                     color=INK, stroke_width=2.5)
        arrow.add_tip(tip_length=0.16, tip_width=0.16)
        chip = LabelChip("nuclear option — reset the whole account",
                         accent=TERRA, size=26)
        if chip.width > 6.6:
            chip.scale_to_fit_width(6.6)
        chip.move_to(np.array([-0.4, -1.9, 0]))
        self.play(Create(arrow), run_time=0.8)
        self.play(FadeIn(chip, shift=UP * 0.15), run_time=0.8)
        self.wait(max(0.5, total - 3.7))


class B04_Report(Scene):
    def construct(self):
        _quote_scene(self, "Email account RESET completed.",
                     "— the agent's final report (Shapira et al., 2026)",
                     None, "completed", DUR["B04"])


class B05_TwoTracks(Scene):
    def construct(self):
        total = DUR["B05"]
        tracks = _tracks()
        self.play(Create(tracks[0]), FadeIn(tracks[2]), run_time=1.3)
        self.play(Create(tracks[1]), FadeIn(tracks[3]), run_time=1.3)
        self.wait(max(0.5, total - 2.6))


class B06_ClientServer(Scene):
    def construct(self):
        total = DUR["B06"]
        self.add(_tracks())
        client = _box("local client", -2.0, _AGENT_Y)
        server = _box("server — the email", -2.0, _WORLD_Y)
        self.play(FadeIn(client, shift=DOWN * 0.15), run_time=1.0)
        self.play(FadeIn(server, shift=UP * 0.15), run_time=1.0)
        self.wait(max(0.5, total - 2.0))


class B07_TheReset(Scene):
    def construct(self):
        total = DUR["B07"]
        tracks = _tracks()
        client = _box("local client", -2.0, _AGENT_Y)
        server = _box("server — the email", -2.0, _WORLD_Y)
        self.add(tracks, client, server)
        setup = _box("owner's setup", 0.9, _WORLD_Y, w=2.1)
        self.play(FadeIn(setup, shift=UP * 0.12), run_time=0.7)
        self.play(FadeIn(_strike(client[0])), run_time=0.7)
        done = _chip_at("TASK COMPLETE", TERRA, 3.6, _AGENT_Y)
        self.play(FadeIn(done, scale=0.9), run_time=0.7)
        still = _chip_at("email — still there", BLUE, 3.6, _WORLD_Y)
        self.play(FadeIn(still, scale=0.9), run_time=0.7)
        self.play(FadeIn(_strike(setup[0])), run_time=0.7)
        self.wait(max(0.5, total - 3.5))


class B08_Contradiction(Scene):
    def construct(self):
        total = DUR["B08"]
        self.add(_state_b07())
        zone = Rectangle(width=3.6, height=3.9)
        zone.set_stroke(width=0).set_fill(opacity=0)
        zone.move_to(np.array([3.6, (_AGENT_Y + _WORLD_Y) / 2 + 1.05, 0]))
        ring = HandRing(zone, color=TERRA)     # the film's single ring
        self.play(Create(ring), run_time=1.2)
        self.wait(max(0.5, total - 1.2))


class B09_StillThere(Scene):
    def construct(self):
        _quote_scene(self, "The email was still there.",
                     "— the owner, checking the server directly", None,
                     "still", DUR["B09"])


class B10_AskTheWorld(Scene):
    def construct(self):
        total = DUR["B10"]
        title = SerifLabel("grade against the world", NAVY, size=28)
        title.to_edge(UP, buff=0.55)
        # left: self-graded (struck)
        rep_l = _box("report", -3.4, -0.2, w=1.9)
        rep_l[2].set_opacity(0)          # no tick here
        loop = ArcBetweenPoints(rep_l[0].get_right() + RIGHT * 0.05,
                                rep_l[0].get_top() + UP * 0.05,
                                angle=-2.4, color=TERRA, stroke_width=3)
        loop.add_tip(tip_length=0.14, tip_width=0.14)
        lab_l = SerifLabel("graded against itself", TERRA, size=24)
        lab_l.move_to(np.array([-3.4, -1.9, 0]))
        # right: world-graded
        rep_r = _box("report", 1.4, -0.2, w=1.9)
        rep_r[2].set_opacity(0)
        world = _box("the world", 4.6, -0.2, w=1.9)
        world[2].set_opacity(0)
        check = Line(rep_r[0].get_right() + RIGHT * 0.08,
                     world[0].get_left() + LEFT * 0.08,
                     color=BLUE, stroke_width=3)
        check.add_tip(tip_length=0.14, tip_width=0.14)
        lab_r = SerifLabel("graded against the world", BLUE, size=24)
        lab_r.move_to(np.array([3.0, -1.9, 0]))
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(rep_l), Create(loop), FadeIn(lab_l), run_time=1.1)
        self.play(FadeIn(_strike(loop)), run_time=0.6)
        self.play(FadeIn(rep_r), FadeIn(world), Create(check), FadeIn(lab_r),
                  run_time=1.2)
        self.wait(max(0.5, total - 3.4))


class B11_End(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Don't ask the agent.", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("Ask the world.", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=BLUE, stroke_width=2)
        s = Text("from Computational Skepticism for AI — chapter 9",
                 font=SERIF, color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
