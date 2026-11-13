"""Builds beat_sheet.json + gamedev-evidence.json for claude-liam-walker-towerdefense-gamedev
(godot-gamedev walker). Teaching contract: code-then-result-v1.

    python3 make_sheet.py author    # narration + shots
    python3 make_sheet.py finish    # after Kokoro: pad audio, cut result clips, cues
    python3 make_sheet.py ledger    # after Remotion: hash media, write gamedev-evidence.json

Every code panel is read from the game's own files by line number at build time.
Every result is real engine output of the same build (caf082c): a scripted-input
capture, or a recorded test receipt. Nothing is retimed.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

REEL = Path(__file__).resolve().parent
CAPS = REEL.parent / 'walker-towerdefense-captures'
sys.path.insert(0, str(CAPS))
import reelkit as rk  # noqa: E402

GAME_PKG = REEL.parents[1] / 'Walker-Godot-TowerDefense'
GODOT = GAME_PKG / 'godot'
SLUG = 'claude-liam-walker-towerdefense-gamedev'
TITLE = 'Walker Tower Defense: Inside the Godot Code'
ASK = ('Please use Walker to convert my game design document about a four-element tower defense — '
       'Fire, Ice, Poison and Storm towers on a 12-by-8 grid, where every tower you build reshapes '
       'the monsters\' route — into a playable Godot project.')
PROJ = 'walker-towerdefense @ caf082c'


def lines(path, a, b):
    return '\n'.join((GODOT / path).read_text().splitlines()[a - 1:b])


TREE = [l.rstrip() for l in (CAPS / 'tree_probe.txt').read_text().splitlines()[1:] if l.strip()]

# (code beat, result beat) pairs.
PAIRS = [
 dict(code='B03', result='B04', component='scene-root', path='game/main.tscn', a=1, b=6,
  title='The Whole Scene File', size=34,
  notes=[('Saved scene', 'one Node2D + session.gd'), ('Everything else', 'constructed by session.gd at runtime')],
  cues=[('One Node2D', 5, 'the only node in the saved scene'), ('one script', 6, 'session.gd does the rest')],
  narration=("Here's the entire scene file. One Node2D, one script attached: session dot g d. There's no "
             "Grid node to click on in the editor, no HUD scene, no tower prefab. Everything is built in "
             "code when the game starts, which keeps the whole project as diffable text."),
  take='opening', start=0, end=290,
  rnarr=("Those six lines boot into this: board, HUD and menu card, all built and drawn by one script. "
         "Click start, and the same script owns the run."),
  obs='Boot of the real main scene: board, HUD and menu card appear; START begins a run.'),
 dict(code='B05', result='B06', component='input', path='game/session.gd', a=460, b=470,
  title='Input Is Registered in Code', size=24,
  notes=[('InputMap', 'actions added at startup, not in project.godot'), ('Once missing', 'dropped in a rewrite; 56 checks stayed green')],
  cues=[('adds every action', 463, 'for each action in the table'), ('InputMap at startup', 466, 'registered one by one')],
  narration=("Input is registered in code too. Setup-input adds every action — confirm, pause, restart, next "
             "wave, the number keys — to Godot's InputMap at startup. This function once vanished in a "
             "rewrite. Fifty-six tests stayed green, because none of them pressed a key, and the whole keyboard "
             "was dead."),
  take='opening', start=380, end=780,
  rnarr=("Now real key events through that map: two picks Ice, a right-click cancels, two again, four asks "
         "for Storm and is refused, Escape backs out. Every press goes through unhandled-input, the path the "
         "old tests never touched."),
  obs='Keys 2, 4 and Esc and a right-click, delivered as input events, drive build mode and refusals.'),
 dict(code='B07', result='B08', component='grid-and-routing', path='features/grid/grid.gd', a=152, b=162,
  title='The Rule the Original Lacked', size=26,
  notes=[('Unity source', 'no route check; stranded monsters teleported'), ('Level data', 'level_01.json + tile_kinds.gd decide walkable')],
  cues=[('pretends', 154, 'the new cell counts as blocked'), ('from the spawn', 155, 'spawn must reach the exit'),
        ("every monster's", 160, 'and every live monster')],
  narration=("This is the rule the Unity original didn't have. The level's JSON and a tile-kind table decide "
             "what's walkable. Before a tower is placed, the grid pretends it's already there, then runs A-star "
             "from the spawn, and from every monster's current cell, to the exit. Any failure, and the "
             "placement is refused."),
  take='maze', start=395, end=767,
  rnarr=("Here it is refusing: a tower beside the spawn is fine; the one that would seal the corner is not — "
         "would block the path. Then a tower dropped onto the road passes the same check, and the route tint "
         "bends round it."),
  obs='Seal of the spawn corner refused with "Would block the path"; a tower on the road accepted and the route changes.'),
 dict(code='B09', result='B10', component='simulation-clock', path='game/session.gd', a=21, b=30,
  title='The Pacing Fix Is a Clock', size=25,
  notes=[('Before', '44 px/s monsters; wave 1 took 26 s'), ('After', 'same numbers, 3x clock; 1x/2x/3x on top')],
  cues=[('one unit', 22, 'a tile was one Unity unit'), ('three times faster', 29, 'BASE_SIM_SPEED'), ('one, two or three', 30, 'player multiplier')],
  narration=("The pacing fix is two constants. The Unity timings assumed a tile was one unit; this board draws a "
             "tile at sixty-four pixels, and monsters crawled at forty-four pixels a second. Instead of "
             "rewriting every recovered number, the whole simulation clock runs three times faster, and the "
             "player can multiply that by one, two or three."),
  take='opening', start=885, end=1256,
  rnarr=("Watch the speed readout: the button takes it to two, F to three, and back to one. The rules don't "
         "change, only the clock — every duration scales together, so a tower still lands the same damage per "
         "pass."),
  obs='SPEED button to 2x, F to 3x, F back to 1x, during waves 2 and 3.'),
 dict(code='B11', result='B12', component='monsters-and-damage', path='features/monsters/monster.gd', a=112, b=120,
  title='Every Hit Lands Here', size=30,
  notes=[('Inputs', 'one float — no element, no attacker'), ('hit_flash', '0.14 s white wash, added in b67653a')],
  cues=[('One number', 112, 'take_damage(amount)'), ('Hit-flash', 115, 'presentation only'), ('compounding', 116, 'health from the wave ramp')],
  narration=("Every hit in the game lands here. One number in, subtracted from health: no element, no "
             "resistance, no colour check. That's why the elemental tower defense has no elemental damage. "
             "Hit-flash is set first, a brief wash toward white. The health it subtracts from comes from the wave "
             "spawner's compounding ramp."),
  take='opening', start=1797, end=1984,
  rnarr="Each hit lands in that function: a white flash, a shorter bar, and at zero, four gold.",
  obs='Wave 1 against an upgraded Fire tower: hits flash white, bars drop, kills raise gold from 0 to 8.'),
 dict(code='B13', result='B14', component='monsters-and-damage', path='features/monsters/monster.gd', a=74, b=84,
  title='Poison Goes Through the Same Door', size=26,
  notes=[('Tick', 'every 0.1 s of simulated time'), ('Side effect', 'take_damage resets hit_flash to 0.14 s')],
  cues=[('tenth of a second', 82, 'a tick every poison_tick'), ('calls take-damage', 84, 'each tick is a hit')],
  narration=("Poison runs through the same door. Every tenth of a second of simulated time, a poison tick calls "
             "take-damage, and take-damage resets hit-flash. The flash never gets the chance to fade. So the "
             "green poison tint, drawn first, is washed toward white for as long as the poison lasts."),
  take='poison', start=445, end=800,
  rnarr=("And there it is in wave two: the poisoned monster at the front stays pale the whole time. Two "
         "systems, each reasonable alone, combine into a status a player may not read as poison."),
  obs='The poisoned lead monster of wave 2 stays pale white rather than green.'),
 dict(code='B15', result='B16', component='projectiles', path='features/projectiles/projectile.gd', a=129, b=139,
  title='How Storm Chooses a Neighbour', size=24,
  notes=[('Coin flip', 'may re-pick the previous target (Unity quirk, kept)'), ('Beam life', '0.4 s then 0.2 s per hop, on the 3x clock')],
  cues=[('nearest live monster', 136, 'closest within reach'), ('flips a coin', 129, 'exclude previous, or not'), ('three-times clock', 132, 'every live monster considered')],
  narration=("Storm's chain picks the nearest live monster within reach of its current target, and flips a coin "
             "on whether to skip the one it just hit, so a chain can bounce back and forth. That quirk is from the "
             "Unity source, kept on purpose. The beam's lifetimes, four-tenths and two-tenths of a second, run on "
             "the three-times clock."),
  take='storm', segments=[('play', 60, 144), ('replay', 173, 6, 8), ('play', 204, 30)],
  rnarr=("Real speed first: the beam hits, hops to the neighbour, and it's gone — six frames. Again at an "
         "eighth of the speed. The code does exactly what it says; whether a person sees a chain is a "
         "different question."),
  obs='The beam is visible for frames 173-178 (0.2 s) at real speed, then replayed at 1/8 speed, labelled.'),
 dict(code='B17', result='B18', component='debug-overlay', path='game/session.gd', a=596, b=600,
  title='Drawn Under Its Own Child', size=26,
  notes=[('Overlay', 'session._draw(), x 8 to 338'), ('Board', 'Grid child added at session.gd:92, origin x 96')],
  cues=[('x eight', 599, 'the overlay rectangle'), ('children draw after', 599, 'the Grid child paints next')],
  narration=("The F1 overlay is drawn by the session itself, in its own draw function, at x eight to three "
             "thirty-eight. But the grid is a child of the session, added in ready, starting at x ninety-six — and "
             "in Godot, children draw after their parent. So the board is painted straight over most of the overlay."),
  take='poison', start=160, end=445,
  rnarr=("F1 on: the panel appears, and the board covers everything past its first few characters, including "
         "the per-tower damage numbers it was built to show."),
  obs='The F1 overlay is cut off at the board edge; only its left 88 logical px are visible.'),
 dict(code='B19', result='B20', component='towers-and-art', path='features/towers/tower.gd', a=135, b=142,
  title='All the Art Is Code', size=27,
  notes=[('Shared routine', 'placed tower, build-bar miniature (hud.gd), ghost'), ('Stats', 'tower_tuning.gd DATA table')],
  cues=[('six-point polygon', 136, 'Storm bolt'), ('chevron', 141, 'upgrade marker')],
  narration=("All the art is code. This is the end of draw-tower-body: Storm's bolt is a six-point polygon, and the "
             "upgrade marker is a three-point chevron in the same yellow — shape, not just colour. The same "
             "function draws the placed tower, the build-bar miniature and the placement ghost, and the stats "
             "behind them live in one tuning table."),
  take='opening', start=1500, end=1800,
  rnarr=("Build, select, upgrade: the chevron appears under the tower, and the panel reads maxed. The bar's "
         "miniatures and the ghost came from that same routine."),
  obs='An upgraded Fire tower gains the chevron; the panel reads SELL 34 and MAXED.'),
 dict(code='B21', result='B22', component='tests', path='tests/test_keyboard.gd', a=33, b=41,
  title='A Test That Presses Keys', size=30,
  notes=[('Path', 'Input.parse_input_event -> _unhandled_input'), ('Other suites', 'call session methods directly')],
  cues=[('real key events', 36, 'InputEventKey'), ('parse-input-event', 39, 'the player\'s path')],
  narration=("Tests get their own look. This is the keyboard suite's core: it builds real key events and pushes "
             "them through Input dot parse-input-event, so they travel the path a player's do. That's the "
             "difference from the other suites, which call session methods directly: fast, deterministic, and "
             "blind to input."),
  receipt=True,
  rnarr=("These are the recorded receipts, not a demo. With the one-line fix reverted, eight of nine keyboard "
         "checks fail; with it restored, nine of nine pass. What a passing suite still can't tell you is whether "
         "a refusal can be read in three-tenths of a second, or whether poison looks like poison. That takes "
         "footage, and a person."),
  obs='Receipt keyboard-1790012997.43825.json: 8 of 9 FAIL with the fix reverted; keyboard-1790606725.01996.json: 9 of 9 PASS.'),
 dict(code='B23', result='B24', component='level-load', path='game/session.gd', a=91, b=96,
  title='A Comment Nobody Tested', size=30,
  notes=[('Promise', '"the session stays out of PLAYING"'), ('HUD', 'CanvasLayer — drawn above the error panel')],
  cues=[('fails to load', 93, 'load_level returns false'), ('stays out of playing', 95, 'the promise')],
  narration=("One more comment worth testing. If the level file fails to load, this branch keeps the state at "
             "menu, and the comment promises the session stays out of playing. But nothing stops Enter from "
             "starting a session later, and the menu-card HUD is drawn on a canvas layer above the error panel."),
  take='broken', start=0, end=389, staged=True,
  rnarr=("Staged, in a copy with the level's exit removed: the error panel sits under the menu card. Enter sets "
         "playing, Space even starts wave one, but the HUD never redraws. The comment was a promise nothing "
         "checked."),
  obs='With level_01.json missing "exit": the error panel is covered by the menu card; Enter sets PLAYING and Space starts wave 1 behind a frozen HUD.'),
]

COMPONENTS = {
 'scene-root': ('One six-line scene; session.gd constructs and owns the board, HUD and entities; project settings.', ['game/main.tscn', 'game/session.gd', 'project.godot'], ['B02', 'B03', 'B04']),
 'input': ('Runtime InputMap registration and _unhandled_input routing.', ['game/session.gd'], ['B05', 'B06']),
 'grid-and-routing': ('Level JSON, tile rules, 4-neighbour A*, and the no-seal placement rule.', ['features/grid/grid.gd', 'features/grid/astar.gd', 'features/grid/tile_kinds.gd', 'levels/level_01.json'], ['B07', 'B08']),
 'simulation-clock': ('One fixed-step world loop running at 3x the source rate, times a player 1x/2x/3x.', ['game/session.gd'], ['B09', 'B10']),
 'monsters-and-damage': ('Monster movement, flat damage, status timers and drawing; recovered monster stats.', ['features/monsters/monster.gd', 'features/monsters/monster_tuning.gd'], ['B11', 'B12', 'B13', 'B14']),
 'waves': ('Wave release cadence and the compounding health ramp that feeds take_damage.', ['features/waves/wave_spawner.gd', 'features/waves/wave_tuning.gd'], ['B11']),
 'projectiles': ('Four delivery styles; Storm chain selection with the source coin flip.', ['features/projectiles/projectile.gd'], ['B15', 'B16']),
 'debug-overlay': ('F1 playtest overlay drawn in session._draw beneath the Grid child.', ['game/session.gd'], ['B17', 'B18']),
 'towers-and-art': ('Tower targeting and procedural drawing shared with the HUD build bar and ghost; tower stat table.', ['features/towers/tower.gd', 'features/towers/tower_tuning.gd', 'ui/hud.gd'], ['B19', 'B20']),
 'tests': ('Headless SceneTree suites; only the keyboard suite drives real input events.', ['tests/test_keyboard.gd', 'tests/test_data.gd', 'tests/test_game.gd', 'tests/test_match.gd', 'tests/check_persistence.gd', 'tests/capture_game.gd', 'tests/capture_boot.gd'], ['B21', 'B22']),
 'level-load': ('Level validation and the load-error surface.', ['game/session.gd', 'features/grid/grid.gd'], ['B23', 'B24']),
}
EXCLUSIONS = {
 '.gitignore': 'Version-control ignore list; no runtime role.',
 'export_presets.cfg': 'Export presets (macOS, Windows, Linux). Exports were not run or shown in this film; every capture ran the project from source.',
}

ROLES = {'game/main.tscn': 'saved scene stub', 'game/session.gd': 'session root script', 'project.godot': 'project settings',
         'levels/level_01.json': 'level data'}


def bookends():
    head = [
     dict(id='B00', act='ASK', pattern='ClaudeComposerAsk',
      narration=("Merhaba — this is Liam, in for Bear. That's the kind of prompt Walker expects, reconstructed here, "
                 "not a transcript. This time we open the project itself: a piece of code, then the exact thing it "
                 "does on screen, in the real build."),
      props=dict(greeting='Merhaba, Liam', topic='WALKER · GODOT · GAMEDEV', segment='Inside the Godot Code',
                 command=ASK, runningText='illustrative reconstruction — not the historical prompt',
                 output=['Built: one 6-line scene file and about 3,000 lines of GDScript.',
                         'Every visual drawn in code; 65 automated checks.'],
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B01', act='BLUF', pattern='BrutalistHesitantWriter', lead=0.8, tail=1.5,
      narration=("Walker Tower Defense is built from script and draw calls. It's one six-line scene, about three "
                 "thousand lines of GDScript, and not a single image file. So every piece of code we read has a "
                 "result you can watch."),
      props=dict(text=("Walker Tower Defense\nis built from scenes and sprites.\nIt is one six-line scene,\n"
                       "about 3,000 lines of GDScript,\nand not a single image file."),
                 triggerWords='scenes and sprites', replacementWords='script and draw calls', fontSize=96,
                 lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
                 seed='walker-towerdefense-gamedev-2026-10', ink='#3D3929', accent='#D97757', bg='#FAF9F5',
                 face='serif', align='center', brandLabel='@NikBearBrown')),
     dict(id='B02', act='BODY', pattern='GodotDevWorkbench',
      narration=("Open the scene file and there's one node. Run it, and the session script builds the rest: the "
                 "board, a canvas layer for the HUD, one node per tower and monster. Not one of them is named — the "
                 "live tree reads at-Node2D-at-two. The tidy Grid and Hud in the project's own brief are "
                 "descriptions, not node names."),
      props=dict(mode='tree', title='Saved Scene vs. Live Tree', project=PROJ,
                 source='Live tree: probed from a running instance of res://game/main.tscn on an isolated copy '
                        '(tree_probe.gd), after Enter, one Fire tower and Space — input only.',
                 treeLabel='Remote (runtime) tree — probed', tree=TREE,
                 inspectorLabel='Source notes — not Inspector values',
                 notes=[{'label': 'Saved scene (game/main.tscn)', 'value': '1 node: WalkerTowerDefense'},
                        {'label': 'Live, one tower, wave 1', 'value': '7 nodes, created by session.gd'},
                        {'label': 'Names', 'value': 'auto-generated (@Node2D@2…); never set in code'}],
                 cues=[{'at': 2.0, 'line': 1, 'label': 'the only saved node'},
                       {'at': 6.0, 'line': 2, 'label': 'Grid, added in _ready'},
                       {'at': 9.0, 'line': 4, 'label': 'HUD on a CanvasLayer'},
                       {'at': 12.0, 'line': 5, 'label': 'one node per tower and monster'}])),
    ]
    tail = [
     dict(id='B25', act='VERDICT', pattern='ClaudeVerdictArtifact',
      narration=("Verdict. This is a project you can read top to bottom as text, and its best habit, the input-only "
                 "keyboard test, exists because of a real failure. The three defects I found are all draw order and "
                 "layering: places where the code is right and the screen isn't. And a person still has to play it."),
      props=dict(artifactTitle='Verdict', artifactHeading='Readable code, unreadable corners', brandLabel='@NikBearBrown',
                 artifactLines=['Implemented: one 6-line scene, ~3,000 lines of GDScript, every pixel from _draw().',
                                'Good habits: one fixed-step loop, recovered constants locked by tests, an input-only keyboard suite.',
                                'Defects on screen: F1 overlay under the board; error panel under the menu card; poison reads white.',
                                'Not judged here: fun, fairness, balance. That is a human playtest — 0 of 22 done.'])),
     dict(id='B26', act='HANDOFF', pattern='ClaudeComposerAsk',
      narration=("Your turn. Paste this into Claude in your own Godot project: Use Walker on my Godot project. Pick "
                 "one draw-order or layering assumption — which node or canvas layer paints over which — and predict "
                 "what the player will see. Then write a capture that proves or disproves it with real input, and "
                 "only after that, propose the smallest code change. Make the prediction before you look; it's the "
                 "only way to find out whether you understand your own scene tree. Liam, in for Bear."),
      props=dict(greeting='Your turn.', topic='WALKER · YOUR TURN', segment='Predict, Then Capture',
                 command=("Use Walker on my Godot project. Pick one draw-order or layering assumption — which node or "
                          "canvas layer paints over which — and predict what the player will see. Then write a "
                          "capture that proves or disproves it with real input, and only after that, propose the "
                          "smallest code change."),
                 runningText='paste this into Claude…',
                 output=['Look for: a prediction written before the capture.',
                         'Look for: the smallest change, not a rewrite.'],
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B27', act='OUTRO', pattern='ClaudeTitleOutro', tail=1.0,
      narration=f'{TITLE}. At Nik Bear Brown.',
      props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
    ]
    return head, tail


QC_CLIP = {'full_bleed': True, 'full_bleed_reason': ('The engine frame (3049x2160) fills the full frame height '
           'by design: native 4K game pixels, not a title card. Our overlays sit inside title-safe; the game HUD at '
           'the top edge is game UI.')}
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
                                     source=f"godot/{p['path']}:{p['a']}-{p['b']} at caf082c · Godot editor reconstruction",
                                     code=code, startLine=p['a'], codeFontSize=p['size'],
                                     inspectorLabel='Source notes — not Inspector values',
                                     notes=[{'label': k, 'value': v} for k, v in p['notes']],
                                     output=[f"{p['path']} · lines {p['a']}–{p['b']}"]), pair=p))
        if p.get('receipt'):
            beats.append(dict(id=p['result'], act='BODY', pattern='ExecutedData', narration=p['rnarr'], min_total=15.2,
                              props=dict(title='Recorded Keyboard-Suite Receipts', mode='table',
                                         columnLabels=['Run (receipt)', 'Checks'],
                                         rows=[{'label': 'Fix reverted — FAIL', 'value': 8, 'at': 1.0},
                                               {'label': 'Fix reverted — PASS', 'value': 1, 'at': 2.0},
                                               {'label': 'Current build — PASS', 'value': 9, 'at': 4.0},
                                               {'label': 'Current build — FAIL', 'value': 0, 'at': 5.0}],
                                         note='Recorded receipts, 2026-09-21 and 2026-09-28. Synthetic key events, not play.'), pair=p))
        else:
            beats.append(dict(id=p['result'], act='BODY', take=p['take'], narration=p['rnarr'], pair=p, lead=0.3,
                              **({'segments': p['segments']} if 'segments' in p else {'start': p['start'], 'end': p['end']})))
    beats.sort(key=lambda b: int(b['id'][1:]))
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
                         'method': 'scripted-input', 'staged': bool(spec['pair'].get('staged')),
                         'type_note': "engine capture of the game's own UI; GATE T pixel checks exempt (see BUILD-LOG.md)",
                         'show': [{'at': 0.0, 'event': f"real gameplay, take '{spec['take']}', build caf082c"}]}
            b['qc'] = QC_CLIP
        else:
            b['shot'] = {'type': 'GRAPHIC', 'source': 'remotion',
                         'remotion': {'pattern': spec['pattern'], 'props': dict(spec['props'])},
                         'show': [{'at': 0.0, 'event': spec['pattern']}]}
            if spec['pattern'] == 'BrutalistHesitantWriter':
                b['qc'] = QC_WRITER
        if spec['id'] == 'B27':
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
        'caption_policy': 'none', 'greeting_language': 'Turkish (Merhaba)',
        'teaching_contract': 'code-then-result-v1',
        'audience': "makers following the channel's Claude + Walker game workflows",
        'game_build': {'commit': 'caf082c7968bca13cf8751983d27787107b46b2d', 'snapshot_sha256': rk.BUILD_ID,
                       'engine': 'Godot 4.7.2.stable.official.ed1daf0bf'},
        'note': ('godot-gamedev walker film. Code panels are Godot editor reconstructions with verbatim source; each is '
                 'followed by real engine output of the same build. No game change, no paid calls, no upload.'),
        'tags': ['Walker', 'Godot 4', 'GDScript', 'game development', 'tower defense', 'Claude', 'Kokoro'],
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
            label = (['STAGED FAILURE', 'level file broken', 'in an isolated copy', f'build {rk.BUILD_COMMIT}']
                     if spec['pair'].get('staged') else None)
            info = rk.cut_segments(take, segs, REEL / f'media/{bid}.mp4', label)
            total = info['frames'] / rk.FPS
            held = sum(s['output_frames'] for s in info['segments'] if s['kind'] == 'hold')
            if held:
                print(f'{bid}: {held} held frames')
            b['shot']['clip'] = info
            b['shot']['evidence_media'] = f'media/{bid}.mp4'
        else:
            total = rk.frames_for(max(spec.get('min_total', 0.0),
                                      lead + speech + spec.get('tail', 0.0) + (0.4 if b['act'] == 'VERDICT' else 0.3))) / rk.FPS
            props = b['shot']['remotion']['props']
            if spec['pattern'] != 'ExecutedData':
                props['durationSeconds'] = total
            if spec['pattern'] == 'ExecutedData':
                b['shot']['evidence_media'] = f'media/{bid}.mp4'
            if spec['pattern'] == 'GodotDevWorkbench' and 'pair' in spec:
                props['cues'] = cue_list(spec['narration'], spec['pair']['cues'], lead, speech)
        rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
        b['audio_file'] = f'audio/beat-{bid}.wav'
        b['actual_duration_s'] = total
    for take in sorted({s['take'] for s in specs.values() if 'take' in s}):
        for suffix in ('.mp4', '-inputs.jsonl'):
            shutil.copy2(rk.TAKES / f'{take}{suffix}', REEL / f'capture/{take}{suffix}')
    for name in ('keyboard-1790012997.43825.json', 'keyboard-1790606725.01996.json'):
        shutil.copy2(GAME_PKG / 'evidence' / name, REEL / 'evidence' / name)
    shutil.copy2(CAPS / 'tree_probe.txt', REEL / 'evidence/tree_probe.txt')
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    for b in sheet['beats']:
        print(f"{b['beat_id']:4} {b['act']:8} {b['actual_duration_s']:7.2f}s  speech {b['kokoro_duration_s']:6.2f}s")
    print('total', round(sum(b['actual_duration_s'] for b in sheet['beats']), 1), 's')


def ledger():
    sheet = json.loads((REEL / 'beat_sheet.json').read_text())
    inv = sorted(p.relative_to(GODOT).as_posix() for p in GODOT.rglob('*')
                 if p.is_file() and not any(x in ('.godot', '.git') for x in p.relative_to(GODOT).parts)
                 and p.suffix != '.uid')
    comp_of = {}
    for cid, (_, files, _) in COMPONENTS.items():
        for f in files:
            comp_of.setdefault(f, []).append(cid)
    files = []
    for path in inv:
        if path in EXCLUSIONS:
            continue
        if path not in comp_of:
            raise SystemExit(f'unassociated file: {path}')
        files.append({'path': path, 'sha256': hashlib.sha256((GODOT / path).read_bytes()).hexdigest(),
                      'role': ROLES.get(path, 'test script' if path.startswith('tests/') else 'runtime script'),
                      'component_ids': comp_of[path]})
    pairs = []
    for p in PAIRS:
        media = REEL / f"media/{p['result']}.mp4"
        pairs.append({'code_beat': p['code'], 'result_beat': p['result'], 'observation': p['obs'],
                      'media': {'path': f"media/{p['result']}.mp4", 'sha256': rk.sha256(media)}})
    data = {'schema_version': 1, 'teaching_contract': 'code-then-result-v1',
            'game': {'path': '../../Walker-Godot-TowerDefense/godot', 'commit': 'caf082c', 'build_id': rk.BUILD_ID},
            'files': files,
            'components': [{'id': cid, 'explanation': e, 'beat_ids': beats, 'files': fl}
                           for cid, (e, fl, beats) in COMPONENTS.items()],
            'excerpts': [{'beat_id': p['code'], 'path': p['path'], 'start_line': p['a'], 'end_line': p['b'],
                          'text': lines(p['path'], p['a'], p['b'])} for p in PAIRS],
            'exclusions': [{'path': k, 'reason': v} for k, v in EXCLUSIONS.items()],
            'code_result_pairs': pairs}
    (REEL / 'gamedev-evidence.json').write_text(json.dumps(data, indent=1, ensure_ascii=False) + '\n')
    print(f'ledger: {len(files)} files, {len(EXCLUSIONS)} exclusions, {len(pairs)} pairs')


if __name__ == '__main__':
    {'author': author, 'finish': finish, 'ledger': ledger}[sys.argv[1]]()
