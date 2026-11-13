SLUG = 'claude-liam-stage-runner-gdd'
TITLE = 'Stage Runner: The Design Document Came Last'

ASK_COMMAND = ('Please use Walker to convert my game design document about a vertical shooter — fly a wisp up three '
               'ruined city streets, shoot the monster army marching down at you, and defeat the Cerberus at the city '
               'gate — into a playable Godot project.')

BEATS = [
 dict(id='B00', act='ASK', kind='composer',
  narration=("Hola, this is Liam, in for Bear. This is how Walker is meant to be asked: hand it a game design document, "
             "get back a playable Godot project. The prompt on screen is a reconstruction, not a transcript, because this "
             "game was rebuilt first, and its document came after."),
  props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · GDD', segment='The Design Document',
             command=ASK_COMMAND, runningText='illustrative reconstruction — not the historical prompt',
             output=['What happened: a two-stage Unity shooter was rebuilt in Godot first.',
                     'GDD.md was written afterwards, from the evidence.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B01', act='BLUF', kind='writer', lead=0.8, tail=1.5,
  narration=("Stage Runner came before its design document. It rebuilds a two-stage Unity shooter where one touch ended "
             "the game, and finishes it with lives, drops and a boss. The document was written last, and nothing in it "
             "is signed off."),
  props=dict(text=("Stage Runner\nwas built from its design document.\n"
                   "It finishes a Unity shooter\nwith a third stage and a boss.\n"
                   "The document was written last,\nand nothing in it is signed off."),
             triggerWords='was built from', replacementWords='came before',
             fontSize=92, lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
             seed='stage-runner-gdd-2026-11', ink='#3D3929', accent='#D97757', bg='#FAF9F5', face='serif',
             align='center', brandLabel='@NikBearBrown')),
 dict(id='B02', act='BODY', kind='board', status='comparison',
  sections=['Status vocabulary', '1. Metadata'], lines=(8, 8),
  narration=("The document opens by separating six kinds of claim: recovered from the Unity code, invented for the rebuild, "
             "built, observed, proposed, or still waiting on a person. Built: fourteen scripts and a shader. Observed: "
             "the game's own playtest passes, and sixty-two assertions pass in this film's three scripted takes. Human "
             "playtests: zero."),
  props=dict(title='How the Document Labels a Claim', section='Status vocabulary · 1. Metadata',
             status='COMPARISON · built ≠ observed ≠ approved',
             visualLabel="Labels from the GDD's six-term vocabulary", layout='cards',
             cards=[{'label': 'Source · Authored', 'text': 'recovered from the Unity C#, or new in the rebuild'},
                    {'label': 'Implemented', 'text': '14 GDScript files + 1 shader, 2,210 lines'},
                    {'label': 'Observed', 'text': "the game's playtest passes · 62 film-capture assertions"},
                    {'label': 'Pending', 'text': '0 human playtests · no section signed off'}]),
  cues=['recovered from', 'Built:', 'Observed:', 'Human']),
 dict(id='B03', act='BODY', kind='board', status='pending',
  sections=['2. Vision', '3. Pillars (PROPOSED)'], lines=(37, 37),
  narration=("The vision is a proposal: fly a lone wisp up three ruined streets, thin out an army that keeps marching, and "
             "win the city back from the Cerberus. Who it's for is left open. The three pillars are read off the code: "
             "always firing, the street keeps coming, and one mistake costs while three end it."),
  props=dict(title='A Vision Nobody Signed', section='2. Vision · 3. Pillars',
             status='PROPOSED vision · audience PENDING', layout='cards',
             visualLabel='Pillars, proposed from the code',
             cards=[{'label': 'Always firing', 'text': 'fire is held: the choice is where to stand'},
                    {'label': 'The street keeps coming', 'text': 'spawns speed up as you score'},
                    {'label': 'One mistake costs', 'text': '3 lives · invulnerability · mercy rule'}]),
  cues=['The vision', 'always firing', 'the street', 'one mistake']),
 dict(id='B04', act='BODY', kind='clip', status='observed', sections=['4. Core loop (IMPLEMENTED, OBSERVED)'],
  take='campaign', segments=[('play', 350, 75), ('play', 880, 90), ('play', 1325, 90), ('play', 1430, 80)], lead=0.3,
  narration=("Here's the core loop on the real build, played by a script, not a person. The countdown. Hold fire and line "
             "up under the army; kills become points. At the goal, stage clear, and the card totals the run. Every step is "
             "a cut from one take, in order.")),
 dict(id='B05', act='BODY', kind='board', status='proposed',
  sections=['5. Player-experience goals (PROPOSED, all PENDING a human playtest)'], lines=(61, 62),
  narration=("Four experience goals, all proposed, each with a test a person has to run. The captures can only hint. The "
             "script cleared stage one in thirty-one seconds of play and stage two in thirty-eight, without losing a "
             "life. But it sees every monster's position, every frame. That's not a first-time player."),
  props=dict(title='Goals Nobody Has Tested', section='5. Player-experience goals',
             status='PROPOSED · 4 goals · all PENDING a playtest', layout='cards',
             visualLabel='What the scripted run can and cannot say',
             cards=[{'label': 'PX-01 · stage 1 on try one or two', 'text': 'script: 30.9 s, 0 hits, but it sees everything'},
                    {'label': 'PX-02 · a step up, not a wall', 'text': 'script: stage 2 in 38.3 s, 0 hits'}]),
  cues=['The captures', 'But it sees']),
 dict(id='B06', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(70, 70),
  narration=("Movement is a straight port. Unity moved at five units a second, and one unit is seventy-two pixels, so the "
             "wisp moves at three hundred and sixty. What changed is the box: Unity clamped to the whole camera, the "
             "rebuild to a six hundred and forty pixel street. And holding Shift, new, halves the speed."),
  props=dict(title='Same Speed, Narrower Street', section='M-01 · Movement and focus',
             status='SOURCE vs IMPLEMENTED', layout='cards',
             visualLabel='Unity source vs. the Godot rebuild',
             cards=[{'label': 'Unity · Main Char.cs', 'text': 'moveSpeed 5 · clamped to the camera'},
                    {'label': 'Godot · player.gd', 'text': '360 px/s in a 640 px street · focus at half speed'}]),
  cues=['Unity moved', 'What changed', 'And holding']),
 dict(id='B07', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='campaign', segments=[('play', 558, 150)], lead=0.3,
  narration=("Focus, in play. Shift held, the wisp slows, and a white dot marks the hitbox: a circle of radius thirteen "
             "inside a sixty-four pixel sprite. Fire is J, at Unity's rate: one shot every fifth of a second.")),
 dict(id='B08', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(96, 96),
  narration=("Unity's enemy script had one set of defaults: three health, a hundred points, one unit a second. Every other "
             "value lived in prefabs that never arrived. So the rebuild authored thirteen monsters, from two to six health "
             "and sixty-two to a hundred and ninety-five pixels a second, with four ways to move."),
  props=dict(title='One Script, Thirteen Monsters', section='M-03 · The army',
             status='SOURCE defaults · AUTHORED roster', layout='cards',
             visualLabel='Where the numbers came from',
             cards=[{'label': 'Unity · Enemy.cs', 'text': '3 HP · 100 points · speed −1 (72 px/s)'},
                    {'label': 'Rebuild · enemy.gd TYPES', 'text': '13 types · 2–6 HP · fall, weave, hop, hunt'}]),
  cues=["Unity's enemy", 'So the rebuild']),
 dict(id='B09', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='campaign', segments=[('play', 1760, 270)], lead=0.3,
  narration=("Stage two's army, live: a monster every seven tenths of a second, the interval from Unity's own stage-two "
             "script. Its roster weaves, sprints and hunts the wisp, and the green ooze takes six hits.")),
 dict(id='B10', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(100, 100),
  narration=("In Unity, one touch was the whole game: show the game-over screen, and stop time. The rebuild gives three "
             "lives a stage. A hit flashes the street red and gives one point six seconds of invulnerability, and a mercy "
             "rule clears every fireball, so one hit never chains into the next."),
  props=dict(title='One Touch Was the Whole Game', section='M-04 · Lives, hits and drops',
             status='SOURCE vs AUTHORED', layout='cards',
             visualLabel='Unity behaviour vs. the rebuild',
             cards=[{'label': 'Unity · Main Char.cs', 'text': 'first touch: game over, timeScale 0'},
                    {'label': 'Rebuild', 'text': '3 lives · 1.6 s invulnerable · fireballs cleared on a hit'}]),
  cues=['In Unity', 'The rebuild gives', 'and a mercy']),
 dict(id='B11', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='defeat', segments=[('play', 185, 185), ('play', 470, 60)], lead=0.3,
  narration=("The failure path, on purpose: the script flies into monsters without firing. Red flash, a heart goes dark, "
             "the wisp blinks. The third touch, and game over, with Unity's crying face. Try Again reloads the stage.")),
 dict(id='B12', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='extras', segments=[('play', 1440, 45), ('play', 1950, 75)], lead=0.3,
  narration=("Drops are rolled per kill. A heart can only drop while a life is missing. Here, after one deliberate hit, a "
             "monster drops one, and the wisp collects it: plus one life, three hearts again.")),
 dict(id='B13', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(112, 112),
  narration=("The goals are a quiet gap. Unity's game manager checks the score against a goal score, but that number was "
             "set in the editor, and the scene files never arrived. So two thousand and four thousand are the rebuild's "
             "choices, not recovered values. The document says so."),
  props=dict(title='Goals Nobody Wrote Down', section='M-05 · Stages and goals',
             status='SOURCE logic · AUTHORED values', layout='cards',
             visualLabel='What the source does and does not say',
             cards=[{'label': 'Unity · GameManager.cs', 'text': 'score ≥ goalScore → next scene'},
                    {'label': 'Rebuild', 'text': 'goals 2000 · 4000 · the Cerberus'}]),
  cues=["Unity's game manager", 'So two thousand']),
 dict(id='B14', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(116, 116),
  narration=("The boss is new. A hundred and ten health, five thousand points. It walks in shielded, then repeats four "
             "attacks: an aimed fan, a ring, another fan, and two minions. At half health it's enraged: faster, with wider "
             "fans and fuller rings."),
  props=dict(title='A Boss Unity Never Had', section='M-06 · The Cerberus',
             status='AUTHORED · OBSERVED in take campaign', layout='cards',
             visualLabel='From boss.gd',
             cards=[{'label': 'Cycle', 'text': 'fan of 5 → ring of 12 → fan of 5 → 2 minions'},
                    {'label': 'Enraged at ≤ 55 HP', 'text': 'every 0.95 s · fans of 7 · rings of 16'}]),
  cues=['A hundred', 'It walks in', 'At half health']),
 dict(id='B15', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='campaign', segments=[('play', 3130, 60), ('play', 3225, 110), ('play', 3735, 75), ('play', 4005, 70)], lead=0.3,
  narration=("In the take: the walk-in, with shots absorbed. A fan, then a ring of fireballs. Enraged at fifty-five health. "
             "And victory, thirty seconds after go, with all three lives left.")),
 dict(id='B16', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(126, 126),
  narration=("Menus port Unity's buttons, with one change on purpose. Unity's restart always went back to stage one. The "
             "rebuild restarts the stage you're on. It adds keys: Escape or P to pause, M for sound, and R to restart from "
             "a menu. That last one has a bug."),
  props=dict(title='Restart Means This Stage', section='M-07 · Menus, pause and scenes',
             status='SOURCE vs IMPLEMENTED', layout='cards',
             visualLabel='Unity behaviour vs. the rebuild',
             cards=[{'label': 'Unity · UI Manager.cs', 'text': 'RestartGame() loads StageOne'},
                    {'label': 'Rebuild · game.gd', 'text': 'restart reloads the current stage'}]),
  cues=["Unity's restart", 'The rebuild restarts', 'It adds keys']),
 dict(id='B17', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='extras', segments=[('play', 955, 120)], lead=0.3,
  narration=("Escape, then R. On screen, the stage simply restarts. In the log, Godot reports a script error at line six "
             "oh six: the restart call has already removed the scene, so the next line has no viewport.")),
 dict(id='B18', act='BODY', kind='board', status='implemented',
  sections=['7. World (AUTHORED)', '8. Art and audio'], lines=(138, 138),
  narration=("The world is one painted street per stage, scrolling down, with a mirrored copy so the seam always matches. "
             "The art is the source folder's: three paintings, a bullet, a crying face, a pack of pixel monsters. The "
             "sound isn't. Unity had an audio source and no audio files, so all of it was synthesized."),
  props=dict(title='Painted Streets, Synthesized Sound', section='7. World · 8. Art and audio',
             status='AUTHORED world · art from the source folder', layout='cards',
             visualLabel='What the folders supplied',
             cards=[{'label': 'World', 'text': 'scrolling street + mirrored copy · 70, 95, 45 px/s'},
                    {'label': 'Audio', 'text': 'none in the source · 15 effects, 3 loops synthesized'}]),
  cues=['The world', 'The art', 'The sound']),
 dict(id='B19', act='BODY', kind='board', status='implemented',
  sections=['9. UI (IMPLEMENTED)', '10. Out of scope', '11. Technical'], lines=(170, 170),
  narration=("Under the hood, every scene is thin. A stage scene file is seven lines; it sets one number. Eight seconds "
             "into stage one, the running stage holds a hundred and thirteen nodes, all built in code. Out of scope, by "
             "decision: more stages, difficulty settings, online scores."),
  props=dict(title='Seven Lines, 113 Nodes', section='9. UI · 10. Out of scope · 11. Technical',
             status='IMPLEMENTED · scope set by the rebuild', layout='cards',
             visualLabel='Measured from the running game (tree_probe.txt)',
             cards=[{'label': 'stage_1.tscn', 'text': '7 lines → 113 live nodes at 8 s'},
                    {'label': 'Out of scope', 'text': 'more stages · difficulty settings · online scores'}]),
  cues=['every scene is thin', 'Eight seconds', 'Out of scope']),
 dict(id='B20', act='BODY', kind='board', status='pending',
  sections=['12. Risks and known defects', '13. Acceptance tests (OBSERVED)', '14. Provenance', '15. Open questions (PENDING)'],
  lines=(181, 181),
  narration=("The risks section is candid. Nobody has played this by hand, and the Windows build has never run. The "
             "capture found the restart error, and one mismatch: the comment says monsters spawn within four and a half "
             "units of centre, but the code uses two hundred and eighty-eight pixels, which is four. Five open questions "
             "remain for a person."),
  props=dict(title='What a Person Still Has to Decide', section='12 · 13 · 14 · 15',
             status='PENDING · 5 open questions · 0 human playtests', layout='cards',
             visualLabel='Found while making the films',
             cards=[{'label': 'R-01 · R on the pause menu', 'text': 'SCRIPT ERROR at game.gd:606; restart still works'},
                    {'label': 'R-04 · spawn range', 'text': 'comment: ±4.5 units · code: ±288 px = 4 units'}]),
  cues=['The capture', 'the comment says']),
 dict(id='B21', act='VERDICT', kind='verdict',
  narration=("Verdict. This document organizes; it doesn't approve. The loop runs end to end on real input, from the menu "
             "to the boss, and to defeat and retry. The rebuild's own additions are labelled. One script error and one "
             "wrong comment slipped past the game's own test. What's left is a person's call: the audience, the goals, "
             "and whether stage two is fair."),
  props=dict(artifactTitle='Verdict', artifactHeading='Organized, not approved', brandLabel='@NikBearBrown',
             artifactLines=['Observed end to end: menu → 3 stages → Cerberus → credits; and contact → game over → retry.',
                            "Checks: the game's playtest passes · 62 film-capture assertions pass.",
                            'Found: R on the pause menu logs a script error; the spawn comment says 4.5 units, the code 4.',
                            'Pending a person: audience, goal scores, boss health, 0 playtests.'])),
 dict(id='B22', act='HANDOFF', kind='composer',
  narration=("Your turn. Paste this into Claude with your own design document: Here is my game's design document. Pick one "
             "proposed experience goal. Rewrite it as a hypothesis with a test I can run with three players, and tell me "
             "which result would make me change the design. If no result would change your mind, it isn't a hypothesis "
             "yet. Liam, in for Bear."),
  props=dict(greeting='Your turn.', topic='WALKER · YOUR TURN', segment='Test One Design Hypothesis',
             command=("Here is my game's design document. Pick one proposed experience goal. Rewrite it as a hypothesis "
                      "with a test I can run with three players, and tell me which result would make me change the design."),
             runningText='paste this into Claude…',
             output=['Look for: a measurement, not an opinion.', 'Look for: a result that would change the design.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B23', act='OUTRO', kind='outro', tail=1.0,
  narration=f'{TITLE}. At Nik Bear Brown.',
  props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
]
