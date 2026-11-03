# Fantasy Survival Crafting — three films — Yeshwanth Balaji

Three films about **Fantasy Survival Crafting**. It is a Godot 4.7.2 rebuild of a partial Unity first-person survival-crafting prototype, completed into a one-night survival game. Each film was made with a Brutalist Godot skill, run with the `walker` modifier.

| Film | Skill | Landscape | Vertical |
|---|---|---|---|
| Fantasy Survival Crafting: The Design Document Came Last | godot-gdd walker | 3840×2160, 5:57 | 2160×3840 |
| Fantasy Survival Crafting: Every Feature, Played | godot-waikthrough walker | 3840×2160, 6:05 | 2160×3840 |
| Fantasy Survival Crafting: Inside the Godot Code | godot-gamedev walker | 3840×2160, 6:08 | 2160×3840 |

This folder is the recipe only: the GDD, scripts and records. The videos are on Drive.

## This week's contribution

**Question.** What does the finished game actually do, how is it built, and what would its design document say? Can the films show that honestly, with no human playtest done yet?

**Built.**

- **Verified the game in the engine.**
  - The game's own tests pass on an isolated copy: `_tools/playtest` 32/32 and `_tools/playtest_load` 10/10.
  - The exported macOS app boots (headless, 300 frames, exit 0).
  - The Windows `.exe` was not run.
- **Three scripted-input captures of the real build,** at native 4K, 30 fps. They were played only through key, mouse and joypad events: no teleports and no game method calls. 74 of 74 assertions pass.
  - `day`: new game through crafting the axe and campfire, hunting, drinking, cooking and eating, then Save Game.
  - `night`: Load Game, dusk by the fire, rest, and dawn.
  - `defeat`: walk away from the fire, freeze, then Load Save.
- **`GDD.md`,** written after the game from the folders' evidence. Every claim is labelled SOURCE / AUTHORED / IMPLEMENTED / OBSERVED / PROPOSED / PENDING, and nothing is signed off.
- **Three films,** each pairing claims with real engine footage of the same build (`build_id a514438`).
  - The walkthrough shows 43 features and lists the 7 it did not exercise.

**Observed.** The captures and probes found things a quick play would miss:

- **Objective counters.** Once a recipe consumes its materials, the ticked objectives read "[x] Gather 3 Sticks (0/3)". Gold, Logs and Stones do the same. The counters show the current inventory, not what was gathered (`world.gd:759-773`).
- **Built in code.** `game.tscn` is 6 lines, and it becomes 1,976 live nodes at runtime (`captures/tree_probe.txt`). All 6 scenes are thin; `world.gd` builds the valley.
- **Unity leftovers.** The N debug-damage key from the Unity source still ships. Unity declared swing and chop sounds that no script played; the rebuild uses them.
- **Survival pacing.** By day the clock runs 24 s per game hour, by night 12 s, and 9× faster while resting. Calories fell from 100 to 35 by 12:47 in the day take, and three meals restored them.

**Next experiment.** A human playtest of the four proposed experience goals (GDD §5), starting with PX-01 ("a first-time player places the campfire before 20:00 without reading How to Play").

## Human and AI work

**My decisions:**

- the game, and the request for the same three-film set as the basketball submission;
- that the game is not modified;
- where the films and submissions go, and that nothing is published from the toolkit.

**AI tools and voices:**

- Claude (Claude Code) wrote the GDD, the capture driver, beat sheets, narration and these records, and ran the renders.
- Narration is the AI voice "Liam" (Kokoro `am_onyx`, local), named in the narration. It is not a recording of me.

**Rejected or corrected during the build:**

- The GDD film's calorie claim was rewritten from the day take's log: lowest 35, at 12:47.
- The GDD film's out-of-scope card now matches GDD §10 ("Multiple save slots").
- Three GDD excerpt panels were narrowed to the lines the narration covers, after a frame review found them running into the footer.
- Two walkthrough clip boundaries moved by 8 frames, so the pause-menu press and the first debug-damage press fall inside the clips that narrate them. Footage was never retimed.
- Two earlier 4K capture attempts stopped drawing when macOS covered the window. They were discarded (`captures/CAPTURE.md`).

**Unverified:**

- No human playtest.
- The Windows export was never run.
- These were not captured:
  - F11 fullscreen, the Quit buttons, Play Again and the settings sliders;
  - Red Cap, Bread and the Water Flask;
  - sprint-jump as a separate demonstration.
- Game audio was not captured; the films carry narration only.
- YouTube 4K processing has not been checked.

## Reproduce

| Item | Value |
|---|---|
| Brutalist version | brutalist.art at `22264a3` |
| Game source | `fantasy-survival-crafting-godot/` (not a git repo), snapshot `build_id a5144381d771f6311baea35f13239d9812457fd52f69997470b3bbde908cc82d` (446 files; method in `captures/CAPTURE.md`); Godot 4.7.2.stable.official.ed1daf0bf |
| Captures | `captures/CAPTURE.md` (method, isolated copy, overlays), `capture_driver.gd` (built from `core.gd` + `survival.gd` + `takes.gd` by `assemble.sh`), `run_take.sh`, `record_all.sh`, input logs `*-inputs.jsonl`. The capture MP4s (3.5 GB) stay in the local working folder `youtube/fantasy-captures/takes/`; their hashes are in `CAPTURE.md` |
| Each film | `make_sheet.py` (author → Kokoro → finish), then `BUILD-PROMPT.md`. Verticals: `captures/make_vertical_all.sh gdd\|walkthrough\|gamedev` |
| Checks | `./art godot-gdd --check` PASS (16 sections, 11 excerpts) · `godot-waikthrough --check` PASS (43 features, 7 not exercised) · `godot-gamedev --check` PASS (13 code→result pairs). GATE T PASS and Gate V clean on all six masters; frames reviewed by eye |
| Approvals | none claimed; every GDD section is PENDING |

## Watch and review

| Video | Drive link | Size | Duration | SHA-256 |
|---|---|---|---|---|
| GDD, landscape (`fantasy-gdd_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 357.0 s | `62c936776e7cf4f2e1ba9a9e48376feff03dd0c04f068e0135aff01f6fb23d64` |
| Walkthrough, landscape (`fantasy-walkthrough_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 364.7 s | `53735a9cb7165fe0bff8ab38db72a5b46437483669d8754cbe3be4bcbdffbc05` |
| Gamedev, landscape (`fantasy-gamedev_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 367.6 s | `fb8c408ae155de4634d364d786fa45f4e9d383930234a24fb15bfef4df35bb21` |
| GDD, vertical (`fantasy-gdd_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 357.0 s | `be1e7a855b66da642dca7879ac537797abe86425cd681bc792970a144f7314db` |
| Walkthrough, vertical (`fantasy-walkthrough_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 364.7 s | `f37c569017e2fba26b8ba2b880200c5ce9bf7962bc9a027b1984843efdaecaea` |
| Gamedev, vertical (`fantasy-gamedev_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 367.6 s | `a11774de335ec8d1541fe3ab059583ae9449afa030f94a061e4baa75fa343c48` |

**How the verticals were made.** They are native 9:16, not crops. Narration and timing are identical to landscape.

- **Gameplay:** re-cut in portrait from the same source frames, with the game at full width.
- **Boards and code panels:** redrawn as large-type portrait cards (`captures/portrait_cards.py`, `make_vertical_cards.py`). Quotes are verified verbatim against the GDD, and code lines are exact source lines.
- **Composer, writer and outro:** the toolkit's 916 compositions.

| Review step | Status |
|---|---|
| PM review | pending |
| YouTube 4K processing check | pending upload |
| Professors' publication decision | pending |
