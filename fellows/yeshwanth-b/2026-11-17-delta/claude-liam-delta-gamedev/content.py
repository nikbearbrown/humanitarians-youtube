SLUG = 'claude-liam-delta-gamedev'
TITLE = 'Delta: Inside the Godot Code'
ASK = ('Please use Walker to convert my game design document about a first-person puzzle game — a space station '
       'folded into two layers, energy cells carried between machines, and an unstable core taken past two '
       'guardians — into a playable Godot project.')
PROJ = 'Delta @ 25e03b2'

C1, C2, D, E = 'campaign1', 'campaign2', 'defeat', 'extras'

PAIRS = [
 dict(code='B03', result='B04', component='scenes', path='scenes/level_01.tscn', a=1, b=7,
  title='The Whole Level Scene', size=40,
  notes=[('Saved scene', 'one Node3D + level.gd, level_id = 1'), ('Live at 8 s', '604 nodes, built in code')],
  cues=[('One Node3D', 5, 'the only node'), ('level dot g d', 3, 'the script'), ('level I D', 7, 'level_id = 1')],
  narration=("Here's the whole of level one: seven lines. One Node3D, with level dot g d attached, and a single property, "
             "level I D, set to one. All twelve level scenes are the same file with a different number. Everything else "
             "is built when the scene starts."),
  take=C1, start=304, end=520,
  rnarr=("Those seven lines become this: walls, floors, lamps and windows from the modular kit, the desk, the cell, the "
         "socket, the door, the lift, and VEGA's first line."),
  obs='Level 1 loads fully built: kit walls and lamps, the cell on a desk, socket, door, exit lift, VEGA subtitle.'),
 dict(code='B05', result='B06', component='levels', path='scripts/levels.gd', a=29, b=47,
  title='A Level Is a Text Map', size=22,
  notes=[('Grid', 'each character is a 5 × 5 m cell'), ('Legend', 'c cell on a desk · S socket · D door · G lift')],
  cues=[('dot is floor', 33, '"  .......  "'), ('the at sign', 34, '@ start'), ('the c', 43, '"c": [...]'),
        ('S is a socket', 45, '"S": socket powers d1'), ('D is the door', 46, '"D": door d1')],
  narration=("And the number picks this entry. Each character is a five metre cell: a dot is floor, the at sign is the "
             "start, G the lift. The legend says what the letters mean: the c is a desk with a charged cell on it, S is a "
             "socket that powers d one, and D is the door with that id."),
  take=C1, start=520, end=1015,
  rnarr="That map, played: the cell on the desk, the socket beside the door, and the lift behind it.",
  obs='The cell is on a desk, the socket beside door d1 powers it, and the lift lies beyond.'),
 dict(code='B07', result='B08', component='player', path='scripts/player.gd', a=118, b=131,
  title='Look Needs a Captured Mouse', size=24,
  notes=[('Mouse', '0.11° per pixel × sensitivity'), ('Keys', 'jump · interact · pickup · switch_dimension')],
  cues=[('captured', 121, 'MOUSE_MODE_CAPTURED'), ('turns the view', 123, '_look(...)'), ('E', 127, 'try_interaction'),
        ('F', 129, 'try_pickup'), ('Q', 131, 'begin_switch')],
  narration=("All player input lands here. Mouse motion turns the view, but only while the mouse is captured. Then the "
             "actions: jump, E for interact, F for pickup, and Q to switch dimension."),
  take=E, start=568, end=740,
  rnarr="The mouse sweeps the view left and right, Shift runs, and Space jumps.",
  obs='Captured-mouse look turns the view; Shift runs; Space jumps.'),
 dict(code='B09', result='B10', component='interaction', path='scripts/player.gd', a=282, b=298,
  title='Pickup Is a Ray', size=20,
  notes=[('Ray', 'look_target(): 3 m from the camera'), ('In a device', 'comes out with E, not F')],
  cues=[('already holding', 283, 'if held'), ('the ray', 289, 'look_target()'), ('inside a device', 292, 'has_holder()'),
        ('picked up', 296, 'item.pickup(self)')],
  narration=("F drops whatever you're already holding. Otherwise it asks the ray what's under the crosshair. If it's an "
             "item inside a device, it tells you to use E instead. If not, the item is picked up, and the level hears an "
             "event."),
  take=C1, start=575, end=720,
  rnarr="So the cell is picked up only when the crosshair is on it, and then it floats in front of the camera.",
  obs='F picks up the cell under the crosshair; it is held in front of the camera.'),
 dict(code='B11', result='B12', component='shifting', path='scripts/level.gd', a=673, b=694,
  title='A Shift Can Be Refused', size=18,
  notes=[('Distance', '±50 m between the layers'), ('Refused', 'no floor, or the capsule overlaps rock')],
  cues=[('the other layer', 674, 'other := ...'), ('no floor', 678, 'walkable(other, cell)'),
        ('capsule', 683, 'CapsuleShape3D'), ('anything solid', 692, 'intersect_shape')],
  narration=("Where a shift lands is decided here. It looks at the other layer. If that cell has no floor and no platform, "
             "it refuses. Otherwise it tests a player-sized capsule fifty metres away, and if anything solid overlaps "
             "it, it refuses again. Unity's switcher had no such check."),
  take=D, start=380, end=500,
  rnarr="So in a corner where Lower Delta has no floor, Q only gives a toast: something solid is in the way.",
  obs='Q at a spot with no floor below is refused; the toast reads "Something solid is in the way on the other side".'),
 dict(code='B13', result='B14', component='shifting', path='scripts/player.gd', a=351, b=375,
  title='Never Shift Holding the Core', size=18,
  notes=[('Unity', 'DimensionSwitcher: Damage() + ExplodeHeldObject()'), ('Then', 'move ±50 m, item comes along')],
  cues=[('peak of the glitch', 351, '_at_glitch_peak'), ('the core', 356, 'held.kind == "core"'), ('critical', 362, 'enter_critical_state'),
        ('moves', 370, 'global_position = target')],
  narration=("At the peak of the glitch, the shift happens. Unless you're holding the core: then you take damage, it's "
             "thrown out of your hands, and it goes critical. Otherwise you move to the target, and whatever you hold "
             "moves with you."),
  take=C2, start=7180, end=7310,
  rnarr="Shift with the core: the damage flash, the core flies, explodes, and rebuilds itself at its spawn.",
  obs='Shifting while holding the core: damage flash, the core is ejected, explodes and respawns.'),
 dict(code='B15', result='B16', component='devices', path='scripts/charger.gd', a=63, b=80,
  title='Charging Is One Line per Frame', size=20,
  notes=[('Rate', '750 / s charging, 1500 / s draining'), ('Busy', "can't be used while working")],
  cues=[('already full', 66, 'item.is_full()'), ('working', 68, 'working = true'), ('adds', 74, 'energy + rate * delta'),
        ('stops', 76, 'is_full()')],
  narration=("A charger ignores a cell that's already full. Otherwise it starts working, and each frame adds seven "
             "hundred and fifty times the frame time to the cell. When the cell is full, it stops, plays a sound, and "
             "tells the level."),
  take=C1, start=2740, end=2920,
  rnarr="The prompt says charging while it works. Four seconds later, the cell is full, and E takes it out.",
  obs='The charger takes the empty cell, shows Charging..., fills it, and E removes it.'),
 dict(code='B17', result='B18', component='devices', path='scripts/gate.gd', a=72, b=87,
  title='The Gate Throws It Back', size=20,
  notes=[('Rejects', 'a cell with charge, or the core'), ('Arc', 'shown for 0.3 s')],
  cues=[('charge', 73, 'not body.is_empty()'), ('which side', 78, 'Throw it back'), ('knocks it out', 81, 'item.drop()'),
        ('arc', 83, '_show_arc')],
  narration=("The arc gate checks what crosses its field. A cell with any charge, or the core, is rejected: it works out "
             "which side the item came from, knocks it out of your hands, throws it back that way, and draws a lightning "
             "arc."),
  take=C1, start=7060, end=7140,
  rnarr="Walking in with a charged cell: the arc, and the cell lands back on this side.",
  obs='Walking into the arc gate with a charged cell: an arc flashes and the cell is thrown back.'),
 dict(code='B19', result='B20', component='devices', path='scripts/duplicator.gd', a=72, b=87,
  title='Only One Copy', size=20,
  notes=[('Refuses', 'empty cradle · a copy of a copy'), ('Replaces', 'the previous copy is removed')],
  cues=[('empty', 73, 'held == null'), ("won't copy a copy", 76, 'held == last_clone'), ('removed', 82, 'queue_free()'),
        ('new copy', 83, 'make_clone')],
  narration=("The duplicator's button refuses an empty cradle, and it won't copy a copy. If an earlier copy exists, that "
             "one is removed first. Then it makes the new copy beside the cradle, with a purple flash."),
  take=C2, start=2010, end=2120,
  rnarr="The button pressed with the cell in the cradle: the flash, and a second cell beside it.",
  obs='Pressing the duplicator button makes a copy of the cell next to the cradle.'),
 dict(code='B21', result='B22', component='guardians', path='scripts/final.gd', a=481, b=509,
  title='Follow, Lock, Strike', size=18,
  notes=[('Follow', '5 s, the sparks ride on the player'), ('Lock', '3 s, then the lightning')],
  cues=[('attached to the player', 485, 'not spark_locked'), ('lock', 488, 'spark_locked = true'), ('ring', 494, 'TorusMesh'),
        ('strike', 507, '_strike(spark_dim, target)')],
  narration=("A strike is a timer. For five seconds the sparks are attached to the player. Then they're moved into the "
             "world where they are, and locked, with a red ring of the strike radius. Three seconds later, the lightning "
             "hits that spot."),
  take=C2, start=9180, end=9400,
  rnarr="The guardian has found you: the sparks follow, lock, the warning says get clear, and the script does.",
  obs='Sparks follow the player, lock with a red ring and STRIKE LOCKED warning; the player gets clear before the bolt.'),
 dict(code='B23', result='B24', component='guardians', path='scripts/final.gd', a=524, b=532,
  title='The Strike Is the Key', size=24,
  notes=[('Shield', 'falls to a strike within 3 m'), ('Player', 'dies within 3 m in the same layer')],
  cues=[('shield', 524, 'shield_up and shield_generator'), ('within', 527, 'flat.length() < STRIKE_RADIUS'),
        ('destroyed', 528, '_destroy_shield()'), ('the player', 530, 'distance_to(target) < STRIKE_RADIUS')],
  narration=("The same strike is how the level is solved. If the shield generator stands within three metres of where "
             "the lightning lands, the shield is destroyed. And if the player is within three metres, the player dies."),
  take=C2, start=13440, end=13660,
  rnarr="So the script waits beside the shield generator until a strike locks there, then steps clear. The shield goes down.",
  obs='A strike locked beside the shield generator destroys it once the player has stepped clear.'),
 dict(code='B25', result='B26', component='hud', path='scripts/hud.gd', a=313, b=318,
  title='An Invisible Wall Over the Buttons', size=26,
  notes=[('Added last', 'a full-screen CenterContainer'), ('Defect', 'it takes every click')],
  cues=[('options panel', 313, 'OptionsPanel.new()'), ('full-screen', 316, 'PRESET_FULL_RECT'), ('added last', 318, 'add_child(options_center)')],
  narration=("Here's the first defect. The pause menu is built, and then the options panel is wrapped in a full-screen "
             "centre container, added last. Even with the options hidden, that container covers the whole screen, on "
             "top of the pause buttons, and catches every click."),
  take=D, start=2063, end=2160,
  rnarr="So a mouse click on Resume does nothing. Only the arrow keys and Enter reach the menu.",
  obs='A mouse click on Resume in the pause menu does not register; the game stays paused.'),
 dict(code='B27', result='B28', component='level-flow', path='scripts/level.gd', a=804, b=818,
  title='Keys a Paused Node Never Hears', size=20,
  notes=[('Meant', 'Esc toggles · R restarts · N skips while paused'), ('Defect', 'the level pauses with the tree')],
  cues=[('pause', 807, 'is_action_pressed("pause")'), ('while paused', 812, 'elif paused and ...'),
        ('restart', 813, '"restart"'), ('skip', 815, '"skip_level"')],
  narration=("And the second. The level's input handler toggles pause on Escape, and while paused, R restarts and N skips. "
             "But this node pauses with the rest of the tree, so once the game is paused, it never receives another key. "
             "Escape won't resume, and R and N do nothing."),
  take=D, start=2395, end=2490,
  rnarr="R, pressed while paused: nothing. The menu's own Restart level, chosen with the keys, works.",
  obs='R while paused does nothing; Restart level from the menu restarts the level.'),
]

COMPONENTS = {
 'scenes': ('Fifteen thin scenes; each level is one Node3D with level.gd and a level_id.',
            ['scenes/level_%02d.tscn' % i for i in range(1, 13)] + ['scenes/main_menu.tscn', 'scenes/instructions.tscn',
             'scenes/credits.tscn'], ['B02', 'B03', 'B04', 'B29']),
 'levels': ('levels.gd: the twelve ASCII maps, legends and narrator lines; level.gd builds them.',
            ['scripts/levels.gd', 'scripts/level.gd'], ['B02', 'B05', 'B06']),
 'player': ('player.gd: movement, look, input, health and camera shake; the playtest autopilot hook.',
            ['scripts/player.gd'], ['B07', 'B08']),
 'interaction': ('player.gd ray, pickable.gd items, interactable.gd and holder_device.gd devices.',
                 ['scripts/player.gd', 'scripts/pickable.gd', 'scripts/interactable.gd', 'scripts/holder_device.gd'],
                 ['B09', 'B10']),
 'shifting': ('DimensionSwitcher port in player.gd; switch_target in level.gd; glitch.gdshader.',
              ['scripts/player.gd', 'scripts/level.gd', 'scripts/glitch.gdshader'], ['B11', 'B12', 'B13', 'B14']),
 'devices': ('device.gd power ports and every device script; plasma and hologram shaders.',
             ['scripts/device.gd', 'scripts/socket.gd', 'scripts/charger.gd', 'scripts/door.gd', 'scripts/platform.gd',
              'scripts/button.gd', 'scripts/pad.gd', 'scripts/gate.gd', 'scripts/duplicator.gd', 'scripts/teleporter.gd',
              'scripts/plasma.gd', 'scripts/generator.gd', 'scripts/plasma.gdshader', 'scripts/hologram.gdshader'],
             ['B15', 'B16', 'B17', 'B18', 'B19', 'B20']),
 'guardians': ('final.gd: the guardians, strikes, shockwaves, vault, shield, stabiliser and ending.',
               ['scripts/final.gd'], ['B21', 'B22', 'B23', 'B24']),
 'hud': ('hud.gd: crosshair prompt, subtitles, banners, pause menu, options and complete panel; options_panel.gd.',
         ['scripts/hud.gd', 'scripts/options_panel.gd'], ['B25', 'B26']),
 'level-flow': ('level.gd pause, completion, death and narrator; game_state.gd campaign, input map and save.',
                ['scripts/level.gd', 'scripts/game_state.gd'], ['B27', 'B28']),
 'menus': ('main_menu.gd, instructions.gd and credits.gd.', ['scripts/main_menu.gd', 'scripts/instructions.gd',
           'scripts/credits.gd'], ['B29']),
 'audio': ('audio.gd autoload: named sounds, loops, music and the narrator duck; bus layout.',
           ['scripts/audio.gd', 'default_bus_layout.tres'], ['B29']),
 'kit': ('kit.gd autoload: model instancing and flat materials for untextured devices.', ['scripts/kit.gd'], ['B29']),
 'tools-and-tests': ('_tools: the asset converter, sky shrinker, screenshot and model preview tools, and the playtest.',
                     [], ['B29']),
 'config': ('project.godot (3 autoloads, Forward+, Jolt), export presets and README.',
            ['project.godot', 'export_presets.cfg', 'README.md'], ['B02', 'B29']),
 'art-assets': ('The sci-fi kit, device meshes, textures, sky, UI images, fonts and synthesized audio, with import settings.',
                [], ['B29']),
}

GREETING_NARR = ("Hola, this is Liam, in for Bear. That's the kind of prompt Walker expects, reconstructed here, not a "
                 "transcript. This time we open the project itself: a piece of code, then the exact thing it does on "
                 "screen, in the real build.")
OUTPUT = ['Built: 15 thin scenes, 27 scripts and 3 shaders, 5,319 lines.', 'Art from the Unity folder; levels and sound authored.']
BLUF_NARR = ("Delta is built in code. Its twelve level scenes are seven lines each, and fifty-three hundred lines of "
             "GDScript and shader code build every wall, device and menu at runtime, from text maps. So every piece of code we read has "
             "a result you can watch.")
BLUF_TEXT = ("Delta\nis built from scenes.\nTwelve level scenes, seven lines each,\nand 5,319 lines of GDScript\n"
             "that build every level.")
TREE_NARR = ("Open a level scene and there's one node. Run it for eight seconds, and level dot g d has built the rest: an "
             "environment and a sun, an items node with the cell, Upper Delta with its walls, lamps, socket and door, "
             "the HUD, and the player with a camera. Six hundred and four nodes.")
REST_NARR = ("The rest of the project, in one pass. A main menu with Continue, Select level and options, a How to play "
             "page, and credits. An audio autoload with synthesized sounds and music. A kit autoload for the models. "
             "Tools that convert the Unity art, and a playtest that steers through a hook in the player script. The "
             "film's captures pressed the keys instead.")
VERDICT_NARR = ("Verdict. This is a project you can read top to bottom: thin scenes, levels as text, one small script per "
                "device. Two real defects live in the pause menu: a container that eats clicks, and a handler that "
                "pauses itself. The game's own test never paused, so it never saw them. And nobody has played it yet.")
VERDICT_HEADING = 'Readable code, two pause defects'
VERDICT_LINES = ['Implemented: 15 thin scenes; level.gd builds each level from an ASCII map.',
                 'Good habits: shift refusal; a core that rebuilds; one copy at a time.',
                 'Defects: hud.gd:316 container eats clicks; level.gd:804 never runs while paused.',
                 'Not judged: fun, difficulty, level 12 fairness. 0 human playtests.']
HANDOFF_NARR = ("Your turn. Paste this into Claude in your own Godot project: Use Walker on my Godot project. Find one input "
                "handler that is supposed to work while the game is paused. Predict whether it will ever run. Then write a "
                "capture that pauses with real input, presses the key, and checks what happened, and only after that, "
                "propose the smallest fix. Liam, in for Bear.")
HANDOFF_COMMAND = ("Use Walker on my Godot project. Find one input handler that is supposed to work while the game is "
                   "paused. Predict whether it will ever run. Then write a capture that pauses with real input, presses "
                   "the key, and checks what happened, and only after that, propose the smallest fix.")
