extends SceneTree
## Prints the live node tree of arena 1 after 3 s (input-free), grouped by parent, for the gamedev film.
var n := 0
func _initialize() -> void:
	change_scene_to_file("res://scenes/level_1.tscn")
func _physics_process(_d: float) -> bool:
	n += 1
	if n == 180:
		print("LIVE TREE res://scenes/level_1.tscn at 3.0 s (no input)")
		_dump(current_scene, 0)
		for a in ["GameState", "Audio"]:
			var node := root.get_node(a)
			print("autoload /root/%s (%s) children=%d" % [a, node.get_class(), node.get_child_count()])
		quit(0)
	return false
func _dump(node: Node, depth: int) -> void:
	var kids := node.get_children()
	var counts := {}
	for k in kids:
		var key: String = k.get_class() + ("" if not k.get_script() else " + " + str(k.get_script().resource_path.get_file()))
		counts[key] = counts.get(key, 0) + 1
	print("%s%s (%s)%s" % ["  ".repeat(depth), node.name, node.get_class(), "" if not node.get_script() else " script=" + node.get_script().resource_path.get_file()])
	if depth >= 2:
		var parts := []
		for k in counts:
			parts.append("%d× %s" % [counts[k], k])
		if parts.size() > 0:
			print("%s  … %s" % ["  ".repeat(depth), ", ".join(parts)])
		return
	for k in kids:
		_dump(k, depth + 1)
