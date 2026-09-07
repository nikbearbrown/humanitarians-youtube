"""
Manim scenes for chapter14-json-fix (3-min Bella recut).

Counts from SOURCE.md. GATE W: never put the word "chapter" on a slide.
GATE B: stroke_opacity=0; counts sit next_to(track, RIGHT).
"""
from manim import *

PALETTE = {
    "bg": "#FAF9F5",
    "ink": "#3D3929",
    "accent": "#D97757",
    "mute": "#8B8878",
}


def _title(text, toy):
    t = Text(text, color=PALETTE["ink"], font_size=28)
    t.to_edge(UP, buff=0.62)
    s = Text(toy, color=PALETTE["mute"], font_size=15)
    s.next_to(t, DOWN, buff=0.10)
    return t, s


class B06_OtherRows(Scene):
    """Why the row problem is not one bad cell — 42 of 46."""

    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title, toy = _title("Not One Broken Row", "sources per flagged assertion")
        self.add(title, toy)

        rows = [("1 source", 4), ("2 sources", 18), ("3 sources", 21), ("4 sources", 3)]
        max_n = 21
        bar_w, bar_h, start_y, spacing, left_x = 7.0, 0.42, 1.35, 0.70, -1.5
        for i, (label, n) in enumerate(rows):
            y = start_y - i * spacing
            w = max(0.08, bar_w * (n / max_n))
            track = Rectangle(width=bar_w, height=bar_h, fill_color=PALETTE["ink"],
                              fill_opacity=0.08, stroke_width=0, stroke_opacity=0)
            track.move_to([left_x + bar_w / 2, y, 0])
            bar = Rectangle(width=w, height=bar_h, fill_color=PALETTE["accent"],
                            fill_opacity=0.95 if n >= 18 else 0.55,
                            stroke_width=0, stroke_opacity=0)
            bar.align_to(track, LEFT).align_to(track, UP)
            row = Text(label, color=PALETTE["ink"], font_size=18).next_to(track, LEFT, buff=0.18)
            count = Text(str(n), color=PALETTE["ink"], font_size=18).next_to(track, RIGHT, buff=0.16)
            self.add(track, row)
            self.play(FadeIn(bar), FadeIn(count), run_time=0.28)

        foot = Text("42 of 46 flagged assertions needed more than one source.",
                    color=PALETTE["ink"], font_size=20)
        foot.to_edge(DOWN, buff=0.52)
        self.play(Write(foot), run_time=0.4)
        self.wait(10.0)


class B09_OneToMany(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title, toy = _title("One Cell Cannot Hold a List", "the row problem")
        self.add(title, toy)

        box = RoundedRectangle(width=10.6, height=1.35, corner_radius=0.08,
                               fill_color=PALETTE["ink"], fill_opacity=0.07,
                               stroke_width=0, stroke_opacity=0)
        box.move_to(UP * 1.35)
        lab = Text("Sites Visited  ·  one cell", color=PALETTE["mute"], font_size=16)
        lab.next_to(box, UP, buff=0.12)
        flat = Text("pubmed…  +  nature…  +  pubmed…   flattened", color=PALETTE["ink"], font_size=22)
        flat.move_to(box.get_center())
        self.play(FadeIn(box), FadeIn(lab), FadeIn(flat), run_time=0.6)

        arrows = Text("one sentence   →   many independent sources", color=PALETTE["accent"], font_size=24)
        arrows.move_to(ORIGIN)
        self.play(Write(arrows), run_time=0.45)

        cards = VGroup()
        for i, v in enumerate(("CONFIRMED", "CONFIRMED", "OUTDATED")):
            c = RoundedRectangle(width=3.2, height=1.15, corner_radius=0.08,
                                 fill_color=PALETTE["ink"], fill_opacity=0.07,
                                 stroke_width=0, stroke_opacity=0)
            t = Text(f"source {i+1}", color=PALETTE["mute"], font_size=14)
            n = Text(v, color=PALETTE["accent"] if v != "OUTDATED" else PALETTE["ink"], font_size=22)
            inner = VGroup(t, n).arrange(DOWN, buff=0.08)
            inner.move_to(c.get_center())
            cards.add(VGroup(c, inner))
        cards.arrange(RIGHT, buff=0.28).move_to(DOWN * 1.45)
        self.play(FadeIn(cards), run_time=0.7)
        self.wait(10.5)


class B12_WarburgThree(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title, toy = _title("Assertion 21 — Warburg", "one sentence · three sources")
        self.add(title, toy)

        head = Text("TRUE", color=PALETTE["accent"], font_size=52)
        sub = Text("overall verdict sits above the list", color=PALETTE["ink"], font_size=18)
        top = VGroup(head, sub).arrange(DOWN, buff=0.10).move_to(UP * 1.35)
        self.play(FadeIn(top), run_time=0.5)

        for i, (src, verd) in enumerate((
            ("PubMed 21508971", "CONFIRMED"),
            ("Nature nrc3038", "CONFIRMED"),
            ("PubMed 27911732", "CONFIRMED"),
        )):
            plate = RoundedRectangle(width=10.4, height=0.72, corner_radius=0.08,
                                     fill_color=PALETTE["ink"], fill_opacity=0.07,
                                     stroke_width=0, stroke_opacity=0)
            a = Text(src, color=PALETTE["ink"], font_size=20)
            b = Text(verd, color=PALETTE["accent"], font_size=20)
            row = VGroup(a, b).arrange(RIGHT, buff=2.4)
            row.move_to(plate.get_center())
            grp = VGroup(plate, row).move_to(UP * (0.35 - i * 0.88))
            self.play(FadeIn(grp), run_time=0.32)

        foot = Text("The list stays. Nothing is flattened.", color=PALETTE["ink"], font_size=18)
        foot.to_edge(DOWN, buff=0.72)
        self.play(Write(foot), run_time=0.4)
        self.wait(10.5)
