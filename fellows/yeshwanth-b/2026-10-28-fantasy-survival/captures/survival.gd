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
