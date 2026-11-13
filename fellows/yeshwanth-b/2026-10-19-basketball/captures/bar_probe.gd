extends SceneTree
## Read-only: prints the runtime size of the HUD's grenade and fuel bars and their hint labels (defect D-02).
var n := 0
func _initialize() -> void:
	change_scene_to_file("res://scenes/level_1.tscn")
func _process(_d: float) -> bool:
	n += 1
	if n == 30:
		var s := current_scene
		for name in ["grenade_bar", "fuel_bar"]:
			var b: ProgressBar = s.get(name)
			print("%s position=%s size=%s min=%s" % [name, b.position, b.size, b.get_combined_minimum_size()])
		for c in s.get_children():
			if c is CanvasLayer:
				for k in c.get_children():
					if k is Label and (k.text == "RMB / G" or k.text == "SHIFT"):
						print("label '%s' position=%s size=%s" % [k.text, k.position, k.size])
		quit(0)
	return false
