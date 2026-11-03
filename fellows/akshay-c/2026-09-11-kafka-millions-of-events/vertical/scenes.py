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
        self.title("DIRECT FAN-OUT: ONE SLOW SERVICE BECOMES EVERYONE'S PROBLEM")
        api=self.box("ORDER API",4.4,1.0,ACCENT).shift(UP*3.7)
        names=["INVENTORY","FRAUD","ANALYTICS","EMAIL","BILLING"]
        svcs=VGroup(*[self.box(n,4.2,.78) for n in names]).arrange(DOWN,buff=.34).shift(DOWN*1.15)
        self.play(FadeIn(api),FadeIn(svcs),run_time=4)
        # Route fan-out through a clean left-side trunk.
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
        self.play(LaggedStart(*[Create(x) for x in branches], lag_ratio=.12), run_time=2)
        fraud=svcs[1]; slow=Text("SLOW",font_size=28,color=BAD).next_to(fraud,RIGHT,buff=.18)
        self.play(fraud[0].animate.set_stroke(BAD),FadeIn(slow),run_time=3)
        q=VGroup(*[self.event(str(i)) for i in range(8)]).arrange_in_grid(rows=2,cols=4,buff=(.12,.12)).move_to(UP*2.15)
        self.play(LaggedStart(*[FadeIn(x) for x in q],lag_ratio=.08),run_time=4)
        warn=VGroup(Text("LATENCY â†‘",font_size=29,color=BAD),Text("TIMEOUTS â†‘",font_size=29,color=BAD),Text("COUPLING â†‘",font_size=29,color=BAD)).arrange(DOWN,buff=.16).to_edge(DOWN,buff=.75)
        self.play(FadeIn(warn),run_time=2); self.wait(3)

class B02_DurableLog(BrutalistScene):
    def construct(self):
        self.title("KAFKA PUTS A DURABLE LOG BETWEEN PRODUCERS AND CONSUMERS")
        prod=self.box("PRODUCERS",4.3,.9,ACCENT).shift(UP*4.0)
        log=Rectangle(width=6.8,height=3.0,stroke_color=FG,stroke_width=3).shift(UP*.65)
        topic=Text("TOPIC: orders",font_size=28,color=FG,weight=BOLD).next_to(log,UP,buff=.22)
        retain=Text("retained ordered records",font_size=23,color=MUTED).next_to(log,DOWN,buff=.18)
        row1=VGroup(*[self.event(str(i)) for i in range(6)]).arrange(RIGHT,buff=.18)
        row2=VGroup(*[self.event(str(i)) for i in range(6,12)]).arrange(RIGHT,buff=.18)
        cells=VGroup(row1,row2).arrange(DOWN,buff=.34).move_to(log)
        cons=VGroup(self.box("FAST CONSUMER",4.2,.78,GOOD),self.box("SLOW CONSUMER",4.2,.78,BAD)).arrange(DOWN,buff=.45).shift(DOWN*4.0)
        self.play(FadeIn(prod),FadeIn(log),FadeIn(topic),FadeIn(retain),FadeIn(cons),run_time=4)
        self.play(LaggedStart(*[FadeIn(c) for c in row1],*[FadeIn(c) for c in row2],lag_ratio=.06),run_time=5)
        self.play(Create(Arrow(prod.get_bottom(),log.get_top(),buff=.2,color=MUTED)),run_time=4)
        fast_arrow = Arrow(
            log.get_bottom(),
            cons[0].get_top(),
            buff=.18,
            color=GOOD
        )

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

        self.play(Create(fast_arrow), Create(slow_route), run_time=2)
        self.wait(4.5)

class B03_Partitions(BrutalistScene):
    def construct(self):
        self.title("PARTITIONS TURN ONE TOPIC INTO PARALLEL ORDERED LANES")
        lanes=VGroup(*[Rectangle(width=6.6,height=1.0,stroke_color=FG,stroke_width=2) for _ in range(6)]).arrange(DOWN,buff=.30).shift(DOWN*.35)
        labels=VGroup(*[Text(f"P{i}",font_size=25,color=ACCENT).next_to(lanes[i],LEFT,buff=.18) for i in range(6)])
        self.play(FadeIn(lanes),FadeIn(labels),run_time=3)
        keys=["A1","B1","C1","A2","B2","D1","A3","C2"]; dest=[0,1,2,0,1,4,0,2]
        events=VGroup(*[self.event(k) for k in keys]).arrange_in_grid(rows=2,cols=4,buff=(.18,.18)).shift(UP*4.25)
        self.play(FadeIn(events),run_time=3)
        counts={}; targets=[]
        for d in dest:
            idx=counts.get(d,0); counts[d]=idx+1
            targets.append(lanes[d].get_left()+RIGHT*(1.0+1.05*idx))
        self.play(*[events[i].animate.move_to(targets[i]) for i in range(len(events))],run_time=6)
        note=VGroup(Text("ORDER IS GUARANTEED",font_size=27,color=FG,weight=BOLD),Text("within a partition",font_size=27,color=ACCENT),Text("not across the whole topic",font_size=24,color=FG)).arrange(DOWN,buff=.14).to_edge(DOWN,buff=.75)
        self.play(FadeIn(note),run_time=3); self.wait(4.5)

class B05_Brokers(BrutalistScene):
    def construct(self):
        self.title("BROKERS DISTRIBUTE PARTITION LEADERSHIP ACROSS MACHINES")
        brokers=VGroup()
        for i in range(3):
            rect=Rectangle(width=5.4,height=2.45,stroke_color=FG,stroke_width=3)
            label=Text(f"BROKER {i+1}",font_size=27,color=FG,weight=BOLD)
            label.move_to(rect.get_top()+DOWN*.38)
            brokers.add(VGroup(rect,label))
        brokers.arrange(DOWN,buff=.55).shift(DOWN*.25)
        self.play(FadeIn(brokers),run_time=3)
        mapping=[["P0 leader","P3 leader"],["P1 leader","P4 leader"],["P2 leader","P5 leader"]]
        for b,ps in zip(brokers,mapping):
            cards=VGroup(*[self.box(p,2.15,.65,ACCENT,22) for p in ps]).arrange(RIGHT,buff=.35)
            cards.move_to(b[0].get_center()+DOWN*.48)
            self.play(FadeIn(cards),run_time=3)
        foot=VGroup(Text("STORAGE + NETWORK",font_size=28,color=GOOD,weight=BOLD),Text("reads + writes spread horizontally",font_size=24,color=FG)).arrange(DOWN,buff=.12).to_edge(DOWN,buff=.75)
        self.play(FadeIn(foot),run_time=3); self.wait(4.5)

class B06_ConsumerGroups(BrutalistScene):
    def construct(self):
        self.title("CONSUMER GROUPS DIVIDE PARTITIONS INTO PARALLEL WORK")
        parts=VGroup(*[self.box(f"P{i}",1.55,.62,ACCENT,23) for i in range(6)]).arrange(DOWN,buff=.22).shift(LEFT*2.65+UP*.3)
        consumers=VGroup(*[self.box(f"C{i+1}",1.75,.62,GOOD,23) for i in range(7)]).arrange(DOWN,buff=.18).shift(RIGHT*2.55+UP*.3)
        self.play(FadeIn(parts),FadeIn(consumers),run_time=4)
        lines=VGroup(*[Line(parts[i].get_right(),consumers[i].get_left(),color=MUTED) for i in range(6)])
        self.play(Create(lines),run_time=5)
        idle=Text("IDLE",font_size=23,color=BAD).next_to(consumers[6],RIGHT,buff=.16)
        self.play(FadeIn(idle),run_time=2)
        rule=VGroup(Text("ONE PARTITION",font_size=28,color=ACCENT,weight=BOLD),Text("â†’ at most one active consumer",font_size=25,color=FG),Text("inside one consumer group",font_size=23,color=MUTED)).arrange(DOWN,buff=.13).to_edge(DOWN,buff=.75)
        self.play(FadeIn(rule),run_time=3); self.wait(6)

class B07_Offsets(BrutalistScene):
    def construct(self):
        self.title("OFFSETS TRACK PROGRESS - AND ENABLE RESTARTS OR REPLAY")
        log_box=Rectangle(width=6.7,height=5.0,stroke_color=FG,stroke_width=3).shift(UP*.65)
        log_label=Text("PARTITION LOG",font_size=28,color=FG,weight=BOLD).next_to(log_box,UP,buff=.2)
        cells=VGroup(*[self.event(str(i)) for i in range(100,109)]).arrange_in_grid(rows=3,cols=3,buff=(.42,.42)).scale(1.28).move_to(log_box)
        self.play(Create(log_box),FadeIn(log_label),FadeIn(cells),run_time=4)
        marker=Triangle(fill_color=ACCENT,fill_opacity=1,stroke_width=0).scale(.22).rotate(PI).next_to(cells[5],UP,buff=.16)
        lab=Text("next offset: 105",font_size=29,color=ACCENT).move_to(DOWN*2.25)
        self.play(FadeIn(marker),FadeIn(lab),run_time=3)
        crash_box=RoundedRectangle(width=5.5,height=1.0,corner_radius=.08,stroke_color=BAD,stroke_width=3).shift(DOWN*3.25)
        crash=Text("CONSUMER CRASHES",font_size=29,color=BAD,weight=BOLD).move_to(crash_box)
        self.play(FadeIn(crash_box),FadeIn(crash),run_time=2); self.play(FadeOut(crash_box),FadeOut(crash),run_time=2)
        restart_box=RoundedRectangle(width=6.5,height=1.15,corner_radius=.08,stroke_color=GOOD,stroke_width=3).shift(DOWN*3.25)
        restart=VGroup(Text("RESTART",font_size=27,color=GOOD,weight=BOLD),Text("resume from committed progress",font_size=22,color=GOOD)).arrange(DOWN,buff=.08).move_to(restart_box)
        self.play(FadeIn(restart_box),FadeIn(restart),run_time=3)
        new_lab=Text("rewind to 102 â†’ replay",font_size=28,color=ACCENT).move_to(DOWN*2.25)
        self.play(marker.animate.next_to(cells[2],UP,buff=.16),Transform(lab,new_lab),run_time=5); self.wait(9)

class B09_Rebalance(BrutalistScene):
    def construct(self):
        self.title("WHEN A CONSUMER DIES, THE GROUP REBALANCES")
        parts=VGroup(*[self.box(f"P{i}",1.5,.62,ACCENT,23) for i in range(6)]).arrange(DOWN,buff=.28).shift(LEFT*2.7+UP*.45)
        cs=VGroup(*[self.box(f"C{i+1}",1.9,.78,GOOD,24) for i in range(4)]).arrange(DOWN,buff=.75).shift(RIGHT*2.55+UP*.45)
        self.play(FadeIn(parts),FadeIn(cs),run_time=3)
        pairs=[(0,0),(1,0),(2,1),(3,1),(4,2),(5,3)]
        lines=VGroup(*[Line(parts[p].get_right(),cs[c].get_left(),color=MUTED) for p,c in pairs]); self.play(Create(lines),run_time=4)
        self.play(cs[1][0].animate.set_stroke(BAD),cs[1][1].animate.set_color(BAD),run_time=2)
        self.play(FadeOut(cs[1]),FadeOut(lines[2]),FadeOut(lines[3]),run_time=2)
        rb=RoundedRectangle(width=5.3,height=1.0,corner_radius=.08,stroke_color=ACCENT,stroke_width=3)
        rt=Text("REBALANCING",font_size=34,color=ACCENT,weight=BOLD).move_to(rb)
        rg=VGroup(rb,rt).shift(DOWN*3.7)
        self.play(FadeIn(rg),run_time=2); self.play(FadeOut(rg),run_time=2)
        self.play(Create(Line(parts[2].get_right(),cs[0].get_left(),color=GOOD)),Create(Line(parts[3].get_right(),cs[2].get_left(),color=GOOD)),run_time=3)
        self.wait(3.5)

class B10_Replication(BrutalistScene):
    def construct(self):
        self.title("REPLICATION GIVES A PARTITION FAILOVER OPTIONS")
        names=["BROKER A","BROKER B","BROKER C"]; brokers=VGroup()
        for name in names:
            rect=Rectangle(width=5.5,height=2.55,stroke_color=FG,stroke_width=3)
            label=Text(name,font_size=27,color=FG,weight=BOLD).move_to(rect.get_top()+DOWN*.38)
            brokers.add(VGroup(rect,label))
        brokers.arrange(DOWN,buff=.55).shift(DOWN*.25); self.play(FadeIn(brokers),run_time=4)
        reps=VGroup(self.box("P0 LEADER",2.7,.72,ACCENT,23),self.box("P0 REPLICA",2.7,.72,GOOD,23),self.box("P0 REPLICA",2.7,.72,GOOD,23))
        for role,broker in zip(reps,brokers): role.move_to(broker[0].get_center()+DOWN*.42)
        self.play(FadeIn(reps),run_time=3)
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
            replication_route(reps[1], reps[2])
        )

        self.play(Create(arrows), run_time=4)
        self.play(brokers[0][0].animate.set_stroke(BAD),FadeOut(reps[0]),run_time=3)
        promoted=self.box("P0 NEW LEADER",3.0,.72,ACCENT,22).move_to(reps[1])
        self.play(Transform(reps[1],promoted),run_time=4); self.wait(5)

class B11_FullScale(BrutalistScene):
    def construct(self):
        self.title("SCALE COMES FROM DISTRIBUTING THE LOG AND THE WORK")
        producers=self.box("MANY PRODUCERS",5.0,1.0,ACCENT).shift(UP*4.4)
        brokers=VGroup(*[self.box(f"BROKER {i+1}",2.6,1.25,FG,23) for i in range(4)]).arrange_in_grid(rows=2,cols=2,buff=(.45,.45)).shift(UP*.5)
        groups=VGroup(self.box("GROUP A - 6 WORKERS",5.0,1.0,GOOD,23),self.box("GROUP B - 4 WORKERS",5.0,1.0,GOOD,23)).arrange(DOWN,buff=.45).shift(DOWN*3.0)
        self.play(FadeIn(producers),FadeIn(brokers),FadeIn(groups),run_time=4)
        self.play(Create(Arrow(producers.get_bottom(),brokers.get_top(),color=ACCENT,buff=.25)),Create(Arrow(brokers.get_bottom(),groups.get_top(),color=GOOD,buff=.25)),run_time=4)
        counter=Text("10,000 events",font_size=38,color=FG).to_edge(DOWN,buff=.65); self.play(FadeIn(counter),run_time=2)
        for txt in ["100,000 events","1,000,000+ events"]:
            self.play(Transform(counter,Text(txt,font_size=38,color=ACCENT).to_edge(DOWN,buff=.65)),run_time=3)
        self.wait(6)

class B12_Tradeoffs(BrutalistScene):
    def construct(self):
        self.title("KAFKA SCALES BY PARTITIONING WORK - LIMITS STILL EXIST")
        cards=VGroup(
            self.box("TOO FEW\nPARTITIONS",5.4,1.55,BAD,25),
            self.box("TOO MANY\nPARTITIONS",5.4,1.55,BAD,25),
            self.box("HOT KEY",5.4,1.55,BAD,25),
            self.box("CONSUMER LAG",5.4,1.55,BAD,25)
        ).arrange(DOWN,buff=.42).shift(DOWN*.15)
        self.play(LaggedStart(*[FadeIn(c) for c in cards],lag_ratio=.35),run_time=8)
        notes=VGroup(Text("CAPACITY PLANNING STILL MATTERS",font_size=26,color=FG,weight=BOLD),Text("disk Â· network Â· retention Â· replication",font_size=22,color=MUTED)).arrange(DOWN,buff=.12).to_edge(DOWN,buff=.7)
        self.play(FadeIn(notes),run_time=3); self.wait(10)
