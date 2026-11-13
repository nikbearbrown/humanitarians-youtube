SLUG = 'claude-liam-stage-runner-gamedev'
TITLE = 'Stage Runner: Inside the Godot Code'
ASK = ('Please use Walker to convert my game design document about a vertical shooter — fly a wisp up three '
       'ruined city streets, shoot the monster army marching down at you, and defeat the Cerberus at the city '
       'gate — into a playable Godot project.')
PROJ = 'Stage Runner @ d90fa19'

PAIRS = [
 dict(code='B03', result='B04', component='scenes', path='scenes/stage_1.tscn', a=1, b=7,
  title='The Whole Stage Scene', size=40,
  notes=[('Saved scene', 'one Node2D + game.gd, stage_id = 1'), ('Live at 8 s', '113 nodes, built in code')],
  cues=[('One Node2D', 5, 'the only node'), ('game dot g d', 6, 'the script'), ('stage I D', 7, 'stage_id = 1')],
  narration=("Here's the whole of stage one: seven lines. One Node2D, with game dot g d attached, and a single property, "
             "stage I D, set to one. Stages two and three are the same file with a different number. Everything else is "
             "built when the scene starts."),
  take='campaign', start=330, end=630,
  rnarr=("Those seven lines become this: the scrolling street, both side panels, the stage banner, the countdown, and "
         "the first monsters, all built by one script."),
  obs='Stage 1 loads fully built: scrolling street, side panels, STAGE 1 banner, countdown, first monsters.'),
 dict(code='B05', result='B06', component='stage-config', path='scripts/game.gd', a=19, b=33,
  title='A Stage Is a Table Row', size=20,
  notes=[('From Unity', 'interval 2.0 (Army.cs)'), ('Authored', 'goal, drop chance, army, scroll')],
  cues=[('scroll speed', 25, '"scroll": 70.0'), ('Unity\'s two seconds', 26, '"interval": 2.0'),
        ('the goal', 28, '"goal": 2000'), ('the army', 31, '"army": [...]')],
  narration=("And the number picks a row from this table. Stage one: the Ruined Street painting, a scroll speed of seventy, "
             "Unity's two seconds between monsters, shrinking toward one point three, the goal, a seven percent drop chance, "
             "and the army, five monster types."),
  take='campaign', start=412, end=660,
  rnarr=("That row, on screen: the street scrolling, five monster icons under Incoming, and reach two thousand points on "
         "the right."),
  obs='Stage 1 HUD shows five Incoming monster icons and "Reach 2000 points to clear the stage."'),
 dict(code='B07', result='B08', component='player', path='scripts/player.gd', a=95, b=102,
  title='Move, Focus, Clamp', size=24,
  notes=[('Speed', '5 Unity units × 72 px = 360 px/s'), ('Focus', 'FOCUS_FACTOR 0.5')],
  cues=[('reads the four', 95, 'Input.get_vector'), ('halves the speed', 98, 'FOCUS_FACTOR'), ('clamps', 101, 'clampf(…)')],
  narration=("Movement reads the four move actions as one vector, so diagonals aren't faster. Holding focus halves the "
             "speed. Then the position clamps to the street, not to the screen, which is where Unity clamped."),
  take='campaign', start=555, end=740,
  rnarr="Shift held: half speed, the hitbox dot appears, and the wisp stays inside the street.",
  obs='With Shift held the wisp slows and the white hitbox dot appears.'),
 dict(code='B09', result='B10', component='shooting', path='scripts/player.gd', a=122, b=131,
  title='One Shot Becomes Three', size=30,
  notes=[('Rate', 'FIRE_RATE 0.2 s, from Shooting.cs'), ('Spread', '−0.2, 0, +0.2 rad for 10 s')],
  cues=[('one angle', 123, '[0.0]'), ('spread time', 124, 'spread_time > 0.0'), ('rotated', 129, 'rotated(angle)')],
  narration=("A shot is a list of angles. Normally it's one angle, straight up. While spread time is above zero, it's three: "
             "minus point two, zero, and plus point two radians. Each bullet's velocity is straight up, rotated by its angle."),
  take='campaign', start=755, end=955,
  rnarr="A triple-shot pickup sets spread time to ten seconds, and every shot fans into three.",
  obs='After collecting a triple shot, each shot fires three bullets in a fan.'),
 dict(code='B11', result='B12', component='enemies', path='scripts/enemy.gd', a=96, b=108,
  title='Four Ways to Walk Down', size=20,
  notes=[('Unity', 'y += speed × deltaTime, one pattern'), ('Rebuild', 'fall, weave, hunt, hop')],
  cues=[('walks down', 96, 'position.y +='), ('Weave', 99, 'sin(…) * 70.0'), ('Hunt', 102, 'move_toward'),
        ('Hop', 105, 'squash')],
  narration=("Every monster walks down, like Unity's. Then the pattern adds one thing. Weave sways seventy pixels either way. "
             "Hunt drifts toward the player's column until it passes them. Hop only squashes the sprite as it walks."),
  take='campaign', start=1760, end=2005,
  rnarr=("Stage two mixes them: spiders and slimes swaying, scorpions steering toward the wisp, oozes squashing as they "
         "go."),
  obs='Stage 2 shows weaving, hunting and hopping monsters together.'),
 dict(code='B13', result='B14', component='drops', path='scripts/game.gd', a=511, b=516,
  title='A Heart Only When You Need One', size=34,
  notes=[('Roll', 'drop chance per kill: 7% / 6% / 14%'), ('Heart', 'only below 3 lives, 40%')],
  cues=[('a heart only if', 513, 'lives < MAX_LIVES'), ('forty percent', 513, 'randf() < 0.4'), ('Otherwise', 513, '"spread"')],
  narration=("When a kill rolls a drop, this decides what it is. It's a heart only if a life is missing, and then forty "
             "percent of the time. Otherwise it's a triple shot. At full health, a heart can never drop."),
  take='extras', start=1868, end=2052,
  rnarr="Two lives left here, so the roll can make a heart. The wisp collects it: plus one life.",
  obs='With 2 lives, a heart drops and is collected: +1 LIFE, three hearts.'),
 dict(code='B15', result='B16', component='lives', path='scripts/player.gd', a=152, b=164,
  title='Three Lives, Not One Touch', size=28,
  notes=[('Unity', 'first touch: game over'), ('Rebuild', '3 lives, then 1.6 s invulnerable')],
  cues=[('does nothing', 153, 'invulnerable > 0.0'), ('loses a life', 155, 'lives -= 1'),
        ('At zero', 158, 'lives <= 0'), ('Otherwise', 164, 'INVULNERABLE_TIME')],
  narration=("A hit does nothing while the player is invulnerable. Otherwise it loses a life and tells the stage. At zero, "
             "the wisp is hidden and the player stops detecting contacts. Otherwise, one point six seconds of "
             "invulnerability start."),
  take='defeat', start=185, end=400,
  rnarr="Each contact: a red flash, a heart goes dark, the wisp blinks. The third: it bursts and disappears.",
  obs='Three deliberate contacts: two lives lost with blinking, then the wisp bursts.'),
 dict(code='B17', result='B18', component='game-over', path='scripts/game.gd', a=550, b=558,
  title="Unity's Game Over, Kept", size=30,
  notes=[('Unity', 'SetActive(true); timeScale = 0'), ('Rebuild', 'menu visible; tree paused')],
  cues=[("Unity's idea", 551, 'MainChar comment'), ('score against the goal', 555, '"Score: %d     /%d"'),
        ('tree pauses', 557, 'paused = true')],
  narration=("Game over keeps Unity's idea, as the comment says: show the screen, and stop the game. The text is the score "
             "against the goal, or, in the boss stage, a line about the Cerberus. Then the menu shows and the whole tree "
             "pauses."),
  take='defeat', start=330, end=550,
  rnarr="Game over, with Unity's crying face: score zero out of two thousand, the street frozen. Try Again.",
  obs='GAME OVER menu with the crying face and "Score: 0 /2000"; Try Again restarts.'),
 dict(code='B19', result='B20', component='stage-flow', path='scripts/game.gd', a=579, b=591,
  title='Stage Clear Is One Tween', size=20,
  notes=[('Unity', 'LoadScene("FinishStageOne") or "ClearTheGame"'), ('Rebuild', 'banner, fly-off, then the scene')],
  cues=[('banner', 581, 'tween banner scale'), ('flies the wisp', 584, 'position:y → -80'),
        ('records the stage', 587, 'complete_stage'), ('loads', 591, 'go_to("stage_clear")')],
  narration=("Clearing a stage is one tween. It pops the banner, waits, flies the wisp off the top of the street, then "
             "records the stage's score and loads the next scene: the clear card, or after stage three, the credits. The "
             "comments name Unity's scenes."),
  take='campaign', start=1320, end=1520,
  rnarr="Stage clear at two thousand, the wisp flies away, and the clear card totals the stage.",
  obs='STAGE CLEAR! banner, the wisp flies off the top, then the Stage 1 Clear card.'),
 dict(code='B21', result='B22', component='boss', path='scripts/boss.gd', a=94, b=106,
  title='Four Attacks in a Loop', size=21,
  notes=[('Every', '1.3 s, or 0.95 s when enraged'), ('Summon', 'only if fewer than 4 enemies')],
  cues=[('fan', 97, '_fan(5 or 7)'), ('ring', 99, '_ring(12 or 16)'), ('summons', 102, 'summon.emit'),
        ('three-shot fan', 105, '_fan(3, …)')],
  narration=("The boss counts its attacks and takes the count modulo four. Zero and two fire an aimed fan, one fires a ring, "
             "and three summons two minions, unless the street already holds four monsters, in which case it fires a "
             "tight three-shot fan."),
  take='campaign', start=3225, end=3420,
  rnarr="Fan, ring, fan, and two minions drop in beside it.",
  obs='The Cerberus fires a red fan, an orange ring, another fan, then summons minions.'),
 dict(code='B23', result='B24', component='boss', path='scripts/boss.gd', a=138, b=150,
  title='Shielded, Then Enraged', size=20,
  notes=[('Shield', 'state "enter": hits absorbed'), ('Enrage', 'at MAX_HEALTH / 2 = 55')],
  cues=[('walking in', 140, 'state == "enter"'), ('loses health', 143, 'health - amount'),
        ('crosses half', 147, 'enraged()'), ('roars', 149, 'boss_roar')],
  narration=("Damage first checks the state. While it's walking in, the shot is absorbed: a spark, but no damage. After "
             "that, it loses health. The moment it crosses half, it tints red, roars, and attacks again almost at once."),
  take='campaign', segments=[('play', 3110, 75), ('play', 3735, 80)],
  rnarr="Shots spark off it on the way in. Later, at fifty-five health, it turns red.",
  obs='Shots are absorbed during the walk-in; at 55 HP the boss is tinted red and enraged.'),
 dict(code='B25', result='B26', component='input-map', path='scripts/game_state.gd', a=122, b=136,
  title='The Input Map Is Code', size=20,
  notes=[('Unity', 'Horizontal / Vertical axes + J'), ('Rebuild', 'keys, mouse and pad added at startup')],
  cues=[('W A S D and the arrows', 123, 'move_*'), ('J, Space and Z', 127, 'fire'), ('left mouse', 131, '_add_mouse'),
        ('gamepad', 133, '_add_joy_button')],
  narration=("There's no input map in the project settings. The GameState autoload builds it at startup: W A S D and the "
             "arrows, J, Space and Z to fire, the left mouse button too, then the gamepad: A to fire, the left bumper to "
             "focus, Start to pause."),
  take='extras', segments=[('play', 318, 60), ('play', 445, 60), ('play', 1095, 120)],
  rnarr="So arrows and Z work, the mouse button works, and so does a simulated gamepad.",
  obs='Arrows + Z, held left mouse, and synthetic pad stick + A all move and fire.'),
 dict(code='B27', result='B28', component='pause-restart', path='scripts/game.gd', a=595, b=606,
  title='One Line Too Late', size=26,
  notes=[('Pause', 'Esc / P / Start toggles'), ('Defect', 'line 606: get_viewport() is null')],
  cues=[('Pause toggles', 596, 'is_action_pressed("pause")'), ('restart', 604, '"restart"'),
        ('changes the scene', 605, '_restart()'), ('null', 606, 'get_viewport()')],
  narration=("Here's the defect. Pause toggles the menu and marks the event handled. Restart does the same, but restart "
             "changes the scene first. By the next line, this node has left the tree, its viewport is null, and the call "
             "fails."),
  take='extras', start=930, end=1240,
  rnarr=("Escape, then R. On screen, the stage simply restarts. In the log: script error, cannot call set input as "
         "handled on a null value, line six oh six."),
  obs='R on the pause menu restarts the stage; extras-run.log records the SCRIPT ERROR at game.gd:606.'),
 dict(code='B29', result='B30', component='credits', path='scripts/game_clear.gd', a=94, b=106,
  title="Unity's Credits Scroll", size=28,
  notes=[('Speed', '150 px/s, from Thanks.cs'), ('Stop', 'when the last line sits above the buttons')],
  cues=[('move up', 97, 'SCROLL_SPEED * delta'), ('where to stop', 98, 'stop_y'), ('fades in', 105, 'modulate:a')],
  narration=("The credits are Unity's Thanks script: move up at a hundred and fifty pixels a second. The rebuild computes "
             "where to stop from the credits' own height, then fades in Play Again and Main Menu."),
  take='campaign', start=4097, end=4460,
  rnarr=("The city is safe: final score, monsters, best score, the credits, and they stop. Main Menu, and the best score "
         "is saved."),
  obs='Credits scroll up over the restored city and stop; Main Menu is clicked.'),
]

COMPONENTS = {
 'scenes': ('Seven thin scenes; each stage is one Node2D with game.gd and a stage_id.',
            ['scenes/stage_1.tscn', 'scenes/stage_2.tscn', 'scenes/stage_3.tscn', 'scenes/main_menu.tscn',
             'scenes/instructions.tscn', 'scenes/stage_clear.tscn', 'scenes/game_clear.tscn'], ['B02', 'B03', 'B04', 'B31']),
 'stage-config': ('game.gd builds the background, world, HUD and overlay from the STAGES table.',
                  ['scripts/game.gd'], ['B02', 'B05', 'B06']),
 'player': ('player.gd: input vector, focus, clamp, contacts and the playtest-only autopilot hook.',
            ['scripts/player.gd'], ['B07', 'B08']),
 'shooting': ('player.gd _shoot and bullet.gd: fire rate, spread angles, one damage per bullet.',
              ['scripts/player.gd', 'scripts/bullet.gd'], ['B09', 'B10']),
 'enemies': ('enemy.gd TYPES and patterns, hit_flash.gdshader, effects.gd bursts and score popups.',
             ['scripts/enemy.gd', 'scripts/hit_flash.gdshader', 'scripts/effects.gd'], ['B11', 'B12']),
 'drops': ('_drop_pickup in game.gd and pickup.gd (heart or triple shot).',
           ['scripts/game.gd', 'scripts/pickup.gd'], ['B13', 'B14']),
 'lives': ('take_hit in player.gd and the mercy rule in game.gd.', ['scripts/player.gd', 'scripts/game.gd'], ['B15', 'B16']),
 'game-over': ('_show_game_over in game.gd: score text, menu, paused tree.', ['scripts/game.gd'], ['B17', 'B18']),
 'stage-flow': ('_stage_clear in game.gd, stage_clear.gd, and the campaign state in game_state.gd.',
                ['scripts/game.gd', 'scripts/stage_clear.gd', 'scripts/game_state.gd'], ['B19', 'B20']),
 'boss': ('boss.gd attack cycle, shield and enrage; enemy_bullet.gd fireballs.',
          ['scripts/boss.gd', 'scripts/enemy_bullet.gd'], ['B21', 'B22', 'B23', 'B24']),
 'input-map': ('GameState._configure_input builds every key, mouse and pad binding at startup.',
               ['scripts/game_state.gd'], ['B25', 'B26']),
 'pause-restart': ('_unhandled_input, _pause, _resume and _restart in game.gd; the line-606 defect.',
                   ['scripts/game.gd'], ['B27', 'B28']),
 'credits': ('game_clear.gd: Thanks.cs scroll, computed stop, Play Again and Main Menu.',
             ['scripts/game_clear.gd'], ['B29', 'B30']),
 'menus': ('main_menu.gd and instructions.gd: the title screen, best score, audio button and How to Play.',
           ['scripts/main_menu.gd', 'scripts/instructions.gd'], ['B31']),
 'audio': ('audio.gd autoload: 15 named sounds, 3 music loops, a pool of 20 voices, the audio toggle; bus layout.',
           ['scripts/audio.gd', 'default_bus_layout.tres'], ['B31']),
 'tools-and-tests': ('_tools: the asset synthesizer, a screenshot driver and the autopilot playtest.', [], ['B31']),
 'config': ('project.godot (2 autoloads, 1280×720, canvas_items), export presets and README.',
            ['project.godot', 'export_presets.cfg', 'README.md'], ['B02', 'B31']),
 'art-assets': ('Stage paintings, monster sprites, FX textures, UI images, fonts and audio files with their import settings.',
                [], ['B31']),
}

GREETING_NARR = ("Hola, this is Liam, in for Bear. That's the kind of prompt Walker expects, reconstructed here, not a "
                 "transcript. This time we open the project itself: a piece of code, then the exact thing it does on screen, "
                 "in the real build.")
OUTPUT = ['Built: 7 thin scenes, 14 scripts and a shader, 2,210 lines.', 'Art from the Unity folder; sound synthesized.']
BLUF_NARR = ("Stage Runner is built in code. Its seven scene files are a few lines each, and twenty-two hundred lines of "
             "GDScript build every street, monster and menu at runtime. So every piece of code we read has a result you "
             "can watch.")
BLUF_TEXT = ("Stage Runner\nis built from scenes.\nSeven scene files, a few lines each,\nand 2,210 lines of GDScript\n"
             "that build every street.")
TREE_NARR = ("Open a stage scene and there's one node. Run it for eight seconds, and game dot g d has built the rest: a "
             "background with two copies of the street painting, a world holding the player and the first monsters, a "
             "camera for screen shake, and two canvas layers, one for the HUD and one for the banner and menus. A hundred "
             "and thirteen nodes.")
TREE = None   # filled from tree_probe.txt by make_sheet.py
REST_NARR = ("The rest of the project, in one pass. A main menu with the best score and an audio button, and a How to Play "
             "page. An audio autoload with fifteen sounds and three music loops, all synthesized by a Python tool. And a "
             "playtest that clears all three stages, steering through a hook the player script exposes for it. The film's "
             "captures pressed the keys instead.")
VERDICT_NARR = ("Verdict. This is a small project you can read top to bottom: thin scenes, one stage script driven by a "
                "table, and a boss in under two hundred lines. One real defect: R on a menu logs a script error, one line "
                "too late. Its own test steers through a hook; the captures pressed keys. And nobody has played it yet.")
VERDICT_HEADING = 'Readable code, one defect'
VERDICT_LINES = ['Implemented: 7 thin scenes; game.gd builds each stage from the STAGES table.',
                 'Good habits: one damage per bullet; a mercy rule; hearts only when a life is missing.',
                 'Defect: R on the pause menu logs a SCRIPT ERROR at game.gd:606; restart still works.',
                 'Not judged: fun, difficulty, boss fairness. 0 human playtests.']
HANDOFF_NARR = ("Your turn. Paste this into Claude in your own Godot project: Use Walker on my Godot project. Find one "
                "handler that changes the scene and then keeps running code. Predict what that code will touch after the "
                "node has left the tree. Then write a capture that triggers it with real input and checks the log, and only "
                "after that, propose the smallest fix. Liam, in for Bear.")
HANDOFF_COMMAND = ("Use Walker on my Godot project. Find one handler that changes the scene and then keeps running code. "
                   "Predict what that code will touch after the node has left the tree. Then write a capture that triggers "
                   "it with real input and checks the log, and only after that, propose the smallest fix.")
