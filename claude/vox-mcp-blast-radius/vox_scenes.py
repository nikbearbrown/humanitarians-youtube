import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B02_ServerStreams(Scene):
    """Server icon with two output streams: TEAL read-only and CRIMSON write."""

    def construct(self):
        dur = DUR.get("B02", 14.0)

        # Server box (center-left)
        server_box = Rectangle(width=2.6, height=1.8)
        server_box.set_fill(SLATE, 0.3)
        server_box.set_stroke(SLATE, 2.5)
        server_box.move_to([-3.5, 0.5, 0.0])

        server_lbl = Text("MCP\nSERVER", font=SANS, font_size=18, color=TEAL)
        server_lbl.move_to([-3.5, 0.5, 0.0])

        self.play(FadeIn(server_box), run_time=0.4)
        self.play(FadeIn(server_lbl), run_time=0.3)

        # TEAL stream — read
        read_line = Line([-2.2, 1.0, 0.0], [1.5, 1.0, 0.0], stroke_width=3.0, color=TEAL)
        self.play(Create(read_line), run_time=0.4)

        read_box = Rectangle(width=2.8, height=0.8)
        read_box.set_fill(TEAL, 0.18)
        read_box.set_stroke(TEAL, 2)
        read_box.move_to([3.0, 1.0, 0.0])
        read_lbl = Text("READ (resource)", font=SANS, font_size=15, color=TEAL)
        read_lbl.move_to([3.0, 1.0, 0.0])

        self.play(FadeIn(read_box), run_time=0.3)
        self.play(FadeIn(read_lbl), run_time=0.3)

        # CRIMSON stream — write
        write_line = Line([-2.2, 0.0, 0.0], [1.5, 0.0, 0.0], stroke_width=3.0, color=CRIMSON)
        self.play(Create(write_line), run_time=0.4)

        write_box = Rectangle(width=2.8, height=0.8)
        write_box.set_fill(CRIMSON, 0.18)
        write_box.set_stroke(CRIMSON, 2.5)
        write_box.move_to([3.0, 0.0, 0.0])
        write_lbl = Text("WRITE (tool)", font=SANS, font_size=15, color=CRIMSON)
        write_lbl.move_to([3.0, 0.0, 0.0])

        self.play(FadeIn(write_box), run_time=0.3)
        self.play(FadeIn(write_lbl), run_time=0.3)

        # Ticket icon updated — CRIMSON ripple below write box
        ticket_box = Rectangle(width=2.0, height=0.6)
        ticket_box.set_fill(CRIMSON, 0.12)
        ticket_box.set_stroke(CRIMSON, 1.5)
        ticket_box.move_to([3.0, -0.9, 0.0])
        ticket_lbl = Text("TICKET UPDATED", font=SANS, font_size=13, color=CRIMSON)
        ticket_lbl.move_to([3.0, -0.9, 0.0])

        arr_down = Line([3.0, -0.4, 0.0], [3.0, -0.6, 0.0], stroke_width=2, color=CRIMSON)
        self.play(Create(arr_down), run_time=0.2)
        self.play(FadeIn(ticket_box), run_time=0.3)
        self.play(FadeIn(ticket_lbl), run_time=0.3)

        # Underline to distinguish server description from capability
        desc_line = Line([-5.0, -1.8, 0.0], [5.5, -1.8, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(desc_line), run_time=0.3)

        desc_note = Text("Server description: 'project management'", font=SANS, font_size=13, color=SLATE)
        desc_note.move_to([0.0, -2.3, 0.0])
        self.play(FadeIn(desc_note), run_time=0.3)

        self.wait(max(0.1, dur - 5.5))


class B04_ResourceVsTool(Scene):
    """Resource vs tool split from one server description — the key mechanism."""

    def construct(self):
        dur = DUR.get("B04", 20.0)

        # Server description banner at top
        desc_box = Rectangle(width=7.0, height=0.8)
        desc_box.set_fill(SLATE, 0.25)
        desc_box.set_stroke(SLATE, 2)
        desc_box.move_to([0.0, 2.8, 0.0])
        desc_lbl = Text("Server: 'project management integration'", font=SANS, font_size=16, color=TEAL)
        desc_lbl.move_to([0.0, 2.8, 0.0])

        self.play(FadeIn(desc_box), run_time=0.4)
        self.play(FadeIn(desc_lbl), run_time=0.3)

        # Split line from server box down
        split_line_left = Line([0.0, 2.4, 0.0], [-3.0, 1.4, 0.0], stroke_width=2, color=SLATE)
        split_line_right = Line([0.0, 2.4, 0.0], [3.0, 1.4, 0.0], stroke_width=2, color=SLATE)
        self.play(Create(split_line_left), run_time=0.3)
        self.play(Create(split_line_right), run_time=0.3)

        # Left column — RESOURCE (TEAL)
        res_header = Rectangle(width=3.5, height=0.7)
        res_header.set_fill(TEAL, 0.22)
        res_header.set_stroke(TEAL, 2.5)
        res_header.move_to([-3.0, 1.0, 0.0])
        res_hdr_lbl = Text("RESOURCE", font=DISPLAY, font_size=18, color=TEAL)
        res_hdr_lbl.move_to([-3.0, 1.0, 0.0])

        self.play(FadeIn(res_header), run_time=0.3)
        self.play(FadeIn(res_hdr_lbl), run_time=0.3)

        res_desc = Text("read-only\ndata fetch", font=SANS, font_size=14, color=TEAL)
        res_desc.move_to([-3.0, 0.2, 0.0])
        self.play(FadeIn(res_desc), run_time=0.3)

        # Read arrow
        read_arr = Line([-3.0, -0.3, 0.0], [-3.0, -0.8, 0.0], stroke_width=2.5, color=TEAL)
        self.play(Create(read_arr), run_time=0.2)

        read_note = Text("state unchanged", font=SANS, font_size=13, color=TEAL)
        read_note.move_to([-3.0, -1.1, 0.0])
        self.play(FadeIn(read_note), run_time=0.3)

        # Right column — TOOL (CRIMSON)
        tool_header = Rectangle(width=3.5, height=0.7)
        tool_header.set_fill(CRIMSON, 0.22)
        tool_header.set_stroke(CRIMSON, 2.5)
        tool_header.move_to([3.0, 1.0, 0.0])
        tool_hdr_lbl = Text("TOOL", font=DISPLAY, font_size=18, color=CRIMSON)
        tool_hdr_lbl.move_to([3.0, 1.0, 0.0])

        self.play(FadeIn(tool_header), run_time=0.3)
        self.play(FadeIn(tool_hdr_lbl), run_time=0.3)

        tool_desc = Text("callable function\nchanges external state", font=SANS, font_size=14, color=CRIMSON)
        tool_desc.move_to([3.0, 0.2, 0.0])
        self.play(FadeIn(tool_desc), run_time=0.3)

        # Write arrow with ripple
        write_arr = Line([3.0, -0.3, 0.0], [3.0, -0.8, 0.0], stroke_width=2.5, color=CRIMSON)
        self.play(Create(write_arr), run_time=0.2)

        write_note = Text("state changes", font=SANS, font_size=13, color=CRIMSON)
        write_note.move_to([3.0, -1.1, 0.0])
        self.play(FadeIn(write_note), run_time=0.3)

        # Bottom divider
        bottom_div = Line([-5.5, -1.7, 0.0], [5.5, -1.7, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(bottom_div), run_time=0.3)

        # "identical in manifest" note
        manifest_note = Text("Both appear as capability entries in the server manifest", font=SANS, font_size=13, color=SLATE)
        manifest_note.move_to([0.0, -2.2, 0.0])
        self.play(FadeIn(manifest_note), run_time=0.3)

        self.wait(max(0.1, dur - 6.5))


class B06_CalendarExample(Scene):
    """Calendar assistant: description hides create/delete tools, agent sends external invite."""

    def construct(self):
        dur = DUR.get("B06", 22.0)

        # Server box
        srv_box = Rectangle(width=2.8, height=1.6)
        srv_box.set_fill(SLATE, 0.25)
        srv_box.set_stroke(SLATE, 2)
        srv_box.move_to([-4.0, 1.5, 0.0])
        srv_lbl = Text("Calendar\nAssistant", font=SANS, font_size=16, color=TEAL)
        srv_lbl.move_to([-4.0, 1.5, 0.0])

        self.play(FadeIn(srv_box), run_time=0.4)
        self.play(FadeIn(srv_lbl), run_time=0.3)

        # Description label
        desc_chip = Rectangle(width=3.0, height=0.55)
        desc_chip.set_fill(SLATE, 0.15)
        desc_chip.set_stroke(SLATE, 1.5)
        desc_chip.move_to([-4.0, 0.4, 0.0])
        desc_chip_lbl = Text('"calendar access"', font=SANS, font_size=14, color=SLATE)
        desc_chip_lbl.move_to([-4.0, 0.4, 0.0])
        self.play(FadeIn(desc_chip), FadeIn(desc_chip_lbl), run_time=0.3)

        # Reveal capabilities below
        cap_title = Text("Actual capabilities:", font=SANS, font_size=13, color=SLATE)
        cap_title.move_to([-4.0, -0.3, 0.0])
        self.play(FadeIn(cap_title), run_time=0.3)

        # Read events (TEAL)
        read_box = Rectangle(width=2.6, height=0.5)
        read_box.set_fill(TEAL, 0.18)
        read_box.set_stroke(TEAL, 1.8)
        read_box.move_to([-4.0, -0.8, 0.0])
        read_lbl = Text("read events (resource)", font=SANS, font_size=12, color=TEAL)
        read_lbl.move_to([-4.0, -0.8, 0.0])
        self.play(FadeIn(read_box), run_time=0.3)
        self.play(FadeIn(read_lbl), run_time=0.3)

        # Create event (CRIMSON)
        create_box = Rectangle(width=2.6, height=0.5)
        create_box.set_fill(CRIMSON, 0.18)
        create_box.set_stroke(CRIMSON, 2)
        create_box.move_to([-4.0, -1.35, 0.0])
        create_lbl = Text("create event (tool)", font=SANS, font_size=12, color=CRIMSON)
        create_lbl.move_to([-4.0, -1.35, 0.0])
        self.play(FadeIn(create_box), run_time=0.3)
        self.play(FadeIn(create_lbl), run_time=0.3)

        # Delete event (CRIMSON)
        delete_box = Rectangle(width=2.6, height=0.5)
        delete_box.set_fill(CRIMSON, 0.18)
        delete_box.set_stroke(CRIMSON, 2)
        delete_box.move_to([-4.0, -1.9, 0.0])
        delete_lbl = Text("delete event (tool)", font=SANS, font_size=12, color=CRIMSON)
        delete_lbl.move_to([-4.0, -1.9, 0.0])
        self.play(FadeIn(delete_box), run_time=0.3)
        self.play(FadeIn(delete_lbl), run_time=0.3)

        # Agent acts: create-event path
        act_line = Line([-2.7, -1.35, 0.0], [0.5, -1.35, 0.0], stroke_width=2.5, color=CRIMSON)
        self.play(Create(act_line), run_time=0.4)

        # Three contact boxes to the right
        contact_xs = [2.0, 3.5, 5.0]
        contact_ys = [-0.6, -1.35, -2.1]
        for i in range(3):
            c_box = Rectangle(width=1.3, height=0.55)
            c_box.set_fill(CRIMSON, 0.15)
            c_box.set_stroke(CRIMSON, 1.8)
            c_box.move_to([contact_xs[i], contact_ys[i], 0.0])
            c_lbl = Text(f"Client {i+1}", font=SANS, font_size=12, color=CRIMSON)
            c_lbl.move_to([contact_xs[i], contact_ys[i], 0.0])
            self.play(FadeIn(c_box), run_time=0.25)
            self.play(FadeIn(c_lbl), run_time=0.2)

        # "INVITE SENT" label
        sent_lbl = Text("INVITE SENT", font=DISPLAY, font_size=20, color=CRIMSON)
        sent_lbl.move_to([3.5, 0.5, 0.0])
        self.play(FadeIn(sent_lbl), run_time=0.4)

        self.wait(max(0.1, dur - 7.0))


class B07_EvalColumns(Scene):
    """Two columns: description-only (CRIMSON) vs tool-list evaluation (TEAL)."""

    def construct(self):
        dur = DUR.get("B07", 20.0)

        # Divider
        div = Line([0.0, 3.0, 0.0], [0.0, -3.0, 0.0], stroke_width=1.5, color=SLATE)
        self.play(Create(div), run_time=0.3)

        # Left header
        lhdr = Text("Description-Only", font=DISPLAY, font_size=20, color=CRIMSON)
        lhdr.move_to([-3.0, 2.7, 0.0])
        self.play(FadeIn(lhdr), run_time=0.3)

        # Right header
        rhdr = Text("Tool-List Evaluation", font=DISPLAY, font_size=20, color=TEAL)
        rhdr.move_to([3.0, 2.7, 0.0])
        self.play(FadeIn(rhdr), run_time=0.3)

        # Left column content: one big box (broad access)
        lbox = Rectangle(width=4.5, height=2.5)
        lbox.set_fill(CRIMSON, 0.12)
        lbox.set_stroke(CRIMSON, 2)
        lbox.move_to([-3.0, 0.8, 0.0])
        llbl = Text("'calendar access'\n(all capabilities)", font=SANS, font_size=15, color=CRIMSON)
        llbl.move_to([-3.0, 0.8, 0.0])
        self.play(FadeIn(lbox), run_time=0.4)
        self.play(FadeIn(llbl), run_time=0.3)

        l_result = Text("FULL BLAST RADIUS", font=SANS, font_size=14, color=CRIMSON)
        l_result.move_to([-3.0, -1.0, 0.0])
        self.play(FadeIn(l_result), run_time=0.3)

        # Right column: three small boxes, one highlighted TEAL (read only needed)
        r1 = Rectangle(width=4.5, height=0.6)
        r1.set_fill(TEAL, 0.15)
        r1.set_stroke(TEAL, 1.8)
        r1.move_to([3.0, 1.8, 0.0])
        r1_lbl = Text("read events ← needed (resource)", font=SANS, font_size=12, color=TEAL)
        r1_lbl.move_to([3.0, 1.8, 0.0])
        self.play(FadeIn(r1), run_time=0.3)
        self.play(FadeIn(r1_lbl), run_time=0.3)

        r2 = Rectangle(width=4.5, height=0.6)
        r2.set_fill(CRIMSON, 0.12)
        r2.set_stroke(CRIMSON, 1.5)
        r2.move_to([3.0, 1.0, 0.0])
        r2_lbl = Text("create event — not needed (disable)", font=SANS, font_size=12, color=CRIMSON)
        r2_lbl.move_to([3.0, 1.0, 0.0])
        self.play(FadeIn(r2), run_time=0.3)
        self.play(FadeIn(r2_lbl), run_time=0.3)

        r3 = Rectangle(width=4.5, height=0.6)
        r3.set_fill(CRIMSON, 0.12)
        r3.set_stroke(CRIMSON, 1.5)
        r3.move_to([3.0, 0.2, 0.0])
        r3_lbl = Text("delete event — not needed (disable)", font=SANS, font_size=12, color=CRIMSON)
        r3_lbl.move_to([3.0, 0.2, 0.0])
        self.play(FadeIn(r3), run_time=0.3)
        self.play(FadeIn(r3_lbl), run_time=0.3)

        r_result = Text("MINIMUM SURFACE", font=SANS, font_size=14, color=TEAL)
        r_result.move_to([3.0, -1.0, 0.0])
        self.play(FadeIn(r_result), run_time=0.3)

        # Bottom separator
        bot_sep = Line([-5.5, -1.7, 0.0], [5.5, -1.7, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(bot_sep), run_time=0.3)

        # Accent tick on divider (distinct 7th state)
        div_tick = Line([0.0, 0.6, 0.0], [0.0, 0.0, 0.0], stroke_width=3.5, color=TEAL)
        self.play(Create(div_tick), run_time=0.25)

        self.wait(max(0.1, dur - 6.8))


class B08_McpChecklist(Scene):
    """Three TEAL chips for MCP evaluation checklist."""

    def construct(self):
        dur = DUR.get("B08", 16.0)

        # Title
        title = Text("Before connecting any MCP server:", font=DISPLAY, font_size=22, color=TEAL)
        title.move_to([0.0, 2.8, 0.0])
        self.play(FadeIn(title), run_time=0.4)

        steps = [
            ("1", "Open the tool list, not just the description"),
            ("2", "Label each capability: read-only or write"),
            ("3", "Disable write tools the task does not need"),
        ]

        chip_ys = [1.5, 0.3, -0.9]

        for i, (num, text) in enumerate(steps):
            y = chip_ys[i]

            num_circ = Circle(radius=0.36)
            num_circ.set_fill(TEAL, 0.35)
            num_circ.set_stroke(TEAL, 2)
            num_circ.move_to([-4.2, y, 0.0])

            num_lbl = Text(num, font=DISPLAY, font_size=22, color=TEAL)
            num_lbl.move_to([-4.2, y, 0.0])

            chip_box = Rectangle(width=7.8, height=0.72)
            chip_box.set_fill(TEAL, 0.1)
            chip_box.set_stroke(TEAL, 1.5)
            chip_box.move_to([0.7, y, 0.0])

            step_lbl = Text(text, font=SANS, font_size=17, color=TEAL)
            step_lbl.move_to([0.7, y, 0.0])

            self.play(FadeIn(num_circ), FadeIn(num_lbl), run_time=0.3)
            self.play(FadeIn(chip_box), FadeIn(step_lbl), run_time=0.35)

        # Separator
        sep = Line([-5.5, -1.9, 0.0], [5.5, -1.9, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(sep), run_time=0.3)

        note = Text("The surface is not the description — it is the full list of what can change.", font=SANS, font_size=14, color=SLATE)
        note.move_to([0.0, -2.5, 0.0])
        self.play(FadeIn(note), run_time=0.4)

        self.wait(max(0.1, dur - 5.0))
