"""vox_scenes.py — Vox-Style Explainers, Explained (the meta film, 16:9).

One Scene per GRAPHIC/CARD beat; the compile ladder retimes to measured
audio. Durations from beat_sheet.json (audio locked 2026-07-06):
B02 8.20 · B03 10.06 · B05 10.81 · B07 11.00 · B08 12.90 · B10 6.27 ·
B19 12.72 · B20 10.89 · B22 9.69 · B24 10.21 · B26 7.92.

Safe area ±6.4 x / ±3.5 y (16:9); every fixed placement carries explicit
margin arithmetic in comments (desk preflight — the film-five discipline).

RECURSIVE DATA: B07 draws its bars from THIS reel's beat_sheet.json at
import; B19 times its ring from THIS reel's mp3/words.json ("now." starts
frame 222 @ 24fps = 9.25s). Both fall back gracefully if run standalone.

Render:  bash scripts/vox_run.sh reels/vox-how-to-vox
"""
import sys, json, pathlib
_HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parents[1] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

GRAY_IM = "#8A8A8A"      # treated-media stand-in gray
CREAM_DK = "#E7DCC6"     # newsprint layer fill (darker cream, no gradient)


def _sheet():
    try:
        return json.load(open(_HERE / "beat_sheet.json"))
    except Exception:
        return None


def _word_start(beat_id, word, default):
    """Start time (s) of the first word containing `word` in the beat —
    the scene-side word clock (REMOTION.md plane not yet built)."""
    try:
        w = json.load(open(_HERE / "mp3" / "words.json"))
        fps = w["fps"]
        for tok in w["beats"][beat_id]:
            if word in tok["text"].lower():
                return tok["startFrame"] / fps
    except Exception:
        pass
    return default


# ---------------------------------------------------------------- CARDS

class B02_Title(Scene):            # 8.20s
    def construct(self):
        eye = Text("UNREAL REELS", font=SERIF, color=BLUE, font_size=24)
        t = Text("VOX-STYLE EXPLAINERS, EXPLAINED", font=SERIF, color=INK,
                 font_size=54, weight=BOLD)
        if t.width > 12.0:                       # 12.0 < 12.8 usable — safe
            t.scale_to_fit_width(12.0)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s = Text("by the video you're watching", font=SERIF, color=INK,
                 font_size=30, slant=ITALIC)
        eye.to_edge(UP, buff=1.2)                # top y ≈ 2.8 < 3.5 safe
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(t), Create(u), run_time=1.0)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(6.0)                           # 0.6+1.0+0.6+6.0 = 8.20


class B10_Phases(Scene):           # 6.27s
    def construct(self):
        eye = Text("THE PIPELINE", font=SERIF, color=BLUE, font_size=24)
        t = Text("SEVEN PHASES, FIVE GATES", font=SERIF, color=INK,
                 font_size=54, weight=BOLD)
        if t.width > 12.0:
            t.scale_to_fit_width(12.0)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s = Text("plan · factcheck · audio · run · stills · video · assemble",
                 font=SERIF, color=INK, font_size=28)
        if s.width > 11.5:
            s.scale_to_fit_width(11.5)
        eye.to_edge(UP, buff=1.2)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        self.play(FadeIn(s), run_time=0.5)
        self.wait(4.37)                          # 0.5+0.9+0.5+4.37 = 6.27


class B24_GetIt(Scene):            # 10.21s
    def construct(self):
        eye = Text("GET IT", font=SERIF, color=BLUE, font_size=24)
        t = Text("UNREAL REELS", font=SERIF, color=INK, font_size=54,
                 weight=BOLD)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        # URL is data — mono, never serif (EQUATIONS.md discipline)
        s1 = Text("github.com/nikbearbrown/unreal-reels", font=MONO,
                  color=INK, font_size=26)
        if s1.width > 11.0:
            s1.scale_to_fit_width(11.0)
        s2 = Text("docs/TUTORIAL.md · MIT license", font=SERIF, color=INK,
                  font_size=26, slant=ITALIC)
        eye.to_edge(UP, buff=1.2)
        s1.next_to(u, DOWN, buff=0.45)
        s2.next_to(s1, DOWN, buff=0.3)           # s2 bottom ≈ -1.6 — safe
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        self.play(FadeIn(s1, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(s2), run_time=0.6)
        self.wait(7.51)                          # 2.7+7.51 = 10.21


class B26_Next(Scene):             # 7.92s — outro law replaces this slot
    def construct(self):
        eye = Text("NEXT", font=SERIF, color=BLUE, font_size=24)
        t = Text("SONGBIRD", font=SERIF, color=INK, font_size=54, weight=BOLD)
        u = Line(t.get_corner(DL) + DOWN * 0.15, t.get_corner(DR) + DOWN * 0.15,
                 color=CRIMSON, stroke_width=2)
        s = Text("unreal reels · music videos", font=SERIF, color=INK,
                 font_size=28)
        eye.to_edge(UP, buff=1.4)
        s.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        self.play(FadeIn(s), run_time=0.5)
        self.wait(6.02)                          # 1.9+6.02 = 7.92


# ---------------------------------------------------------------- GRAPHICS

class B03_LaunderingFunnel(Scene):  # 10.06s — mismatched in, matched out
    def construct(self):
        # inputs: 1.6×1.1 plates at x=-4.8 (left edge -5.6 < 6.4 safe),
        # rows y 1.9 / 0.4 / -1.1 (top 2.45 < 3.5 safe)
        specs = [(TERRA, 0.7, "archival photo"), (NAVY, 0.6, "AI still"),
                 (GOLD, 0.8, "film scan")]
        plates, tags = VGroup(), VGroup()
        for i, (col, op, name) in enumerate(specs):
            p = Rectangle(width=1.6, height=1.1).set_fill(col, op).set_stroke(col, 2)
            p.move_to([-4.8, 1.9 - i * 1.5, 0])
            tag = Text(name, font=SERIF, color=INK, font_size=20)
            tag.next_to(p, DOWN, buff=0.12)
            plates.add(p); tags.add(tag)
        # treatment bar: 1.1×4.4 at (0, 0.4) — top 2.6 < 3.5 safe
        bar = Rectangle(width=1.1, height=4.4).set_fill(INK, 0.85).set_stroke(width=0)
        bar.move_to([0, 0.4, 0])
        bar_lb = SerifLabel("one treatment", accent=TERRA, size=26)
        bar_lb.move_to([0, 3.0, 0])              # top ≈ 3.2 < 3.5 safe
        # output plane: line y=-2.35 from x 2.6..6.3 (< 6.4 safe)
        plane = Line([2.6, -2.35, 0], [6.3, -2.35, 0], color=INK, stroke_width=3)
        plane_lb = Text("one plane", font=SERIF, color=INK, font_size=22)
        plane_lb.move_to([4.45, -2.8, 0])        # bottom ≈ -2.95 — safe
        self.play(FadeIn(plates), FadeIn(tags), run_time=0.9)
        self.play(FadeIn(bar), FadeIn(bar_lb), run_time=0.7)
        # each plate passes through and lands MATCHED: same gray, same stroke
        for i, p in enumerate(plates):
            target = p.copy().move_to([4.6, 1.9 - i * 1.5, 0])
            target.set_fill(GRAY_IM, 0.55).set_stroke(INK, 2)
            self.play(Transform(p, target), run_time=1.6, rate_func=linear)
        self.play(Create(plane), FadeIn(plane_lb), run_time=0.9,
                  rate_func=linear)
        self.wait(2.76)                          # 0.9+0.7+4.8+0.9+2.76 = 10.06


class B05_RestraintRules(Scene):   # 10.81s — the flourish gets the X
    def construct(self):
        # three rule rows, left edge x=-5.8 (> -6.4 safe), y 2.0 / 0.7 / -0.6
        sw1 = Square(0.4).set_fill(BLUE, 1).set_stroke(width=0)
        sw2 = Square(0.4).set_fill(TERRA, 1).set_stroke(width=0)
        r1t = Text("two accents, max", font=SERIF, color=INK, font_size=28)
        row1 = VGroup(sw1, sw2, r1t).arrange(RIGHT, buff=0.25)
        row1.move_to([-5.8, 2.0, 0], aligned_edge=LEFT)
        row2 = SerifLabel("serif labels, hairline underlines", accent=BLUE,
                          size=28)
        row2.move_to([-5.8, 0.7, 0], aligned_edge=LEFT)
        r3t = Text("one editor's pen per graphic", font=SERIF, color=INK,
                   font_size=28)
        r3t.move_to([-5.8, -0.6, 0], aligned_edge=LEFT)
        ring = HandRing(r3t, color=TERRA)        # the pen, demonstrating itself
        # the decorative flourish: flat gold star at (3.8, -2.3) —
        # right edge 4.5 < 6.4, bottom -3.0 < 3.5 safe
        flourish = Star(n=8, outer_radius=0.7, inner_radius=0.35)
        flourish.set_fill(GOLD, 0.9).set_stroke(GOLD, 2).move_to([3.8, -2.3, 0])
        fl_tag = Text("decoration", font=SERIF, color=INK, font_size=20,
                      slant=ITALIC).next_to(flourish, LEFT, buff=0.3)
        # the ink X: two strokes crossing the flourish (not text — QC-clean)
        x1 = Line(flourish.get_center() + np.array([-0.85, 0.85, 0]),
                  flourish.get_center() + np.array([0.85, -0.85, 0]),
                  color=CRIMSON, stroke_width=7)
        x2 = Line(flourish.get_center() + np.array([-0.85, -0.85, 0]),
                  flourish.get_center() + np.array([0.85, 0.85, 0]),
                  color=CRIMSON, stroke_width=7)
        self.play(FadeIn(row1, shift=UP * 0.1), run_time=0.7); self.wait(0.8)
        self.play(FadeIn(row2, shift=UP * 0.1), run_time=0.7); self.wait(0.8)
        self.play(FadeIn(r3t), Create(ring), run_time=0.7); self.wait(0.8)
        self.play(FadeIn(flourish, scale=1.15), FadeIn(fl_tag), run_time=0.8)
        self.wait(1.5)
        self.play(Create(x1), Create(x2), run_time=0.7, rate_func=linear)
        self.play(flourish.animate.set_opacity(0.15),
                  fl_tag.animate.set_opacity(0.3), run_time=0.6)
        self.wait(2.71)                # 4.5+0.8+1.5+0.7+0.6+2.71 = 10.81


class B07_AudioClock(Scene):       # 11.00s — THIS sheet's bars; B07 fills live
    def construct(self):
        sheet = _sheet()
        if sheet:
            durs = [(b["beat_id"], b.get("actual_duration_s") or 10.0)
                    for b in sheet["beats"]]
        else:
            durs = [(f"B{i:02d}", 10.0) for i in range(1, 27)]
        n = len(durs)                            # 26
        # bars: pitch 0.42 → span 26*0.42−0.12 = 10.8; centers −5.25..+5.25
        # (< 6.4 safe); baseline y=−1.9; height 0.17/s → max 12.9s → 2.19
        # (top 0.29 < 3.5 safe)
        x0, pitch, y0, hscale = -5.25, 0.42, -1.9, 0.17
        top_lb = SerifLabel("every beat in this film, measured", accent=BLUE,
                            size=28)
        top_lb.move_to([0, 3.0, 0])              # top ≈ 3.2 < 3.5 safe
        base = Line([x0 - 0.35, y0, 0], [x0 + (n - 1) * pitch + 0.35, y0, 0],
                    color=INK, stroke_width=2)
        bars, self_bar, self_h = VGroup(), None, 1.0
        for i, (bid, d) in enumerate(durs):
            h = d * hscale
            if bid == "B07":
                self_bar, self_h = i, h
                continue                          # B07's bar animates later
            b = Rectangle(width=0.30, height=h)
            b.set_fill(NAVY, 0.6).set_stroke(width=0)
            b.move_to([x0 + i * pitch, y0 + h / 2, 0])
            bars.add(b)
        bot_lb = Text("the audio decides — never the word count", font=SERIF,
                      color=INK, font_size=26, slant=ITALIC)
        bot_lb.to_edge(DOWN, buff=0.55)          # bottom ≈ −3.45 — safe
        self.play(Create(base), FadeIn(top_lb), run_time=1.0)
        self.play(AnimationGroup(*[FadeIn(b, shift=UP * 0.1) for b in bars],
                                 lag_ratio=0.02, run_time=1.5))
        self.play(FadeIn(bot_lb), run_time=0.8)
        # B07's own bar grows in real time — 6.0s of linear fill
        gx = x0 + self_bar * pitch
        grow = Rectangle(width=0.30, height=self_h)
        grow.set_fill(CRIMSON, 1).set_stroke(width=0)
        grow.move_to([gx, y0 + self_h / 2, 0])
        self.play(GrowFromEdge(grow, DOWN), run_time=6.0, rate_func=linear)
        chip = Text("11.0 s", font=MONO, color=CRIMSON, font_size=22)
        chip.move_to([gx, y0 + self_h + 0.35, 0])   # y ≈ 0.32 — safe
        self.play(FadeIn(chip, shift=UP * 0.1), run_time=0.7)
        self.wait(1.0)                 # 1.0+1.5+0.8+6.0+0.7+1.0 = 11.00


class B08_TwoAxisGrid(Scene):      # 12.90s — type × source; one square swaps
    def construct(self):
        sheet = _sheet()
        counts = {}                              # (type, source) -> n
        if sheet:
            for b in sheet["beats"]:
                t, s = b["shot"]["type"], b["shot"]["source"]
                if t == "COMPOSITE":
                    continue                     # footnote chip carries it
                counts[(t, s)] = counts.get((t, s), 0) + 1
        else:
            counts = {("STILL", "ai"): 2, ("STILL", "own"): 2,
                      ("FOOTAGE", "own"): 4, ("DOCUMENT", "own"): 4,
                      ("GRAPHIC", "own"): 7, ("CARD", "own"): 4}
        rows = ["STILL", "FOOTAGE", "DOCUMENT", "GRAPHIC", "CARD"]
        cols = ["archive", "ai", "own"]
        colx = {"archive": -0.9, "ai": 1.7, "own": 4.3}   # rightmost 4.3+1.1<6.4
        rowy = {r: 1.9 - i * 0.95 for i, r in enumerate(rows)}   # 1.9..−1.9
        heads = VGroup(*[Text(c, font=SERIF, color=INK, font_size=24,
                              weight=BOLD).move_to([colx[c], 2.7, 0])
                         for c in cols])         # top 2.85 < 3.5 safe
        hline = Line([-4.6, 2.35, 0], [5.6, 2.35, 0], color=INK,
                     stroke_width=1).set_opacity(0.5)
        labels = VGroup()
        for r in rows:
            t = Text(r, font=SERIF, color=INK, font_size=24)
            t.move_to([-3.0, rowy[r], 0], aligned_edge=RIGHT)  # left ≥ −5.0
            labels.add(t)
        marks = VGroup()
        swap_mark, swap_target = None, None
        for (t, s), nn in sorted(counts.items()):
            for k in range(nn):
                m = Square(0.16).set_fill(NAVY if s == "own" else TERRA, 1)
                m.set_stroke(width=0)
                m.move_to([colx[s] - (nn - 1) * 0.13 + k * 0.26, rowy[t], 0])
                marks.add(m)
                # the swap demo tells B01's true history: planned ai,
                # became own (the interface decision) — one STILL mark
                # STARTS in the ai column and slides home during the beat
                if t == "STILL" and s == "own" and k == 0:
                    swap_mark, swap_target = m, m.get_center().copy()
                    m.move_to([colx["ai"], rowy["STILL"], 0])
                    m.set_fill(TERRA)
        form_lb = SerifLabel("form locks early", accent=NAVY, size=24)
        form_lb.move_to([-3.4, -2.6, 0])
        swap_lb = SerifLabel("source swaps late", accent=TERRA, size=24)
        swap_lb.move_to([3.0, -2.6, 0])
        chip = LabelChip("COMPOSITE = STILL + the annotation plane",
                         accent=SLATE, size=19)
        chip.move_to([0, -3.15, 0])              # bottom ≈ −3.4 < 3.5 safe
        self.play(FadeIn(heads), Create(hline), FadeIn(labels), run_time=1.2)
        self.wait(0.8)
        self.play(AnimationGroup(*[FadeIn(m, scale=0.85) for m in marks],
                                 lag_ratio=0.03, run_time=3.0))
        self.play(FadeIn(form_lb, shift=UP * 0.1), run_time=0.7)
        # the swap: B01's square slides ai → own — same row, same beat
        # (one method per .animate — recolor rides the next play)
        self.play(swap_mark.animate.move_to(swap_target), run_time=1.2)
        self.play(FadeIn(swap_lb, shift=UP * 0.1),
                  swap_mark.animate.set_fill(NAVY), run_time=0.7)
        self.play(FadeIn(chip), run_time=0.8)
        self.wait(4.5)       # 1.2+0.8+3.0+0.7+1.2+0.7+0.8+4.5 = 12.90


class B19_AnnotationPlane(Scene):  # 12.72s — the ring lands on "now" (9.25s)
    def construct(self):
        t_now = _word_start("B19", "now", 9.25)
        # three skewed layers: base w 6.0, skew 1.2, h 0.9;
        # x span −3.4..3.8 (< 6.4 safe); y bases −2.6 / −0.75 / 1.1
        def layer(y, fill, op):
            p = Polygon([-3.4, y, 0], [2.6, y, 0], [3.8, y + 0.9, 0],
                        [-2.2, y + 0.9, 0])
            p.set_fill(fill, op).set_stroke(INK, 2)
            return p
        ground = layer(-2.6, CREAM_DK, 1.0)
        media = layer(-0.75, GRAY_IM, 0.5)
        plane = layer(1.1, GROUND, 0.0)          # annotation plane: stroke only
        sample = LabelChip("label", accent=TERRA, size=18)
        sample.move_to([0.4, 1.55, 0])           # sits on the top layer
        names = [("annotation plane", 1.55), ("graphics plane", -0.30),
                 ("newsprint ground", -2.15)]
        tags = VGroup()
        for nm, y in names:
            t = Text(nm, font=SERIF, color=INK, font_size=24)
            t.move_to([-6.1, y, 0], aligned_edge=LEFT)   # left −6.1 > −6.4
            tags.add(t)
        self.play(FadeIn(ground), FadeIn(tags[2]), run_time=1.1)
        self.play(FadeIn(media), FadeIn(tags[1]), run_time=1.1)
        self.play(Create(plane), FadeIn(sample), FadeIn(tags[0]), run_time=1.1)
        # explode: top +0.55, bottom −0.55 (tops stay ≤ 3.0 < 3.5 safe)
        self.play(VGroup(plane, sample, tags[0]).animate.shift(UP * 0.55),
                  VGroup(ground, tags[2]).animate.shift(DOWN * 0.55),
                  run_time=1.0)
        self.play(tags[0].animate.set_color(TERRA), run_time=0.6)
        # word clock: ring Create COMPLETES at t_now (elapsed so far: 4.9)
        elapsed = 1.1 + 1.1 + 1.1 + 1.0 + 0.6
        ring_rt = 0.55
        self.wait(max(0.1, t_now - elapsed - ring_rt))
        ring = HandRing(sample, color=TERRA)
        self.play(Create(ring), run_time=ring_rt, rate_func=linear)
        bot = Text("the media below is never touched", font=SERIF, color=INK,
                   font_size=26, slant=ITALIC)
        bot.to_edge(DOWN, buff=0.55)             # bottom ≈ −3.45 — safe
        self.play(FadeIn(bot, shift=UP * 0.1), run_time=0.8)
        self.wait(max(0.1, 12.72 - t_now - 0.8))


class B20_Reband(Scene):           # 10.89s — side by side → stacked
    def construct(self):
        # landscape frame 4.8×2.7 at (−3.5, 0.9): x −5.9..−1.1, y −0.45..2.25
        land = Rectangle(width=4.8, height=2.7).set_stroke(INK, 3)
        land.move_to([-3.5, 0.9, 0])
        e1 = Rectangle(width=1.7, height=1.5).set_fill(NAVY, 0.8).set_stroke(width=0)
        e2 = Rectangle(width=1.7, height=1.5).set_fill(TERRA, 0.8).set_stroke(width=0)
        e1.move_to([-4.35, 0.9, 0]); e2.move_to([-2.65, 0.9, 0])
        land_lb = Text("16:9 — side by side", font=SERIF, color=INK,
                       font_size=24).move_to([-3.5, -1.1, 0])
        # portrait frame 2.0×3.56 at (3.7, 0.3): y −1.48..2.08 < ±3.5 safe
        port = Rectangle(width=2.0, height=3.56).set_stroke(INK, 3)
        port.move_to([3.7, 0.3, 0])
        port_lb = Text("9:16 — stacked", font=SERIF, color=INK,
                       font_size=24).move_to([3.7, -2.15, 0])
        bot = Text("same beats, re-banded — nothing renders twice",
                   font=SERIF, color=INK, font_size=26, slant=ITALIC)
        bot.to_edge(DOWN, buff=0.55)
        self.play(Create(land), FadeIn(land_lb), run_time=1.2)
        self.play(FadeIn(e1), FadeIn(e2), run_time=0.8)
        self.play(Create(port), run_time=0.8)
        # the re-band: COPIES travel — the originals stay (derivative cut)
        c1, c2 = e1.copy(), e2.copy()
        self.play(c1.animate.move_to([3.7, 1.15, 0]), run_time=1.3)
        self.play(c2.animate.move_to([3.7, -0.55, 0]), run_time=1.3)
        self.play(FadeIn(port_lb), run_time=0.7)
        self.play(FadeIn(bot, shift=UP * 0.1), run_time=0.7)
        self.wait(4.09)      # 1.2+0.8+0.8+1.3+1.3+0.7+0.7+4.09 = 10.89


class B22_CostIsotype(Scene):      # duration from sheet — 26 free · 1 + 1 paid
    def construct(self):
        # counts are claims — FACTCHECK.md B22 row (revised 2026-07-06):
        # 26 beats compiled free; paid = 1 narration (crimson) + 1 ai still
        # (terracotta — B18, the stand-in demo). B22's audio was regenerated
        # after the rewrite, so the final wait reads the sheet's duration.
        sheet = _sheet()
        dur = 9.69
        if sheet:
            for b in sheet["beats"]:
                if b["beat_id"] == "B22" and b.get("actual_duration_s"):
                    dur = b["actual_duration_s"]
        free = IsotypeGrid([26], [BLUE], per_row=13, size=0.22, gap=0.12)
        free.move_to([0, 1.6, 0])                # 13×0.34≈4.4 wide — safe
        free_lb = SerifLabel("free — every beat, compiled locally",
                             accent=BLUE, size=26)
        free_lb.move_to([0, 0.45, 0])
        paid = VGroup(
            Square(0.22).set_fill(CRIMSON, 1).set_stroke(width=0),
            Square(0.22).set_fill(TERRA, 1).set_stroke(width=0),
        )
        paid.arrange(RIGHT, buff=0.12).move_to([0, -1.1, 0])
        paid_lb = SerifLabel("paid — one narration + one still",
                             accent=TERRA, size=26)
        paid_lb.move_to([0, -1.85, 0])
        chip = LabelChip("everything else: $0", accent=SLATE, size=22)
        chip.move_to([0, -2.9, 0])               # bottom ≈ −3.15 — safe
        self.play(free.count_up(3.2))            # counts finish with the line
        self.play(FadeIn(free_lb), run_time=0.6)
        self.play(AnimationGroup(*[FadeIn(m, scale=0.85) for m in paid],
                                 lag_ratio=0.15, run_time=1.2))
        self.play(FadeIn(paid_lb), run_time=0.6)
        self.play(FadeIn(chip, scale=1.1), run_time=0.8)
        self.wait(max(0.1, dur - 6.4))   # 3.2+0.6+1.2+0.6+0.8 = 6.4 elapsed
