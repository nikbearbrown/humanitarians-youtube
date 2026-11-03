const FPS := 30.0
const W := 3840
const H := 2160

var take := ""
var out_dir := ""
var frame := 0
var log_file: FileAccess
var failed := false
var mouse := Vector2(640, 360)      ## logical (1280x720) viewport coordinates
var ring := 0.0
var overlay: Node2D
var held := {}                      ## physical keycode -> true while held
var fire_held := false
var segment := ""
var stats := {}
var nosave := false
const CHUNK := 150
var chunk_file: FileAccess
var chunk_index := 0

class CursorOverlay extends Node2D:
	var driver
	func _process(_d: float) -> void:
		queue_redraw()
	func _draw() -> void:
		if Input.mouse_mode != Input.MOUSE_MODE_VISIBLE:
			return
		var p: Vector2 = driver.mouse
		if driver.ring > 0.0:
			var t: float = 1.0 - driver.ring
			draw_arc(p, 6.0 + 16.0 * t, 0.0, TAU, 32, Color(0.91, 0.45, 0.16, 1.0 - t), 2.5)
		var arrow := PackedVector2Array([p, p + Vector2(0, 17), p + Vector2(4.5, 13),
			p + Vector2(8, 20), p + Vector2(10.5, 19), p + Vector2(7, 12), p + Vector2(12.5, 12)])
		draw_colored_polygon(arrow, Color(1, 1, 1))
		var outline := arrow.duplicate()
		outline.append(p)
		draw_polyline(outline, Color(0.08, 0.08, 0.08), 1.4, true)

func _initialize() -> void:
	var args := OS.get_cmdline_user_args()
	take = args[0]
	out_dir = args[1]
	nosave = args.size() > 2 and args[2] == "nosave"
	DirAccess.make_dir_recursive_absolute(out_dir)
	log_file = FileAccess.open(out_dir + "/inputs.jsonl", FileAccess.WRITE)
	if not nosave:
		DisplayServer.window_set_size(Vector2i(W, H))
	# Raw RGB frames are appended to 150-frame chunk files; run_take.sh encodes and deletes them.
	DirAccess.make_dir_recursive_absolute(out_dir + "/frames")
	var layer := CanvasLayer.new()
	layer.layer = 128
	root.add_child(layer)
	overlay = CursorOverlay.new()
	overlay.driver = self
	layer.add_child(overlay)
	RenderingServer.frame_post_draw.connect(_save_frame)
	change_scene_to_file(ProjectSettings.get_setting("application/run/main_scene"))
	note("boot", {"take": take, "main_scene": ProjectSettings.get_setting("application/run/main_scene"),
		"engine": Engine.get_version_info().string})
	call_deferred("run")

func _save_frame() -> void:
	if nosave:
		frame += 1
		iterations_since_draw = 0
		ring = maxf(0.0, ring - 1.0 / 12.0)
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
	frame += 1
	iterations_since_draw = 0
	ring = maxf(0.0, ring - 1.0 / 12.0)

## Watchdog: macOS stops drawing an occluded window while game logic keeps running.
## If no frame is drawn for 60 iterations, the take is aborted as a failure.
var iterations_since_draw := 0
var draw_stalled := false
func _process(_delta: float) -> bool:
	iterations_since_draw += 1
	if iterations_since_draw > 60 and not nosave and not draw_stalled:
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
		if pending < 3:
			return
		OS.delay_msec(200)

# --- observation (read-only) ---

func scene() -> Node:
	return current_scene

SNAPSHOT_PLACEHOLDER

func note(event: String, detail: Dictionary = {}) -> void:
	var line := {"frame": frame, "t": snappedf(frame / FPS, 0.001), "event": event, "detail": detail,
		"game": snapshot() if current_scene else {}}
	log_file.store_line(JSON.stringify(line))
	log_file.flush()
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
	Input.parse_input_event(ev)

func click(p: Vector2, label: String, travel: int = 18) -> void:
	await move(p, travel)
	await wait(5)
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
	held[code] = true
	note("key_down", {"key": label})
	_key_event(code, true)

func release(code: Key, label: String) -> void:
	if not held.has(code):
		return
	held.erase(code)
	note("key_up", {"key": label})
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

func right_click(label: String) -> void:
	note("click", {"button": "right", "on": label})
	_button(MOUSE_BUTTON_RIGHT, true)
	await process_frame
	_button(MOUSE_BUTTON_RIGHT, false)

func joy_axis(axis: JoyAxis, value: float, label: String) -> void:
	note("joy_axis", {"axis": label, "value": value})
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

func press_button(text: String) -> void:
	var b := find_button(text)
	expect(b != null, "button visible: " + text)
	if b:
		await click(b.get_global_rect().get_center(), text, 22)

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

# --- the arena autopilot: observes positions, outputs only key/mouse events ---