extends SceneTree
## Read-only: prints the live node tree of res://scenes/game.tscn after 2 s (no input), grouped by type.
var n := 0
func _initialize() -> void:
	change_scene_to_file("res://scenes/game.tscn")
func _physics_process(_d: float) -> bool:
	n += 1
	if n == 120:
		print("LIVE TREE res://scenes/game.tscn at 2.0 s (no input)")
		_dump(current_scene, 0)
		for a in ["GameState", "Audio", "Models"]:
			var node := root.get_node(a)
			print("autoload /root/%s (%s) children=%d" % [a, node.get_class(), node.get_child_count()])
		var total := [0]
		_count(current_scene, total)
		print("total nodes under the game scene: %d" % total[0])
		quit(0)
	return false
func _count(node: Node, total: Array) -> void:
	total[0] += 1
	for k in node.get_children():
		_count(k, total)
func _dump(node: Node, depth: int) -> void:
	print("%s%s (%s)%s" % ["  ".repeat(depth), node.name, node.get_class(), "" if not node.get_script() else " script=" + node.get_script().resource_path.get_file()])
	if depth >= 1:
		var counts := {}
		for k in node.get_children():
			var key: String = k.get_class() + ("" if not k.get_script() else " + " + str(k.get_script().resource_path.get_file()))
			counts[key] = counts.get(key, 0) + 1
		var parts := []
		for k in counts:
			parts.append("%d× %s" % [counts[k], k])
		if parts.size() > 0:
			print("%s  … %s" % ["  ".repeat(depth), ", ".join(parts)])
		return
	for k in node.get_children():
		_dump(k, depth + 1)
