"""Builds beat_sheet.json + gamedev-evidence.json for claude-liam-basketball-gamedev
(godot-gamedev walker). Teaching contract: code-then-result-v1.

    python3 make_sheet.py author    # narration + shots
    python3 make_sheet.py finish    # after Kokoro: pad audio, cut result clips, cues
    python3 make_sheet.py ledger    # after Remotion: hash media, write gamedev-evidence.json

Every code panel is read from the game's own files by line number at build time.
Every result is real engine output of the same build (8f86cc8): a scripted-input
capture (sometimes a labelled zoom of one), never retimed.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

REEL = Path(__file__).resolve().parent
CAPS = REEL.parent / 'basketball-captures'
sys.path.insert(0, str(CAPS))
import reelkit as rk  # noqa: E402

GODOT = REEL.parents[1] / 'basketball-game-godot-completed'
SLUG = 'claude-liam-basketball-gamedev'
TITLE = 'Basketball Blaster: Inside the Godot Code'
ASK = ('Please use Walker to convert my game design document about Basketball Blaster: Fowl Play — '
       'Mr. Block, armed with a basketball gun and basketball grenades, collects every egg across three '
       'arenas while chickens pour out of pipes — into a playable Godot project.')
PROJ = 'Basketball Blaster @ 8f86cc8'


def lines(path, a, b):
    return '\n'.join((GODOT / path).read_text().splitlines()[a - 1:b])


TREE_ALL = [l.rstrip() for l in (CAPS / 'tree_probe.txt').read_text().splitlines()[1:] if l.strip()]
TREE = TREE_ALL[:9] + ['    … 12 platform bodies + tile sprites', '    RespawnGate (Sprite2D)',
                       '    @Node2D@61 (Node2D) script=spotlight.gd   × 3', '    @Node2D@78 (Node2D)   × 5 egg nests',
                       '    @Camera2D@109 (Camera2D)', '  @CanvasLayer@110 (CanvasLayer)   HUD, pause, finish card',
                       '  @CanvasLayer@136 (CanvasLayer)   fade']
FILES_TREE = ['res://',
              '  project.godot · export_presets.cfg · default_bus_layout.tres',
              '  scenes/   8 .tscn, 7–12 lines each',
              '  scripts/  14 .gd + hit_flash.gdshader · 2,408 lines',
              '  assets/audio/   14 .wav (synthesized for the port)',
              '  assets/enemy/   19 images (walk ×4, attack ×10, pipe, feather, splatter)',
              '  assets/player/  8 images (Mr. Block, gun, ball, grenade, jetpack, dust)',
              '  assets/world/   14 images (court wall, tiles, gate, nest, spotlight)',
              '  assets/fx/ 8 · assets/ui/ 7 · assets/fonts/ 3',
              '  builds/   macOS .app + Windows .exe (exports)',
              '  tests/    — none —']

ZOOM_HUD = (0, 1584, 1024, 576)

PAIRS = [
 dict(code='B03', result='B04', component='scenes', path='scenes/level_1.tscn', a=1, b=7,
  title='The Whole Arena Scene', size=40,
  notes=[('Saved scene', 'one Node2D + game.gd + level_id'), ('Arenas 2 and 3', 'same file, a different number')],
  cues=[('One Node2D', 5, 'the only node'), ('one exported number', 7, 'level_id = 1')],
  narration=("Here's the entire arena one scene: seven lines. One Node2D, game dot g d attached, and one exported "
             "number, level id, set to one. Arenas two and three are the same file with a different number. All "
             "the difference lives in a data table."),
  take='campaign', start=1150, end=1290,
  rnarr=("Those seven lines boot into this: backdrop, platforms, pipes, spotlights, nests, Mister Block and the "
         "HUD, all built by one script as the briefing fades out."),
  obs='Arena 1 appears fully built from the 7-line scene: backdrop, platforms, pipes, spotlights, nests, player, HUD.'),
 dict(code='B05', result='B06', component='level-data', path='scripts/game.gd', a=147, b=160,
  title='An Arena Is One Dictionary', size=24,
  notes=[('Arena 3', '44 tiles · 2.2 s · cap 18 · 4-hit chickens'), ('Platforms', '[column, row, width] in 64 px tiles')],
  cues=[('forty-four tiles', 152, 'width_tiles: 44'), ('two point two', 153, 'spawn_interval: 2.2'),
        ('four-hit', 155, 'chicken_health: 4'), ('sixteen platforms', 158, '16 one-way platforms'),
        ('seven eggs', 159, '7 nests')],
  narration=("That table is here. Arena three is one dictionary: forty-four tiles wide, a new chicken every two "
             "point two seconds per pipe, a cap of eighteen, four-hit chickens, four pipe columns, five spotlights, "
             "sixteen platforms as column, row and width, and seven eggs. Change a number, and the arena changes."),
  take='campaign', start=3977, end=4200,
  rnarr=("Arena three, built from that dictionary: four pipes, the navy tint, platforms up to row five, and "
         "chickens that take four hits."),
  obs='Arena 3 shows 4 pipes, the 38 % navy tint and a top platform row, matching the dictionary.'),
 dict(code='B07', result='B08', component='input', path='scripts/game_state.gd', a=71, b=84,
  title='Input Is Registered in Code', size=26,
  notes=[('InputMap', 'actions added at boot, not in project.godot'), ('Keys', 'physical keycodes, so layout-independent')],
  cues=[('every action', 72, 'move, jump, fire …'), ('both mouse buttons', 82, 'left fires, right throws')],
  narration=("Input is registered in code, not in the project settings. At boot, game state adds every action to "
             "Godot's InputMap: keys by physical position, both mouse buttons, and, a few lines further down, the "
             "joypad buttons and sticks. That's why one script can drive the keyboard, the mouse and a controller "
             "through the same actions."),
  take='defeat', start=170, end=380,
  rnarr=("Here are synthetic joypad events going through those same actions: the left stick walks, the right "
         "stick aims, the trigger fires, A jumps, and Start pauses and resumes."),
  obs='Joypad events drive move, aim, fire, jump and pause through the code-registered actions.'),
 dict(code='B09', result='B10', component='player', path='scripts/player.gd', a=211, b=225,
  title='Jump, Buffer, Coyote, Double', size=24,
  notes=[('Buffer', '0.12 s'), ('Coyote', '0.15 s (Unity had 0.5 s)'), ('Air jumps', 'one, restored on landing')],
  cues=[('Down plus jump', 213, 'S + Space on a platform'), ('buffered', 218, 'jump_buffer_time'),
        ('coyote time', 221, 'floor or coyote'), ('double jump', 223, 'the one air jump')],
  narration=("The jump handler. Down plus jump on a platform turns platform collisions off for a quarter second: "
             "that's the drop-through. Otherwise the press is buffered for twelve hundredths of a second. On the "
             "floor, or within coyote time, it jumps. In the air, it spends the one double jump."),
  take='campaign', start=1290, end=1395,
  rnarr="First press: a jump. Second press, in mid-air: the double jump, and he climbs again before gravity wins.",
  obs='Space jumps; a second Space in mid-air re-launches upward (asserted: velocity jumped by more than 200).'),
 dict(code='B11', result='B12', component='player', path='scripts/player.gd', a=241, b=249,
  title='The Jetpack Unity Never Wired Up', size=26,
  notes=[('Fuel', '1.6 s · 1 per second while held'), ('Rise cap', '430 px/s')],
  cues=[('Shift is held', 242, 'jetpack action + fuel'), ('burns fuel', 244, 'fuel -= delta'),
        ('pushes velocity', 245, 'capped at JETPACK_MAX_RISE'), ('resets time in air', 246, 'delays extra gravity')],
  narration=("The jetpack, which Unity declared and never used. While Shift is held and fuel remains, it burns "
             "fuel at one second per second and pushes velocity upward, capped at four hundred and thirty pixels a "
             "second. It also resets time in air, so the extra fall gravity waits."),
  take='campaign', start=1395, end=1480,
  rnarr="Shift held: the flame, the climb, and the blue fuel bar running down.",
  obs='Holding Shift lifts the player and drains the fuel bar (asserted: fuel below 1.0).'),
 dict(code='B13', result='B14', component='player', path='scripts/player.gd', a=261, b=270,
  title='Weapons Emit, the Arena Builds', size=26,
  notes=[('Fire', 'held · every 0.4 s (Unity 0.5 s)'), ('Grenade', 'fresh press · 0.8 s cooldown')],
  cues=[('Holding fire', 263, 'is_action_pressed'), ('fresh press', 267, 'is_action_just_pressed'),
        ('emits a signal', 266, 'shoot_requested.emit')],
  narration=("Weapons sit in one function. Holding fire spawns a ball whenever the cooldown hits zero, every four "
             "tenths of a second. The grenade needs a fresh press and has its own cooldown. Neither spawns anything "
             "itself: the player emits a signal, and the arena builds the projectile."),
  take='campaign', start=1480, end=1590,
  rnarr=("Held left click: a steady stream of basketballs toward the crosshair, each with a muzzle flash and a "
         "small recoil."),
  obs='Held left click fires basketballs toward the crosshair at a steady rate with muzzle flash and recoil.'),
 dict(code='B15', result='B16', component='grenade', path='scripts/grenade.gd', a=59, b=70,
  title='A Rigid Body With a Fuse', size=24,
  notes=[('Blinks', '3, spread over 3 s'), ('Early fuse', 'touching a chicken explodes it')],
  cues=[('adds time', 62, 'countdown += delta'), ('Three blinks', 64, 'blink before each third'),
        ('explodes', 70, 'explode() at 3 s')],
  narration=("The grenade is a rigid body with a fuse. Every physics frame it adds time to a countdown. Three "
             "blinks are spaced across three seconds, each a red light and a beep signal, and at three seconds it "
             "explodes. Touching a chicken explodes it early."),
  take='campaign', start=1590, end=1694,
  rnarr="Right-click: the grenade arcs out, bounces, blinks, and blows, and the screen shakes.",
  obs='Right-click lobs a grenade that bounces, blinks three times and explodes about 3 s later.'),
 dict(code='B17', result='B18', component='shader', path='scripts/hit_flash.gdshader', a=1, b=10,
  title='One Shader, Two Jobs', size=30,
  notes=[('tint', 'pipe colour, 8-colour palette'), ('flash', 'white for 0.1 s on a hit')],
  cues=[('A tint uniform', 4, 'multiplies the sprite'), ('A flash uniform', 5, 'mixes toward white'),
        ('mixes', 9, 'mix(base * tint, white, flash)')],
  narration=("One ten-line shader does two jobs. A tint uniform multiplies the sprite's colour, which is how a pipe "
             "paints its chicken one of eight palette colours. A flash uniform mixes toward white: the hit flash. The "
             "script sets flash to one, and a tween resets it a tenth of a second later."),
  take='campaign', start=1900, end=2130,
  rnarr=("Chickens in different tints from the same white sprite sheet, and every ball that lands flashes its "
         "target white for a tenth of a second."),
  obs='Chickens appear in several palette tints; hit chickens flash white briefly.'),
 dict(code='B19', result='B20', component='mega-kill', path='scripts/game.gd', a=460, b=479,
  title='Three Deaths, One Frame', size=22,
  notes=[('Window', 'until the next physics frame'), ('Source', 'Unity AudioManager · megaKillAmount = 3')],
  cues=[('adds a kill', 464, 'kills += 1'), ('defers a check', 468, 'call_deferred'),
        ('three or more', 473, 'MEGA_KILL_AMOUNT')],
  narration=("Each chicken death adds a kill and bumps a counter. The first death in a frame defers a check to the "
             "next physics frame. If three or more died by then, it's a mega kill: sound, floating text and shake. "
             "It's the same window Unity's audio manager used."),
  take='campaign', segments=[('play', 1740, 60), ('replay', 1780, 24, 4), ('play', 1800, 60)],
  rnarr=("One grenade, four deaths before the next physics frame: mega kill. And again, at a quarter of the "
         "speed, labelled as a replay."),
  obs='A grenade kills four chickens in one window: MEGA KILL! and the kill counter jumps 0 to 4.'),
 dict(code='B21', result='B22', component='damage', path='scripts/game.gd', a=481, b=497,
  title='Contact Is a Distance Check', size=22,
  notes=[('Range', '58 px, every physics frame'), ('Per life', '3 health · 1 s invulnerable')],
  cues=[('unless the player is invulnerable', 482, 'invulnerable_time'), ('measures the distance', 487, 'distance_to'),
        ('one health', 492, 'health -= 1'), ('a life is lost', 497, '_lose_life()')],
  narration=("Contact damage is a distance check, not a physics collision. Every frame, unless the player is "
             "invulnerable, the arena measures the distance to each live chicken. Under fifty-eight pixels, it's a "
             "hit: one health, a sound, a shake, a knockback. At zero health, a life is lost."),
  take='defeat', start=485, end=640,
  rnarr=("Walking into the flock: a hit and a knockback, another, and the third costs the life, followed by the "
         "fade and the respawn at the gate."),
  obs='Three contacts cost three health balls and a life; fade and respawn at the gate follow.'),
 dict(code='B23', result='B24', component='eggs', path='scripts/game.gd', a=549, b=562,
  title='Eggs Use the Same Idea', size=22,
  notes=[('Range', '62 px'), ('Win', 'eggs_collected reaches the arena total')],
  cues=[('walks backwards', 550, 'safe removal mid-loop'), ('closer than sixty-two', 552, 'EGG_PICKUP_RANGE'),
        ('the level completes', 560, '_level_complete()')],
  narration=("Eggs use the same idea. Each frame, every nest closer than sixty-two pixels is collected: a sparkle, "
             "plus-one-egg text, the counter. The loop walks backwards, so removing a nest mid-loop is safe. When the "
             "count reaches the arena's total, the level completes."),
  take='campaign', start=2620, end=2900,
  rnarr="Egg after egg on the route, the counter ticking, and the last one ends the arena: court cleared.",
  obs='Nests are collected with sparkle and +1 EGG; the fifth shows COURT CLEARED!'),
 dict(code='B25', result='B26', component='briefing', path='scripts/intro_briefing.gd', a=46, b=68,
  title='Where the Click Goes', size=20,
  notes=[('Advances on', 'ui_accept or any mouse press, in _unhandled_input'), ('Shade', 'ColorRect, mouse filter STOP by default')],
  cues=[('ui accept', 51, 'or InputEventMouseButton'), ('full-screen shade', 65, 'ColorRect.new()'),
        ('stops mouse events', 68, 'added over everything below')],
  narration=("Now a defect, in the code. The briefing advances on ui accept, or on any mouse button press, but only "
             "in unhandled input. A few lines below, build screen adds a full-screen shade ColorRect. A ColorRect "
             "stops mouse events by default, so the click is consumed as GUI input and never arrives."),
  take='campaign', start=440, end=640,
  rnarr=("And the consequence: two clicks, on and above the dialogue box, and nothing happens. Enter advances at "
         "once."),
  obs='Two clicks do not advance the briefing (asserted); Enter does.'),
 dict(code='B27', result='B28', component='hud', path='scripts/game.gd', a=715, b=722,
  title='A Bar That Grew', size=22,
  notes=[('Asked for', '80 × 14 px'), ('Measured at runtime', '80 × 34 px (bar_probe.txt)')],
  cues=[('sets the bar\'s size', 718, 'bar.size = bar_size'), ('show percentage off', 719, 'show_percentage = false')],
  narration=("And a second layout defect, in the HUD's bar helper. It sets the bar's size before it turns show "
             "percentage off. A probe of the running game measures both bars at thirty-four pixels tall, not "
             "fourteen. The likely cause is that order: the size is clamped to the taller minimum the percentage text "
             "still needed."),
  take='campaign', zoom=ZOOM_HUD, start=1395, end=1480,
  rnarr=("Zoomed into the real frame: the bars run over their own hint labels, RMB slash G, and SHIFT, while the "
         "fuel bar drains."),
  obs='Zoomed engine frames: the grenade and fuel bars cover the lower part of their hint labels.'),
]

COMPONENTS = {
 'scenes': ('Eight thin scene files; levels share game.gd and differ only by an exported level_id.',
            ['scenes/level_1.tscn', 'scenes/level_2.tscn', 'scenes/level_3.tscn'], ['B02', 'B03', 'B04']),
 'level-builder': ('game.gd builds the whole arena at runtime: layers, geometry, gate, spotlights, nests, pipes, player, camera and HUD.',
                   ['scripts/game.gd'], ['B02', 'B04']),
 'level-data': ('Arenas are dictionaries in _get_level_config: width, spawn rate, cap, chicken health, pipes, spotlights, platforms, eggs.',
                ['scripts/game.gd'], ['B05', 'B06']),
 'input': ('GameState registers every keyboard, mouse and joypad action into the InputMap at boot.',
           ['scripts/game_state.gd', 'project.godot'], ['B07', 'B08']),
 'player': ('player.gd: movement, jump buffer, coyote time, double jump, drop-through, jetpack, aiming and weapon signals.',
            ['scripts/player.gd'], ['B09', 'B10', 'B11', 'B12', 'B13', 'B14']),
 'projectiles': ('bullet.gd (Area2D ball) and grenade.gd (RigidBody2D with a 3-blink fuse).',
                 ['scripts/bullet.gd', 'scripts/grenade.gd'], ['B13', 'B14', 'B15', 'B16']),
 'shader': ('hit_flash.gdshader: one tint uniform for the palette colour, one flash uniform for the hit flash.',
            ['scripts/hit_flash.gdshader'], ['B17', 'B18']),
 'chickens-and-pipes': ('pipe.gd recolours itself and requests a chicken; chicken.gd walks, hops, flies, takes knockback and dies.',
                        ['scripts/pipe.gd', 'scripts/chicken.gd'], ['B17', 'B18', 'B29']),
 'mega-kill': ('_on_chicken_died and _resolve_death_window: three or more deaths before the next physics frame.',
               ['scripts/game.gd'], ['B19', 'B20']),
 'damage': ('_check_chicken_contacts and _player_hit: a 58 px distance check, health, lives and respawn.',
            ['scripts/game.gd'], ['B21', 'B22']),
 'eggs': ('_check_eggs: 62 px pickup, a backwards loop, and the win condition.', ['scripts/game.gd'], ['B23', 'B24']),
 'briefing': ('intro_briefing.gd: typed dialogue; its full-screen shade ColorRect swallows clicks (defect D-01).',
              ['scripts/intro_briefing.gd', 'scenes/intro.tscn'], ['B25', 'B26']),
 'hud': ('_build_ui and _make_bar: the HUD; bars sized before show_percentage is off measure 34 px tall (defect D-02).',
         ['scripts/game.gd'], ['B27', 'B28']),
 'menus-and-end-screens': ('main_menu.gd (Play, Continue, How to Play, Quit), instructions.gd, and end_screen.gd serving victory and defeat via an exported mode.',
                           ['scripts/main_menu.gd', 'scripts/instructions.gd', 'scripts/end_screen.gd', 'scenes/main_menu.tscn',
                            'scenes/instructions.tscn', 'scenes/victory.tscn', 'scenes/defeat.tscn'], ['B29']),
 'state-and-config': ('GameState autoload (campaign totals, theme, widgets) plus project, bus layout and export settings.',
                      ['scripts/game_state.gd', 'project.godot', 'default_bus_layout.tres', 'export_presets.cfg', 'README.md'],
                      ['B02', 'B29']),
 'audio': ('Audio autoload: 13 named sounds, 16 pooled voices, looping music; 14 synthesized .wav files.',
           ['scripts/audio.gd'], ['B29']),
 'effects': ('effects.gd: static helpers for feathers, splatter, ball hits, dust, explosions, sparkles and floating text; spotlight.gd swings the lamps.',
             ['scripts/effects.gd', 'scripts/spotlight.gd'], ['B20', 'B29']),
 'art-assets': ('Textures, sprite frames, fonts and sounds, reused from the Unity project or synthesized; six images and one font are never used.',
                [], ['B29']),
}


def bookends():
    head = [
     dict(id='B00', act='ASK', pattern='ClaudeComposerAsk',
      narration=("Hola, this is Liam, in for Bear. That's the kind of prompt Walker expects, reconstructed here, "
                 "not a transcript. This time we open the project itself: a piece of code, then the exact thing it "
                 "does on screen, in the real build."),
      props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · GAMEDEV', segment='Inside the Godot Code',
                 command=ASK, runningText='illustrative reconstruction — not the historical prompt',
                 output=['Built: 8 thin scenes, 14 GDScript files and 1 shader, 2,408 lines.',
                         'Art reused from the Unity project; no automated tests.'],
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B01', act='BLUF', pattern='BrutalistHesitantWriter', lead=0.8, tail=1.5,
      narration=("Basketball Blaster is built in code. Its eight scene files are a few lines each, and twenty-four "
                 "hundred lines of GDScript build everything else at runtime. So every piece of code we read has a "
                 "result you can watch."),
      props=dict(text=("Basketball Blaster\nis built from scenes.\nEight scene files, a few lines each,\n"
                       "and 2,408 lines of GDScript\nthat build everything else."),
                 triggerWords='from scenes', replacementWords='in code', fontSize=96,
                 lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
                 seed='basketball-gamedev-2026-10', ink='#3D3929', accent='#D97757', bg='#FAF9F5',
                 face='serif', align='center', brandLabel='@NikBearBrown')),
     dict(id='B02', act='BODY', pattern='GodotDevWorkbench',
      narration=("Open level one's scene file and there's one node. Run it, and game dot g d builds the rest: a World "
                 "node holding the backdrop, decals, actors, projectiles and effects; every platform as a static body; "
                 "three spotlights; the nests; a camera; and two canvas layers, one for the HUD and one for the fade. "
                 "Most are never named, so the live tree reads at-Sprite2D-at-twenty-two."),
      props=dict(mode='tree', title='Saved Scene vs. Live Tree', project=PROJ,
                 source='Live tree: printed from a running instance of res://scenes/level_1.tscn at 3 s, headless, '
                        'no input, on an isolated copy (tree_probe.gd).',
                 treeLabel='Remote (runtime) tree — probed', tree=TREE,
                 inspectorLabel='Source notes — not Inspector values',
                 notes=[{'label': 'Saved scene (level_1.tscn)', 'value': '1 node: Level1 + game.gd'},
                        {'label': 'Live at 3 s', 'value': '~100 nodes, all created by game.gd'},
                        {'label': 'Autoloads', 'value': 'GameState · Audio (16 voices + music)'}],
                 cues=[{'at': 2.0, 'line': 1, 'label': 'the only saved node'},
                       {'at': 6.0, 'line': 2, 'label': 'World, built in _ready'},
                       {'at': 11.0, 'line': 13, 'label': 'spotlights, nests, camera'},
                       {'at': 15.0, 'line': 15, 'label': 'HUD and fade layers'}])),
    ]
    tail = [
     dict(id='B29', act='BODY', pattern='GodotDevWorkbench',
      narration=("The rest of the project, in one pass. A main menu, How to Play, and one end-screen script that serves "
                 "both victory and defeat through an exported mode. An Audio autoload that loads thirteen named sounds "
                 "into sixteen pooled voices. A static effects library for feathers, splatter, dust and the explosion. "
                 "Fifty-six images and three fonts, mostly reused from the Unity project. Six of those images, and one "
                 "font, are never used. And there is no test folder at all."),
      props=dict(mode='tree', title='The Rest of the Project', project=PROJ,
                 source='FileSystem summary from a file listing of the project (builds/ and .godot/ noted, not taught)',
                 treeLabel='FileSystem — res://', tree=FILES_TREE,
                 inspectorLabel='Source notes — not Inspector values',
                 notes=[{'label': 'Unused images', 'value': 'banner.jpg, mr_block_portrait.png, color_palette.png, ground_dark/ledge.png, dust03.png'},
                        {'label': 'Unused font', 'value': 'gixel.ttf: preloaded as pixel_font, never read'},
                        {'label': 'Tests', 'value': 'none in the project'}],
                 cues=[{'at': 3.0, 'line': 2, 'label': 'menus and end screens'},
                       {'at': 9.0, 'line': 4, 'label': '14 synthesized sounds'},
                       {'at': 17.0, 'line': 6, 'label': 'reused Unity art'},
                       {'at': 24.0, 'line': 10, 'label': 'no tests'}])),
     dict(id='B30', act='VERDICT', pattern='ClaudeVerdictArtifact',
      narration=("Verdict. This is a project you can read top to bottom: thin scenes, data tables, signals between "
                 "player and arena, and one shader doing two jobs. The two defects I found are input plumbing and "
                 "layout: places where the logic is right and the screen isn't. There are no tests, and a person still "
                 "has to play it."),
      props=dict(artifactTitle='Verdict', artifactHeading='Readable code, two screen-level bugs', brandLabel='@NikBearBrown',
                 artifactLines=['Implemented: 8 thin scenes, 2,408 lines of GDScript, arenas as data tables.',
                                'Good habits: player and arena talk by signals; one shader for tint and flash.',
                                'Defects on screen: a shade eats briefing clicks; HUD bars draw over their labels.',
                                'Missing: automated tests. Not judged: fun, balance — 0 human playtests.'])),
     dict(id='B31', act='HANDOFF', pattern='ClaudeComposerAsk',
      narration=("Your turn. Paste this into Claude in your own Godot project: Use Walker on my Godot project. Pick one "
                 "UI control and predict what a mouse click does: which node receives the event, and which nodes could "
                 "swallow it first. Then write a capture that proves or disproves it with real input, and only after "
                 "that, propose the smallest code change. Make the prediction before you look. Liam, in for Bear."),
      props=dict(greeting='Your turn.', topic='WALKER · YOUR TURN', segment='Predict, Then Capture',
                 command=("Use Walker on my Godot project. Pick one UI control and predict what a mouse click does: which "
                          "node receives the event, and which nodes could swallow it first. Then write a capture that "
                          "proves or disproves it with real input, and only after that, propose the smallest code change."),
                 runningText='paste this into Claude…',
                 output=['Look for: a prediction written before the capture.',
                         'Look for: the smallest change, not a rewrite.'],
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B32', act='OUTRO', pattern='ClaudeTitleOutro', tail=1.0,
      narration=f'{TITLE}. At Nik Bear Brown.',
      props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
    ]
    return head, tail


CONTRAST_REG = [{'label': 'disclosure strip text', 'box': [0.05, 0.905, 0.58, 0.952]}]
CONTRAST_REASON = 'Gameplay beat: the frame is the real engine render (dark navy menus, pause and fade screens are game art), scaled to 90 % above a dark disclosure strip. Whole-frame sampling takes the strip as background and the game as ink. Our own essential text, the disclosure strip, is measured in its own region; the game pixels are evidence, not typography.'
QC_CLIP = {'full_bleed': True, 'full_bleed_reason': ('The engine frame (scaled to 3456x1944) runs to the top edge by '
           'design: real game pixels, not a title card. Our disclosure strip sits inside title-safe; the game HUD at the '
           'top of the frame is game UI.'),
           'contrast_regions': CONTRAST_REG, 'contrast_reason': CONTRAST_REASON}
QC_WRITER = {'sparse_by_design': True, 'sparse_reason': ('Hesitant writer: text is typed on screen over the '
             'narration, so mid-beat samples legitimately show a partial page. The finished text fills the safe '
             'area and holds for the last 1.5 s.')}


def all_beats():
    head, tail = bookends()
    beats = list(head)
    for p in PAIRS:
        code = lines(p['path'], p['a'], p['b'])
        beats.append(dict(id=p['code'], act='BODY', pattern='GodotDevWorkbench', narration=p['narration'],
                          props=dict(mode='code', title=p['title'], project=PROJ, path=f"res://{p['path']}",
                                     source=f"{p['path']}:{p['a']}-{p['b']} at 8f86cc8 · Godot editor reconstruction",
                                     code=code, startLine=p['a'], codeFontSize=p['size'],
                                     inspectorLabel='Source notes — not Inspector values',
                                     notes=[{'label': k, 'value': v} for k, v in p['notes']],
                                     output=[f"{p['path']} · lines {p['a']}–{p['b']}"]), pair=p))
        beats.append(dict(id=p['result'], act='BODY', take=p['take'], narration=p['rnarr'], pair=p, lead=0.3,
                          **({'segments': p['segments']} if 'segments' in p else {'start': p['start'], 'end': p['end']})))
    beats += tail
    return beats


def author():
    out = []
    for spec in all_beats():
        b = {'beat_id': spec['id'], 'act': spec['act'], 'narration_text': spec['narration'],
             'voice': 'am_onyx', 'engine': 'kokoro',
             'estimated_duration_s': round(len(spec['narration'].split()) / 3.3, 1)}
        if 'take' in spec:
            b['shot'] = {'type': 'SCREEN', 'source': 'own', 'treatment': 'none', 'capture': spec['take'],
                         'method': 'scripted-input', 'zoom': bool(spec['pair'].get('zoom')),
                         'type_note': "engine capture of the game's own UI; GATE T pixel checks exempt (see BUILD-LOG.md)",
                         'show': [{'at': 0.0, 'event': f"real gameplay, take '{spec['take']}', build 8f86cc8"}]}
            b['qc'] = QC_CLIP
        else:
            b['shot'] = {'type': 'GRAPHIC', 'source': 'remotion',
                         'remotion': {'pattern': spec['pattern'], 'props': dict(spec['props'])},
                         'show': [{'at': 0.0, 'event': spec['pattern']}]}
            if spec['pattern'] == 'BrutalistHesitantWriter':
                b['qc'] = QC_WRITER
        if spec['act'] == 'OUTRO':
            b['kind'] = 'outro_voice'
            b['tail_silence_s'] = 1.0
        if spec.get('lead'):
            b['lead_silence_s'] = spec['lead']
        out.append(b)
    sheet = {'metadata': {
        'slug': SLUG, 'title': TITLE, 'topic': 'WALKER · GODOT · GAMEDEV', 'skill': 'godot-gamedev', 'modifier': 'walker',
        'channel': 'claude-liam', 'brand': 'claude-liam', 'persona': 'Liam (in for Bear)', 'in_for_bear': True,
        'voice': 'am_onyx', 'voice_kokoro': 'am_onyx', 'engine': 'kokoro', 'palette': 'claude', 'register': 'Teardown',
        'fps': 30, 'width': 3840, 'height': 2160, 'aspect_ratio': '16:9', 'fit': 'crop', 'captions': False,
        'caption_policy': 'none', 'greeting_language': 'Spanish (Hola)',
        'teaching_contract': 'code-then-result-v1',
        'audience': "makers following the channel's Claude + Walker game workflows",
        'game_build': {'commit': None, 'snapshot_sha256': rk.BUILD_ID, 'engine': 'Godot 4.7.2.stable.official.ed1daf0bf'},
        'note': ('godot-gamedev walker film. Code panels are Godot editor reconstructions with verbatim source; each is '
                 'followed by real engine output of the same build. No game change, no paid calls, no upload.'),
        'tags': ['Walker', 'Godot 4', 'GDScript', 'game development', 'arena shooter', 'Claude', 'Kokoro'],
    }, 'beats': out}
    (REEL / 'beat_sheet.json').write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    print(f'authored {len(out)} beats')


def cue_list(narration, cues, lead, dur):
    res = []
    for phrase, line, label in cues:
        pos = narration.find(phrase)
        if pos < 0:
            raise SystemExit(f'cue phrase not found: {phrase!r}')
        res.append({'at': round(lead + dur * pos / len(narration), 2), 'line': line, 'label': label})
    return sorted(res, key=lambda c: c['at'])


def finish():
    sheet_path = REEL / 'beat_sheet.json'
    sheet = json.loads(sheet_path.read_text())
    specs = {s['id']: s for s in all_beats()}
    for d in ('audio', 'media', 'capture', 'evidence'):
        (REEL / d).mkdir(exist_ok=True)
    for b in sheet['beats']:
        bid, spec = b['beat_id'], specs[b['beat_id']]
        mp3 = REEL / f'mp3/beat-{bid}.mp3'
        speech = rk.probe_duration(mp3)
        lead = spec.get('lead', 0.0)
        b['kokoro_audio_file'] = f'mp3/beat-{bid}.mp3'
        b['kokoro_duration_s'] = round(speech, 3)
        if 'take' in spec:
            take, need = spec['take'], rk.frames_for(lead + speech + 0.5)
            if spec['pair'].get('zoom'):
                n = spec['end'] - spec['start']
                info = rk.cut_zoom(take, spec['start'], n, spec['pair']['zoom'], REEL / f'media/{bid}.mp4',
                                   hold=max(0, need - n))
            else:
                if 'segments' in spec:
                    segs = list(spec['segments'])
                    have = sum(s[2] * (s[3] if s[0] == 'replay' else 1) for s in segs)
                    k, s0, n = segs[-1][:3]
                    grow = max(0, min(rk.take_frames(take) - (s0 + n), need - have))
                    segs[-1] = (k, s0, n + grow)
                    if need - have - grow > 0:
                        segs.append(('hold', need - have - grow))
                else:
                    n = spec['end'] - spec['start']
                    segs = [('play', spec['start'], n)] + ([('hold', need - n)] if need > n else [])
                info = rk.cut_segments(take, segs, REEL / f'media/{bid}.mp4')
            total = info['frames'] / rk.FPS
            held = sum(s['output_frames'] for s in info['segments'] if s['kind'] == 'hold')
            if held:
                print(f'{bid}: {held} held frames')
            b['shot']['clip'] = info
            b['shot']['evidence_media'] = f'media/{bid}.mp4'
        else:
            total = rk.frames_for(lead + speech + spec.get('tail', 0.0) + (0.4 if b['act'] == 'VERDICT' else 0.3)) / rk.FPS
            props = b['shot']['remotion']['props']
            props['durationSeconds'] = total
            if 'pair' in spec:
                props['cues'] = cue_list(spec['narration'], spec['pair']['cues'], lead, speech)
        rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
        b['audio_file'] = f'audio/beat-{bid}.wav'
        b['actual_duration_s'] = total
    for take in sorted({s['take'] for s in specs.values() if 'take' in s}):
        for suffix in ('.mp4', '-inputs.jsonl'):
            shutil.copy2(rk.TAKES / f'{take}{suffix}', REEL / f'capture/{take}{suffix}')
    for name in ('tree_probe.txt', 'tree_probe.gd', 'bar_probe.txt', 'bar_probe.gd'):
        shutil.copy2(CAPS / name, REEL / 'evidence' / name)
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    for b in sheet['beats']:
        print(f"{b['beat_id']:4} {b['act']:8} {b['actual_duration_s']:7.2f}s  speech {b['kokoro_duration_s']:6.2f}s")
    print('total', round(sum(b['actual_duration_s'] for b in sheet['beats']), 1), 's')


ROLE_BY_DIR = {'scripts': 'runtime script', 'scenes': 'scene', 'assets/audio': 'audio asset or import settings',
               'assets/fonts': 'font asset or import settings'}
EXCLUSION_REASON = 'exported build artefact (macOS app / Windows exe), not source; boot-tested separately (export-boot.log)'


def ledger():
    sheet = json.loads((REEL / 'beat_sheet.json').read_text())
    inv = sorted(p.relative_to(GODOT).as_posix() for p in GODOT.rglob('*')
                 if p.is_file() and not any(x in ('.godot', '.git') for x in p.relative_to(GODOT).parts)
                 and p.suffix != '.uid')
    comp_of = {}
    for cid, (_, files, _) in COMPONENTS.items():
        for f in files:
            comp_of.setdefault(f, []).append(cid)
    assets = [p for p in inv if p.startswith('assets/')]
    COMPONENTS['art-assets'] = (COMPONENTS['art-assets'][0], assets, COMPONENTS['art-assets'][2])
    for p in assets:
        comp_of.setdefault(p, []).append('art-assets')
    files, exclusions = [], []
    for path in inv:
        if path.startswith('builds/'):
            exclusions.append({'path': path, 'reason': EXCLUSION_REASON})
            continue
        if path not in comp_of:
            raise SystemExit(f'unassociated file: {path}')
        role = next((v for k, v in ROLE_BY_DIR.items() if path.startswith(k)), None)
        if role is None:
            role = 'art asset or import settings' if path.startswith('assets/') else 'project configuration'
        files.append({'path': path, 'sha256': hashlib.sha256((GODOT / path).read_bytes()).hexdigest(),
                      'role': role, 'component_ids': comp_of[path]})
    pairs = []
    for p in PAIRS:
        media = REEL / f"media/{p['result']}.mp4"
        pairs.append({'code_beat': p['code'], 'result_beat': p['result'], 'observation': p['obs'],
                      'media': {'path': f"media/{p['result']}.mp4", 'sha256': rk.sha256(media)}})
    data = {'schema_version': 1, 'teaching_contract': 'code-then-result-v1',
            'game': {'path': '../../basketball-game-godot-completed', 'build_id': rk.BUILD_ID},
            'files': files,
            'components': [{'id': cid, 'explanation': e, 'beat_ids': beats, 'files': fl}
                           for cid, (e, fl, beats) in COMPONENTS.items()],
            'excerpts': [{'beat_id': p['code'], 'path': p['path'], 'start_line': p['a'], 'end_line': p['b'],
                          'text': lines(p['path'], p['a'], p['b'])} for p in PAIRS],
            'exclusions': exclusions,
            'code_result_pairs': pairs}
    (REEL / 'gamedev-evidence.json').write_text(json.dumps(data, indent=1, ensure_ascii=False) + '\n')
    print(f'ledger: {len(files)} files, {len(exclusions)} exclusions, {len(pairs)} pairs')


if __name__ == '__main__':
    {'author': author, 'finish': finish, 'ledger': ledger}[sys.argv[1]]()
