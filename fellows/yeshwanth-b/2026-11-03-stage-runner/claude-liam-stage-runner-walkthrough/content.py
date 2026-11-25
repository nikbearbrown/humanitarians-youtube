SLUG = 'claude-liam-stage-runner-walkthrough'
TITLE = 'Stage Runner: Every Feature, Played'

ASK = ('Please use Walker to convert my game design document about a vertical shooter — fly a wisp up three '
       'ruined city streets, shoot the monster army marching down at you, and defeat the Cerberus at the city '
       'gate — into a playable Godot project.')

GREETING_NARR = ("Hola, this is Liam, in for Bear. This is how Walker is meant to be asked: a game design document in, "
                 "a playable Godot project out. The prompt is a reconstruction. This game was a two-stage Unity "
                 "shooter, rebuilt in Godot and finished with a third.")
OUTPUT = ['Built: 3 stages, 13 monster types and a boss, 14 scripts.',
          'Played here: 3 scripted-input takes, 62 of 62 assertions passing.']

BLUF_NARR = ("Stage Runner is a vertical shooter: three streets, a monster army, a boss at the gate. Every feature "
             "here is played through real key, mouse and gamepad input, by a script. Nobody has played it by hand yet.")
BLUF_PROPS = dict(text=("Stage Runner\nis a twin-stick shooter.\nThree streets and a boss."),
                  triggerWords='a twin-stick shooter', replacementWords='a vertical shooter',
                  seed='stage-runner-walkthrough-2026-11')

CLIPS = [
 dict(id='B02', take='campaign', start=0, end=320, lead=0.3,
  narration=("It opens on the main menu: best score zero, the first street drifting behind it. How to Play lays out "
             "the goal, the controls and the two drops, and Escape steps back.")),
 dict(id='B03', take='campaign', start=320, end=558, lead=0.3,
  narration=("Start Game. Stage one, Ruined Street: three, two, one, go. W A S D moves, and J, Unity's own key, "
             "fires.")),
 dict(id='B04', take='campaign', start=558, end=740, lead=0.3,
  narration=("Hold Shift to focus: half speed, and a white dot marks the small hitbox.")),
 dict(id='B05', take='campaign', start=740, end=1100, lead=0.3,
  narration=("A kill can drop a pickup. This one is a triple shot: three bullets in a fan for ten seconds, counted "
             "down on the right. Monsters flash white when hit, and burst into their points.")),
 dict(id='B06', take='campaign', start=1100, end=1416, lead=0.3,
  narration=("The goal is two thousand points, and the army spawns faster as you close in. At exactly two "
             "thousand: stage clear, and the wisp flies off the top of the street.")),
 dict(id='B07', take='campaign', start=1416, end=1700, lead=0.3,
  narration=("The clear card totals it: two thousand points, eighteen monsters. Go to Stage 2, Overgrown Avenue, "
             "where the army comes three times as fast.")),
 dict(id='B08', take='campaign', start=1700, end=2300, lead=0.3,
  narration=("This stage is played with the arrow keys and Space, to show both bindings. A monster arrives every "
             "seven tenths of a second, and the types get tougher: spiders and slimes that weave, wolves that "
             "sprint, scorpions and rats that hunt your position, and oozes that take six hits.")),
 dict(id='B09', take='campaign', start=2300, end=2874, lead=0.3,
  narration=("Four thousand to clear. Triple shots stack up near the end, and the autopilot never loses a life. "
             "That says more about a script that sees every position than about the difficulty. Stage clear, at "
             "four thousand and fifty.")),
 dict(id='B10', take='campaign', start=2874, end=3200, lead=0.3,
  narration=("Stage three, the Gatekeeper, is the first street again, at dusk. The Cerberus walks in shielded: "
             "every shot is absorbed until it arrives.")),
 dict(id='B11', take='campaign', start=3200, end=3720, lead=0.3,
  narration=("Then it attacks on a cycle: an aimed fan of five fireballs, a ring of twelve, another fan, then two "
             "minions. Its health bar runs across the top of the street. The wisp threads the gaps and keeps "
             "firing.")),
 dict(id='B12', take='campaign', start=3720, end=4097, lead=0.3,
  narration=("At half health it's enraged: attacks come faster, fans widen to seven, rings to sixteen. A last run "
             "of hits, and it bursts. Victory, and five thousand points.")),
 dict(id='B13', take='campaign', start=4097, end=4549, lead=0.3,
  narration=("The credits scroll up and stop: a final score of twelve thousand two hundred and fifty, and "
             "fifty-eight monsters. Back on the main menu, the best score is saved.")),
 dict(id='B14', take='defeat', start=0, end=353, lead=0.3,
  narration=("Now the failure path, in a second take. The script steers into monsters on purpose, without firing. "
             "Each touch costs a life, flashes the street red and empties a heart. The third ends the stage.")),
 dict(id='B15', take='defeat', start=353, end=877, lead=0.3,
  narration=("Game over, with Unity's crying face and the score against the goal, and the game paused underneath. "
             "Try Again reloads the stage with three lives and a score of zero. Escape pauses: Resume, Restart "
             "Stage, Audio, and Main Menu.")),
 dict(id='B16', take='extras', start=0, end=433, lead=0.3,
  narration=("A third take covers the other inputs. On the menu, the audio button turns the music off and back on. "
             "In play, the arrow keys move and Z fires, the third fire key.")),
 dict(id='B17', take='extras', start=433, end=690, lead=0.3,
  narration=("The left mouse button fires too. M toggles sound at any time: the panel reads Sound: Off, then On.")),
 dict(id='B18', take='extras', start=690, end=1080, lead=0.3,
  narration=("P pauses, and the pause menu has its own audio button. Resume. Then Escape, and R restarts the stage. "
             "It works, but the game logs a script error: line six oh six runs after its scene is already gone.")),
 dict(id='B19', take='extras', start=1080, end=1419, lead=0.3,
  narration=("Now a simulated gamepad. The left stick steers, A fires, the left bumper focuses, and Start pauses "
             "and resumes.")),
 dict(id='B20', take='extras', start=1419, end=2176, lead=0.3,
  narration=("Last, the heart. The script takes one deliberate hit: two lives. Then it plays normally until a heart "
             "drops, which only happens while a life is missing. A triple shot comes first, then the heart, and "
             "three lives again. Escape, Main Menu.")),
]

FEATURES = [
 ('main-menu', 'B02', 'campaign', 50, 'Main menu with Start Game, How to Play, Audio On, Quit and BEST SCORE 0.',
  'An empty save shows a zero best score; it is the only persistent state.'),
 ('how-to-play', 'B02', 'campaign', 104, 'How to Play opens: goal, controls, drops.', 'Everything a player needs is one page.'),
 ('escape-back', 'B02', 'campaign', 257, 'Esc on How to Play returns to the main menu.', 'The pause action doubles as back.'),
 ('start-game', 'B03', 'campaign', 327, 'Start Game loads stage 1.', 'New run: run score and kills reset.'),
 ('stage-intro', 'B03', 'campaign', 380, 'STAGE 1, Ruined Street, then 3, 2, 1, GO!', 'A countdown before any monster spawns.'),
 ('move-fire-keys', 'B03', 'campaign', 450, 'WASD moves; holding J fires.', "J is Unity's original fire key."),
 ('focus', 'B04', 'campaign', 600, 'Holding Shift halves speed and shows the hitbox dot.', 'Focus trades speed for precision.'),
 ('triple-shot', 'B05', 'campaign', 762, 'A triple shot drop is collected; three-way fire and the timer bar.', 'Drops are random; this seed gave two early.'),
 ('kills-score', 'B05', 'campaign', 901, 'Monsters flash white when hit and burst into +points.', 'Score feedback appears at the kill.'),
 ('stage-1-goal', 'B06', 'campaign', 1338, 'At 2000 points: STAGE CLEAR!, the wisp flies off the top.', 'The goal check is Unity GameManager logic.'),
 ('stage-clear-card', 'B07', 'campaign', 1450, 'Stage clear card: stage score 2000, run total, 18 monsters.', "Unity's FinishStageOne scene, reused."),
 ('go-to-stage-2', 'B07', 'campaign', 1564, 'Go to Stage 2 loads Overgrown Avenue.', 'The card leads into the next stage.'),
 ('arrows-space', 'B08', 'campaign', 1750, 'Stage 2 played with the arrow keys and Space.', 'Both key sets are bound.'),
 ('stage-2-army', 'B08', 'campaign', 2000, 'Faster spawns and tougher, weaving and hunting monsters.', 'The 0.7 s interval comes from ArmyStage2.cs.'),
 ('stage-2-goal', 'B09', 'campaign', 2796, 'Stage 2 clears at 4050 of 4000.', 'Overshoot comes from multi-kills.'),
 ('boss-entry-shield', 'B10', 'campaign', 3150, 'The Cerberus walks in while shots are absorbed.', 'Shielded while entering.'),
 ('boss-attacks', 'B11', 'campaign', 3300, 'Aimed fans, rings of fireballs and summoned minions; boss bar at the top.', 'A repeating four-step cycle.'),
 ('boss-enrage', 'B12', 'campaign', 3739, 'Enraged at 55 HP: faster, wider attacks.', 'Below half health.'),
 ('victory', 'B12', 'campaign', 4019, 'The Cerberus bursts: VICTORY!, +5000.', 'Stage 3 ends the run.'),
 ('credits', 'B13', 'campaign', 4200, 'Credits scroll and stop over the restored city; Main Menu.', "Thanks.cs scroll speed, 150 px/s."),
 ('best-score', 'B13', 'campaign', 4500, 'Main menu now shows BEST SCORE 12250.', 'Saved to the capture copy only.'),
 ('contact-hit', 'B14', 'defeat', 209, 'Touching a monster costs a life, a red flash and an emptied heart.', 'Deliberate contacts, not a dodge failure.'),
 ('game-over', 'B14', 'defeat', 319, 'Third contact: the wisp explodes; the stage is over.', 'Lives replace Unity one-touch death.'),
 ('game-over-menu', 'B15', 'defeat', 400, 'GAME OVER with the crying face and Score 0 /2000; tree paused.', "Unity's game-over face."),
 ('try-again', 'B15', 'defeat', 501, 'Try Again restarts stage 1 with 3 lives and score 0.', 'Retry resets the stage only.'),
 ('pause-esc', 'B15', 'defeat', 735, 'Esc opens PAUSED: Resume, Restart Stage, Audio On, Main Menu.', 'Pause stops the tree.'),
 ('pause-main-menu', 'B15', 'defeat', 825, 'Main Menu from the pause menu.', 'Back to the start.'),
 ('menu-audio-toggle', 'B16', 'extras', 69, 'The menu audio button switches between Audio On and Audio Off.', 'AudioController.PauseAndResume port.'),
 ('arrows-z', 'B16', 'extras', 320, 'Arrow keys move; Z fires.', 'Z is not listed on the HUD.'),
 ('mouse-fire', 'B17', 'extras', 445, 'Holding the left mouse button fires.', 'Not listed on the HUD either.'),
 ('m-sound', 'B17', 'extras', 565, 'M toggles sound; the HUD reads Sound: Off (M).', 'A global key handled by GameState.'),
 ('p-pause', 'B18', 'extras', 693, 'P pauses.', 'Second pause key.'),
 ('pause-audio', 'B18', 'extras', 768, 'Audio button inside the pause menu toggles.', 'Same toggle as the main menu.'),
 ('resume', 'B18', 'extras', 898, 'Resume closes the pause menu.', 'Unpauses the tree.'),
 ('r-restart', 'B18', 'extras', 1002, 'R on the pause menu restarts the stage; a SCRIPT ERROR is logged at game.gd:606.', 'Works, with an error.'),
 ('pad-move-fire', 'B19', 'extras', 1100, 'Left stick moves; A fires.', 'Synthetic joypad events, no real controller.'),
 ('pad-focus', 'B19', 'extras', 1205, 'LB focuses: the hitbox dot appears.', 'Pad focus binding.'),
 ('pad-start-pause', 'B19', 'extras', 1325, 'Start pauses and Start resumes.', 'Pad pause binding.'),
 ('deliberate-hit', 'B20', 'extras', 1459, 'One contact: lives 3 → 2.', 'Set up for the heart.'),
 ('heart', 'B20', 'extras', 1994, 'A heart drop is collected: lives back to 3, +1 LIFE.', 'Hearts drop only while a life is missing.'),
]

NOT_SHOWN = [
 ('fullscreen', 'F11 / Alt+Enter toggles fullscreen; not captured, because it would change the fixed capture window.'),
 ('quit', 'The Quit button was not clicked.'),
 ('play-again', 'Play Again on the credits screen was not clicked; Main Menu was.'),
 ('boss-game-over', "Game over in stage 3 ('The Cerberus still guards the gate.') was not captured."),
 ('focus-loss-pause', 'The game pauses when its window loses focus; seen only in a discarded pilot.'),
 ('game-audio', 'The game has synthesized music and sound effects; game audio was not captured. Narration only.'),
]

VERDICT_NARR = ("Verdict. Every implemented feature but six was played through real input, and sixty-two assertions "
                "pass. One defect: R on the pause menu logs a script error, though the restart works. What a script "
                "can't tell you is whether stage two is fair, or whether the boss is fun. That's a person's call.")
VERDICT_LINES = ['Observed: menus → 3 stages → boss → credits; and contact → game over → retry.',
                 'Checks: 62 of 62 film-capture assertions pass; the game\'s own playtest passes.',
                 'Defect: R on the pause menu logs a SCRIPT ERROR (game.gd:606).',
                 'Untested: a human playtest, Windows, fullscreen, game audio.']
