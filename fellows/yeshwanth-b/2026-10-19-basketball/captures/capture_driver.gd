extends SceneTree
## Film-capture harness for Basketball Blaster: Fowl Play. NOT part of the game.
##
## Boots the scene named in project.godot (run/main_scene) and plays only through
## Input.parse_input_event: keyboard keys, mouse motion, mouse buttons and joypad
## events. It reads game state to decide WHEN and WHERE to press, and asserts
## outcomes. It never writes game state, never calls game methods, never teleports.
##
## Every drawn frame of the root viewport (the engine's own render) is streamed
## to ffmpeg as raw RGB. A JSONL log records each input and assertion by frame.
## On menus the OS cursor is not in the viewport texture, so a white arrow is drawn
## on a harness CanvasLayer (layer 128) at the synthetic mouse position. In the
## arenas the game hides the OS cursor and draws its own crosshair.
##
## Usage: harness/run_take.sh <take> <out_dir>  (runs Godot and a chunk encoder)

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
var last_grenade_frame := -9999
var megakill_seen := 0
var stats := {}
var nosave := false
const CHUNK := 150
var chunk_file: FileAccess
var chunk_index := 0
var seen_fx := {}

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
	ring = maxf(0.0, ring - 1.0 / 12.0)

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

func arena() -> Node:
	var s := current_scene
	return s if s and "level_id" in s else null

func snapshot() -> Dictionary:
	var s := current_scene
	var d := {"scene": s.scene_file_path.get_file().get_basename() if s else ""}
	var a := arena()
	if a and is_instance_valid(a.player):
		d.merge({"level": a.level_id, "lives": a.lives, "health": a.health, "kills": a.kills,
			"eggs": a.eggs_collected, "need": a.eggs_needed, "chickens": get_nodes_in_group("chickens").size(),
			"pos": [snappedf(a.player.global_position.x, 1), snappedf(a.player.global_position.y, 1)],
			"fuel": snappedf(a.player.jetpack_fuel, 0.01), "paused": paused})
	return d

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

func screen_of(world: Vector2) -> Vector2:
	return current_scene.get_viewport().get_canvas_transform() * world

func finish() -> void:
	release_all()
	await wait(4)
	note("end", {"failed": failed, "megakills": megakill_seen, "stats": stats})
	log_file.close()
	RenderingServer.frame_post_draw.disconnect(_save_frame)
	_close_chunk()
	if not nosave:
		FileAccess.open(out_dir + "/frames/DONE", FileAccess.WRITE).store_line(str(frame))
	quit(1 if failed else 0)

# --- the arena autopilot: observes positions, outputs only key/mouse events ---

func live_chickens() -> Array:
	var out := []
	for c in get_nodes_in_group("chickens"):
		if is_instance_valid(c) and not c.dead:
			out.append(c)
	return out

func nearest_chicken(p: Vector2, max_d: float) -> Node:
	var best: Node = null
	var bd := max_d
	for c in live_chickens():
		var d := p.distance_to(c.global_position)
		if d < bd:
			bd = d
			best = c
	return best

func cluster_at(p: Vector2) -> Array:
	## Best grenade target: the chicken with the most neighbours inside the blast radius.
	var best := []
	for c in live_chickens():
		var group := []
		for o in live_chickens():
			if c.global_position.distance_to(o.global_position) <= 200.0:
				group.append(o)
		if group.size() > best.size() and p.distance_to(c.global_position) > 160.0 and p.distance_to(c.global_position) < 620.0:
			best = group
	return best

## One frame of steering toward `target` (a nest position), with shooting.
## Returns nothing; inputs are held/released as events.
var air_jumps := 0
var was_floor := true
func steer(target: Vector2, shoot := true, grenades := true) -> void:
	var a := arena()
	var pl = a.player
	var p: Vector2 = pl.global_position
	var standing_y := target.y + 30.0 - 54.0
	var dx := target.x - p.x
	var dy := p.y - standing_y      ## > 0: target is above
	var on_floor: bool = pl.is_on_floor()
	# horizontal
	if dx > 14.0:
		release(KEY_A, "A"); hold(KEY_D, "D")
	elif dx < -14.0:
		release(KEY_D, "D"); hold(KEY_A, "A")
	else:
		release(KEY_A, "A"); release(KEY_D, "D")
	# vertical
	if on_floor and not was_floor:
		air_jumps = 0
	was_floor = on_floor
	if dy > 24.0:
		release(KEY_S, "S")
		if on_floor:
			if absf(dx) < 260.0 or dy > 150.0:
				await key(KEY_SPACE, "Space")
				air_jumps = 1
		elif pl.velocity.y > -120.0 and air_jumps == 1 and pl.double_jump_available:
			await key(KEY_SPACE, "Space")
			air_jumps = 2
		elif air_jumps >= 2 and pl.velocity.y > 0.0 and dy > 40.0 and pl.jetpack_fuel > 0.2:
			hold(KEY_SHIFT, "Shift")
		if held.has(KEY_SHIFT) and (dy < 0.0 or pl.jetpack_fuel <= 0.05):
			release(KEY_SHIFT, "Shift")
	else:
		release(KEY_SHIFT, "Shift")
		if dy < -40.0 and on_floor and absf(dx) < 200.0 and p.y < 1034.0 - 10.0:  # feet above the ground row: on a platform
			hold(KEY_S, "S")
			await process_frame
			await key(KEY_SPACE, "Space (with S: drop)")
			release(KEY_S, "S")
	# aim + shoot
	var c := nearest_chicken(p, 760.0) if shoot else null
	if c:
		var aim := screen_of(c.global_position + c.velocity * 0.12)
		_motion(mouse.lerp(aim, 0.45))
		set_fire(true)
		if grenades and frame - last_grenade_frame > 150 and pl.grenade_cooldown <= 0.0:
			var group := cluster_at(p)
			if group.size() >= 2:
				var centre := Vector2.ZERO
				for g in group:
					centre += g.global_position
				centre /= group.size()
				_motion(screen_of(centre + Vector2(0, -60)))
				await process_frame
				await right_click("grenade at a cluster of %d" % group.size())
				last_grenade_frame = frame
	else:
		set_fire(false)
		var ahead := p + Vector2(260.0 * signf(dx if dx != 0.0 else 1.0), -40.0)
		_motion(mouse.lerp(screen_of(ahead), 0.2))

## Hold a spot on the ground away from the nests and fight: shoot, and grenade
## clusters. Ends after `max_frames`, or once a mega kill has been seen and at least 10 kills.
func fight(spot: Vector2, max_frames: int) -> void:
	var a := arena()
	var n := 0
	while n < max_frames and not a.game_finished:
		if a.respawning or paused:
			release_all()
		else:
			await steer(spot)
		await process_frame
		n += 1
		for fx in a.effects.get_children():
			if fx is Label and fx.text == "MEGA KILL!" and not seen_fx.has(fx.get_instance_id()):
				seen_fx[fx.get_instance_id()] = true
				megakill_seen += 1
				note("megakill_seen", {"count": megakill_seen})
		if (megakill_seen > 0 and a.kills >= 10) or a.lives <= 1:
			break
	release_all()
	note("fight_result", {"frames": n, "kills": a.kills, "megakills": megakill_seen})

func nearest_nest(p: Vector2) -> Node2D:
	var best: Node2D = null
	var bd := INF
	for n in arena().nests:
		if is_instance_valid(n):
			# prefer the same height band: vertical distance costs more than horizontal
			var d := absf(n.global_position.x - p.x) + 1.6 * absf(n.global_position.y - p.y)
			if d < bd:
				bd = d
				best = n
	return best

## Play the current arena to completion (or until lives run out).
func play_arena(max_frames: int) -> bool:
	var a := arena()
	var n := 0
	var target: Node2D = null
	var stuck := 0
	var last_eggs: int = a.eggs_collected
	while is_instance_valid(a) and not a.game_finished and n < max_frames:
		if a.respawning or paused:
			release_all()
			await process_frame
			n += 1
			continue
		if not is_instance_valid(target) or not a.nests.has(target):
			target = nearest_nest(a.player.global_position)
			if target:
				note("target_egg", {"at": [target.global_position.x, target.global_position.y]})
		if target:
			await steer(target.global_position)
		await process_frame
		n += 1
		stuck += 1
		for fx in a.effects.get_children():
			if fx is Label and fx.text == "MEGA KILL!" and not seen_fx.has(fx.get_instance_id()):
				seen_fx[fx.get_instance_id()] = true
				megakill_seen += 1
				note("megakill_seen", {"count": megakill_seen})
		if a.eggs_collected != last_eggs:
			last_eggs = a.eggs_collected
			stuck = 0
			note("egg", {"collected": a.eggs_collected})
		if stuck > 900:
			note("unstick", {})
			target = null
			stuck = 0
			release_all()
			hold(KEY_SHIFT, "Shift")
			await wait(20)
			release(KEY_SHIFT, "Shift")
	release_all()
	var won: bool = is_instance_valid(a) and a.level_won
	note("arena_result", {"won": won, "frames": n})
	return won

# --- takes ---

func run() -> void:
	await wait(3)
	match take:
		"campaign": await take_campaign()
		"defeat": await take_defeat()
		"extras": await take_extras()
		_: expect(false, "unknown take")
	await finish()

func in_scene(name: String) -> bool:
	return current_scene != null and current_scene.scene_file_path.ends_with(name + ".tscn")

func take_campaign() -> void:
	mark("main_menu")
	await wait_until(func(): return in_scene("main_menu"), 60, "main menu")
	await wait(45)
	await move(find_button("Play").get_global_rect().get_center(), 30)
	await wait(20)
	await move(find_button("Quit").get_global_rect().get_center(), 30)
	await wait(20)
	mark("how_to_play")
	await press_button("How to Play")
	await wait_until(func(): return in_scene("instructions"), 30, "instructions scene")
	await wait(150)
	await press_button("Back to Menu")
	await wait_until(func(): return in_scene("main_menu"), 30, "back at menu")
	await wait(30)
	mark("briefing")
	await press_button("Play")
	await wait_until(func(): return in_scene("intro"), 30, "briefing scene")
	var intro := current_scene
	# line 1: let it type out completely
	await wait_until(func(): return intro.line_complete, 200, "line 1 typed out")
	await wait(40)
	# Finding: the prompt says "ENTER / CLICK TO CONTINUE", but a full-screen shade
	# ColorRect (mouse_filter STOP by default) consumes every click before it can
	# reach _unhandled_input, so clicking never advances the briefing.
	var line_before: int = intro.dialogue_index
	await click(Vector2(640, 600), "dialogue panel")
	await wait(20)
	expect(intro.dialogue_index == line_before, "click on the dialogue panel does not advance")
	await click(Vector2(900, 330), "above the panel")
	await wait(20)
	expect(intro.dialogue_index == line_before, "click above the panel does not advance either")
	await wait(10)
	await key(KEY_ENTER, "Enter")
	await wait(12)
	expect(intro.dialogue_index == line_before + 1 and not intro.line_complete, "Enter advanced to line 2, still typing")
	await key(KEY_ENTER, "Enter (finish line)")
	await wait(2)
	expect(intro.line_complete, "Enter completed line 2 at once")
	await wait(40)
	var guard := 0
	while in_scene("intro") and guard < 12:
		guard += 1
		await key(KEY_ENTER, "Enter")
		await wait(3)
		if in_scene("intro") and not intro.leaving:
			await wait_until(func(): return intro.line_complete, 200, "line %d typed" % (intro.dialogue_index + 1))
			await wait(36)
		else:
			break
	await wait_until(func(): return in_scene("level_1"), 90, "arena 1 loaded")
	# arena 1: show the moves first, then play it out
	mark("arena1_moves")
	await wait(70)
	await moves_demo()
	mark("arena1_fight")
	await fight(Vector2(800, 1058), 1500)
	mark("arena1_play")
	var won := await play_arena(9000)
	expect(won, "arena 1 cleared")
	stats["arena1"] = snapshot()
	mark("arena1_cleared")
	await wait_until(func(): return arena().finish_overlay.visible, 90, "court cleared overlay")
	await wait(75)
	await press_button("Next Arena")
	await wait_until(func(): return in_scene("level_2"), 90, "arena 2 loaded")
	mark("arena2_pause")
	await wait(80)
	await key(KEY_ESCAPE, "Esc")
	await wait(2)
	expect(paused and arena().pause_overlay.visible, "pause overlay up")
	await wait(80)
	await press_button("Resume")
	await wait(4)
	expect(not paused, "resumed")
	await wait(40)
	mark("arena2_continue")
	await key(KEY_ESCAPE, "Esc")
	await wait(40)
	await press_button("Main Menu")
	await wait_until(func(): return in_scene("main_menu"), 60, "menu from pause")
	await wait(30)
	expect(find_button("Continue: Arena 2") != null, "menu offers Continue: Arena 2")
	await wait(30)
	await press_button("Continue: Arena 2")
	await wait_until(func(): return in_scene("level_2"), 90, "arena 2 again")
	mark("arena2_play")
	await wait(40)
	won = await play_arena(12000)
	expect(won, "arena 2 cleared")
	stats["arena2"] = snapshot()
	await wait_until(func(): return arena().finish_overlay.visible, 90, "court cleared overlay 2")
	await wait(60)
	await press_button("Next Arena")
	await wait_until(func(): return in_scene("level_3"), 90, "arena 3 loaded")
	mark("arena3_play")
	await wait(40)
	var tries := 0
	won = await play_arena(15000)
	while not won and tries < 3 and in_scene("level_3") or (not won and tries < 3 and in_scene("defeat")):
		tries += 1
		note("arena3_retry", {"try": tries})
		await wait_until(func(): return in_scene("defeat"), 200, "defeat screen")
		await wait(60)
		await press_button("Retry Arena")
		await wait_until(func(): return in_scene("level_3"), 90, "arena 3 retry")
		await wait(40)
		won = await play_arena(15000)
	expect(won, "arena 3 cleared")
	stats["arena3"] = snapshot()
	mark("arena3_cleared")
	await wait_until(func(): return arena().finish_overlay.visible, 90, "final overlay")
	await wait(75)
	await press_button("Claim the Trophy")
	await wait_until(func(): return in_scene("victory"), 90, "victory scene")
	mark("victory")
	await wait(150)
	await press_button("Main Menu")
	await wait_until(func(): return in_scene("main_menu"), 60, "menu after victory")
	await wait(30)
	expect(find_button("Continue: Arena 2") == null and find_button("Continue: Arena 3") == null, "no Continue after the campaign")
	await wait(60)

## Movement and weapons shown one at a time near the gate, before the autopilot.
func moves_demo() -> void:
	var a := arena()
	var pl = a.player
	note("demo", {"part": "walk"})
	hold(KEY_D, "D"); await wait(36); release(KEY_D, "D"); await wait(10)
	hold(KEY_A, "A"); await wait(20); release(KEY_A, "A"); await wait(14)
	note("demo", {"part": "jump"})
	await key(KEY_SPACE, "Space"); await wait(40)
	note("demo", {"part": "double_jump"})
	await key(KEY_SPACE, "Space"); await wait(12)
	var y0: float = pl.velocity.y
	await key(KEY_SPACE, "Space")
	await process_frame
	expect(pl.velocity.y < y0 - 200.0, "second Space in mid-air re-launched upward")
	await wait_until(func(): return pl.is_on_floor(), 120, "landed after double jump")
	await wait(16)
	note("demo", {"part": "jetpack"})
	hold(KEY_SHIFT, "Shift")
	await wait(36)
	expect(pl.jetpack_fuel < 1.0, "jetpack burned fuel")
	release(KEY_SHIFT, "Shift")
	await wait_until(func(): return pl.is_on_floor(), 150, "landed after jetpack")
	await wait(20)
	note("demo", {"part": "aim_and_shoot"})
	var c := nearest_chicken(pl.global_position, 1200.0)
	var aim_at := screen_of(c.global_position) if c else screen_of(pl.global_position + Vector2(300, -80))
	await move(aim_at, 20)
	set_fire(true)
	for i in range(54):
		c = nearest_chicken(pl.global_position, 1200.0)
		if c:
			_motion(mouse.lerp(screen_of(c.global_position), 0.4))
		await process_frame
	set_fire(false)
	await wait(12)
	note("demo", {"part": "grenade"})
	var g := nearest_chicken(pl.global_position, 900.0)
	await move(screen_of(g.global_position + Vector2(0, -80)) if g else screen_of(pl.global_position + Vector2(320, -160)), 16)
	await wait(6)
	await right_click("grenade demo")
	last_grenade_frame = frame
	await wait(100)
	stats["after_demo"] = snapshot()

func take_defeat() -> void:
	mark("defeat_menu")
	await wait_until(func(): return in_scene("main_menu"), 60, "main menu")
	await wait(30)
	await press_button("Play")
	await wait_until(func(): return in_scene("intro"), 30, "briefing")
	await wait(50)
	mark("briefing_skip")
	await key(KEY_ESCAPE, "Esc (skip briefing)")
	await wait_until(func(): return in_scene("level_1"), 90, "arena 1 after skip")
	await wait(50)
	mark("gamepad")
	var pl = arena().player
	joy_axis(JOY_AXIS_LEFT_X, 1.0, "left stick right")
	await wait(30)
	joy_axis(JOY_AXIS_LEFT_X, 0.0, "left stick centre")
	joy_axis(JOY_AXIS_RIGHT_X, -1.0, "right stick left")
	await wait(20)
	expect(pl.aim_direction.x < -0.9, "right stick aimed left")
	joy_axis(JOY_AXIS_RIGHT_X, 0.0, "right stick centre")
	joy_axis(JOY_AXIS_RIGHT_Y, -1.0, "right stick up")
	await wait(14)
	joy_axis(JOY_AXIS_TRIGGER_RIGHT, 1.0, "RT")
	await wait(30)
	joy_axis(JOY_AXIS_TRIGGER_RIGHT, 0.0, "RT release")
	joy_axis(JOY_AXIS_RIGHT_Y, 0.0, "right stick centre")
	joy_button(JOY_BUTTON_A, true, "A"); await process_frame; joy_button(JOY_BUTTON_A, false, "A")
	await wait(40)
	joy_button(JOY_BUTTON_START, true, "Start"); await process_frame; joy_button(JOY_BUTTON_START, false, "Start")
	await wait(6)
	expect(paused, "Start paused the game")
	await wait(50)
	joy_button(JOY_BUTTON_START, true, "Start"); await process_frame; joy_button(JOY_BUTTON_START, false, "Start")
	await wait(6)
	expect(not paused, "Start resumed")
	mark("restart")
	await wait(40)
	await key(KEY_R, "R (restart arena)")
	await wait(4)
	expect(in_scene("level_1") and arena().kills == 0, "R reloaded arena 1")
	await wait(60)
	# Stand in the flock with weapons holstered: the real hit/respawn path.
	mark("lose_lives")
	var a := arena()
	var lost := 0
	var n := 0
	while in_scene("level_1") and not a.game_finished and n < 6000:
		if a.respawning:
			release_all()
			await process_frame
			n += 1
			continue
		var c := nearest_chicken(a.player.global_position, 3000.0)
		if c:
			var dx: float = c.global_position.x - a.player.global_position.x
			if dx > 20.0:
				release(KEY_A, "A"); hold(KEY_D, "D")
			elif dx < -20.0:
				release(KEY_D, "D"); hold(KEY_A, "A")
			if c.global_position.y < a.player.global_position.y - 80.0 and a.player.is_on_floor() and absf(dx) < 140.0:
				await key(KEY_SPACE, "Space")
		await process_frame
		n += 1
	release_all()
	expect(a.lives <= 0 if is_instance_valid(a) else true, "all three lives lost")
	mark("defeat_screen")
	await wait_until(func(): return in_scene("defeat"), 240, "defeat screen")
	await wait(120)
	await press_button("Retry Arena")
	await wait_until(func(): return in_scene("level_1"), 90, "retry loads arena 1")
	mark("after_retry")
	await wait(30)
	expect(arena().lives == 3, "retry restores three lives")
	await wait(60)

func take_extras() -> void:
	mark("extras_menu")
	await wait_until(func(): return in_scene("main_menu"), 60, "main menu")
	await wait(30)
	await press_button("How to Play")
	await wait_until(func(): return in_scene("instructions"), 30, "instructions")
	await wait(45)
	await key(KEY_ESCAPE, "Esc (back to menu)")
	await wait(3)
	expect(in_scene("main_menu"), "Esc on How to Play returns to the menu")
	await wait(30)
	await press_button("Play")
	await wait_until(func(): return in_scene("intro"), 30, "briefing")
	await wait(30)
	await key(KEY_ESCAPE, "Esc (skip briefing)")
	await wait_until(func(): return in_scene("level_1"), 90, "arena 1")
	await wait(50)
	var pl = arena().player
	mark("drop_through")
	# walk under the first platform (x 256-576, top y 896), jump twice to land on it
	hold(KEY_D, "D")
	await wait_until(func(): return pl.global_position.x > 300.0, 90, "under platform")
	release(KEY_D, "D")
	await key(KEY_SPACE, "Space")
	await wait(14)
	await key(KEY_SPACE, "Space")
	await wait_until(func(): return pl.is_on_floor(), 90, "landed")
	await wait(20)
	expect(pl.global_position.y < 900.0, "standing on the platform")
	await wait(20)
	hold(KEY_S, "S")
	await wait(4)
	await key(KEY_SPACE, "Space (with S: drop)")
	release(KEY_S, "S")
	await wait_until(func(): return pl.is_on_floor() and pl.global_position.y > 1000.0, 90, "dropped through to the ground")
	await wait(30)
	mark("alt_keys")
	var c := nearest_chicken(pl.global_position, 1400.0)
	await move(screen_of(c.global_position) if c else screen_of(pl.global_position + Vector2(300, -60)), 16)
	hold(KEY_F, "F (fire)")
	for i in range(40):
		c = nearest_chicken(pl.global_position, 1400.0)
		if c:
			_motion(mouse.lerp(screen_of(c.global_position), 0.4))
		await process_frame
	release(KEY_F, "F (fire)")
	await wait(10)
	await key(KEY_G, "G (grenade)")
	await wait(40)
	mark("pad_extras")
	joy_button(JOY_BUTTON_LEFT_SHOULDER, true, "LB"); await process_frame; joy_button(JOY_BUTTON_LEFT_SHOULDER, false, "LB")
	await wait(30)
	joy_button(JOY_BUTTON_RIGHT_SHOULDER, true, "RB")
	await wait(24)
	expect(pl.jetpack_fuel < 1.4, "RB burned jetpack fuel")
	joy_button(JOY_BUTTON_RIGHT_SHOULDER, false, "RB")
	await wait_until(func(): return pl.is_on_floor(), 150, "landed after RB")
	await wait(30)
	mark("restart_button")
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	await press_button("Restart Arena")
	await wait(4)
	expect(in_scene("level_1") and not paused and arena().kills == 0, "Restart Arena reloaded arena 1")
	await wait(50)
	mark("quit")
	await key(KEY_ESCAPE, "Esc")
	await wait(30)
	await press_button("Main Menu")
	await wait_until(func(): return in_scene("main_menu"), 60, "menu")
	await wait(40)
	# Quit ends the process: close the log and the last frame chunk first.
	note("end", {"failed": failed, "note": "clicking Quit next; the process exit code is the result"})
	log_file.flush()
	await move(find_button("Quit").get_global_rect().get_center(), 22)
	await wait(5)
	_close_chunk()
	nosave = true
	FileAccess.open(out_dir + "/frames/DONE", FileAccess.WRITE).store_line(str(frame))
	ring = 1.0
	_button(MOUSE_BUTTON_LEFT, true)
	await process_frame
	_button(MOUSE_BUTTON_LEFT, false)
	await wait(30)
	expect(false, "Quit did not exit")
