"""Builds beat_sheet.json + coverage.json for claude-liam-walker-towerdefense-walkthrough
(godot-waikthrough walker).

    python3 make_sheet.py author    # narration + shots (before Kokoro)
    python3 make_sheet.py finish    # after Kokoro: exact clips, padded audio, coverage

Gameplay beats are consecutive, non-overlapping windows of scripted-input takes of the
real main scene (build caf082c). A clip is never retimed: if narration outruns a take,
the clip ends on a labelled held frame.
"""
import json
import shutil
import sys
from pathlib import Path

REEL = Path(__file__).resolve().parent
CAPS = REEL.parent / 'walker-towerdefense-captures'
sys.path.insert(0, str(CAPS))
import reelkit as rk  # noqa: E402

SLUG = 'claude-liam-walker-towerdefense-walkthrough'
TITLE = 'Walker Tower Defense: Every Feature, Played'

ASK = ('Please use Walker to convert my game design document about a four-element tower defense — '
       'Fire, Ice, Poison and Storm towers on a 12-by-8 grid, where every tower you build reshapes '
       'the monsters\' route — into a playable Godot project.')

# Gameplay beats: (id, take, window or segments, narration)
CLIPS = [
 dict(id='B02', take='opening', start=0, end=410, lead=0.3,
  narration=("It opens on the menu: best wave, zero. Click start: fifty gold, five lives. Pick Fire from "
             "the bar, and a ghost tower and its range follow the cursor. Over lava it turns red, and the "
             "click is refused. The corner takes it.")),
 dict(id='B03', take='opening', start=410, end=902, lead=0.3,
  narration=("Key two picks Ice; a right-click cancels it. Two again, and Ice goes in beside the road — "
             "five gold left. Key four asks for Storm: not enough gold. Escape leaves build mode. Space "
             "sends wave one: two monsters on the shortest road. The towers fire on their own; each kill "
             "pays four.")),
 dict(id='B04', take='opening', start=902, end=1500, lead=0.3,
  narration=("Wave two, and the speed control: the button takes it to double, F to triple. Same rules, "
             "faster clock. Two monsters get through — lives drop to three. Back to normal speed for wave "
             "three, and this opening can't hold it. Five lives gone. The exit was overrun: furthest wave "
             "three, and that's now the best. Enter, and you're straight back in.")),
 dict(id='B05', take='opening', start=1500, end=1984, lead=0.3,
  narration=("A different opening: one Fire tower, then click it. The panel offers sell for ten, or "
             "upgrade for thirty. Upgrade — a chevron appears, and the button reads maxed: each tower "
             "upgrades exactly once. Right-click clears the selection, and the next wave walks in.")),
 dict(id='B06', take='maze', start=30, end=333, lead=0.3,
  narration=("New run, started with Enter. Wave one walks, and I try to build where a monster stands: "
             "refused, monster in the way. With no towers, both monsters walk out.")),
 dict(id='B07', take='maze', start=333, end=967, lead=0.3,
  narration=("Fire beside the spawn is fine. A second Fire that would seal the corner is refused: would "
             "block the path — and that message is gone in three-tenths of a second. A tower dropped onto "
             "the road is allowed; the tinted route bends round it, and wave two follows the new line. "
             "Click the corner tower and sell it: ten gold back.")),
 dict(id='B08', take='poison', start=50, end=445, lead=0.3,
  narration=("Poison by key three, Fire by key one, and F1 for the debug overlay — which you can barely "
             "read: the board is drawn on top of it. Escape mid-wave pauses; the card says so. Enter "
             "resumes.")),
 dict(id='B09', take='poison', start=445, end=728, lead=0.3,
  narration=("Wave two. Watch the lead monster once it's poisoned: it goes pale, not green. Every poison "
             "tick counts as a hit, and every hit flashes white.")),
 dict(id='B10', take='storm', segments=[('play', 60, 144), ('replay', 173, 6, 8), ('play', 204, 30)], lead=0.3,
  narration=("Storm, alone on the board. Space. The beam hits one monster and jumps to its neighbour — on "
             "screen for a fifth of a second at real speed. Here it is again, slowed down. Chain, or "
             "flicker? That's for a person to say.")),
 dict(id='B11', take='focus', start=68, end=335, lead=0.3,
  narration=("Mid-wave, the capture brings Finder forward. The game loses focus and pauses itself. Focus "
             "returns; it stays paused until Enter.")),
 dict(id='B12', take='lose', start=520, end=829, lead=0.3,
  narration=("No towers, so wave two ends the run. Enter plays again. Then mid-wave, R: a full restart — "
             "wave zero, fifty gold, the ramp reset.")),
 dict(id='B13', take='relaunch', start=0, end=354, lead=0.3,
  narration=("A relaunch boots with best wave three: the score survived. This run has debug tools switched "
             "on in project settings. F1 for the overlay, then F2 skips straight to the next wave — twice.")),
 dict(id='B14', take='broken', start=0, end=389, lead=0.3, staged=True,
  narration=("Last, a staged failure: the level file deliberately broken in a copy. The error panel exists — "
             "but the menu card sits on top of it, and Enter quietly starts a session that can't move.")),
]

# Feature inventory: (id, beat, take, action_frame, observation, riff)
FEATURES = [
 ('menu-and-best-readout', 'B02', 'opening', 30, 'Boot shows the menu card; the top bar reads BEST 0 on a fresh save folder.', 'The best wave is the only thing the game remembers; a fresh save proves it starts from nothing.'),
 ('start-by-click', 'B02', 'opening', 85, 'Clicking START enters play with 50 gold and 5 lives.', 'Mouse and keyboard both start a run; the mouse path never touched the InputMap, which is how the dead-keyboard bug hid.'),
 ('build-bar-pick', 'B02', 'opening', 145, 'Clicking the Fire button highlights it and enters build mode.', 'The bar shows cost and a one-word skill, so the choice is legible before any tooltip.'),
 ('build-ghost-and-range', 'B02', 'opening', 200, 'A ghost tower and its 2.5-tile range circle follow the cursor across the board.', 'Range is visible before spending, which matters when every tower also reshapes the road.'),
 ('refusal-cant-build-here', 'B02', 'opening', 269, 'Clicking lava flashes the tile red with "Can\'t build here".', 'Lava is walkable but not buildable; the tint warns before the click.'),
 ('place-tower', 'B02', 'opening', 359, 'Fire placed at (10,1); gold drops 50 to 30.', 'The corner covers both legs of the default L-shaped route.'),
 ('build-key-pick', 'B02', 'opening', 389, 'Key 2 enters Ice build mode.', 'Keys 1 to 4 mirror the bar; they arrived in the Phase B input audit.'),
 ('cancel-build-right-click', 'B03', 'opening', 455, 'Right-click cancels build mode; the ghost disappears.', 'A cheap undo before money is spent.'),
 ('refusal-not-enough-gold', 'B03', 'opening', 587, 'Storm (35) with 5 gold is refused: "Not enough gold".', 'Gold is checked first, so even a lava click reports gold when you are broke.'),
 ('cancel-build-esc', 'B03', 'opening', 619, 'Esc leaves build mode and does not pause.', 'One key, two meanings, ordered: cancel first, pause second.'),
 ('wave-release-and-route', 'B03', 'opening', 667, 'Space releases wave 1; two monsters walk the tinted shortest route from IN to OUT.', 'The route tint is the whole maze readout; whether it is strong enough is checklist item 1.'),
 ('towers-fire-and-kill-reward', 'B03', 'opening', 780, 'Fire and Ice shoot automatically; by the end of wave 1 gold has gone from 5 to 13.', 'Kill income is 4 gold flat; checklist item 14 asks whether that keeps a player building.'),
 ('speed-toggle', 'B04', 'opening', 951, 'The SPEED button goes 1x to 2x; F goes to 3x and later back to 1x.', 'Speed multiplies the clock, not the rules, so outcomes should not change with speed.'),
 ('leak-costs-life', 'B04', 'opening', 1032, 'Two wave-2 monsters reach OUT; LIVES drops from 5 to 3.', 'A leak is the only way to lose; on main it is shown only by the LIVES counter, which turns red at two or fewer. (AUDIO-PLAN.md mentions a red vignette; that exists only on the unmerged art branch.)'),
 ('game-over-card', 'B04', 'opening', 1366, 'At 0 lives: "The exit was overrun. Furthest wave: 3  Best: 3".', 'Endless by decision: losing is the only end state.'),
 ('play-again-enter', 'B04', 'opening', 1466, 'Enter on the game-over card starts a fresh run: 50 gold, 5 lives, wave 0.', 'Retry is one key; the compounding ramp resets with it.'),
 ('select-tower-panel', 'B05', 'opening', 1656, 'Clicking a placed tower shows its range and SELL 10 / UPGRADE 30.', 'Sell and upgrade live in one panel, priced before you commit.'),
 ('upgrade-once', 'B05', 'opening', 1710, 'UPGRADE spends 30; a chevron appears; the button reads MAXED; SELL becomes 34.', 'One tier only; sale value adds round(0.8 x 30).'),
 ('right-click-clear-selection', 'B05', 'opening', 1788, 'Right-click with a tower selected clears the selection.', 'Same gesture as cancel, applied to the other mode.'),
 ('start-by-enter', 'B06', 'maze', 41, 'Enter on the menu starts a run.', 'The keyboard path that was once dead now works on its own.'),
 ('refusal-monster-in-the-way', 'B06', 'maze', 100, 'Trying to build on a tile a monster occupies is refused: "Monster in the way".', 'You cannot drop a tower on a monster to trap it.'),
 ('refusal-would-block', 'B07', 'maze', 482, 'With Fire at (0,1), Fire at (1,0) would seal the spawn and is refused: "Would block the path".', 'The rule the Unity original lacked; the reason is visible for at most 0.3 s.'),
 ('reroute-around-tower', 'B07', 'maze', 602, 'A tower placed on the road at (5,0) is accepted and the tinted route changes; wave 2 follows it.', 'This is the maze: building changes where they walk, not just what shoots them.'),
 ('sell-tower', 'B07', 'maze', 888, 'Selecting the (0,1) tower and pressing SELL returns 10 gold.', 'Selling reopens the tile and re-paths everyone.'),
 ('debug-overlay-f1', 'B08', 'poison', 205, 'F1 shows the debug overlay; only its left edge is visible, the rest is covered by the board.', 'Defect: drawn by the session under its own Grid child.'),
 ('pause-and-resume-keys', 'B08', 'poison', 327, 'Esc mid-wave shows "Paused." and freezes the board; Enter resumes.', 'The card lists R and Esc; Enter also resumes.'),
 ('poison-status', 'B09', 'poison', 510, 'A poisoned wave-2 monster turns pale white rather than green while the poison ticks.', 'Each 0.1 s tick is a hit, and each hit resets the white flash; checklist item 10.'),
 ('storm-chain', 'B10', 'storm', 173, 'The Storm beam hits one monster and hops to its neighbour, visible for 6 frames (0.2 s) at 1x.', 'Shown again as a labelled 1/8-speed replay; checklist item 11.'),
 ('pause-on-focus-loss', 'B11', 'focus', 191, 'When macOS brings Finder forward, the game pauses; it stays paused when focus returns until Enter.', 'Correct and conservative: regaining focus does not resume play.'),
 ('restart-r', 'B12', 'lose', 779, 'R mid-wave restarts: wave 0, 50 gold, board cleared.', 'Restart resets the health ramp too (deviation D-05).'),
 ('best-persists-relaunch', 'B13', 'relaunch', 30, 'A new process boots showing BEST 3, written by an earlier run.', 'The one value saved to disk survives a relaunch.'),
 ('wave-skip-f2-debug', 'B13', 'relaunch', 208, 'With walker/debug/enabled=true, F2 jumps from wave 1 to 2, then to 3.', 'A playtest tool, off by default; this take enabled it on purpose.'),
 ('level-load-error-panel', 'B14', 'broken', 61, 'With level_01.json missing "exit", an error panel is drawn but the menu card covers most of it; Enter then sets PLAYING and Space starts wave 1 behind a frozen HUD.', 'Staged in a copy. The failure surface exists, but a player cannot read it.'),
]
PLANNED = [
 ('audio-cues', 'AUDIO-PLAN.md specifies eight cues; the source had no audio and none has been added.'),
 ('recovered-art-on-main', 'An unmerged branch wires recovered PNGs behind a default-off toggle; main ships no recovered art pending provenance review.'),
]


def bookends():
    return [
     dict(id='B00', act='ASK', pattern='ClaudeComposerAsk',
      narration=("Jambo — this is Liam, in for Bear. Here's the kind of prompt Walker is built for — "
                 "reconstructed, not a transcript. Today I'm not reading the design. I'm playing the build: "
                 "every feature the code implements, driven by a script through the game's real inputs, at "
                 "real speed."),
      props=dict(greeting='Jambo, Liam', topic='WALKER · GODOT · WALKTHROUGH', segment='Every Feature, Played',
                 command=ASK, runningText='illustrative reconstruction — not the historical prompt',
                 output=['Built: one 12×8 map, four towers, endless waves (Godot 4.7.2).',
                         'Not yet: a human playtest — 0 of 22 checklist items.'],
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B01', act='BLUF', pattern='BrutalistHesitantWriter', lead=0.8, tail=1.5,
      narration=("Walker Tower Defense is a playable game: one map, four towers, endless waves. Every feature "
                 "you'll see was played by a script, not a person — so this shows what works, not whether "
                 "it's any fun."),
      props=dict(text=("Walker Tower Defense\nis a finished game:\none map, four towers,\nendless waves.\n"
                       "Every feature here was played\nby a script, not by a person."),
                 triggerWords='finished', replacementWords='playable', fontSize=96, lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
                 seed='walker-towerdefense-walkthrough-2026-10', ink='#3D3929', accent='#D97757',
                 bg='#FAF9F5', face='serif', align='center', brandLabel='@NikBearBrown')),
    ], [
     dict(id='B15', act='VERDICT', pattern='ClaudeVerdictArtifact',
      narration=("Verdict. Everything the code implements, I could play through its real inputs, and it does "
                 "what the code says. Three things look broken on screen: the debug overlay and the error "
                 "panel are both covered up, and poison reads as white. Three more are too fast to judge "
                 "without a person. And every opening I scripted was overrun by wave five. Balance and fun "
                 "are still nobody's call yet."),
      props=dict(artifactTitle='Verdict', artifactHeading='Plays as written. Not proven.', brandLabel='@NikBearBrown',
                 artifactLines=['Observed working: 33 implemented features, each through real key and mouse input.',
                                'Defects on screen: F1 overlay under the board; level-error panel under the menu card; poison reads white.',
                                'Needs a person: 0.3 s refusal text, 0.2 s storm chain, poison on green monsters.',
                                'Untested by anyone: fun, fairness, balance. Every scripted opening lost by wave 5.',
                                'Planned, not built: audio (8 cues specified), recovered art on main.'])),
     dict(id='B16', act='HANDOFF', pattern='ClaudeComposerAsk',
      narration=("Your turn. Paste this into Claude in your own Godot project: Use Walker on my Godot game. "
                 "Write an input-only capture driver: it may read game state to decide when to act, but it may "
                 "only press keys and click. Play every feature, assert each visible result, and log every "
                 "input. Then list three things the footage shows that my automated tests never check. "
                 "The first rule is the one that matters: a driver that calls game functions directly will miss "
                 "exactly what a player hits. That's how this game's keyboard died with every test green. "
                 "Liam, in for Bear."),
      props=dict(greeting='Your turn.', topic='WALKER · YOUR TURN', segment='Play It Like a Player',
                 command=("Use Walker on my Godot game. Write an input-only capture driver: it may read game "
                          "state to decide when to act, but it may only press keys and click. Play every "
                          "feature, assert each visible result, and log every input. Then list three things the "
                          "footage shows that my automated tests never check."),
                 runningText='paste this into Claude…',
                 output=['Look for: inputs only — no direct calls into the game.',
                         'Look for: things the footage shows that no test asserts.'],
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B17', act='OUTRO', pattern='ClaudeTitleOutro', tail=1.0,
      narration=f'{TITLE}. At Nik Bear Brown.',
      props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
    ]


def author():
    head, tail = bookends()
    beats = []
    old_path = REEL / 'beat_sheet.json'
    old = {b['beat_id']: b for b in json.loads(old_path.read_text())['beats']} if old_path.exists() else {}
    for spec in head + CLIPS + tail:
        b = {'beat_id': spec['id'], 'act': spec.get('act', 'BODY'), 'narration_text': spec['narration'],
             'voice': 'am_onyx', 'engine': 'kokoro',
             'estimated_duration_s': round(len(spec['narration'].split()) / 3.3, 1)}
        if 'take' in spec:
            b['shot'] = {'type': 'SCREEN', 'source': 'own', 'treatment': 'none', 'capture': spec['take'],
                         'type_note': 'engine capture of the game\'s own UI; GATE T pixel checks exempt (see BUILD-LOG.md); overlays verified by eye',
                         'method': 'scripted-input', 'staged': bool(spec.get('staged')),
                         'show': [{'at': 0.0, 'event': f"real gameplay, take '{spec['take']}', build caf082c"}]}
            b['qc'] = {'full_bleed': True, 'full_bleed_reason': ('The engine frame (3049x2160) fills the full '
                       'frame height by design: native 4K game pixels, not a title card. Our overlays sit inside '
                       'title-safe; the game HUD at the top edge is game UI.')}
        else:
            b['shot'] = {'type': 'GRAPHIC', 'source': 'remotion',
                         'remotion': {'pattern': spec['pattern'], 'props': dict(spec['props'])},
                         'show': [{'at': 0.0, 'event': spec['pattern']}]}
        if spec.get('pattern') == 'BrutalistHesitantWriter':
            b['qc'] = {'sparse_by_design': True, 'sparse_reason': ('Hesitant writer: text is typed on screen over '
                       'the narration, so mid-beat samples legitimately show a partial page. The finished six-line '
                       'text fills the safe area and holds for the last 1.5 s.')}
        if spec['id'] == 'B17':
            b['kind'] = 'outro_voice'
            b['tail_silence_s'] = 1.0
        if spec.get('lead'):
            b['lead_silence_s'] = spec['lead']
        prev = old.get(spec['id'])
        if prev and prev.get('narration_text') == spec['narration'] and 'kokoro_audio_file' in prev:
            b['audio_file'] = prev['kokoro_audio_file']
        beats.append(b)
    sheet = {'metadata': {
        'slug': SLUG, 'title': TITLE, 'topic': 'WALKER · GODOT · WALKTHROUGH', 'skill': 'godot-waikthrough',
        'modifier': 'walker', 'channel': 'claude-liam', 'brand': 'claude-liam', 'persona': 'Liam (in for Bear)',
        'in_for_bear': True, 'voice': 'am_onyx', 'voice_kokoro': 'am_onyx', 'engine': 'kokoro',
        'palette': 'claude', 'register': 'Teardown', 'fps': 30, 'width': 3840, 'height': 2160,
        'aspect_ratio': '16:9', 'fit': 'crop', 'captions': False, 'caption_policy': 'none',
        'greeting_language': 'Swahili (Jambo)',
        'audience': 'makers following the channel\'s Claude + Walker game workflows',
        'game_build': {'commit': 'caf082c7968bca13cf8751983d27787107b46b2d', 'snapshot_sha256': rk.BUILD_ID,
                       'engine': 'Godot 4.7.2.stable.official.ed1daf0bf'},
        'note': ('godot-waikthrough walker film. Every gameplay beat is an exact-frame window of a '
                 'scripted-input take of the real main scene; no human playtest. The game is silent; '
                 'no sound was added. No paid calls, no upload.'),
        'tags': ['Walker', 'Godot 4', 'tower defense', 'gameplay walkthrough', 'Claude', 'Kokoro'],
    }, 'beats': beats}
    old_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    print(f'authored {len(beats)} beats')


def finish():
    sheet_path = REEL / 'beat_sheet.json'
    sheet = json.loads(sheet_path.read_text())
    head, tail = bookends()
    specs = {s['id']: s for s in head + CLIPS + tail}
    for d in ('audio', 'capture', 'media'):
        (REEL / d).mkdir(exist_ok=True)
    windows = {}
    for b in sheet['beats']:
        bid, spec = b['beat_id'], specs[b['beat_id']]
        mp3 = REEL / f'mp3/beat-{bid}.mp3'
        speech = rk.probe_duration(mp3)
        lead = spec.get('lead', 0.0)
        b['kokoro_audio_file'] = f'mp3/beat-{bid}.mp3'
        b['kokoro_duration_s'] = round(speech, 3)
        if 'take' in spec:
            need = rk.frames_for(lead + speech + 0.5)
            take = spec['take']
            if 'segments' in spec:
                segs = list(spec['segments'])
                have = sum(s[2] * (s[3] if s[0] == 'replay' else 1) for s in segs)
                k, s0, n = segs[-1][:3]
                room = rk.take_frames(take) - (s0 + n)
                grow = max(0, min(room, need - have))
                segs[-1] = (k, s0, n + grow)
                if need - have - grow > 0:
                    segs.append(('hold', need - have - grow))
                win = (spec['segments'][0][1], s0 + n + grow)
            else:
                n = spec['end'] - spec['start']
                segs = [('play', spec['start'], n)]
                if need > n:
                    segs.append(('hold', need - n))
                win = (spec['start'], spec['end'])
            label = None
            if spec.get('staged'):
                label = ['STAGED FAILURE', 'level file broken', 'in an isolated copy', f'build {rk.BUILD_COMMIT}']
            info = rk.cut_segments(take, segs, REEL / f'media/{bid}.mp4', label)
            total = info['frames'] / rk.FPS
            rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
            b['audio_file'] = f'audio/beat-{bid}.wav'
            b['actual_duration_s'] = total
            b['shot']['clip'] = info
            b['shot']['evidence_media'] = f'media/{bid}.mp4'
            windows[bid] = (take, win)
            held = sum(s['output_frames'] for s in info['segments'] if s['kind'] == 'hold')
            if held:
                print(f'{bid}: {held} held frames ({held / 30:.1f}s) — narration outran the window')
            continue
        tail_s = spec.get('tail', 0.0)
        total = rk.frames_for(lead + speech + tail_s + (0.4 if b['act'] == 'VERDICT' else 0.25)) / rk.FPS
        rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
        b['audio_file'] = f'audio/beat-{bid}.wav'
        b['actual_duration_s'] = total
        b['shot']['remotion']['props']['durationSeconds'] = total
    takes = sorted({t for t, _ in windows.values()})
    captures = {}
    for take in takes:
        for suffix in ('.mp4', '-inputs.jsonl'):
            shutil.copy2(rk.TAKES / f'{take}{suffix}', REEL / f'capture/{take}{suffix}')
        captures[take] = {'path': f'capture/{take}.mp4', 'sha256': rk.sha256(REEL / f'capture/{take}.mp4'),
                          'build_id': rk.BUILD_ID, 'method': 'scripted-input',
                          'input_log': f'capture/{take}-inputs.jsonl',
                          'staged': take == 'broken',
                          'note': ('level_01.json deliberately broken in a second isolated copy'
                                   if take == 'broken' else 'unmodified game code; harness config only')}
    features = []
    for fid, bid, take, action, obs, riff in FEATURES:
        t, (w0, w1) = windows[bid]
        assert t == take, (fid, t, take)
        if not w0 < action < w1:
            raise SystemExit(f'{fid}: action frame {action} outside {bid} window {w0}-{w1}')
        features.append({'id': fid, 'status': 'implemented', 'evidence': [{
            'capture': take, 'beat_id': bid, 'start_s': round(w0 / 30, 3), 'action_s': round(action / 30, 3),
            'end_s': round(w1 / 30, 3), 'observation': obs, 'riff': riff}]})
    for fid, reason in PLANNED:
        features.append({'id': fid, 'status': 'planned', 'reason': reason, 'evidence': []})
    coverage = {'schema_version': 1, 'game': {'name': 'walker-towerdefense', 'build_id': rk.BUILD_ID,
                                              'commit': 'caf082c'},
                'captures': captures, 'features': features,
                'not_exercised': ['exported builds (all takes ran from source)',
                                  'audio (the game has none)']}
    (REEL / 'coverage.json').write_text(json.dumps(coverage, indent=1, ensure_ascii=False) + '\n')
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    for b in sheet['beats']:
        print(f"{b['beat_id']:4} {b['act']:8} {b['actual_duration_s']:7.2f}s  speech {b['kokoro_duration_s']:6.2f}s")
    print('total', round(sum(b['actual_duration_s'] for b in sheet['beats']), 1), 's;',
          len(FEATURES), 'implemented features,', len(PLANNED), 'planned')


if __name__ == '__main__':
    {'author': author, 'finish': finish}[sys.argv[1]]()
