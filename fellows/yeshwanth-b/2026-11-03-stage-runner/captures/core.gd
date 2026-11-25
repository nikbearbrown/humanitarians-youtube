extends SceneTree

# Scripted-input capture driver for Stage Runner (film evidence, not a playtest).
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

func stage() -> Node:
	var s := current_scene
	return s if s and s.get("stage_id") != null else null

func player() -> Node2D:
	var s := stage()
	return s.player if s else null

func snapshot() -> Dictionary:
	var d := {"scene": scene_name(), "paused": paused}
	var s := stage()
	if s:
		d["state"] = s.state
		d["score"] = s.score
		d["kills"] = s.kills
		var p: Node2D = s.player
		if is_instance_valid(p):
			d["lives"] = p.lives
			d["pos"] = [snappedf(p.position.x, 0.1), snappedf(p.position.y, 0.1)]
			d["spread"] = snappedf(p.spread_time, 0.01)
			d["invulnerable"] = snappedf(p.invulnerable, 0.01)
		d["enemies"] = get_nodes_in_group("enemies").size()
		d["fireballs"] = get_nodes_in_group("enemy_bullets").size()
		d["pickups"] = get_nodes_in_group("pickups").size()
		if is_instance_valid(s.boss):
			d["boss_hp"] = s.boss.health
			d["boss_state"] = s.boss.state
		d["pause_menu"] = s.pause_menu.visible
		d["game_over_menu"] = s.game_over_menu.visible
	var audio := root.get_node_or_null("Audio")
	if audio:
		d["audio"] = audio.enabled
	var gs := root.get_node_or_null("GameState")
	if gs:
		d["run_score"] = gs.run_score
		d["best"] = gs.best_score
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
