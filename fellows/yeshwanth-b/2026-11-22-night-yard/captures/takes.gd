
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
