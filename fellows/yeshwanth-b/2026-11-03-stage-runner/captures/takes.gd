
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
