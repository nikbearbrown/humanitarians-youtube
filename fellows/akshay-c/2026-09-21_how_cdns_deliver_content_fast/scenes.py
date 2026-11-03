# -*- coding: utf-8 -*-
from manim import *

config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 24
config.frame_width = 16
config.frame_height = 9

BG = "#111111"
FG = "#F2EEE8"
ACCENT = "#C46F4B"
MUTED = "#777777"
GOOD = "#78A083"
BAD = "#B65C5C"


class BrutalistScene(Scene):

    def setup(self):
        self.camera.background_color = BG

    def heading(self, text):
        words = text.split()
        lines = []
        current = []

        limit = 48

        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > limit and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)

        if current:
            lines.append(" ".join(current))

        title = VGroup(*[
            Text(
                line,
                font_size=34,
                color=FG,
                weight=BOLD
            )
            for line in lines
        ]).arrange(DOWN, buff=.10)

        title.move_to(UP * 3.55)

        rule = Line(
            LEFT * 6.8,
            RIGHT * 6.8,
            color=ACCENT,
            stroke_width=5
        ).next_to(title, DOWN, buff=.18)

        return VGroup(title, rule)

    def node(self, label, color=FG):
        rect = RoundedRectangle(
            width=4.2,
            height=1.25,
            corner_radius=.08,
            stroke_color=color,
            stroke_width=3
        )

        text = Text(
            label,
            font_size=27,
            color=color,
            weight=BOLD
        )

        text.move_to(rect)

        return VGroup(rect, text)

    def note(self, text, color=FG):
        return Text(
            text,
            font_size=25,
            color=color,
            weight=BOLD
        )

    def flow_scene(
        self,
        title_text,
        nodes,
        notes,
        active_index=1,
        bypass_origin=False
    ):
        title = self.heading(title_text)

        boxes = VGroup(*[
            self.node(
                n,
                ACCENT if i == active_index else FG
            )
            for i, n in enumerate(nodes)
        ])


        boxes.arrange(RIGHT, buff=1.05)
        boxes.move_to(UP * .2)

        self.play(FadeIn(title), run_time=1.0)

        self.play(
            LaggedStart(*[FadeIn(x) for x in boxes], lag_ratio=.18),
            run_time=2.0
        )

        arrows = VGroup()

        for i in range(len(boxes) - 1):
            a = Arrow(
                boxes[i].get_right(),
                boxes[i + 1].get_left(),
                buff=.16,
                color=GOOD if i == 0 else MUTED,
                stroke_width=5
            )
            arrows.add(a)

        self.play(
            LaggedStart(*[Create(x) for x in arrows], lag_ratio=.25),
            run_time=2.2
        )


        if bypass_origin:
            cross = VGroup(
                Line(
                    boxes[-1].get_corner(UL),
                    boxes[-1].get_corner(DR),
                    color=MUTED,
                    stroke_width=5
                ),
                Line(
                    boxes[-1].get_corner(UR),
                    boxes[-1].get_corner(DL),
                    color=MUTED,
                    stroke_width=5
                )
            )

            self.play(Create(cross), run_time=.8)

        notes_group = VGroup(*[
            self.note(
                n,
                GOOD if i == 0 else MUTED
            )
            for i, n in enumerate(notes)
        ]).arrange(DOWN, buff=.18)

        notes_group.move_to(DOWN * 3.35)

        self.play(FadeIn(notes_group), run_time=1.4)
        self.wait(2.5)



class B01_DirectFanoutFails(BrutalistScene):
    def construct(self):
        self.flow_scene(
            "WITHOUT A CDN: EVERY REQUEST TRAVELS TO THE ORIGIN",
            ["USER", "INTERNET", "DISTANT ORIGIN"],
            ["LONG NETWORK PATH", "MORE ROUND-TRIP LATENCY"],
            active_index=2
        )


class B02_DurableLog(BrutalistScene):
    def construct(self):
        self.flow_scene(
            "A CDN PUTS EDGE LOCATIONS CLOSER TO USERS",
            ["USER", "CDN EDGE", "ORIGIN"],
            ["SHORTER DELIVERY PATH", "DISTRIBUTED POINTS OF PRESENCE"],
            active_index=1
        )


class B03_Partitions(BrutalistScene):
    def construct(self):

        title = self.heading(
            "ROUTING SENDS THE REQUEST TO AN APPROPRIATE EDGE"
        )

        self.play(FadeIn(title), run_time=1)

        router = self.node("CDN ROUTING", ACCENT)

        router.move_to(UP * 1.5)

        edges = VGroup(
            self.node("EDGE A"),
            self.node("EDGE B", GOOD),
            self.node("EDGE C")
        ).arrange(RIGHT, buff=.75).move_to(DOWN * .6)

        self.play(FadeIn(router), FadeIn(edges), run_time=2)

        arrows = VGroup(*[
            Arrow(
                router.get_bottom(),
                edge.get_top(),
                buff=.15,
                color=GOOD if i == 1 else MUTED
            )
            for i, edge in enumerate(edges)
        ])


        self.play(
            LaggedStart(*[Create(x) for x in arrows], lag_ratio=.2),
            run_time=2
        )

        chosen = self.note("HEALTHY · LOW-LATENCY EDGE", GOOD)
        chosen.move_to(DOWN * 3.35)

        self.play(FadeIn(chosen), run_time=1.2)
        self.wait(2.5)


class B05_Brokers(BrutalistScene):
    def construct(self):
        self.flow_scene(
            "CACHE HIT: THE EDGE SERVES THE OBJECT",
            ["BROWSER", "EDGE CACHE", "ORIGIN"],
            ["CACHE HIT", "ORIGIN NOT NEEDED"],
            active_index=1,
            bypass_origin=True
        )


class B06_ConsumerGroups(BrutalistScene):
    def construct(self):
        self.flow_scene(
            "CACHE MISS: THE EDGE FETCHES UPSTREAM",
            ["BROWSER", "EDGE CACHE", "ORIGIN"],
            ["CACHE MISS", "FETCH FROM ORIGIN"],
            active_index=1
        )


class B07_Offsets(BrutalistScene):
    def construct(self):
        self.flow_scene(
            "THE ORIGIN RESPONSE POPULATES THE EDGE CACHE",
            ["ORIGIN", "CDN EDGE", "USER"],
            ["STORE COPY", "RETURN RESPONSE"],
            active_index=1
        )


class B09_Rebalance(BrutalistScene):
    def construct(self):
        self.flow_scene(
            "THE NEXT REQUEST CAN BE SERVED FROM THE EDGE",
            ["SECOND USER", "EDGE CACHE", "ORIGIN"],
            ["CACHE HIT", "SHORTER PATH"],
            active_index=1,
            bypass_origin=True
        )


class B10_Replication(BrutalistScene):
    def construct(self):

        title = self.heading(
            "TTL, REVALIDATION, AND PURGE KEEP CACHES FRESH"
        )

        self.play(FadeIn(title), run_time=1)

        states = VGroup(
            self.node("FRESH", GOOD),
            self.node("EXPIRED", BAD),
            self.node("REVALIDATED", ACCENT)
        )

        states.arrange(RIGHT, buff=1).move_to(UP * .2)

        arrows = VGroup(
            Arrow(states[0].get_right(), states[1].get_left(), buff=.15, color=MUTED),
            Arrow(states[1].get_right(), states[2].get_left(), buff=.15, color=ACCENT)
        )

        self.play(
            LaggedStart(*[FadeIn(x) for x in states], lag_ratio=.2),
            run_time=2
        )

        self.play(Create(arrows), run_time=2)

        note = VGroup(
            self.note("TTL DEFINES FRESHNESS", GOOD),
            self.note("PURGE CAN REMOVE CONTENT EARLY", MUTED)
        ).arrange(DOWN, buff=.18)

        note.move_to(DOWN * 3.35)

        self.play(FadeIn(note), run_time=1.5)
        self.wait(2.5)


class B11_FullScale(BrutalistScene):
    def construct(self):

        title = self.heading(
            "POPULAR CONTENT CAN BE DISTRIBUTED ACROSS MANY EDGES"
        )

        self.play(FadeIn(title), run_time=1)

        origin = self.node("ORIGIN", ACCENT)

        origin.move_to(UP * 1.7)

        edges = VGroup(
            self.node("EDGE · AMERICAS"),
            self.node("EDGE · EUROPE"),
            self.node("EDGE · ASIA")
        ).arrange(RIGHT, buff=.55).move_to(DOWN * .6)

        self.play(FadeIn(origin), FadeIn(edges), run_time=2)

        links = VGroup(*[
            Arrow(
                origin.get_bottom(),
                edge.get_top(),
                buff=.12,
                color=MUTED
            )
            for edge in edges
        ])

        self.play(Create(links), run_time=2)

        assets = VGroup(
            self.note("IMAGES · CSS · JAVASCRIPT", GOOD),
            self.note("FONTS · DOWNLOADS · VIDEO SEGMENTS", MUTED)
        ).arrange(DOWN, buff=.18)

        assets.move_to(DOWN * 3.35)

        self.play(FadeIn(assets), run_time=1.5)
        self.wait(2.5)


class B12_Tradeoffs(BrutalistScene):
    def construct(self):

        title = self.heading(
            "CDNS REDUCE LATENCY, BUT THE ORIGIN STILL MATTERS"
        )

        self.play(FadeIn(title), run_time=1)

        cards = VGroup(
            self.node("CACHE MISS", BAD),
            self.node("DYNAMIC CONTENT", ACCENT),
            self.node("STALE CONTENT", BAD),
            self.node("ORIGIN LATENCY", ACCENT)
        )

        cards.arrange_in_grid(rows=2, cols=2, buff=(.7, .55))
        cards.move_to(UP * .1)

        self.play(
            LaggedStart(*[FadeIn(x) for x in cards], lag_ratio=.15),
            run_time=2.5
        )

        note = self.note(
            "EDGE DELIVERY REDUCES REPEATED LONG-DISTANCE WORK",
            GOOD
        )

        note.scale(1)
        note.move_to(DOWN * 3.35)

        self.play(FadeIn(note), run_time=1.5)
        self.wait(3)
