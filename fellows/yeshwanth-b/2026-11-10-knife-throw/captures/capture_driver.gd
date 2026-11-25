extends SceneTree

# Scripted-input capture driver for Gino: Knife Throw (film evidence, not a playtest).
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

func player() -> CharacterBody2D:
	var l := level()
	return l.player if l else null

func snapshot() -> Dictionary:
	var d := {"scene": scene_name(), "paused": paused}
	var l := level()
	if l:
		d["level"] = l.level_id
		d["state"] = l.state
		d["diamonds"] = l.diamonds_found
		d["enemies_left"] = get_nodes_in_group("enemies").size()
		var p: CharacterBody2D = l.player
		if is_instance_valid(p):
			d["pos"] = [snappedf(p.global_position.x, 0.1), snappedf(p.global_position.y, 0.1)]
			d["health"] = p.health
			d["gino"] = p.state
			d["combo"] = p.combo
			d["on_floor"] = p.is_on_floor()
	var gs := root.get_node_or_null("GameState")
	if gs:
		d["score"] = gs.score
		d["knives"] = gs.knives
	var audio := root.get_node_or_null("Audio")
	if audio:
		d["audio"] = audio.enabled
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
	note("click", {"button": "left", "on": label, "logical": [snappedf(p.x, 0.1), snappedf(p.y, 0.1)]})
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

func find_button(text: String) -> Button:
	return _find_button(root, text)

func _find_button(n: Node, text: String) -> Button:
	if n is Button and n.text == text and n.is_visible_in_tree():
		return n
	for c in n.get_children():
		var b := _find_button(c, text)
		if b:
			return b
	return null

func press_button(text: String, travel: int = 22) -> void:
	var b := find_button(text)
	expect(b != null, "button visible: " + text)
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

# --- the platform autopilot: observes positions, outputs only key/mouse/pad events ---
# Platforming follows the routes the game's own level checker found (_tools/routes.json),
# with the same align-then-act rule as _tools/playtest.gd. Where the playtest hands the
# player a move dictionary through its test-only `autopilot` hook, this driver presses
# and releases the real keys. Enemies are NOT removed: between route edges, on the ground,
# the driver throws knives at range and slashes when an enemy is close.

const KEY_NAMES := {KEY_A: "A", KEY_D: "D", KEY_LEFT: "Left", KEY_RIGHT: "Right", KEY_SPACE: "Space", KEY_J: "J",
	KEY_X: "X", KEY_K: "K", KEY_C: "C", KEY_W: "W", KEY_UP: "Up", KEY_ENTER: "Enter"}
var left_key: Key = KEY_A
var right_key: Key = KEY_D
var attack_key: Key = KEY_J
var throw_key: Key = KEY_K
var routes := {}
var route: Array = []
var edge_index := 0
var edge_phase := "align"
var edge_frame := 0
var align_frames := 0
var taps: Array = []          # keys to release on the next frame
var fight_cooldown := 0
var throw_cooldown := 0
var hint_wait := 0
var fights := false
var wait_frames := 0
var evade_frames := 0
var drop_kind := ""          # "leap" or "drop" while a guarded descent is under way
var drop_frames := 0

func tap(code: Key) -> void:
	note("key", {"key": KEY_NAMES.get(code, str(code))})
	_key_event(code, true)
	taps.append(code)

func flush_taps() -> void:
	for code in taps:
		_key_event(code, false)
	taps.clear()

var move_dir := 0
var edge_airborne := false
var DEBUG_MOVES := false

func set_move(dir: int) -> void:
	if dir != move_dir and DEBUG_MOVES:
		var st := get_stack()
		note("move_dbg", {"dir": dir, "line": st[1].line if st.size() > 1 else -1, "fn": st[1].function if st.size() > 1 else ""})
	move_dir = dir
	if dir > 0:
		release(left_key)
		hold(right_key, KEY_NAMES[right_key])
	elif dir < 0:
		release(right_key)
		hold(left_key, KEY_NAMES[left_key])
	else:
		release(left_key)
		release(right_key)

func is_bat(e: Node) -> bool:
	return e.get_script().resource_path.ends_with("bat.gd")

func is_plant(e: Node) -> bool:
	return e.get_script().resource_path.ends_with("plant.gd")

## Plants are never fought up close: their snap reaches 46 px and outranges the sword, but
## a snap only covers the side Gino was on when it reared up, so running past is safe.
func nearest_enemy(p: Vector2, max_dx: float, max_dy: float, plants := false) -> Node2D:
	var best: Node2D = null
	var bd := INF
	for e in get_nodes_in_group("enemies"):
		if not e.alive or (is_plant(e) and not plants):
			continue
		var c: Vector2 = e.center()
		var dx := absf(c.x - p.x)
		var dy := absf(c.y - (p.y - 14.0))
		if dx < max_dx and dy < max_dy and dx < bd:
			bd = dx
			best = e
	return best

## Rock or a one-way plank (the rope bridge, ledges) just under the point.
func floor_under(l: Node, x: float, y: float) -> bool:
	var cx := floori(x / 16.0)
	var cy := floori((y + 4.0) / 16.0)
	if cx < 0 or cx >= l.cols or cy < 0 or cy >= l.rows_count:
		return false
	return l.grid[cy * l.cols + cx] != 0

## Unbroken footing from Gino to x (a walker across a gap never comes over).
func floor_between(l: Node, p: Vector2, x: float) -> bool:
	var step := 8.0 * signf(x - p.x)
	var cx := p.x
	while absf(x - cx) > 8.0:
		cx += step
		if not floor_under(l, cx, p.y):
			return false
	return true

## One frame of fighting. Returns true if the driver spent this frame on an enemy.
## Fighting never walks Gino off his footing (Level 3's rope bridge stops one tile short of the rock).
func fight(l: Node, pl: CharacterBody2D) -> bool:
	var busy := fight_moves(l, pl)
	if busy and move_dir != 0 and pl.is_on_floor():
		var p := pl.global_position
		if not floor_under(l, p.x + move_dir * 9.0, p.y) or not floor_under(l, p.x + move_dir * 15.0, p.y):
			if pl.facing == move_dir:
				set_move(0)
				if Engine.get_process_frames() % 30 == 0:
					var near := nearest_enemy(p, 200.0, 80.0, true)
					note("floor_guard", {"near": near.get_script().resource_path.get_file() if near else "", "dx": snappedf(near.center().x - p.x, 0.1) if near else 0.0, "dy": snappedf(near.center().y - p.y, 0.1) if near else 0.0, "wait": wait_frames, "state": near.state if near else ""})
	return busy

func fight_moves(l: Node, pl: CharacterBody2D) -> bool:
	if not fights or not pl.is_on_floor() or not pl.state in ["normal", "attack"]:
		return false
	var p := pl.global_position
	# mid-combo: keep pressing J so Attack1 chains to the Attack4 finisher (100 damage in all)
	var foe := nearest_enemy(p, 70.0, 40.0)
	# bats curl up for 0.7 s before they strike, then wait ~1 s: back off during the wind-up,
	# punish after the strike (two slashes fit in the gap)
	if foe and is_bat(foe) and foe.state == "attack" and foe.state_time < 0.95:
		if pl.state == "normal" and absf(foe.center().x - p.x) < 44.0:
			var away := -1 if foe.center().x > p.x else 1
			if floor_under(l, p.x + away * 12.0, p.y):
				set_move(away)
				return true
		if pl.state == "normal":
			set_move(0)
			return true
	if pl.state == "attack" and foe and absf(foe.center().x - p.x) < 44.0 and (not is_bat(foe) or pl.combo < 2):
		set_move(0)
		if fight_cooldown <= 0:
			tap(attack_key)
			fight_cooldown = 5
		wait_frames = 0
		return true
	# inside a walker's or bat's strike cone (~28 px): back off first, then fight at sword range.
	# Gino runs at 105 px/s, faster than either chases (50 and 58).
	var danger := nearest_enemy(p, 30.0, 34.0)
	if danger and pl.state == "normal":
		var away := -1 if danger.center().x > p.x else 1
		if floor_under(l, p.x + away * 12.0, p.y):
			set_move(away)
			if evade_frames == 0:
				note("evade", {"from": danger.get_script().resource_path.get_file(), "dx": snappedf(danger.center().x - p.x, 0.1)})
			evade_frames += 1
			return true
	evade_frames = 0
	# slash inside ~38 px: the first slash reaches ~40 px, the walker's bite cone only ~28
	var close := nearest_enemy(p, 38.0, 34.0)
	if close:
		var dir := 1 if close.center().x > p.x else -1
		if pl.state == "normal" and pl.facing != dir:
			set_move(dir)          # one frame of running turns Gino round
			return true
		set_move(0)
		if fight_cooldown <= 0:
			tap(attack_key)
			wait_frames = 0
			note("slash", {"dx": snappedf(close.center().x - p.x, 0.1), "dy": snappedf(close.center().y - p.y, 0.1), "hp": close.health, "enemy_state": close.state, "gino": pl.state, "anim": String(pl.sprite.animation), "combo": pl.combo})
			fight_cooldown = 5
		return true
	# a walker or bat in chase range: stand, face it and let it come into sword range,
	# rather than hopping onto it (the route advances in ~70 px hops)
	var near := nearest_enemy(p, 160.0, 44.0)
	if near == null:
		near = nearest_enemy(p, 150.0, 64.0)     # a bat swooping down from a ledge above
		if near and not is_bat(near):
			near = null
	if near and wait_frames < 150:
		wait_frames += 1
		var dir := 1 if near.center().x > p.x else -1
		var coming: bool = near.velocity.x * -dir > 5.0
		var ground_ahead: bool = floor_under(l, p.x + dir * 10.0, p.y)
		if not coming and not floor_between(l, p, near.center().x) and wait_frames > 15 and not is_bat(near):
			wait_frames = 150      # it waits across a gap and never will come: jump the gap past it
			note("gap_walker", {"dx": snappedf(near.center().x - p.x, 0.1)})
			return false
		if pl.state == "normal" and pl.facing != dir:
			set_move(dir)
		elif not coming and wait_frames > 15 and ground_ahead and absf(near.center().x - p.x) > 38.0:
			set_move(dir)      # it isn't coming (a ledge stops it): walk up to sword range
		else:
			set_move(0)
		if wait_frames == 1:
			note("waiting_for", {"enemy": near.get_script().resource_path.get_file()})
		return true
	if not near:
		wait_frames = 0
	var root_gs := root.get_node("GameState")
	if root_gs.knives > 0 and throw_cooldown <= 0 and pl.state == "normal":
		var far := nearest_enemy(p, 170.0, 20.0, true)
		if far:
			var dir := 1 if far.center().x > p.x else -1
			var dx := absf(far.center().x - p.x)
			if dx > 64.0:
				if pl.facing != dir:
					set_move(dir)
					return true
				set_move(0)
				tap(throw_key)
				throw_cooldown = 24
				note("knife_thrown", {"at": far.get_script().resource_path.get_file()})
				return true
	return false

func route_step(l: Node, pl: CharacterBody2D) -> void:
	var p := pl.global_position
	var on_floor := pl.is_on_floor()
	if edge_index >= route.size():
		if pl.near_door != null and on_floor:
			set_move(0)
			if absf(pl.velocity.x) < 1.0 and pl.state == "normal":
				tap(KEY_W)
		else:
			set_move(int(signf(l.door.global_position.x - p.x)))
		return
	var edge: Dictionary = route[edge_index]
	if edge_phase == "align":
		align_frames += 1
		var dx: float = edge.from[0] - p.x
		var still := absf(pl.velocity.x) < 0.5
		if (absf(dx) <= 1.0 and still and on_floor) or align_frames > 120:
			if align_frames > 120:
				note("align_timeout", {"edge": edge_index, "dx": snappedf(dx, 0.1)})
			edge_phase = "act"
			edge_frame = 0
		elif absf(dx) > 4.0:
			set_move(int(signf(dx)))
			return
		elif still and on_floor:
			set_move(0)
			if align_frames % 3 == 0:
				tap(right_key if dx > 0 else left_key)
			return
		else:
			set_move(0)
			return
	if edge.kind == "jump" and edge_frame == 0 and drop_kind == "":
		drop_kind = guarded_descent(l, edge)
		drop_frames = 0
		if drop_kind != "":
			note("guarded_descent", {"edge": edge_index, "kind": drop_kind})
	if drop_kind != "":
		descend(l, pl, edge)
		return
	var f := edge_frame
	edge_frame += 1
	if edge.kind == "walk":
		var frames := int(ceil(float(edge.param) / 2.0))   # the route counts 60 Hz ticks
		set_move(int(edge.move) if f < frames else 0)
		if f >= frames and on_floor and absf(pl.velocity.x) < 0.01:
			next_edge(edge, p)
	else:
		if not on_floor:
			edge_airborne = true
		if f == 0:
			edge_airborne = false
			var around := []
			for e in get_nodes_in_group("enemies"):
				var c: Vector2 = e.center()
				if absf(c.x - p.x) < 260:
					around.append([e.get_script().resource_path.get_file(), snappedf(c.x - p.x, 0.1), snappedf(c.y - (p.y - 14.0), 0.1)])
			if around:
				note("jump_with_enemies", {"edge": edge_index, "around": around, "wait": wait_frames})
			set_move(int(edge.move))
			hold(KEY_SPACE, "Space")
		elif on_floor and f > 2 and not edge_airborne:
			# the jump never left the ground (Space pressed during a slash): press it again
			release(KEY_SPACE)
			set_move(0)
			edge_frame = 0
			note("jump_retry", {"edge": edge_index})
		elif on_floor and f > 1 and edge_airborne:
			# landed just past a walker: keep running out of its bite before stopping
			var behind := nearest_enemy(p, 46.0, 30.0)
			if behind and not is_bat(behind) and (behind.center().x - p.x) * int(edge.move) < 0.0 \
					and floor_under(l, p.x + int(edge.move) * 12.0, p.y):
				set_move(int(edge.move))
				return
			if not floor_under(l, p.x + int(edge.move) * 3.0, p.y) and absf(pl.velocity.x) > 0.01:
				set_move(-int(edge.move))      # landed on a rim: brake back onto it
				return
			set_move(0)
			release(KEY_SPACE)
			if absf(pl.velocity.x) < 0.01:
				next_edge(edge, p)
		else:
			var mv := int(edge.move)
			var ty := float(edge.to[1])
			# the landing spot is a rim (Level 3's rock pillars): steer back so Gino stops on it
			var near_rim: bool = pl.velocity.y > 0.0 and (float(edge.to[0]) - mv * 8.0 - p.x) * mv < 16.0 \
					and floor_under(l, float(edge.to[0]) - mv * 8.0, ty) and not floor_under(l, float(edge.to[0]) + mv * 4.0, ty)
			var off_rim: bool = pl.velocity.y > 0.0 and p.y > ty - 2.0 and not floor_under(l, p.x, ty) \
					and floor_under(l, p.x - mv * 10.0, ty)
			set_move(-mv if near_rim or off_rim else mv)
			if f / FPS >= float(edge.param):
				release(KEY_SPACE)

## A walker waiting on the floor a jump drops to bites Gino as he lands, while he is still in the air.
## Leap well past it when it stands under the jump, or step off the rim and land short when it waits
## beyond the landing; either way it has to walk to Gino, into sword range.
func guarded_descent(l: Node, edge: Dictionary) -> String:
	if float(edge.to[1]) < float(edge.from[1]) + 16.0:
		return ""
	var dir := int(edge.move)
	for e in get_nodes_in_group("enemies"):
		if is_bat(e) or is_plant(e) or absf(e.global_position.y - float(edge.to[1])) > 10.0:
			continue
		var ahead: float = (e.global_position.x - float(edge.from[0])) * dir
		var span: float = (float(edge.to[0]) - float(edge.from[0])) * dir
		if ahead > 0.0 and ahead < span - 6.0:
			return "leap"
		if ahead >= span - 6.0 and ahead < span + 70.0:
			return "drop"
	return ""

func descend(l: Node, pl: CharacterBody2D, edge: Dictionary) -> void:
	var p := pl.global_position
	var dir := int(edge.move)
	var on_floor := pl.is_on_floor()
	drop_frames += 1
	var rim: bool = not floor_under(l, p.x + dir * 9.0, p.y)
	if on_floor and p.y < float(edge.from[1]) + 4.0:
		# still up top: run to the rim (a leap takes off from it)
		set_move(dir)
		if drop_kind == "leap" and rim:
			hold(KEY_SPACE, "Space")
		return
	if not on_floor:
		if drop_kind == "leap":
			set_move(dir)
			if pl.velocity.y > 0.0:
				release(KEY_SPACE)
		else:
			set_move(dir if drop_frames % 4 == 0 else 0)   # barely drift: land just below the rim
		return
	set_move(0)
	release(KEY_SPACE)
	drop_kind = ""
	next_edge(edge, p)

func next_edge(edge: Dictionary, p: Vector2) -> void:
	var drift := p.distance_to(Vector2(edge.to[0], edge.to[1]))
	if drift > 6.0:
		note("edge_drift", {"edge": edge_index, "drift": snappedf(drift, 0.1)})
	edge_index += 1
	edge_phase = "align"
	edge_frame = 0
	align_frames = 0

## Play the current level to its door. Returns the level state it ended in.
func play_level(max_frames: int, each_frame := Callable()) -> String:
	var l := level()
	route = routes[str(l.level_id)]
	edge_index = 0
	drop_kind = ""
	edge_phase = "align"
	edge_frame = 0
	align_frames = 0
	var last_health := -1
	var last_knives := -1
	var n := 0
	while n < max_frames:
		flush_taps()
		l = level()
		if l == null:
			break
		var pl := player()
		var gs := root.get_node("GameState")
		if last_health >= 0 and pl.health < last_health:
			var by := nearest_enemy(pl.global_position, 80.0, 60.0, true)
			note("gino_hit", {"health": pl.health, "by": by.get_script().resource_path.get_file() if by else "spike/other",
				"dx": snappedf(by.center().x - pl.global_position.x, 0.1) if by else 0.0, "by_state": by.state if by else ""})
			stats["hits"] = stats.get("hits", 0) + 1
		elif last_health >= 0 and pl.health > last_health:
			note("gino_healed", {"health": pl.health})
		last_health = pl.health
		if last_knives >= 0 and gs.knives > last_knives:
			note("knife_picked_up", {"knives": gs.knives})
		last_knives = gs.knives
		fight_cooldown -= 1
		throw_cooldown -= 1
		if l.state == "hint":
			set_move(0)
			release(KEY_SPACE)
			if l.hint_ready:
				hint_wait += 1
				if hint_wait > 40:
					hint_wait = 0
					tap(KEY_ENTER)
					note("hint_closed", {"hint": l.active_hint})
			await process_frame
			n += 1
			continue
		if l.state in ["clear", "dead"]:
			break
		if paused:
			expect(false, "game paused itself during play (focus loss?)")
			break
		if each_frame.is_valid() and each_frame.call(n) == true:
			break
		if edge_phase == "align" and fight(l, pl):
			await process_frame
			n += 1
			continue
		route_step(l, pl)
		await process_frame
		n += 1
	set_move(0)
	release(KEY_SPACE)
	flush_taps()
	var lv := level()
	return lv.state if lv else scene_name()

func in_scene(name: String) -> bool:
	return scene_name() == name

func wait_level(id: int) -> bool:
	return await wait_until(func(): return level() != null and level().level_id == id and level().state in ["intro", "play"], 120,
		"level %d loaded" % id)

# --- takes ---

func run() -> void:
	routes = JSON.parse_string(FileAccess.get_file_as_string("res://_tools/routes.json"))
	await wait_until(func(): return in_scene("MainMenu"), 120, "main menu loaded")
	match take:
		"campaign": await take_campaign()
		"defeat": await take_defeat()
		"extras": await take_extras()
		_: expect(false, "unknown take " + take)
	await finish()

func clear_level(id: int) -> void:
	mark("level%d" % id)
	await wait_level(id)
	var result := await play_level(150 * 30)
	expect(result == "clear", "level %d cleared (health %d)" % [id, player().health if player() else -1])
	await wait_until(func(): return level() != null and level().clear_menu.visible, 90, "level %d complete panel" % id)
	mark("clear%d" % id)
	await wait(110)
	await press_button("Finish" if id == 3 else "Next Level")

func take_campaign() -> void:
	fights = true
	mark("menu")
	await wait(70)
	await press_button("How to Play")
	await wait_until(func(): return in_scene("Instructions"), 60, "How to Play opens")
	mark("instructions")
	await wait(150)
	await key(KEY_ESCAPE, "Esc")
	await wait_until(func(): return in_scene("MainMenu"), 60, "Esc returns to the main menu")
	await wait(30)
	await press_button("New Game")
	for id in [1, 2, 3]:
		await clear_level(id)
	await wait_until(func(): return in_scene("Credits"), 150, "credits roll")
	mark("credits")
	await wait_until(func(): return in_scene("MainMenu"), 60 * 30, "credits return to the main menu")
	mark("menu_after")
	await wait(90)
	expect(find_button("Continue  (Level 3)") != null, "Continue offers the furthest level")

func take_defeat() -> void:
	fights = true
	mark("menu")
	await wait(40)
	await press_button("New Game")
	await wait_level(1)
	mark("pause")
	await wait(70)
	await key(KEY_ESCAPE, "Esc")
	await wait_until(func(): return level().pause_menu.visible and paused, 10, "Esc pauses")
	await wait(60)
	await press_button("Resume")
	await wait_until(func(): return not paused, 10, "Resume unpauses")
	mark("to_pit")
	# walk right along the route until the first pit, then run off the edge into it
	var l := level()
	var pit_x := -1
	for x in range(l.cols):
		if l.grid[(l.rows_count - 1) * l.cols + x] == 0:
			pit_x = x
			break
	note("first_pit", {"x_px": pit_x * 16})
	var to_pit := func(_n: int) -> bool:
		return player().global_position.x > pit_x * 16 - 120
	await play_level(60 * 30, to_pit)
	mark("fall")
	set_move(1)
	await wait_until(func(): return player().state == "dead", 6 * 30, "Gino falls into the pit")
	set_move(0)
	await wait_until(func(): return level().game_over_menu.visible, 90, "game-over panel")
	mark("game_over")
	await wait(110)
	await press_button("Retry")
	await wait_level(1)
	expect(player().health == 6, "Retry restores full health")
	mark("retry")
	await wait(80)
	await key(KEY_ESCAPE, "Esc")
	await wait_until(func(): return level().pause_menu.visible, 10, "pause again")
	await wait(40)
	await key(KEY_R, "R")
	await wait_until(func(): return level() != null and level().state == "intro", 40, "R restarts the level")
	await wait(70)
	await key(KEY_ESCAPE, "Esc")
	await wait(40)
	await press_button("Main Menu")
	await wait_until(func(): return in_scene("MainMenu"), 60, "back to the main menu")
	await wait(40)

func take_extras() -> void:
	fights = true
	mark("menu_audio")
	await wait(40)
	await press_button("Sound: On")
	await wait(30)
	await press_button("Sound: Off")
	await wait(30)
	await press_button("New Game")
	await wait_level(1)
	mark("alt_keys")
	left_key = KEY_LEFT
	right_key = KEY_RIGHT
	attack_key = KEY_X
	throw_key = KEY_C
	var until_x := func(_n: int) -> bool:
		return player().global_position.x > 330.0
	await play_level(40 * 30, until_x)
	mark("sound_key")
	await key(KEY_M, "M")
	await wait(40)
	await key(KEY_M, "M")
	await wait(20)
	mark("pad")
	await pad_run(150)
	if level().state == "hint":
		# the pad run reached a hint sign: close it with the pad's A button
		await wait_until(func(): return level().hint_ready, 120, "hint ready for the pad")
		await wait(20)
		joy_button(JOY_BUTTON_A, true, "A")
		await wait(2)
		joy_button(JOY_BUTTON_A, false, "A")
		await wait_until(func(): return level().state == "play", 30, "pad A closes the hint")
		await wait(20)
	joy_button(JOY_BUTTON_START, true, "Start")
	await wait(2)
	joy_button(JOY_BUTTON_START, false, "Start")
	await wait_until(func(): return level().pause_menu.visible, 10, "Start pauses")
	await wait(45)
	joy_button(JOY_BUTTON_START, true, "Start")
	await wait(2)
	joy_button(JOY_BUTTON_START, false, "Start")
	await wait_until(func(): return not paused, 10, "Start resumes")
	await wait(20)
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	await press_button("Main Menu")
	await wait_until(func(): return in_scene("MainMenu"), 60, "back to the main menu")
	await wait(40)

## A few seconds of gamepad play: the left stick runs, A jumps, X slashes.
func pad_run(frames: int) -> void:
	for n in range(frames):
		if n == 0:
			joy_axis(JOY_AXIS_LEFT_X, 1.0, "left_x")
		if n == 40:
			joy_button(JOY_BUTTON_A, true, "A")
		if n == 52:
			joy_button(JOY_BUTTON_A, false, "A")
		if n == 90:
			joy_axis(JOY_AXIS_LEFT_X, 0.0, "left_x")
		if n == 100 or n == 112:
			joy_button(JOY_BUTTON_X, true, "X")
		if n == 102 or n == 114:
			joy_button(JOY_BUTTON_X, false, "X")
		await process_frame
	joy_axis(JOY_AXIS_LEFT_X, 0.0, "left_x")
