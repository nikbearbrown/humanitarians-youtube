SLUG = 'claude-liam-knife-throw-gdd'
TITLE = 'Gino: Knife Throw, The Design Document Came Last'

ASK_COMMAND = ('Please use Walker to convert my game design document about a 2D action platformer — guide Gino home '
               'through three hostile valleys with a sword combo, three throwing knives and three hearts — into a '
               'playable Godot project.')

BEATS = [
 dict(id='B00', act='ASK', kind='composer',
  narration=("Hola, this is Liam, in for Bear. This is how Walker is meant to be asked: hand it a game design document, "
             "get back a playable Godot project. The prompt on screen is a reconstruction, not a transcript, because this "
             "game was rebuilt first, and its document came after."),
  props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · GDD', segment='The Design Document',
             command=ASK_COMMAND, runningText='illustrative reconstruction — not the historical prompt',
             output=['What happened: a Unity platformer with no levels was rebuilt in Godot first.',
                     'GDD.md was written afterwards, from the evidence.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B01', act='BLUF', kind='writer', lead=0.8, tail=1.5,
  narration=("Gino: Knife Throw came before its design document. Unity left forty scripts and a pack of art, but no "
             "levels, scenes or sound. The rebuild made all three levels. The document was written last, and nothing in "
             "it is signed off."),
  props=dict(text=("Gino: Knife Throw\nwas built from its design document.\n"
                   "Unity left scripts and art,\nbut no levels at all.\n"
                   "The document was written last,\nand nothing in it is signed off."),
             triggerWords='was built from', replacementWords='came before',
             fontSize=92, lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
             seed='knife-throw-gdd-2026-11', ink='#3D3929', accent='#D97757', bg='#FAF9F5', face='serif',
             align='center', brandLabel='@NikBearBrown')),
 dict(id='B02', act='BODY', kind='board', status='comparison',
  sections=['Status vocabulary', '1. Metadata'], lines=(8, 8),
  narration=("The document separates six kinds of claim: recovered from the Unity code, invented for the rebuild, built, "
             "observed, proposed, or still waiting on a person. Built: fourteen scripts and a shader. Observed: the game's "
             "playtest passes, and forty-six assertions pass in this film's three scripted takes. Human playtests: zero."),
  props=dict(title='How the Document Labels a Claim', section='Status vocabulary · 1. Metadata',
             status='COMPARISON · built ≠ observed ≠ approved',
             visualLabel="Labels from the GDD's six-term vocabulary", layout='cards',
             cards=[{'label': 'Source · Authored', 'text': 'recovered from the Unity C#, or new in the rebuild'},
                    {'label': 'Implemented', 'text': '14 GDScript files + 1 shader, 2,620 lines'},
                    {'label': 'Observed', 'text': "the game's playtest passes · 46 film-capture assertions"},
                    {'label': 'Pending', 'text': '0 human playtests · no section signed off'}]),
  cues=['recovered from', 'Built:', 'Observed:', 'Human']),
 dict(id='B03', act='BODY', kind='board', status='pending',
  sections=['2. Vision', '3. Pillars (PROPOSED)'], lines=(37, 37),
  narration=("The vision is a proposal: take Gino home through three hostile valleys with a sword, three knives and three "
             "hearts. Who it's for is left open. The pillars are read off the code: read the wind-up, commit to the combo, "
             "and knives are scarce."),
  props=dict(title='A Vision Nobody Signed', section='2. Vision · 3. Pillars',
             status='PROPOSED vision · audience PENDING', layout='cards',
             visualLabel='Pillars, proposed from the code',
             cards=[{'label': 'Read the wind-up', 'text': 'bite 0.2 s · bat orb 0.7 s · plant 0.6 s'},
                    {'label': 'Commit to the combo', 'text': '20 + 20 + 20 + 40 = 100 HP'},
                    {'label': 'Knives are scarce', 'text': '3 at most · 30 damage · refilled by daggers'}]),
  cues=['The vision', 'read the wind-up', 'commit to', 'knives are scarce']),
 dict(id='B04', act='BODY', kind='clip', status='observed', sections=['4. Core loop (IMPLEMENTED, OBSERVED)'],
  take='campaign', segments=[('play', 318, 70), ('play', 700, 140), ('play', 1985, 40), ('play', 2025, 90)], lead=0.3,
  narration=("Here's the core loop on the real build, played by a script, not a person. A level opens with its banner. A "
             "walker comes in and the sword meets it. Gino reaches the door and presses W, and the Level Complete panel "
             "totals the run. Every step is a cut from one take, in order.")),
 dict(id='B05', act='BODY', kind='board', status='proposed',
  sections=['5. Player-experience goals (PROPOSED, all PENDING a human playtest)'], lines=(61, 63),
  narration=("Four experience goals, all proposed, each with a test a person has to run. The captures can only hint. The "
             "script finished Rocky Outskirts in forty-three seconds with no hits. But it never discovered the four-hit "
             "combo, and it finished the last level on half a heart."),
  props=dict(title='Goals Nobody Has Tested', section='5. Player-experience goals',
             status='PROPOSED · 4 goals · all PENDING a playtest', layout='cards',
             visualLabel='What the scripted run can and cannot say',
             cards=[{'label': 'PX-01 · level 1 on the first try', 'text': 'script: 0:43, 0 hits, but it sees everything'},
                    {'label': 'PX-03 · the four-hit combo', 'text': 'script: never chained past 2 hits'}]),
  cues=['The captures', 'But it never']),
 dict(id='B06', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(70, 70),
  narration=("Movement changed on purpose. Unity pushed Gino with a force of fifty and about three units a second. The "
             "rebuild runs at a hundred and five pixels a second, six and a half tiles, to suit the level sizes. Coyote "
             "time and a jump buffer are new, and an early release cuts the jump."),
  props=dict(title='Faster Than Unity, on Purpose', section='M-01 · Movement',
             status='SOURCE vs IMPLEMENTED', layout='cards',
             visualLabel='Unity source vs. the Godot rebuild',
             cards=[{'label': 'Unity · PlayerController.cs', 'text': 'AddForce · speed 50 · ~3 units/s'},
                    {'label': 'Godot · player.gd', 'text': '105 px/s · coyote 0.1 s · buffer 0.12 s'}]),
  cues=['Unity pushed', 'The rebuild runs', 'Coyote']),
 dict(id='B07', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='campaign', segments=[('play', 2380, 150)], lead=0.3,
  narration=("Jumping, in play. Hold Space for the full jump, three hundred and twenty pixels a second straight up, "
             "and keep running in the air. Here the script uses the long jump to land past a walker waiting below.")),
 dict(id='B08', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(74, 74),
  narration=("The combo is Unity's: J starts a slash and further presses chain up to four. Unity's trigger dealt twenty "
             "for every hit. The rebuild makes the fourth, the magic blast, worth forty, so a full combo is exactly an "
             "enemy's hundred health. That number is the rebuild's choice."),
  props=dict(title='Four Hits, a Hundred Health', section='M-02 · Sword combo',
             status='SOURCE chain · AUTHORED finisher', layout='cards',
             visualLabel='Where the numbers came from',
             cards=[{'label': 'Unity · AttackTrigger.cs', 'text': 'dmg = 20, every hit'},
                    {'label': 'Rebuild · player.gd HITS', 'text': '20 · 20 · 20 · 40 (magic blast)'}]),
  cues=["The combo is", "Unity's trigger", 'The rebuild makes']),
 dict(id='B09', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='defeat', segments=[('play', 640, 130)], lead=0.3,
  narration=("In the takes, the script lands single slashes and two-hit chains: each hit knocks the walker back out of "
             "reach. So the four-hit chain and the magic blast never appear on screen. The game's own playtest is what "
             "checks them.")),
 dict(id='B10', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(78, 78),
  narration=("Knives come from Unity too: thrown straight, picked up as daggers, capped at three. The rebuild sets the "
             "numbers: four hundred and twenty pixels a second for one point three seconds, thirty damage, and the knife "
             "leaves a fraction of a second into the throw. Gino starts every new game with none."),
  props=dict(title='Three Knives, Thirty Damage', section='M-03 · Knives',
             status='SOURCE rules · IMPLEMENTED numbers', layout='cards',
             visualLabel='From knife.gd and pickup.gd',
             cards=[{'label': 'Unity · KnifeMove.cs', 'text': 'flies straight · cap 3 (GameMaster)'},
                    {'label': 'Rebuild · knife.gd', 'text': '420 px/s · 1.3 s · 30 damage'}]),
  cues=['Knives come', 'The rebuild sets', 'Gino starts']),
 dict(id='B11', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='campaign', segments=[('play', 1590, 160)], lead=0.3,
  narration=("K, in play. The knife leaves Gino's hand, flies straight across the screen and hits the walker for "
             "thirty. The count under the hearts drops to zero. The sword finishes the job.")),
 dict(id='B12', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(88, 88),
  narration=("Three enemies, each with a tell. The walker bites a fifth of a second after its cone fires. The bat curls "
             "into an orb for seven tenths of a second. The plant rears up. Unity's attack dealt two, a full heart. But "
             "health and points lived in prefabs that never arrived, so the hundred health and twenty-five points are authored."),
  props=dict(title='Every Enemy Has a Tell', section='M-04 · Enemies',
             status='SOURCE behaviour · AUTHORED health', layout='cards',
             visualLabel='From walker.gd, bat.gd and plant.gd',
             cards=[{'label': 'Walker · bat · plant', 'text': 'bite 0.2 s · orb 0.7 s · rear up 0.6 s'},
                    {'label': 'Unity · EnemyAttack.cs', 'text': 'dmg = 2 · prefabs not delivered'}]),
  cues=['The walker bites', 'The bat curls', "Unity's attack"]),
 dict(id='B13', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='campaign', segments=[('play', 2880, 190), ('play', 6320, 60)], lead=0.3,
  narration=("A bat in level two: a knife first, then the sword. And the plant's snap, in level three, as Gino runs "
             "past: rooted, it reaches about forty-six pixels, further than the sword.")),
 dict(id='B14', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(92, 92),
  narration=("Health is Unity's six, shown as three hearts in halves. An enemy costs a full heart, a spike half a heart, "
             "and a pit the whole level. After a hit, Gino blinks for one point one seconds. Hearts as pickups are new: "
             "the sprites were in the pack, unused."),
  props=dict(title='Six Halves, Three Hearts', section='M-05 · Health, hazards and pickups',
             status='SOURCE vs AUTHORED', layout='cards',
             visualLabel='Unity behaviour vs. the rebuild',
             cards=[{'label': 'Unity · PlayerController.cs', 'text': 'maxHealth = 6 · HeartUI halves'},
                    {'label': 'Rebuild', 'text': 'enemy 2 · spike 1 · pit = level · 1.1 s blink'}]),
  cues=['Health is', 'An enemy costs', 'After a hit', 'Hearts as']),
 dict(id='B15', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='campaign', segments=[('play', 4795, 50), ('play', 5345, 45)], lead=0.3,
  narration=("Both costs, in level three. Floor spikes: half a heart, and a knockback. Then a walker's bite: a full "
             "heart, and the blink.")),
 dict(id='B16', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='defeat', segments=[('play', 1440, 220)], lead=0.3,
  narration=("And the pit, on purpose: the script runs Gino off the edge. Gino is down, the level is lost, and Retry "
             "starts it again with the score and knives Gino entered it with.")),
 dict(id='B17', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(103, 103),
  narration=("The biggest gap: Unity delivered no levels at all. All three are text maps in a Python tool, which checks "
             "them and simulates Gino's jumps frame by frame to prove every door and diamond is reachable. Rocky "
             "Outskirts teaches, Thorn Hollow climbs, Moonlit Depths has twelve enemies."),
  props=dict(title='Three Levels Unity Never Had', section='M-06 · Levels',
             status='AUTHORED · route-simulated', layout='cards',
             visualLabel='From _tools/levels.py',
             cards=[{'label': 'Maps', 'text': 'ASCII → levels.gd + routes.json'},
                    {'label': 'Enemies per level', 'text': '5 · 7 · 12'}]),
  cues=['The biggest gap', 'All three', 'Rocky']),
 dict(id='B18', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='campaign', segments=[('play', 2190, 60), ('play', 4105, 60), ('play', 5975, 110)], lead=0.3,
  narration=("Thorn Hollow and Moonlit Depths in the take. And here's what the map check missed: level three's rope "
             "bridge stops one tile short of the rock. A sixteen pixel hole over the spikes. The route jumps it, so the "
             "check passed. A trial run fell through.")),
 dict(id='B19', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(112, 112),
  narration=("Menus port Unity's: a pause menu, a victory panel with Next Level, a game-over panel with Retry, credits. "
             "The rebuild adds Continue, How to Play, a sound key and R to restart from a menu. That last one has a "
             "bug."),
  props=dict(title='Unity Menus, Plus a Restart Key', section='M-07 · Menus, pause and scenes',
             status='SOURCE vs IMPLEMENTED', layout='cards',
             visualLabel='Unity behaviour vs. the rebuild',
             cards=[{'label': 'Unity · UI.cs, Pause.cs', 'text': 'pause · victory · game over · credits'},
                    {'label': 'Rebuild', 'text': 'Continue · How to Play · M · R restart'}]),
  cues=["Menus port", 'The rebuild adds', 'That last']),
 dict(id='B20', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='defeat', segments=[('play', 1724, 110)], lead=0.3,
  narration=("Escape, then R: the level restarts. But the log shows a script error at line seven sixty-one. The "
             "scene is already gone.")),
 dict(id='B21', act='BODY', kind='board', status='implemented',
  sections=['7. World (AUTHORED)', '8. Art and audio'], lines=(126, 126),
  narration=("The world is sixteen pixel tiles, auto-tiled from the pack's level sheet, light for the first two levels "
             "and dark for the cave. The art is the pack's. The sound isn't: Unity had a sound manager and no audio "
             "files, so twenty-three effects and three music loops were synthesized."),
  props=dict(title='Pack Art, Synthesized Sound', section='7. World · 8. Art and audio',
             status='AUTHORED world · art from the source folder', layout='cards',
             visualLabel='What the folders supplied',
             cards=[{'label': 'World', 'text': '16 px tiles · light and dark · 3 parallax layers'},
                    {'label': 'Audio', 'text': 'none in the source · 23 effects, 3 loops synthesized'}]),
  cues=['The world', 'The art', 'The sound']),
 dict(id='B22', act='BODY', kind='board', status='implemented',
  sections=['9. UI (IMPLEMENTED)', '10. Out of scope', '11. Technical'], lines=(149, 149),
  narration=("Under the hood, every scene is thin. A level scene is one node running one script with a level number, and "
             "everything else is built from the text map when it loads. Out of scope, by decision: more levels, "
             "difficulty settings, pathfinding for the bat."),
  props=dict(title='One Node per Level', section='9. UI · 10. Out of scope · 11. Technical',
             status='IMPLEMENTED · scope set by the rebuild', layout='cards',
             visualLabel='From the scenes and level.gd',
             cards=[{'label': 'level_1.tscn', 'text': 'one node · level.gd · level_id = 1'},
                    {'label': 'Out of scope', 'text': 'more levels · difficulty · bat pathfinding'}]),
  cues=['every scene is thin', 'everything else', 'Out of scope']),
 dict(id='B23', act='BODY', kind='board', status='pending',
  sections=['12. Risks and known defects', '13. Acceptance tests (OBSERVED)', '14. Provenance', '15. Open questions (PENDING)'],
  lines=(157, 157),
  narration=("The risks section is candid. Nobody has played this by hand, and the Windows build has never run. The "
             "captures found two defects the game's own test missed: the bridge hole, and the restart error. And walkers "
             "waiting under drops bite Gino in mid-air. Five open questions remain for a person."),
  props=dict(title='What a Person Still Has to Decide', section='12 · 13 · 14 · 15',
             status='PENDING · 5 open questions · 0 human playtests', layout='cards',
             visualLabel='Found while making the films',
             cards=[{'label': 'R-01 · level 3 bridge', 'text': 'a 16 px hole at x 1568–1584'},
                    {'label': 'R-02 · R on a menu', 'text': 'SCRIPT ERROR at level.gd:761'}]),
  cues=['The captures', 'And walkers']),
 dict(id='B24', act='VERDICT', kind='verdict',
  narration=("Verdict. This document organizes; it doesn't approve. The loop runs end to end on real input, from the menu "
             "through three levels to the credits, and to defeat and retry. The rebuild's own numbers are labelled. Two "
             "defects slipped past the game's own test. What's left is a person's call: the audience, the combo's "
             "damage, and whether the drops are fair."),
  props=dict(artifactTitle='Verdict', artifactHeading='Organized, not approved', brandLabel='@NikBearBrown',
             artifactLines=['Observed end to end: menu → 3 levels → credits; and pit → game over → retry.',
                            "Checks: the game's playtest passes · 46 film-capture assertions pass.",
                            'Found: a 16 px hole in level 3\'s bridge; R on a menu logs a script error.',
                            'Pending a person: audience, combo damage, drops, 0 playtests.'])),
 dict(id='B25', act='HANDOFF', kind='composer',
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
 dict(id='B26', act='OUTRO', kind='outro', tail=1.0,
  narration=f'{TITLE}. At Nik Bear Brown.',
  props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
]
