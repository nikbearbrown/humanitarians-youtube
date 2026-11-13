"""Builds beat_sheet.json + coverage.json for claude-liam-basketball-walkthrough
(godot-waikthrough walker).

    python3 make_sheet.py author    # narration + shots (before Kokoro)
    python3 make_sheet.py finish    # after Kokoro: exact clips, padded audio, coverage

Gameplay beats are consecutive, non-overlapping windows of the three scripted-input
takes of the real game (build 8f86cc8). A clip is never retimed: if narration
outruns its window, the clip ends on a labelled held frame.
"""
import json
import shutil
import sys
from pathlib import Path

REEL = Path(__file__).resolve().parent
CAPS = REEL.parent / 'basketball-captures'
sys.path.insert(0, str(CAPS))
import reelkit as rk  # noqa: E402

SLUG = 'claude-liam-basketball-walkthrough'
TITLE = 'Basketball Blaster: Every Feature, Played'

ASK = ('Please use Walker to convert my game design document about Basketball Blaster: Fowl Play — '
       'Mr. Block, armed with a basketball gun and basketball grenades, collects every egg across three '
       'arenas while chickens pour out of pipes — into a playable Godot project.')

CLIPS = [
 dict(id='B02', take='campaign', start=0, end=387, lead=0.3,
  narration=("It opens on the title art with three buttons. How to Play lists every key, the controller layout, "
             "and seven rules: eggs clear an arena, grenades beep three times, three lives of three hits each. "
             "Back to Menu returns.")),
 dict(id='B03', take='campaign', start=387, end=1156, lead=0.3,
  narration=("Play starts the pre-game briefing. The coach's first line types out letter by letter, and the prompt "
             "says enter or click to continue. So the script clicks the dialogue box. Nothing. It clicks above it. "
             "Still nothing: a full-screen shade layer eats every click. Enter works. A press mid-line finishes the "
             "line at once; the next press moves on. Eight lines later, Mister Block says let's ball, and the court "
             "fades in.")),
 dict(id='B04', take='campaign', start=1156, end=1694, lead=0.3,
  narration=("Arena one, Street Court. The banner says grab every egg. A walk, a jump, and a second Space in mid-air "
             "for the double jump. Shift fires the jetpack, and the blue bar is fuel. The gun tracks the crosshair, a "
             "ball every four tenths of a second, and right-click lobs the grenade. Two chickens tag him. Watch the "
             "health balls dim.")),
 dict(id='B05', take='campaign', start=1694, end=2471, lead=0.3,
  narration=("Now the script holds one spot and fights. With one health ball left, the next touch costs a life: a "
             "fade, and a respawn at the glowing gate. Then a grenade lands in a crowd, and four chickens go at once. "
             "Mega kill. Every death throws feathers and a splat that fades, and every hit shakes the camera. Ten "
             "kills later, the egg counter still reads one of five. Kills don't move it.")),
 dict(id='B06', take='campaign', start=2471, end=2999, lead=0.3,
  narration=("So it goes for the eggs. Another life goes on the way: one left now. Jetpack up to the high platforms, "
             "egg, egg, egg, and the fifth one ends it. Court cleared, with kills, eggs and lives totted up. Next Arena.")),
 dict(id='B07', take='campaign', start=2999, end=3398, lead=0.3,
  narration=("Arena two. Escape pauses: time out, the flock will wait. Resume. Pause again, and Main Menu. The menu "
             "now offers Continue, Arena 2, because the campaign remembers where you were. Continue.")),
 dict(id='B08', take='campaign', start=3398, end=3977, lead=0.3,
  narration=("Sunset Rooftops: three pipes, an orange tint, six eggs. Same idea, higher up. A hit, another, a "
             "respawn, and the sixth egg clears it with two lives to spare. Kills this time: two. The script barely "
             "fought, and it didn't need to.")),
 dict(id='B09', take='campaign', start=3977, end=4755, lead=0.3,
  narration=("Arena three, the Fowl Play Finals: four pipes, a navy tint, seven eggs, and chickens that take four "
             "hits. This is the closest the run comes to losing. A life goes. Then another. Down to its last life, "
             "it keeps grabbing eggs. Seven of seven. Court cleared, one kill, one life left, and the button now reads "
             "Claim the Trophy.")),
 dict(id='B10', take='campaign', start=4755, end=5029, lead=0.3,
  narration=("Victory: thirteen kills and eighteen eggs, totalled across all three arenas. Main Menu, and the "
             "Continue button is gone.")),
 dict(id='B11', take='defeat', start=0, end=379, lead=0.3,
  narration=("A second run. Play, and Escape skips the whole briefing. Then a controller, simulated: the left stick "
             "walks, the right stick aims, the trigger fires, A jumps, and Start pauses and resumes.")),
 dict(id='B12', take='defeat', start=379, end=916, lead=0.3,
  narration=("R restarts the arena on the spot. Now the failure path, on purpose: the script walks into the flock "
             "with the gun silent. Three hits empty the health balls and cost a life. A respawn. Again. And the "
             "third life.")),
 dict(id='B13', take='defeat', start=916, end=1216, lead=0.3,
  narration=("Game over. The flock won arena one: run it back? Retry Arena loads the same court with three fresh "
             "lives.")),
 dict(id='B14', take='extras', start=0, end=406, lead=0.3,
  narration=("One last run, for the inputs not seen yet. Escape backs out of How to Play and skips the briefing. On "
             "the first platform, S plus Space drops straight through it.")),
 dict(id='B15', take='extras', start=406, end=872, lead=0.3,
  narration=("F fires and G throws a grenade, for players without a mouse. On the controller, LB throws and RB "
             "burns the jetpack. The pause menu's Restart Arena reloads the court. Main Menu, and Quit closes the game.")),
]

# (feature id, beat, take, action frame, observation, riff)
FEATURES = [
 ('main-menu', 'B02', 'campaign', 30, 'Title art with Play, How to Play and Quit; the harness arrow hovers Play then Quit.', 'Three buttons and a one-line hint: the menu promises the goal before the briefing does.'),
 ('how-to-play', 'B02', 'campaign', 177, 'How to Play lists 9 controls, 7 rules and the controller layout.', 'The same control list appears in three places: README, this screen and the pause menu.'),
 ('back-to-menu', 'B02', 'campaign', 354, 'Back to Menu returns to the title.', 'A plain round trip; no state is touched.'),
 ('briefing-typing', 'B03', 'campaign', 440, 'Line 1 types out character by character, then shows ENTER / CLICK TO CONTINUE · ESC TO SKIP.', 'Typing at 20 ms a character paces the reading without blocking it.'),
 ('briefing-click-dead', 'B03', 'campaign', 527, 'Clicks on and above the dialogue panel do not advance the line (defect D-01).', 'A full-screen shade ColorRect stops the mouse event before _unhandled_input sees it.'),
 ('briefing-enter', 'B03', 'campaign', 618, 'Enter advances; Enter mid-line completes the line at once.', 'Keyboard works, so the defect only bites mouse-first players.'),
 ('briefing-to-arena', 'B03', 'campaign', 1140, 'After line 8, Enter fades to arena 1.', 'One fade, then the arena loads.'),
 ('walk', 'B04', 'campaign', 1226, 'D then A walks Mr. Block right and left with a tilt and dust.', 'Acceleration differs on ground and in the air, so turns feel softer mid-jump.'),
 ('jump', 'B04', 'campaign', 1306, 'Space jumps.', 'Extra gravity after 0.2 s makes the fall quicker than the rise.'),
 ('double-jump', 'B04', 'campaign', 1365, 'A second Space in mid-air re-launches him upward.', 'One air jump, restored on landing.'),
 ('jetpack', 'B04', 'campaign', 1400, 'Holding Shift lifts him; the blue fuel bar drains.', 'Fuel refills fast on the ground and slowly in the air.'),
 ('aim-and-shoot', 'B04', 'campaign', 1490, 'The gun follows the crosshair; held left click fires a ball every 0.4 s.', 'Aim is the cursor, not the facing, so you can run one way and shoot the other.'),
 ('grenade', 'B04', 'campaign', 1593, 'Right-click lobs a grenade: three blinks, then the blast.', 'A fuse makes the grenade a placement decision, not a second gun.'),
 ('health-and-hit', 'B04', 'campaign', 1465, 'A chicken touch dims a health ball and flashes the player.', 'Three health per life; contact is a distance check.'),
 ('lose-life-respawn', 'B05', 'campaign', 1728, 'Last health ball lost: fade to navy, "Ouch! 2 lives left", respawn at the gate.', 'The gate is cleared of chickens before the respawn.'),
 ('mega-kill', 'B05', 'campaign', 1795, 'A grenade kills four chickens in one frame: MEGA KILL!, kill counter 0 to 4.', 'Same rule as the Unity audio manager: three or more in one frame window.'),
 ('death-effects', 'B05', 'campaign', 1800, 'Feathers, a dark-red splatter that fades, and screen shake on every death.', 'The juice is all code: particles and tweens, no animation files.'),
 ('kills-dont-clear', 'B05', 'campaign', 2400, 'After 10 kills the egg counter still reads 1 / 5.', 'The objective is eggs; the kill counter is only a score.'),
 ('egg-collect', 'B06', 'campaign', 2645, 'Touching a nest: sparkle, +1 EGG, the counter ticks.', 'Pickup is a 62 px radius, so a jump past a nest still counts.'),
 ('court-cleared', 'B06', 'campaign', 2894, 'The fifth egg shows COURT CLEARED! with kills, eggs and lives.', 'Remaining chickens burst into feathers so the win reads cleanly.'),
 ('next-arena', 'B06', 'campaign', 2996, 'Next Arena loads arena 2.', 'Totals carry in the GameState autoload.'),
 ('pause-resume', 'B07', 'campaign', 3083, 'Esc shows TIME OUT; Resume continues.', 'The world node is pausable; the HUD and overlay keep processing.'),
 ('pause-main-menu', 'B07', 'campaign', 3305, 'Pause → Main Menu returns to the title.', 'Leaving mid-arena keeps the campaign position.'),
 ('continue-button', 'B07', 'campaign', 3395, 'The menu shows Continue: Arena 2; clicking it loads arena 2.', 'Continue appears only while a campaign is active past arena 1.'),
 ('arena-2', 'B08', 'campaign', 3500, 'Sunset Rooftops: 3 pipes, orange tint, 6 eggs; cleared with 2 lives.', 'More pipes and a faster spawn rate are the whole difficulty change.'),
 ('arena-3', 'B09', 'campaign', 4100, 'Fowl Play Finals: 4 pipes, navy tint, 7 eggs, 4-hit chickens; cleared on the last life.', 'The closest the scripted run came to losing.'),
 ('claim-trophy', 'B09', 'campaign', 4752, 'The final card reads Claim the Trophy and opens the victory screen.', 'Same overlay, different label on the last arena.'),
 ('victory-screen', 'B10', 'campaign', 4780, 'CHAMPION! YOU KILLED: 013 · EGGS: 18, with Play Again and Main Menu.', 'The totals are summed across arenas.'),
 ('campaign-ends', 'B10', 'campaign', 4965, 'Back at the menu, no Continue button.', 'The victory screen finishes the campaign.'),
 ('briefing-skip', 'B11', 'defeat', 112, 'Esc skips the briefing straight to arena 1.', 'Returning players never have to read it again.'),
 ('gamepad', 'B11', 'defeat', 244, 'Synthetic joypad events: left stick walks, right stick aims, RT fires, A jumps.', 'Same actions as the keyboard, bound in code.'),
 ('gamepad-pause', 'B11', 'defeat', 315, 'Start pauses and resumes.', 'Pause is one action with keyboard and pad bindings.'),
 ('restart-key', 'B12', 'defeat', 419, 'R reloads the arena immediately.', 'reload_current_scene: the cheapest possible restart.'),
 ('three-lives', 'B12', 'defeat', 759, 'Walking into the flock without firing costs three lives with fade-respawns.', 'Each life is three touches; invulnerability prevents instant chains.'),
 ('defeat-screen', 'B13', 'defeat', 972, 'GAME OVER: THE FLOCK WON ARENA 1. RUN IT BACK?', 'The defeat screen names the arena you lost.'),
 ('retry-arena', 'B13', 'defeat', 1119, 'Retry Arena reloads arena 1 with three lives.', 'Retry restarts the arena, not the campaign.'),
 ('how-to-play-esc', 'B14', 'extras', 107, 'Esc on How to Play returns to the menu.', 'Esc is the universal back key.'),
 ('drop-through', 'B14', 'extras', 363, 'On a platform, S + Space falls through it to the ground.', 'Platform collisions are switched off for 0.25 s.'),
 ('alt-fire-keys', 'B15', 'extras', 472, 'Held F fires; G throws a grenade.', 'Keyboard-only play is possible.'),
 ('gamepad-grenade-jetpack', 'B15', 'extras', 545, 'Pad LB throws a grenade; RB burns jetpack fuel.', 'Every action has a pad binding.'),
 ('restart-button', 'B15', 'extras', 687, 'Pause → Restart Arena reloads the court.', 'Same reload as the R key.'),
 ('quit', 'B15', 'extras', 860, 'Pause → Main Menu → Quit; the game process exits with code 0.', 'The take ends just before the click; the exit code is the evidence.'),
]

NOT_SHOWN = [
 ('fullscreen-toggle', 'F11 / Alt+Enter toggle fullscreen in game_state.gd; not captured, because a mode change would break the fixed 3840x2160 capture window.'),
 ('play-again', 'The victory screen\'s Play Again button starts a new campaign; not clicked (Main Menu was).'),
 ('exit-game-defeat', 'The defeat screen\'s Exit Game calls the same get_tree().quit as Quit; not clicked.'),
 ('game-audio', '13 sounds and a music loop exist; game audio was not captured. The film carries narration only.'),
]


def bookends():
    head = [
     dict(id='B00', act='ASK', pattern='ClaudeComposerAsk',
      narration=("Hola, this is Liam, in for Bear. Hand Walker a design document, and this is the kind of prompt it "
                 "expects. This one is reconstructed, not a transcript. What came back is a playable Godot game, and "
                 "this film plays every feature of it, with a script at the controls."),
      props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · WALKTHROUGH', segment='Every Feature, Played',
                 command=ASK, runningText='illustrative reconstruction — not the historical prompt',
                 output=['Built: 3 arenas, 8 scenes, 2,408 lines of GDScript.',
                         'Played here: 3 scripted-input takes, 76 of 76 assertions passing.'],
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B01', act='BLUF', pattern='BrutalistHesitantWriter', lead=0.8, tail=1.5,
      narration=("Basketball Blaster is an arena shooter. Mister Block fires basketballs at chickens across three "
                 "arenas, and he wins by collecting eggs, not by racking up kills. Everything you'll see was played by "
                 "a script, not a person."),
      props=dict(text=("Basketball Blaster\nis a basketball game.\nMr. Block fires basketballs\nat chickens in three arenas,\n"
                       "and wins by collecting eggs."),
                 triggerWords='a basketball game', replacementWords='an arena shooter', fontSize=96,
                 lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
                 seed='basketball-walkthrough-2026-10', ink='#3D3929', accent='#D97757', bg='#FAF9F5',
                 face='serif', align='center', brandLabel='@NikBearBrown')),
    ]
    tail = [
     dict(id='B16', act='VERDICT', pattern='ClaudeVerdictArtifact',
      narration=("Verdict. Everything implemented was played and seen working: three arenas, every move and weapon, "
                 "pause, continue, defeat, retry, victory and quit. Two defects are on screen: the click that never "
                 "continues, and HUD hints drawn over their own bars. And one design question: rushing eggs beats "
                 "fighting. Whether any of it is fun is a person's call. Nobody has played it yet."),
      props=dict(artifactTitle='Verdict', artifactHeading='Plays end to end, unjudged', brandLabel='@NikBearBrown',
                 artifactLines=['Seen working: 3 arenas, every move and weapon, pause, continue, defeat, retry, victory, quit.',
                                'Defects: click-to-continue is dead · HUD hints overlap their bars.',
                                'Design question: rushing the eggs beats fighting the flock.',
                                'Not shown: F11 fullscreen, Play Again. Not judged: fun — 0 human playtests.'])),
     dict(id='B17', act='HANDOFF', pattern='ClaudeComposerAsk',
      narration=("Your turn. Paste this into Claude in your own Godot project: Use Walker on my Godot game. Write an "
                 "input-only capture script that plays one feature through real key and mouse events, asserts what "
                 "should happen on screen, and fails loudly if it doesn't. Then tell me one thing the capture can't "
                 "prove. That last part matters: a script that wins is not a player who had fun. Liam, in for Bear."),
      props=dict(greeting='Your turn.', topic='WALKER · YOUR TURN', segment='Capture One Feature',
                 command=("Use Walker on my Godot game. Write an input-only capture script that plays one feature through "
                          "real key and mouse events, asserts what should happen on screen, and fails loudly if it "
                          "doesn't. Then tell me one thing the capture can't prove."),
                 runningText='paste this into Claude…',
                 output=['Look for: inputs, not teleports.', 'Look for: an honest limit, written down.'],
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B18', act='OUTRO', pattern='ClaudeTitleOutro', tail=1.0,
      narration=f'{TITLE}. At Nik Bear Brown.',
      props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
    ]
    return head, tail


CONTRAST_REG = [{'label': 'disclosure strip text', 'box': [0.05, 0.905, 0.58, 0.952]}]
CONTRAST_REASON = 'Gameplay beat: the frame is the real engine render (dark navy menus, pause and fade screens are game art), scaled to 90 % above a dark disclosure strip. Whole-frame sampling takes the strip as background and the game as ink. Our own essential text, the disclosure strip, is measured in its own region; the game pixels are evidence, not typography.'
QC_CLIP = {'full_bleed': True, 'full_bleed_reason': ('The engine frame (scaled to 3456x1944) runs to the top edge '
           'by design: real game pixels, not a title card. Our disclosure strip sits inside title-safe; the game HUD '
           'at the top of the frame is game UI.')}
QC_WRITER = {'sparse_by_design': True, 'sparse_reason': ('Hesitant writer: text is typed on screen over the '
             'narration, so mid-beat samples legitimately show a partial page. The finished text fills the safe '
             'area and holds for the last 1.5 s.')}


def author():
    head, tail = bookends()
    beats = []
    for spec in head + CLIPS + tail:
        b = {'beat_id': spec['id'], 'act': spec.get('act', 'BODY'), 'narration_text': spec['narration'],
             'voice': 'am_onyx', 'engine': 'kokoro',
             'estimated_duration_s': round(len(spec['narration'].split()) / 3.3, 1)}
        if 'take' in spec:
            b['shot'] = {'type': 'SCREEN', 'source': 'own', 'treatment': 'none', 'capture': spec['take'],
                         'type_note': "engine capture of the game's own UI; GATE T pixel checks exempt (see BUILD-LOG.md); overlays verified by eye",
                         'method': 'scripted-input',
                         'show': [{'at': 0.0, 'event': f"real gameplay, take '{spec['take']}', build 8f86cc8"}]}
            b['qc'] = QC_CLIP
        else:
            b['shot'] = {'type': 'GRAPHIC', 'source': 'remotion',
                         'remotion': {'pattern': spec['pattern'], 'props': dict(spec['props'])},
                         'show': [{'at': 0.0, 'event': spec['pattern']}]}
            if spec['pattern'] == 'BrutalistHesitantWriter':
                b['qc'] = QC_WRITER
        if spec.get('act') == 'OUTRO':
            b['kind'] = 'outro_voice'
            b['tail_silence_s'] = 1.0
        if spec.get('lead'):
            b['lead_silence_s'] = spec['lead']
        beats.append(b)
    sheet = {'metadata': {
        'slug': SLUG, 'title': TITLE, 'topic': 'WALKER · GODOT · WALKTHROUGH', 'skill': 'godot-waikthrough',
        'modifier': 'walker', 'channel': 'claude-liam', 'brand': 'claude-liam', 'persona': 'Liam (in for Bear)',
        'in_for_bear': True, 'voice': 'am_onyx', 'voice_kokoro': 'am_onyx', 'engine': 'kokoro',
        'palette': 'claude', 'register': 'Teardown', 'fps': 30, 'width': 3840, 'height': 2160,
        'aspect_ratio': '16:9', 'fit': 'crop', 'captions': False, 'caption_policy': 'none',
        'greeting_language': 'Spanish (Hola)',
        'audience': "makers following the channel's Claude + Walker game workflows",
        'game_build': {'commit': None, 'snapshot_sha256': rk.BUILD_ID,
                       'engine': 'Godot 4.7.2.stable.official.ed1daf0bf'},
        'note': ('godot-waikthrough walker film. Every gameplay beat is an exact-frame window of a scripted-input take '
                 'of the real game; no human playtest. Game audio was not captured; narration only. No paid calls, no upload.'),
        'tags': ['Walker', 'Godot 4', 'arena shooter', 'gameplay walkthrough', 'Claude', 'Kokoro'],
    }, 'beats': beats}
    (REEL / 'beat_sheet.json').write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
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
            n = spec['end'] - spec['start']
            segs = [('play', spec['start'], n)]
            if need > n:
                segs.append(('hold', need - n))
            info = rk.cut_segments(take, segs, REEL / f'media/{bid}.mp4')
            total = info['frames'] / rk.FPS
            rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
            b['audio_file'] = f'audio/beat-{bid}.wav'
            b['actual_duration_s'] = total
            b['shot']['clip'] = info
            b['shot']['evidence_media'] = f'media/{bid}.mp4'
            windows[bid] = (take, (spec['start'], spec['end']))
            held = sum(s['output_frames'] for s in info['segments'] if s['kind'] == 'hold')
            if held:
                print(f'{bid}: {held} held frames ({held / 30:.1f}s) — narration outran the window')
            continue
        total = rk.frames_for(lead + speech + spec.get('tail', 0.0) + (0.4 if b['act'] == 'VERDICT' else 0.25)) / rk.FPS
        rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
        b['audio_file'] = f'audio/beat-{bid}.wav'
        b['actual_duration_s'] = total
        b['shot']['remotion']['props']['durationSeconds'] = total
    captures = {}
    for take in sorted({t for t, _ in windows.values()}):
        for suffix in ('.mp4', '-inputs.jsonl'):
            shutil.copy2(rk.TAKES / f'{take}{suffix}', REEL / f'capture/{take}{suffix}')
        captures[take] = {'path': f'capture/{take}.mp4', 'sha256': rk.sha256(REEL / f'capture/{take}.mp4'),
                          'build_id': rk.BUILD_ID, 'method': 'scripted-input',
                          'input_log': f'capture/{take}-inputs.jsonl',
                          'note': 'unmodified game code; harness window config only (see CAPTURE.md)'}
    features = []
    for fid, bid, take, action, obs, riff in FEATURES:
        t, (w0, w1) = windows[bid]
        assert t == take, (fid, t, take)
        if not w0 < action < w1:
            raise SystemExit(f'{fid}: action frame {action} outside {bid} window {w0}-{w1}')
        features.append({'id': fid, 'status': 'implemented', 'evidence': [{
            'capture': take, 'beat_id': bid, 'start_s': round(w0 / 30, 3), 'action_s': round(action / 30, 3),
            'end_s': round(w1 / 30, 3), 'observation': obs, 'riff': riff}]})
    coverage = {'schema_version': 1, 'game': {'name': 'basketball-blaster-fowl-play', 'build_id': rk.BUILD_ID},
                'captures': captures, 'features': features,
                'not_exercised': [{'id': k, 'reason': v} for k, v in NOT_SHOWN]}
    (REEL / 'coverage.json').write_text(json.dumps(coverage, indent=1, ensure_ascii=False) + '\n')
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    for b in sheet['beats']:
        print(f"{b['beat_id']:4} {b['act']:8} {b['actual_duration_s']:7.2f}s  speech {b['kokoro_duration_s']:6.2f}s")
    print('total', round(sum(b['actual_duration_s'] for b in sheet['beats']), 1), 's;',
          len(FEATURES), 'features shown,', len(NOT_SHOWN), 'not exercised')


if __name__ == '__main__':
    {'author': author, 'finish': finish}[sys.argv[1]]()
