SLUG = 'claude-liam-fantasy-walkthrough'
TITLE = 'Fantasy Survival Crafting: Every Feature, Played'

ASK = ('Please use Walker to convert my game design document about a first-person survival-crafting game — '
       'wake in an abandoned valley, gather sticks, gold and stone, craft an axe and a campfire, and survive '
       'one night until dawn — into a playable Godot project.')

CLIPS = [
 dict(id='B02', take='day', start=0, end=318, lead=0.3,
  narration=("It opens on a sunrise sky: New Game, How to Play and Quit, and no Load Game yet, because there's no save. "
             "How to Play lists the controls and seven survival rules.")),
 dict(id='B03', take='day', start=318, end=661, lead=0.3,
  narration=("New Game starts a three-page story: the first night. You wake by an abandoned village, nights are bitter, "
             "and the plan is axe, logs, stones, fire.")),
 dict(id='B04', take='day', start=661, end=1143, lead=0.3,
  narration=("Day one, half past seven. A look around the village. The inventory is twenty-one empty slots, and crafting "
             "shows the axe it can't make yet. Pressing one says craft an axe first. Then the orchard: E shakes an apple "
             "loose from a tree.")),
 dict(id='B05', take='day', start=1143, end=1828, lead=0.3,
  narration=("West to the pine grove. Aim at a stick, its name appears under the crosshair, and E picks it up, with a popup "
             "each time. Three sticks, and a mushroom on the way. The objective list ticks itself, and the calories bar "
             "drops as he walks.")),
 dict(id='B06', take='day', start=1828, end=2484, lead=0.3,
  narration=("Gold glints next to the split ore rocks by the standing stones: three nuggets. Three stones lie nearby. "
             "Then C for crafting: the Tools tab, three gold and three sticks owned, and the Craft button appears. "
             "One click, an axe, and one to equip it.")),
 dict(id='B07', take='day', start=2484, end=3264, lead=0.3,
  narration=("Back to the pines. With the axe equipped, the prompt counts the hits left. Four swings, and the tree topples "
             "away from him, leaving a stump and two logs. Then a second pine. Four logs. Watch the objective counters: "
             "the sticks and gold are ticked, but now read zero of three.")),
 dict(id='B08', take='day', start=3264, end=3572, lead=0.3,
  narration=("Crafting again, the Survival tab: four logs and three stones make a campfire. Then a rabbit. It bolts, "
             "he sprints after it, one hit, and it leaves meat.")),
 dict(id='B09', take='day', start=3572, end=4205, lead=0.3,
  narration=("To the lake. Wading in, aim at the water, and E drinks: water back to a hundred. He tries to place the fire "
             "facing the lake, and the game refuses: you can't build a fire in the water. A few steps inland, and a "
             "right-click on the campfire lights it.")),
 dict(id='B10', take='day', start=4205, end=4722, lead=0.3,
  narration=("Now the recipe that needs a fire: cooked meat. In the inventory, hovering shows an item's description, a drag "
             "moves one to the last slot, and right-click eats: cooked meat, an apple, a mushroom.")),
 dict(id='B11', take='day', start=4722, end=5170, lead=0.3,
  narration=("M pauses. Settings, back, then Save Game and Save: one slot, written. Resume.")),
 dict(id='B12', take='night', start=0, end=500, lead=0.3,
  narration=("A new take continues from that save. Load Game is on the menu now, and it puts him back at one in the "
             "afternoon, at the fire. Then the long wait for night.")),
 dict(id='B13', take='night', start=4600, end=5333, lead=0.3,
  narration=("Skip ahead nearly six hours. The sky turns to sunset, the light goes, and at eight: night falls, stay by "
             "your fire. By the fire, he's warm. He saves again, for the next take.")),
 dict(id='B14', take='night', start=5333, end=6061, lead=0.3,
  narration=("E at the fire: you rest by the fire, and the night runs nine times faster. Dawn breaks on day two: sixteen "
             "items, two trees, one rabbit. Back at the menu, Load Game is waiting.")),
 dict(id='B15', take='defeat', start=0, end=433, lead=0.3,
  narration=("The failure path, from the night save. A controller, simulated: the right stick looks, Y opens the "
             "inventory. Then he walks away from the fire. You are freezing.")),
 dict(id='B16', take='defeat', start=433, end=1175, lead=0.3,
  narration=("N is Unity's own debug-damage key: ten health a press. The cold takes the rest, a point every one point four "
             "seconds, and the health bar starts to pulse.")),
 dict(id='B17', take='defeat', start=1175, end=1551, lead=0.3,
  narration=("Lost to the wilds: you froze in the night. Load Save puts him back at the fire, alive. Then the menu.")),
]

# (feature id, beat, take, action frame, observation, riff)
FEATURES = [
 ('main-menu', 'B02', 'day', 40, 'Sunrise menu with New Game, How to Play and Quit; no Load Game on an empty save folder.', 'Load Game only appears once a save exists.'),
 ('how-to-play', 'B02', 'day', 130, 'How to Play lists 11 controls and 7 survival rules.', 'The same controls are in the README.'),
 ('intro-story', 'B03', 'day', 450, 'Three intro pages, each advanced with Continue.', 'The story sets the deadline before play starts.'),
 ('first-look', 'B04', 'day', 700, 'Captured-mouse look around the village at 07:30.', 'Look is relative mouse motion, clamped in pitch.'),
 ('inventory-window', 'B04', 'day', 840, 'I opens a 21-slot inventory and frees the cursor.', 'Windows stop look and selection while open.'),
 ('crafting-window', 'B04', 'day', 910, 'C shows the Axe recipe at 3 Gold [0], 3 Stick [0], no Craft button.', 'The button only exists when the recipe is affordable.'),
 ('equip-without-axe', 'B04', 'day', 990, 'Pressing 1 without an axe shows "Craft an axe first [C]".', 'A refusal that teaches the next step.'),
 ('apple-tree', 'B04', 'day', 1101, 'E on an orchard tree adds an Apple.', 'Each tree holds three apples, saved with the game.'),
 ('look-and-pick-up', 'B05', 'day', 1455, 'The stick name appears under the crosshair; E collects it with a pickup popup.', 'Reach is 4 m from the screen centre.'),
 ('objectives', 'B05', 'day', 1700, 'The objective list ticks "Gather 3 Sticks".', 'Objectives refresh twice a second from the inventory.'),
 ('calories-drain', 'B05', 'day', 1600, 'Calories fall while walking (100 to 76 by 09:07).', 'One calorie per 5 m walked.'),
 ('gold-near-ore', 'B06', 'day', 1915, 'Gold nuggets lie beside the split ore rocks.', 'A placement hint, not a marker.'),
 ('stones', 'B06', 'day', 2116, 'Three stones picked up near the standing stones.', 'Stones also ring the lake.'),
 ('craft-axe', 'B06', 'day', 2389, 'Tools tab; Craft Axe consumes 3 Gold + 3 Stick.', 'The Unity recipe, kept.'),
 ('equip-axe', 'B06', 'day', 2452, 'Key 1 equips the axe; it appears in the hand and the HUD.', 'Right-click in the inventory also equips.'),
 ('chop-pine', 'B07', 'day', 2683, 'Four left-click swings fell a pine; the prompt counts hits left.', 'Uses the swing and chop sounds Unity declared.'),
 ('logs-drop', 'B07', 'day', 2862, 'A felled pine leaves a stump and two spinning Logs.', 'Dropped items spin; placed ones do not.'),
 ('objective-counter-defect', 'B07', 'day', 3000, 'Ticked objectives read "(0/3)" after the axe consumed the sticks and gold.', 'Counters read the current inventory, not what was gathered.'),
 ('craft-campfire', 'B08', 'day', 3343, 'Survival tab; Craft Campfire consumes 4 Log + 3 Stone.', 'Authored recipe; no Unity counterpart.'),
 ('hunt-rabbit', 'B08', 'day', 3478, 'A rabbit flees; one axe hit plays its Dead clip and drops meat.', 'Seen in motion, which the GDD lists as unreviewed (R-04).'),
 ('drink-lake', 'B09', 'day', 3787, 'Aiming at the lake and pressing E restores water to 100.', 'The lake is a ray target, not a pickup.'),
 ('fire-in-water-refused', 'B09', 'day', 3872, '"You can\'t build a fire in the water"; the campfire stays in the inventory.', 'The spot is 2.6 m ahead of the player.'),
 ('place-campfire', 'B09', 'day', 4152, 'Right-click the campfire on dry ground: lit, with light and particles.', 'Placing closes the inventory.'),
 ('cook-meat', 'B10', 'day', 4284, 'Cooked Meat crafts only with a campfire within 9 m.', 'The recipe checks the fire distance.'),
 ('item-info-hover', 'B10', 'day', 4420, 'Hovering a slot shows name, description and function.', 'Ported from InventoryItem.cs.'),
 ('drag-drop', 'B10', 'day', 4463, 'Dragging an item to the last slot moves it, with a preview.', 'Onto a full slot it would swap.'),
 ('eat', 'B10', 'day', 4541, 'Right-click eats Cooked Meat, Apple and Mushroom; calories 35 → 100.', 'Each effect is clamped to 100.'),
 ('pause-menu', 'B11', 'day', 4730, 'M pauses: Resume, Save Game, Settings, Main Menu, Quit Game.', 'The HUD hides while paused.'),
 ('settings-page', 'B11', 'day', 4789, 'Settings shows mouse sensitivity and volume sliders.', 'Opened, not changed.'),
 ('save-game', 'B11', 'day', 4986, 'Save Game → Save writes the one slot ("Game saved.").', 'One JSON file; saving overwrites.'),
 ('load-game', 'B12', 'night', 59, 'Load Game restores 13:09 with the fire placed.', 'Position, inventory, flags and fires come back.'),
 ('dusk-sky', 'B13', 'night', 4700, 'The sky blends to sunset and the light falls.', 'Three skybox panoramas blended by a shader.'),
 ('night-falls', 'B13', 'night', 4993, '"Night falls. Stay by your fire." at 20:00.', 'Night runs at 12 s per hour.'),
 ('warm-by-fire', 'B13', 'night', 5113, 'No cold beside the fire at night.', 'Warmth radius 9 m.'),
 ('rest-by-fire', 'B14', 'night', 5358, 'E at the fire: "You rest by the fire...", time runs 9× faster.', 'Resting skips the dull part of the night.'),
 ('victory', 'B14', 'night', 5850, 'Dawn Breaks: day 2, 16 items, 2 trees felled, 1 rabbit.', 'Victory needs dawn and a night near the fire.'),
 ('menu-load-after', 'B14', 'night', 6030, 'Back at the main menu, Load Game is offered.', 'The save outlives the run.'),
 ('gamepad', 'B15', 'defeat', 140, 'Synthetic pad: right stick looks; Y opens and closes the inventory.', 'Same actions as keyboard, bound in code.'),
 ('freezing', 'B15', 'defeat', 351, 'Away from the fire: "You are freezing!" and a blue overlay.', 'Cold damages 1 health per 1.4 s.'),
 ('debug-damage', 'B16', 'defeat', 441, 'N takes 10 health a press.', 'Kept from Unity\'s PlayerState debug key.'),
 ('low-health-pulse', 'B16', 'defeat', 900, 'Below 25 health the bar pulses.', 'A late warning.'),
 ('defeat-screen', 'B17', 'defeat', 1200, 'Lost to the Wilds: "You froze in the night", with Load Save.', 'The cause is named.'),
 ('load-save', 'B17', 'defeat', 1352, 'Load Save returns to the night save beside the fire.', 'Defeat is recoverable.'),
]

NOT_SHOWN = [
 ('fullscreen', 'F11 toggles fullscreen; not captured, because it would change the fixed capture window.'),
 ('quit', 'The Quit buttons were not clicked.'),
 ('play-again', 'Play Again on the end screens was not clicked.'),
 ('sliders', 'The Settings sliders were shown but not moved.'),
 ('other-foods', 'Red Cap, Bread and the Water Flask were not picked up or eaten.'),
 ('sprint-jump', 'Sprint and jump appear only inside movement, not as a separate demonstration.'),
 ('game-audio', 'The game has synthesized sounds and music; game audio was not captured. Narration only.'),
]

VERDICT_NARR = ("Verdict. Everything the game asks of a player was played and seen working, through real input: gather, "
                "craft, chop, hunt, drink, cook, eat, save, load, survive to dawn, and freeze to death. One display defect "
                "is on screen: ticked objectives that read zero of three. Whether one night is tense or tedious is a "
                "person's call. Nobody has played it yet.")
VERDICT_LINES = ['Seen working: gather, craft, chop, hunt, drink, cook, eat, save, load, dawn and defeat.',
                 'Defect: ticked objectives read 0/3 once a recipe uses the materials.',
                 'Shown honestly: a fire in the water is refused.',
                 'Not judged: fun, tension, tuning. 0 human playtests.']
GREETING_NARR = ("Hola, this is Liam, in for Bear. Hand Walker a design document, and this is the kind of prompt it expects. "
                 "This one is reconstructed, not a transcript. What came back is a playable Godot game, and this film plays "
                 "every feature of it, with a script at the controls.")
BLUF_NARR = ("Fantasy Survival Crafting is a race against the clock. You gather and craft through one afternoon in an "
             "abandoned valley, light a fire before dark, and survive until dawn. Everything you'll see was played by a "
             "script, not a person.")
BLUF_PROPS = dict(text=("Fantasy Survival Crafting\nis a crafting game.\nGather, craft, light a fire,\n"
                        "and survive one night."),
                  triggerWords='a crafting game', replacementWords='a race against the clock')
OUTPUT = ['Built: a 260 m valley, 23 scripts, one night to survive.',
          'Played here: 3 scripted-input takes, 74 of 74 assertions passing.']
