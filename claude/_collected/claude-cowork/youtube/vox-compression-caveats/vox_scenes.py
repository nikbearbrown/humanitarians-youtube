import sys, pathlib, os, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {}
try:
    _data = json.load(open(os.path.join(os.path.dirname(__file__), "beat_sheet.json")))
    DUR = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0)
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}


class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        t1 = Text("Why Summarizing Deletes", font=SERIF, color=INK, font_size=36, weight=BOLD)
        t2 = Text("Exactly the Caveats", font=SERIF, color=INK, font_size=36, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.15).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(block, shift=UP * 0.1), Create(u), run_time=1.1)
        self.wait(max(0.5, total - 1.6))


class B03_TheQuestion(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Summarizing should shrink a document roughly evenly. "
            "Instead it kept every confident claim and dropped every caveat. "
            "Why that selection?",
            "— the question this film answers",
            None,
            "Why?",
            DUR["B03"],
        )


class B04_SourceStack(Scene):
    def construct(self):
        total = DUR["B04"]
        pairs = VGroup()
        for i in range(6):
            claim = Rectangle(width=4.8, height=0.45, color=TEAL, fill_opacity=0.18)
            claim.set_stroke(color=TEAL, width=2, opacity=1)
            caveat = Rectangle(width=4.8, height=0.22, color=CRIMSON, fill_opacity=0.18)
            caveat.set_stroke(color=CRIMSON, width=1.5, opacity=1)
            pair = VGroup(claim, caveat).arrange(DOWN, buff=0.04)
            pairs.add(pair)
        pairs.arrange(DOWN, buff=0.10).move_to(LEFT * 0.3)

        claim_lbl = Text("claim", font=MONO, color=TEAL, font_size=16)
        claim_lbl.next_to(pairs[0].submobjects[0], RIGHT, buff=0.3)
        caveat_lbl = Text("caveat", font=MONO, color=CRIMSON, font_size=16)
        caveat_lbl.next_to(pairs[0].submobjects[1], RIGHT, buff=0.3)

        header = Text("12-PAGE REPORT", font=DISPLAY, color=SLATE, font_size=18)
        header.next_to(pairs, UP, buff=0.35)

        self.play(FadeIn(header), run_time=0.3)
        self.play(FadeIn(pairs, shift=UP * 0.05), run_time=0.8)
        self.play(FadeIn(claim_lbl), FadeIn(caveat_lbl), run_time=0.4)
        self.wait(max(0.3, total - 1.5))


class B05_CollapseBar(Scene):
    def construct(self):
        total = DUR["B05"]

        # Phase 1: source stack — claims + caveats
        source_pairs = VGroup()
        caveat_rects = VGroup()
        for i in range(6):
            claim = Rectangle(width=4.4, height=0.40, color=TEAL, fill_opacity=0.18)
            claim.set_stroke(color=TEAL, width=2, opacity=1)
            caveat = Rectangle(width=4.4, height=0.20, color=CRIMSON, fill_opacity=0.18)
            caveat.set_stroke(color=CRIMSON, width=1.5, opacity=1)
            pair = VGroup(claim, caveat).arrange(DOWN, buff=0.04)
            source_pairs.add(pair)
            caveat_rects.add(caveat)
        source_pairs.arrange(DOWN, buff=0.08).move_to(ORIGIN)

        src_lbl = Text("SOURCE", font=DISPLAY, color=SLATE, font_size=18)
        src_lbl.next_to(source_pairs, UP, buff=0.35)

        # Phase 2: summary stack — claims only, same width
        summary_claims = VGroup()
        for i in range(6):
            c = Rectangle(width=4.4, height=0.40, color=TEAL, fill_opacity=0.18)
            c.set_stroke(color=TEAL, width=2, opacity=1)
            summary_claims.add(c)
        summary_claims.arrange(DOWN, buff=0.22).move_to(ORIGIN)

        sum_lbl = Text("SUMMARY", font=DISPLAY, color=TEAL, font_size=18)
        sum_lbl.next_to(summary_claims, UP, buff=0.35)

        gone_lbl = Text("caveats: gone", font=MONO, color=CRIMSON, font_size=20)
        gone_lbl.move_to(DOWN * 2.6)

        self.play(FadeIn(src_lbl), FadeIn(source_pairs), run_time=0.6)
        self.wait(0.3)
        self.play(FadeOut(caveat_rects), FadeOut(src_lbl), run_time=0.7)
        self.play(FadeIn(sum_lbl), run_time=0.4)
        self.play(FadeIn(gone_lbl, shift=UP * 0.05), run_time=0.4)
        self.wait(max(0.3, total - 2.4))


class B06_SectionMechanism(Scene):
    def construct(self):
        total = DUR["B06"]
        heading = Text("THE MECHANISM", font=DISPLAY, color=INK, font_size=48, weight=BOLD)
        sub = Text("compression is not neutral", font=SERIF, color=SLATE, font_size=28, slant=ITALIC)
        block = VGroup(heading, sub).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(heading, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.3, total - 0.9))


class B07_SelectionBias(Scene):
    def construct(self):
        total = DUR["B07"]

        # KEPT column (TEAL)
        kept_header = Text("KEPT", font=DISPLAY, color=TEAL, font_size=28, weight=BOLD)
        kept_items = VGroup(
            Text("confident claims", font=SERIF, color=TEAL, font_size=21),
            Text("clear results", font=SERIF, color=TEAL, font_size=21),
            Text("central findings", font=SERIF, color=TEAL, font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        kept_col = VGroup(kept_header, kept_items).arrange(DOWN, buff=0.28)
        kept_border = Rectangle(width=3.0, height=2.6, color=TEAL, fill_opacity=0.06)
        kept_border.set_stroke(color=TEAL, width=2, opacity=1)
        kept_border.move_to(LEFT * 3.0)
        kept_col.move_to(LEFT * 3.0)

        # DROPPED column (CRIMSON)
        drop_header = Text("DROPPED", font=DISPLAY, color=CRIMSON, font_size=28, weight=BOLD)
        drop_items = VGroup(
            Text("caveats", font=SERIF, color=CRIMSON, font_size=21),
            Text("uncertainty", font=SERIF, color=CRIMSON, font_size=21),
            Text("minority findings", font=SERIF, color=CRIMSON, font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        drop_col = VGroup(drop_header, drop_items).arrange(DOWN, buff=0.28)
        drop_border = Rectangle(width=3.0, height=2.6, color=CRIMSON, fill_opacity=0.06)
        drop_border.set_stroke(color=CRIMSON, width=2, opacity=1)
        drop_border.move_to(RIGHT * 3.0)
        drop_col.move_to(RIGHT * 3.0)

        compress_lbl = Text("compression", font=MONO, color=SLATE, font_size=18)
        compress_lbl.move_to(ORIGIN + UP * 1.0)
        arrow = Arrow(ORIGIN + UP * 0.6, LEFT * 1.8 + UP * 0.6, buff=0,
                      color=TEAL, stroke_width=2)

        self.play(FadeIn(kept_border), FadeIn(kept_col), run_time=0.5)
        self.play(FadeIn(drop_border), FadeIn(drop_col), run_time=0.5)
        self.play(FadeIn(compress_lbl), Create(arrow), run_time=0.6)
        self.wait(max(0.3, total - 1.6))


class B08_MechanismQuote(Scene):
    def construct(self):
        _quote_scene(
            self,
            "What gets cut is not random. It tends to be caveats, uncertainty, "
            "and minority findings. Compression makes confident prose from materials "
            "that were never that certain.",
            "— the mechanism",
            None,
            "not random",
            DUR["B08"],
        )


class B09_BeforeAfter(Scene):
    def construct(self):
        total = DUR["B09"]

        src_lbl = Text("SOURCE", font=DISPLAY, color=SLATE, font_size=18)
        src_claim = Rectangle(width=2.8, height=0.45, color=TEAL, fill_opacity=0.18)
        src_claim.set_stroke(color=TEAL, width=2, opacity=1)
        src_caveat = Rectangle(width=2.8, height=0.22, color=CRIMSON, fill_opacity=0.18)
        src_caveat.set_stroke(color=CRIMSON, width=1.5, opacity=1)
        src_pair = VGroup(src_claim, src_caveat).arrange(DOWN, buff=0.06)
        src_group = VGroup(src_lbl, src_pair).arrange(DOWN, buff=0.25)
        src_group.move_to(LEFT * 3.0)

        arrow = Arrow(LEFT * 1.2, RIGHT * 1.2, buff=0, color=SLATE, stroke_width=2)
        arrow.move_to(ORIGIN)

        sum_lbl = Text("SUMMARY", font=DISPLAY, color=TEAL, font_size=18)
        sum_claim = Rectangle(width=2.8, height=0.45, color=TEAL, fill_opacity=0.18)
        sum_claim.set_stroke(color=TEAL, width=2, opacity=1)
        sum_group = VGroup(sum_lbl, sum_claim).arrange(DOWN, buff=0.25)
        sum_group.move_to(RIGHT * 3.0)

        gone_lbl = Text("caveat: gone", font=MONO, color=CRIMSON, font_size=18, slant=ITALIC)
        gone_lbl.move_to(RIGHT * 3.0 + DOWN * 0.7)

        self.play(FadeIn(src_group), run_time=0.5)
        self.play(Create(arrow), run_time=0.4)
        self.play(FadeIn(sum_group), run_time=0.5)
        self.play(FadeIn(gone_lbl, shift=UP * 0.05), run_time=0.4)
        self.wait(max(0.3, total - 1.8))


class B11_Example(Scene):
    def construct(self):
        total = DUR["B11"]

        src_text = Text(
            '"engagement is projected to exceed targets"',
            font=SERIF, color=TEAL, font_size=24
        )
        src_text.move_to(UP * 1.6)

        arrow = Arrow(src_text.get_bottom() + DOWN * 0.08,
                      src_text.get_bottom() + DOWN * 0.75,
                      buff=0, color=SLATE, stroke_width=2)

        sum_text = Text(
            '"engagement exceeded targets"',
            font=SERIF, color=CRIMSON, font_size=24, weight=BOLD
        )
        sum_text.next_to(arrow, DOWN, buff=0.15)

        counter = Text("claims: 6 → 6   ·   caveats: 6 → 0",
                       font=MONO, color=SLATE, font_size=20)
        counter.move_to(DOWN * 2.2)

        illus = Text("illustrative", font=MONO, color=SLATE, font_size=16, slant=ITALIC)
        illus.to_corner(DR, buff=0.35)

        self.play(FadeIn(src_text, shift=DOWN * 0.1), run_time=0.5)
        self.play(Create(arrow), run_time=0.4)
        self.play(FadeIn(sum_text, shift=UP * 0.05), run_time=0.5)
        self.play(FadeIn(counter, shift=UP * 0.05), run_time=0.5)
        self.play(FadeIn(illus), run_time=0.3)
        self.wait(max(0.3, total - 2.2))


class B12_Counter(Scene):
    def construct(self):
        total = DUR["B12"]
        n = 6
        in_claims = VGroup(*[
            Rectangle(width=0.55, height=0.4, color=TEAL, fill_opacity=0.25)
            for _ in range(n)
        ]).arrange(RIGHT, buff=0.08)
        in_claims.set_stroke(color=TEAL, width=1.5, opacity=1)

        in_caveats = VGroup(*[
            Rectangle(width=0.55, height=0.22, color=CRIMSON, fill_opacity=0.25)
            for _ in range(n)
        ]).arrange(RIGHT, buff=0.08)
        in_caveats.set_stroke(color=CRIMSON, width=1.2, opacity=1)

        in_lbl = Text("IN", font=DISPLAY, color=SLATE, font_size=22)
        in_group = VGroup(in_lbl, in_claims, in_caveats).arrange(DOWN, buff=0.18)
        in_group.move_to(LEFT * 3.2)

        arrow = Arrow(LEFT * 1.0, RIGHT * 1.0, buff=0, color=SLATE, stroke_width=2)
        arrow.move_to(ORIGIN)

        out_claims = VGroup(*[
            Rectangle(width=0.55, height=0.4, color=TEAL, fill_opacity=0.25)
            for _ in range(n)
        ]).arrange(RIGHT, buff=0.08)
        out_claims.set_stroke(color=TEAL, width=1.5, opacity=1)

        out_lbl = Text("OUT", font=DISPLAY, color=SLATE, font_size=22)
        out_group = VGroup(out_lbl, out_claims).arrange(DOWN, buff=0.18)
        out_group.move_to(RIGHT * 3.2)

        tally = Text("claims: 6→6  ·  caveats: 6→0", font=MONO, color=CRIMSON, font_size=20)
        tally.move_to(DOWN * 2.4)

        self.play(FadeIn(in_group), run_time=0.5)
        self.play(Create(arrow), run_time=0.3)
        self.play(FadeIn(out_group), run_time=0.5)
        self.play(FadeIn(tally, shift=UP * 0.05), run_time=0.5)
        self.wait(max(0.3, total - 1.8))


class B13_Quote(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Compression preserves the impressive. It does not preserve the accurate.",
            "— the example",
            None,
            "accurate",
            DUR["B13"],
        )


class B14_Endcard(Scene):
    def construct(self):
        total = DUR["B14"]
        copy = Text("The summary kept every claim.\nIt dropped every caveat.",
                    font=SERIF, color=INK, font_size=32, weight=BOLD)
        sub = Text("CLAUDE COWORK", font=DISPLAY, color=TEAL, font_size=22)
        u = Line(copy.get_corner(DL) + DOWN * 0.14, copy.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        u.set_stroke(opacity=1)
        block = VGroup(copy, u).move_to(UP * 0.15)
        sub.next_to(block, DOWN, buff=0.5)
        self.play(FadeIn(copy, shift=UP * 0.1), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.4))
