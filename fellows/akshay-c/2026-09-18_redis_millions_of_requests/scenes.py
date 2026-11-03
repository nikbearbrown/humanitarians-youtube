# -*- coding: utf-8 -*-
from manim import *

# Native 4K UHD landscape canvas.
config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 24
config.frame_width = 16
config.frame_height = 9

BG = "#111111"; FG = "#F2EEE8"; ACCENT = "#C46F4B"; MUTED = "#777777"; GOOD = "#78A083"; BAD = "#B65C5C"

class BrutalistScene(Scene):
    def setup(self): self.camera.background_color = BG
    def title(self, text):
        # Explicitly wrap long headings into short centered lines.
        words = text.split()
        lines = []
        current = []

        for word in words:
            candidate = " ".join(current + [word])

            if len(candidate) > 30 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)

        if current:
            lines.append(" ".join(current))

        title_group = VGroup(
            *[
                Text(
                    line,
                    font_size=34,
                    color=FG,
                    weight=BOLD
                )
                for line in lines
            ]
        ).arrange(DOWN, buff=.10)

        # Hard safety width considerably inside the 16-unit frame.
        for line in title_group:
            if line.width > 11.0:
                line.scale_to_fit_width(11.0)

        title_group.move_to(UP * 3.45)

        self.add(title_group)
        return title_group

    def box(self, label, w=2.2, h=0.85, color=FG):
        r=Rectangle(width=w,height=h,stroke_color=color,stroke_width=3)
        tx=Text(label,font_size=26,color=color).move_to(r)
        return VGroup(r,tx)
    def event(self, label, color=ACCENT):
        c=RoundedRectangle(width=.72,height=.42,corner_radius=.08,stroke_color=color,fill_color=color,fill_opacity=.16)
        return VGroup(c,Text(label,font_size=18,color=FG).move_to(c))

class B01_DirectFanoutFails(BrutalistScene):
    def construct(self):
        self.title("WITHOUT REDIS: THE DATA PATH BECOMES THE BOTTLENECK")

        api = self.box(
            "API",
            2.4,
            1.0,
            ACCENT
        ).shift(LEFT * 5)

        names = [
            "SESSIONS",
            "PROFILES",
            "PRODUCTS",
            "COUNTERS",
            "RATE LIMITS"
        ]

        svcs = VGroup(
            *[
                self.box(
                    n,
                    2.2,
                    .72
                )
                for n in names
            ]
        ).arrange(
            DOWN,
            buff=.28
        ).shift(RIGHT * 3.5)

        self.play(
            FadeIn(api),
            FadeIn(svcs),
            run_time=4
        )

        lines = VGroup(
            *[
                Arrow(
                    api.get_right(),
                    svc.get_left(),
                    buff=.12,
                    stroke_width=3,
                    color=MUTED
                )
                for svc in svcs
            ]
        )

        self.play(
            LaggedStart(
                *[
                    Create(line)
                    for line in lines
                ],
                lag_ratio=.12
            ),
            run_time=4
        )

        overloaded = svcs[2]

        slow = Text(
            "SLOW BACKING\nSTORE",
            font_size=26,
            color=BAD,
            line_spacing=.9
        ).next_to(overloaded, RIGHT, buff=.25)

        self.play(
            overloaded[0].animate.set_stroke(BAD),
            FadeIn(slow),
            run_time=3
        )

        q = (
            VGroup(
                *[
                    self.event(str(i))
                    for i in range(8)
                ]
            )
            .arrange(RIGHT, buff=.06)
            .scale(.8)
            .next_to(api, UP, buff=.6)
            .align_to(api, LEFT)
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(x)
                    for x in q
                ],
                lag_ratio=.08
            ),
            run_time=4
        )

        warn = Text(
            "latency ↑   database load ↑   queues ↑",
            font_size=34,
            color=BAD
        ).to_edge(DOWN)

        self.play(
            FadeIn(warn),
            run_time=2
        )

        self.wait(3)
class B02_DurableLog(BrutalistScene):
    def construct(self):
        self.title("REDIS PUTS HOT DATA ON THE FAST PATH")

        prod = self.box(
            "APPLICATION",
            2.3,
            .9,
            ACCENT
        ).move_to(LEFT * 5.6)

        cons = VGroup(
            self.box("CACHE HIT", 2.7, .75, GOOD),
            self.box("BACKING DB", 2.7, .75, BAD)
        ).arrange(DOWN, buff=.75).move_to(RIGHT * 5.45)

        log = Rectangle(
            width=6.0,
            height=2.0,
            stroke_color=FG,
            stroke_width=3
        ).move_to(ORIGIN)

        topic = Text(
            "REDIS / MEMORY - frequently accessed data",
            font_size=25,
            color=FG
        ).next_to(log, UP, buff=.22)

        # Two rows of cached entries kept physically inside
        # the Redis memory box.
        row1 = VGroup(
            *[self.event(str(i)) for i in range(6)]
        ).arrange(RIGHT, buff=.16)

        row2 = VGroup(
            *[self.event(str(i)) for i in range(6, 12)]
        ).arrange(RIGHT, buff=.16)

        cells = VGroup(
            row1,
            row2
        ).arrange(DOWN, buff=.22).move_to(log)

        self.play(
            FadeIn(prod),
            FadeIn(log),
            FadeIn(topic),
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
                    prod.get_right(),
                    log.get_left(),
                    buff=.15,
                    color=MUTED
                )
            ),
            run_time=4
        )

        self.play(
            Create(
                Arrow(
                    log.get_right(),
                    cons[0].get_left(),
                    buff=.15,
                    color=GOOD
                )
            ),
            Create(
                Arrow(
                    log.get_right(),
                    cons[1].get_left(),
                    buff=.15,
                    color=BAD
                )
            ),
            run_time=2
        )

        self.wait(4.5)

class B03_Partitions(BrutalistScene):
    def construct(self):
        self.title("EVENT-DRIVEN NETWORKING HANDLES MANY CLIENT CONNECTIONS")

        lanes = VGroup(
            *[
                Rectangle(
                    width=9.5,
                    height=.7,
                    stroke_color=FG,
                    stroke_width=2
                )
                for _ in range(6)
            ]
        ).arrange(DOWN, buff=.22).shift(DOWN * .15)

        labels = VGroup(
            *[
                Text(
                    f"C{i + 1}",
                    font_size=26,
                    color=ACCENT
                ).next_to(lanes[i], LEFT)
                for i in range(6)
            ]
        )

        self.play(
            FadeIn(lanes),
            FadeIn(labels),
            run_time=3
        )

        commands = [
            "GET",
            "SET",
            "INCR",
            "GET",
            "SET",
            "GET",
            "INCR",
            "GET"
        ]

        dest = [0, 1, 2, 0, 1, 4, 0, 2]

        events = VGroup(
            *[self.event(cmd) for cmd in commands]
        ).arrange(RIGHT, buff=.12).to_edge(UP, buff=1.5)

        self.play(
            FadeIn(events),
            run_time=3
        )

        xstarts = [
            lanes[d].get_left()
            + RIGHT * (
                1.0
                + 1.1 * sum(
                    1 for j in dest[:i] if j == d
                )
            )
            for i, d in enumerate(dest)
        ]

        self.play(
            *[
                events[i].animate.move_to(xstarts[i])
                for i in range(len(events))
            ],
            run_time=6
        )

        note = Text(
            "Many connections stay open; Redis reacts when sockets have work ready.",
            font_size=30,
            color=FG
        ).to_edge(DOWN)

        self.play(
            FadeIn(note),
            run_time=3
        )

        self.wait(4.5)
class B05_Brokers(BrutalistScene):
    def construct(self):
        self.title("REDIS CLUSTER SPREADS THE KEYSPACE ACROSS NODES")

        brokers = VGroup(
            *[
                self.box(
                    f"REDIS NODE {chr(65 + i)}",
                    3.3,
                    3.8
                )
                for i in range(3)
            ]
        ).arrange(RIGHT, buff=.8).shift(DOWN * .2)

        self.play(FadeIn(brokers), run_time=3)

        mapping = [
            ["SLOTS 0-2730", "SLOTS 2731-5460"],
            ["SLOTS 5461-8191", "SLOTS 8192-10922"],
            ["SLOTS 10923-13652", "SLOTS 13653-16383"]
        ]

        for b, ranges in zip(brokers, mapping):
            cards = VGroup(
                *[
                    VGroup(
                        Rectangle(
                            width=2.7,
                            height=.62,
                            stroke_color=ACCENT,
                            stroke_width=3
                        ),
                        Text(
                            r,
                            font_size=20,
                            color=FG
                        )
                    )
                    for r in ranges
                ]
            ).arrange(DOWN, buff=.4).move_to(b)

            self.play(FadeIn(cards), run_time=3)

        foot = Text(
            "memory + network traffic + command processing spread horizontally",
            font_size=32,
            color=GOOD
        ).to_edge(DOWN)

        self.play(FadeIn(foot), run_time=3)
        self.wait(4.5)
class B06_ConsumerGroups(BrutalistScene):
    def construct(self):
        self.title("HASH SLOTS ROUTE EACH KEY TO ITS OWNING NODE")

        keys = VGroup(
            self.box("user:42  →  slot 1200", 3.4, .58, ACCENT),
            self.box("cart:18  →  slot 4100", 3.4, .58, ACCENT),
            self.box("item:7  →  slot 6200", 3.4, .58, ACCENT),
            self.box("rate:9  →  slot 8800", 3.4, .58, ACCENT),
            self.box("sess:5  →  slot 12100", 3.4, .58, ACCENT),
            self.box("count:3  →  slot 15000", 3.4, .58, ACCENT)
        ).arrange(DOWN, buff=.14).shift(LEFT * 4.5)

        nodes = VGroup(
            self.box("NODE A", 2.2, .58, GOOD),
            self.box("NODE A", 2.2, .58, GOOD),
            self.box("NODE B", 2.2, .58, GOOD),
            self.box("NODE B", 2.2, .58, GOOD),
            self.box("NODE C", 2.2, .58, GOOD),
            self.box("NODE C", 2.2, .58, GOOD)
        ).arrange(DOWN, buff=.14).shift(RIGHT * 4.5)

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

        self.play(
            Create(lines),
            run_time=5
        )

        rule = Text(
            "KEY  →  HASH SLOT  →  OWNING NODE",
            font_size=31,
            color=FG
        ).to_edge(DOWN)

        self.play(
            FadeIn(rule),
            run_time=3
        )

        self.wait(6)

class B07_Offsets(BrutalistScene):
    def construct(self):
        self.title("PIPELINING REDUCES REPEATED NETWORK ROUND TRIPS")

        command_box = Rectangle(
            width=11.6,
            height=2.4,
            stroke_color=FG,
            stroke_width=3
        ).shift(UP * .15)

        command_label = Text(
            "REDIS COMMANDS",
            font_size=28,
            color=FG,
            weight=BOLD
        ).next_to(command_box, UP, buff=.18)

        commands = [
            "GET", "SET", "INCR",
            "GET", "SET", "GET",
            "INCR", "GET", "SET"
        ]

        cells = VGroup(
            *[
                self.event(cmd)
                for cmd in commands
            ]
        ).arrange(RIGHT, buff=.16).scale(1.22)

        cells.move_to(command_box)

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
        ).scale(.22).rotate(PI).next_to(cells[0], UP, buff=.18)

        lab = Text(
            "one command -> wait -> one reply",
            font_size=30,
            color=ACCENT
        ).next_to(marker, UP, buff=.12)

        self.play(
            FadeIn(marker),
            FadeIn(lab),
            run_time=3
        )

        slow_box = RoundedRectangle(
            width=6.4,
            height=.95,
            corner_radius=.08,
            stroke_color=BAD,
            stroke_width=3
        ).shift(DOWN * 2.15)

        slow = Text(
            "REPEATED NETWORK ROUND TRIPS",
            font_size=29,
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
            width=7.4,
            height=.95,
            corner_radius=.08,
            stroke_color=GOOD,
            stroke_width=3
        ).shift(DOWN * 2.15)

        pipeline = Text(
            "PIPELINE -> SEND COMMANDS WITHOUT WAITING",
            font_size=27,
            color=GOOD,
            weight=BOLD
        ).move_to(pipeline_box)

        self.play(
            FadeIn(pipeline_box),
            FadeIn(pipeline),
            run_time=3
        )

        self.play(
            marker.animate.next_to(cells[8], UP, buff=.18),
            Transform(
                lab,
                Text(
                    "multiple commands in flight",
                    font_size=30,
                    color=ACCENT
                ).next_to(cells[8], UP, buff=.12)
            ),
            run_time=5
        )

        self.wait(9)

class B09_Rebalance(BrutalistScene):
    def construct(self):
        self.title("CLUSTER TOPOLOGY CHANGES CAN REDIRECT REQUESTS")

        parts = VGroup(
            *[
                self.box(
                    f"SLOT {i+1}",
                    1.5,
                    .55,
                    ACCENT
                )
                for i in range(6)
            ]
        ).arrange(DOWN, buff=.18).shift(LEFT * 4.8)

        cs = VGroup(
            *[
                self.box(
                    f"NODE {chr(65 + i)}",
                    1.8,
                    .72,
                    GOOD
                )
                for i in range(4)
            ]
        ).arrange(DOWN, buff=.55).shift(RIGHT * 4.5)

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

        self.play(
            Create(lines),
            run_time=4
        )

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

        reb = Text(
            "MOVED",
            font_size=38,
            color=ACCENT
        ).move_to(ORIGIN)

        self.play(
            FadeIn(reb),
            run_time=2
        )

        self.play(
            FadeOut(reb),
            run_time=2
        )

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

        broker_names = ["REDIS NODE A", "REDIS NODE B", "REDIS NODE C"]

        broker_groups = VGroup()

        for name in broker_names:
            rect = Rectangle(
                width=3.25,
                height=3.0,
                stroke_color=FG,
                stroke_width=3
            )

            label = Text(
                name,
                font_size=28,
                color=FG,
                weight=BOLD
            )

            # Dedicated header zone.
            label.move_to(
                rect.get_top() + DOWN * .42
            )

            broker_groups.add(
                VGroup(rect, label)
            )

        broker_groups.arrange(
            RIGHT,
            buff=.95
        ).shift(DOWN * .25)

        self.play(
            FadeIn(broker_groups),
            run_time=4
        )

        reps = VGroup(
            self.box("PRIMARY", 2.15, .72, ACCENT),
            self.box("REPLICA", 2.15, .72, GOOD),
            self.box("REPLICA", 2.15, .72, GOOD)
        )

        # Place role cards well below each node header.
        for role, broker in zip(reps, broker_groups):
            role.move_to(
                broker[0].get_center() + DOWN * .55
            )

        self.play(
            FadeIn(reps),
            run_time=3
        )

        # Preserve the proven connector geometry:
        # A -> B direct; A -> C through a clean upper routing lane.
        arrow_to_b = Arrow(
            reps[0].get_right(),
            reps[1].get_left(),
            buff=.18,
            color=MUTED
        )

        top_lane_y = broker_groups.get_top()[1] + .45
        start_c = reps[0].get_top()
        end_c = reps[2].get_top()

        route_to_c = VGroup(
            Line(
                start_c,
                [start_c[0], top_lane_y, 0],
                color=MUTED,
                stroke_width=3
            ),
            Line(
                [start_c[0], top_lane_y, 0],
                [end_c[0], top_lane_y, 0],
                color=MUTED,
                stroke_width=3
            ),
            Arrow(
                [end_c[0], top_lane_y, 0],
                end_c,
                buff=.12,
                color=MUTED,
                stroke_width=3
            )
        )

        self.play(
            Create(arrow_to_b),
            Create(route_to_c),
            run_time=4
        )

        self.play(
            broker_groups[0][0].animate.set_stroke(BAD),
            FadeOut(reps[0]),
            run_time=3
        )

        promoted = self.box(
            "NEW PRIMARY",
            2.25,
            .72,
            ACCENT
        ).move_to(reps[1])

        self.play(
            Transform(reps[1], promoted),
            run_time=4
        )

        self.wait(5)

class B11_FullScale(BrutalistScene):
    def construct(self):
        self.title("REDIS SCALES BY DISTRIBUTING DATA AND REQUEST LOAD")

        producers = self.box(
            "CLIENTS",
            2.4,
            1.1,
            ACCENT
        ).shift(LEFT * 5.2)

        brokers = VGroup(
            *[
                self.box(
                    f"NODE {chr(65 + i)}",
                    1.5,
                    2.8
                )
                for i in range(4)
            ]
        ).arrange(RIGHT, buff=.35)

        groups = VGroup(
            self.box(
                "REPLICAS",
                2.7,
                1.2,
                GOOD
            ),
            self.box(
                "BACKING\nSYSTEMS",
                2.7,
                1.2,
                GOOD
            )
        ).arrange(DOWN, buff=.7).shift(RIGHT * 5.6)

        self.play(
            FadeIn(producers),
            FadeIn(brokers),
            FadeIn(groups),
            run_time=4
        )

        self.play(
            Create(
                Arrow(
                    producers.get_right(),
                    brokers.get_left(),
                    color=ACCENT
                )
            ),
            Create(
                Arrow(
                    brokers.get_right(),
                    groups.get_left(),
                    color=GOOD
                )
            ),
            run_time=4
        )

        counter = Text(
            "10,000 requests",
            font_size=44,
            color=FG
        ).to_edge(DOWN)

        self.play(
            FadeIn(counter),
            run_time=2
        )

        for txt in [
            "100,000 requests",
            "1,000,000+ requests"
        ]:
            self.play(
                Transform(
                    counter,
                    Text(
                        txt,
                        font_size=44,
                        color=ACCENT
                    ).to_edge(DOWN)
                ),
                run_time=3
            )

        self.wait(6)
class B12_Tradeoffs(BrutalistScene):
    def construct(self):
        self.title("REDIS IS FAST, BUT WORKLOAD LIMITS STILL MATTER")

        cards = VGroup(
            self.box(
                "HOT\nKEY",
                3.2,
                1.7,
                BAD
            ),
            self.box(
                "COSTLY / LARGE\nOPS",
                3.2,
                1.7,
                BAD
            ),
            self.box(
                "MEMORY\nPRESSURE",
                3.2,
                1.7,
                BAD
            ),
            self.box(
                "NETWORK /\nPERSISTENCE",
                3.2,
                1.7,
                BAD
            )
        ).arrange_in_grid(
            rows=2,
            cols=2,
            buff=(1.0, .7)
        ).shift(DOWN * .2)

        self.play(
            LaggedStart(
                *[FadeIn(c) for c in cards],
                lag_ratio=.35
            ),
            run_time=8
        )

        notes = Text(
            "workload design still matters: memory · network · persistence · client behavior",
            font_size=29,
            color=FG
        ).to_edge(DOWN)

        self.play(
            FadeIn(notes),
            run_time=3
        )

        self.wait(10)