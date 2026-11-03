# -*- coding: utf-8 -*-
from manim import *

config.pixel_width = 2160
config.pixel_height = 3840
config.frame_rate = 24
config.frame_width = 9
config.frame_height = 16

BG = "#111111"; FG = "#F2EEE8"; ACCENT = "#C46F4B"; MUTED = "#777777"; GOOD = "#78A083"; BAD = "#B65C5C"

class BrutalistScene(Scene):
    def setup(self): self.camera.background_color = BG
    def title(self, text):
        words=text.split(); lines=[]; current=[]
        for word in words:
            candidate=" ".join(current+[word])
            if len(candidate)>20 and current:
                lines.append(" ".join(current)); current=[word]
            else:
                current.append(word)
        if current: lines.append(" ".join(current))
        g=VGroup(*[Text(line,font_size=31,color=FG,weight=BOLD) for line in lines]).arrange(DOWN,buff=.10)
        for line in g:
            if line.width>7.2: line.scale_to_fit_width(7.2)
        g.move_to(UP*6.25); self.add(g); return g
    def box(self,label,w=3.0,h=.9,color=FG,fs=25):
        r=Rectangle(width=w,height=h,stroke_color=color,stroke_width=3)
        tx=Text(label,font_size=fs,color=color).move_to(r)
        if tx.width>w-.35: tx.scale_to_fit_width(w-.35)
        return VGroup(r,tx)
    def event(self,label,color=ACCENT):
        c=RoundedRectangle(width=.72,height=.46,corner_radius=.08,stroke_color=color,fill_color=color,fill_opacity=.16)
        return VGroup(c,Text(label,font_size=18,color=FG).move_to(c))

class B01_DirectFanoutFails(BrutalistScene):
    def construct(self):
        self.title("WITHOUT REDIS: THE DATA PATH BECOMES THE BOTTLENECK")

        api = self.box("API", 4.4, 1.0, ACCENT).shift(UP * 3.7)

        names = [
            "SESSIONS",
            "PROFILES",
            "PRODUCTS",
            "COUNTERS",
            "RATE LIMITS"
        ]

        svcs = VGroup(
            *[self.box(n, 4.2, .78) for n in names]
        ).arrange(DOWN, buff=.34).shift(DOWN * 1.15)

        self.play(FadeIn(api), FadeIn(svcs), run_time=4)

        # Clean left-side routing trunk.
        lane_x = svcs.get_left()[0] - .65
        trunk_top = [lane_x, api.get_center()[1], 0]
        trunk_bottom = [lane_x, svcs[-1].get_center()[1], 0]

        trunk = VGroup(
            Line(api.get_left(), trunk_top, color=MUTED, stroke_width=3),
            Line(trunk_top, trunk_bottom, color=MUTED, stroke_width=3)
        )

        branches = VGroup(*[
            Arrow(
                [lane_x, svc.get_center()[1], 0],
                svc.get_left(),
                buff=.10,
                stroke_width=3,
                color=MUTED
            )
            for svc in svcs
        ])

        self.play(Create(trunk), run_time=2)
        self.play(
            LaggedStart(*[Create(x) for x in branches], lag_ratio=.12),
            run_time=2
        )

        overloaded = svcs[2]
        slow = Text(
            "SLOW\nBACKING STORE",
            font_size=20,
            color=BAD,
            line_spacing=.9
        ).next_to(overloaded, RIGHT, buff=.18)

        self.play(
            overloaded[0].animate.set_stroke(BAD),
            FadeIn(slow),
            run_time=3
        )

        q = VGroup(
            *[self.event(str(i)) for i in range(8)]
        ).arrange_in_grid(
            rows=2,
            cols=4,
            buff=(.12, .12)
        ).move_to(UP * 2.15)

        self.play(
            LaggedStart(*[FadeIn(x) for x in q], lag_ratio=.08),
            run_time=4
        )

        warn = VGroup(
            Text("LATENCY UP", font_size=29, color=BAD),
            Text("DATABASE LOAD UP", font_size=29, color=BAD),
            Text("QUEUES UP", font_size=29, color=BAD)
        ).arrange(DOWN, buff=.16).to_edge(DOWN, buff=.75)

        self.play(FadeIn(warn), run_time=2)
        self.wait(3)


class B02_DurableLog(BrutalistScene):
    def construct(self):
        self.title("REDIS PUTS HOT DATA ON THE FAST PATH")

        prod = self.box(
            "APPLICATION", 4.3, .9, ACCENT
        ).shift(UP * 4.0)

        log = Rectangle(
            width=6.8,
            height=3.0,
            stroke_color=FG,
            stroke_width=3
        ).shift(UP * .65)

        topic = Text(
            "REDIS / MEMORY",
            font_size=28,
            color=FG,
            weight=BOLD
        ).next_to(log, UP, buff=.22)

        retain = Text(
            "frequently accessed data",
            font_size=23,
            color=MUTED
        ).next_to(log, DOWN, buff=.18)

        row1 = VGroup(
            *[self.event(str(i)) for i in range(6)]
        ).arrange(RIGHT, buff=.18)

        row2 = VGroup(
            *[self.event(str(i)) for i in range(6, 12)]
        ).arrange(RIGHT, buff=.18)

        cells = VGroup(
            row1, row2
        ).arrange(DOWN, buff=.34).move_to(log)

        cons = VGroup(
            self.box("CACHE HIT", 4.2, .78, GOOD),
            self.box("BACKING DB", 4.2, .78, BAD)
        ).arrange(DOWN, buff=.45).shift(DOWN * 4.0)

        self.play(
            FadeIn(prod),
            FadeIn(log),
            FadeIn(topic),
            FadeIn(retain),
            FadeIn(cons),
            run_time=4
        )

        self.play(
            LaggedStart(
                *[FadeIn(c) for c in row1],
                *[FadeIn(c) for c in row2],
                lag_ratio=.06
            ),
            run_time=5
        )

        self.play(
            Create(
                Arrow(
                    prod.get_bottom(),
                    log.get_top(),
                    buff=.2,
                    color=MUTED
                )
            ),
            run_time=4
        )

        fast_arrow = Arrow(
            log.get_bottom(),
            cons[0].get_top(),
            buff=.18,
            color=GOOD
        )

        # Keep the slower backing-store path in the clean right-side lane.
        lane_x = cons.get_right()[0] + .65
        start_slow = log.get_right()
        end_slow = cons[1].get_right()

        slow_route = VGroup(
            Line(
                start_slow,
                [lane_x, start_slow[1], 0],
                color=BAD,
                stroke_width=3
            ),
            Line(
                [lane_x, start_slow[1], 0],
                [lane_x, end_slow[1], 0],
                color=BAD,
                stroke_width=3
            ),
            Arrow(
                [lane_x, end_slow[1], 0],
                end_slow,
                buff=.12,
                color=BAD,
                stroke_width=3
            )
        )

        self.play(
            Create(fast_arrow),
            Create(slow_route),
            run_time=2
        )

        self.wait(4.5)


class B03_Partitions(BrutalistScene):
    def construct(self):
        self.title("EVENT-DRIVEN NETWORKING HANDLES MANY CLIENT CONNECTIONS")

        lanes = VGroup(
            *[
                Rectangle(
                    width=6.6,
                    height=1.0,
                    stroke_color=FG,
                    stroke_width=2
                )
                for _ in range(6)
            ]
        ).arrange(DOWN, buff=.30).shift(DOWN * .35)

        labels = VGroup(
            *[
                Text(
                    f"C{i + 1}",
                    font_size=25,
                    color=ACCENT
                ).next_to(lanes[i], LEFT, buff=.18)
                for i in range(6)
            ]
        )

        self.play(FadeIn(lanes), FadeIn(labels), run_time=3)

        commands = [
            "GET", "SET", "INCR", "GET",
            "SET", "GET", "INCR", "GET"
        ]

        dest = [0, 1, 2, 0, 1, 4, 0, 2]

        events = VGroup(
            *[self.event(cmd) for cmd in commands]
        ).arrange_in_grid(
            rows=2,
            cols=4,
            buff=(.18, .18)
        ).shift(UP * 4.25)

        self.play(FadeIn(events), run_time=3)

        counts = {}
        targets = []

        for d in dest:
            idx = counts.get(d, 0)
            counts[d] = idx + 1
            targets.append(
                lanes[d].get_left() + RIGHT * (1.0 + 1.05 * idx)
            )

        self.play(
            *[
                events[i].animate.move_to(targets[i])
                for i in range(len(events))
            ],
            run_time=6
        )

        note = VGroup(
            Text(
                "MANY CONNECTIONS STAY OPEN",
                font_size=27,
                color=FG,
                weight=BOLD
            ),
            Text(
                "Redis reacts when sockets",
                font_size=25,
                color=ACCENT
            ),
            Text(
                "have work ready",
                font_size=24,
                color=FG
            )
        ).arrange(DOWN, buff=.14).to_edge(DOWN, buff=.75)

        self.play(FadeIn(note), run_time=3)
        self.wait(4.5)


class B05_Brokers(BrutalistScene):
    def construct(self):
        self.title("REDIS CLUSTER SPREADS THE KEYSPACE ACROSS NODES")

        brokers = VGroup()

        for i in range(3):
            rect = Rectangle(
                width=5.4,
                height=2.45,
                stroke_color=FG,
                stroke_width=3
            )

            label = Text(
                f"REDIS NODE {chr(65 + i)}",
                font_size=27,
                color=FG,
                weight=BOLD
            )

            label.move_to(rect.get_top() + DOWN * .38)
            brokers.add(VGroup(rect, label))

        brokers.arrange(DOWN, buff=.55).shift(DOWN * .25)

        self.play(FadeIn(brokers), run_time=3)

        mapping = [
            ["SLOTS 0-2730", "SLOTS 2731-5460"],
            ["SLOTS 5461-8191", "SLOTS 8192-10922"],
            ["SLOTS 10923-13652", "SLOTS 13653-16383"]
        ]

        for b, ranges in zip(brokers, mapping):
            cards = VGroup(
                *[
                    self.box(r, 2.35, .65, ACCENT, 20)
                    for r in ranges
                ]
            ).arrange(RIGHT, buff=.25)

            cards.move_to(
                b[0].get_center() + DOWN * .48
            )

            self.play(FadeIn(cards), run_time=3)

        foot = VGroup(
            Text(
                "KEYSPACE + REQUEST LOAD",
                font_size=28,
                color=GOOD,
                weight=BOLD
            ),
            Text(
                "spread across cluster nodes",
                font_size=24,
                color=FG
            )
        ).arrange(DOWN, buff=.12).to_edge(DOWN, buff=.75)

        self.play(FadeIn(foot), run_time=3)
        self.wait(4.5)


class B06_ConsumerGroups(BrutalistScene):
    def construct(self):
        self.title("HASH SLOTS ROUTE EACH KEY TO ITS OWNING NODE")

        keys = VGroup(
            self.box("user:42 / 1200", 2.8, .62, ACCENT, 21),
            self.box("cart:18 / 4100", 2.8, .62, ACCENT, 21),
            self.box("item:7 / 6200", 2.8, .62, ACCENT, 21),
            self.box("rate:9 / 8800", 2.8, .62, ACCENT, 21),
            self.box("sess:5 / 12100", 2.8, .62, ACCENT, 21),
            self.box("count:3 / 15000", 2.8, .62, ACCENT, 21)
        ).arrange(DOWN, buff=.22).shift(LEFT * 2.65 + UP * .3)

        nodes = VGroup(
            self.box("NODE A", 1.75, .62, GOOD, 23),
            self.box("NODE A", 1.75, .62, GOOD, 23),
            self.box("NODE B", 1.75, .62, GOOD, 23),
            self.box("NODE B", 1.75, .62, GOOD, 23),
            self.box("NODE C", 1.75, .62, GOOD, 23),
            self.box("NODE C", 1.75, .62, GOOD, 23)
        ).arrange(DOWN, buff=.22).shift(RIGHT * 2.55 + UP * .3)

        self.play(
            FadeIn(keys),
            FadeIn(nodes),
            run_time=4
        )

        lines = VGroup(
            *[
                Line(
                    keys[i].get_right(),
                    nodes[i].get_left(),
                    color=MUTED
                )
                for i in range(6)
            ]
        )

        self.play(Create(lines), run_time=5)

        rule = VGroup(
            Text(
                "KEY",
                font_size=28,
                color=ACCENT,
                weight=BOLD
            ),
            Text(
                "to HASH SLOT",
                font_size=25,
                color=FG
            ),
            Text(
                "to OWNING NODE",
                font_size=23,
                color=MUTED
            )
        ).arrange(DOWN, buff=.13).to_edge(DOWN, buff=.75)

        self.play(FadeIn(rule), run_time=3)
        self.wait(6)


class B07_Offsets(BrutalistScene):
    def construct(self):
        self.title("PIPELINING REDUCES REPEATED NETWORK ROUND TRIPS")

        command_box = Rectangle(
            width=6.7,
            height=5.0,
            stroke_color=FG,
            stroke_width=3
        ).shift(UP * .65)

        command_label = Text(
            "REDIS COMMANDS",
            font_size=28,
            color=FG,
            weight=BOLD
        ).next_to(command_box, UP, buff=.2)

        commands = [
            "GET", "SET", "INCR",
            "GET", "SET", "GET",
            "INCR", "GET", "SET"
        ]

        cells = VGroup(
            *[self.event(cmd) for cmd in commands]
        ).arrange_in_grid(
            rows=3,
            cols=3,
            buff=(.42, .42)
        ).scale(1.28).move_to(command_box)

        self.play(
            Create(command_box),
            FadeIn(command_label),
            FadeIn(cells),
            run_time=4
        )

        marker = Triangle(
            fill_color=ACCENT,
            fill_opacity=1,
            stroke_width=0
        ).scale(.22).rotate(PI).next_to(
            cells[0],
            UP,
            buff=.16
        )

        lab = Text(
            "one command, then wait",
            font_size=29,
            color=ACCENT
        ).move_to(DOWN * 2.25)

        self.play(
            FadeIn(marker),
            FadeIn(lab),
            run_time=3
        )

        slow_box = RoundedRectangle(
            width=5.5,
            height=1.0,
            corner_radius=.08,
            stroke_color=BAD,
            stroke_width=3
        ).shift(DOWN * 3.25)

        slow = Text(
            "REPEATED ROUND TRIPS",
            font_size=27,
            color=BAD,
            weight=BOLD
        ).move_to(slow_box)

        self.play(
            FadeIn(slow_box),
            FadeIn(slow),
            run_time=2
        )

        self.play(
            FadeOut(slow_box),
            FadeOut(slow),
            run_time=2
        )

        pipeline_box = RoundedRectangle(
            width=6.5,
            height=1.15,
            corner_radius=.08,
            stroke_color=GOOD,
            stroke_width=3
        ).shift(DOWN * 3.25)

        pipeline = VGroup(
            Text(
                "PIPELINE",
                font_size=27,
                color=GOOD,
                weight=BOLD
            ),
            Text(
                "send commands without waiting",
                font_size=22,
                color=GOOD
            )
        ).arrange(DOWN, buff=.08).move_to(pipeline_box)

        self.play(
            FadeIn(pipeline_box),
            FadeIn(pipeline),
            run_time=3
        )

        new_lab = Text(
            "multiple commands in flight",
            font_size=28,
            color=ACCENT
        ).move_to(DOWN * 2.25)

        self.play(
            marker.animate.next_to(cells[8], UP, buff=.16),
            Transform(lab, new_lab),
            run_time=5
        )

        self.wait(9)


class B09_Rebalance(BrutalistScene):
    def construct(self):
        self.title("CLUSTER TOPOLOGY CHANGES CAN REDIRECT REQUESTS")

        parts = VGroup(
            *[
                self.box(
                    f"SLOT {i + 1}",
                    1.7,
                    .62,
                    ACCENT,
                    22
                )
                for i in range(6)
            ]
        ).arrange(DOWN, buff=.28).shift(LEFT * 2.7 + UP * .45)

        cs = VGroup(
            *[
                self.box(
                    f"NODE {chr(65 + i)}",
                    1.9,
                    .78,
                    GOOD,
                    23
                )
                for i in range(4)
            ]
        ).arrange(DOWN, buff=.75).shift(RIGHT * 2.55 + UP * .45)

        self.play(
            FadeIn(parts),
            FadeIn(cs),
            run_time=3
        )

        pairs = [
            (0, 0),
            (1, 0),
            (2, 1),
            (3, 1),
            (4, 2),
            (5, 3)
        ]

        lines = VGroup(
            *[
                Line(
                    parts[p].get_right(),
                    cs[c].get_left(),
                    color=MUTED
                )
                for p, c in pairs
            ]
        )

        self.play(Create(lines), run_time=4)

        self.play(
            cs[1][0].animate.set_stroke(BAD),
            cs[1][1].animate.set_color(BAD),
            run_time=2
        )

        self.play(
            FadeOut(cs[1]),
            FadeOut(lines[2]),
            FadeOut(lines[3]),
            run_time=2
        )

        rb = RoundedRectangle(
            width=5.3,
            height=1.0,
            corner_radius=.08,
            stroke_color=ACCENT,
            stroke_width=3
        )

        rt = Text(
            "MOVED",
            font_size=34,
            color=ACCENT,
            weight=BOLD
        ).move_to(rb)

        rg = VGroup(rb, rt).shift(DOWN * 3.7)

        self.play(FadeIn(rg), run_time=2)
        self.play(FadeOut(rg), run_time=2)

        self.play(
            Create(
                Line(
                    parts[2].get_right(),
                    cs[0].get_left(),
                    color=GOOD
                )
            ),
            Create(
                Line(
                    parts[3].get_right(),
                    cs[2].get_left(),
                    color=GOOD
                )
            ),
            run_time=3
        )

        self.wait(3.5)


class B10_Replication(BrutalistScene):
    def construct(self):
        self.title("REPLICATION GIVES A REDIS PRIMARY FAILOVER OPTIONS")

        names = [
            "REDIS NODE A",
            "REDIS NODE B",
            "REDIS NODE C"
        ]

        brokers = VGroup()

        for name in names:
            rect = Rectangle(
                width=5.5,
                height=2.55,
                stroke_color=FG,
                stroke_width=3
            )

            label = Text(
                name,
                font_size=27,
                color=FG,
                weight=BOLD
            ).move_to(
                rect.get_top() + DOWN * .38
            )

            brokers.add(VGroup(rect, label))

        brokers.arrange(
            DOWN,
            buff=.55
        ).shift(DOWN * .25)

        self.play(FadeIn(brokers), run_time=4)

        reps = VGroup(
            self.box("PRIMARY", 2.7, .72, ACCENT, 23),
            self.box("REPLICA", 2.7, .72, GOOD, 23),
            self.box("REPLICA", 2.7, .72, GOOD, 23)
        )

        for role, broker in zip(reps, brokers):
            role.move_to(
                broker[0].get_center() + DOWN * .42
            )

        self.play(FadeIn(reps), run_time=3)

        # Route replication arrows through a clean right-side lane.
        lane_x = brokers.get_right()[0] + .60

        def replication_route(src, dst):
            start = src.get_right()
            end = dst.get_right()

            return VGroup(
                Line(
                    start,
                    [lane_x, start[1], 0],
                    color=MUTED,
                    stroke_width=3
                ),
                Line(
                    [lane_x, start[1], 0],
                    [lane_x, end[1], 0],
                    color=MUTED,
                    stroke_width=3
                ),
                Arrow(
                    [lane_x, end[1], 0],
                    end,
                    buff=.12,
                    color=MUTED,
                    stroke_width=3
                )
            )

        arrows = VGroup(
            replication_route(reps[0], reps[1]),
            replication_route(reps[0], reps[2])
        )
        self.play(Create(arrows), run_time=4)

        self.play(
            brokers[0][0].animate.set_stroke(BAD),
            FadeOut(reps[0]),
            run_time=3
        )

        promoted = self.box(
            "NEW PRIMARY",
            3.0,
            .72,
            ACCENT,
            22
        ).move_to(reps[1])

        self.play(
            Transform(reps[1], promoted),
            run_time=4
        )

        self.wait(5)


class B11_FullScale(BrutalistScene):
    def construct(self):
        self.title("REDIS SCALES BY DISTRIBUTING DATA AND REQUEST LOAD")

        clients = self.box(
            "CLIENTS",
            5.0,
            1.0,
            ACCENT
        ).shift(UP * 4.4)

        brokers = VGroup(
            *[
                self.box(
                    f"NODE {chr(65 + i)}",
                    2.6,
                    1.25,
                    FG,
                    23
                )
                for i in range(4)
            ]
        ).arrange_in_grid(
            rows=2,
            cols=2,
            buff=(.45, .45)
        ).shift(UP * .5)

        groups = VGroup(
            self.box(
                "REPLICAS",
                5.0,
                1.0,
                GOOD,
                23
            ),
            self.box(
                "BACKING SYSTEMS",
                5.0,
                1.0,
                GOOD,
                23
            )
        ).arrange(DOWN, buff=.45).shift(DOWN * 3.0)

        self.play(
            FadeIn(clients),
            FadeIn(brokers),
            FadeIn(groups),
            run_time=4
        )

        self.play(
            Create(
                Arrow(
                    clients.get_bottom(),
                    brokers.get_top(),
                    color=ACCENT,
                    buff=.25
                )
            ),
            Create(
                Arrow(
                    brokers.get_bottom(),
                    groups.get_top(),
                    color=GOOD,
                    buff=.25
                )
            ),
            run_time=4
        )

        counter = Text(
            "10,000 requests",
            font_size=38,
            color=FG
        ).to_edge(DOWN, buff=.65)

        self.play(FadeIn(counter), run_time=2)

        for txt in [
            "100,000 requests",
            "1,000,000+ requests"
        ]:
            self.play(
                Transform(
                    counter,
                    Text(
                        txt,
                        font_size=38,
                        color=ACCENT
                    ).to_edge(DOWN, buff=.65)
                ),
                run_time=3
            )

        self.wait(6)


class B12_Tradeoffs(BrutalistScene):
    def construct(self):
        self.title("REDIS IS FAST, BUT WORKLOAD LIMITS STILL MATTER")

        cards = VGroup(
            self.box(
                "HOT KEY",
                5.4,
                1.55,
                BAD,
                25
            ),
            self.box(
                "COSTLY / LARGE OPS",
                5.4,
                1.55,
                BAD,
                25
            ),
            self.box(
                "MEMORY PRESSURE",
                5.4,
                1.55,
                BAD,
                25
            ),
            self.box(
                "NETWORK / PERSISTENCE",
                5.4,
                1.55,
                BAD,
                25
            )
        ).arrange(DOWN, buff=.42).shift(DOWN * .15)

        self.play(
            LaggedStart(
                *[FadeIn(c) for c in cards],
                lag_ratio=.35
            ),
            run_time=8
        )

        notes = VGroup(
            Text(
                "WORKLOAD DESIGN STILL MATTERS",
                font_size=26,
                color=FG,
                weight=BOLD
            ),
            Text(
                "memory · network · persistence · client behavior",
                font_size=22,
                color=MUTED
            )
        ).arrange(DOWN, buff=.12).to_edge(DOWN, buff=.7)

        self.play(FadeIn(notes), run_time=3)
        self.wait(10)
