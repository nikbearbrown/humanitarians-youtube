extends SceneTree
## Film-capture harness for walker-towerdefense. NOT part of the game.
##
## Boots the real main scene named in project.godot and plays it only through
## input events (Input.parse_input_event): keys, mouse motion, mouse buttons.
## It observes game state to decide WHEN to act and to assert outcomes, but it
## never writes game state, never calls session methods, and never teleports.
##
## Every drawn frame of the root viewport (the engine's own render) is saved as
## a PNG, plus a JSONL input log keyed to the same frame numbers.
## A small cursor + click ring is drawn on a harness CanvasLayer because the
## game draws no cursor; it is labelled as harness overlay in CAPTURE.md.
##
## Usage: godot --path . --fixed-fps 30 --script res://capture_driver.gd -- <take> <out_dir>

const TowerTuning = preload("res://features/towers/tower_tuning.gd")

var game: Node
var take := ""
var out_dir := ""
var frame := 0
var log_file: FileAccess
var failed := false
var mouse := Vector2(480, 300)      ## logical coordinates
var ring := 0.0
var overlay: Node2D
var save := true

class CursorOverlay extends Node2D:
	var driver
	func _process(_d: float) -> void:
		queue_redraw()
	func _draw() -> void:
		var p: Vector2 = driver.mouse
		if driver.ring > 0.0:
			var t: float = 1.0 - driver.ring
			draw_arc(p, 6.0 + 16.0 * t, 0.0, TAU, 32, Color(0.85, 0.47, 0.34, 1.0 - t), 2.5)
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
	save = not (args.size() > 2 and args[2] == "nosave")
	DirAccess.make_dir_recursive_absolute(out_dir + "/frames")
	log_file = FileAccess.open(out_dir + "/inputs.jsonl", FileAccess.WRITE)
	if take == "relaunch":
		# Disclosed: the F2 wave-skip debug tool only exists when this project
		# setting is true. Set before the scene's _ready reads it.
		ProjectSettings.set_setting("walker/debug/enabled", true)
	DisplayServer.window_set_size(Vector2i(3840, 2160))
	var packed: PackedScene = load(ProjectSettings.get_setting("application/run/main_scene"))
	game = packed.instantiate()
	root.add_child(game)
	var layer := CanvasLayer.new()
	layer.layer = 128
	root.add_child(layer)
	overlay = CursorOverlay.new()
	overlay.driver = self
	layer.add_child(overlay)
	RenderingServer.frame_post_draw.connect(_save_frame)
	note("boot", {"take": take, "main_scene": ProjectSettings.get_setting("application/run/main_scene"),
		"engine": Engine.get_version_info().string, "user_dir": OS.get_user_data_dir()})
	call_deferred("run")

func _save_frame() -> void:
	if save:
		root.get_texture().get_image().save_png("%s/frames/%05d.png" % [out_dir, frame])
	frame += 1
	ring = maxf(0.0, ring - 1.0 / 12.0)

func snapshot() -> Dictionary:
	return {"state": int(game.state), "gold": int(game.gold), "lives": int(game.lives),
		"wave": int(game.wave_reached), "best": int(game.best_wave),
		"monsters": game.monsters.size(), "towers": game.grid.towers.size(),
		"build": int(game.build_element), "speed": int(game.speed_multiplier()),
		"refusal": int(game.refusal_kind) if game.refusal_timer > 0.0 else 0,
		"overlay": bool(game.debug_overlay)}

func note(event: String, detail: Dictionary = {}) -> void:
	var line := {"frame": frame, "t": snappedf(frame / 30.0, 0.001), "event": event,
		"detail": detail, "game": snapshot() if is_instance_valid(game) and game.grid else {}}
	log_file.store_line(JSON.stringify(line))
	log_file.flush()
	print(JSON.stringify(line))

func expect(ok: bool, label: String) -> void:
	note("assert", {"label": label, "pass": ok})
	if not ok:
		failed = true

func wait(n: int) -> void:
	for i in range(n):
		await process_frame

func wait_until(cond: Callable, max_frames: int, label: String) -> void:
	var n := 0
	while not cond.call() and n < max_frames:
		await process_frame
		n += 1
	expect(cond.call(), "wait_until " + label)

# --- input, only through events ---

func to_window(p: Vector2) -> Vector2:
	return root.get_final_transform() * p

func _motion(p: Vector2) -> void:
	mouse = p
	var ev := InputEventMouseMotion.new()
	ev.position = to_window(p)
	ev.global_position = ev.position
	Input.parse_input_event(ev)

func move(p: Vector2, frames: int = 18) -> void:
	var start := mouse
	for i in range(1, frames + 1):
		var t := float(i) / float(frames)
		t = t * t * (3.0 - 2.0 * t)
		_motion(start.lerp(p, t))
		await process_frame

func click(p: Vector2, button: MouseButton = MOUSE_BUTTON_LEFT, travel: int = 18) -> void:
	await move(p, travel)
	await wait(4)
	note("click", {"button": "right" if button == MOUSE_BUTTON_RIGHT else "left",
		"logical": [snappedf(p.x, 0.1), snappedf(p.y, 0.1)], "cell": [game.grid.cell_of(p).x, game.grid.cell_of(p).y]})
	ring = 1.0
	for pressed in [true, false]:
		var ev := InputEventMouseButton.new()
		ev.button_index = button
		ev.pressed = pressed
		ev.position = to_window(p)
		ev.global_position = ev.position
		Input.parse_input_event(ev)
		await process_frame

func key(code: Key, label: String) -> void:
	note("key", {"key": label})
	for pressed in [true, false]:
		var ev := InputEventKey.new()
		ev.physical_keycode = code
		ev.keycode = code
		ev.pressed = pressed
		Input.parse_input_event(ev)
		await process_frame

func cell(c: Vector2i) -> Vector2:
	return game.grid.world_of(c)

func rect_centre(r: Rect2) -> Vector2:
	return r.position + r.size * 0.5

func wave_over() -> bool:
	return not game.spawner.is_wave_running() and game.monsters.is_empty()

func finish() -> void:
	await wait(3)
	note("end", {"failed": failed})
	log_file.close()
	quit(1 if failed else 0)

# --- takes ---

func run() -> void:
	await wait(2)
	match take:
		"opening": await take_opening()
		"maze": await take_maze()
		"poison": await take_poison()
		"storm": await take_storm()
		"lose": await take_lose()
		"relaunch": await take_relaunch()
		"focus": await take_focus()
		"broken": await take_broken()
		_: expect(false, "unknown take")
	await finish()

## Build `element` at cell `c` through the build bar, between waves.
func build(element: int, c: Vector2i, via_key: bool = false) -> void:
	var before: int = game.grid.towers.size()
	if via_key:
		await key([KEY_1, KEY_2, KEY_3, KEY_4][element], str(element + 1))
	else:
		await click(rect_centre(game.hud.button_rect(element)))
	await wait(10)
	await move(cell(c), 26)
	await wait(14)
	await click(cell(c), MOUSE_BUTTON_LEFT, 4)
	await wait(4)
	expect(game.grid.towers.size() == before + 1, "built element %d at %s" % [element, str(c)])

func play_wave(max_frames: int = 3000) -> void:
	await key(KEY_SPACE, "Space")
	await wait(2)
	var n := 0
	while game.state == 1 and not wave_over() and n < max_frames:
		await process_frame
		n += 1
	note("wave_result", {"wave": game.wave_reached, "frames": n})
	await wait(12)

## Wait out the running wave without input (state may become OVER).
func ride_wave(max_frames: int = 3000) -> void:
	var n := 0
	while game.state in [1, 2] and not wave_over() and n < max_frames:
		await process_frame
		n += 1
	note("wave_result", {"wave": game.wave_reached, "frames": n})

func start_by_enter() -> void:
	await wait(40)
	expect(game.state == 0, "menu on screen")
	await key(KEY_ENTER, "Enter")
	await wait(20)
	expect(game.state == 1 and game.gold == 50 and game.lives == 5, "Enter starts: 50 gold, 5 lives")

## Opening: start, build-bar and key picks, ghost and range, two refusals,
## first waves, the speed toggle, then play on until the run ends naturally.
func take_opening() -> void:
	await wait(50)
	expect(game.state == 0, "starts on menu")
	await click(rect_centre(game.hud.start_rect()), MOUSE_BUTTON_LEFT, 30)
	await wait(24)
	expect(game.state == 1 and game.gold == 50 and game.lives == 5, "START click: 50 gold 5 lives")
	await click(rect_centre(game.hud.button_rect(TowerTuning.Element.FIRE)), MOUSE_BUTTON_LEFT, 30)
	await wait(12)
	expect(game.build_element == TowerTuning.Element.FIRE, "fire picked from bar")
	await move(cell(Vector2i(2, 2)), 30)
	await wait(18)
	await move(cell(Vector2i(5, 3)), 34)
	await wait(22)
	await click(cell(Vector2i(5, 3)), MOUSE_BUTTON_LEFT, 2)
	await wait(2)
	expect(game.refusal_kind == 2, "lava refused: can't build here")
	await wait(28)
	await move(cell(Vector2i(10, 1)), 34)
	await wait(18)
	await click(cell(Vector2i(10, 1)), MOUSE_BUTTON_LEFT, 2)
	await wait(4)
	expect(game.gold == 30 and game.grid.towers.size() == 1, "fire built at (10,1), 30 gold")
	await wait(24)
	await key(KEY_2, "2")
	await wait(10)
	await move(cell(Vector2i(6, 1)), 30)
	await wait(18)
	await click(cell(Vector2i(6, 1)), MOUSE_BUTTON_RIGHT, 2)
	await wait(4)
	expect(game.build_element == -1, "right click cancels build")
	await wait(20)
	await key(KEY_2, "2")
	await wait(12)
	await click(cell(Vector2i(6, 1)), MOUSE_BUTTON_LEFT, 6)
	await wait(4)
	expect(game.gold == 5 and game.grid.towers.size() == 2, "ice built at (6,1), 5 gold")
	await wait(20)
	await key(KEY_4, "4")
	await wait(10)
	await move(cell(Vector2i(4, 1)), 26)
	await wait(12)
	await click(cell(Vector2i(4, 1)), MOUSE_BUTTON_LEFT, 2)
	await wait(2)
	expect(game.refusal_kind == 1, "storm refused: not enough gold")
	await wait(28)
	await key(KEY_ESCAPE, "Esc")
	await wait(6)
	expect(game.build_element == -1 and game.state == 1, "Esc cancels build, does not pause")
	await move(Vector2(700, 520), 24)
	await wait(16)
	await play_wave()                                 # wave 1 at 1x
	await key(KEY_SPACE, "Space")                     # wave 2
	await wait(30)
	await click(rect_centre(game.hud.speed_rect()), MOUSE_BUTTON_LEFT, 24)
	await wait(6)
	expect(game.speed_multiplier() == 2, "SPEED button -> 2x")
	await wait(40)
	await key(KEY_F, "F")
	await wait(4)
	expect(game.speed_multiplier() == 3, "F -> 3x")
	await ride_wave()
	await key(KEY_F, "F")
	await wait(4)
	expect(game.speed_multiplier() == 1, "F -> back to 1x")
	await wait(16)
	while game.state == 1 and game.wave_reached < 8:
		await play_wave()
	expect(game.state == 3, "run ended: the exit was overrun")
	note("game_over", {"wave_reached": game.wave_reached, "best": game.best_wave})
	await wait(100)
	await key(KEY_ENTER, "Enter")
	await wait(30)
	expect(game.state == 1 and game.lives == 5 and game.gold == 50 and game.wave_reached == 0, "Enter: play again, fresh run")
	await wait(20)
	# Second run, different opening: one Fire tower, upgraded at once.
	await build(TowerTuning.Element.FIRE, Vector2i(10, 1))
	await wait(16)
	await click(cell(Vector2i(10, 1)), MOUSE_BUTTON_LEFT, 30)
	await wait(18)
	expect(game.selected_tower != null and game.gold == 30, "fire selected: SELL 10, UPGRADE 30")
	await click(rect_centre(game.hud.upgrade_rect()), MOUSE_BUTTON_LEFT, 30)
	await wait(8)
	expect(game.grid.towers[Vector2i(10, 1)].upgraded and game.gold == 0, "upgraded: chevron, MAXED, 0 gold")
	await wait(40)
	await click(Vector2(480, 500), MOUSE_BUTTON_RIGHT, 24)
	await wait(10)
	await play_wave()

## Maze rules: monster in the way, would block the path, a reroute, a sale.
func take_maze() -> void:
	await start_by_enter()
	await key(KEY_SPACE, "Space")
	await wait(4)
	await key(KEY_1, "1")
	var target := Vector2i(-1, -1)
	var guard := 0
	while guard < 400 and target.x < 0:
		for m in game.monsters:
			if not m.finished and m.progress < 0.3 and m.cell.y == 0 and m.cell.x >= 2 and m.cell.x <= 6 \
					and game.grid.is_buildable_ground(m.cell):
				target = m.cell
		if target.x < 0:
			await move(Vector2(mouse.x + 0.0, mouse.y), 1)
		guard += 1
	note("monster_tile", {"cell": [target.x, target.y]})
	await click(cell(target), MOUSE_BUTTON_LEFT, 3)
	await wait(2)
	expect(game.refusal_kind == 3, "monster in the way")
	await wait(30)
	await key(KEY_ESCAPE, "Esc")
	await ride_wave()
	await wait(20)
	await build(TowerTuning.Element.FIRE, Vector2i(0, 1), true)
	await wait(16)
	await key(KEY_1, "1")
	await wait(10)
	await move(cell(Vector2i(1, 0)), 26)
	await wait(18)
	await click(cell(Vector2i(1, 0)), MOUSE_BUTTON_LEFT, 2)
	await wait(2)
	expect(game.refusal_kind == 4, "sealing the spawn refused: would block the path")
	await wait(34)
	await key(KEY_ESCAPE, "Esc")
	await wait(14)
	var before: Array = game.grid.preview_path.duplicate()
	await key(KEY_1, "1")
	await wait(10)
	await move(cell(Vector2i(5, 0)), 30)
	await wait(18)
	await click(cell(Vector2i(5, 0)), MOUSE_BUTTON_LEFT, 2)
	await wait(6)
	note("route", {"before": before.size(), "after": game.grid.preview_path.size(),
		"changed": before != game.grid.preview_path})
	expect(game.grid.towers.has(Vector2i(5, 0)) and before != game.grid.preview_path, "tower on the road: route changed")
	await wait(40)
	await key(KEY_SPACE, "Space")
	await wait(150)                                    # monsters walk the new route
	await click(cell(Vector2i(0, 1)), MOUSE_BUTTON_LEFT, 30)
	await wait(16)
	expect(game.selected_tower != null, "tower selected: panel shows SELL")
	var g: int = game.gold
	await click(rect_centre(game.hud.sell_rect()), MOUSE_BUTTON_LEFT, 30)
	await wait(6)
	expect(game.gold == g + 10 and not game.grid.towers.has(Vector2i(0, 1)), "sold for 10 gold")
	await ride_wave()
	await wait(30)

## Poison and Fire, F1 overlay, pause and resume, then an upgrade when affordable.
func take_poison() -> void:
	await start_by_enter()
	await build(TowerTuning.Element.POISON, Vector2i(6, 1), true)
	await build(TowerTuning.Element.FIRE, Vector2i(10, 1), true)
	await key(KEY_F1, "F1")
	await wait(8)
	expect(game.debug_overlay, "F1 overlay on")
	await key(KEY_SPACE, "Space")
	await wait(120)
	await key(KEY_ESCAPE, "Esc")
	await wait(4)
	expect(game.state == 2, "Esc pauses mid-wave")
	await wait(50)
	await key(KEY_ENTER, "Enter")
	await wait(4)
	expect(game.state == 1, "Enter resumes")
	await ride_wave()
	await wait(12)
	while game.state == 1 and game.wave_reached < 3:
		await play_wave()
	await wait(20)

## Storm alone, waves until a chain of more than one hop is seen, Ice when affordable.
func take_storm() -> void:
	await start_by_enter()
	await build(TowerTuning.Element.STORM, Vector2i(6, 1), true)
	var chained := false
	var bought_ice := false
	while game.state == 1 and game.wave_reached < 6 and not chained:
		if not bought_ice and game.gold >= 25:
			await build(TowerTuning.Element.ICE, Vector2i(9, 1), true)
			bought_ice = true
		await key(KEY_SPACE, "Space")
		await wait(2)
		var n := 0
		while game.state == 1 and not wave_over() and n < 3000:
			for pr in game.projectiles:
				if pr.element == TowerTuning.Element.STORM and pr.beam_points.size() > 2 and not chained:
					chained = true
					note("chain_seen", {"points": pr.beam_points.size()})
			await process_frame
			n += 1
		note("wave_result", {"wave": game.wave_reached, "chained": chained})
	expect(chained, "storm chain of 2+ hops observed")
	await wait(30)

func take_lose() -> void:
	await wait(40)
	expect(game.state == 0, "menu")
	await key(KEY_ENTER, "Enter")
	await wait(20)
	expect(game.state == 1, "Enter starts")
	while game.state == 1:
		await key(KEY_SPACE, "Space")
		await wait(2)
		var n := 0
		while game.state == 1 and not wave_over() and n < 3000:
			await process_frame
			n += 1
		await wait(20)
	expect(game.state == 3 and game.lives == 0, "game over at 0 lives")
	note("game_over", {"wave_reached": game.wave_reached, "best": game.best_wave})
	await wait(90)
	await key(KEY_ENTER, "Enter")
	await wait(20)
	expect(game.state == 1 and game.lives == 5 and game.wave_reached == 0, "Enter plays again")
	await key(KEY_SPACE, "Space")
	await wait(50)
	await key(KEY_R, "R")
	await wait(4)
	expect(game.state == 1 and game.wave_reached == 0 and game.monsters.is_empty() and game.gold == 50, "R restarts")
	await wait(40)

func take_relaunch() -> void:
	await wait(60)
	note("menu_best", {"best": game.best_wave})
	expect(game.state == 0 and game.best_wave > 0, "best wave survived relaunch")
	await key(KEY_ENTER, "Enter")
	await wait(20)
	await build(TowerTuning.Element.FIRE, Vector2i(10, 1), true)
	await key(KEY_F1, "F1")
	await wait(10)
	await key(KEY_SPACE, "Space")
	await wait(45)
	var w: int = game.wave_reached
	await key(KEY_F2, "F2")
	await wait(4)
	expect(game.wave_reached == w + 1, "F2 skipped to the next wave")
	await wait(60)
	await key(KEY_F2, "F2")
	await wait(4)
	expect(game.wave_reached == w + 2, "F2 skipped again")
	await wait(70)


## Pause on focus loss, through a real OS focus change: the driver asks macOS
## to bring Finder forward (`open -a Finder`); the game window loses focus.
func take_focus() -> void:
	DisplayServer.window_set_flag(DisplayServer.WINDOW_FLAG_NO_FOCUS, false)
	DisplayServer.window_move_to_foreground()
	await start_by_enter()
	await build(TowerTuning.Element.FIRE, Vector2i(10, 1), true)
	await key(KEY_SPACE, "Space")
	await wait(60)
	expect(game.state == 1, "playing before focus change")
	note("os_focus_change", {"command": "open -a Finder"})
	OS.create_process("open", ["-a", "Finder"])
	var n := 0
	while game.state != 2 and n < 150:
		await process_frame
		n += 1
	expect(game.state == 2, "window lost focus -> paused")
	note("paused_after_frames", {"frames": n})
	# macOS stops drawing an occluded window; bring the game back to the front.
	# Regaining focus must NOT unpause -- only Enter or Esc does.
	note("os_focus_back", {"call": "DisplayServer.window_move_to_foreground"})
	DisplayServer.window_move_to_foreground()
	await wait(75)
	expect(game.state == 2, "still paused after focus returns")
	await key(KEY_ENTER, "Enter")
	await wait(4)
	expect(game.state == 1, "Enter resumes")
	await wait(60)

## Staged failure surface: this take runs on a second isolated copy whose
## levels/level_01.json was deliberately broken (no "exit" key).
func take_broken() -> void:
	await wait(120)
	expect(game.grid.load_error != "", "level load error shown")
	note("load_error", {"text": game.grid.load_error, "state": int(game.state)})
	await key(KEY_ENTER, "Enter")
	await wait(90)
	note("after_enter", {"state": int(game.state)})
	await key(KEY_SPACE, "Space")
	await wait(170)
	note("after_space", {"state": int(game.state), "wave": int(game.wave_reached)})
