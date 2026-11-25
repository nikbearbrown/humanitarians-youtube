extends SceneTree

# Scripted-input capture driver for Delta (film evidence, not a playtest).
#   godot --path <capture copy> --fixed-fps 30 --script res://harness/capture_driver.gd -- <take> <out> [nosave] [seed=N]
# Plays only through Input.parse_input_event (keys, mouse, joypad). It reads game
# state to decide what to press and to assert outcomes; it never writes game
# state, never calls game methods and never teleports.

const FPS := 30.0
const W := 3840
const H := 2160
const CHUNK := 150

var take := ""
var out_dir := ""
var frame := 0
var log_file: FileAccess
var failed := false
var mouse := Vector2(1180, 690)      ## logical (1280x720) viewport coordinates
var mouse_idle := 999
var ring := 0.0
var overlay: Node2D
var held := {}                       ## physical keycode -> true while held
var fire_held := false
var segment := ""
var stats := {}
var nosave := false
var rng_seed := -1
var chunk_file: FileAccess
var chunk_index := 0

class CursorOverlay extends Node2D:
	var driver
	func _process(_d: float) -> void:
		queue_redraw()
	func _draw() -> void:
		# The OS cursor is not part of the viewport texture, so the driver draws its own.
		# It fades out after 2 s without mouse movement.
		var a: float = clampf(1.0 - (driver.mouse_idle - 60) / 15.0, 0.0, 1.0)
		if a <= 0.0:
			return
		var p: Vector2 = driver.mouse
		if driver.ring > 0.0:
			var t: float = 1.0 - driver.ring
			draw_arc(p, 6.0 + 16.0 * t, 0.0, TAU, 32, Color(1.0, 0.76, 0.24, 1.0 - t), 2.5)
		var arrow := PackedVector2Array([p, p + Vector2(0, 17), p + Vector2(4.5, 13),
			p + Vector2(8, 20), p + Vector2(10.5, 19), p + Vector2(7, 12), p + Vector2(12.5, 12)])
		draw_colored_polygon(arrow, Color(1, 1, 1, a))
		var outline := arrow.duplicate()
		outline.append(p)
		draw_polyline(outline, Color(0.08, 0.08, 0.08, a), 1.4, true)

func _initialize() -> void:
	var args := OS.get_cmdline_user_args()
	take = args[0]
	out_dir = args[1]
	for a in args.slice(2):
		if a == "nosave":
			nosave = true
		elif a.begins_with("seed="):
			rng_seed = int(a.get_slice("=", 1))
	DirAccess.make_dir_recursive_absolute(out_dir + "/frames")
	log_file = FileAccess.open(out_dir + "/inputs.jsonl", FileAccess.WRITE)
	if not nosave:
		DisplayServer.window_set_size(Vector2i(W, H))
	if rng_seed >= 0:
		seed(rng_seed)    # the global RNG the game draws from; disclosed in CAPTURE.md
	var layer := CanvasLayer.new()
	layer.layer = 128
	root.add_child(layer)
	overlay = CursorOverlay.new()
	overlay.driver = self
	layer.add_child(overlay)
	RenderingServer.frame_post_draw.connect(_save_frame)
	change_scene_to_file(ProjectSettings.get_setting("application/run/main_scene"))
	note("boot", {"take": take, "seed": rng_seed, "main_scene": ProjectSettings.get_setting("application/run/main_scene"),
		"engine": Engine.get_version_info().string})
	call_deferred("run")

func _tick() -> void:
	frame += 1
	iterations_since_draw = 0
	mouse_idle += 1
	ring = maxf(0.0, ring - 1.0 / 12.0)

func _save_frame() -> void:
	if nosave:
		return
	var img := root.get_texture().get_image()
	if img.get_width() != W or img.get_height() != H:
		if frame == 0:
			note("viewport_size", {"w": img.get_width(), "h": img.get_height()})
		img.resize(W, H, Image.INTERPOLATE_BILINEAR)
	img.convert(Image.FORMAT_RGB8)
	if chunk_file == null:
		_throttle()
		chunk_file = FileAccess.open("%s/frames/%05d.raw" % [out_dir, chunk_index], FileAccess.WRITE)
	chunk_file.store_buffer(img.get_data())
	if (frame + 1) % CHUNK == 0:
		_close_chunk()
	_tick()

## Watchdog: macOS stops drawing an occluded window while game logic keeps running.
## If no frame is drawn for 60 iterations, the take is aborted as a failure.
var iterations_since_draw := 0
var draw_stalled := false
func _process(_delta: float) -> bool:
	if nosave:
		_tick()
		return false
	iterations_since_draw += 1
	if iterations_since_draw > 60 and not draw_stalled:
		draw_stalled = true
		note("draw_stalled", {"at_frame": frame})
		failed = true
		_close_chunk()
		FileAccess.open(out_dir + "/frames/DONE", FileAccess.WRITE).store_line(str(frame))
		quit(3)
	return false

func _close_chunk() -> void:
	if chunk_file == null:
		return
	chunk_file.close()
	chunk_file = null
	FileAccess.open("%s/frames/%05d.ready" % [out_dir, chunk_index], FileAccess.WRITE).store_line("ok")
	chunk_index += 1

## Wait (wall-clock only; the game clock is fixed per frame) if the encoder falls behind.
func _throttle() -> void:
	while true:
		var pending := 0
		for f in DirAccess.get_files_at(out_dir + "/frames"):
			if f.ends_with(".raw"):
				pending += 1
		if pending < 2:
			return
		OS.delay_msec(200)

# --- observation (read-only) ---

func scene() -> Node:
	return current_scene

func scene_name() -> String:
	return String(current_scene.name) if current_scene else ""

func level() -> Node:
	var s := current_scene
	return s if s and s.get("level_id") != null else null

func player() -> CharacterBody3D:
	var l := level()
	return l.player if l else null

func snapshot() -> Dictionary:
	var d := {"scene": scene_name(), "paused": paused, "mouse_captured": Input.mouse_mode == Input.MOUSE_MODE_CAPTURED}
	var l := level()
	if l:
		d["level"] = l.level_id
		d["dim"] = l.current_dim
		d["completed"] = l.completed
		d["game_paused"] = l.paused
		var p: CharacterBody3D = l.player
		if is_instance_valid(p):
			var g := p.global_position
			d["pos"] = [snappedf(g.x, 0.1), snappedf(g.y, 0.1), snappedf(g.z, 0.1)]
			d["yaw"] = snappedf(rad_to_deg(p.rotation.y), 0.1)
			d["held"] = p.held.kind if p.held else ""
			d["dead"] = p.dead
		if l.final_logic:
			d["shield_up"] = l.final_logic.shield_up
			d["wave_hit"] = l.final_logic.wave_hit
			d["overcharged"] = l.final_logic.overcharged
	var gs := root.get_node_or_null("GameState")
	if gs:
		d["unlocked"] = gs.unlocked_level
	return d

func note(event: String, detail: Dictionary = {}) -> void:
	var line := {"frame": frame, "t": snappedf(frame / FPS, 0.001), "event": event, "detail": detail,
		"game": snapshot() if current_scene else {}}
	log_file.store_line(JSON.stringify(line))
	log_file.flush()
	if event != "key_down" and event != "key_up":
		print(JSON.stringify(line))

func mark(name: String) -> void:
	segment = name
	note("segment", {"name": name})

func expect(ok: bool, label: String) -> void:
	note("assert", {"label": label, "pass": ok})
	if not ok:
		failed = true

func wait(n: int) -> void:
	for i in range(n):
		await process_frame

func wait_until(cond: Callable, max_frames: int, label: String) -> bool:
	var n := 0
	while not cond.call() and n < max_frames:
		await process_frame
		n += 1
	var ok: bool = cond.call()
	expect(ok, "wait_until " + label)
	return ok

# --- input, only through events ---

func to_window(p: Vector2) -> Vector2:
	return root.get_final_transform() * p

func _motion(p: Vector2) -> void:
	var ev := InputEventMouseMotion.new()
	ev.relative = to_window(p) - to_window(mouse)
	mouse = p
	mouse_idle = 0
	ev.position = to_window(p)
	ev.global_position = ev.position
	if fire_held:
		ev.button_mask = MOUSE_BUTTON_MASK_LEFT
	Input.parse_input_event(ev)

func move(p: Vector2, frames: int = 18) -> void:
	var start := mouse
	for i in range(1, frames + 1):
		var t := float(i) / float(frames)
		t = t * t * (3.0 - 2.0 * t)
		_motion(start.lerp(p, t))
		await process_frame

func _button(button: MouseButton, pressed: bool) -> void:
	var ev := InputEventMouseButton.new()
	ev.button_index = button
	ev.pressed = pressed
	ev.position = to_window(mouse)
	ev.global_position = ev.position
	if pressed:
		ev.button_mask = MOUSE_BUTTON_MASK_LEFT
	mouse_idle = 0
	Input.parse_input_event(ev)

func click(p: Vector2, label: String, travel: int = 18) -> void:
	await move(p, travel)
	await wait(6)
	var hov: Control = root.gui_get_hovered_control()
	note("click", {"button": "left", "on": label, "logical": [snappedf(p.x, 0.1), snappedf(p.y, 0.1)],
		"under_mouse": (hov.get_class() + ":" + (hov.text if hov is Button else String(hov.name))) if hov else ""})
	ring = 1.0
	_button(MOUSE_BUTTON_LEFT, true)
	await process_frame
	_button(MOUSE_BUTTON_LEFT, false)
	await process_frame

func _key_event(code: Key, pressed: bool) -> void:
	var ev := InputEventKey.new()
	ev.physical_keycode = code
	ev.keycode = code
	ev.pressed = pressed
	Input.parse_input_event(ev)

func key(code: Key, label: String) -> void:
	note("key", {"key": label})
	_key_event(code, true)
	await process_frame
	_key_event(code, false)
	await process_frame

func hold(code: Key, label: String) -> void:
	if held.has(code):
		return
	held[code] = label
	note("key_down", {"key": label})
	_key_event(code, true)

func release(code: Key, label: String = "") -> void:
	if not held.has(code):
		return
	note("key_up", {"key": held[code]})
	held.erase(code)
	_key_event(code, false)

func release_all() -> void:
	_set_stick(Vector2.ZERO)
	for code in held.keys():
		held.erase(code)
		_key_event(code, false)
	if fire_held:
		set_fire(false)
	note("release_all")

func set_fire(on: bool) -> void:
	if on == fire_held:
		return
	fire_held = on
	note("mouse_down" if on else "mouse_up", {"button": "left"})
	_button(MOUSE_BUTTON_LEFT, on)

func joy_axis(axis: JoyAxis, value: float, label: String) -> void:
	note("joy_axis", {"axis": label, "value": snappedf(value, 0.01)})
	var ev := InputEventJoypadMotion.new()
	ev.device = 0
	ev.axis = axis
	ev.axis_value = value
	Input.parse_input_event(ev)

func joy_button(button: JoyButton, pressed: bool, label: String) -> void:
	note("joy_button", {"button": label, "pressed": pressed})
	var ev := InputEventJoypadButton.new()
	ev.device = 0
	ev.button_index = button
	ev.pressed = pressed
	ev.pressure = 1.0 if pressed else 0.0
	Input.parse_input_event(ev)

## Turn the view by (yaw, pitch) degrees this frame. In a captured window this is real
## mouse motion; headless (no mouse capture possible) it is the gamepad right stick, at
## the same rate: both are capped at 5 degrees a frame (150 degrees a second).
const MOUSE_SCALE := 0.11
const MAX_TURN := 5.0
var stick := Vector2.ZERO
var look_mode := ""
func turn(yaw: float, pitch: float) -> void:
	yaw = clampf(yaw, -MAX_TURN, MAX_TURN)
	pitch = clampf(pitch, -MAX_TURN, MAX_TURN)
	var sens: float = root.get_node("GameState").sensitivity
	if Input.mouse_mode == Input.MOUSE_MODE_CAPTURED and not nosave:
		_set_stick(Vector2.ZERO)
		if absf(yaw) < 0.01 and absf(pitch) < 0.01:
			return
		if look_mode != "mouse":
			look_mode = "mouse"
			note("look_input", {"via": "mouse"})
		var ev := InputEventMouseMotion.new()
		ev.relative = Vector2(-yaw, -pitch) / (MOUSE_SCALE * sens)
		ev.position = to_window(Vector2(640, 360))
		ev.global_position = ev.position
		Input.parse_input_event(ev)
	else:
		if look_mode != "stick":
			look_mode = "stick"
			note("look_input", {"via": "right stick"})
		var r := Vector2(-yaw, -pitch) / (MAX_TURN * sens)
		var l := r.length()
		if l < 0.002:
			_set_stick(Vector2.ZERO)
		else:
			_set_stick(r / l * minf(1.0, 0.2 + 0.8 * l))

func _set_stick(v: Vector2) -> void:
	if v.is_equal_approx(stick):
		return
	stick = v
	for pair in [[JOY_AXIS_RIGHT_X, v.x], [JOY_AXIS_RIGHT_Y, v.y]]:
		var ev := InputEventJoypadMotion.new()
		ev.device = 0
		ev.axis = pair[0]
		ev.axis_value = pair[1]
		Input.parse_input_event(ev)

func find_button(text: String) -> Button:
	return _find_button(root, text)

func _find_button(n: Node, text: String) -> Button:
	if n is Button and n.text.begins_with(text) and n.is_visible_in_tree():
		return n
	for c in n.get_children():
		var b := _find_button(c, text)
		if b:
			return b
	return null

func press_button(text: String, travel: int = 22) -> void:
	var b := find_button(text)
	expect(b != null, "button visible: " + text)
	if b == null:
		var seen := []
		_visible_buttons(root, seen)
		note("buttons_seen", {"texts": seen})
	if b:
		await click(b.get_global_rect().get_center(), text, travel)

func finish() -> void:
	release_all()
	await wait(4)
	note("end", {"failed": failed, "stats": stats})
	log_file.close()
	RenderingServer.frame_post_draw.disconnect(_save_frame)
	_close_chunk()
	if not nosave:
		FileAccess.open(out_dir + "/frames/DONE", FileAccess.WRITE).store_line(str(frame))
	quit(1 if failed else 0)

func _visible_buttons(n: Node, out: Array) -> void:
	if n is Button and n.is_visible_in_tree():
		out.append(n.text)
	for c in n.get_children():
		_visible_buttons(c, out)

# --- Delta takes -------------------------------------------------------------
# The level solutions follow the game's own playtest (_tools/playtest.gd), but every
# action here is an input event: W A S D (held), mouse motion or the right stick (look),
# F (pick up / drop), E (use), Q (shift), Space (jump), mouse clicks on menus.
# Grid helpers below re-read the level's own map data; they do not call level methods.

const CELL := 5.0
const DIM_Y := {"a": 50.0, "b": 0.0, "f": 200.0}

var moving := {}            # "W","A","S","D" -> true while the driver holds it
var guard_note := ""

func lv() -> Node:
	return level()

func pl() -> CharacterBody3D:
	return player()

func dim() -> String:
	return lv().current_dim

# ---------------------------------------------------------------- map (read-only)

func char_at(key: String, cell: Vector2i) -> String:
	var rows: Array = lv().dims[key]["map"]
	if cell.y < 0 or cell.y >= rows.size():
		return " "
	var row: String = rows[cell.y]
	if cell.x < 0 or cell.x >= row.length():
		return " "
	return row[cell.x]

func entities_for(ch: String) -> Array:
	var legend: Dictionary = lv().data.get("legend", {})
	if legend.has(ch):
		var entry = legend[ch]
		return entry if entry is Array else [entry]
	if ch == "@":
		return [{"type": "start"}]
	if ch == "G":
		return [{"type": "goal"}]
	return []

func walkable(key: String, cell: Vector2i) -> bool:
	var ch := char_at(key, cell)
	if ch in [" ", ".", "o", "_", "~"]:
		return ch in [".", "o"]
	var list := entities_for(ch)
	var t: String = "." if list.is_empty() else list[0].get("floor", ".")
	return t in [".", "o"]

func cell_center(key: String, cell: Vector2i) -> Vector3:
	return Vector3(cell.x * CELL, DIM_Y[key], cell.y * CELL)

func world_to_cell(p: Vector3) -> Vector2i:
	return Vector2i(roundi(p.x / CELL), roundi(p.z / CELL))

func find_char(key: String, ch: String) -> Vector2i:
	var rows: Array = lv().dims[key]["map"]
	for r in rows.size():
		var c: int = (rows[r] as String).find(ch)
		if c >= 0:
			return Vector2i(c, r)
	return Vector2i(-1, -1)

func cell_of(ch: String, key := "") -> Vector2i:
	return find_char(key if key != "" else dim(), ch)

func pos_of(ch: String, key := "") -> Vector3:
	var k := key if key != "" else dim()
	return cell_center(k, find_char(k, ch))

func device_at(type: String, ch: String, key := "") -> Node:
	var k := key if key != "" else dim()
	var c := find_char(k, ch)
	for id in lv().devices:
		var d: Node = lv().devices[id]
		if d.name == "%s_%s_%d_%d" % [type, k, c.x, c.y]:
			return d
	return null

func item_near(p: Vector3, kind: String) -> Node:
	var best: Node = null
	for item in lv().items:
		if item.kind == kind and item.holder != pl():
			if best == null or item.global_position.distance_to(p) < best.global_position.distance_to(p):
				best = item
	return best

func _blocked(key: String, cell: Vector2i) -> bool:
	var center := cell_center(key, cell)
	for item in lv().items:
		if item.holder == null and item.global_position.distance_to(center + Vector3(0, 0.4, 0)) < 1.3:
			return true
	for e in entities_for(char_at(key, cell)):
		var t: String = e.get("type", "")
		if t in ["generator", "deco", "duplicator", "plasma", "console", "vault", "shield_generator", "stabilizer"]:
			return true
		if t in ["socket", "charger", "discharger"] and not e.has("at"):
			return true
	return false

func _path(from: Vector2i, to: Vector2i) -> Array:
	var key := dim()
	var prev := {from: from}
	var queue := [from]
	while not queue.is_empty():
		var c: Vector2i = queue.pop_front()
		if c == to:
			break
		for d in [Vector2i(1, 0), Vector2i(-1, 0), Vector2i(0, 1), Vector2i(0, -1)]:
			var n: Vector2i = c + d
			if prev.has(n) or not walkable(key, n):
				continue
			if n != to and _blocked(key, n):
				continue
			prev[n] = c
			queue.append(n)
	if not prev.has(to):
		return []
	var out := []
	var c := to
	while c != from:
		out.push_front(c)
		c = prev[c]
	return out

func _free(spot: Vector3) -> bool:
	var params := PhysicsShapeQueryParameters3D.new()
	var capsule := CapsuleShape3D.new()
	capsule.radius = 0.45
	capsule.height = 1.7
	params.shape = capsule
	params.transform = Transform3D(Basis.IDENTITY, spot + Vector3(0, 0.95, 0))
	params.collision_mask = 1 | 4
	var exclude: Array[RID] = [pl().get_rid()]
	if pl().held:
		exclude.append(pl().held.get_rid())
	params.exclude = exclude
	return pl().get_world_3d().direct_space_state.intersect_shape(params, 1).is_empty()

# ---------------------------------------------------------------- frame step + guard

## One frame. Before it, the guard reacts to the final level's guardians: it jumps a
## shockwave ring as it reaches Gino and backs out of a locked strike.
func step() -> void:
	_guard()
	await process_frame

var _escaping := false
func _guard() -> void:
	var l := lv()
	if l == null or l.final_logic == null:
		return
	var fl: Node = l.final_logic
	var p := pl()
	if fl.wave != null and is_instance_valid(fl.wave) and fl.wave_dim == l.current_dim and not fl.wave_hit:
		var flat: Vector3 = p.global_position - fl.wave.global_position
		flat.y = 0.0
		var gap: float = flat.length() - fl.wave_radius
		if gap > 0.0 and gap < 3.1 and p.is_on_floor():
			if guard_note != "jump":
				note("guard", {"action": "jump the shockwave", "gap": snappedf(gap, 0.01)})
				guard_note = "jump"
			_key_event(KEY_SPACE, true)
			_space_down = 2
	if _space_down > 0:
		_space_down -= 1
		if _space_down == 0:
			_key_event(KEY_SPACE, false)
	_escaping = false
	if fl.spark != null and is_instance_valid(fl.spark) and fl.spark_locked and fl.spark_dim == l.current_dim and not lure_hold:
		var away: Vector3 = p.global_position - fl.spark.global_position
		away.y = 0.0
		if away.length() < 3.7:
			_escaping = true
			if guard_note != "escape":
				_escape_to = _escape_spot(fl.spark.global_position)
				note("guard", {"action": "get clear of the locked strike", "dist": snappedf(away.length(), 0.01),
					"to": [snappedf(_escape_to.x, 0.1), snappedf(_escape_to.z, 0.1)]})
				guard_note = "escape"
			var dir: Vector3 = _escape_to - p.global_position
			dir.y = 0.0
			_move_dir(dir.normalized() if dir.length() > 0.2 else away.normalized())
	if not _escaping and guard_note == "escape":
		guard_note = ""
		set_move(Vector2.ZERO)

var _space_down := 0
var _escape_to := Vector3.ZERO

## A spot 4.6 m from the strike with free floor all the way there, nearest Gino's heading.
func _escape_spot(center: Vector3) -> Vector3:
	var p := pl()
	var key := dim()
	var best := center + Vector3(4.6, 0, 0)
	var best_score := -INF
	for i in 24:
		var ang := i * TAU / 24.0
		var dir := Vector3(cos(ang), 0, sin(ang))
		var ok := true
		for k in range(1, 8):
			var q := center + dir * (k * 0.66)
			q.y = DIM_Y[key]
			if not walkable(key, world_to_cell(q)) or not _free(q):
				ok = false
				break
		if not ok:
			continue
		var from_me: Vector3 = (center + dir * 4.6) - p.global_position
		var score := -from_me.length()
		if score > best_score:
			best_score = score
			best = center + dir * 4.6
	best.y = DIM_Y[key]
	return best
var lure_hold := false

## Hold the W A S D keys that move Gino along a world direction (8-way, relative to his yaw).
func _move_dir(world: Vector3) -> void:
	var b: Basis = pl().global_basis
	var local := Vector2(world.dot(b.x), world.dot(b.z))
	var v := Vector2(0 if absf(local.x) < 0.38 else signf(local.x), 0 if absf(local.y) < 0.38 else signf(local.y))
	set_move(v)

## v.x: -1 A, +1 D; v.y: -1 W, +1 S.
func set_move(v: Vector2) -> void:
	for pair in [["W", KEY_W, v.y < 0], ["S", KEY_S, v.y > 0], ["A", KEY_A, v.x < 0], ["D", KEY_D, v.x > 0]]:
		var on: bool = pair[2]
		if on and not moving.has(pair[0]):
			moving[pair[0]] = true
			hold(pair[1], pair[0])
		elif not on and moving.has(pair[0]):
			moving.erase(pair[0])
			release(pair[1])

func frames(n: int) -> void:
	for i in n:
		await step()

func until(cond: Callable, seconds: float) -> bool:
	var n := int(seconds * FPS)
	while not cond.call() and n > 0:
		await step()
		n -= 1
	return cond.call()

# ---------------------------------------------------------------- looking and walking

func _wrap(a: float) -> float:
	return wrapf(a, -180.0, 180.0)

func _yaw_to(point: Vector3) -> float:
	var d := point - pl().global_position
	return rad_to_deg(atan2(-d.x, -d.z))

func _pitch_to(point: Vector3) -> float:
	var eye: Vector3 = pl().head.global_position
	var d := point - eye
	return rad_to_deg(atan2(d.y, Vector2(d.x, d.z).length()))

## Turn toward a point (yaw and pitch) at the capped look rate until within 1 degree.
func look(point: Vector3, max_frames := 60) -> void:
	for i in max_frames:
		var dy := _wrap(_yaw_to(point) - rad_to_deg(pl().rotation.y))
		var dp: float = _pitch_to(point) - pl()._pitch
		if absf(dy) < 0.8 and absf(dp) < 0.8:
			turn(dy, dp)
			await step()
			break
		turn(dy, dp)
		await step()
	turn(0, 0)
	await frames(2)

func _speed() -> float:
	var v: Vector3 = pl().velocity
	return Vector2(v.x, v.z).length()

func steer(point: Vector3, tol: float) -> String:
	var best := INF
	var stuck := 0
	var detours := 0
	while true:
		var p := pl()
		if lv().completed or (lv().final_logic and lv().final_logic.ended):
			set_move(Vector2.ZERO)
			turn(0, 0)
			return ""
		if p.dead:
			set_move(Vector2.ZERO)
			return "player died"
		if _escaping:
			await step()
			continue
		var d := point - p.global_position
		d.y = 0
		var dist := d.length()
		var dy := _wrap(_yaw_to(point) - rad_to_deg(p.rotation.y))
		var dp: float = -8.0 - p._pitch
		turn(dy if dist > 0.25 else 0.0, dp)
		if dist < tol and _speed() < 0.6:
			set_move(Vector2.ZERO)
			turn(0, 0)
			return ""
		var brake := tol * 0.6 + 0.11 * _speed()
		if dist > brake and absf(dy) < 40.0:
			set_move(Vector2(0, -1))
		else:
			set_move(Vector2.ZERO)
		await step()
		if dist < best - 0.05:
			best = dist
			stuck = 0
		else:
			stuck += 1
			if stuck > 45:
				detours += 1
				if detours > 6:
					set_move(Vector2.ZERO)
					return "stuck at %s going to %s" % [p.global_position.snapped(Vector3.ONE * 0.1), point.snapped(Vector3.ONE * 0.1)]
				note("detour", {"n": detours})
				var side := 1.0 if detours % 2 == 1 else -1.0
				set_move(Vector2(side, 1))
				await frames(12)
				set_move(Vector2(side, -1))
				await frames(15)
				set_move(Vector2.ZERO)
				stuck = 0
				best = INF
	return ""

func walk(target: Vector3, tol := 0.35) -> String:
	var key := dim()
	var start := world_to_cell(pl().global_position)
	var goal := world_to_cell(target)
	var cells := _path(start, goal)
	if cells.is_empty() and start != goal:
		return "no path from %s to %s in %s" % [start, goal, key]
	var points := []
	for i in cells.size() - 1:
		points.append(cell_center(key, cells[i]))
	points.append(target)
	for i in points.size():
		var err: String = await steer(points[i], tol if i == points.size() - 1 else 1.0)
		if err != "":
			return err
		if lv().completed:
			return ""
	return ""

func approach(target: Vector3, distance: float) -> String:
	var key := dim()
	var best := Vector3.INF
	var best_d := INF
	for i in 16:
		var ang := i * TAU / 16.0
		var spot := target + Vector3(cos(ang), 0, sin(ang)) * distance
		spot.y = DIM_Y[key]
		if not walkable(key, world_to_cell(spot)) or not _free(spot):
			continue
		var d := spot.distance_to(pl().global_position)
		if d < best_d:
			best_d = d
			best = spot
	if best == Vector3.INF:
		return "nowhere to stand near %s" % target.snapped(Vector3.ONE * 0.1)
	return await walk(best, 0.3)

# ---------------------------------------------------------------- actions (keys)

## What the crosshair ray hits (the same 3 m ray the game uses), read-only.
func aimed() -> Object:
	var p := pl()
	var cam: Camera3D = p.camera
	var origin := cam.global_position
	var q := PhysicsRayQueryParameters3D.create(origin, origin - cam.global_basis.z * 3.0, 1 | 4 | 8)
	var ex: Array[RID] = [p.get_rid()]
	if p.held:
		ex.append(p.held.get_rid())
	q.exclude = ex
	var hit := p.get_world_3d().direct_space_state.intersect_ray(q)
	if hit.is_empty():
		return null
	var c: Object = hit.collider
	if c.has_meta("interactable"):
		return c.get_meta("interactable")
	return c

func pick(item: Node) -> String:
	if item == null:
		return "no item to pick up"
	var err: String = await approach(item.global_position, 1.5)
	if err != "":
		return err
	await look(item.global_position)
	if aimed() != item:
		await look(item.global_position + Vector3(0, 0.15, 0))
	await key(KEY_F, "F")
	await frames(12)
	return "" if pl().held == item else "pickup failed for %s" % item.kind

func use(device: Node, eye_height := 0.9, distance := 1.9) -> String:
	if device == null:
		return "device missing"
	var err: String = await approach(device.global_position, distance)
	if err != "":
		return err
	await look(device.global_position + Vector3(0, eye_height, 0))
	if aimed() != device:
		for dh in [0.3, -0.3, 0.6]:
			await look(device.global_position + Vector3(0, eye_height + dh, 0), 20)
			if aimed() == device:
				break
	if aimed() != device:
		note("aim_miss", {"device": String(device.name)})
	await key(KEY_E, "E")
	await frames(24)
	return ""

func drop_on(target: Vector3) -> String:
	var err: String = await approach(target, 1.4)
	if err != "":
		return err
	await look(target + Vector3(0, 0.6, 0))
	await frames(24)
	await key(KEY_F, "F")
	await frames(30)
	return ""

func shift() -> String:
	var from := dim()
	await key(KEY_Q, "Q")
	await frames(27)
	return "" if dim() != from else "shift refused at %s" % pl().global_position.snapped(Vector3.ONE * 0.1)

func ride(platform: Node, from_cell: Vector2i, to_cell: Vector2i) -> String:
	var start: Vector3 = platform.global_position + platform.start_pos
	var end_pos: Vector3 = platform.global_position + platform.end_pos
	var err: String = await walk(cell_center(dim(), from_cell))
	if err != "":
		return err
	if not await until(func(): return platform.body.global_position.distance_to(start) < 0.3, 30.0):
		return "platform never came"
	var t := 0
	var exit_point := cell_center(dim(), to_cell)
	var aboard := false
	while platform.body.global_position.distance_to(end_pos) > 0.6:
		var deck: Vector3 = platform.body.global_position
		var d: Vector3 = deck - pl().global_position
		d.y = 0
		if not aboard and d.length() < 1.0 and pl().is_on_floor():
			aboard = true
			note("ride", {"aboard": true})
		var aim := exit_point if aboard else deck
		var dy := _wrap(_yaw_to(aim) - rad_to_deg(pl().rotation.y))
		turn(dy, -8.0 - pl()._pitch)
		if aboard:
			# Gino creeps ahead of a moving deck (see CAPTURE.md): stay near its middle
			if d.length() > 0.9:
				_move_dir(d)
			elif d.length() < 0.4:
				set_move(Vector2.ZERO)
		else:
			set_move(Vector2(0, -1) if d.length() > 0.7 and absf(dy) < 40.0 else Vector2.ZERO)
		await step()
		t += 1
		if t % 6 == 0:
			note("ride_dbg", {"deck": [snappedf(deck.x, 0.01), snappedf(deck.y, 0.01), snappedf(deck.z, 0.01)], "floor": pl().is_on_floor(), "vel": [snappedf(pl().velocity.x, 0.01), snappedf(pl().velocity.z, 0.01)]})
		if t > 40 * 30 or pl().global_position.y < deck.y - 3.0:
			set_move(Vector2.ZERO)
			return "fell off or missed the platform"
	return await steer(exit_point, 0.5)

func charge_at(charger: Node, discharge := false) -> String:
	var err: String = await use(charger)
	if err != "":
		return err
	var cell: Node = charger.held
	if cell == null:
		return "charger did not take the cell"
	var done := func(): return cell.is_empty() if discharge else cell.is_full()
	if not await until(done, 8.0):
		return "cell did not %s" % ("discharge" if discharge else "charge")
	await frames(9)
	err = await use(charger)
	return err if err != "" else ("" if pl().held == cell else "could not take the cell back")

func chain(steps: Array) -> String:
	for i in steps.size():
		var err: String = await steps[i].call()
		if err != "":
			return "step %d: %s" % [i + 1, err]
	return ""

# ---------------------------------------------------------------- level solutions

func level_1() -> String:
	return await chain([
		func(): return await pick(item_near(pos_of("c"), "cell")),
		func(): return await use(device_at("socket", "S")),
		func(): return "" if lv().devices["d1"].is_open else "door d1 did not open",
		func(): return await walk(pos_of("G")),
	])

func level_2() -> String:
	return await chain([
		func(): return await walk(cell_center("a", Vector2i(4, 2))),
		func(): return await shift(),
		func(): return await walk(cell_center("b", Vector2i(8, 2))),
		func(): return await shift(),
		func(): return await walk(pos_of("G")),
	])

func level_3() -> String:
	return await chain([
		func(): return await pick(item_near(pos_of("e"), "cell")),
		func(): return await charge_at(device_at("charger", "C")),
		func(): return await use(device_at("socket", "S")),
		func(): return "" if lv().devices["d1"].is_open else "door d1 did not open",
		func(): return await walk(pos_of("G")),
	])

func level_4() -> String:
	return await chain([
		func(): return await pick(item_near(pos_of("x"), "crate")),
		func(): return await drop_on(pos_of("P")),
		func(): return "" if lv().devices["d1"].is_open else "pad P did not open d1",
		func(): return await walk(pos_of("D") + Vector3(0, 0, 3.0)),
		func(): return await pick(item_near(pos_of("y"), "crate")),
		func(): return await drop_on(pos_of("Q")),
		func(): return await pick(item_near(pos_of("f"), "cell")),
		func(): return await drop_on(pos_of("R")),
		func(): return "" if lv().devices["d2"].is_open else "pads Q and R did not open d2",
		func(): return await walk(pos_of("G")),
	])

func level_5() -> String:
	var gate := pos_of("A")
	return await chain([
		func(): return await pick(item_near(pos_of("c"), "cell")),
		func():
			var err: String = await walk(gate + Vector3(0, 0, -3.0))
			if err != "":
				return err
			await steer(gate + Vector3(0, 0, 2.5), 0.4)
			set_move(Vector2.ZERO)
			await frames(15)
			return "" if pl().held == null else "the gate let a charged cell through",
		func(): return await walk(gate + Vector3(0, 0, -3.5)),
		func(): return await pick(item_near(pl().global_position, "cell")),
		func(): return await charge_at(device_at("discharger", "X"), true),
		func(): return await walk(gate + Vector3(0, 0, 3.0)),
		func(): return "" if pl().held != null else "lost the empty cell at the gate",
		func(): return await charge_at(device_at("charger", "C")),
		func(): return await use(device_at("socket", "S")),
		func(): return await walk(pos_of("G")),
	])

func level_6() -> String:
	return await chain([
		func(): return await pick(item_near(pos_of("c"), "cell")),
		func(): return await use(device_at("socket", "S"), 0.9, 2.0),
		func():
			await frames(105)
			var err: String = await walk(cell_center("a", Vector2i(3, 5)))
			if err != "":
				return err
			return await steer(pos_of("k"), 0.4),
		func(): return await ride(lv().devices[device_at("platform", "M").id], Vector2i(4, 8), Vector2i(8, 8)),
		func(): return await walk(pos_of("G")),
	])

func level_7() -> String:
	return await chain([
		func(): return await pick(item_near(pos_of("c"), "cell")),
		func(): return await walk(cell_center("a", Vector2i(3, 2))),
		func(): return await shift(),
		func(): return await use(device_at("socket", "S", "b")),
		func(): return await walk(cell_center("b", Vector2i(3, 2))),
		func(): return await shift(),
		func(): return "" if lv().devices["d1"].is_open else "socket in Lower Delta did not open d1",
		func(): return await walk(cell_center("a", Vector2i(4, 5))),
		func(): return await shift(),
		func(): return await walk(cell_center("b", Vector2i(4, 7))),
		func(): return await shift(),
		func(): return await walk(pos_of("G")),
	])

func level_8() -> String:
	var dup: Node = lv().devices["u1"]
	return await chain([
		func(): return await pick(item_near(pos_of("c"), "cell")),
		func(): return await use(dup, 0.35, 1.9),
		func(): return "" if dup.held != null else "duplicator did not take the cell",
		func(): return await use(device_at("button", "b"), 1.1, 1.5),
		func(): return "" if dup.last_clone != null else "no clone made",
		func(): return await use(dup, 0.35, 1.9),
		func(): return await use(device_at("socket", "S")),
		func(): return await pick(dup.last_clone),
		func(): return await use(device_at("socket", "T")),
		func(): return "" if lv().devices["d1"].is_open else "two sockets did not open d1",
		func(): return await walk(pos_of("G")),
	])

func level_9() -> String:
	return await chain([
		func(): return await use(lv().devices[device_at("console", "K").id], 1.0, 1.9),
		func(): return await use(device_at("button", "b"), 1.1, 1.5),
		func(): return await pick(item_near(pos_of("y"), "cell")),
		func(): return await use(device_at("socket", "S")),
		func(): return "" if lv().devices["d1"].is_open else "door did not open",
		func(): return await walk(pos_of("G")),
	])

func level_10() -> String:
	return await chain([
		func(): return await pick(item_near(pos_of("e"), "cell")),
		func(): return await walk(cell_center("a", Vector2i(3, 2))),
		func(): return await shift(),
		func(): return await charge_at(device_at("charger", "C", "b")),
		func(): return await ride(device_at("platform", "M", "b"), Vector2i(4, 3), Vector2i(4, 6)),
		func(): return await shift(),
		func(): return await use(device_at("socket", "S")),
		func(): return await walk(pos_of("G")),
	])

func level_11() -> String:
	var core := item_near(pos_of("k"), "core")
	return await chain([
		func(): return await pick(core),
		func():
			note("deliberate", {"what": "shift while holding the unstable core"})
			await key(KEY_Q, "Q")
			await frames(90)
			return "" if dim() == "a" and pl().held == null and core.global_position.distance_to(core.spawn_position) < 0.8 else "core did not explode and respawn",
		func(): return await pick(item_near(pos_of("c"), "cell")),
		func(): return await walk(cell_center("a", Vector2i(6, 2))),
		func(): return await shift(),
		func(): return await use(device_at("socket", "S", "b")),
		func(): return await walk(cell_center("b", Vector2i(6, 2))),
		func(): return await shift(),
		func(): return await pick(core),
		func(): return await walk(pos_of("G")),
	])

func level_12() -> String:
	var fl: Node = lv().final_logic
	return await chain([
		func(): return await pick(item_near(pos_of("c"), "cell")),
		func(): return await use(device_at("socket", "g")),
		func(): return "" if fl.overcharged == 1 else "generator 1 did not overcharge",
		func(): return await walk(cell_center("a", Vector2i(7, 7))),
		func(): return await shift(),
		func(): return await pick(item_near(pos_of("z", "b"), "cell")),
		func(): return await charge_at(device_at("charger", "C", "b")),
		func(): return await use(device_at("socket", "h", "b")),
		func(): return "" if fl.overcharged == 2 else "generator 2 did not overcharge",
		func(): return await walk(cell_center("b", Vector2i(11, 5))),
		func(): return await shift(),
		func(): return await lure_strike(fl),
		func(): return await pick(item_near(pos_of("K"), "core")),
		func():
			var err: String = await walk(pos_of("F"))
			if dim() == "f" or err == "":
				return ""
			return err,
		func():
			await until(func(): return dim() == "f", 3.0)
			return "" if dim() == "f" else "final stage trigger did not fire",
		func():
			await frames(20)
			await steer(pos_of("X", "f"), 0.3)
			set_move(Vector2.ZERO)
			await frames(30)
			return "" if fl.ended else "stabiliser did not accept the core",
	])

## Stand beside the shield generator until a guardian strike locks on Gino there, then
## get clear: the lightning destroys the generator. Shockwaves meanwhile are jumped.
func lure_strike(fl: Node) -> String:
	var spot: Vector3 = fl.shield_generator.global_position + Vector3(-1.6, 0, -1.2)
	var err: String = await walk(spot, 0.4)
	if err != "":
		return err
	note("lure", {"what": "waiting beside the shield generator for a strike"})
	var waited := 0
	while fl.shield_up and waited < 70 * 30:
		var locked: bool = fl.spark != null and is_instance_valid(fl.spark) and fl.spark_locked
		if not locked and pl().global_position.distance_to(spot) > 0.8 and not _escaping:
			lure_hold = true
			await steer(spot, 0.4)
			lure_hold = false
		await step()
		waited += 1
	if fl.shield_up:
		return "no strike destroyed the shield generator"
	await frames(15)
	return ""

# ---------------------------------------------------------------- takes

func run() -> void:
	await wait_until(func(): return scene_name() == "MainMenu", 120, "main menu loaded")
	await wait(30)
	match take:
		"campaign1":
			await take_campaign(1, 6, true)
		"campaign2":
			await take_campaign(7, 12, false)
		"defeat":
			await take_defeat()
		"extras":
			await take_extras()
		"only":
			await take_only()
	await finish()

func play_level(id: int) -> bool:
	await wait_until(func(): return lv() != null and lv().level_id == id and pl() != null, 240, "level %d loaded" % id)
	mark("level%d" % id)
	await frames(45)
	var err: String = await call("level_%d" % id)
	set_move(Vector2.ZERO)
	turn(0, 0)
	if err != "":
		note("level_error", {"level": id, "error": err})
	var done: bool = (id < 12 and lv() != null and lv().completed) or (id == 12 and lv() != null and lv().final_logic.ended)
	expect(done and err == "", "level %d solved" % id)
	return done

func take_campaign(first: int, last: int, from_new: bool) -> void:
	mark("menu")
	if from_new:
		await press_button("How to play")
		await wait_until(func(): return scene_name() == "Instructions", 60, "How to Play opens")
		await wait(150)
		await press_button("Back")
		await wait_until(func(): return scene_name() == "MainMenu", 60, "back to the main menu")
		await wait(30)
		await press_button("New game")
	else:
		await press_button("Continue")
	for id in range(first, last + 1):
		if not await play_level(id):
			return
		if id < last:
			await wait(75)
			await press_button("Continue")
	if last < 12:
		await wait(75)
		await press_button("Main menu")
		await wait_until(func(): return scene_name() == "MainMenu", 60, "back to the main menu")
		await wait(45)
		return
	# level 12: the ending, then the credits, then the menu
	await wait_until(func(): return scene_name() == "Credits", 60 * 30, "ending plays, then the credits")
	mark("credits")
	await wait_until(func(): return scene_name() == "MainMenu", 150 * 30, "credits return to the main menu")
	await wait(60)

## Trial helper: play one level from Select level (headless only).
func take_only() -> void:
	var id := int(OS.get_environment("ONLY_LEVEL"))
	await press_button("Select level")
	await wait(10)
	await press_button("%02d" % id)
	await play_level(id)

func select_level(id: int) -> void:
	await press_button("Select level")
	await wait(40)
	await press_button("%02d" % id)

func pause_menu_open() -> bool:
	return lv() != null and lv().paused

func take_defeat() -> void:
	mark("select7")
	await select_level(7)
	await wait_until(func(): return lv() != null and lv().level_id == 7 and pl() != null, 240, "level 7 loaded")
	await frames(45)
	# a refused shift: Lower Delta has no floor under this spot
	mark("shift_refused")
	await walk(cell_center("a", Vector2i(1, 2)))
	await look(pl().global_position + Vector3(-3, 1.2, 0))
	var before := dim()
	await key(KEY_Q, "Q")
	await frames(40)
	expect(dim() == before, "shift refused where the other layer has no floor")
	# open the door from Lower Delta, as in the campaign, then walk into the plasma
	mark("plasma")
	var err: String = await chain([
		func(): return await pick(item_near(pos_of("c"), "cell")),
		func(): return await walk(cell_center("a", Vector2i(3, 2))),
		func(): return await shift(),
		func(): return await use(device_at("socket", "S", "b")),
		func(): return await walk(cell_center("b", Vector2i(3, 2))),
		func(): return await shift(),
		func(): return await walk(cell_center("a", Vector2i(4, 5))),
	])
	expect(err == "", "door opened before the plasma (%s)" % err)
	note("deliberate", {"what": "walk into the plasma ball"})
	await steer(pos_of("P", "a"), 0.2)
	await wait_until(func(): return pl() == null or pl().dead, 90, "plasma is fatal")
	await wait_until(func(): return lv() != null and lv().level_id == 7 and pl() != null and not pl().dead, 150, "level restarts after the death")
	await frames(60)
	# pause menu: options, resume, R restart, N skip. Mouse clicks on the pause menu do not
	# reach its buttons (a full-screen container for the options panel sits on top of them),
	# so after showing one click, the take uses the keyboard: arrows and Enter.
	mark("pause")
	await key(KEY_ESCAPE, "Esc")
	await wait_until(pause_menu_open, 20, "Esc pauses")
	await wait(30)
	note("deliberate", {"what": "click Resume with the mouse"})
	await press_button("Resume")
	await wait(30)
	expect(pause_menu_open(), "a mouse click on Resume does not register (still paused)")
	await menu_keys(3)
	await wait(70)
	await press_button("Back")
	await wait(30)
	await menu_keys(0)
	await wait_until(func(): return not pause_menu_open(), 20, "Enter on Resume unpauses")
	await frames(40)
	# R, N and Esc are meant to work while paused, but the level node pauses with the
	# tree and never sees them. Shown once, then the menu entries are used instead.
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	var lvl_before := lv()
	note("deliberate", {"what": "press R while paused"})
	await key(KEY_R, "R")
	await wait(45)
	expect(lv() == lvl_before and pause_menu_open(), "R while paused does nothing (still paused, same level)")
	await menu_keys(1)
	await wait_until(func(): return lv() != null and lv() != lvl_before and lv().level_id == 7, 90, "Restart level restarts it")
	await frames(60)
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	await menu_keys(2)
	await wait_until(func(): return lv() != null and lv().level_id == 8, 120, "Skip level loads level 8")
	await frames(60)
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	await menu_keys(4)
	await wait_until(func(): return scene_name() == "MainMenu", 90, "back to the main menu")
	await wait(30)
	# falling: a cell thrown off the deck returns home, and so does Gino
	mark("falls")
	await select_level(6)
	await wait_until(func(): return lv() != null and lv().level_id == 6 and pl() != null, 240, "level 6 loaded")
	await frames(45)
	var cell := item_near(pos_of("c"), "cell")
	await pick(cell)
	# the bridge is still retracted: cell (3, 6) is open space
	await walk(cell_center("a", Vector2i(3, 5)))
	await steer(cell_center("a", Vector2i(3, 5)) + Vector3(0, 0, 1.6), 0.3)
	await look(cell_center("a", Vector2i(3, 5)) + Vector3(0, -2.0, 6.0))
	note("deliberate", {"what": "drop the cell into the gap"})
	await key(KEY_F, "F")
	await wait_until(func(): return cell.holder == null and cell.global_position.y < 40.0, 90, "the cell falls")
	await wait_until(func(): return cell.global_position.distance_to(cell.spawn_position) < 0.8, 240, "a fallen cell returns to its spawn point")
	await frames(30)
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	await menu_keys(4)
	await wait_until(func(): return scene_name() == "MainMenu", 90, "back to the main menu")
	await wait(30)
	# Gino's own fall: level 12's deck has an open gap two steps from the start
	await select_level(12)
	await wait_until(func(): return lv() != null and lv().level_id == 12 and pl() != null, 240, "level 12 loaded")
	await frames(45)
	await walk(cell_center("a", Vector2i(7, 3)))
	note("deliberate", {"what": "walk off the deck into the gap"})
	var start_y: float = pl().global_position.y
	await look(cell_center("a", Vector2i(7, 5)) + Vector3(0, -1.0, 0))
	set_move(Vector2(0, -1))
	await until(func(): return pl().global_position.y < start_y - 4.0, 4.0)
	set_move(Vector2.ZERO)
	await wait_until(func(): return pl().global_position.y > start_y - 1.0 and pl().global_position.distance_to(lv().checkpoint) < 1.5, 240, "falling puts Gino back at the checkpoint")
	await frames(60)
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	await menu_keys(4)
	await wait_until(func(): return scene_name() == "MainMenu", 90, "back to the main menu")
	await wait(30)

## Pause-menu keyboard navigation: focus starts on Resume; Down n times, then Enter.
func menu_keys(downs: int) -> void:
	for i in downs:
		await key(KEY_DOWN, "Down")
		await wait(8)
	await wait(10)
	await key(KEY_ENTER, "Enter")

func pad(button: JoyButton, label: String) -> void:
	joy_button(button, true, label)
	await frames(2)
	joy_button(button, false, label)
	await frames(2)

func take_extras() -> void:
	mark("options")
	await press_button("Options")
	await wait(90)
	await press_button("Back")
	await wait(30)
	mark("credits_menu")
	await press_button("Credits")
	await wait_until(func(): return scene_name() == "Credits", 60, "credits from the menu")
	await wait(150)
	await key(KEY_ESCAPE, "Esc")
	await wait_until(func(): return scene_name() == "MainMenu", 120, "Esc leaves the credits")
	await wait(30)
	mark("select1")
	await select_level(1)
	await wait_until(func(): return lv() != null and lv().level_id == 1 and pl() != null, 240, "level 1 loaded")
	await frames(45)
	mark("look_and_keys")
	var yaw0: float = pl().rotation.y
	for i in 36:
		turn(2.5, 0.0)
		await step()
	for i in 36:
		turn(-2.5, 0.0)
		await step()
	turn(0, 0)
	expect(absf(rad_to_deg(pl().rotation.y - yaw0)) < 5.0, "the view turns left and right (%s)" % look_mode)
	hold(KEY_UP, "Up")
	await frames(20)
	hold(KEY_SHIFT, "Shift")
	await frames(20)
	expect(_speed() > 5.0, "Shift runs")
	release(KEY_SHIFT)
	release(KEY_UP)
	await frames(15)
	await key(KEY_SPACE, "Space")
	await frames(30)
	mark("pad")
	var cell := item_near(pos_of("c"), "cell")
	await approach(cell.global_position, 1.5)
	await look(cell.global_position)
	await pad(JOY_BUTTON_Y, "Y")
	await frames(10)
	expect(pl().held == cell, "pad Y picks up")
	var sock: Node = device_at("socket", "S")
	await approach(sock.global_position, 1.9)
	await look(sock.global_position + Vector3(0, 0.9, 0))
	await pad(JOY_BUTTON_X, "X")
	await frames(30)
	expect(lv().devices["d1"].is_open, "pad X uses the socket")
	# the left stick walks Gino toward the open door; keys finish the route
	var door_pos: Vector3 = lv().devices["d1"].global_position
	var n := 0
	while n < 70:
		var dy := _wrap(_yaw_to(door_pos) - rad_to_deg(pl().rotation.y))
		turn(dy, 0.0)
		joy_axis(JOY_AXIS_LEFT_Y, -1.0 if absf(dy) < 30.0 else 0.0, "left_y")
		await step()
		n += 1
	joy_axis(JOY_AXIS_LEFT_Y, 0.0, "left_y")
	await frames(10)
	await walk(pos_of("G"))
	expect(lv() != null and lv().completed, "level 1 completed")
	await wait(60)
	await press_button("Main menu")
	await wait_until(func(): return scene_name() == "MainMenu", 90, "back to the main menu")
	await wait(30)
