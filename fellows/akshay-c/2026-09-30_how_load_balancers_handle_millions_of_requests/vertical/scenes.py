# -*- coding: utf-8 -*-
from manim import *

# Native 4K portrait — DO NOT change to 1080x1920.
config.pixel_width = 2160
config.pixel_height = 3840
config.frame_rate = 24
config.frame_width = 9
config.frame_height = 16

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

        # Portrait-safe wrapping.
        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 25 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)

        if current:
            lines.append(" ".join(current))

        title = VGroup(*[
            Text(line, font_size=31, color=FG, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=.10)

        title.move_to(UP * 6.55)

        if title.width > 7.0:
            title.scale_to_fit_width(7.0)

        rule = Line(
            LEFT * 3.35,
            RIGHT * 3.35,
            color=ACCENT,
            stroke_width=5
        ).next_to(title, DOWN, buff=.18)

        return VGroup(title, rule)

    def box(self, label, width=5.7, height=1.10,
            color=FG, font_size=27):

        rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=.08,
            stroke_color=color,
            stroke_width=3
        )

        text = Text(
            label,
            font_size=font_size,
            color=color,
            weight=BOLD
        )

        if text.width > width - .45:
            text.scale_to_fit_width(width - .45)

        text.move_to(rect)

        return VGroup(rect, text)

    def server(self, label, color=FG):
        return self.box(
            label,
            width=5.4,
            height=1.05,
            color=color,
            font_size=25
        )

    def request(self, label):
        return self.box(
            label,
            width=2.1,
            height=.72,
            color=ACCENT,
            font_size=20
        )

    def caption(self, text, color=MUTED):
        t = Text(
            text,
            font_size=23,
            color=color,
            weight=BOLD
        )

        if t.width > 7.0:
            t.scale_to_fit_width(7.0)

        t.move_to(DOWN * 6.45)
        return t

    def vertical_arrow(self, source, target, color=GOOD,
                       stroke_width=5, buff=.14):
        return Arrow(
            source.get_bottom(),
            target.get_top(),
            buff=buff,
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=.14
        )

    def server_stack(self, colors=None):
        colors = colors or [FG, FG, FG]

        servers = VGroup(
            self.server("SERVER 1", colors[0]),
            self.server("SERVER 2", colors[1]),
            self.server("SERVER 3", colors[2])
        )

        servers.arrange(DOWN, buff=.48)

        return servers

    def load_balancer(self):
        return self.box(
            "LOAD BALANCER",
            width=5.8,
            height=1.20,
            color=ACCENT,
            font_size=27
        )


# ============================================================
# B00 — MILLIONS OF REQUESTS
# ============================================================

class B00_MillionsOfRequests(BrutalistScene):

    def construct(self):
        title = self.heading("MILLIONS OF REQUESTS")

        requests = VGroup(*[
            self.request(f"REQ {i}")
            for i in range(1, 7)
        ])

        requests.arrange_in_grid(
            rows=2,
            cols=3,
            buff=(.30, .32)
        )
        requests.move_to(UP * 2.7)

        app = self.box(
            "APPLICATION",
            width=5.7,
            height=1.25,
            color=FG
        ).move_to(DOWN * 1.8)

        self.play(FadeIn(title), run_time=.7)

        self.play(
            LaggedStart(
                *[FadeIn(r) for r in requests],
                lag_ratio=.10
            ),
            run_time=1.0
        )

        self.play(FadeIn(app), run_time=.4)

        arrows = VGroup(*[
            Arrow(
                r.get_bottom(),
                app.get_top(),
                buff=.16,
                color=GOOD,
                stroke_width=3,
                max_tip_length_to_length_ratio=.12
            )
            for r in requests
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in arrows],
                lag_ratio=.08
            ),
            run_time=1.5
        )

        cap = self.caption(
            "POPULAR SERVICES CAN RECEIVE ENORMOUS TRAFFIC"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B01 — ONE SERVER BOTTLENECK
# ============================================================

class B01_OneServerBottleneck(BrutalistScene):

    def construct(self):
        title = self.heading("ONE SERVER. TOO MUCH TRAFFIC.")

        requests = VGroup(*[
            self.request(f"REQ {i}")
            for i in range(1, 6)
        ])

        requests.arrange_in_grid(
            rows=2,
            cols=3,
            buff=(.30, .32)
        )
        requests.move_to(UP * 2.8)

        server = self.server(
            "SERVER",
            BAD
        ).move_to(DOWN * 1.8)

        self.play(FadeIn(title), run_time=.7)

        self.play(
            LaggedStart(
                *[FadeIn(r) for r in requests],
                lag_ratio=.10
            ),
            run_time=.8
        )

        self.play(FadeIn(server), run_time=.4)

        arrows = VGroup(*[
            Arrow(
                r.get_bottom(),
                server.get_top(),
                buff=.16,
                color=BAD,
                stroke_width=4,
                max_tip_length_to_length_ratio=.12
            )
            for r in requests
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in arrows],
                lag_ratio=.10
            ),
            run_time=1.4
        )

        overloaded = Text(
            "OVERLOADED",
            font_size=27,
            color=BAD,
            weight=BOLD
        ).next_to(server, DOWN, buff=.45)

        self.play(FadeIn(overloaded), run_time=.5)
        self.wait(1)


# ============================================================
# B02 — MORE SERVERS
# ============================================================

class B02_MoreServers(BrutalistScene):

    def construct(self):
        title = self.heading("MORE SERVERS. NOW WHAT?")

        incoming = self.box(
            "INCOMING REQUESTS",
            width=5.8,
            height=1.15,
            color=ACCENT
        ).move_to(UP * 3.3)

        question = Text(
            "?",
            font_size=68,
            color=ACCENT,
            weight=BOLD
        ).move_to(UP * .9)

        servers = self.server_stack()
        servers.move_to(DOWN * 2.1)

        self.play(FadeIn(title), run_time=.7)
        self.play(FadeIn(incoming), run_time=.5)
        self.play(FadeIn(question), run_time=.4)

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.15
            ),
            run_time=1
        )

        cap = self.caption(
            "WHO DECIDES WHERE EACH REQUEST GOES?"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(1)




# ============================================================
# B03 — LOAD BALANCER
# ============================================================

class B03_LoadBalancer(BrutalistScene):

    def construct(self):
        title = self.heading("THE LOAD BALANCER")

        users = self.box(
            "USERS",
            width=5.2,
            color=FG
        ).move_to(UP * 4.0)

        lb = self.load_balancer().move_to(UP * 1.5)

        servers = self.server_stack()
        servers.move_to(DOWN * 3.0)

        self.play(FadeIn(title), run_time=.7)

        self.play(
            FadeIn(users),
            FadeIn(lb),
            run_time=.8
        )

        inbound = self.vertical_arrow(users, lb, GOOD)
        self.play(Create(inbound), run_time=.7)

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            run_time=.8
        )

        # One clean downward connection into the server pool.
        # Avoids diagonal routes crossing server boxes.
        pool_arrow = Arrow(
            lb.get_bottom(),
            servers[0].get_top(),
            buff=.16,
            color=GOOD,
            stroke_width=5,
            max_tip_length_to_length_ratio=.12
        )

        self.play(Create(pool_arrow), run_time=.7)

        self.play(
            LaggedStart(
                *[
                    s[0].animate.set_stroke(
                        color=GOOD,
                        width=5
                    )
                    for s in servers
                ],
                lag_ratio=.15
            ),
            run_time=.8
        )

        self.wait(1)


# ============================================================
# B04 — ROUND ROBIN
# ============================================================

class B04_RoundRobin(BrutalistScene):

    def construct(self):
        title = self.heading("ROUND ROBIN")

        lb = self.load_balancer().move_to(UP * 4.0)

        servers = self.server_stack()
        servers.move_to(DOWN * 1.25)

        self.play(
            FadeIn(title),
            FadeIn(lb),
            run_time=.8
        )

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            run_time=.8
        )

        labels = [
            "REQUEST 1",
            "REQUEST 2",
            "REQUEST 3"
        ]

        for i, server in enumerate(servers):

            # Request indicator stays centered and inside
            # the portrait-safe width.
            req = Text(
                labels[i],
                font_size=19,
                color=ACCENT,
                weight=BOLD
            )

            req.next_to(server, UP, buff=.16)

            arrow = Arrow(
                req.get_bottom(),
                server.get_top(),
                buff=.08,
                color=GOOD,
                stroke_width=4,
                max_tip_length_to_length_ratio=.16
            )

            self.play(
                FadeIn(req),
                Create(arrow),
                run_time=.55
            )

            self.play(
                server[0].animate.set_stroke(
                    color=GOOD,
                    width=5
                ),
                run_time=.25
            )

            self.play(
                FadeOut(req),
                FadeOut(arrow),
                server[0].animate.set_stroke(
                    color=FG,
                    width=3
                ),
                run_time=.25
            )

        cap = self.caption(
            "S1  →  S2  →  S3  →  S1 ..."
        )

        self.play(FadeIn(cap), run_time=.4)
        self.wait(.7)


# ============================================================
# B05 — LEAST CONNECTIONS
# ============================================================

class B05_LeastConnections(BrutalistScene):

    def construct(self):
        title = self.heading("LEAST CONNECTIONS")

        lb = self.load_balancer().move_to(UP * 4.0)

        servers = self.server_stack()
        servers.move_to(DOWN * 1.25)

        self.play(
            FadeIn(title),
            FadeIn(lb),
            run_time=.8
        )

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            run_time=.8
        )

        # Connection counts are centered below each server,
        # rather than placed outside the box horizontally.
        counts = VGroup(
            Text(
                "8 ACTIVE",
                font_size=18,
                color=MUTED,
                weight=BOLD
            ),
            Text(
                "2 ACTIVE",
                font_size=18,
                color=GOOD,
                weight=BOLD
            ),
            Text(
                "6 ACTIVE",
                font_size=18,
                color=MUTED,
                weight=BOLD
            )
        )

        for count, server in zip(counts, servers):
            count.next_to(server, DOWN, buff=.10)

        self.play(
            LaggedStart(
                *[FadeIn(c) for c in counts],
                lag_ratio=.12
            ),
            run_time=.7
        )

        chosen = servers[1]


        self.play(
            chosen[0].animate.set_stroke(
                color=GOOD,
                width=6
            ),
            run_time=.4
        )

        selected = Text(
            "NEXT REQUEST",
            font_size=19,
            color=GOOD,
            weight=BOLD
        )

        # Keep the routing decision separate from all server labels.
        selected.move_to(DOWN * 4.65)
        self.play(FadeIn(selected), run_time=.4)

        cap = self.caption(
            "FEWEST ACTIVE CONNECTIONS",
            GOOD
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(1)


# ============================================================
# B06 — HEALTH CHECKS
# ============================================================

class B06_HealthChecks(BrutalistScene):

    def construct(self):
        title = self.heading("HEALTH CHECKS")

        lb = self.load_balancer().move_to(UP * 4.0)

        servers = self.server_stack(
            [GOOD, BAD, GOOD]
        )
        servers.move_to(DOWN * 1.15)

        self.play(
            FadeIn(title),
            FadeIn(lb),
            run_time=.8
        )

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            run_time=.8
        )

        # Status labels live inside the right side of each box,
        # keeping everything within the portrait-safe area.
        states = VGroup(
            Text("HEALTHY", font_size=17, color=GOOD, weight=BOLD),
            Text("UNAVAILABLE", font_size=17, color=BAD, weight=BOLD),
            Text("HEALTHY", font_size=17, color=GOOD, weight=BOLD)
        )

        for state, server in zip(states, servers):
            state.next_to(
                server,
                DOWN,
                buff=.11
            )

        # A single health-check indicator points to the server pool,
        # avoiding lines that cross intervening server boxes.
        check_label = Text(
            "HEALTH CHECKS",
            font_size=20,
            color=MUTED,
            weight=BOLD
        ).move_to(UP * 1.55)

        check_arrow = DashedLine(
            lb.get_bottom(),
            servers[0].get_top(),
            dash_length=.12,
            color=MUTED,
            stroke_width=4
        )

        self.play(
            FadeIn(check_label),
            Create(check_arrow),
            run_time=.8
        )

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in states],
                lag_ratio=.15
            ),
            run_time=.8
        )

        self.wait(1)


# ============================================================
# B07 — ROUTE AROUND FAILURE
# ============================================================

class B07_RouteAroundFailure(BrutalistScene):

    def construct(self):
        title = self.heading("ROUTE AROUND FAILURE")

        lb = self.load_balancer().move_to(UP * 4.0)

        servers = self.server_stack(
            [GOOD, BAD, GOOD]
        )
        servers.move_to(DOWN * 1.15)

        self.play(
            FadeIn(title),
            FadeIn(lb),
            run_time=.8
        )

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            run_time=.8
        )

        offline = Text(
            "OFFLINE",
            font_size=18,
            color=BAD,
            weight=BOLD
        ).next_to(
            servers[1],
            DOWN,
            buff=.11
        )

        self.play(FadeIn(offline), run_time=.4)

        # Short local arrows show traffic reaching only the
        # healthy servers without crossing any server boxes.
        top_arrow = Arrow(
            servers[0].get_left() + LEFT * 1.15,
            servers[0].get_left(),
            buff=.12,
            color=GOOD,
            stroke_width=5,
            max_tip_length_to_length_ratio=.18
        )

        bottom_arrow = Arrow(
            servers[2].get_left() + LEFT * 1.15,
            servers[2].get_left(),
            buff=.12,
            color=GOOD,
            stroke_width=5,
            max_tip_length_to_length_ratio=.18
        )

        self.play(
            Create(top_arrow),
            Create(bottom_arrow),
            servers[0][0].animate.set_stroke(
                color=GOOD,
                width=6
            ),
            servers[2][0].animate.set_stroke(
                color=GOOD,
                width=6
            ),
            run_time=.8
        )

        no_traffic = Text(
            "NO TRAFFIC",
            font_size=18,
            color=BAD,
            weight=BOLD
        ).move_to(DOWN * 4.55)

        self.play(FadeIn(no_traffic), run_time=.4)

        cap = self.caption(
            "REQUESTS CONTINUE THROUGH HEALTHY SERVERS",
            GOOD
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(1)


# ============================================================
# B08 — FINAL ARCHITECTURE
# ============================================================

class B08_ScalableResilientService(BrutalistScene):

    def construct(self):
        title = self.heading(
            "SCALE WITHOUT A SINGLE SERVER BOTTLENECK"
        )

        users = self.box(
            "USERS",
            width=5.2
        ).move_to(UP * 4.25)

        lb = self.load_balancer().move_to(UP * 1.75)

        servers = self.server_stack(
            [GOOD, GOOD, GOOD]
        )
        servers.move_to(DOWN * 2.75)

        self.play(FadeIn(title), run_time=.7)

        self.play(
            FadeIn(users),
            FadeIn(lb),
            run_time=.7
        )

        inbound = self.vertical_arrow(
            users,
            lb,
            GOOD
        )

        self.play(Create(inbound), run_time=.6)

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            run_time=.8
        )

        pool_arrow = Arrow(
            lb.get_bottom(),
            servers[0].get_top(),
            buff=.16,
            color=GOOD,
            stroke_width=5,
            max_tip_length_to_length_ratio=.12
        )

        self.play(Create(pool_arrow), run_time=.6)

        self.play(
            LaggedStart(
                *[
                    s[0].animate.set_stroke(
                        color=GOOD,
                        width=5
                    )
                    for s in servers
                ],
                lag_ratio=.15
            ),
            run_time=.7
        )

        cap = self.caption(
            "SCALABLE  •  AVAILABLE  •  RESILIENT",
            GOOD
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(1)
