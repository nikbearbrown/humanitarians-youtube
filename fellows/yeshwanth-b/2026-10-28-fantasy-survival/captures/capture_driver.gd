extends SceneTree
## Film-capture harness for Fantasy Survival Crafting. NOT part of the game.
##
## Boots run/main_scene and plays only through Input.parse_input_event: keyboard keys,
## relative mouse motion (look), mouse buttons and joypad events. It reads game state to
## decide WHEN and WHERE to press, and asserts outcomes. It never writes game state, never
## calls game methods and never teleports. The game's own _tools playtests are separate.
##
## Every rendered frame of the root viewport is appended to 150-frame raw chunks that
## run_take.sh encodes. When the game frees the cursor (menus, inventory) a white arrow is
## drawn on a harness CanvasLayer (layer 128): the OS cursor is not in the viewport texture.
##
## Usage: harness/run_take.sh <take> <out_dir>

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

func world() -> Node:
	var s := current_scene
	return s if s and "player" in s and "inventory" in s else null

func snapshot() -> Dictionary:
	var s := current_scene
	var d := {"scene": s.scene_file_path.get_file().get_basename() if s else ""}
	var w := world()
	if w and is_instance_valid(w.player) and w.stats:
		var counts := {}
		for item in w.inventory.slots:
			if item != "":
				counts[item] = counts.get(item, 0) + 1
		d.merge({"day": w.day, "hour": snappedf(w.hour, 0.01), "health": int(w.stats.current_health),
			"calories": int(w.stats.current_calories), "water": int(w.stats.current_hydration),
			"inv": counts, "equipped": w.player.equipped, "resting": w.resting, "paused": paused,
			"pos": [snappedf(w.player.global_position.x, 0.1), snappedf(w.player.global_position.z, 0.1)]})
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

# --- look and walk, only through input events ---

## Relative mouse motion in viewport units, scaled to window pixels the way a real mouse would be.
func look_rel(rel_vp: Vector2) -> void:
	var ev := InputEventMouseMotion.new()
	ev.relative = rel_vp * root.get_final_transform().get_scale()
	ev.position = to_window(Vector2(640, 360))
	ev.global_position = ev.position
	Input.parse_input_event(ev)

const LOOK_SCALE := 0.0022
const TURN_STEP := 0.085            ## radians per frame at most, so turns read as a person's

func aim(yaw_target: float, pitch_target: float, step := TURN_STEP) -> float:
	var pl = world().player
	var sens: float = gs().mouse_sensitivity
	var ey := wrapf(yaw_target - pl.rotation.y, -PI, PI)
	var ep: float = pitch_target - pl.x_rotation
	var sy := clampf(ey, -step, step)
	var sp := clampf(ep, -step * 0.7, step * 0.7)
	if absf(sy) > 0.0005 or absf(sp) > 0.0005:
		look_rel(Vector2(-sy, -sp) / (LOOK_SCALE * sens))
	return absf(ey) + absf(ep)

func yaw_to(p: Vector3) -> float:
	var d: Vector3 = p - world().player.global_position
	return atan2(-d.x, -d.z)

func pitch_to(p: Vector3) -> float:
	var pl = world().player
	var eye: Vector3 = pl.global_position + Vector3(0, 1.62, 0)
	var flat := Vector2(p.x - eye.x, p.z - eye.z).length()
	return atan2(p.y - eye.y, maxf(flat, 0.01))

func flat_dist(p: Vector3) -> float:
	var q: Vector3 = world().player.global_position
	return Vector2(p.x - q.x, p.z - q.z).length()

func stop_walking() -> void:
	for code in [KEY_W, KEY_A, KEY_S, KEY_D, KEY_SHIFT]:
		release(code, OS.get_keycode_string(code))

## Walk (and sprint when far) to within `stop` metres of `p`. Unsticks by side-stepping and jumping.
func walk_to(p: Vector3, stop := 1.8, max_frames := 2400, label := "") -> bool:
	var w := world()
	var n := 0
	var last_pos: Vector3 = w.player.global_position
	var stuck_checks := 0
	note("walk", {"to": [snappedf(p.x, 0.1), snappedf(p.z, 0.1)], "why": label})
	while n < max_frames and world() == w and w.stats.alive and not w.finished:
		var d := flat_dist(p)
		if d < stop:
			stop_walking()
			return true
		var err := aim(yaw_to(p), -0.12)
		if absf(wrapf(yaw_to(p) - w.player.rotation.y, -PI, PI)) < 0.55:
			hold(KEY_W, "W")
		else:
			release(KEY_W, "W")
		if d > 7.0:
			hold(KEY_SHIFT, "Shift")
		else:
			release(KEY_SHIFT, "Shift")
		await process_frame
		n += 1
		if n % 45 == 0:
			if w.player.global_position.distance_to(last_pos) < 0.7 and held.has(KEY_W):
				stuck_checks += 1
				note("unstick", {"n": stuck_checks})
				hold(KEY_D if stuck_checks % 2 == 1 else KEY_A, "D" if stuck_checks % 2 == 1 else "A")
				await key(KEY_SPACE, "Space")
				await wait(24)
				release(KEY_D, "D")
				release(KEY_A, "A")
			last_pos = w.player.global_position
	stop_walking()
	expect(false, "reached " + label)
	return false

## Aim the centre ray at `node` (at `point`) and press `action` when the game reports it as the target.
func use_target(node: Node, point: Vector3, action := "E", max_frames := 150) -> bool:
	var w := world()
	var n := 0
	while n < max_frames and is_instance_valid(node) and world() == w:
		aim(yaw_to(point), pitch_to(point))
		await process_frame
		n += 1
		if w.player.target == node:
			if action == "E":
				await key(KEY_E, "E")
			else:
				_button(MOUSE_BUTTON_LEFT, true)
				await process_frame
				_button(MOUSE_BUTTON_LEFT, false)
				note("click", {"button": "left", "on": node.name if node else ""})
			return true
	return false

func pickups_of(item: String) -> Array:
	var out := []
	var w := world()
	for id in w.entities:
		var e = w.entities[id]
		if is_instance_valid(e) and "item_name" in e and e.item_name == item and not blacklist.has(id):
			out.append(e)
	return out

var blacklist := {}

func nearest(nodes: Array, from: Vector3) -> Node:
	var best: Node = null
	var bd := INF
	for e in nodes:
		var d: float = Vector2(e.global_position.x - from.x, e.global_position.z - from.z).length()
		if d < bd:
			bd = d
			best = e
	return best

## Collect `count` more of `item` from the nearest world pickups.
func collect(item: String, count: int, near := Vector3.INF) -> int:
	var w := world()
	var got := 0
	var tries := 0
	while got < count and tries < count + 6 and world() == w:
		tries += 1
		var from: Vector3 = near if near != Vector3.INF and got == 0 else w.player.global_position
		var node := nearest(pickups_of(item), from)
		if node == null:
			break
		var before: int = w.inventory.count(item)
		var id: String = node.entity_id
		if not await walk_to(node.global_position, 1.6, 2400, item):
			blacklist[id] = true
			continue
		var ok := await use_target(node, shape_center(node), "E", 120)
		await wait(6)
		if ok and w.inventory.count(item) > before:
			got += 1
			note("picked", {"item": item, "now": w.inventory.count(item)})
		else:
			blacklist[id] = true
	expect(got >= count, "collected %d %s" % [count, item])
	return got

# --- UI (cursor visible) ---

func slot_of(item: String) -> int:
	return world().inventory.slots.find(item)

func slot_center(i: int) -> Vector2:
	return world().inventory.slot_nodes[i].get_global_rect().get_center()

func open_inventory(on := true) -> void:
	if world().inventory_open != on:
		await key(KEY_I, "I")
		await wait(8)

func open_crafting(on := true) -> void:
	if world().crafting_open != on:
		await key(KEY_C, "C")
		await wait(10)

func craft_button(item: String) -> Button:
	for row in world().crafting.recipe_list.get_children():
		if row.is_queued_for_deletion():
			continue
		var labels: Array = row.find_children("*", "Label", true, false)
		var buttons: Array = row.find_children("*", "Button", true, false)
		for l in labels:
			if l.text == item and buttons.size() > 0 and buttons[0].visible:
				return buttons[0]
	return null

func craft(item: String, category: String) -> bool:
	var w := world()
	var before: int = w.inventory.count(item)
	await open_crafting(true)
	var tab := find_button(category)
	if tab:
		await click(tab.get_global_rect().get_center(), category, 18)
		await wait(20)
	for attempt in range(4):
		var b := craft_button(item)
		if b == null:
			await wait(16)
			continue
		await move(b.get_global_rect().get_center(), 18)
		await wait(4)
		b = craft_button(item)
		if b == null:
			continue
		note("click", {"button": "left", "on": "Craft " + item})
		ring = 1.0
		_motion(b.get_global_rect().get_center())
		_button(MOUSE_BUTTON_LEFT, true)
		await process_frame
		_button(MOUSE_BUTTON_LEFT, false)
		await wait(10)
		if w.inventory.count(item) > before:
			break
	var ok: bool = w.inventory.count(item) > before
	expect(ok, "crafted " + item)
	await wait(40)
	await open_crafting(false)
	return ok

func use_slot(item: String) -> bool:
	var i := slot_of(item)
	if i < 0:
		expect(false, "have %s to use" % item)
		return false
	await move(slot_center(i), 20)
	await wait(20)
	ring = 1.0
	await right_click("use " + item)
	await wait(12)
	return true

func drag_slot(from_i: int, to_i: int) -> void:
	await move(slot_center(from_i), 18)
	await wait(6)
	note("drag", {"from": from_i, "to": to_i})
	_button(MOUSE_BUTTON_LEFT, true)
	var start := mouse
	var end := slot_center(to_i)
	for k in range(1, 25):
		var ev := InputEventMouseMotion.new()
		var p := start.lerp(end, float(k) / 24.0)
		ev.relative = to_window(p) - to_window(mouse)
		mouse = p
		ev.position = to_window(p)
		ev.global_position = ev.position
		ev.button_mask = MOUSE_BUTTON_MASK_LEFT
		Input.parse_input_event(ev)
		await process_frame
	await wait(4)
	_button(MOUSE_BUTTON_LEFT, false)
	await wait(10)

# --- world actions ---

func chop_tree(tree: Node) -> bool:
	var w := world()
	if not await walk_to(tree.global_position, 1.9, 2400, "pine"):
		return false
	var trunk: Vector3 = tree.global_position + Vector3(0, 1.3, 0)
	var swings := 0
	while is_instance_valid(tree) and not tree.falling and swings < 10:
		if await use_target(tree, trunk, "click", 90):
			swings += 1
			await wait(20)
		else:
			await walk_to(tree.global_position, 1.3, 120, "closer to pine")
	expect(not is_instance_valid(tree) or tree.falling, "felled a pine in %d swings" % swings)
	await wait(75)
	return true

func choppable_trees() -> Array:
	var out := []
	for id in world().entities:
		var e = world().entities[id]
		if is_instance_valid(e) and "hits_left" in e and not e.falling:
			out.append(e)
	return out

func live_rabbits() -> Array:
	var out := []
	for id in world().entities:
		var e = world().entities[id]
		if is_instance_valid(e) and "fleeing" in e and not e.dead:
			out.append(e)
	return out

func hunt_rabbit(max_frames := 2400) -> bool:
	var w := world()
	var r := nearest(live_rabbits(), w.player.global_position)
	if r == null:
		return false
	note("hunt", {"rabbit": r.entity_id})
	var n := 0
	while n < max_frames and is_instance_valid(r) and not r.dead and world() == w:
		var p: Vector3 = r.global_position
		var d := flat_dist(p)
		aim(yaw_to(p), pitch_to(p + Vector3(0, 0.25, 0)) if d < 6.0 else -0.1, 0.14)
		hold(KEY_W, "W")
		if d > 3.0:
			hold(KEY_SHIFT, "Shift")
		else:
			release(KEY_SHIFT, "Shift")
		await process_frame
		n += 1
		if w.player.target == r and w.player.swing_cooldown <= 0.0:
			note("click", {"button": "left", "on": "rabbit"})
			_button(MOUSE_BUTTON_LEFT, true)
			await process_frame
			_button(MOUSE_BUTTON_LEFT, false)
	stop_walking()
	var ok: bool = is_instance_valid(r) and r.dead
	expect(ok, "hunted a rabbit")
	await wait(60)
	return ok

func lake_edge_point() -> Vector3:
	## A point on the line to the lake centre where the ground is 0.4 m under the water surface.
	var w := world()
	var c: Vector2 = w.terrain.LAKE_CENTER
	var p: Vector3 = w.player.global_position
	var a := Vector2(p.x, p.z)
	for k in range(200):
		var q := a.lerp(c, k / 200.0)
		if w.terrain.height_at(q.x, q.y) < -0.4:
			return Vector3(q.x, 0.0, q.y)
	return Vector3(c.x, 0.0, c.y)

func drink(times := 2) -> bool:
	var w := world()
	var edge := lake_edge_point()
	await walk_to(edge, 1.0, 2400, "lake edge")
	var ok := false
	for i in range(times):
		var before: float = w.stats.current_hydration
		for n in range(90):
			aim(w.player.rotation.y, -0.75)
			await process_frame
			if w.player.target and w.hud.interaction_label.text.begins_with("Lake"):
				await key(KEY_E, "E (drink)")
				break
		await wait(36)
		ok = w.stats.current_hydration > before or w.stats.current_hydration >= 99.5
		expect(ok, "drank from the lake (water %d)" % int(w.stats.current_hydration))
	return ok

func pick_apple() -> bool:
	var w := world()
	var tree: Node = null
	var bd := INF
	for id in w.entities:
		var e = w.entities[id]
		if is_instance_valid(e) and "apples" in e and e.apples > 0:
			var d := flat_dist(e.global_position)
			if d < bd:
				bd = d
				tree = e
	if tree == null:
		return false
	await walk_to(tree.global_position, 2.2, 2400, "apple tree")
	var before: int = w.inventory.count("Apple")
	await use_target(tree, tree.global_position + Vector3(0, 1.6, 0), "E", 120)
	await wait(20)
	var ok: bool = w.inventory.count("Apple") > before
	expect(ok, "picked an apple from a tree")
	return ok

func menu_page_button(text: String) -> Button:
	return find_button(text)

func shape_center(node: Node) -> Vector3:
	for c in node.get_children():
		if c is CollisionShape3D:
			return c.global_position
	return node.global_position + Vector3(0, 0.2, 0)

func gs() -> Node:
	return root.get_node("GameState")


# --- takes ---

func run() -> void:
	await wait(3)
	match take:
		"day": await take_day()
		"night": await take_night()
		"defeat": await take_defeat()
		"probe": await take_probe()
		_: expect(false, "unknown take")
	await finish()

func in_scene(name: String) -> bool:
	return current_scene != null and current_scene.scene_file_path.ends_with(name + ".tscn")

func wait_game(cond: Callable, max_frames: int, label: String) -> bool:
	return await wait_until(cond, max_frames, label)

func take_probe() -> void:
	## Quick check that captured-mouse look and WASD reach the game.
	await wait_until(func(): return in_scene("main_menu"), 60, "main menu")
	await press_button("New Game")
	await wait_until(func(): return in_scene("intro"), 60, "intro")
	await key(KEY_ESCAPE, "Esc (skip intro)")
	await wait_until(func(): return world() != null, 200, "game loaded")
	await wait(40)
	var pl = world().player
	note("mouse_mode", {"mode": Input.mouse_mode})
	var y0: float = pl.rotation.y
	for i in range(20):
		aim(y0 + 1.0, 0.0)
		await process_frame
	expect(absf(wrapf(pl.rotation.y - y0, -PI, PI)) > 0.5, "mouse look turned the player")
	var p0: Vector3 = pl.global_position
	hold(KEY_W, "W")
	await wait(30)
	release(KEY_W, "W")
	expect(pl.global_position.distance_to(p0) > 1.5, "W walked forward")

func take_day() -> void:
	mark("main_menu")
	await wait_until(func(): return in_scene("main_menu"), 60, "main menu")
	await wait(50)
	expect(find_button("Load Game") == null, "fresh save folder: no Load Game")
	await move(find_button("New Game").get_global_rect().get_center(), 26)
	await wait(16)
	mark("how_to_play")
	await press_button("How to Play")
	await wait_until(func(): return in_scene("instructions"), 30, "how to play")
	await wait(140)
	await press_button("Back")
	await wait_until(func(): return in_scene("main_menu"), 30, "back at menu")
	await wait(24)
	mark("intro")
	await press_button("New Game")
	await wait_until(func(): return in_scene("intro"), 60, "intro")
	for i in range(3):
		await wait(75)
		await press_button("Continue")
	await wait_until(func(): return world() != null, 240, "game loaded")
	var w := world()
	mark("arrival")
	await wait(70)
	expect(Input.mouse_mode == Input.MOUSE_MODE_CAPTURED, "mouse captured in game")
	stats["start"] = snapshot()
	# Look around the village, then the empty inventory and the crafting screen.
	var y0: float = w.player.rotation.y
	for i in range(50):
		aim(y0 + 1.2, -0.05, 0.05)
		await process_frame
	for i in range(50):
		aim(y0, -0.05, 0.05)
		await process_frame
	await open_inventory(true)
	await wait(50)
	await open_inventory(false)
	await open_crafting(true)
	await wait(60)
	await open_crafting(false)
	await key(KEY_1, "1 (equip, no axe yet)")
	await wait(60)

	mark("orchard")
	await pick_apple()
	await wait(20)

	mark("sticks")
	await collect("Stick", 3, Vector3(-72, 0, -24))
	await collect("Mushroom", 1)
	mark("gold")
	await collect("Gold", 3, Vector3(-62, 0, -40))
	mark("stones")
	await collect("Stone", 3, Vector3(-62, 0, -40))

	mark("craft_axe")
	await craft("Axe", "Tools")
	await key(KEY_1, "1 (equip axe)")
	await wait(30)
	expect(w.player.has_axe_equipped(), "axe equipped")

	mark("chop")
	var felled := 0
	for attempt in range(4):
		if felled >= 2:
			break
		var t := nearest(choppable_trees(), Vector3(-72, 0, -24) if felled == 0 else w.player.global_position)
		if t and await chop_tree(t):
			felled += 1
			await collect("Log", 2)
	expect(w.inventory.count("Log") >= 4, "4 logs gathered")

	mark("craft_campfire")
	await craft("Campfire", "Survival")
	stats["after_campfire_craft"] = snapshot()

	mark("hunt")
	await hunt_rabbit(2400)
	if pickups_of("Rabbit Meat").size() > 0:
		await collect("Rabbit Meat", 1)

	mark("lake")
	await drink(1)
	# Facing the water from the edge: the game refuses a fire whose spot is in the lake.
	mark("water_refusal")
	await open_inventory(true)
	await use_slot("Campfire")
	await wait(30)
	expect(not w.campfire_placed and w.inventory.count("Campfire") == 1, "fire in the water refused")
	await open_inventory(false)
	await wait(50)
	# Walk inland, turn back toward the lake, and place it on dry ground.
	var edge := lake_edge_point()
	var inland: Vector3 = w.player.global_position + (w.player.global_position - edge).normalized() * 9.0
	await walk_to(inland, 1.0, 600, "dry shore")
	var lake := Vector3(w.terrain.LAKE_CENTER.x, 0, w.terrain.LAKE_CENTER.y)
	for i in range(45):
		aim(yaw_to(lake), -0.2)
		await process_frame
	mark("place_campfire")
	await open_inventory(true)
	await use_slot("Campfire")
	await wait(40)
	expect(w.campfire_placed, "campfire placed")
	await open_inventory(false)
	var fire: Node = w.campfires[0] if w.campfires.size() > 0 else null

	mark("cook_eat")
	if w.inventory.count("Rabbit Meat") > 0:
		await craft("Cooked Meat", "Survival")
	await open_inventory(true)
	var hover := slot_of("Mushroom")
	if hover >= 0:
		await move(slot_center(hover), 22)
		await wait(60)
	var free: int = w.inventory.slots.find("")
	var first_item := 0
	for i in range(w.inventory.slots.size()):
		if w.inventory.slots[i] != "":
			first_item = i
			break
	if free >= 0:
		await drag_slot(first_item, 20)
		expect(w.inventory.slots[20] != "", "dragged an item to the last slot")
	for food in ["Cooked Meat", "Apple", "Mushroom"]:
		if w.inventory.count(food) > 0:
			var c0: float = w.stats.current_calories
			await use_slot(food)
			await wait(20)
			expect(w.stats.current_calories > c0 or w.stats.current_calories >= 99.0, "ate " + food)
	await open_inventory(false)

	mark("menu")
	await key(KEY_M, "M")
	await wait(30)
	expect(paused and w.menu_open, "menu paused the game")
	await press_button("Settings")
	await wait(60)
	await press_button("Back")
	await wait(20)
	await press_button("Save Game")
	await wait(30)
	await press_button("Save")
	await wait(50)
	expect(gs().has_save(), "day save written")
	await press_button("Back")
	await wait(20)
	await press_button("Resume")
	await wait(20)
	expect(not paused, "resumed")

	stats["end_of_day_take"] = snapshot()
	await wait(30)

func take_night() -> void:
	mark("load")
	await wait_until(func(): return in_scene("main_menu"), 60, "main menu")
	await wait(30)
	await press_button("Load Game")
	await wait_until(func(): return world() != null, 240, "day save loaded")
	var w := world()
	await wait(60)
	expect(w.campfire_placed and not w.is_night(), "loaded the afternoon save with the fire placed")
	var fire: Node = w.campfires[0] if w.campfires.size() > 0 else null
	mark("wait_for_dusk")
	if fire:
		await walk_to(fire.global_position, 3.0, 600, "fire")
	stats["before_dusk"] = snapshot()
	var n := 0
	while not w.is_night() and n < 12000:
		# Stand by the fire and look around now and then, as a waiting player would.
		if fire and flat_dist(fire.global_position) > 6.0:
			await walk_to(fire.global_position, 3.0, 300, "fire")
		if n % 600 < 120:
			aim(w.player.rotation.y + 0.02, -0.08, 0.02)
		await process_frame
		n += 1
	expect(w.is_night(), "night fell")
	mark("night")
	await wait(120)
	expect(not w.stats.freezing, "warm beside the fire at night")
	# A night save for the defeat take, then rest until dawn.
	await key(KEY_M, "M")
	await wait(20)
	await press_button("Save Game")
	await wait(20)
	await press_button("Save")
	await wait(30)
	await press_button("Back")
	await wait(12)
	await press_button("Resume")
	await wait(20)
	stats["night_save"] = snapshot()
	mark("rest")
	if fire:
		await walk_to(fire.global_position, 2.2, 300, "fire")
		await use_target(fire, fire.global_position + Vector3(0, 0.3, 0), "E", 150)
		await wait(10)
		expect(w.resting, "resting by the fire")
	await wait_until(func(): return in_scene("victory"), 1800, "dawn: victory screen")
	mark("victory")
	await wait(150)
	await press_button("Main Menu")
	await wait_until(func(): return in_scene("main_menu"), 60, "main menu after victory")
	await wait(30)
	expect(find_button("Load Game") != null, "menu now offers Load Game")
	await wait(40)

func take_defeat() -> void:
	mark("load")
	await wait_until(func(): return in_scene("main_menu"), 60, "main menu")
	await wait(30)
	await press_button("Load Game")
	await wait_until(func(): return world() != null, 240, "save loaded")
	var w := world()
	await wait(70)
	expect(w.is_night() and w.campfire_placed, "loaded the night save beside the fire")
	mark("gamepad")
	var pl = w.player
	var y0: float = pl.rotation.y
	joy_axis(JOY_AXIS_RIGHT_X, 1.0, "right stick right")
	await wait(30)
	joy_axis(JOY_AXIS_RIGHT_X, 0.0, "right stick centre")
	expect(absf(wrapf(pl.rotation.y - y0, -PI, PI)) > 0.5, "right stick turned the view")
	joy_button(JOY_BUTTON_Y, true, "Y"); await process_frame; joy_button(JOY_BUTTON_Y, false, "Y")
	await wait(40)
	expect(w.inventory_open, "pad Y opened the inventory")
	joy_button(JOY_BUTTON_Y, true, "Y"); await process_frame; joy_button(JOY_BUTTON_Y, false, "Y")
	await wait(20)
	mark("walk_away")
	var fire: Node = w.campfires[0]
	var away: Vector3 = pl.global_position + (pl.global_position - fire.global_position).normalized() * 30.0
	await walk_to(away, 2.0, 900, "away from the fire")
	await wait_until(func(): return w.stats.freezing, 120, "freezing away from the fire")
	await wait(90)
	mark("debug_damage")
	for i in range(8):
		await key(KEY_N, "N (debug damage)")
		await wait(12)
	await wait_until(func(): return in_scene("defeat"), 2400, "defeat screen")
	mark("defeat_screen")
	await wait(150)
	expect(find_button("Load Save") != null, "defeat screen offers Load Save")
	await press_button("Load Save")
	await wait_until(func(): return world() != null, 240, "save reloaded from defeat")
	mark("reloaded")
	await wait(90)
	expect(world().stats.alive and world().is_night(), "back at the fire, alive")
	await key(KEY_M, "M")
	await wait(30)
	await press_button("Main Menu")
	await wait_until(func(): return in_scene("main_menu"), 60, "main menu")
	await wait(40)
