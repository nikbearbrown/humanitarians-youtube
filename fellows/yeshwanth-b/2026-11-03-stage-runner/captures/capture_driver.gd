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

# --- the street autopilot: observes positions, outputs only key/mouse/pad events ---
# Ported from the game's own _tools/playtest.gd look-ahead dodge, but where the
# playtest hands the player a move vector through its test-only `autopilot`
# hook, this driver turns the chosen heading into held keys.

const WASD := {"left": KEY_A, "right": KEY_D, "up": KEY_W, "down": KEY_S}
const ARROWS := {"left": KEY_LEFT, "right": KEY_RIGHT, "up": KEY_UP, "down": KEY_DOWN}
const KEY_NAMES := {KEY_A: "A", KEY_D: "D", KEY_W: "W", KEY_S: "S", KEY_LEFT: "Left", KEY_RIGHT: "Right",
	KEY_UP: "Up", KEY_DOWN: "Down", KEY_J: "J", KEY_SPACE: "Space", KEY_Z: "Z", KEY_SHIFT: "Shift"}
const MOVE_SPEED := 360.0

var scheme: Dictionary = WASD
var fire_key: Key = KEY_J
var kamikaze := false

func heading() -> Vector2:
	var p := player()
	if p == null:
		return Vector2.ZERO
	var pos := p.position
	if kamikaze:
		var near: Node2D = null
		var best_d := INF
		for e in get_nodes_in_group("enemies"):
			if e.position.y > 0 and e.position.distance_to(pos) < best_d:
				best_d = e.position.distance_to(pos)
				near = e
		if near == null:
			return ((Vector2(640, 420) - pos) / 60.0).limit_length(1.0)
		return ((near.position + Vector2(0, 30) - pos) / 30.0).limit_length(1.0)
	var move := Vector2.ZERO
	var target: Node2D = null
	var best := INF
	for e in get_nodes_in_group("enemies"):
		if e.position.y < -20 or e.position.y > pos.y - 40:
			continue
		var score: float = (pos.y - e.position.y) + absf(e.position.x - pos.x) * 0.6
		if e.is_in_group("boss"):
			score += 140.0
		if score < best:
			best = score
			target = e
	var aim_y := 610.0
	var prize: Node2D = null
	for k in get_nodes_in_group("pickups"):
		if k.position.y > 150 and k.position.y < 680 and absf(k.position.x - pos.x) < 330:
			prize = k
	if prize:
		move.x = clampf((prize.position.x - pos.x) / 30.0, -1.0, 1.0)
		aim_y = clampf(prize.position.y + 10.0, 420.0, 680.0)
	elif target:
		move.x = clampf((target.position.x - pos.x) / 40.0, -1.0, 1.0)
	else:
		move.x = clampf((640.0 - pos.x) / 120.0, -1.0, 1.0)
	move.y = clampf((aim_y - pos.y) / 60.0, -1.0, 1.0)
	var threats: Array = []
	for group in ["enemy_bullets", "enemies"]:
		for t in get_nodes_in_group(group):
			if t.position.distance_to(pos) < 260.0:
				var vel: Vector2 = t.velocity if group == "enemy_bullets" else Vector2(0, t.speed if t.get("speed") != null else 0.0)
				var radius := 20.0 if group == "enemy_bullets" else 48.0
				if t.is_in_group("boss"):
					radius = 120.0
				threats.append([t.position, vel, radius])
	if threats.is_empty():
		return move.limit_length(1.0)
	var speed := MOVE_SPEED * (0.5 if held.has(KEY_SHIFT) else 1.0)
	var best_move := move
	var best_value := -INF
	for dir in [Vector2.ZERO, Vector2.LEFT, Vector2.RIGHT, Vector2.UP, Vector2.DOWN, Vector2(-1, -1), Vector2(1, -1), Vector2(-1, 1), Vector2(1, 1), move]:
		var h: Vector2 = dir.normalized() if dir.length() > 0.01 else Vector2.ZERO
		var clearance := INF
		for step in range(1, 8):
			var t := step * 0.05
			var q: Vector2 = pos + h * speed * t
			q.x = clampf(q.x, 348, 932)
			q.y = clampf(q.y, 34, 690)
			for th in threats:
				clearance = minf(clearance, q.distance_to(th[0] + th[1] * t) - th[2])
		var follow := h.dot(move.normalized()) if move.length() > 0.01 else 0.0
		var edge := 0.0
		var end: Vector2 = pos + h * speed * 0.35
		if end.x < 360 or end.x > 920 or end.y > 690 or end.y < 330:
			edge = 40.0
		var value := minf(clearance, 60.0) * 2.0 + follow * 10.0 - edge
		if value > best_value:
			best_value = value
			best_move = h
	return best_move

func steer(v: Vector2) -> void:
	var want := {
		scheme.left: v.x < -0.3, scheme.right: v.x > 0.3,
		scheme.up: v.y < -0.3, scheme.down: v.y > 0.3}
	for code in want:
		if want[code]:
			hold(code, KEY_NAMES[code])
		else:
			release(code)

func stop_moving() -> void:
	for code in [scheme.left, scheme.right, scheme.up, scheme.down]:
		release(code)

## Fly the current stage until it leaves "play" (clear or over) or max_frames pass.
func play_stage(max_frames: int, shoot := true, each_frame := Callable()) -> String:
	var n := 0
	var last_lives := -1
	var last_spread := 0.0
	var last_pickups := 0
	var s := stage()
	while n < max_frames:
		s = stage()
		if s == null or s.state != "play":
			break
		if paused:
			expect(false, "game paused itself during play (focus loss?)")
			break
		var p := player()
		if last_lives >= 0 and p.lives < last_lives:
			note("player_hit", {"lives": p.lives})
			stats["hits"] = stats.get("hits", 0) + 1
		elif last_lives >= 0 and p.lives > last_lives:
			note("heart_collected", {"lives": p.lives})
			stats["hearts"] = stats.get("hearts", 0) + 1
		last_lives = p.lives
		if p.spread_time > last_spread + 1.0:
			note("triple_shot_collected")
			stats["triples"] = stats.get("triples", 0) + 1
		last_spread = p.spread_time
		var k := get_nodes_in_group("pickups").size()
		if k > last_pickups:
			note("pickup_dropped", {"count": k})
		last_pickups = k
		if shoot:
			hold(fire_key, KEY_NAMES[fire_key])
		else:
			release(fire_key)
		if each_frame.is_valid() and each_frame.call(n) == true:
			break
		steer(heading())
		await process_frame
		n += 1
	stop_moving()
	release(fire_key)
	s = stage()
	return s.state if s else scene_name()

func wait_stage_play(label: String) -> bool:
	return await wait_until(func(): return stage() != null and stage().state == "play", 240, label + " reaches GO")

func in_scene(name: String) -> bool:
	return scene_name() == name

# --- takes ---

func run() -> void:
	await wait_until(func(): return in_scene("MainMenu"), 120, "main menu loaded")
	match take:
		"campaign": await take_campaign()
		"defeat": await take_defeat()
		"extras": await take_extras()
		_: expect(false, "unknown take " + take)
	await finish()

func take_campaign() -> void:
	mark("menu")
	await wait(75)
	await press_button("How to Play")
	await wait_until(func(): return in_scene("Instructions"), 60, "instructions open")
	mark("instructions")
	await wait(150)
	await key(KEY_ESCAPE, "Esc")
	await wait_until(func(): return in_scene("MainMenu"), 60, "Esc returns to the main menu")
	await wait(40)
	await press_button("Start Game")
	await wait_until(func(): return stage() != null and stage().stage_id == 1, 60, "stage 1 loaded")

	mark("stage1")
	scheme = WASD
	fire_key = KEY_J
	await wait_stage_play("stage 1")
	var focus_demo := func(n: int) -> void:
		if n == 150:
			hold(KEY_SHIFT, "Shift")
			note("focus_on")
		elif n == 240:
			release(KEY_SHIFT)
			note("focus_off")
	var result := await play_stage(240 * 30, true, focus_demo)
	release(KEY_SHIFT)
	expect(result == "clear", "stage 1 cleared (score %d)" % stage().score)
	await wait_until(func(): return in_scene("StageClear"), 150, "stage clear screen")
	mark("clear1")
	await wait(120)
	await press_button("Go to Stage 2")
	await wait_until(func(): return stage() != null and stage().stage_id == 2, 60, "stage 2 loaded")

	mark("stage2")
	scheme = ARROWS
	fire_key = KEY_SPACE
	await wait_stage_play("stage 2")
	result = await play_stage(240 * 30)
	expect(result == "clear", "stage 2 cleared (score %d)" % stage().score)
	await wait_until(func(): return in_scene("StageClear"), 150, "second stage clear screen")
	mark("clear2")
	await wait(120)
	await press_button("Go to Stage 3")
	await wait_until(func(): return stage() != null and stage().stage_id == 3, 60, "stage 3 loaded")

	mark("stage3")
	scheme = WASD
	fire_key = KEY_J
	await wait_stage_play("stage 3")
	var boss_watch := func(_n: int) -> void:
		var b = stage().boss
		if is_instance_valid(b):
			if b.state == "fight" and not stats.has("boss_fight_at"):
				stats["boss_fight_at"] = frame
				note("boss_fight")
			if b.enraged() and not stats.has("enraged_at"):
				stats["enraged_at"] = frame
				note("boss_enraged", {"hp": b.health})
	result = await play_stage(240 * 30, true, boss_watch)
	expect(result == "clear", "Cerberus defeated (score %d)" % stage().score)
	await wait_until(func(): return in_scene("GameClear"), 200, "credits scene")
	mark("credits")
	await wait_until(func(): return current_scene.finished, 30 * 30, "credits stop scrolling")
	await wait(75)
	await press_button("Main Menu")
	await wait_until(func(): return in_scene("MainMenu"), 60, "back on the main menu")
	mark("menu_after")
	await wait(90)
	expect(root.get_node("GameState").best_score > 0, "best score shown on the main menu")

func take_defeat() -> void:
	mark("menu")
	await wait(40)
	await press_button("Start Game")
	await wait_until(func(): return stage() != null and stage().stage_id == 1, 60, "stage 1 loaded")
	mark("collide")
	scheme = WASD
	fire_key = KEY_J
	await wait_stage_play("stage 1")
	kamikaze = true
	var result := await play_stage(90 * 30, false)
	kamikaze = false
	expect(result == "over", "three monster contacts end the stage")
	await wait_until(func(): return stage().game_over_menu.visible, 90, "game over menu")
	expect(paused, "tree paused under the game over menu")
	mark("game_over")
	await wait(120)
	await press_button("Try Again")
	await wait_until(func(): return stage() != null and stage().state == "intro", 60, "retry reloads stage 1")
	expect(stage().score == 0 and player().lives == 3, "retry resets score and lives")
	mark("retry")
	await wait_stage_play("stage 1 retry")
	await play_stage(150)
	await key(KEY_ESCAPE, "Esc")
	await wait_until(func(): return stage().pause_menu.visible, 10, "pause menu")
	mark("pause_menu")
	await wait(60)
	await press_button("Main Menu")
	await wait_until(func(): return in_scene("MainMenu"), 60, "main menu from pause")
	await wait(45)

func take_extras() -> void:
	mark("menu_audio")
	await wait(40)
	await press_button("Audio On")
	await wait(20)
	expect(not root.get_node("Audio").enabled, "menu button turns audio off")
	await wait(30)
	await press_button("Audio Off")
	await wait(20)
	expect(root.get_node("Audio").enabled, "menu button turns audio back on")
	await wait(30)
	await press_button("Start Game")
	await wait_until(func(): return stage() != null, 60, "stage 1 loaded")
	mark("keys")
	scheme = ARROWS
	fire_key = KEY_Z
	await wait_stage_play("stage 1")
	await play_stage(120)
	mark("mouse_fire")
	await move(Vector2(1180, 690), 12)
	set_fire(true)
	await play_stage(120, false)
	set_fire(false)
	mark("sound_key")
	await key(KEY_M, "M")
	await wait(2)
	expect(not root.get_node("Audio").enabled, "M turns sound off")
	await play_stage(75)
	await key(KEY_M, "M")
	await wait(2)
	expect(root.get_node("Audio").enabled, "M turns sound back on")
	await play_stage(45)
	mark("pause_p")
	await key(KEY_P, "P")
	await wait_until(func(): return stage().pause_menu.visible and paused, 10, "P pauses")
	await wait(45)
	await press_button("Audio On")
	await wait(20)
	expect(not root.get_node("Audio").enabled, "pause-menu button turns audio off")
	await wait(25)
	await press_button("Audio Off")
	await wait(25)
	await press_button("Resume")
	await wait_until(func(): return not paused, 10, "Resume unpauses")
	await play_stage(60)
	mark("restart_r")
	await key(KEY_ESCAPE, "Esc")
	await wait_until(func(): return stage().pause_menu.visible, 10, "Esc pauses")
	await wait(40)
	await key(KEY_R, "R")
	await wait_until(func(): return stage() != null and stage().state == "intro", 30, "R restarts the stage")
	await wait_stage_play("stage 1 after restart")
	mark("pad")
	await pad_play(240)
	mark("pad_pause")
	joy_button(JOY_BUTTON_START, true, "Start")
	await wait(2)
	joy_button(JOY_BUTTON_START, false, "Start")
	await wait_until(func(): return stage().pause_menu.visible, 10, "Start pauses")
	await wait(45)
	joy_button(JOY_BUTTON_START, true, "Start")
	await wait(2)
	joy_button(JOY_BUTTON_START, false, "Start")
	await wait_until(func(): return not paused, 10, "Start resumes")
	await pad_play(45)
	mark("hit_then_heart")
	kamikaze = true
	var hit_by := func(_n: int) -> bool:
		if player().lives < 3 and kamikaze:
			kamikaze = false
			note("one_hit_taken")
			return true
		return false
	await play_stage(20 * 30, false, hit_by)
	kamikaze = false
	expect(player().lives == 2, "one monster contact costs one life")
	var healed := func(_n: int) -> bool:
		if player().lives == 3 and not stats.has("healed_at"):
			stats["healed_at"] = frame
			return true
		return false
	var n := 0
	while not stats.has("healed_at") and n < 90 * 30 and stage().state == "play":
		await play_stage(30, true, healed)
		n += 30
	expect(stats.has("healed_at"), "a heart drop restores the lost life")
	await play_stage(60)
	await key(KEY_ESCAPE, "Esc")
	await wait(40)
	await press_button("Main Menu")
	await wait_until(func(): return in_scene("MainMenu"), 60, "main menu")
	await wait(45)

## The same autopilot, steering through the left stick; A fires, LB focuses.
func pad_play(frames: int) -> void:
	joy_button(JOY_BUTTON_A, true, "A")
	var focus := false
	var last := Vector2(99, 99)
	for n in range(frames):
		var s := stage()
		if s == null or s.state != "play":
			break
		if n == 120 and not focus:
			focus = true
			joy_button(JOY_BUTTON_LEFT_SHOULDER, true, "LB")
		elif n == 200 and focus:
			focus = false
			joy_button(JOY_BUTTON_LEFT_SHOULDER, false, "LB")
		var v := heading()
		if v.distance_to(last) > 0.05:
			joy_axis(JOY_AXIS_LEFT_X, v.x, "left_x")
			joy_axis(JOY_AXIS_LEFT_Y, v.y, "left_y")
			last = v
		await process_frame
	joy_axis(JOY_AXIS_LEFT_X, 0.0, "left_x")
	joy_axis(JOY_AXIS_LEFT_Y, 0.0, "left_y")
	if focus:
		joy_button(JOY_BUTTON_LEFT_SHOULDER, false, "LB")
	joy_button(JOY_BUTTON_A, false, "A")
