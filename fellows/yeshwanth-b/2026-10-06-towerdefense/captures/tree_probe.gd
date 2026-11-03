extends SceneTree
## Runtime tree probe (harness, not game). Boots main.tscn, starts a run by
## Enter, builds one Fire tower by key + click, sends a wave, then prints the
## live node tree. Input only, like capture_driver.gd.
var game
func _initialize() -> void:
	game = (load(ProjectSettings.get_setting("application/run/main_scene")) as PackedScene).instantiate()
	root.add_child(game)
	call_deferred("run")
func ev_key(k):
	for p in [true, false]:
		var e := InputEventKey.new(); e.physical_keycode = k; e.keycode = k; e.pressed = p
		Input.parse_input_event(e); await process_frame
func ev_click(pt: Vector2):
	var m := InputEventMouseMotion.new(); m.position = root.get_final_transform() * pt; Input.parse_input_event(m); await process_frame
	for p in [true, false]:
		var e := InputEventMouseButton.new(); e.button_index = MOUSE_BUTTON_LEFT; e.pressed = p
		e.position = root.get_final_transform() * pt; Input.parse_input_event(e); await process_frame
func dump(n: Node, depth: int) -> void:
	var s: Script = n.get_script()
	print("%s%s (%s)%s" % ["  ".repeat(depth), n.name, n.get_class(), "  [" + s.resource_path + "]" if s else ""])
	for c in n.get_children(): dump(c, depth + 1)
func run() -> void:
	for i in 5: await process_frame
	await ev_key(KEY_ENTER)
	await ev_key(KEY_1)
	await ev_click(game.grid.world_of(Vector2i(10, 1)))
	await ev_key(KEY_SPACE)
	for i in 40: await process_frame
	print("--- live tree, state=%d towers=%d monsters=%d projectiles=%d ---" % [game.state, game.grid.towers.size(), game.monsters.size(), game.projectiles.size()])
	dump(game, 0)
	quit(0)
