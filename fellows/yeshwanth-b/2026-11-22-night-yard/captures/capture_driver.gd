extends SceneTree

# Scripted-input capture driver for Night Yard (film evidence, not a playtest).
#   godot --path <capture copy> --fixed-fps 60 --script res://harness/capture_driver.gd -- <take> <out> [nosave] [seed=N]
# The engine runs one 60 Hz physics tick per frame (as the game is tuned); every second
# rendered frame is saved, so the film is 30 fps of game time.
# Plays only through Input.parse_input_event (keys, mouse, joypad). It reads game
# state to decide what to press and to assert outcomes; it never writes game
# state, never calls game methods and never teleports.
# In the levels, the decisions come from the game's own bot brain (scripts/ai.gd in
# autopilot mode, as _tools/playtest.gd uses it), run on the driver's side: the
# brain is NOT attached to the player (player.brain stays null, so the player reads
# Input like a person's game), and each tick its eight input flags are turned into
# key presses (A D W S Space J K Shift) sent with Input.parse_input_event.

const FPS := 30.0                    ## video frames a second: take timings are written in these units
const STEP := 2                      ## engine frames per video frame (--fixed-fps 60, every 2nd frame saved)
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
		elif a.begins_with("level="):
			set("trial_level_id", int(a.get_slice("=", 1)))
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

var _draws := 0
func _save_frame() -> void:
	if nosave:
		return
	iterations_since_draw = 0
	_draws += 1
	if _draws % STEP != 1 and STEP > 1:
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
var _procs := 0
func _process(_delta: float) -> bool:
	_bridge_apply()
	if nosave:
		_procs += 1
		if _procs % STEP == 0:
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

func player():
	var l := level()
	return l.player if l else null

func snapshot() -> Dictionary:
	var d := {"scene": scene_name(), "paused": paused}
	var l := level()
	if l:
		d["level"] = l.level_id
		d["score"] = l.score
		d["gate_open"] = l.gate_open
		d["finished"] = l.finished
		d["kos"] = l.kos
		d["deaths"] = l.deaths
		var p = l.player
		if is_instance_valid(p):
			var g: Vector3 = p.global_position
			d["pos"] = [snappedf(g.x, 0.1), snappedf(g.y, 0.1)]
			d["hp"] = snappedf(p.hp, 0.1)
			d["state"] = p.S.keys()[p.state]
			d["attack"] = p.attack_id
			d["holding"] = p.holding != null
		if l.boss and is_instance_valid(l.boss):
			d["boss_hp"] = snappedf(l.boss.hp, 0.1)
	var gs := root.get_node_or_null("GameState")
	if gs:
		d["unlocked"] = gs.unlocked_level
		d["fighter"] = gs.selected_fighter
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
	for i in range(n * STEP):
		await process_frame

func wait_until(cond: Callable, max_frames: int, label: String) -> bool:
	var n := 0
	while not cond.call() and n < max_frames * STEP:
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
		await wait(1)

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


# --- the bridge: the game's own bot brain decides, the driver presses the keys ---

const BRIDGE_KEYS := {"l": [KEY_A, "A"], "r": [KEY_D, "D"], "u": [KEY_W, "W"], "d": [KEY_S, "S"],
	"j": [KEY_SPACE, "Space"], "a": [KEY_J, "J"], "b": [KEY_K, "K"], "t": [KEY_SHIFT, "Shift"]}
var brain: Node = null
var bridge_on := false
var bridge_level = null
var _skipped := {}
var _goal_since := 0.0
var _last_goal = null

func bridge_start() -> void:
	var l := level()
	brain = load("res://scripts/ai.gd").new()
	brain.fighter = l.player
	brain.level = l
	brain.autopilot = true
	root.add_child(brain)            # NOT the player's brain: player.brain stays null
	bridge_level = l
	_skipped = {}
	_goal_since = 0.0
	_last_goal = null
	bridge_on = true
	note("bridge_on", {"level": l.level_id, "player_brain_is_null": l.player.brain == null})

func bridge_stop() -> void:
	if not bridge_on:
		return
	bridge_on = false
	for k in BRIDGE_KEYS:
		release(BRIDGE_KEYS[k][0])
	if is_instance_valid(brain):
		brain.queue_free()
	brain = null
	note("bridge_off")

## The goal choice of _tools/playtest.gd (nearest light, else a bot, else the gate; the boss first).
func _bridge_goal(l, p, dt: float) -> void:
	var goal = null
	if l.data.get("boss", false) and l.boss and not l.boss.is_dead():
		goal = l.boss
	elif not l.gate_open:
		var best := INF
		for q in l.pickups:
			if _skipped.has(q):
				continue
			var dd: float = absf(q.global_position.x - p.global_position.x) + absf(q.global_position.y - p.global_position.y) * 2.0
			if dd < best:
				best = dd
				goal = q
		if goal == null:
			for e in l.alive_enemies():
				if not _skipped.has(e):
					goal = e
					break
	if goal == null:
		brain.goal = Vector3(l.gate_x + 2.0, 2.0, 0)
	else:
		brain.goal = goal.global_position
		if l.pickups.has(goal):
			brain.goal.y = floorf(goal.global_position.y)
	if goal != _last_goal:
		_last_goal = goal
		_goal_since = 0.0
	_goal_since += dt
	if goal != null and brain.goal_blocked and _goal_since > 3.0:
		_skipped[goal] = true
		brain.goal_blocked = false
	if goal != null and _goal_since > 30.0 and goal != l.boss:
		_skipped[goal] = true
		note("goal_skipped", {"after_s": 30})

func _physics_process(delta: float) -> bool:
	if not bridge_on:
		return false
	var l := level()
	if l == null or l != bridge_level or not is_instance_valid(brain):
		bridge_stop()
		return false
	var p = l.player
	if paused:
		return false
	_bridge_goal(l, p, delta)
	brain.think(delta)
	# The engine applies input once per frame and runs two physics ticks per frame, so the
	# brain's wishes are collected over the frame's ticks (a key wanted on either tick is
	# pressed) and sent once per frame from _process: a one-tick tap still lasts a frame.
	for k in BRIDGE_KEYS:
		if brain.get(k):
			_want[k] = true
	return false

var _want := {}
func _bridge_apply() -> void:
	if not bridge_on:
		_want = {}
		return
	for k in BRIDGE_KEYS:
		var code: Key = BRIDGE_KEYS[k][0]
		var want: bool = _want.get(k, false)
		if want and not held.has(code):
			hold(code, BRIDGE_KEYS[k][1])
		elif not want and held.has(code):
			release(code)
	_want = {}

# --- takes -------------------------------------------------------------------------

func run() -> void:
	await wait(45)
	match take:
		"campaign":
			await take_campaign()
		"defeat":
			await take_defeat()
		"extras":
			await take_extras()
		"trial_level":
			await take_trial_level()
		"trial_pause":
			await take_trial_pause()
		_:
			note("unknown_take", {"take": take})
			failed = true
	await finish()

func wait_scene(name: String, max_frames: int = 300) -> bool:
	return await wait_until(func(): return scene_name() == name, max_frames, "scene " + name)

func wait_level(id: int) -> bool:
	var ok := await wait_until(func(): return level() != null and level().level_id == id and is_instance_valid(level().player), 400, "level %d loaded" % id)
	await wait(20)
	return ok

## Play the current level with the bridge until its gate is walked through.
func play_level(id: int, limit_s: float = 300.0) -> void:
	mark("level_%02d" % id)
	await wait_level(id)
	var l := level()
	# the banner: let the level title show before moving
	await wait(75)
	bridge_start()
	# stall guard: no new ground and no score for 60 s -> Restart level from the pause menu (logged)
	var restarts := 0
	var best_x := -INF
	var last_score := -1
	var idle := 0
	var n := 0
	while n < int(limit_s * FPS) and not (level() == l and l.finished):
		await wait(1)
		n += 1
		if level() != l:
			break
		var px: float = l.player.global_position.x
		var boss_hp: float = l.boss.hp if l.boss and is_instance_valid(l.boss) else 0.0
		var progress: float = px + l.score * 10.0 - boss_hp * 5.0
		if progress > best_x + 0.5:
			best_x = progress
			idle = 0
		else:
			idle += 1
		if idle > int(60 * FPS) and restarts < 2:
			restarts += 1
			note("stall_restart", {"level": id, "x": snappedf(px, 0.1), "score": l.score})
			bridge_stop()
			release_all()
			await key(KEY_ESCAPE, "Esc")
			await wait(30)
			await press_button("Restart level")
			await wait_until(func(): return level() != null and level() != l, 120, "restarted")
			await wait_level(id)
			l = level()
			await wait(75)
			bridge_start()
			best_x = -INF
			idle = 0
	var ok: bool = level() == l and l.finished
	expect(ok, "level %d finished" % id)
	bridge_stop()
	release_all()
	if ok:
		var s: Dictionary = l.player.stats
		stats["L%d" % id] = {"time": snappedf(l.time, 0.1), "score": l.score, "kos": l.kos, "deaths": l.deaths,
			"jumps": s["jumps"], "grabs": s["grabs"], "climbs": s["climbs"], "wall_jumps": s["wall_jumps"],
			"slides": s["slides"], "throws": s["throws"], "hammers": s["hammers"], "takedowns": s["takedowns"],
			"stomps": s["stomps"], "hits": s["hits"], "blocks": s["blocks"]}
		note("level_done", stats["L%d" % id])
		var checks := {1: {"grabs": 1}, 2: {"wall_jumps": 1, "climbs": 3}, 3: {"throws": 1}, 4: {"takedowns": 1, "slides": 1}, 5: {"hammers": 1}}
		for k in checks.get(id, {}):
			note("signature_move", {"level": id, "move": k, "count": s[k], "playtest_expects": checks[id][k]})
		if id == 6:
			expect(l.boss != null and l.boss.is_dead(), "the Forewoman is down")

func complete_panel(next_text: String) -> void:
	await wait_until(func(): return find_button(next_text) != null and find_button(next_text).get_parent().get_parent().get_parent().modulate.a > 0.95, 200, "level-clear panel")
	await wait(70)
	await press_button(next_text)

func choose_fighter(key: String) -> void:
	# hover each Y Bot (the hover light follows the mouse), then click the chosen one
	var cs := scene()
	var cam: Camera3D = cs.camera
	for k in ["YELLOW", "RED", "GREEN"]:
		var pos: Vector3 = (cs.bots[k] as Node3D).position + Vector3(0, 1.0, 0)
		await move(cam.unproject_position(pos), 20)
		await wait(20)
	var target: Vector3 = (cs.bots[key] as Node3D).position + Vector3(0, 1.0, 0)
	await click(cam.unproject_position(target), "Y Bot " + key, 20)
	await wait(50)
	expect(cs.selected == key, "selected " + key)

func take_campaign() -> void:
	mark("menu")
	await wait_scene("MainMenu")
	await wait(60)
	await press_button("How to play")
	await wait_scene("Instructions")
	await wait(200)
	await press_button("Back")
	await wait_scene("MainMenu")
	await wait(30)
	await press_button("New game")
	mark("character_select")
	await wait_scene("CharacterSelect")
	await wait(40)
	await choose_fighter("YELLOW")
	await press_button("Play")
	for id in range(1, 7):
		await play_level(id)
		await complete_panel("Credits" if id == 6 else "Next level")
	mark("credits")
	await wait_scene("Credits", 300)
	await wait_until(func(): return scene_name() == "MainMenu", int(90 * FPS), "credits return to the menu")
	await wait(60)

## The game times a double tap (which turns on running) on the wall clock, 0.18 s. Headless
## trials run far faster than real time, so a manual press right after the bridge's own press
## could count as a double tap; a short real-time pause keeps trials like the recording.
func real_pause() -> void:
	OS.delay_msec(300)

func walk_to_x(x: float, run: bool = false, max_frames: int = 600) -> bool:
	real_pause()
	var p = player()
	var code := KEY_D if x > p.global_position.x else KEY_A
	if run:
		hold(KEY_SHIFT, "Shift")
	hold(code, "D" if code == KEY_D else "A")
	var ok := await wait_until(func(): return (player().global_position.x >= x) if code == KEY_D else (player().global_position.x <= x), max_frames, "walk to x %.1f" % x)
	release(code)
	release(KEY_SHIFT)
	return ok

func take_defeat() -> void:
	mark("menu")
	await wait_scene("MainMenu")
	await wait(40)
	await press_button("Select level")
	await wait(60)
	await press_button("01")
	await wait_level(1)
	await wait(75)
	var l := level()
	# the bridge plays up to the ground just past the first block, then the driver walks into the pit
	mark("to_pit")
	bridge_start()
	await wait_until(func(): return player().global_position.x > 21.2 and player().global_position.x < 24.0 and player().is_on_floor() and player().global_position.y < 2.5, int(60 * FPS), "on the ground before the pit")
	bridge_stop()
	release_all()
	await wait(30)
	mark("fall")
	real_pause()
	hold(KEY_D, "D")
	await wait_until(func(): return player().global_position.y < -1.0 or l.deaths >= 1, 200, "walked into the pit")
	release(KEY_D)
	await wait_until(func(): return l.deaths >= 1, 200, "the fall counts as a K.O.")
	await wait_until(func(): return not player().is_dead() and player().global_position.x < 6.0, 200, "back at the start")
	await wait(40)
	# the bridge brings the player to the checkpoint before the spike plates
	mark("to_spikes")
	bridge_start()
	await wait_until(func(): return player().global_position.x > 63.5 and player().global_position.x < 66.0 and player().is_on_floor(), int(150 * FPS), "reached the checkpoint before the plates")
	bridge_stop()
	release_all()
	await wait(30)
	mark("spikes")
	var d0: int = l.deaths
	real_pause()
	hold(KEY_D, "D")
	await wait_until(func(): return player().global_position.x >= 67.2 or l.deaths > d0, 160, "stepped onto the spike plate")
	release(KEY_D)
	await wait_until(func(): return l.deaths > d0, 150, "the spike plate kills")
	await wait_until(func(): return not player().is_dead(), 200, "respawned at the checkpoint")
	await wait(40)
	expect(player().global_position.x > 60.0 and player().global_position.x < 67.0, "respawn at the checkpoint, not the start")
	# pause, R restarts while paused
	mark("pause")
	await key(KEY_ESCAPE, "Esc")
	await wait(60)
	expect(paused, "Esc pauses")
	await key(KEY_R, "R")
	await wait_until(func(): return level() != null and level() != l, 120, "R restarts the level while paused")
	await wait_level(1)
	l = level()
	await wait(60)
	await key(KEY_ESCAPE, "Esc")
	await wait(40)
	await press_button("Options")
	await wait(90)
	await press_button("Back")
	await wait(30)
	await press_button("Resume")
	await wait(40)
	expect(not paused, "Resume unpauses")
	# Found while capturing: after Options -> Back from the pause menu, the hidden OptionsPanel
	# (options_panel.gd:52-55 checks its own `visible`) takes every pause press.
	await key(KEY_ESCAPE, "Esc")
	await wait(40)
	note("defect_options_eats_pause", {"tree_paused": paused, "pause_panel_shown": find_button("Quit to menu") != null})
	await press_button("Quit to menu")
	await wait_scene("MainMenu")
	await wait(45)

func moves_demo() -> void:
	# a showcase of the move list on level 1's open floor, keys only
	var p = player()
	mark("moves")
	await key(KEY_J, "J")
	await wait(9)
	await key(KEY_J, "J")
	await wait(9)
	await key(KEY_J, "J")
	await wait(40)
	note("combo", {"attack": p.attack_id})
	hold(KEY_W, "W")
	await key(KEY_J, "J")
	release(KEY_W)
	await wait(45)
	hold(KEY_K, "K")
	await wait(40)
	release(KEY_K)
	await wait(15)
	hold(KEY_S, "S")
	await key(KEY_J, "J")
	release(KEY_S)
	await wait(75)
	expect(p.stats["hammers"] >= 1, "S + attack brings down the hammer")
	hold(KEY_SPACE, "Space")
	await wait(12)
	release(KEY_SPACE)
	await wait(30)
	await key(KEY_SPACE, "Space")
	await wait(30)

func take_extras() -> void:
	mark("menu")
	await wait_scene("MainMenu")
	await wait(40)
	await press_button("Options")
	await wait(110)
	await press_button("Back")
	await wait(30)
	mark("change_fighter")
	await press_button("Change fighter")
	await wait_scene("CharacterSelect")
	await wait(40)
	# arrow keys choose too
	await key(KEY_RIGHT, "Right")
	await wait(50)
	await key(KEY_RIGHT, "Right")
	await wait(50)
	await key(KEY_LEFT, "Left")
	await wait(50)
	var cs := scene()
	expect(cs.selected != "", "arrow keys select a fighter")
	note("fighter", {"selected": cs.selected})
	await key(KEY_ENTER, "Enter")
	await wait_scene("MainMenu")
	await wait(30)
	mark("select_level")
	await press_button("Select level")
	await wait(100)
	await press_button("01")
	await wait_level(1)
	await wait(75)
	await moves_demo()
	mark("run_slide")
	hold(KEY_SHIFT, "Shift")
	hold(KEY_D, "D")
	await wait(30)
	hold(KEY_S, "S")
	await wait(30)
	release(KEY_S)
	release(KEY_D)
	release(KEY_SHIFT)
	await wait(30)
	mark("gamepad")
	joy_axis(JOY_AXIS_LEFT_X, 0.9, "left stick right")
	await wait(45)
	joy_button(JOY_BUTTON_A, true, "A")
	await wait(10)
	joy_button(JOY_BUTTON_A, false, "A")
	await wait(35)
	joy_axis(JOY_AXIS_LEFT_X, 0.0, "left stick")
	await wait(10)
	for i in 3:
		joy_button(JOY_BUTTON_X, true, "X")
		await wait(3)
		joy_button(JOY_BUTTON_X, false, "X")
		await wait(10)
	await wait(30)
	joy_button(JOY_BUTTON_START, true, "Start")
	await wait(2)
	joy_button(JOY_BUTTON_START, false, "Start")
	await wait(50)
	expect(paused, "Start pauses")
	await press_button("Quit to menu")
	await wait_scene("MainMenu")
	await wait(30)
	mark("credits")
	await press_button("Credits")
	await wait_scene("Credits")
	await wait(240)
	await key(KEY_ESCAPE, "Esc")
	await wait(60)
	await wait_until(func(): return scene_name() == "MainMenu", 600, "back to the menu")
	await wait(30)

## Trials only (never recorded): load one level directly and log the player every 2 s.
var trial_level_id := 1
func take_trial_level() -> void:
	change_scene_to_file("res://scenes/level_%02d.tscn" % trial_level_id)
	await wait_level(trial_level_id)
	await wait(75)
	var l := level()
	bridge_start()
	var n := 0
	while n < int(300 * FPS) and not l.finished:
		await wait(1)
		n += 1
		if n % 60 == 0:
			var p = l.player
			note("trace", {"x": snappedf(p.global_position.x, 0.1), "y": snappedf(p.global_position.y, 0.1), "state": p.S.keys()[p.state],
				"link": brain._link.kind if brain._link else "-", "goal": [snappedf(brain.goal.x, 0.1), snappedf(brain.goal.y, 0.1)], "score": l.score,
				"keys": held.values()})
	expect(l.finished, "trial level finished")
	bridge_stop()

## Trials only: the pause key after Resume.
func take_trial_pause() -> void:
	change_scene_to_file("res://scenes/level_01.tscn")
	await wait_level(1)
	await wait(60)
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	note("A1 after Esc", {"paused": paused})
	await press_button("Resume")
	await wait(30)
	note("A2 after Resume click", {"paused": paused, "focus": str(root.gui_get_focus_owner())})
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	note("A3 Esc after Resume click", {"paused": paused})
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	note("A4 Esc again", {"paused": paused})
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	note("B1 Esc", {"paused": paused})
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	note("B2 Esc toggles off", {"paused": paused})
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	note("B3 Esc toggles on", {"paused": paused})
	await press_button("Resume")
	await wait(30)
	await move(Vector2(200, 650), 10)
	await wait(10)
	note("C1 mouse moved off the button", {"focus": str(root.gui_get_focus_owner())})
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	note("C2 Esc", {"paused": paused})
