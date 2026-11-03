# BUILD-LOG — Basketball Blaster: The Design Document Came Last

**Built by Claude in Claude Code.** The game was not modified. No paid calls, no upload.

- **GDD first.** `GDD.md` v0.1 was written from the folder's evidence. Its capture claims were corrected to the recorded take before the film was built:
  - Egg times are 12.6 / 13.6 / 18.7 s. The dry runs had suggested "under 15 s".
  - The fight cost one life, not two.
- **Narration sync.** Four clips were re-timed by moving narration, never footage:
  - B04: the clip starts earlier and the narration was reordered.
  - B09: re-segmented; the replay is a labelled 1/4 speed of frames 1780–1803.
  - B11: a 3.5 s lead was added.
  - B16: the clip starts at frame 440.
- **GATE T.** Five boards that embedded game stills (B03, B05, B10, B15, B18) failed min-size and local contrast on text inside the game's own UI. Following the tower-defense precedent, they were switched to the cards layout; the real gameplay is in the adjacent clips. B13 keeps its still.
- **Gate V.** Gameplay beats declare `contrast_regions` for our disclosure strip. The dark game screens otherwise read as low-contrast ink against the strip.
- **Vertical.**
  - Boards and the verdict are native large-type portrait cards (`portrait_cards.py`), with quotes verified verbatim against `GDD.md`. B02 was trimmed to one card to fit the safe area.
  - The B01 writer text was shortened to 12 words or fewer and set at 150 px, for the portrait no-wordy-card and size floors. The narration is unchanged.
  - Portrait gameplay declares `full_bleed`, because the game spans the full 2160 px width.
- **Checks.** `./art godot-gdd --check` PASS (20 sections, 11 excerpts). GATE T PASS and Gate V clean, both aspects. Frames reviewed by eye.
- **Greeting (2026-10-19).** At the presenter's request, B00 now opens "Hola, this is Liam". Only B00 narration and its composer card changed; both aspects were re-rendered and re-checked.
