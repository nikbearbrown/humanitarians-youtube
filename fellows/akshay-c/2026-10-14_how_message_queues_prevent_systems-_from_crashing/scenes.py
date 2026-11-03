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

        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 40 and current:
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

        if title.width > 12.8:
            title.scale_to_fit_width(12.8)

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

        max_text_width = width - .35
        if text.width > max_text_width:
            text.scale_to_fit_width(max_text_width)

        text.move_to(rect)
        return VGroup(rect, text)

    def message(self, label):
        return self.box(
            label,
            width=1.35,
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
        return Arrow(
            source.get_right(),
            target.get_left(),
            buff=buff,
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=.14
        )

    def producer(self):
        return self.box(
            "PRODUCER",
            width=2.8,
            height=1.15,
            color=FG
        )

    def message_queue(self):
        return self.box(
            "MESSAGE QUEUE",
            width=3.3,
            height=1.25,
            color=ACCENT,
            font_size=23
        )

    def consumer(self, label="CONSUMER", color=FG):
        return self.box(
            label,
            width=2.8,
            height=1.05,
            color=color,
            font_size=22
        )


# ============================================================
# B00 — TRAFFIC BURST
# ============================================================

class B00_TrafficBurst(BrutalistScene):

    def construct(self):
        title = self.heading("WHEN TRAFFIC ARRIVES ALL AT ONCE")

        jobs = VGroup(*[
            self.message(f"JOB {i}")
            for i in range(1, 6)
        ]).arrange(DOWN, buff=.16)

        jobs.move_to(LEFT * 5.1)

        service = self.box(
            "SERVICE",
            width=3.0,
            height=1.25,
            color=FG
        ).move_to(RIGHT * 3.8)

        self.play(FadeIn(title), FadeIn(service), run_time=.7)

        self.play(
            LaggedStart(
                *[FadeIn(job) for job in jobs],
                lag_ratio=.10
            ),
            run_time=.8
        )

        arrows = VGroup(*[
            Arrow(
                job.get_right(),
                service.get_left(),
                buff=.15,
                color=BAD,
                stroke_width=3,
                max_tip_length_to_length_ratio=.12
            )
            for job in jobs
        ])

        self.play(
            LaggedStart(
                *[Create(a) for a in arrows],
                lag_ratio=.07
            ),
            run_time=1.2
        )

        spike = Text(
            "TRAFFIC SPIKE",
            font_size=27,
            color=BAD,
            weight=BOLD
        ).next_to(service, DOWN, buff=.5)

        self.play(FadeIn(spike), run_time=.5)

        cap = self.caption(
            "THOUSANDS OF JOBS CAN ARRIVE IN A SHORT BURST"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B01 — OVERLOAD
# ============================================================

class B01_ServiceOverload(BrutalistScene):

    def construct(self):
        title = self.heading("WORK ARRIVES FASTER THAN IT CAN FINISH")

        service = self.box(
            "SERVICE",
            width=3.1,
            height=1.3,
            color=BAD
        ).move_to(RIGHT * 4.3)

        backlog = VGroup(*[
            self.message(f"JOB {i}")
            for i in range(1, 6)
        ]).arrange(RIGHT, buff=.16)

        if backlog.width > 6.0:
            backlog.scale_to_fit_width(6.0)

        backlog.move_to(LEFT * 2.2)

        self.play(FadeIn(title), FadeIn(service), run_time=.7)

        self.play(
            LaggedStart(
                *[FadeIn(job) for job in backlog],
                lag_ratio=.10
            ),
            run_time=.9
        )

        overload = Text(
            "OVERLOADED",
            font_size=30,
            color=BAD,
            weight=BOLD
        ).next_to(service, DOWN, buff=.5)

        self.play(FadeIn(overload), run_time=.5)

        backlog_label = Text(
            "PENDING WORK",
            font_size=22,
            color=ACCENT,
            weight=BOLD
        ).next_to(backlog, DOWN, buff=.5)

        self.play(FadeIn(backlog_label), run_time=.4)

        cap = self.caption(
            "UNCONTROLLED BACKLOGS CAN INCREASE LATENCY AND FAILURES"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B02 — ADD MESSAGE QUEUE
# ============================================================

class B02_AddQueue(BrutalistScene):

    def construct(self):
        title = self.heading("ADD A MESSAGE QUEUE")

        producer = self.producer().move_to(LEFT * 4.8)
        queue = self.message_queue().move_to(ORIGIN)
        consumer = self.consumer().move_to(RIGHT * 4.8)

        self.play(
            FadeIn(title),
            FadeIn(producer),
            FadeIn(consumer),
            run_time=.7
        )

        self.play(FadeIn(queue), run_time=.6)

        a1 = self.edge_arrow(producer, queue)
        a2 = self.edge_arrow(queue, consumer)

        self.play(Create(a1), Create(a2), run_time=.9)

        cap = self.caption(
            "THE QUEUE BUFFERS WORK BETWEEN PRODUCERS AND CONSUMERS"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B03 — PRODUCERS PUBLISH
# ============================================================

class B03_PublishMessages(BrutalistScene):

    def construct(self):
        title = self.heading("PRODUCERS PUBLISH. THEN MOVE ON.")

        producer = self.producer().move_to(LEFT * 4.6)
        queue = self.message_queue().move_to(RIGHT * 2.7)

        self.play(
            FadeIn(title),
            FadeIn(producer),
            FadeIn(queue),
            run_time=.7
        )

        lane = self.edge_arrow(producer, queue, GOOD)
        self.play(Create(lane), run_time=.7)

        messages = VGroup(*[
            self.message(f"MSG {i}")
            for i in range(1, 4)
        ]).arrange(DOWN, buff=.18)

        messages.arrange(RIGHT, buff=.18)
        messages.move_to(
            (producer.get_right() + queue.get_left()) / 2 + UP * .75
        )

        self.play(
            LaggedStart(
                *[FadeIn(msg) for msg in messages],
                lag_ratio=.15
            ),
            run_time=.8
        )

        async_label = Text(
            "ASYNCHRONOUS",
            font_size=27,
            color=GOOD,
            weight=BOLD
        ).next_to(queue, DOWN, buff=.5)

        self.play(FadeIn(async_label), run_time=.5)

        cap = self.caption(
            "THE PRODUCER DOESN'T WAIT FOR DOWNSTREAM WORK TO FINISH"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B04 — CONTROLLED CONSUMPTION
# ============================================================

class B04_ControlledConsumption(BrutalistScene):

    def construct(self):
        title = self.heading("CONSUMERS PROCESS AT A SAFE RATE")

        queue = self.message_queue().move_to(LEFT * 3.6)
        consumer = self.consumer().move_to(RIGHT * 3.7)

        self.play(
            FadeIn(title),
            FadeIn(queue),
            FadeIn(consumer),
            run_time=.7
        )

        path = self.edge_arrow(queue, consumer, GOOD)
        self.play(Create(path), run_time=.7)

        messages = VGroup(
            self.message("MSG 1"),
            self.message("MSG 2"),
            self.message("MSG 3")
        ).arrange(RIGHT, buff=.18)

        messages.move_to(RIGHT * .45 + UP * .75)

        msg1, msg2, msg3 = messages

        self.play(FadeIn(msg1), run_time=.35)
        self.play(FadeIn(msg2), run_time=.35)
        self.play(FadeIn(msg3), run_time=.35)

        rate = Text(
            "CONTROLLED FLOW",
            font_size=27,
            color=GOOD,
            weight=BOLD
        ).next_to(consumer, DOWN, buff=.5)

        self.play(FadeIn(rate), run_time=.5)

        cap = self.caption(
            "QUEUED WORK CAN BE PROCESSED ACCORDING TO AVAILABLE CAPACITY"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B05 — ABSORB THE SPIKE
# ============================================================

class B05_AbsorbSpike(BrutalistScene):

    def construct(self):
        title = self.heading("LET THE QUEUE ABSORB THE SPIKE")

        queue = self.message_queue().move_to(LEFT * 2.3)
        consumer = self.consumer().move_to(RIGHT * 4.6)

        self.play(
            FadeIn(title),
            FadeIn(queue),
            FadeIn(consumer),
            run_time=.7
        )

        backlog = VGroup(*[
            self.message(f"M{i}")
            for i in range(1, 7)
        ]).arrange_in_grid(
            rows=2,
            cols=3,
            buff=(.16, .16)
        )

        backlog.scale(.52)

        queue_label = queue[1]
        queue_label.scale(.72)
        queue_label.move_to(queue.get_center() + UP * .38)

        backlog.move_to(queue.get_center() + DOWN * .20)

        self.play(
            LaggedStart(
                *[FadeIn(msg) for msg in backlog],
                lag_ratio=.08
            ),
            run_time=.9
        )

        path = self.edge_arrow(queue, consumer, GOOD)
        self.play(Create(path), run_time=.7)

        buffered = Text(
            "BACKLOG BUFFERED",
            font_size=25,
            color=ACCENT,
            weight=BOLD
        ).next_to(queue, DOWN, buff=.55)

        safe = Text(
            "STEADY INPUT",
            font_size=23,
            color=GOOD,
            weight=BOLD
        ).next_to(consumer, DOWN, buff=.55)

        self.play(FadeIn(buffered), FadeIn(safe), run_time=.6)

        cap = self.caption(
            "MESSAGES WAIT IN THE QUEUE INSTEAD OF ARRIVING ALL AT ONCE"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B06 — SCALE CONSUMERS
# ============================================================

class B06_ScaleConsumers(BrutalistScene):

    def construct(self):
        title = self.heading("ADD CONSUMERS AS WORKLOAD GROWS")

        queue = self.message_queue().move_to(LEFT * 3.9)

        c1 = self.consumer("CONSUMER 1").move_to(RIGHT * 4.2 + UP * 1.65)
        c2 = self.consumer("CONSUMER 2").move_to(RIGHT * 4.2)
        c3 = self.consumer("CONSUMER 3").move_to(RIGHT * 4.2 + DOWN * 1.65)

        self.play(
            FadeIn(title),
            FadeIn(queue),
            run_time=.7
        )

        self.play(
            FadeIn(c1),
            FadeIn(c2),
            FadeIn(c3),
            run_time=.7
        )

        # Separate direct connectors. They share the queue boundary,
        # but each terminates at a different consumer boundary.
        a1 = Arrow(
            queue.get_right() + UP * .34,
            c1.get_left(),
            buff=.15,
            color=GOOD,
            stroke_width=4,
            max_tip_length_to_length_ratio=.12
        )

        a2 = Arrow(
            queue.get_right(),
            c2.get_left(),
            buff=.15,
            color=GOOD,
            stroke_width=4,
            max_tip_length_to_length_ratio=.12
        )

        a3 = Arrow(
            queue.get_right() + DOWN * .34,
            c3.get_left(),
            buff=.15,
            color=GOOD,
            stroke_width=4,
            max_tip_length_to_length_ratio=.12
        )

        self.play(
            LaggedStart(
                Create(a1),
                Create(a2),
                Create(a3),
                lag_ratio=.15
            ),
            run_time=1.2
        )

        scale = Text(
            "MORE PROCESSING CAPACITY",
            font_size=26,
            color=GOOD,
            weight=BOLD
        ).move_to(DOWN * 2.65)

        self.play(FadeIn(scale), run_time=.5)

        cap = self.caption(
            "PARALLEL CONSUMERS CAN INCREASE THROUGHPUT"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(.8)


# ============================================================
# B07 — PAYOFF
# ============================================================

class B07_QueuePayoff(BrutalistScene):

    def construct(self):
        title = self.heading("BUFFER THE SPIKE. KEEP SERVICES RESPONSIVE.")

        producer = self.producer().move_to(LEFT * 5.0)
        queue = self.message_queue().move_to(ORIGIN)
        consumers = self.box(
            "CONSUMERS",
            width=3.0,
            height=1.15,
            color=FG
        ).move_to(RIGHT * 5.0)

        self.play(
            FadeIn(title),
            FadeIn(producer),
            FadeIn(queue),
            FadeIn(consumers),
            run_time=.8
        )

        a1 = self.edge_arrow(producer, queue, GOOD)
        a2 = self.edge_arrow(queue, consumers, GOOD)

        self.play(Create(a1), Create(a2), run_time=.9)

        benefits = VGroup(
            Text(
                "BUFFER SPIKES",
                font_size=22,
                color=GOOD,
                weight=BOLD
            ),
            Text(
                "DECOUPLE SERVICES",
                font_size=22,
                color=GOOD,
                weight=BOLD
            ),
            Text(
                "STAY RESPONSIVE",
                font_size=22,
                color=GOOD,
                weight=BOLD
            )
        ).arrange(RIGHT, buff=1.05)

        if benefits.width > 12.0:
            benefits.scale_to_fit_width(12.0)

        benefits.move_to(DOWN * 2.15)

        self.play(FadeIn(benefits), run_time=.7)

        cap = self.caption(
            "QUEUES SMOOTH BURSTS AND SEPARATE PRODUCERS FROM CONSUMERS"
        )

        self.play(FadeIn(cap), run_time=.5)
        self.wait(1)



