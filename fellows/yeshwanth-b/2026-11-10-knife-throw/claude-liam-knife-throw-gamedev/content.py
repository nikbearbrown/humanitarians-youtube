SLUG = 'claude-liam-knife-throw-gamedev'
TITLE = 'Gino: Knife Throw, Inside the Godot Code'
ASK = ('Please use Walker to convert my game design document about a 2D action platformer — guide Gino home '
       'through three hostile valleys with a sword combo, three throwing knives and three hearts — into a '
       'playable Godot project.')
PROJ = 'Gino: Knife Throw @ cffbb01'

PAIRS = [
 dict(code='B03', result='B04', component='scenes', path='scenes/level_1.tscn', a=1, b=7,
  title='The Whole Level Scene', size=40,
  notes=[('Saved scene', 'one Node2D + level.gd, level_id = 1'), ('Live at 8 s', '200 nodes, built in code')],
  cues=[('One Node2D', 5, 'the only node'), ('level dot g d', 3, 'the script'), ('level I D', 7, 'level_id = 1')],
  narration=("Here's the whole of level one: seven lines. One Node2D, with level dot g d attached, and a single "
             "property, level I D, set to one. Levels two and three are the same file with a different number. "
             "Everything else is built when the scene starts."),
  take='campaign', start=314, end=600,
  rnarr=("Those seven lines become this: the tiles, the props, the parallax background, the HUD, the level banner, "
         "and the first hint, all built by one script."),
  obs='Level 1 loads fully built: terrain, props, background, HUD, LEVEL 1 ROCKY OUTSKIRTS banner, first hint.'),
 dict(code='B05', result='B06', component='level-build', path='scripts/level.gd', a=380, b=405,
  title='A Letter Becomes an Enemy', size=20,
  notes=[('Map', 'scripts/levels.gd, one character per tile'), ('Letters', 'P · b w p · o O k h · D · 1–9')],
  cues=[('reads the map', 383, '_cell(x, y)'), ('A P', 387, '"P"'), ('b, w or p', 397, '"b", "w", "p"'),
        ('counts it', 405, 'enemies_total += 1')],
  narration=("The level script reads the map one tile at a time. A P becomes Gino, with his signals wired to the HUD. "
             "A b, w or p becomes a bat, a walker or a plant, standing on that tile, and the level counts it. Diamonds, "
             "daggers, hearts, the door and the hint crystals come from letters too."),
  take='campaign', start=420, end=760,
  rnarr=("So every enemy and diamond on screen is a letter in a text map. Here's the first walker, standing exactly "
         "where its w is."),
  obs='The first walker and diamonds appear at their map positions; the walker turns and runs at Gino.'),
 dict(code='B07', result='B08', component='player', path='scripts/player.gd', a=157, b=175,
  title='Run, Jump, Cut the Jump', size=20,
  notes=[('Run', '105 px/s, accel 1200, decel 1600'), ('Jump', '320 px/s · coyote 0.1 s · buffer 0.12 s')],
  cues=[('target speed', 157, 'move * RUN_SPEED'), ('jumps only', 164, 'jump_buffer and coyote'),
        ('cuts the jump', 171, 'velocity.y *= JUMP_CUT'), ('gravity', 175, 'GRAVITY * delta')],
  narration=("Running eases toward a target speed, faster on the ground than in the air. Gino jumps only when a "
             "recent press and a recent floor overlap: that's the buffer and the coyote time. Let go of Space early "
             "and it cuts the jump to under half. Then gravity, capped at a maximum fall."),
  take='campaign', start=2380, end=2650,
  rnarr=("Space held the whole way: the full jump, long enough to clear the walker waiting below. The driver chose "
         "that jump; the physics are the game's."),
  obs='A held full jump carries Gino over and past a walker at the foot of the rock.'),
 dict(code='B09', result='B10', component='combat', path='scripts/player.gd', a=256, b=267,
  title='The Combo Chains on a Finished Swing', size=24,
  notes=[('Queue', 'J during a swing, from its second frame'), ('Chain', 'attack1 → 2 → 3 → 4, on the ground')],
  cues=[('finishes', 259, '"attack1", …'), ('queued', 262, 'combo_queued and combo < 4'),
        ('next swing', 264, '_start_swing'), ('back to normal', 266, 'state = "normal"')],
  narration=("The combo advances only when a swing finishes. If J was queued during it, the combo is under four, and "
             "Gino is on the ground, the next swing starts. Otherwise Gino goes back to normal and the count resets."),
  take='defeat', start=640, end=980,
  rnarr=("In the takes, the queue rarely survives: each hit pushes the walker back out of reach, so the script lands "
         "single slashes and two-hit chains. The fourth swing never appears on screen."),
  obs='Repeated J presses land single slashes and at most two-hit chains; the walker is knocked back each hit.'),
 dict(code='B11', result='B12', component='combat', path='scripts/player.gd', a=54, b=60,
  title='Every Swing Is a Table Row', size=30,
  notes=[('Columns', 'first frame, last frame, reach box, damage'), ('Finisher', 'attack4: 40 damage')],
  cues=[('first and last animation', 55, '[1, 3, …]'), ('reach box', 55, 'Rect2(-22, -30, 52, 28)'),
        ('forty', 58, '"attack4": … 40')],
  narration=("Each swing is a row: the first and last animation frame that can hit, a reach box relative to Gino's "
             "feet, and the damage. Twenty for the first three swings and the jump attack, forty for the magic blast. "
             "A hit is recorded per swing, so one swing can't hit the same enemy twice."),
  take='campaign', start=700, end=840,
  rnarr=("Twenty a slash: the walker flashes white on each hit, and the screen shakes a little. Five hits and it's "
         "gone, plus twenty-five."),
  obs='The first walker takes repeated 20-damage slashes with a white flash and shake, then dies (+25).'),
 dict(code='B13', result='B14', component='knife', path='scripts/knife.gd', a=28, b=45,
  title='A Knife in Four Substeps', size=22,
  notes=[('Speed', '420 px/s, 4 substeps a frame'), ('Ends', 'enemy (30) · rock · 1.3 s · off the level')],
  cues=[('four small steps', 31, 'SUBSTEPS'), ('enemy', 36, 'intersects(hurt_rect())'), ('rock', 41, 'is_solid_at(tip)'),
        ('expires', 44, 'age > LIFETIME')],
  narration=("A knife moves in four small steps every frame, so it can't skip through a thin enemy. Each step checks "
             "every enemy: a touch deals thirty and breaks the knife. Then it checks rock at the tip. And it expires "
             "after one point three seconds, or off the edge of the level."),
  take='campaign', start=1590, end=1750,
  rnarr="K: the knife flies straight across the screen, hits the walker for thirty, and breaks.",
  obs='A thrown knife crosses the screen and breaks on the walker; the knife count drops to 0.'),
 dict(code='B15', result='B16', component='enemies', path='scripts/walker.gd', a=54, b=66,
  title='The Walker Never Leaves Its Ledge', size=22,
  notes=[('Chase', 'inside 120 × 44 px, at 50 px/s'), ('Ledges', '_can_walk: floor ahead, no wall')],
  cues=[('turns to face', 55, 'facing = …'), ('chases', 57, 'chasing'), ('only if it can walk', 59, '_can_walk(facing)'),
        ('bite', 65, 'player_in(CONE, facing)')],
  narration=("Outside an attack, the walker turns to face Gino. It chases while he's within its range box, but only "
             "if it can walk: there has to be floor ahead and no wall. And when Gino enters the cone in front of it, "
             "the bite starts."),
  take='campaign', start=5300, end=5460,
  rnarr=("So a walker across a gap just waits. Gino jumps it, lands past, and the bite still catches him: a full "
         "heart. Then the sword."),
  obs='A walker waits at a gap edge; after Gino jumps past, its bite costs a full heart; then it is defeated.'),
 dict(code='B17', result='B18', component='enemies', path='scripts/bat.gd', a=46, b=72,
  title='The Bat Curls, Then Strikes', size=18,
  notes=[('Wind-up', '0.7 s before the strike box opens'), ('Chase', 'steers at Gino within 104 px')],
  cues=[('slows to a stop', 47, 'move_toward(Vector2.ZERO)'), ('strike', 50, 'open_attack(STRIKE_BOX)'),
        ('steers', 59, 'to_player.normalized() * SPEED'), ('either side', 69, 'player_in(CONE, ±1)')],
  narration=("While it's attacking, the bat slows to a stop, and only after seven tenths of a second does the strike "
             "box open. Otherwise it steers at Gino's chest whenever he's near, or bobs at home. It checks a cone on "
             "either side, so it can strike in both directions."),
  take='campaign', start=2880, end=3070,
  rnarr="A bat in level two: a knife first, thirty damage, then the sword, while it hangs in the air.",
  obs='Gino throws a knife at a bat, then slashes it down.'),
 dict(code='B19', result='B20', component='health', path='scripts/player.gd', a=288, b=311,
  title='One Hit, Then a Grace Period', size=18,
  notes=[('Grace', '1.1 s invulnerable, 0.35 s hurt'), ('Knockback', '130 px/s away, 170 up')],
  cues=[('A hit is ignored', 289, 'invulnerable > 0.0'), ('loses the damage', 294, 'health - amount'),
        ('At zero', 299, 'health <= 0'), ('knocked away', 310, 'velocity = …')],
  narration=("A hit is ignored while Gino is dead, at a door, or still invulnerable. Otherwise he loses the damage, "
             "flashes, and the screen shakes. At zero, he dies. If not, he's hurt for a third of a second, "
             "invulnerable for a little over one, and knocked away from whatever hit him."),
  take='campaign', start=4795, end=4900,
  rnarr="Floor spikes, one damage: half a heart, a knockback away from the spikes, and Gino blinks.",
  obs='Spikes cost half a heart; Gino is knocked back and blinks.'),
 dict(code='B21', result='B22', component='level-flow', path='scripts/level.gd', a=821, b=839,
  title='The Door Freezes the Game', size=20,
  notes=[('Unity', 'Door.cs: W freezes the game, victory panel'), ('Panel', 'score · diamonds · enemies · knives · time')],
  cues=[('Entering the door', 821, '_enter_door'), ('waits', 828, 'create_timer(0.8)'),
        ('records', 832, 'complete_level'), ('pauses', 834, 'paused = true')],
  narration=("Entering the door works only in play. It hides the prompt, walks Gino in, waits under a second, then "
             "completes the level: it records the run, pauses the tree, and fills the panel with score, diamonds, "
             "enemies, knives and time."),
  take='campaign', start=1985, end=2165,
  rnarr="W at the door, and the panel: a hundred thirty-five, six of ten diamonds, three of five enemies, forty-three seconds.",
  obs='W at the door opens LEVEL COMPLETE: Score 135, Diamonds 6/10, Enemies 3/5, Knives 0, Time 0:43.'),
 dict(code='B23', result='B24', component='input-map', path='scripts/game_state.gd', a=170, b=192,
  title='The Input Map Is Code', size=18,
  notes=[('Keys', 'A/D or arrows · Space · J/X · K/C · W/Up'), ('Pad', 'A jumps and confirms · Start pauses')],
  cues=[('A and D', 171, 'move_left / move_right'), ('J or X', 174, 'attack'), ('gamepad', 181, '_add_joy_button'),
        ('left stick', 190, '_add_joy_axis')],
  narration=("There's no input map in the project settings. The GameState autoload builds it at startup: A and D or "
             "the arrows, Space, J or X to slash, K or C to throw. Then the gamepad: A jumps and confirms, Start "
             "pauses, and the left stick runs."),
  take='extras', segments=[('play', 230, 140), ('play', 440, 250)],
  rnarr=("So the arrow keys run instead of A and D. Then a simulated pad, not a real controller: its left stick runs "
         "Gino into a hint, pad A closes it, and Start pauses, then resumes."),
  obs='Arrow keys run; synthetic pad stick runs; pad A closes a hint; Start pauses and resumes.'),
 dict(code='B25', result='B26', component='pause-restart', path='scripts/level.gd', a=749, b=761,
  title='One Line Too Late', size=24,
  notes=[('Pause', 'Esc / P / Start toggles'), ('Defect', 'line 761: get_viewport() is null')],
  cues=[('Pause toggles', 750, 'is_action_pressed("pause")'), ('Restart', 759, '"restart"'),
        ('reloads the level', 760, '_restart()'), ('null', 761, 'get_viewport()')],
  narration=("Here's the defect. Pause toggles the menu and marks the event handled. Restart does the same, but "
             "restart reloads the level first. By the next line, this node has left the tree, its viewport is null, "
             "and the call fails."),
  take='defeat', start=1666, end=1973,
  rnarr=("Escape, then R. On screen, the level simply restarts. In the log: script error, cannot call set input as "
         "handled on a null value, line seven sixty-one."),
  obs='R on the pause menu restarts the level; defeat-run.log records the SCRIPT ERROR at level.gd:761.'),
]

COMPONENTS = {
 'scenes': ('Six thin scenes; each level is one Node2D with level.gd and a level_id.',
            ['scenes/level_1.tscn', 'scenes/level_2.tscn', 'scenes/level_3.tscn', 'scenes/main_menu.tscn',
             'scenes/instructions.tscn', 'scenes/credits.tscn'], ['B02', 'B03', 'B04', 'B27']),
 'level-build': ('level.gd builds the grid, terrain, props, entities, camera, HUD and overlay from the ASCII maps in levels.gd.',
                 ['scripts/level.gd', 'scripts/levels.gd'], ['B02', 'B05', 'B06']),
 'player': ('player.gd: input, run, jump, coyote time, jump buffer and jump cut; the playtest-only autopilot hook.',
            ['scripts/player.gd'], ['B07', 'B08']),
 'combat': ('player.gd combo chain and HITS table; hit_flash.gdshader for the white flash.',
            ['scripts/player.gd', 'scripts/hit_flash.gdshader'], ['B09', 'B10', 'B11', 'B12']),
 'knife': ('knife.gd: substepped flight, enemy and rock checks, lifetime; pickup.gd daggers.',
           ['scripts/knife.gd', 'scripts/pickup.gd'], ['B13', 'B14']),
 'enemies': ('enemy.gd base (health, attacks as timed rectangles), walker.gd, bat.gd, plant.gd.',
             ['scripts/enemy.gd', 'scripts/walker.gd', 'scripts/bat.gd', 'scripts/plant.gd'], ['B15', 'B16', 'B17', 'B18']),
 'health': ('player.gd damage, heal and death; the heart HUD in level.gd.', ['scripts/player.gd', 'scripts/level.gd'],
            ['B19', 'B20']),
 'level-flow': ('level.gd door, level complete, game over; GameState campaign and save.',
                ['scripts/level.gd', 'scripts/game_state.gd'], ['B21', 'B22']),
 'input-map': ('GameState._configure_input builds every key and pad binding at startup.',
               ['scripts/game_state.gd'], ['B23', 'B24']),
 'pause-restart': ('_unhandled_input, _pause, _resume and _restart in level.gd; the line-761 defect.',
                   ['scripts/level.gd'], ['B25', 'B26']),
 'menus': ('main_menu.gd, instructions.gd and credits.gd: title screen, Continue, How to Play, sound button, credits roll.',
           ['scripts/main_menu.gd', 'scripts/instructions.gd', 'scripts/credits.gd'], ['B27']),
 'audio': ('audio.gd autoload: named sounds, three music loops, the sound toggle; bus layout.',
           ['scripts/audio.gd', 'default_bus_layout.tres'], ['B27']),
 'tools-and-tests': ('_tools: the level checker and route simulator, the asset synthesizer, a screenshot driver and the playtest.',
                     [], ['B27']),
 'config': ('project.godot (2 autoloads, 1280×720, canvas_items), export presets and README.',
            ['project.godot', 'export_presets.cfg', 'README.md'], ['B02', 'B27']),
 'art-assets': ('The Rocky World sprites, terrain, props, FX, UI images, fonts and synthesized audio, with import settings.',
                [], ['B27']),
}

GREETING_NARR = ("Hola, this is Liam, in for Bear. That's the kind of prompt Walker expects, reconstructed here, not a "
                 "transcript. This time we open the project itself: a piece of code, then the exact thing it does on "
                 "screen, in the real build.")
OUTPUT = ['Built: 6 thin scenes, 14 scripts and a shader, 2,620 lines.', 'Art from the Unity folder; levels and sound authored.']
BLUF_NARR = ("Gino: Knife Throw is built in code. Its six scene files are a few lines each, and twenty-six hundred lines "
             "of GDScript build every tile, enemy and menu at runtime, from text maps. So every piece of code we read "
             "has a result you can watch.")
BLUF_TEXT = ("Gino: Knife Throw\nis built from scenes.\nSix scene files, a few lines each,\nand 2,620 lines of GDScript\n"
             "that build every level.")
TREE_NARR = ("Open a level scene and there's one node. Run it for eight seconds, and level dot g d has built the rest: a "
             "background layer, a world holding the tile map, the rock colliders, sixty-one prop sprites, thirteen "
             "pickups, Gino and five enemies, a camera, and two canvas layers for the HUD and the menus. Two hundred "
             "nodes.")
REST_NARR = ("The rest of the project, in one pass. A main menu with Continue and a sound button, a How to Play page, "
             "and credits that roll and fade. An audio autoload with sounds and music loops, all synthesized by a "
             "Python tool. A level tool that checks every map and simulates the jumps. And a playtest that steers "
             "through a hook in the player script. The film's captures pressed the keys instead.")
VERDICT_NARR = ("Verdict. This is a project you can read top to bottom: thin scenes, levels as text, enemies in under a "
                "hundred lines each. Two defects: R on a menu logs a script error, one line too late, and level three's "
                "bridge stops a tile short. Its own test steers through a hook; the captures pressed keys. And nobody "
                "has played it yet.")
VERDICT_HEADING = 'Readable code, two defects'
VERDICT_LINES = ['Implemented: 6 thin scenes; level.gd builds each level from an ASCII map.',
                 'Good habits: knives substepped; attacks as timed boxes; walkers never leave a ledge.',
                 'Defects: R logs a SCRIPT ERROR at level.gd:761; level 3 bridge has a 16 px hole.',
                 'Not judged: fun, difficulty, fairness of the drops. 0 human playtests.']
HANDOFF_NARR = ("Your turn. Paste this into Claude in your own Godot project: Use Walker on my Godot project. Find one "
                "handler that changes the scene and then keeps running code. Predict what that code will touch after the "
                "node has left the tree. Then write a capture that triggers it with real input and checks the log, and only "
                "after that, propose the smallest fix. Liam, in for Bear.")
HANDOFF_COMMAND = ("Use Walker on my Godot project. Find one handler that changes the scene and then keeps running code. "
                   "Predict what that code will touch after the node has left the tree. Then write a capture that triggers "
                   "it with real input and checks the log, and only after that, propose the smallest fix.")
