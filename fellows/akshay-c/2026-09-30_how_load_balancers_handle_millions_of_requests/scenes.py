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

    # ---------- SAFE LAYOUT HELPERS ----------

    def heading(self, text):
        words = text.split()
        lines = []
        current = []

        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 42 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)

        if current:
            lines.append(" ".join(current))

        title = VGroup(*[
            Text(line, font_size=32, color=FG, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=.08)

        title.move_to(UP * 3.55)

        rule = Line(
            LEFT * 6.8,
            RIGHT * 6.8,
            color=ACCENT,
            stroke_width=5
        ).next_to(title, DOWN, buff=.16)

        return VGroup(title, rule)

    def box(self, label, width=3.0, height=1.05,
            color=FG, font_size=24):

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

        # Prevent long labels from escaping their box.
        max_text_width = width - .35
        if text.width > max_text_width:
            text.scale_to_fit_width(max_text_width)

        text.move_to(rect)

        return VGroup(rect, text)

    def server(self, label, color=FG):
        return self.box(
            label,
            width=2.55,
            height=1.05,
            color=color,
            font_size=24
        )

    def request(self, label):
        return self.box(
            label,
            width=1.25,
            height=.58,
            color=ACCENT,
            font_size=18
        )

    def caption(self, text, color=MUTED):
        t = Text(
            text,
            font_size=22,
            color=color,
            weight=BOLD
        )

        if t.width > 12.5:
            t.scale_to_fit_width(12.5)

        t.move_to(DOWN * 3.45)
        return t

    def edge_arrow(self, source, target, color=GOOD,
                   stroke_width=5, buff=.14):

        # Manim calculates the line between the object boundaries.
        # This avoids arrows running through either box.
        return Arrow(
            source.get_right(),
            target.get_left(),
            buff=buff,
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=.14
        )

    def curved_edge_arrow(self, source, target, color=GOOD, angle=.18):
        return CurvedArrow(
            source.get_right(),
            target.get_left(),
            angle=angle,
            color=color,
            stroke_width=4,
            tip_length=.18
        )

    def server_stack(self, colors=None):
        colors = colors or [FG, FG, FG]

        servers = VGroup(
            self.server("SERVER 1", colors[0]),
            self.server("SERVER 2", colors[1]),
            self.server("SERVER 3", colors[2])
        )

        servers.arrange(DOWN, buff=.55)
        servers.move_to(RIGHT * 4.75 + DOWN * .05)

        return servers

    def load_balancer(self):
        return self.box(
            "LOAD BALANCER",
            width=3.25,
            height=1.25,
            color=ACCENT,
            font_size=25
        )


# ============================================================
# B00 — MILLIONS OF REQUESTS
# ============================================================

class B00_MillionsOfRequests(BrutalistScene):

    def construct(self):
        title = self.heading("MILLIONS OF REQUESTS")

        app = self.box(
            "APPLICATION",
            width=3.2,
            height=1.25,
            color=FG
        ).move_to(RIGHT * 4.6)

        requests = VGroup(*[
            self.request(f"REQ {i}")
            for i in range(1, 7)
        ])

        requests.arrange_in_grid(
            rows=3,
            cols=2,
            buff=(.42, .38)
        )
        requests.move_to(LEFT * 4.6)

        self.play(FadeIn(title), run_time=.7)

        self.play(
            LaggedStart(
                *[FadeIn(r) for r in requests],
                lag_ratio=.10
            ),
            FadeIn(app),
            run_time=1.2
        )

        arrows = VGroup(*[
            self.edge_arrow(r, app, GOOD, 3)
            for r in requests
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in arrows],
                lag_ratio=.08
            ),
            run_time=1.7
        )

        cap = self.caption(
            "POPULAR SERVICES CAN RECEIVE ENORMOUS TRAFFIC"
        )

        self.play(FadeIn(cap), run_time=.6)
        self.wait(.8)


# ============================================================
# B01 — ONE SERVER BOTTLENECK
# ============================================================

class B01_OneServerBottleneck(BrutalistScene):

    def construct(self):
        title = self.heading("ONE SERVER. TOO MUCH TRAFFIC.")

        server = self.server(
            "SERVER",
            BAD
        ).move_to(RIGHT * 4.5)

        requests = VGroup(*[
            self.request(f"REQ {i}")
            for i in range(1, 6)
        ])

        requests.arrange(DOWN, buff=.20)
        requests.move_to(LEFT * 4.7)

        self.play(FadeIn(title), FadeIn(server), run_time=.8)

        self.play(
            LaggedStart(
                *[FadeIn(r) for r in requests],
                lag_ratio=.10
            ),
            run_time=.8
        )

        arrows = VGroup(*[
            self.edge_arrow(r, server, BAD, 4)
            for r in requests
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in arrows],
                lag_ratio=.10
            ),
            run_time=1.5
        )

        overloaded = Text(
            "OVERLOADED",
            font_size=27,
            color=BAD,
            weight=BOLD
        ).next_to(server, DOWN, buff=.35)

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
            width=3.2,
            color=ACCENT
        ).move_to(LEFT * 4.7)

        servers = self.server_stack()

        question = Text(
            "?",
            font_size=70,
            color=ACCENT,
            weight=BOLD
        ).move_to(ORIGIN)

        self.play(FadeIn(title), run_time=.7)
        self.play(FadeIn(incoming), run_time=.5)

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.15
            ),
            run_time=1
        )

        self.play(FadeIn(question), run_time=.5)

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
            width=2.4,
            color=FG
        ).move_to(LEFT * 5.4)

        lb = self.load_balancer().move_to(LEFT * .5)

        servers = self.server_stack()

        self.play(FadeIn(title), run_time=.7)

        self.play(
            FadeIn(users),
            FadeIn(lb),
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            run_time=1.1
        )

        inbound = self.edge_arrow(users, lb, GOOD)

        self.play(Create(inbound), run_time=.7)

        routes = VGroup(*[
            self.curved_edge_arrow(
                lb,
                server,
                GOOD,
                angle=(-.16 if i == 0 else .16 if i == 2 else 0)
            )
            for i, server in enumerate(servers)
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in routes],
                lag_ratio=.18
            ),
            run_time=1.5
        )

        self.wait(1)


# ============================================================
# B04 — ROUND ROBIN
# ============================================================

class B04_RoundRobin(BrutalistScene):

    def construct(self):
        title = self.heading("ROUND ROBIN")

        lb = self.load_balancer().move_to(LEFT * 4.2)
        servers = self.server_stack()

        self.play(FadeIn(title), FadeIn(lb), run_time=.8)

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            run_time=.8
        )

        labels = ["REQUEST 1", "REQUEST 2", "REQUEST 3"]

        for i, server in enumerate(servers):

            req = Text(
                labels[i],
                font_size=20,
                color=ACCENT,
                weight=BOLD
            ).move_to(LEFT * .3 + server.get_center() * UP)

            arrow = self.curved_edge_arrow(
                lb,
                server,
                GOOD,
                angle=(-.12 if i == 0 else .12 if i == 2 else 0)
            )

            self.play(
                FadeIn(req),
                Create(arrow),
                run_time=.65
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
                server[0].animate.set_stroke(
                    color=FG,
                    width=3
                ),
                run_time=.25
            )

        cap = self.caption("S1  →  S2  →  S3  →  S1 ...")
        self.play(FadeIn(cap), run_time=.4)
        self.wait(.7)


# ============================================================
# B05 — LEAST CONNECTIONS
# ============================================================

class B05_LeastConnections(BrutalistScene):

    def construct(self):
        title = self.heading("LEAST CONNECTIONS")

        lb = self.load_balancer().move_to(LEFT * 4.2)
        servers = self.server_stack()

        counts = VGroup(
            Text("8 ACTIVE", font_size=19, color=MUTED, weight=BOLD),
            Text("2 ACTIVE", font_size=19, color=GOOD, weight=BOLD),
            Text("6 ACTIVE", font_size=19, color=MUTED, weight=BOLD)
        )

        for count, server in zip(counts, servers):
            count.next_to(server, RIGHT, buff=.32)

        self.play(FadeIn(title), FadeIn(lb), run_time=.8)

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            LaggedStart(
                *[FadeIn(c) for c in counts],
                lag_ratio=.12
            ),
            run_time=1
        )

        chosen = servers[1]

        arrow = self.curved_edge_arrow(
            lb,
            chosen,
            GOOD,
            angle=0
        )

        self.play(Create(arrow), run_time=.8)

        self.play(
            chosen[0].animate.set_stroke(
                color=GOOD,
                width=6
            ),
            run_time=.4
        )

        cap = self.caption(
            "NEXT REQUEST → SERVER WITH FEWEST ACTIVE CONNECTIONS",
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

        lb = self.load_balancer().move_to(LEFT * 4.2)

        servers = self.server_stack(
            [GOOD, BAD, GOOD]
        )
        servers.shift(LEFT * 0.8)

        self.play(FadeIn(title), FadeIn(lb), run_time=.8)

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            run_time=.8
        )

        checks = VGroup()

        for server in servers:
            checks.add(
                DashedLine(
                    lb.get_right(),
                    server.get_left(),
                    dash_length=.12,
                    color=MUTED,
                    stroke_width=3
                )
            )

        self.play(
            LaggedStart(
                *[Create(c) for c in checks],
                lag_ratio=.15
            ),
            run_time=1.2
        )

        states = VGroup(
            Text("HEALTHY", font_size=19, color=GOOD, weight=BOLD),
            Text("UNAVAILABLE", font_size=19, color=BAD, weight=BOLD),
            Text("HEALTHY", font_size=19, color=GOOD, weight=BOLD)
        )

        for state, server in zip(states, servers):
            state.next_to(server, RIGHT, buff=.30)

        self.play(
            LaggedStart(
                *[FadeIn(s) for s in states],
                lag_ratio=.12
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

        lb = self.load_balancer().move_to(LEFT * 4.2)

        servers = self.server_stack(
            [GOOD, BAD, GOOD]
        )

        failed = Text(
            "OFFLINE",
            font_size=19,
            color=BAD,
            weight=BOLD
        ).next_to(servers[1], RIGHT, buff=.3)

        self.play(
            FadeIn(title),
            FadeIn(lb),
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            FadeIn(failed),
            run_time=1
        )

        top_route = self.curved_edge_arrow(
            lb,
            servers[0],
            GOOD,
            angle=-.12
        )

        bottom_route = self.curved_edge_arrow(
            lb,
            servers[2],
            GOOD,
            angle=.12
        )

        self.play(
            Create(top_route),
            Create(bottom_route),
            run_time=1.2
        )

        bypass = Text(
            "NO TRAFFIC",
            font_size=18,
            color=BAD,
            weight=BOLD
        ).next_to(servers[1], LEFT, buff=.45)

        self.play(FadeIn(bypass), run_time=.5)

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
            width=2.3
        ).move_to(LEFT * 5.3)

        lb = self.load_balancer().move_to(LEFT * .6)

        servers = self.server_stack(
            [GOOD, GOOD, GOOD]
        )

        self.play(FadeIn(title), run_time=.7)

        self.play(
            FadeIn(users),
            FadeIn(lb),
            LaggedStart(
                *[FadeIn(s) for s in servers],
                lag_ratio=.12
            ),
            run_time=1
        )

        inbound = self.edge_arrow(
            users,
            lb,
            GOOD
        )

        self.play(Create(inbound), run_time=.6)

        routes = VGroup(
            self.curved_edge_arrow(lb, servers[0], GOOD, -.14),
            self.curved_edge_arrow(lb, servers[1], GOOD, 0),
            self.curved_edge_arrow(lb, servers[2], GOOD, .14)
        )

        self.play(
            LaggedStart(
                *[Create(a) for a in routes],
                lag_ratio=.15
            ),
            run_time=1.2
        )

        cap = self.caption(
            "SCALABLE  •  AVAILABLE  •  RESILIENT",
            GOOD
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(1)
