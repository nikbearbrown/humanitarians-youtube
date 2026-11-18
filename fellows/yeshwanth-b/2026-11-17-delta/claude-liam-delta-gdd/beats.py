SLUG = 'claude-liam-delta-gdd'
TITLE = 'Delta: The Design Document Came Last'

ASK_COMMAND = ('Please use Walker to convert my game design document about a first-person puzzle game — a space station '
               'folded into two layers, energy cells carried between machines, and an unstable core taken past two '
               'guardians — into a playable Godot project.')

C1, C2, D, E = 'campaign1', 'campaign2', 'defeat', 'extras'

BEATS = [
 dict(id='B00', act='ASK', kind='composer',
  narration=("Hola, this is Liam, in for Bear. This is how Walker is meant to be asked: hand it a game design document, "
             "get back a playable Godot project. The prompt on screen is a reconstruction, not a transcript, because this "
             "game was rebuilt first, and its document came after."),
  props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · GDD', segment='The Design Document',
             command=ASK_COMMAND, runningText='illustrative reconstruction — not the historical prompt',
             output=['What happened: a Unity puzzle game with no levels was rebuilt in Godot first.',
                     'GDD.md was written afterwards, from the evidence.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B01', act='BLUF', kind='writer', lead=0.8, tail=1.5,
  narration=("Delta came before its design document. Unity left sixty-four scripts and a kit of art, but no levels, "
             "scenes or sound. The rebuild made all twelve levels. The document was written last, and nothing in it "
             "is signed off."),
  props=dict(text=("Delta\nwas built from its design document.\n"
                   "Unity left scripts and art,\nbut no levels at all.\n"
                   "The document was written last,\nand nothing in it is signed off."),
             triggerWords='was built from', replacementWords='came before',
             fontSize=92, lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
             seed='delta-gdd-2026-11', ink='#3D3929', accent='#D97757', bg='#FAF9F5', face='serif',
             align='center', brandLabel='@NikBearBrown')),
 dict(id='B02', act='BODY', kind='board', status='comparison',
  sections=['Status vocabulary', '1. Metadata'], lines=(8, 8),
  narration=("The document separates six kinds of claim: recovered from the Unity code, invented for the rebuild, built, "
             "observed, proposed, or still waiting on a person. Built: twenty-seven scripts and three shaders. Observed: "
             "the game's playtest passes, and ninety assertions pass in this film's four scripted takes. Human "
             "playtests: zero."),
  props=dict(title='How the Document Labels a Claim', section='Status vocabulary · 1. Metadata',
             status='COMPARISON · built ≠ observed ≠ approved',
             visualLabel="Labels from the GDD's six-term vocabulary", layout='cards',
             cards=[{'label': 'Source · Authored', 'text': 'recovered from the Unity C#, or new in the rebuild'},
                    {'label': 'Implemented', 'text': '27 GDScript files + 3 shaders, 5,319 lines'},
                    {'label': 'Observed', 'text': "the game's playtest passes · 90 film-capture assertions"},
                    {'label': 'Pending', 'text': '0 human playtests · no section signed off'}]),
  cues=['recovered from', 'Built:', 'Observed:', 'Human']),
 dict(id='B03', act='BODY', kind='board', status='pending',
  sections=['2. Vision', '3. Pillars (PROPOSED)'], lines=(37, 37),
  narration=("The vision is a proposal: fold yourself between two layers of a broken station, carry energy where it's "
             "needed, and walk the unstable core to the stabiliser. Who it's for is left open. The pillars are read off "
             "the code: one floor plan in two layers, energy as a thing you carry, and a narrator who teaches while "
             "the level tests."),
  props=dict(title='A Vision Nobody Signed', section='2. Vision · 3. Pillars',
             status='PROPOSED vision · audience PENDING', layout='cards',
             visualLabel='Pillars, proposed from the code',
             cards=[{'label': 'One floor plan, two layers', 'text': 'Upper and Lower Delta, 50 m apart'},
                    {'label': 'Energy you carry', 'text': 'charge · drain · copy · teleport'},
                    {'label': 'The narrator teaches', 'text': "VEGA's subtitles, one device a level"}]),
  cues=['The vision', 'one floor plan', 'energy as', 'a narrator']),
 dict(id='B04', act='BODY', kind='clip', status='observed', sections=['4. Core loop (IMPLEMENTED, OBSERVED)'],
  take=C1, segments=[('play', 304, 60), ('play', 575, 45), ('play', 785, 60), ('play', 995, 120)], lead=0.3,
  narration=("Here's the core loop on the real build, played by a script, not a person. The level banner. Look at a "
             "cell, and F picks it up. Look at the socket, and E plugs it in. The door opens, the lift ends the level, "
             "and the panel shows the time. Every step is a cut from one take, in order.")),
 dict(id='B05', act='BODY', kind='board', status='proposed',
  sections=['5. Player-experience goals (PROPOSED, all PENDING a human playtest)'], lines=(61, 63),
  narration=("Four experience goals, all proposed, each with a test a person has to run. The captures can only hint. "
             "The script cleared all twelve levels without dying. But it knows every solution in advance, and it read "
             "the guardian's timers instead of the warnings. That's not a first-time player."),
  props=dict(title='Goals Nobody Has Tested', section='5. Player-experience goals',
             status='PROPOSED · 4 goals · all PENDING a playtest', layout='cards',
             visualLabel='What the scripted run can and cannot say',
             cards=[{'label': 'PX-01 · shifting by level 2', 'text': 'script: knew where to shift in advance'},
                    {'label': 'PX-03 · reading the strike warning', 'text': 'script: read the timers, not the warning'}]),
  cues=['The captures', 'But it knows']),
 dict(id='B06', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(70, 70),
  narration=("Movement is a straight port of Unity's starter first-person controller: four metres a second walking, "
             "six running, a jump of one point two metres, the same speed change rate. New: a tenth of a second of "
             "coyote time. Mouse look only works while the mouse is captured."),
  props=dict(title='The Starter Controller, Ported', section='M-01 · Movement and look',
             status='SOURCE vs IMPLEMENTED', layout='cards',
             visualLabel='Unity source vs. the Godot rebuild',
             cards=[{'label': 'Unity · FirstPersonController.cs', 'text': 'MoveSpeed 4 · Sprint 6 · JumpHeight 1.2'},
                    {'label': 'Godot · player.gd', 'text': 'same values · coyote 0.1 s · 0.11° per pixel'}]),
  cues=['Movement is', 'New:', 'Mouse look']),
 dict(id='B07', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take=E, segments=[('play', 568, 170)], lead=0.3,
  narration=("In play: the mouse turns the view left and right, Shift runs at six metres a second, and Space jumps.")),
 dict(id='B08', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(74, 74),
  narration=("Interaction is Unity's three metre ray from the camera. F picks up and drops. E uses a device, or puts a "
             "cell in or takes it out. The prompt under the crosshair names the key, and replaces Unity's outline "
             "highlight."),
  props=dict(title='One Ray, Two Keys', section='M-02 · Interaction',
             status='SOURCE ray · IMPLEMENTED keys', layout='cards',
             visualLabel='From InteractionManager.cs and player.gd',
             cards=[{'label': 'Unity · InteractionManager.cs', 'text': 'interactionDistance = 3'},
                    {'label': 'Rebuild', 'text': 'F pick up · E use · prompt under the crosshair'}]),
  cues=['Interaction is', 'F picks', 'The prompt']),
 dict(id='B09', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take=C1, segments=[('play', 2730, 190)], lead=0.3,
  narration=("The prompt in play: press E to place the energy cell. The charging station fills it, and E takes it "
             "back out.")),
 dict(id='B10', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(78, 78),
  narration=("Shifting is Unity's dimension switcher: a glitch up, fifty metres up or down with whatever you hold, and "
             "a glitch down. The rebuild adds one rule. If the other layer has no floor there, or something solid is in "
             "the way, the shift is refused. Unity would have left you stuck in a wall."),
  props=dict(title='Fifty Metres, Unless Something Is There', section='M-03 · Layer shifting',
             status='SOURCE shift · AUTHORED refusal', layout='cards',
             visualLabel='Unity behaviour vs. the rebuild',
             cards=[{'label': 'Unity · DimensionSwitcher.cs', 'text': '0.3 s glitch · ±50 m with the held item'},
                    {'label': 'Rebuild · level.gd', 'text': 'refused if no floor or something solid'}]),
  cues=['Shifting is', 'The rebuild adds', 'Unity would']),
 dict(id='B11', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take=C1, segments=[('play', 1235, 110)], lead=0.3,
  narration=("Q, in play: the glitch, and the warm light of Lower Delta, where the corridor exists.")),
 dict(id='B12', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(89, 89),
  narration=("Eleven devices come from Unity's scripts: sockets, the charging station and the discharger, doors, "
             "pressure pads, bridges and shuttles, the duplicator, the teleporter, plasma and generators. One "
             "example: the arc gate throws a charged cell back, and only a flat one passes."),
  props=dict(title='Eleven Devices, One Currency', section='M-04 · Energy devices',
             status='SOURCE devices · IMPLEMENTED', layout='cards',
             visualLabel='From the device scripts',
             cards=[{'label': 'Energy cell', 'text': '3000 capacity · 750 in, 1500 out per second'},
                    {'label': 'Arc gate', 'text': 'throws a charged cell back · a flat cell passes'}]),
  cues=['Eleven devices', 'One example']),
 dict(id='B13', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take=C2, segments=[('play', 2010, 75), ('play', 3975, 60), ('play', 4380, 75)], lead=0.3,
  narration=("Three of them in the takes. The duplicator copies the cell in its cradle. The console scans a sealed cell "
             "onto the teleporter pad, and the button sends it through the glass.")),
 dict(id='B14', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(98, 98),
  narration=("Unity's health manager reloads the scene on death, and its respawn trigger catches falls. The rebuild keeps "
             "both: fall off a deck and you're back at the checkpoint, a fallen cell goes home, and plasma or a "
             "guardian strike restarts the level."),
  props=dict(title='Falls Are Forgiven, Plasma Is Not', section='M-05 · Health and resets',
             status='SOURCE vs IMPLEMENTED', layout='cards',
             visualLabel='Unity behaviour vs. the rebuild',
             cards=[{'label': 'Unity · HealthManager.cs', 'text': 'Die() reloads · RespawnTrigger'},
                    {'label': 'Rebuild', 'text': 'checkpoint · item respawn · plasma restarts'}]),
  cues=["Unity's health", 'The rebuild keeps']),
 dict(id='B15', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take=D, segments=[('play', 1935, 75), ('play', 5130, 65), ('play', 5690, 125)], lead=0.3,
  narration=("On purpose, in the failure take: plasma, and the level restarts. A cell dropped into space, back at its "
             "spawn. And the player walking off the edge, back at the checkpoint.")),
 dict(id='B16', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(102, 102),
  narration=("The guardians keep Unity's timing: the first attack at seventeen seconds, then every twenty. A strike's "
             "sparks follow you for five seconds, lock, and three seconds later lightning kills within three metres. A "
             "shockwave ring must be jumped. The level around them is the rebuild's: two generators, a vault, a shield."),
  props=dict(title="Unity's Clock, a New Arena", section='M-06 · The guardians',
             status='SOURCE timings · AUTHORED layout', layout='cards',
             visualLabel='From BossManager.cs and final.gd',
             cards=[{'label': 'Unity · BossManager.cs', 'text': 'first at 17 s · every 20 s · follow 5 s · lock 3 s'},
                    {'label': 'Rebuild · final.gd', 'text': '2 generators · vault · shield · stabiliser'}]),
  cues=['The guardians keep', "A strike's", 'A shockwave', 'The level around']),
 dict(id='B17', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take=C2, segments=[('play', 9240, 150), ('play', 9745, 45), ('play', 13460, 180)], lead=0.3,
  narration=("In the take: a strike locks and the script gets clear. A shockwave, jumped. And a strike lured onto the "
             "shield generator, which the lightning destroys.")),
 dict(id='B18', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(121, 121),
  narration=("The biggest gap: Unity delivered no levels at all. All twelve are text maps on a five metre grid, built "
             "at runtime from the modular kit. Each introduces one idea, from a single socket in Cold Start to two "
             "guardians in Delta."),
  props=dict(title='Twelve Levels Unity Never Had', section='M-07 · Levels',
             status='AUTHORED', layout='cards',
             visualLabel='From scripts/levels.gd',
             cards=[{'label': 'Maps', 'text': 'ASCII on a 5 m grid · two layers'},
                    {'label': 'One idea each', 'text': 'Cold Start → Delta'}]),
  cues=['The biggest gap', 'All twelve', 'Each introduces']),
 dict(id='B19', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take=C2, segments=[('play', 1628, 70), ('play', 6996, 70), ('play', 8610, 80)], lead=0.3,
  narration=("Echo, Unstable, Delta: every level opens on its own banner.")),
 dict(id='B20', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(127, 127),
  narration=("Menus port Unity's pause menu, options and scene loader, and add Continue, Select level with best times, "
             "and Credits. The pause menu lists R to restart and N to skip. Both are broken, and so is the mouse."),
  props=dict(title='A Pause Menu That Ignores You', section='M-08 · Menus, pause and scenes',
             status='SOURCE vs IMPLEMENTED', layout='cards',
             visualLabel='Unity behaviour vs. the rebuild',
             cards=[{'label': 'Unity · PauseMenu.cs', 'text': 'pause · restart · next level'},
                    {'label': 'Rebuild', 'text': 'Continue · Select level · Credits · options'}]),
  cues=['Menus port', 'The pause menu']),
 dict(id='B21', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take=D, segments=[('play', 2063, 420)], lead=0.3,
  narration=("Escape pauses. A mouse click on Resume does nothing: a full-screen container for the options panel sits "
             "on top of the buttons. Arrows and Enter work. R, pressed while paused, does nothing too: the level node is "
             "paused with everything else. The menu's own Restart level works.")),
 dict(id='B22', act='BODY', kind='board', status='implemented',
  sections=['7. World (AUTHORED)', '8. Art and audio'], lines=(139, 139),
  narration=("The world is the kit on a five metre grid: indoor floors with lamps and windows onto space, outdoor decks "
             "with rails and asteroids. Upper Delta is cool, Lower Delta warm. The art is the Unity project's. The sound "
             "isn't: Unity had an audio manager and no audio files, so thirty-three effects and three music tracks were "
             "synthesized, and VEGA is subtitles."),
  props=dict(title='Kit Art, Synthesized Sound', section='7. World · 8. Art and audio',
             status='AUTHORED world · art from the source folder', layout='cards',
             visualLabel='What the folders supplied',
             cards=[{'label': 'World', 'text': '5 m grid · two tinted layers · outdoor decks'},
                    {'label': 'Audio', 'text': 'none in the source · 33 effects, 3 music tracks synthesized'}]),
  cues=['The world', 'The art', 'The sound']),
 dict(id='B23', act='BODY', kind='board', status='implemented',
  sections=['9. UI (IMPLEMENTED)', '10. Out of scope', '11. Technical'], lines=(159, 159),
  narration=("Under the hood, every level scene is one node running one script with a level number; the station, "
             "devices and power links are built from the text map. Out of scope, by decision: Unity's outline "
             "highlights and audio-reactive effects, and voiced narration."),
  props=dict(title='One Node per Level', section='9. UI · 10. Out of scope · 11. Technical',
             status='IMPLEMENTED · scope set by the rebuild', layout='cards',
             visualLabel='From the scenes and level.gd',
             cards=[{'label': 'level_01.tscn', 'text': 'one node · level.gd · level_id = 1'},
                    {'label': 'Out of scope', 'text': 'outlines · audio-reactive objects · voice'}]),
  cues=['every level scene', 'Out of scope']),
 dict(id='B24', act='BODY', kind='board', status='pending',
  sections=['12. Risks and known defects', '13. Acceptance tests (OBSERVED)', '14. Provenance', '15. Open questions (PENDING)'],
  lines=(166, 166),
  narration=("The risks section is candid. The captures found what the game's own test missed: the pause menu ignores "
             "clicks, its keys are dead while paused, a player on a moving shuttle creeps forward, and Continue logs an "
             "engine error. The playtest never paused, and steered the player directly. Five questions remain for a "
             "person."),
  props=dict(title='What a Person Still Has to Decide', section='12 · 13 · 14 · 15',
             status='PENDING · 5 open questions · 0 human playtests', layout='cards',
             visualLabel='Found while making the films',
             cards=[{'label': 'R-01 · pause menu', 'text': 'clicks never reach the buttons'},
                    {'label': 'R-02 · while paused', 'text': 'R, N and Esc do nothing'}]),
  cues=['The captures', 'The playtest']),
 dict(id='B25', act='VERDICT', kind='verdict',
  narration=("Verdict. This document organizes; it doesn't approve. The loop runs end to end on real input, through "
             "twelve levels, the guardians and the ending, and through the failures. The rebuild's own levels and layout "
             "are labelled. Four defects slipped past the game's own test. What's left is a person's call: the "
             "audience, voiced narration, and whether level twelve is fair."),
  props=dict(artifactTitle='Verdict', artifactHeading='Organized, not approved', brandLabel='@NikBearBrown',
             artifactLines=['Observed end to end: menu → 12 levels → ending → credits; and plasma, falls, pause.',
                            "Checks: the game's playtest passes · 90 film-capture assertions pass.",
                            'Found: pause ignores clicks; R/N/Esc dead while paused; shuttle creep; Continue error.',
                            'Pending a person: audience, narration, level 12 fairness, 0 playtests.'])),
 dict(id='B26', act='HANDOFF', kind='composer',
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
 dict(id='B27', act='OUTRO', kind='outro', tail=1.0,
  narration=f'{TITLE}. At Nik Bear Brown.',
  props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
]
