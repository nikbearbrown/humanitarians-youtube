SLUG = 'claude-liam-nightyard-gamedev'
TITLE = 'Night Yard: Inside the Godot Code'
ASK = ('Please use Walker to convert my game design document about a 2.5D brawler-platformer — a night shift in '
       'a container yard, three Y Bots to choose from, ledges, wall jumps, an axe and a hammer, and a Forewoman '
       'at the end — into a playable Godot project.')
PROJ = 'Night Yard @ 54ad5ab'

C, D, E = 'campaign', 'defeat', 'extras'

PAIRS = [
 dict(code='B03', result='B04', component='scenes', path='scenes/level_01.tscn', a=1, b=7,
  title='The Whole Level Scene', size=40,
  notes=[('Saved scene', 'one Node3D + level.gd, level_id = 1'), ('Live at 8 s', '385 nodes, built in code')],
  cues=[('One Node3D', 5, 'the only node'), ('level dot g d', 3, 'the script'), ('level I D', 7, 'level_id = 1')],
  narration=("Here's the whole of level one: seven lines. One Node3D, with level dot g d attached, and a single property, "
             "level I D, set to one. All six level scenes are the same file with a different number. Everything else "
             "is built when the scene starts."),
  take=C, start=700, end=900,
  rnarr=("Those seven lines become this: the yard, the containers and fences, the lights, a bot, the HUD, and the "
         "level banner."),
  obs='Level 1 loads fully built: yard backdrop, blocks and containers, lights, HUD, banner.'),
 dict(code='B05', result='B06', component='levels', path='scripts/levels.gd', a=41, b=50,
  title='A Level Is a Text Map', size=16,
  notes=[('Grid', 'each character is a 1 m cell'), ('Legend', 'o light · g bot · ^ spike plate · C checkpoint · X gate')],
  cues=[('A hash', 49, '# concrete'), ('an o', 46, 'o yard light'), ('a g', 48, 'g yard bot'), ('the caret', 48, '^ plate'),
        ('X is the exit', 48, 'X gate')],
  narration=("And the number picks this entry: a side view, one character per metre. A hash is concrete, an o is a yard "
             "light, a g is a yard bot, the caret is a spike plate, and X is the exit gate. The gap in the floor is a pit."),
  take=C, start=920, end=1250,
  rnarr="That map, played: the block by the hint, the lights on top, the ledge, and the first bot.",
  obs='The block, lights, ledge and first bot sit where the level 1 map puts them.'),
 dict(code='B07', result='B08', component='fighter', path='scripts/fighter.gd', a=254, b=262,
  title='Eight Flags from the Keyboard', size=24,
  notes=[('Player', 'flags read from Input every tick'), ('Bots', 'the same flags, set by ai.gd')],
  cues=[('Left and right', 255, 'move_left / move_right'), ('all eight', 257, 'set_input(...)'), ('double tap', 260, '_proc_double_tap')],
  narration=("The player's input lands here. Left and right, then all eight flags in one call: up, down, jump, attack, "
             "block and turbo. The bots fill the same eight flags from their brain. A double tap also turns on turbo, "
             "timed on the wall clock."),
  take=C, start=785, end=960,
  rnarr="So D walks, and Shift runs: here D is held, Shift goes on and off, and Space jumps onto the block.",
  obs='D held; Shift toggles walk and run; Space jumps onto the block.'),
 dict(code='B09', result='B10', component='fighter', path='scripts/fighter.gd', a=372, b=402,
  title='One Button, Many Attacks', size=15,
  notes=[('Order', 'axe · pickup · takedown · hammer · up · run'), ('Hammer', 'down + attack, 9 s cooldown')],
  cues=[('holding the axe', 374, 'if holding != null'), ('Behind an unaware', 392, '_takedown_victim()'), ('Down means the hammer', 396, 'move_down and _hammer_cd'), ('up means', 399, 'move_up')],
  narration=("Attack on the ground means whatever fits first. If you're holding the axe, swing or throw it. If you're on a "
             "weapon, pick it up. Behind an unaware bot, a takedown. Down means the hammer, if it's charged. And up means "
             "an uppercut, or a dragon punch when running."),
  take=E, start=790, end=1020,
  rnarr="In play: jab, cross, up and attack for the uppercut, K to block, then down and attack, and the hammer comes down.",
  obs='Jab, cross, uppercut, block and hammer from the key showcase.'),
 dict(code='B11', result='B12', component='fighter', path='scripts/fighter.gd', a=744, b=757,
  title='A Combo Is a Window', size=20,
  notes=[('Hit', 'damage only inside the hit window'), ('Chain', 'attack again → the next part at combo_at')],
  cues=[('hit window', 745, 'a["hit"]'), ('A throw lets go', 749, 'throw at "release"'), ('press attack again', 753, 'a.has("combo")'), ('next part', 757, '_start_attack(_queued_attack)')],
  narration=("Every attack checks for hits only inside its hit window, measured from the clip. A throw lets go of the axe "
             "at its release time. And if you press attack again after the hit starts, the next part of the combo is "
             "queued and plays at its own moment."),
  take=C, start=2440, end=2620,
  rnarr="So repeated presses chain: jab, cross, kick, on the bots at the foot of level two's shaft.",
  obs='Jab, cross and kick chain on the bots at the foot of the level 2 shaft.'),
 dict(code='B13', result='B14', component='fighter', path='scripts/fighter.gd', a=547, b=571,
  title='A Ledge Is Two Grid Checks', size=15,
  notes=[('Grab', 'solid corner with two free cells above'), ('Snap', 'no big jumps to the hang position')],
  cues=[('must be solid', 564, 'level.solid(cx, cy)'), ('two free cells', 564, 'not level.solid(cx, cy + 1)'), ('the ledge is grabbed', 569, '_grab(...)')],
  narration=("A ledge is found on the level grid. The cell in front at hand height must be solid, with two free cells "
             "above it, and the body mustn't have to snap far to the hang. Then the ledge is grabbed."),
  take=C, start=1120, end=1210,
  rnarr="Level one's first tall block, in play: the hands catch the corner, and the player climbs.",
  obs='The ledge on the level 1 block is grabbed and climbed.'),
 dict(code='B15', result='B16', component='fighter', path='scripts/fighter.gd', a=660, b=685,
  title='Slide Down, Kick Off', size=15,
  notes=[('Slide', 'fall capped at 2.2 m/s'), ('Kick off', 'turn away, jump at 4.8 m/s')],
  cues=[('caps the fall', 662, 'WALL_SLIDE_FALL'), ('checks for a ledge', 668, '_try_ledge_grab()'), ('When jump is pressed', 675, 'jump_pressed'), ('turns away', 678, '_set_facing(-facing)')],
  narration=("A wall slide caps the fall at two point two metres a second, and still checks for a ledge on the way. When "
             "jump is pressed, the fighter turns away from the wall and launches off it."),
  take=C, start=2690, end=2810,
  rnarr="Level two's shaft: the slide, the kick off, the other wall, and the grab at the top.",
  obs='Wall slide, wall jump and the grab at the top of the level 2 shaft.'),
 dict(code='B17', result='B18', component='weapons', path='scripts/fighter.gd', a=1068, b=1074,
  title='Throwing the Axe', size=26,
  notes=[('Release', 'out of the hand, 1.25 m up'), ('Flight', 'weapon.gd: straight, spinning')],
  cues=[('lets go', 1072, 'holding = null'), ('is counted', 1073, 'stats["throws"]'), ('is launched', 1074, 'w.throw(...)')],
  narration=("Throwing is short. The fighter lets go of the weapon, the throw is counted for the playtest, and the axe "
             "is launched from shoulder height in the direction the fighter faces."),
  take=C, start=3960, end=4060,
  rnarr="Level three: the axe picked up, run and attack, and it flies into the bot.",
  obs='The axe is picked up and thrown into a bot.'),
 dict(code='B19', result='B20', component='bots', path='scripts/ai.gd', a=149, b=161,
  title='Bots Have to Notice You', size=18,
  notes=[('In front', 'within 8 m'), ('Behind', 'only right next to it, or running close')],
  cues=[('in front of it', 157, 'in_front and absf(dx) < 8.0'), ('Behind its back', 156, 'heard'), ('Fighting nearby', 160, 'noise')],
  narration=("A bot notices you if you're in front of it, within eight metres. Behind its back, only if you're right next "
             "to it, or running close by. Fighting nearby is noise, and that wakes it too."),
  take=C, start=7230, end=7330,
  rnarr="Level four: a bot with its back turned. The script walks, it doesn't run, and the bot never looks round.",
  obs='The level 4 guard bot stays unaware as the player walks up behind it.'),
 dict(code='B21', result='B22', component='fighter', path='scripts/fighter.gd', a=1076, b=1087,
  title='The Takedown Test', size=18,
  notes=[('Where', 'behind, 0.2–1.3 m, same floor'), ('Who', 'unaware, idle or walking, not the boss')],
  cues=[('facing the same way', 1083, 'd.x * facing'), ('not noticed', 1084, 'not f.aware'), ('The boss is never', 1079, '"sophie"')],
  narration=("And this is the takedown test: a bot just ahead of you, facing the same way, so you're behind it, that has "
             "not noticed you, standing or walking on the same floor. The boss is never a target."),
  take=C, start=7300, end=7420,
  rnarr="So attack, and it's a takedown: the paired animation, and the bot is out.",
  obs='The takedown plays on the unaware bot.'),
 dict(code='B23', result='B24', component='traps', path='scripts/spike_trap.gd', a=60, b=84,
  title='A Plate With Four States', size=15,
  notes=[('States', 'ready · armed · fired · reloading'), ('Kill', 'whoever is on the plate after it fires')],
  cues=[('Ready', 63, '"ready"'), ('Then armed', 72, '"armed"'), ('it fires', 73, 'ARM_DELAY'), ('still on the plate', 79, '_on_plate(f)')],
  narration=("A spike plate is a small state machine. Ready, until a fighter stands on it. Then armed, and after the delay "
             "it fires. Anyone still on the plate is killed by the spikes. Then it reloads."),
  take=D, start=1560, end=1760,
  rnarr="A deliberate step onto the plate: armed, fired, and a K.O.",
  obs='The plate arms, fires and kills; the player respawns at the checkpoint.'),
 dict(code='B25', result='B26', component='level-flow', path='scripts/level.gd', a=845, b=866,
  title='Back to the Checkpoint', size=16,
  notes=[('K.O.', 'deaths counted, K.O. screen, 2.6 s'), ('Respawn', 'the last active checkpoint, full HP')],
  cues=[('counted', 846, 'deaths += 1'), ('two point six', 849, '_respawn_timer'), ('checkpoint', 857, 'c["active"]'),
        ('pushed back', 862, 'e.global_position.x')],
  narration=("When the player dies, the death is counted, the K.O. screen shows, and two point six seconds later the "
             "player respawns at the last active checkpoint. Bots too close to it are pushed back seven metres."),
  take=D, start=560, end=760,
  rnarr="Walking into level one's pit: a fall is a K.O., and with no checkpoint yet, it's back to the start.",
  obs='A fall into the pit is a K.O.; the player respawns at the start.'),
 dict(code='B27', result='B28', component='hud', path='scripts/options_panel.gd', a=52, b=55,
  title='A Hidden Panel Takes the Key', size=34,
  notes=[('Checks', 'its own visible, not is_visible_in_tree()'), ('Defect', 'after Options, pause stops pausing')],
  cues=[('checks its own visible', 53, 'if visible'), ('keeps taking the key', 54, 'set_input_as_handled()'), ('emitting', 55, 'closed.emit()')],
  narration=("Now the first defect. The options panel closes on the pause key, but it checks its own visible flag. Back in "
             "the pause menu hides its container, not the panel, so the hidden panel keeps taking the key, and emitting "
             "closed, which shows the pause panel without pausing."),
  take=D, start=1965, end=2265,
  rnarr="Options, Back, Resume, then Escape: the pause panel appears, but the game is still running behind it.",
  obs='After Options in the pause menu, Esc shows the pause panel without pausing the tree.'),
 dict(code='B29', result='B30', component='menus', path='scripts/character_select.gd', a=170, b=178,
  title='Arrow Keys Do Two Things', size=22,
  notes=[('Select', 'left and right change the Y Bot'), ('Defect', 'as ui_left / ui_right they also move the focus')],
  cues=[('left and right', 173, 'move_left / move_right'), ('select', 176, '_select(ORDER[i])')],
  narration=("And the second. At the character select, left and right pick the next Y Bot. But the arrow keys are also "
             "Godot's own focus keys, so they move the focus between Back and Play at the same time."),
  take=E, start=283, end=560,
  rnarr="Right, right, left: Green is chosen, but the focus is now on Back, so Enter returns to the menu without saving it.",
  obs='Green is chosen with the arrows; Enter presses Back and the choice is not saved.'),
]

COMPONENTS = {
 'scenes': ('Ten thin scenes; each level is one Node3D with level.gd and a level_id.',
            ['scenes/level_%02d.tscn' % i for i in range(1, 7)] + ['scenes/main_menu.tscn', 'scenes/instructions.tscn',
             'scenes/credits.tscn', 'scenes/character_select.tscn'], ['B02', 'B03', 'B04', 'B31']),
 'levels': ('levels.gd: the six ASCII maps, hints and legends; level.gd builds them, places the backdrop and runs the level.',
            ['scripts/levels.gd', 'scripts/level.gd'], ['B02', 'B05', 'B06']),
 'fighter': ('fighter.gd: one CharacterBody3D for the player and every bot: movement, jumps, ledges, walls, attacks, hits and deaths.',
             ['scripts/fighter.gd'], ['B07', 'B08', 'B09', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B21', 'B22']),
 'weapons': ('weapon.gd: the axe on the floor, in the hand, thrown and dropped; the hammer is spawned by fighter.gd.',
             ['scripts/weapon.gd', 'scripts/fighter.gd'], ['B17', 'B18']),
 'bots': ('ai.gd: the bots\' brain (and the playtest autopilot); nav.gd: the grid links it paths over.',
          ['scripts/ai.gd', 'scripts/nav.gd'], ['B19', 'B20']),
 'traps': ('spike_trap.gd: the plates.', ['scripts/spike_trap.gd'], ['B23', 'B24']),
 'level-flow': ('level.gd scoring, gate, checkpoints, death and respawn; game_state.gd campaign, input map and save.',
                ['scripts/level.gd', 'scripts/game_state.gd'], ['B25', 'B26']),
 'hud': ('hud.gd: HP, score, gate, hammer, boss bar, hints, K.O., pause, options and Level Clear; options_panel.gd.',
         ['scripts/hud.gd', 'scripts/options_panel.gd'], ['B27', 'B28']),
 'menus': ('main_menu.gd, character_select.gd, stage.gd (the select stage), instructions.gd and credits.gd.',
           ['scripts/main_menu.gd', 'scripts/character_select.gd', 'scripts/stage.gd', 'scripts/instructions.gd',
            'scripts/credits.gd'], ['B29', 'B30', 'B31']),
 'audio': ('audio.gd autoload: named sounds, loops and music; bus layout.',
           ['scripts/audio.gd', 'default_bus_layout.tres'], ['B31']),
 'kit': ('kit.gd autoload: characters, props, materials and hit effects.', ['scripts/kit.gd'], ['B31']),
 'tools-and-tests': ('_tools: asset converter, bone maps, import patch, animation baker, level drafting aid, icon, screenshots and the playtest.',
                     [], ['B31']),
 'config': ('project.godot (3 autoloads, Forward+, Jolt), export presets and README.',
            ['project.godot', 'export_presets.cfg', 'README.md'], ['B02', 'B31']),
 'art-assets': ('Y Bot, Amy and Sophie with their clips, the yard pack, props, textures, fonts, UI images and synthesized audio, with import settings.',
                [], ['B31']),
}

GREETING_NARR = ("Hola, this is Liam, in for Bear. That's the kind of prompt Walker expects, reconstructed here, not a "
                 "transcript. This time we open the project itself: a piece of code, then the exact thing it does on "
                 "screen, in the real build.")
OUTPUT = ['Built: 10 thin scenes, 17 scripts, 5,215 lines.', 'Art from the Unity folder; levels and sound authored.']
BLUF_NARR = ("Night Yard is built in code. Its six level scenes are seven lines each, and fifty-two hundred lines of "
             "GDScript build every block, bot and menu at runtime, from text maps. So every piece of code we read has "
             "a result you can watch.")
BLUF_TEXT = ("Night Yard\nis built from scenes.\nSix level scenes, seven lines each,\nand 5,215 lines of GDScript\n"
             "that build every level.")
TREE_NARR = ("Open a level scene and there's one node. Run it for eight seconds, and level dot g d has built the rest: an "
             "environment and a moonlight, blocks and containers, the yard pack behind the lane, the spike trap, the "
             "fighters, the HUD and the camera. Three hundred and eighty-five nodes.")
REST_NARR = ("The rest of the project, in one pass. A main menu, a character-select stage, a How to play page, and credits. "
             "An audio autoload with synthesized sounds and music. A kit autoload for the characters and props. Tools "
             "that convert and retarget the Unity art, and a playtest that wires the bot brain into the player. The "
             "film's captures pressed the keys instead.")
VERDICT_NARR = ("Verdict. This is a project you can read top to bottom: thin scenes, levels as text, one fighter class for "
                "everyone. Two real defects live in the menus: an options panel that keeps the pause key, and arrow keys "
                "that also move the focus. The game's own test never opened a menu, so it never saw them. And nobody has "
                "played it yet.")
VERDICT_HEADING = 'Readable code, two menu defects'
VERDICT_LINES = ['Implemented: 10 thin scenes; level.gd builds each level from an ASCII map.',
                 'Good habits: one fighter class, attacks measured from the clips, a grid-checked ledge.',
                 'Defects: options_panel.gd:53 keeps the pause key; arrows move the focus too.',
                 'Not judged: fun, difficulty, boss fairness. 0 human playtests.']
HANDOFF_NARR = ("Your turn. Paste this into Claude in your own Godot project: Use Walker on my Godot project. Find one key "
                "that two parts of my UI both listen to. Predict what happens when it's pressed. Then write a capture that "
                "presses it with real input and checks the result, and only after that, propose the smallest fix. "
                "Liam, in for Bear.")
HANDOFF_COMMAND = ("Use Walker on my Godot project. Find one key that two parts of my UI both listen to. Predict what "
                   "happens when it's pressed. Then write a capture that presses it with real input and checks the "
                   "result, and only after that, propose the smallest fix.")
