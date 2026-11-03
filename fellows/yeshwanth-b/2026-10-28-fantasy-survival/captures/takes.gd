
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
