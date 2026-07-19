"""vox_scenes.py — The Sponsorship Tier That Flips: Why the Famous Brand
Is the Wrong Target (vox-sponsor-flip, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B02 is STILL ai — no scene here (compiles as a slate).

Color law:
  TEAL   = Proven / filing history / the unknown biotech (the good target)
  CRIMSON= Avoid / prestige / no filings (the wrong target)
  GOLD   = editor's-pen highlight, fill only, never text, once per graphic
  SLATE  = structural / neutral components

Exclusions honored: NO LCA mechanics, NO USCIS process steps,
NO entity-resolution / name-matching (card 03), NO immigration-law advice,
NO printed formula notation.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys
import json
import os
import pathlib

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- helpers

def _rect(w, h, color, alpha=1.0):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, alpha).set_stroke(width=0, opacity=0)
    return r


def _outlined_rect(w, h, color):
    """Empty rect with colored border only — for absent bar segments."""
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 0.0).set_stroke(color, 2.5)
    return r


# ================================================================ B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("Why the Famous Brand", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Is the Wrong Target", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ================================================================ B03 TheQuestion

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        line1 = Text("Prestige should predict sponsorship.",
                     font=SERIF, color=INK, font_size=28, weight=BOLD)
        line2 = Text("Here is the case where the famous brand scores Avoid",
                     font=SERIF, color=INK, font_size=22)
        line3 = Text("and the unknown one scores Proven.", font=SERIF, color=INK, font_size=22)
        line4 = Text("Why?", font=DISPLAY, color=CRIMSON, font_size=52, weight=BOLD)
        block = VGroup(line1, line2, line3, line4).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        # gold highlight behind "Why?"
        hl = _rect(line4.width + 0.3, line4.height + 0.12, GOLD, 0.55)
        hl.move_to(line4.get_center())
        self.play(FadeIn(line1), run_time=0.7)
        self.play(FadeIn(line2), FadeIn(line3), run_time=0.7)
        self.play(FadeIn(hl), FadeIn(line4, scale=1.05), run_time=0.9)
        self.wait(max(0.3, total - 2.3))


# ================================================================ B04 NameVsRecord

class B04_NameVsRecord(Scene):
    def construct(self):
        total = DUR["B04"]
        # Left: prestige column; Right: filing record column
        # The two signals are independent — no arrow connecting them

        left_label = LabelChip("prestige", accent=CRIMSON, size=24)
        left_label.move_to(LEFT * 3.2 + UP * 2.0)

        right_label = LabelChip("filing record", accent=TEAL, size=24)
        right_label.move_to(RIGHT * 3.2 + UP * 2.0)

        # Left: a single large brand name block (crimson)
        brand_block = _rect(2.6, 0.7, CRIMSON, 0.85)
        brand_block.next_to(left_label, DOWN, buff=0.35)

        # Right: a small stack of filing bars (teal) — three LCA row bars
        bar1 = _rect(2.6, 0.22, TEAL, 0.85)
        bar2 = _rect(2.6, 0.22, TEAL, 0.85)
        bar3 = _rect(2.6, 0.22, TEAL, 0.85)
        bar_stack = VGroup(bar1, bar2, bar3).arrange(DOWN, buff=0.1)
        bar_stack.next_to(right_label, DOWN, buff=0.35)

        # X mark showing no reliable connection — drawn as two crossing lines
        xc = ORIGIN + UP * 0.3
        x1 = Line(xc + LEFT * 0.25 + UP * 0.25, xc + RIGHT * 0.25 + DOWN * 0.25,
                  color=CRIMSON, stroke_width=5)
        x2 = Line(xc + LEFT * 0.25 + DOWN * 0.25, xc + RIGHT * 0.25 + UP * 0.25,
                  color=CRIMSON, stroke_width=5)
        x_mark = VGroup(x1, x2)

        # Serif annotation below
        note = SerifLabel("independent signals", SLATE, size=22)
        note.move_to(ORIGIN + DOWN * 2.2)

        self.play(FadeIn(left_label), FadeIn(right_label), run_time=0.7)
        self.play(FadeIn(brand_block), LaggedStart(*[FadeIn(b) for b in bar_stack],
                                                    lag_ratio=0.2, run_time=0.9))
        self.play(Create(x1), Create(x2), run_time=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.0))


# ================================================================ B05 RevealedBehavior

class B05_RevealedBehavior(Scene):
    def construct(self):
        total = DUR["B05"]
        card_w, card_h = 3.4, 2.2

        # Left: TEAL "FILING RECORD — revealed behavior"
        teal_box = _rect(card_w, card_h, TEAL, 0.12)
        teal_box.set_stroke(TEAL, 2.5)
        teal_box.move_to(LEFT * 3.0)
        teal_label = LabelChip("filing record", accent=TEAL, size=22)
        teal_label.move_to(LEFT * 3.0 + UP * 0.45)
        teal_sub = SerifLabel("revealed behavior", TEAL, size=22)
        teal_sub.move_to(LEFT * 3.0 + DOWN * 0.45)
        teal_card = VGroup(teal_box, teal_label, teal_sub)

        # Right: CRIMSON "REPUTATION — not a decision"
        crim_box = _rect(card_w, card_h, CRIMSON, 0.08)
        crim_box.set_stroke(CRIMSON, 2.0)
        crim_box.move_to(RIGHT * 3.0)
        crim_label = LabelChip("reputation", accent=CRIMSON, size=22)
        crim_label.move_to(RIGHT * 3.0 + UP * 0.45)
        crim_sub = SerifLabel("not a decision", CRIMSON, size=22)
        crim_sub.move_to(RIGHT * 3.0 + DOWN * 0.45)
        crim_card = VGroup(crim_box, crim_label, crim_sub)

        self.play(FadeIn(crim_card), run_time=0.8)
        self.play(FadeIn(teal_card), run_time=0.8)
        # teal card grows to show dominance
        self.play(teal_box.animate.scale(1.1), run_time=0.7)
        self.wait(max(0.3, total - 2.3))


# ================================================================ B06 Weights

class B06_Weights(Scene):
    def construct(self):
        total = DUR["B06"]
        # Horizontal composite bar — four segments build left to right
        total_w = 10.4
        bar_h = 0.8

        seg_names   = ["LCA filing rate", "approval rate", "funding recency", "company size"]
        seg_weights = [0.40, 0.30, 0.20, 0.10]
        seg_colors  = [TEAL, TEAL, SLATE, SLATE]

        header = SerifLabel("composite sponsorship score", TEAL, size=26)
        header.move_to(UP * 1.9)
        self.play(FadeIn(header, shift=DOWN * 0.15), run_time=0.6)

        x = -total_w / 2
        for name, weight, color in zip(seg_names, seg_weights, seg_colors):
            w = total_w * weight
            seg = _rect(w, bar_h, color, 0.85)
            seg.move_to(RIGHT * (x + w / 2) + UP * 0.6)
            pct = Text(f"{int(weight * 100)}%", font=MONO, color=INK, font_size=28)
            pct.move_to(seg.get_center())
            lbl = Text(name, font=SERIF, color=INK, font_size=18)
            lbl.next_to(seg, DOWN, buff=0.2)
            self.play(FadeIn(seg, shift=RIGHT * 0.2), FadeIn(pct), FadeIn(lbl),
                      run_time=0.8)
            x += w
        self.wait(max(0.3, total - 4.0))


# ================================================================ B07 LcaDominant

class B07_LcaDominant(Scene):
    def construct(self):
        total = DUR["B07"]
        # Rebuild the bar from B06 then highlight the LCA segment
        total_w = 10.4
        segs_data = [
            ("LCA filing rate", 0.40, TEAL),
            ("approval rate", 0.30, TEAL),
            ("funding recency", 0.20, SLATE),
            ("company size", 0.10, SLATE),
        ]
        bar_h = 0.8
        seg_mobs = []
        x = -total_w / 2
        for label, weight, color in segs_data:
            w = total_w * weight
            seg = _rect(w, bar_h, color, 0.85)
            seg.move_to(RIGHT * (x + w / 2) + UP * 0.6)
            pct = Text(f"{int(weight*100)}%", font=MONO, color=INK, font_size=28)
            pct.move_to(seg.get_center())
            lbl = Text(label, font=SERIF, color=INK, font_size=18)
            lbl.next_to(seg, DOWN, buff=0.2)
            seg_mobs.append((seg, pct, lbl, weight, color))
            x += w

        header = SerifLabel("composite sponsorship score", TEAL, size=26)
        header.move_to(UP * 1.9)

        # Add all at once (pre-built state from B06)
        all_mobs = VGroup(header)
        for seg, pct, lbl, _, _ in seg_mobs:
            all_mobs.add(seg, pct, lbl)
        self.add(all_mobs)

        # Fade non-LCA segments to emphasize the first one
        lca_seg, lca_pct, lca_lbl, _, _ = seg_mobs[0]
        non_lca = VGroup(*[m for i, (s, p, l, _, _) in enumerate(seg_mobs)
                            for m in [s, p, l] if i != 0])
        self.play(non_lca.animate.set_opacity(0.3), run_time=0.7)

        # Dominant signal bracket below LCA segment
        bracket_line = Line(
            lca_seg.get_corner(DL) + DOWN * 0.45,
            lca_seg.get_corner(DR) + DOWN * 0.45,
            color=TEAL, stroke_width=3
        )
        tick_l = Line(lca_seg.get_corner(DL) + DOWN * 0.35,
                      lca_seg.get_corner(DL) + DOWN * 0.55,
                      color=TEAL, stroke_width=3)
        tick_r = Line(lca_seg.get_corner(DR) + DOWN * 0.35,
                      lca_seg.get_corner(DR) + DOWN * 0.55,
                      color=TEAL, stroke_width=3)
        dom_label = SerifLabel("dominant signal", TEAL, size=24)
        dom_label.next_to(bracket_line, DOWN, buff=0.18)

        self.play(Create(bracket_line), Create(tick_l), Create(tick_r), run_time=0.7)
        self.play(FadeIn(dom_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 1.9))


# ================================================================ B08 BiotechBar

class B08_BiotechBar(Scene):
    def construct(self):
        total = DUR["B08"]
        # Stacked vertical bar for HelixBio building from bottom
        bar_w = 2.2
        bar_x = LEFT * 1.5
        segs_data = [
            ("LCA rate", 0.40 * 0.85, TEAL),   # 85% of weight = high contribution
            ("approval rate", 0.30 * 0.85, TEAL),
            ("recency", 0.20 * 0.95, TEAL),
            ("size", 0.10 * 0.65, SLATE),
        ]
        seg_heights = [3.8 * w for _, w, _ in segs_data]
        baseline_y = -2.5

        header = SerifLabel("HelixBio", TEAL, size=28)
        header.move_to(bar_x + UP * 3.3)

        title = SerifLabel("composite score builds from all four segments", INK, size=20)
        title.move_to(UP * 3.2)

        self.play(FadeIn(title, shift=DOWN * 0.1), FadeIn(header), run_time=0.6)

        cumulative_y = baseline_y
        seg_mob_list = []
        for (lbl_txt, _, color), h in zip(segs_data, seg_heights):
            seg = _rect(bar_w, h, color, 0.85)
            seg.move_to(bar_x + UP * (cumulative_y + h / 2))
            seg_label = Text(lbl_txt, font=SERIF, color=INK, font_size=16)
            seg_label.move_to(seg.get_center())
            self.play(FadeIn(seg, shift=UP * 0.15), FadeIn(seg_label), run_time=0.8)
            cumulative_y += h
            seg_mob_list.append((seg, seg_label))

        # PROVEN chip at the top
        proven_chip = LabelChip("proven", accent=TEAL, size=26)
        proven_chip.move_to(bar_x + UP * (cumulative_y + 0.4))
        self.play(FadeIn(proven_chip, shift=DOWN * 0.15), run_time=0.7)
        self.wait(max(0.3, total - 5.5))


# ================================================================ B09 BrandBar

class B09_BrandBar(Scene):
    def construct(self):
        total = DUR["B09"]
        # Two bars side by side: HelixBio (complete, teal) vs SponsorCo (empty 70%)
        bar_w = 2.0
        helix_x = LEFT * 3.0
        brand_x = RIGHT * 1.2
        baseline_y = -2.5

        # HelixBio bar (pre-built, full height)
        helix_segs_data = [
            (0.40 * 0.85, TEAL),
            (0.30 * 0.85, TEAL),
            (0.20 * 0.95, TEAL),
            (0.10 * 0.65, SLATE),
        ]
        helix_cumulative_y = baseline_y
        helix_bar = VGroup()
        for (w, color) in helix_segs_data:
            h = 3.8 * w
            seg = _rect(bar_w, h, color, 0.85)
            seg.move_to(helix_x + UP * (helix_cumulative_y + h / 2))
            helix_bar.add(seg)
            helix_cumulative_y += h

        helix_chip = LabelChip("proven", accent=TEAL, size=22)
        helix_chip.move_to(helix_x + UP * (helix_cumulative_y + 0.35))
        helix_label = SerifLabel("HelixBio", TEAL, size=22)
        helix_label.move_to(helix_x + DOWN * 3.1)

        self.add(helix_bar, helix_chip, helix_label)

        # SponsorCo bar: LCA and approval segments are EMPTY outlines
        # only funding + size fill (SLATE), very short bar
        brand_segs = [
            # (height_fraction_of_total, color, filled)
            (0.40 * 0.02, CRIMSON, False),   # LCA: nearly zero
            (0.30 * 0.02, CRIMSON, False),   # approval: nearly zero
            (0.20 * 0.80, SLATE, True),      # recency: ok
            (0.10 * 0.60, SLATE, True),      # size: neutral
        ]
        brand_cumulative_y = baseline_y
        brand_bar_mobs = []
        for (frac, color, filled) in brand_segs:
            h = max(0.18, 3.8 * frac)
            if filled:
                seg = _rect(bar_w, h, color, 0.75)
            else:
                seg = _outlined_rect(bar_w, h, color)
            seg.move_to(brand_x + UP * (brand_cumulative_y + h / 2))
            brand_bar_mobs.append(seg)
            brand_cumulative_y += h

        avoid_chip = LabelChip("avoid", accent=CRIMSON, size=22)
        avoid_chip.move_to(brand_x + UP * (brand_cumulative_y + 0.35))
        brand_label = SerifLabel("SponsorCo", CRIMSON, size=22)
        brand_label.move_to(brand_x + DOWN * 3.1)

        # Annotation: 70% empty
        empty_note = SerifLabel("70% of score: empty", CRIMSON, size=20)
        empty_note.move_to(brand_x + RIGHT * 1.9 + UP * 0.3)

        title_note = SerifLabel("the ranking flip", INK, size=22)
        title_note.move_to(UP * 3.2)

        self.play(FadeIn(title_note), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(s, shift=UP * 0.12) for s in brand_bar_mobs],
                        lag_ratio=0.2, run_time=1.2),
            run_time=1.2
        )
        self.play(FadeIn(brand_label), FadeIn(avoid_chip, shift=DOWN * 0.1), run_time=0.7)
        self.play(FadeIn(empty_note, shift=LEFT * 0.1), run_time=0.6)
        self.wait(max(0.3, total - 3.0))


# ================================================================ B10 Spectrum

class B10_Spectrum(Scene):
    def construct(self):
        total = DUR["B10"]
        # Horizontal spectrum from AVOID to PROVEN
        spec_y = 0.5
        avoid_x = -5.5
        unknown_x = -1.8
        likely_x = 1.8
        proven_x = 5.5

        # Arrow spine
        spine = Arrow(
            LEFT * 5.8 + UP * spec_y, RIGHT * 5.8 + UP * spec_y,
            color=INK, stroke_width=3, tip_length=0.22
        )

        # Tier chips on the spectrum
        avoid_chip = LabelChip("avoid", accent=CRIMSON, size=22)
        avoid_chip.move_to(RIGHT * avoid_x + UP * spec_y)
        unknown_chip = LabelChip("unknown", accent=SLATE, size=22)
        unknown_chip.move_to(RIGHT * unknown_x + UP * spec_y)
        likely_chip = LabelChip("likely", accent=SLATE, size=22)
        likely_chip.move_to(RIGHT * likely_x + UP * spec_y)
        proven_chip = LabelChip("proven", accent=TEAL, size=22)
        proven_chip.move_to(RIGHT * proven_x + UP * spec_y)

        # Action cues below each tier
        def _cue(txt, x):
            t = Text(txt, font=SERIF, color=INK, font_size=18, slant=ITALIC)
            t.move_to(RIGHT * x + UP * (spec_y - 0.9))
            return t

        cue_avoid   = _cue("skip", avoid_x)
        cue_unknown = _cue("investigate", unknown_x)
        cue_likely  = _cue("target", likely_x)
        cue_proven  = _cue("apply", proven_x)

        # Company chips dropping to their positions
        helix_drop = LabelChip("HelixBio", accent=TEAL, size=20)
        helix_drop.move_to(RIGHT * proven_x + UP * 2.4)
        sponsor_drop = LabelChip("SponsorCo", accent=CRIMSON, size=20)
        sponsor_drop.move_to(RIGHT * avoid_x + UP * 2.4)

        self.play(Create(spine), run_time=0.7)
        self.play(
            LaggedStart(
                FadeIn(avoid_chip), FadeIn(unknown_chip),
                FadeIn(likely_chip), FadeIn(proven_chip),
                lag_ratio=0.25, run_time=1.2
            )
        )
        self.play(
            FadeIn(cue_avoid), FadeIn(cue_unknown),
            FadeIn(cue_likely), FadeIn(cue_proven),
            run_time=0.7
        )
        self.play(FadeIn(helix_drop), FadeIn(sponsor_drop), run_time=0.5)
        self.play(
            helix_drop.animate.move_to(RIGHT * proven_x + UP * (spec_y + 0.65)),
            sponsor_drop.animate.move_to(RIGHT * avoid_x + UP * (spec_y + 0.65)),
            run_time=1.0
        )
        self.wait(max(0.3, total - 4.1))


# ================================================================ B11 MarcusExample

class B11_MarcusExample(Scene):
    def construct(self):
        total = DUR["B11"]
        card_w, card_h = 3.6, 3.8
        lx = LEFT * 3.0
        rx = RIGHT * 3.0

        # SponsorCo card (CRIMSON)
        sc_box = _rect(card_w, card_h, CRIMSON, 0.07)
        sc_box.set_stroke(CRIMSON, 2.5)
        sc_box.move_to(lx)
        sc_name = LabelChip("SponsorCo", accent=CRIMSON, size=22)
        sc_name.move_to(lx + UP * 1.4)
        sc_score = Text("0.05", font=MONO, color=CRIMSON, font_size=52, weight=BOLD)
        sc_score.move_to(lx + UP * 0.2)
        sc_action = LabelChip("skip", accent=CRIMSON, size=26)
        sc_action.move_to(lx + DOWN * 1.1)
        sc_note = Text("0 LCAs  |  0 approvals", font=SERIF, color=INK, font_size=17)
        sc_note.move_to(lx + DOWN * 1.75)
        sponsor_card = VGroup(sc_box, sc_name, sc_score, sc_action, sc_note)

        # HelixBio card (TEAL)
        hx_box = _rect(card_w, card_h, TEAL, 0.07)
        hx_box.set_stroke(TEAL, 2.5)
        hx_box.move_to(rx)
        hx_name = LabelChip("HelixBio", accent=TEAL, size=22)
        hx_name.move_to(rx + UP * 1.4)
        hx_score = Text("0.87", font=MONO, color=TEAL, font_size=52, weight=BOLD)
        hx_score.move_to(rx + UP * 0.2)
        hx_action = LabelChip("apply", accent=TEAL, size=26)
        hx_action.move_to(rx + DOWN * 1.1)
        hx_note = Text("12 LCAs  |  83% approval", font=SERIF, color=INK, font_size=17)
        hx_note.move_to(rx + DOWN * 1.75)
        helix_card = VGroup(hx_box, hx_name, hx_score, hx_action, hx_note)

        # Bottom annotation
        bottom = SerifLabel("Marcus ranked them opposite. The data did not.", INK, size=22)
        bottom.move_to(DOWN * 2.7)

        # Note: illustrative numbers — below the annotation
        illus = Text("(illustrative numbers)", font=SERIF, color=SLATE,
                     font_size=15, slant=ITALIC)
        illus.next_to(bottom, DOWN, buff=0.18)

        self.play(FadeIn(sponsor_card), run_time=0.9)
        self.play(FadeIn(helix_card), run_time=0.9)
        self.play(FadeIn(bottom, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(illus), run_time=0.4)
        self.wait(max(0.3, total - 2.9))


# ================================================================ B12 Endcard

class B12_Endcard(Scene):
    def construct(self):
        total = DUR["B12"]
        topic = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        line1 = Text("The record always", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        line2 = Text("outranks the reputation.", font=DISPLAY, color=TEAL,
                     font_size=36, weight=BOLD)
        block = VGroup(line1, line2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(line2.get_corner(DL) + DOWN * 0.13, line2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        topic.next_to(block, UP, buff=0.55)
        self.play(FadeIn(topic), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.1)
        self.wait(max(0.3, total - 1.6))
