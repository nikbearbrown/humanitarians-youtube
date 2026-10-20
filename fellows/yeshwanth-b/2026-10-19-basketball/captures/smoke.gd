extends SceneTree
# Loads every scene and lets it run 150 physics frames; prints a summary line per scene.
var scenes := ["main_menu", "intro", "instructions", "level_1", "level_2", "level_3", "victory", "defeat"]
var idx := -1
var frames := 0
func _initialize() -> void:
	_next()
func _next() -> void:
	idx += 1
	if idx >= scenes.size():
		print("SMOKE DONE")
		quit(0)
		return
	frames = 0
	change_scene_to_file("res://scenes/%s.tscn" % scenes[idx])
func _physics_process(_d: float) -> bool:
	frames += 1
	if frames == 150:
		var s := current_scene
		var extra := ""
		if s and "lives" in s:
			extra = " lives=%d health=%d eggs=%d/%d chickens=%d pipes=%d" % [s.lives, s.health, s.eggs_collected, s.eggs_needed, get_nodes_in_group("chickens").size(), s.pipes.size()]
		print("SCENE %s ok nodes=%d%s" % [scenes[idx], _count(root), extra])
		_next()
	return false
func _count(n: Node) -> int:
	var c := 1
	for k in n.get_children():
		c += _count(k)
	return c
