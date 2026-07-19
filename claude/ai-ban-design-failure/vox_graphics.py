"""vox_graphics.py — the vox-explainer Manim graphics library.

Renders GRAPHIC-type beats as per-beat fragments that drop into a reel's
manim/<beat>.mp4 slot (the compiler picks them up by filename). Every scene is
rendered TO THE BEAT'S MEASURED DURATION — pass it via the BEAT env pair or
edit the fixture scenes at the bottom.

Render (on the user's machine, local, free):
  manim -qh --fps 24 -r 1920,1080 vox_graphics.py B07_HouseSenate
  mv media/videos/.../B07_HouseSenate.mp4 reels/<slug>/manim/B07.mp4

Design tokens (from the vox/ reference frames — keep in sync with SKILL.md):
  ground #F3EBDD · ink #2F2A26 · crimson #BF3339 · navy #3D5A80
  dusty-blue #5B7B9C · terracotta #D35F43 · highlighter #F5D061 · slate #3E5559
Restraint: two accents max; count-up lag_ratio 0.003–0.01 (a grid "counts up",
never bounces); serif labels with hairline underlines; no gradients, glows,
or shadows. If a choice reads as decorative, delete it.
"""
from manim import *

try:            # geometry-stub environments (static_scene_check) lack these
    BOLD
except NameError:
    BOLD = "BOLD"
try:
    ITALIC
except NameError:
    ITALIC = "ITALIC"

import os as _os
# ---- palette registry (DESIGN.md). Same SIX role keys, different values; select with
#      env VOX_PALETTE=teardown|newsprint|neu|medhavy|humanitarians. Default = teardown
#      (NikBearBrown house look: minimalist white / ink / RED-ONLY; good = plain ink,
#      carried by KEPT/LOST label + position — never a second hue).
_PALETTES = {
    #                 GROUND      INK(text)  TEAL(good)  CRIMSON(bad) SLATE(struct) GOLD(highlight) HAIRLINE
    "teardown":      ("#FFFFFF", "#2A1A0E", "#2A1A0E", "#C8102E", "#545454", "#F6D8DC", "#D4D4D4"),
    "newsprint":     ("#F3EBDD", "#2F2A26", "#1F6F5C", "#BF3339", "#3E5559", "#F5D061", "#D4D4D4"),
    "neu":           ("#FFFFFF", "#000000", "#000000", "#545454", "#545454", "#A4804A", "#E3E3E3"),
    "medhavy":       ("#F0EAD6", "#000000", "#009E73", "#D55E00", "#4D4D4D", "#F0E442", "#D4D4D4"),
    "humanitarians": ("#F3EBDD", "#2F2A26", "#1F4E5F", "#E4572E", "#29335C", "#F3A712", "#D4D4D4"),
}
_PAL = _os.environ.get("VOX_PALETTE", "teardown")
GROUND, INK, TEAL, CRIMSON, SLATE, GOLD, HAIRLINE = _PALETTES.get(_PAL, _PALETTES["teardown"])
# TEAL = good/kept/true, CRIMSON = bad/lost/broken (see books/vox/DESIGN.md). In teardown/neu
# TEAL == INK (good is plain ink; the KEPT/LOST label + side carry it — red is the one accent).
# GOLD = highlighter fill ONLY (never text); in teardown it is a wash of the one accent. SLATE = structure.
NEU_RED = "#C8102E"   # NEU brand/emphasis/primary-series only — never "state" (Northeastern brand law)
# retired hues, aliased so legacy scenes + the electoral-college fixture don't crash:
NAVY = TEAL          # navy dropped -> renders the good/kept accent now
BLUE = SLATE         # dusty-blue dropped -> slate
TERRA = CRIMSON      # terracotta dropped -> crimson
# type system — fonts live in books/vox/fonts/, resolved by family name via fontconfig.
# NEU overrides ALL type to Lato (Northeastern brand law); every other palette keeps the house type.
if _PAL == "neu":
    DISPLAY = SANS = SERIF = "Lato"   # NEU: regular-weight headings, sentence case (brand law)
else:
    DISPLAY = "Montserrat"    # titles / big display lines / LabelChip tracked caps
    SANS    = "Inter"         # reserved — no live component role (chips + annotation labels moved to DISPLAY/SERIF, 2026-07)
    SERIF   = "EB Garamond"   # editorial serif: quote cards, attributions, entity cards, SerifLabel (italic)

config.background_color = GROUND

# Portrait sync (the bn_layout fix): Manim CE sets pixel dims from -r W,H but
# does NOT recompute frame_width, leaving the 16:9 default (14.22) — portrait
# scenes composed for a 4.5-unit frame render at a third of their size. Keep
# frame_height 8.0, derive frame_width from the real pixel aspect.
try:
    _pw = getattr(config, "pixel_width", None)
    _ph = getattr(config, "pixel_height", None)
    if _pw and _ph and abs(config.frame_width - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass


# ---------------------------------------------------------------- mobjects

class IsotypeGrid(VGroup):
    """One mark per unit, reading order, colored by category. Squares by
    default (the Electoral College film uses squares on newsprint)."""

    def __init__(self, counts, colors, per_row=None, size=0.14, gap=0.09,
                 mark="square", **kw):
        super().__init__(**kw)
        total = sum(counts)
        per_row = per_row or max(5, min(30, int((total * 1.7) ** 0.5)))
        seq = [c for n, c in zip(counts, colors) for _ in range(n)]
        self.marks = VGroup()
        for i, c in enumerate(seq):
            m = (Square(size) if mark == "square" else Dot(radius=size / 2))
            m.set_fill(c, 1).set_stroke(width=0)
            m.move_to(RIGHT * (i % per_row) * (size + gap)
                      + DOWN * (i // per_row) * (size + gap))
            self.marks.add(m)
        self.add(self.marks)

    def count_up(self, run_time, lag_ratio=0.005):
        """The reveal. Total run_time should come from the beat's audio
        window — the grid finishes counting as the line finishes."""
        return AnimationGroup(*[FadeIn(m, scale=0.85) for m in self.marks],
                              lag_ratio=lag_ratio, run_time=run_time)


class SerifLabel(VGroup):
    """Serif label + hairline underline in its accent (the Vox unit).
    EB Garamond italic — editorial marginalia, kin to the quote cards."""

    def __init__(self, text, accent=BLUE, size=30, **kw):
        super().__init__(**kw)
        # Garamond's x-height runs small next to Inter; bump ~15% so every
        # existing call site keeps its stated size and stays legible on video.
        t = Text(text, font=SERIF, color=INK, font_size=int(size * 1.15),
                 slant=ITALIC)
        u = Line(t.get_corner(DL) + DOWN * 0.08, t.get_corner(DR) + DOWN * 0.08,
                 stroke_width=1.6, color=accent)
        self.add(t, u)


class LabelChip(VGroup):
    """Accent block, white Montserrat caps ('THREE-FIFTHS CLAUSE') — echoes
    the tracked-caps kicker style."""

    def __init__(self, text, accent=CRIMSON, size=26, **kw):
        super().__init__(**kw)
        # Caps set wider than mixed case: shave the size a touch so chips
        # keep their footprint and don't crowd neighbors in old scenes.
        t = Text(text.upper(), font=DISPLAY, color=WHITE,
                 font_size=int(size * 0.88), weight="MEDIUM")
        # stroke opacity 0, not just width 0 — a zero-width stroke still
        # registers as segments in the layout audit and self-strikes the chip
        box = (SurroundingRectangle(t, buff=0.13).set_fill(accent, 1)
               .set_stroke(width=0, opacity=0))
        self.add(box, t)


class StateCard(VGroup):
    """Slate-teal entity card: white serif name (+ optional figure lines)."""

    def __init__(self, name, side=2.6, figures=(), accent=TERRA, **kw):
        super().__init__(**kw)
        card = Square(side).set_fill(SLATE, 1).set_stroke(width=0)
        label = Text(name, font=SERIF, color=WHITE, font_size=34)
        if label.width > side * 0.86:          # QC: label must FIT the card
            label.scale_to_fit_width(side * 0.86)
        label.move_to(card)
        self.add(card, label)
        y = card.get_bottom() + DOWN * 0.35
        for head, value, accented in figures:
            hd = Text(head, font=SERIF, color=INK, font_size=24)
            vl = Text(value, font=SERIF, color=(accent if accented else INK),
                      font_size=40, weight=BOLD)
            hd.move_to(y, UP); vl.next_to(hd, DOWN, buff=0.08)
            self.add(hd, vl)
            y = vl.get_bottom() + DOWN * 0.3


class HandRing(VMobject):
    """The editor's pen — a slightly wobbly hand-drawn ellipse. Use ONCE per
    graphic at most."""

    def __init__(self, around, color=TERRA, wobble=0.05, **kw):
        super().__init__(color=color, stroke_width=6, **kw)
        import numpy as np
        c, w, h = around.get_center(), around.width * 0.75, around.height * 0.85
        pts = [c + np.array([np.cos(a) * w * (1 + wobble * np.sin(3 * a + 1)),
                             np.sin(a) * h * (1 + wobble * np.cos(2 * a)), 0])
               for a in np.linspace(0.3, TAU + 0.55, 60)]
        self.set_points_smoothly(pts)
        self._qc_intentional = True    # the editor's pen touches text on purpose


# ---------------------------- equation tangent (../../EQUATIONS.md, bundled)
# The five-zone tangent translated into Vox language. Doctrine lives in
# EQUATIONS.md (bundled beside SKILL.md); this is the Vox rendering of it:
#   one red, moving  -> CRIMSON spotlight (equation + glossary row + example
#                       value turn crimson together for the symbol being named)
#   pink values box  -> terracotta-tinted panel (the editor's judgment)
#   white mechanics  -> newsprint ground, ink serif
#   KaTeX            -> MathTex (real math: italic vars, roman operators);
#                       falls back to italic serif Text where LaTeX is absent
# A tangent is a BEAT GROUP, not one long beat: the equation card persists as
# the anchor; the zone below swaps per beat (sentences -> glossary -> example
# -> claim). Re-entry is narration only. ~45s across the group; never derive.

MONO = "PT Mono"  # data numbers + math values only — never the running text


def _math(tex, font_size=48, color=INK, plain=None):
    """Real math if LaTeX is available; italic serif otherwise. The fallback
    renders `plain` (the unicode form, 'E = hν') — NEVER the raw TeX."""
    try:
        return MathTex(tex, font_size=font_size, color=color)
    except Exception:
        return Text(plain or tex, font=SERIF, color=color,
                    font_size=int(font_size * 0.75), slant=ITALIC)


class EquationCard(VGroup):
    """Zone 1 — the symbolic form, large, isolated, on a slate card."""

    def __init__(self, tex, spotlight=None, width=9.0, plain=None, **kw):
        super().__init__(**kw)
        eq = _math(tex, font_size=56, color=WHITE, plain=plain)
        if eq.width > width * 0.88:
            eq.scale_to_fit_width(width * 0.88)
        card = Rectangle(width=width, height=eq.height + 1.0)
        card.set_fill(SLATE, 1).set_stroke(width=0)
        eq.move_to(card)
        if spotlight:
            try:                # real MathTex only — on the Text fallback,
                eq.set_color_by_tex(spotlight, CRIMSON)
            except (AttributeError, TypeError):
                pass            # Mobject.__getattr__ fakes a setter and TypeErrors
        self.eq = eq
        self.add(card, eq)


class SentencePair(VGroup):
    """Zone 2 — LHS / RHS as one sentence each, then the relation symbol
    read as a claim. Sentences before symbols; the claim gets the accent."""

    def __init__(self, lhs, rhs, claim, size=30, **kw):
        super().__init__(**kw)
        rows = VGroup()
        for tag, sentence in (("LHS", lhs), ("RHS", rhs)):
            chip = Text(tag, font=SERIF, color=WHITE, font_size=20)
            box = SurroundingRectangle(chip, buff=0.1).set_fill(NAVY, 1).set_stroke(width=0)
            line = Text(sentence, font=SERIF, color=INK, font_size=size)
            row = VGroup(VGroup(box, chip), line).arrange(RIGHT, buff=0.35)
            rows.add(row)
        cl = SerifLabel(claim, accent=CRIMSON, size=size)
        rows.add(cl)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        self.claim = cl
        self.add(rows)


class GlossaryTable(VGroup):
    """Zone 3 — Symbol | Role | Plain meaning | Domain. The Role column is
    the point (random variable vs fixed value vs index vs operator)."""

    COLS = ("Symbol", "Role", "Meaning", "Domain")

    def __init__(self, rows, spotlight=None, col_x=(0.0, 2.2, 5.2, 9.6),
                 size=26, **kw):
        super().__init__(**kw)
        table = VGroup()
        header = VGroup(*[Text(h, font=SERIF, color=BLUE, font_size=size - 4)
                          for h in self.COLS])
        table.add(header)
        for r in rows:
            hot = spotlight is not None and r["sym"] == spotlight
            sym = _math(r.get("sym_tex", r["sym"]), font_size=size + 8,
                        color=CRIMSON if hot else INK, plain=r["sym"])
            cells = VGroup(sym,
                           Text(r["role"], font=SERIF, color=TERRA if hot else BLUE,
                                font_size=size - 4, slant=ITALIC),
                           Text(r["mean"], font=SERIF, color=INK, font_size=size - 2),
                           Text(r["dom"], font=MONO, color=INK, font_size=size - 6))
            table.add(cells)
        for row in table:
            for cell, x in zip(row, col_x):
                cell.move_to(RIGHT * x, aligned_edge=LEFT)
        table.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        spans = [col_x[i + 1] - col_x[i] - 0.35 for i in range(len(col_x) - 1)]
        spans.append(3.4)                       # last column's budget
        for row in table:                       # re-pin columns after arrange
            y = row.get_center()[1]
            for cell, x, span in zip(row, col_x, spans):
                if cell.width > span:           # never bleed into the next column
                    cell.scale_to_fit_width(span)
                cell.move_to(RIGHT * x + UP * y, aligned_edge=LEFT)
        rule = Line(ORIGIN, RIGHT * (col_x[-1] + 1.6), stroke_width=1.6, color=BLUE)
        rule.next_to(table[0], DOWN, buff=0.14, aligned_edge=LEFT)
        self.add(table, rule)


class WorkedExample(VGroup):
    """Zone 4 — real numbers that hold or break. Numbers in mono; verdict
    explicit; end on what it costs the people involved."""

    def __init__(self, ex, spotlight=None, size=30, **kw):
        super().__init__(**kw)
        scenario = Text(ex["scenario"], font=SERIF, color=INK, font_size=size)
        lv = Text(ex["lhs_val"], font=MONO, color=CRIMSON, font_size=size + 14)
        rv = Text(ex["rhs_val"], font=MONO, color=NAVY, font_size=size + 14)
        vs = Text("vs", font=SERIF, color=BLUE, font_size=size - 4)
        pair = VGroup(lv, vs, rv).arrange(RIGHT, buff=0.5)
        verdict = SerifLabel(ex["verdict"], accent=TERRA, size=size)
        cost = Text(ex["cost"], font=SERIF, color=INK, font_size=size - 4,
                    slant=ITALIC)
        self.pair, self.verdict = pair, verdict
        self.add(VGroup(scenario, pair, verdict, cost)
                 .arrange(DOWN, aligned_edge=LEFT, buff=0.45))


class ValuesClaim(VGroup):
    """Zone 5 — the contestable judgment. Terracotta tint = a value claim,
    not mechanics (the Vox reading of the brutalist pink box)."""

    def __init__(self, text, size=30, width=10.5, **kw):
        super().__init__(**kw)
        body = Text(text, font=SERIF, color=INK, font_size=size)
        if body.width > width * 0.9:
            body.scale_to_fit_width(width * 0.9)
        panel = Rectangle(width=width, height=body.height + 0.9)
        panel.set_fill(TERRA, 0.16).set_stroke(TERRA, 1.6)
        body.move_to(panel)
        self.add(panel, body)


class EquationTangent:
    """Builds the per-beat zone layouts from an EQUATIONS.md schema dict.
    Each tangent beat scene calls .frame(zone, spotlight) and animates the
    reveal across the beat's measured duration."""

    def __init__(self, data):
        self.d = data

    def eyebrow(self):
        return LabelChip(self.d["eyebrow"].upper(), accent=CRIMSON, size=22)

    def anchor(self, spotlight=None):
        """The persistent equation card, seated at the top of the frame."""
        return EquationCard(self.d.get("equation_tex", self.d["equation"]),
                            spotlight=spotlight,
                            plain=self.d["equation"]).to_edge(UP, buff=0.9)

    def zone(self, which, spotlight=None):
        d = self.d
        z = {"sentences": lambda: SentencePair(d["lhs"], d["rhs"], d["claim"]),
             "glossary":  lambda: GlossaryTable(d["glossary"], spotlight),
             "example":   lambda: WorkedExample(d["example"], spotlight),
             "claim":     lambda: ValuesClaim(d["values_claim"])}[which]()
        if z.width > 12.2:
            z.scale_to_fit_width(12.2)
        if z.height > 4.3:                      # keep clear of the frame bottom
            z.scale_to_fit_height(4.3)
        z.move_to([0, -1.35, 0])                # band between anchor and bottom
        return z


# --------------------------------------------- fixture scenes (test reel)
# Durations = the beat's actual_duration_s from
# reels/vox-electoral-college/beat_sheet.json. Render → manim/<beat>.mp4.

class B07_HouseSenate(Scene):      # 7.0s
    def construct(self):
        house = VGroup(SerifLabel("House of Representatives — 435", NAVY),
                       IsotypeGrid([435], [INK], per_row=31))
        house.arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT, buff=0.9)
        sen = VGroup(SerifLabel("Senate — 100", NAVY),
                     IsotypeGrid([100], [INK], per_row=10))
        sen.arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=0.9)
        self.play(Write(house[0][0]), Create(house[0][1]), run_time=0.8)
        self.play(house[1].count_up(2.6))
        self.play(Write(sen[0][0]), Create(sen[0][1]), run_time=0.7)
        self.play(sen[1].count_up(1.6))
        self.wait(1.3)


class B10_PlusTwo(Scene):          # 11.0s — the +2 lands terracotta on cue
    def construct(self):
        tx = VGroup(SerifLabel("Texas — 38 electoral votes", NAVY),
                    IsotypeGrid([36, 2], [NAVY, TERRA], per_row=10))
        vt = VGroup(SerifLabel("Vermont — 3", NAVY),
                    IsotypeGrid([1, 2], [NAVY, TERRA], per_row=3))
        for g in (tx, vt):
            g.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        VGroup(tx, vt).arrange(RIGHT, buff=1.6, aligned_edge=UP).move_to(ORIGIN)
        self.play(Write(tx[0][0]), Write(vt[0][0]), run_time=1.0)
        self.play(AnimationGroup(  # representatives first…
            *[FadeIn(m, scale=0.85) for m in list(tx[1].marks[:36]) + [vt[1].marks[0]]],
            lag_ratio=0.006, run_time=3.4))
        self.wait(2.2)             # "…plus two — for each senator."
        self.play(AnimationGroup(  # …the +2 land terracotta on the words
            *[FadeIn(m, scale=1.2) for m in list(tx[1].marks[36:]) + list(vt[1].marks[1:])],
            lag_ratio=0.15, run_time=1.6))
        self.wait(2.8)


class B16_ThreeFifths(Scene):      # 6.0s — restraint: nothing else on screen
    def construct(self):
        grid = IsotypeGrid([3, 2], [INK, GROUND], per_row=5, size=0.9, gap=0.35)
        for m in grid.marks[3:]:
            m.set_stroke(INK, 3).set_fill(opacity=0)
        chip = LabelChip("Three-fifths clause").next_to(grid, UP, buff=0.7)
        grid.move_to(ORIGIN)
        self.play(FadeIn(chip, shift=DOWN * 0.2), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(m) for m in grid.marks], lag_ratio=0.12,
                              run_time=1.8))
        self.wait(3.4)


class B19_Map1948(Scene):          # 5.0s — legend + the ring on New York
    def construct(self):
        # Placeholder geometry: the production map uses PD shapefiles
        # (Census TIGER / Natural Earth) via SVGMobject. Legend + ring
        # mechanics are what this fragment demonstrates.
        year = Text("1948", font=SERIF, color=INK, font_size=44, weight=BOLD)
        year.to_edge(UP, buff=0.6)
        legend = VGroup(*[SerifLabel(n, c, size=30) for n, c in
                          (("Harry Truman", NAVY), ("Thomas Dewey", CRIMSON),
                           ("Strom Thurmond", GOLD))])
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_corner(DL, buff=0.8)
        ny = Square(0.8).set_stroke(width=0).move_to(RIGHT * 3.5 + UP * 1.2)
        self.play(FadeIn(year), LaggedStart(*[Write(l) for l in legend],
                                            lag_ratio=0.3, run_time=1.4))
        self.wait(1.4)
        self.play(Create(HandRing(ny)), run_time=0.9)   # "…New York…"
        self.wait(1.3)


# ------------------------------------------------ remaining fixture scenes
# (every non-archive beat renders from code; the human fills ONLY archive slots)

APPROX_DEM_2016 = {  # two-party Dem share, APPROXIMATE — VERIFY vs FEC before ship
 "AL":.36,"AK":.41,"AZ":.48,"AR":.36,"CA":.66,"CO":.53,"CT":.57,"DE":.56,
 "FL":.49,"GA":.47,"HI":.67,"ID":.31,"IL":.59,"IN":.40,"IA":.45,"KS":.39,
 "KY":.34,"LA":.40,"ME":.51,"MD":.63,"MA":.65,"MI":.50,"MN":.51,"MS":.41,
 "MO":.40,"MT":.38,"NE":.36,"NV":.51,"NH":.50,"NJ":.57,"NM":.54,"NY":.63,
 "NC":.48,"ND":.30,"OH":.46,"OK":.31,"OR":.56,"PA":.50,"RI":.58,"SC":.43,
 "SD":.34,"TN":.37,"TX":.45,"UT":.39,"VT":.61,"VA":.52,"WA":.58,"WV":.29,
 "WI":.50,"WY":.24}
TILE = {  # square-tile US cartogram (col,row), NPR-style layout — VERIFY
 "AK":(0,0),"ME":(11,0),"VT":(10,1),"NH":(11,1),"WA":(1,2),"ID":(2,2),"MT":(3,2),
 "ND":(4,2),"MN":(5,2),"WI":(6,2),"MI":(7,2),"NY":(9,2),"MA":(10,2),"RI":(11,2),
 "OR":(1,3),"NV":(2,3),"WY":(3,3),"SD":(4,3),"IA":(5,3),"IL":(6,3),"IN":(7,3),
 "OH":(8,3),"PA":(9,3),"NJ":(10,3),"CT":(11,3),"CA":(1,4),"UT":(2,4),"CO":(3,4),
 "NE":(4,4),"MO":(5,4),"KY":(6,4),"WV":(7,4),"VA":(8,4),"MD":(9,4),"DE":(10,4),
 "AZ":(2,5),"NM":(3,5),"KS":(4,5),"AR":(5,5),"TN":(6,5),"NC":(7,5),"SC":(8,5),
 "OK":(4,6),"LA":(5,6),"MS":(6,6),"AL":(7,6),"GA":(8,6),"HI":(0,7),"TX":(4,7),"FL":(8,7)}

def _quote_scene(scene, quote, attribution, credit, hi_words, total,
                 qsize=44):
    lines = _wrap(quote, 46)
    q = Paragraph(*lines, font=SERIF, color=INK,
                  font_size=qsize, alignment="center", line_spacing=0.9)
    # fit long quotes to the frame: the wrap alone can exceed the safe area at
    # this font size (short quotes fit; a full-sentence question does not)
    f = max(q.width / 12.4, q.height / 4.6, 1.0)
    if f > 1.0:
        q.scale(1.0 / f)
    q.move_to(UP * 0.6)
    att = Text(attribution, font=SERIF, color=INK, font_size=28)
    att.next_to(q, DOWN, buff=0.7)
    scene.play(FadeIn(q), run_time=1.0)
    scene.play(FadeIn(att, shift=UP * 0.1), run_time=0.6)
    if hi_words:
        key = hi_words.split()[0].lower().strip(".,…'\"")
        for ln_text, ln in zip(lines, q):  # gold bar behind the matching line
            if key in ln_text.lower():
                bar = Rectangle(width=0.1, height=ln.height + 0.18)
                bar.set_fill(GOLD, 0.55).set_stroke(width=0)
                bar.align_to(ln, LEFT).align_to(ln, DOWN).shift(DOWN * 0.04)
                scene.add(bar); ln.set_z_index(1)
                scene.play(bar.animate.stretch_to_fit_width(ln.width + 0.2)
                           .align_to(ln, LEFT), run_time=0.9)
                break
    if credit:
        cr = Text(credit, font=SERIF, color=INK, font_size=20)
        cr.to_corner(DL, buff=0.5)
        scene.play(FadeIn(cr), run_time=0.4)
    scene.wait(max(0.5, total - 3.9))

def _wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    return lines


class B01_Title(Scene):            # ~2s
    def construct(self):
        t = Text("The Electoral College, explained", font=SERIF, color=INK,
                 font_size=54, weight=BOLD)
        u = Line(t.get_corner(DL)+DOWN*0.15, t.get_corner(DR)+DOWN*0.15,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t), Create(u), run_time=0.9)
        self.wait(1.1)


class B05_SwingStates(Scene):      # ~7s
    def construct(self):
        _quote_scene(self, "What matters are those swing states.",
                     "— cable news, 2020", None, "swing states", 7.0)


class B08_TexasVermont(Scene):     # ~7s
    def construct(self):
        tx = StateCard("Texas", side=3.4)
        vt = StateCard("Vermont", side=1.6)
        VGroup(tx, vt).arrange(RIGHT, buff=2.2, aligned_edge=UP).move_to(ORIGIN)
        self.play(FadeIn(tx, shift=UP*0.2), run_time=1.0)
        self.wait(1.6)
        self.play(FadeIn(vt, shift=UP*0.2), run_time=1.0)
        self.wait(3.4)


class B09_Reps(Scene):             # ~5s
    def construct(self):
        tx = VGroup(SerifLabel("Texas — 36 representatives", NAVY),
                    IsotypeGrid([36], [NAVY], per_row=9))
        vt = VGroup(SerifLabel("Vermont — 1", NAVY), IsotypeGrid([1], [NAVY]))
        for g in (tx, vt): g.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        VGroup(tx, vt).arrange(RIGHT, buff=1.8, aligned_edge=UP).move_to(ORIGIN)
        self.play(Write(tx[0][0]), Write(vt[0][0]), run_time=0.9)
        self.play(tx[1].count_up(1.8), vt[1].count_up(0.4))
        self.wait(2.0)


class B11_Bars2016(Scene):         # ~4s — VERIFY data vs FEC
    def construct(self):
        title = SerifLabel("2016 election results by state", CRIMSON, size=34)
        title.to_edge(UP, buff=0.5)
        bars, bw = VGroup(), 0.21
        for i, (st, dem) in enumerate(sorted(APPROX_DEM_2016.items())):
            h = 5.2
            d = Rectangle(width=bw, height=h*dem).set_fill(NAVY,1).set_stroke(width=0)
            r = Rectangle(width=bw, height=h*(1-dem)).set_fill(CRIMSON,1).set_stroke(width=0)
            r.next_to(d, UP, buff=0.012)
            bars.add(VGroup(d, r))
        bars.arrange(RIGHT, buff=0.055, aligned_edge=DOWN).next_to(title, DOWN, buff=0.5)
        self.play(Write(title[0]), Create(title[1]), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(b, shift=UP*0.15) for b in bars],
                              lag_ratio=0.01, run_time=1.6))
        self.wait(1.7)


class B12_Map2016(Scene):          # ~5s — square-tile cartogram; VERIFY winners
    def construct(self):
        DEM = {s for s, v in APPROX_DEM_2016.items() if v >= 0.5}
        title = SerifLabel("2016 election results by state", CRIMSON, size=34)
        title.to_edge(UP, buff=0.5)
        tiles = VGroup()
        for st, (c, r) in TILE.items():
            sq = Square(0.52).set_stroke(GROUND, 2)
            sq.set_fill(NAVY if st in DEM else CRIMSON, 1)
            lb = Text(st, font=SERIF, color=WHITE, font_size=15)
            lb.move_to(sq)
            tiles.add(VGroup(sq, lb).move_to(RIGHT*c*0.56 + DOWN*r*0.56))
        tiles.center().shift(DOWN*0.4)
        self.play(Write(title[0]), Create(title[1]), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.012,
                              run_time=1.6))
        self.wait(2.7)


class B13_BarsEllipse(Scene):      # ~7s — the yellow editor's ellipse
    def construct(self):
        title = SerifLabel("no state is all-red or all-blue", GOLD, size=34)
        title.to_edge(UP, buff=0.5)
        bars, bw = VGroup(), 0.21
        for st, dem in sorted(APPROX_DEM_2016.items()):
            h = 5.2
            d = Rectangle(width=bw, height=h*dem).set_fill(NAVY,1).set_stroke(width=0)
            r = Rectangle(width=bw, height=h*(1-dem)).set_fill(CRIMSON,1).set_stroke(width=0)
            r.next_to(d, UP, buff=0.012)
            bars.add(VGroup(d, r))
        bars.arrange(RIGHT, buff=0.055, aligned_edge=DOWN).next_to(title, DOWN, buff=0.5)
        self.add(bars)
        band = Rectangle(width=bars.width*0.9, height=1.4).move_to(bars)
        self.play(Write(title[0]), Create(title[1]), run_time=0.8)
        self.wait(1.6)
        ring = HandRing(band, color=GOLD)
        self.play(Create(ring), run_time=1.2)
        self.wait(3.4)


class B14_WinnerTakeAll(Scene):    # ~8s — outlined regions flood on "ALL"
    def construct(self):
        grid = IsotypeGrid([100], [INK], per_row=10, size=0.34, gap=0.14)
        grid.move_to(ORIGIN)
        red_idx = [i for i in range(100) if (i % 10) < 4 and (i // 10) < 5]
        blue_idx = [i for i in range(100) if (i % 10) >= 5 and (i // 10) >= 4]
        self.play(grid.count_up(1.8))
        for idx, col in ((red_idx, CRIMSON), (blue_idx, NAVY)):
            outlined = {i: grid.marks[i].copy().set_stroke(col, 3).set_fill(opacity=0)
                        for i in idx}
            self.play(*[Transform(grid.marks[i], t) for i, t in outlined.items()],
                      run_time=0.9)
        self.wait(1.6)  # "…gets ALL its electoral votes."
        flooded = {i: grid.marks[i].copy().set_fill(c, 1).set_stroke(width=0)
                   for idx, c in ((red_idx, CRIMSON), (blue_idx, NAVY)) for i in idx}
        self.play(*[Transform(grid.marks[i], t) for i, t in flooded.items()],
                  run_time=1.2)
        self.wait(1.6)


class B17_VaPa1800(Scene):         # ~12s — VERIFY 1800 census figures
    def construct(self):
        va = StateCard("Virginia", side=2.6,
                       figures=[("Free people:", "539,000", False),
                                ("Enslaved people:", "347,000", True)])
        pa = StateCard("Pennsylvania", side=2.6,
                       figures=[("Free people:", "601,000", False),
                                ("Enslaved people:", "1,700", True)])
        VGroup(va, pa).arrange(RIGHT, buff=2.6, aligned_edge=UP).to_edge(UP, buff=0.9)
        self.play(FadeIn(va[0]), FadeIn(va[1]), FadeIn(pa[0]), FadeIn(pa[1]),
                  run_time=1.2)
        self.play(FadeIn(va[2]), FadeIn(va[3]), FadeIn(pa[2]), FadeIn(pa[3]),
                  run_time=1.0)   # free people
        self.wait(4.0)
        self.play(FadeIn(va[4]), FadeIn(va[5]), FadeIn(pa[4]), FadeIn(pa[5]),
                  run_time=1.0)   # enslaved people, terracotta
        self.wait(4.8)


class B18_Votes1800(Scene):        # ~7s — VERIFY VA 21 / PA 15
    def construct(self):
        va = VGroup(SerifLabel("Virginia — 21", CRIMSON),
                    IsotypeGrid([21], [INK], per_row=4))
        pa = VGroup(SerifLabel("Pennsylvania — 15", NAVY),
                    IsotypeGrid([15], [INK], per_row=4))
        for g in (va, pa): g.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        VGroup(va, pa).arrange(RIGHT, buff=2.4, aligned_edge=UP).move_to(ORIGIN)
        frame = SurroundingRectangle(va, buff=0.25).set_stroke(CRIMSON, 4)
        self.play(Write(va[0][0]), Write(pa[0][0]), run_time=0.9)
        self.play(va[1].count_up(1.6), pa[1].count_up(1.2))
        self.play(Create(frame), run_time=0.8)   # the three-fifths frame
        self.wait(3.3)


class B20_Gossett(Scene):          # ~12s
    def construct(self):
        _quote_scene(self,
            "I have no objection to the Negro in Harlem voting … but I do "
            "resent the fact that … his vote is worth a hundred times as much "
            "… as is the vote of a white man in Texas.",
            "— Rep. Ed Gossett, Texas, 1950", "Source: Alexander Keyssar",
            "a hundred times", 12.0, qsize=38)


class B22_End(Scene):              # ~4s
    def construct(self):
        t = Text("recreated as a vox-explainer test", font=SERIF, color=INK,
                 font_size=40)
        s = Text("not for publication", font=SERIF, color=INK, font_size=26)
        s.next_to(t, DOWN, buff=0.4)
        self.play(FadeIn(t), FadeIn(s), run_time=1.0)
        self.wait(3.0)


# ------------------------------- equation-tangent fixture (EQUATIONS.md demo)
# Demographic parity, straight from the bundled EQUATIONS.md authoring
# schema. One scene per tangent beat; durations are placeholders until a
# reel's beat_sheet.json supplies measured audio. Render any of them:
#   manim -qh --fps 24 -r 1920,1080 vox_graphics.py EQT_Glossary

_DEMO_TANGENT = EquationTangent({
    "eyebrow": "Metric 01 · equation · tangent",
    "equation": "P(Ŷ=1 | A=a) = P(Ŷ=1 | A=b)",
    "equation_tex": r"P(\hat{Y}=1 \mid A=a) = P(\hat{Y}=1 \mid A=b)",
    "lhs": "How often the model says “yes” to group A.",
    "rhs": "How often it says “yes” to group B.",
    "claim": "These two rates must be equal — not close, equal.",
    "glossary": [
        {"sym": "Ŷ", "sym_tex": r"\hat{Y}", "role": "random variable",
         "mean": "the model's prediction", "dom": "{0, 1}"},
        {"sym": "A", "sym_tex": "A", "role": "random variable",
         "mean": "group membership", "dom": "{a, b}"},
        {"sym": "a, b", "sym_tex": "a, b", "role": "fixed values",
         "mean": "the two specific groups", "dom": "categorical"},
        {"sym": "P(·)", "sym_tex": r"P(\cdot)", "role": "operator",
         "mean": "probability of", "dom": "[0, 1]"},
    ],
    "example": {
        "scenario": "A bank approves loans at 40% in neighborhood A, 22% in B.",
        "lhs_val": "40%", "rhs_val": "22%", "verdict": "40% ≠ 22% — violated",
        "cost": "Group B is handed loans far less often, regardless of who would repay.",
    },
    "values_claim": "Outcomes should be equal regardless of base rates — redress over accuracy.",
})


class EQT_Sentences(Scene):        # ~10s — zone 2: sentences before symbols
    def construct(self):
        tg = _DEMO_TANGENT
        eye = tg.eyebrow().to_corner(UL, buff=0.6)
        anchor = tg.anchor()
        z = tg.zone("sentences")
        self.play(FadeIn(eye), FadeIn(anchor), run_time=0.8)
        for row in z[0]:
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.9)
            self.wait(1.6)
        self.wait(2.1)


class EQT_Glossary(Scene):         # ~12s — zone 3: the Role column
    def construct(self):
        tg = _DEMO_TANGENT
        anchor = tg.anchor(spotlight=r"\hat{Y}")
        z = tg.zone("glossary", spotlight="Ŷ")
        self.add(anchor)
        self.play(FadeIn(z, shift=UP * 0.15), run_time=1.0)
        self.wait(11.0)


class EQT_Example(Scene):          # ~12s — zone 4: holds or breaks
    def construct(self):
        tg = _DEMO_TANGENT
        anchor = tg.anchor()
        z = tg.zone("example")
        self.add(anchor)
        rows = z[0]
        self.play(FadeIn(rows[0]), run_time=0.8)     # scenario
        self.wait(2.0)
        self.play(FadeIn(rows[1], shift=UP * 0.15), run_time=0.9)   # 40% vs 22%
        self.wait(2.0)
        self.play(FadeIn(rows[2]), run_time=0.7)     # verdict
        self.wait(1.8)
        self.play(FadeIn(rows[3]), run_time=0.7)     # the cost
        self.wait(3.1)


class EQT_Claim(Scene):            # ~8s — zone 5: the contestable judgment
    def construct(self):
        tg = _DEMO_TANGENT
        anchor = tg.anchor()
        z = tg.zone("claim")
        self.add(anchor)
        self.play(FadeIn(z, shift=UP * 0.15), run_time=1.0)
        self.wait(7.0)
