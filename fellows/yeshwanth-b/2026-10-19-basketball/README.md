# Basketball Blaster: Fowl Play — three films — Yeshwanth Balaji

Three films about **Basketball Blaster: Fowl Play**, a Godot 4.7.2 port of a Unity 2D arena shooter, extended to three arenas. Each film was made with a Brutalist Godot skill, run with the `walker` modifier.

| Film | Skill | Landscape | Vertical |
|---|---|---|---|
| Basketball Blaster: The Design Document Came Last | godot-gdd walker | 3840×2160, 6:08 | 2160×3840 |
| Basketball Blaster: Every Feature, Played | godot-waikthrough walker | 3840×2160, 5:12 | 2160×3840 |
| Basketball Blaster: Inside the Godot Code | godot-gamedev walker | 3840×2160, 7:03 | 2160×3840 |

This folder is the recipe only: the GDD, source, scripts and records. The videos are on Drive.

## This week's contribution

**Question.** What does the finished game actually do, how is it built, and what would its design document say? Can the films show that honestly, with no human playtest done yet?

**Built.**

- **Verified the game in the engine.**
  - All 8 scenes load and run with no script errors.
  - The exported macOS app boots (headless, exit 0).
  - The Windows `.exe` was not run.
- **Three scripted-input captures of the real build**, at native 4K, played only through keyboard, mouse and gamepad events. 76 of 76 assertions pass.
  - `campaign`: all three arenas cleared, victory.
  - `defeat`: three lives lost, then retry.
  - `extras`: drop-through, alternate keys, pad buttons, Restart Arena, Quit.
- **`GDD.md`,** written from the folder's evidence. Every claim is labelled SOURCE / README / AUTHORED / IMPLEMENTED / OBSERVED / PROPOSED / PENDING, and nothing is signed off.
- **Three films,** each pairing claims with real engine footage of the same build (`build_id 8f86cc8`).

**Observed.** The captures and probes found things a quick play would miss:

- **D-01.** The briefing says "ENTER / CLICK TO CONTINUE", but clicking never works. A full-screen shade `ColorRect` swallows every click; Enter and Esc work.
- **D-02.** The HUD hints "RMB / G" and "SHIFT" sit under their bars. The bars measure 80×34 px at runtime, against the 14 px the code asks for.
- **Eggs beat fighting.** The autopilot cleared each arena in 12.6 / 13.6 / 18.7 s. Fighting in place for 25.6 s earned 10 kills and no eggs.
- **Ported and authored.** Unity declared a jetpack input and never read it; the port wired it up. Coyote time and fire rate were retuned (0.5 → 0.15 s and 0.5 → 0.4 s).
- **Unused files.** Six images and one font ship but are never used. The project has no automated tests.

**Next experiment.** A human playtest of the four proposed experience goals (GDD §5), starting with PX-02 ("each arena feels harder") and PX-03 ("fighting is worthwhile").

## Human and AI work

**My decisions:**

- the game and the request for the same three-film set as the tower-defense submission;
- that the game is not modified;
- where the films and submissions go, and that nothing is published from the toolkit.

**AI tools and voices:**

- Claude (Claude Code) wrote the GDD, the capture driver, beat sheets, narration and these records, and ran the renders.
- Narration is the AI voice "Liam" (Kokoro `am_onyx`, local), named in the narration. It is not a recording of me.

**Rejected or corrected during the build** (see each `BUILD-LOG.md`):

- GDD numbers taken from debugging dry runs were replaced with the recorded take's numbers.
- Four clips had narration re-ordered or delayed to match the action; footage was never retimed.
- Five GDD boards dropped their embedded game stills after the text-size gate flagged the game's own UI text.

**Unverified:**

- No human playtest.
- The Windows export was never run.
- F11 fullscreen, Play Again and the defeat screen's Exit Game were not captured.
- Game audio was not captured; the films carry narration only.
- YouTube 4K processing has not been checked.

## Reproduce

| Item | Value |
|---|---|
| Brutalist version | brutalist.art at `22264a3` |
| Game source | `basketball-game-godot-completed/` (not a git repo), snapshot `build_id 8f86cc812e234160bb7f95e65f7150d29662426a460f387d9a7ed77fd59248d5` (188 files; method in `captures/CAPTURE.md`); Godot 4.7.2.stable.official.ed1daf0bf |
| Captures | `captures/CAPTURE.md` (method, isolated copy, overlays), `capture_driver.gd`, `run_take.sh`, input logs `*-inputs.jsonl`. The capture MP4s (262 MB) stay in the local working folder `youtube/basketball-captures/takes/`, with hashes in `CAPTURE.md` |
| Each film | `make_sheet.py` (author → Kokoro → finish), then `BUILD-PROMPT.md` |
| Checks | `./art godot-gdd --check` PASS (20 sections, 11 excerpts) · `godot-waikthrough --check` PASS (42 features) · `godot-gamedev --check` PASS (13 code→result pairs). GATE T PASS and Gate V clean on all six masters; frames reviewed by eye |
| Approvals | none claimed; every GDD section is PENDING |

## Watch and review

| Video | Drive link | Size | Duration | SHA-256 |
|---|---|---|---|---|
| GDD, landscape (`basketball-gdd_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 368.9 s | `9398a72f62af478572dec57a226c7dd0c2dbadfc2077798f78b06b3f5c84ca2e` |
| Walkthrough, landscape (`basketball-walkthrough_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 312.0 s | `19c33c5a30c7b2e24f0f866b6905e9b985aa11c49e20b63333d0aba97979517d` |
| Gamedev, landscape (`basketball-gamedev_yeshwanth_16x9.mp4`) | _add link_ | 3840×2160 | 423.9 s | `86d9ec76ea295ebaf381fb463fc0ea5d3b44b4d56d8bf54cbfde622a0436b687` |
| GDD, vertical (`basketball-gdd_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 368.9 s | `acbe0e2aa622c03807d7dd4f039faac4fc9662f9d88eba1d0f58f120341b4c17` |
| Walkthrough, vertical (`basketball-walkthrough_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 312.0 s | `098234d1c5a41a8a7fcdadb63f8b20a493e307713060fac2e1881270fa652d02` |
| Gamedev, vertical (`basketball-gamedev_yeshwanth_9x16.mp4`) | _add link_ | 2160×3840 | 423.9 s | `8395fc678a1cda7d4f409fdb31f351323e2cd73698617b3f091d8f46a742b861` |

**How the verticals were made.** They are native 9:16, not crops. Narration and timing are identical to landscape.

- **Gameplay:** re-cut in portrait from the same source frames, with the game at full width.
- **Boards and code panels:** redrawn as large-type portrait cards (`captures/portrait_cards.py`). Quotes are verified verbatim against the GDD, and code lines are exact source lines.
- **Composer, writer and outro:** the toolkit's 916 compositions.

| Review step | Status |
|---|---|
| PM review | pending |
| YouTube 4K processing check | pending upload |
| Professors' publication decision | pending |
