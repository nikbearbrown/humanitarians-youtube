# BUILD-LOG — Basketball Blaster: Inside the Godot Code

**Built by Claude in Claude Code.** The game was not modified. No paid calls, no upload.

- **Runtime probes.**
  - `tree_probe.gd` printed the live arena tree.
  - `bar_probe.gd` measured the HUD bars at 80×34 px against the 14 px the code asks for. That turned "taller than set" into a number. The cause is stated as likely, not proven.
- **Unused assets.** Found by grep: six images and the gixel font (preloaded, never read).
- **B28.** A labelled ZOOM 3.4× of real frames 1395–1479, with no retiming. It ends on a labelled held frame because the narration is longer than the window.
- **Remotion.** B29–B31 failed silently in the first batch, under machine load. They were re-rendered one at a time. The Remotion pass also rewrote the sheet and dropped the gameplay `contrast_regions`, which were re-applied before the final.
- **Vertical.** Code beats are portrait cards showing the exact source lines each landscape cue points at. The tree and verdict beats are also cards.
- **Checks.** `./art godot-gamedev --check` PASS (173 files, 9 build artefacts excluded, 13 code→result pairs). GATE T PASS and Gate V clean. Frames reviewed by eye.
- **Greeting (2026-10-19).** At the presenter's request, B00 now opens "Hola, this is Liam". Only B00 narration and its composer card changed; both aspects were re-rendered and re-checked.
