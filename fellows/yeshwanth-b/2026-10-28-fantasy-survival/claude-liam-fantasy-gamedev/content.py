SLUG = 'claude-liam-fantasy-gamedev'
TITLE = 'Fantasy Survival Crafting: Inside the Godot Code'
ASK = ('Please use Walker to convert my game design document about a first-person survival-crafting game — '
       'wake in an abandoned valley, gather sticks, gold and stone, craft an axe and a campfire, and survive '
       'one night until dawn — into a playable Godot project.')
PROJ = 'Fantasy Survival Crafting @ a514438'

ZOOM_OBJECTIVES = (0, 0, 1280, 720)

PAIRS = [
 dict(code='B03', result='B04', component='scenes', path='scenes/game.tscn', a=1, b=6,
  title='The Whole Game Scene', size=40,
  notes=[('Saved scene', 'one Node + world.gd'), ('Live at 2 s', '1,976 nodes, built in code')],
  cues=[('One plain Node', 5, 'the only node'), ('world dot g d', 6, 'the script that builds it all')],
  narration=("Here's the whole game scene: six lines. One plain Node, with world dot g d attached. There's no terrain in "
             "the editor, no player and no village. World dot g d builds all of it when the scene starts: nearly two "
             "thousand nodes."),
  take='day', start=600, end=800,
  rnarr=("Those six lines become this: the fade from black into the valley, the village, the mountains and the HUD, all "
         "built by one script."),
  obs='The game scene fades in fully built: terrain, village, mountains, HUD.'),
 dict(code='B05', result='B06', component='model-repair', path='scripts/model_library.gd', a=89, b=100,
  title='Every Model Gets Repaired', size=26,
  notes=[('Materials', 'rebuilt: the FBX files point at the artists\' .psd paths'), ('3ds Max packs', 'Z-up, turned −90° to stand upright')],
  cues=[('repairs the materials', 93, '_repair(model)'), ('rotates the model', 98, 'rotation_degrees.x = -90')],
  narration=("The art came from Unity asset packs, and it didn't load cleanly. Every model passes through this function. "
             "It repairs the materials, which still point at the original artists' files. For the packs exported from 3ds "
             "Max, it rotates the model ninety degrees, so Z-up becomes Y-up."),
  take='day', start=960, end=1143,
  rnarr=("The result in the orchard: fences, apple trees and village houses standing upright and textured, from those "
         "repaired packs."),
  obs='Orchard trees, fences and houses render upright with textures.'),
 dict(code='B07', result='B08', component='player', path='scripts/player.gd', a=105, b=114,
  title='Look Is Relative Motion', size=28,
  notes=[('Gate', 'no look while a window or the menu is open'), ('Pitch', 'clamped to ±89°')],
  cues=[('While no window is open', 106, 'world.can_look()'), ('turns the whole body', 112, 'rotation.y'),
        ('clamped', 113, 'clampf(…, ±89°)')],
  narration=("Look is relative mouse motion. While no window is open, each motion event turns the whole body left and right, "
             "and tilts only the camera up and down, clamped just short of straight up. The same look function serves the "
             "right stick."),
  take='day', start=700, end=830,
  rnarr="Here it's driven by synthetic mouse motion: a slow turn across the village, and back.",
  obs='Synthetic relative mouse motion turns the view across the village and back.'),
 dict(code='B09', result='B10', component='player', path='scripts/player.gd', a=161, b=172,
  title='A Ray From the Centre', size=26,
  notes=[('Reach', '4 m from the camera'), ('Target', 'anything with get_prompt()')],
  cues=[('re-cast', 167, 'force_raycast_update()'), ('with a prompt', 170, 'has_method("get_prompt")'),
        ('under the crosshair', 172, 'hud.set_interaction')],
  narration=("Selection is a ray from the centre of the screen, four metres long, re-cast every physics frame. If it hits "
             "something with a prompt, that becomes the target, and its prompt goes under the crosshair. E or a click acts "
             "on that target, and only that."),
  take='day', start=1430, end=1500,
  rnarr="Aim at a stick: its name and the action appear, E collects it, and the popup confirms.",
  obs='The stick prompt appears under the crosshair; E collects it with a pickup popup.'),
 dict(code='B11', result='B12', component='crafting', path='scripts/crafting_ui.gd', a=81, b=94,
  title='The Button That Hides', size=24,
  notes=[('Requirement', 'green if owned ≥ needed, red if not'), ('Craft button', 'created always, visible only when affordable')],
  cues=[('counts what you own', 83, 'inventory.count'), ('also checks the distance', 88, 'near_campfire()'),
        ('only visible', 93, 'craft.visible = can_craft')],
  narration=("Each recipe row counts what you own. A requirement is green if you have enough, red if not. A recipe that needs "
             "a fire also checks the distance. And the Craft button is always created, but it's only visible when every "
             "requirement is met."),
  take='day', start=2310, end=2420,
  rnarr="The axe row: three gold and three sticks, both owned, so the button shows. One click, and the materials are gone.",
  obs='The Axe row shows both requirements owned; Craft appears; one click consumes the materials.'),
 dict(code='B13', result='B14', component='objectives', path='scripts/world.gd', a=759, b=773,
  title='Ticked, but Zero of Three', size=22,
  notes=[('Counter', 'the inventory right now'), ('Done flag', 'remembers the craft')],
  cues=[('pairs a counter', 765, 'mini(sticks, 3)'), ('remembers', 765, 'axe_crafted or sticks >= 3'),
        ('reads zero of three', 766, '(0/3), ticked')],
  narration=("Here's the defect. Each objective line pairs a counter with a done flag. The flag remembers that the axe was "
             "crafted. But the counter reads the inventory right now, and crafting just emptied it. So a finished step "
             "reads zero of three."),
  take='day', zoom=ZOOM_OBJECTIVES, start=2420, end=2510,
  rnarr="Zoomed into the real frame: gather three sticks, ticked, zero of three. Gather three gold, ticked, zero of three.",
  obs='Zoomed engine frames: the ticked stick and gold objectives read (0/3) right after crafting the axe.'),
 dict(code='B15', result='B16', component='trees', path='scripts/choppable_tree.gd', a=37, b=47,
  title='Four Hits and a Fall', size=28,
  notes=[('Hits', '4 to fell'), ('Fall', 'away from the player, then a stump and 2 logs')],
  cues=[('subtracts one', 40, 'hits_left -= 1'), ('shake tween', 41, 'create_tween()'), ('At zero', 45, '_fall(from)')],
  narration=("A pine counts down its hits. Each chop subtracts one and plays a short shake tween. At zero it falls, and the "
             "fall direction is computed from where the player stands, so it always topples away from you."),
  take='day', start=2650, end=2790,
  rnarr="Four swings, four shakes, and the pine topples away.",
  obs='Four axe swings shake the pine, which then topples away from the player.'),
 dict(code='B17', result='B18', component='rabbits', path='scripts/rabbit.gd', a=51, b=62,
  title='Five Metres to Bolt', size=26,
  notes=[('Wander', 'Unity AI_Movement: walk 3–6 s, wait 5–7 s'), ('Flee', 'inside 5 m, at 5.5 m/s')],
  cues=[('checks its distance', 54, 'to_player'), ('Under five metres', 56, 'FLEE_RADIUS'), ('runs', 60, 'FLEE_SPEED')],
  narration=("Rabbits port Unity's wandering AI, with one addition. Every physics frame a rabbit checks its distance to the "
             "player. Under five metres, it turns directly away and runs at five and a half metres a second, playing its run "
             "clip."),
  take='day', start=3400, end=3500,
  rnarr="And there it goes. A sprint is faster, and one axe hit plays its death clip.",
  obs='A rabbit flees at close range; a sprinting axe hit plays its Dead clip.'),
 dict(code='B19', result='B20', component='campfire', path='scripts/world.gd', a=723, b=731,
  title='No Fires in the Lake', size=26,
  notes=[('Spot', '2.6 m ahead, on the ground'), ('Rule', 'below the water line + 0.2 m: refused')],
  cues=[('two point six metres', 727, 'forward * 2.6'), ('under the water line', 729, 'WATER_LEVEL + 0.2'),
        ('refuses', 730, 'show_message')],
  narration=("Placing the fire picks a spot two point six metres in front of you, on the ground. If that spot is under the "
             "water line, it refuses, says so, and the campfire stays in your inventory."),
  take='day', start=3840, end=3930,
  rnarr="Facing the lake: you can't build a fire in the water.",
  obs='Facing the lake, placing the campfire is refused with "You can\'t build a fire in the water".'),
 dict(code='B21', result='B22', component='inventory', path='scripts/inventory_slot.gd', a=54, b=63,
  title='Drag, Drop, Right-Click', size=28,
  notes=[('Drop', "Godot's own GUI drag and drop"), ('Full slot', 'swaps, unlike Unity')],
  cues=[('accepts any drop', 55, '_can_drop_data'), ('move the item', 58, 'move_item'), ('right-click', 61, 'MOUSE_BUTTON_RIGHT')],
  narration=("Drag and drop is Godot's own GUI system. A slot accepts any drop that carries an inventory index, and asks the "
             "inventory to move the item, which swaps if the target is full. A right-click on a slot uses the item."),
  take='day', start=4440, end=4560,
  rnarr="Dragging the first item to the last slot, with its sixty-percent preview, then a right-click to eat.",
  obs='An item is dragged to the last slot with a translucent preview; a right-click eats.'),
 dict(code='B23', result='B24', component='day-night', path='scripts/world.gd', a=587, b=605,
  title='The Clock and the Win', size=20,
  notes=[('Rate', '24 s per hour by day, 12 at night, 9× resting'), ('Victory', 'dawn + fire placed + a night near it + alive')],
  cues=[('Time advances', 590, 'hour += delta / …'), ('victory', 600, '_victory()'), ('posts the warning', 604, '"Night falls…"')],
  narration=("Time advances by the frame delta over seconds per hour: twenty-four by day, twelve at night, nine times faster "
             "while resting. When night turns to day with a fire placed, a night spent near it, and the player alive, that's "
             "victory. Night's arrival posts the warning."),
  take='night', start=4900, end=5110,
  rnarr="Dusk, then at eight o'clock: night falls, stay by your fire.",
  obs='The sky goes to night; at 20:00 the "Night falls" warning appears.'),
 dict(code='B25', result='B26', component='stats', path='scripts/player_state.gd', a=62, b=72,
  title='Two Ways to Lose Health', size=24,
  notes=[('Empty stat', '−1 health per second'), ('Cold', '−1 per 1.4 s at night, away from fire')],
  cues=[('An empty calorie', 62, 'current_calories <= 0'), ('the cold', 68, 'if cold:'), ('records its cause', 72, '"You froze in the night"')],
  narration=("Health has two drains here. An empty calorie or water bar costs one health a second. And at night, away from a "
             "fire, the cold costs one every one point four seconds. Each hit records its cause, which the defeat screen shows."),
  take='defeat', start=224, end=460,
  rnarr="Thirty metres from the fire: you are freezing, and the cold overlay creeps in.",
  obs='Away from the fire at night: "You are freezing!" and the blue cold overlay.'),
 dict(code='B27', result='B28', component='save-load', path='scripts/world.gd', a=807, b=829,
  title='One Dictionary, One Slot', size=18,
  notes=[('Written', 'user://savegame.json'), ('Load', 'rebuild the seeded world, then apply the changes')],
  cues=[('one dictionary', 815, 'var data := {'), ('the player', 818, '"player": […]'), ('removed', 824, '"removed"')],
  narration=("Saving writes one dictionary: day and hour, the player's position and look, stats, inventory, the equipped tool, "
             "flags, counters, removed entities, dropped items, fires and apples. Loading rebuilds the seeded world, then "
             "applies that list."),
  take='night', start=0, end=130,
  rnarr="Load Game: back at one in the afternoon, beside the fire, with everything in place.",
  obs='Load Game restores 13:09 with the placed fire, stats and inventory.'),
]

COMPONENTS = {
 'scenes': ('Six thin scenes; game.tscn is one Node with world.gd.', ['scenes/game.tscn', 'scenes/main_menu.tscn',
            'scenes/intro.tscn', 'scenes/instructions.tscn', 'scenes/victory.tscn', 'scenes/defeat.tscn'], ['B02', 'B03', 'B04', 'B29']),
 'world-builder': ('world.gd builds terrain, water, village, scenery, resources, player and UI at runtime.',
                   ['scripts/world.gd', 'scripts/terrain.gd', 'scripts/water_body.gd', 'scripts/pickup.gd'], ['B02', 'B04', 'B29']),
 'model-repair': ('model_library.gd rebuilds FBX materials, strips LOD/UCX meshes, stands Z-up packs upright, merges the rabbit clips.',
                  ['scripts/model_library.gd'], ['B05', 'B06']),
 'player': ('player.gd: relative look, WASD, sprint, jump, the centre ray, swing and interact.',
            ['scripts/player.gd'], ['B07', 'B08', 'B09', 'B10']),
 'crafting': ('crafting_ui.gd and item_db.gd: categories, requirement lines, the hidden Craft button, three blueprints.',
              ['scripts/crafting_ui.gd', 'scripts/item_db.gd'], ['B11', 'B12']),
 'objectives': ('_refresh_objectives in world.gd and the HUD list in hud.gd; the (0/3) defect.',
                ['scripts/world.gd', 'scripts/hud.gd'], ['B13', 'B14']),
 'trees': ('choppable_tree.gd (4 hits, fall away) and fruit_tree.gd (apples).',
           ['scripts/choppable_tree.gd', 'scripts/fruit_tree.gd'], ['B15', 'B16', 'B29']),
 'rabbits': ('rabbit.gd: Unity AI_Movement wander plus flee within 5 m; Dead clip on a hit.', ['scripts/rabbit.gd'], ['B17', 'B18']),
 'campfire': ('_place_campfire in world.gd and campfire.gd (particles, light, warmth radius).',
              ['scripts/world.gd', 'scripts/campfire.gd'], ['B19', 'B20']),
 'inventory': ('inventory_ui.gd and inventory_slot.gd: 21 slots, drag/drop swap, hover info, right-click use.',
               ['scripts/inventory_ui.gd', 'scripts/inventory_slot.gd'], ['B21', 'B22']),
 'day-night': ('_update_time in world.gd and the sky shader that blends three panoramas.',
               ['scripts/world.gd', 'scripts/shaders/sky.gdshader'], ['B23', 'B24']),
 'stats': ('player_state.gd: calories, water, starvation, cold, regeneration, causes of death.',
           ['scripts/player_state.gd'], ['B25', 'B26']),
 'save-load': ('save_game/_apply_save in world.gd and the JSON slot in game_state.gd.',
               ['scripts/world.gd', 'scripts/game_state.gd'], ['B27', 'B28']),
 'menus': ('Main menu, intro story, How to Play, pause menu and end screens.',
           ['scripts/main_menu.gd', 'scripts/intro.gd', 'scripts/instructions.gd', 'scripts/end_screen.gd', 'scripts/game_menu.gd'], ['B29']),
 'rendering': ('Terrain and water shaders.', ['scripts/shaders/terrain.gdshader', 'scripts/shaders/water.gdshader'], ['B29']),
 'audio': ('audio.gd: named sounds, music and night crickets; all synthesized.', ['scripts/audio.gd'], ['B29']),
 'tools-and-tests': ('_tools: the icon baker, screenshot drivers and the two playtests (32 + 10 checks) that call game functions directly.',
                     [], ['B29']),
 'config': ('project.godot (3 autoloads), export presets and README.', ['project.godot', 'export_presets.cfg', 'README.md'], ['B02', 'B29']),
 'art-assets': ('Models, textures, sky, UI, icons, fonts and audio files with their import settings.', [], ['B29']),
}

GREETING_NARR = ("Hola, this is Liam, in for Bear. That's the kind of prompt Walker expects, reconstructed here, not a "
                 "transcript. This time we open the project itself: a piece of code, then the exact thing it does on screen, "
                 "in the real build.")
OUTPUT = ['Built: 6 thin scenes, 23 scripts and 3 shaders, 3,303 lines.', 'Art from Unity asset packs, repaired at load time.']
BLUF_NARR = ("Fantasy Survival Crafting is built in code. Its six scene files are a few lines each, and thirty-three hundred "
             "lines of GDScript build the whole valley at runtime. So every piece of code we read has a result you can watch.")
BLUF_TEXT = "Fantasy Survival Crafting\nis built from scenes.\nSix scene files, a few lines each,\nand 3,303 lines of GDScript\nthat build the whole valley."
TREE_NARR = ("Open the game scene and there's one node. Run it, and world dot g d builds the rest: a Level node holding the "
             "terrain, the lake, two hundred and sixty-six props, eighty-two pickups, thirty-six pines, nine rabbits and "
             "forty-seven grass chunks, then the sky, the sun, and three canvas layers for the HUD, the windows and the menu. "
             "Nearly two thousand nodes.")
REST_NARR = ("The rest of the project, in one pass. A main menu, a three-page story, How to Play, a pause menu and two end "
             "screens. Three shaders for terrain, water and sky. An audio autoload of synthesized sounds. And a tools folder "
             "with two playtests that pass forty-two checks, by calling game functions directly. The film's captures pressed "
             "the keys instead.")
VERDICT_NARR = ("Verdict. This is a project you can read top to bottom: thin scenes, one world script that builds everything, a "
                "repair layer for the asset packs, and a save that lists exactly what changed. One display bug: ticked objectives "
                "that read zero of three. Its own tests call functions; the captures pressed keys. And nobody has played it yet.")
VERDICT_HEADING = 'Readable code, one display bug'
VERDICT_LINES = ['Implemented: 6 thin scenes; world.gd builds ~2,000 nodes; FBX repair at load.',
                 'Good habits: one centre-ray target; recipes gated by visibility; one save dictionary.',
                 'Defect on screen: ticked objectives read 0/3 after a recipe uses the materials.',
                 'Not judged: fun, tuning, balance. 0 human playtests.']
HANDOFF_NARR = ("Your turn. Paste this into Claude in your own Godot project: Use Walker on my Godot project. Find one place "
                "where the screen shows state from two different sources, like a counter and a done flag, and predict a moment "
                "when they disagree. Then write a capture that proves or disproves it with real input, and only after that, "
                "propose the smallest code change. Liam, in for Bear.")
HANDOFF_COMMAND = ("Use Walker on my Godot project. Find one place where the screen shows state from two different sources, "
                   "like a counter and a done flag, and predict a moment when they disagree. Then write a capture that proves "
                   "or disproves it with real input, and only after that, propose the smallest code change.")
